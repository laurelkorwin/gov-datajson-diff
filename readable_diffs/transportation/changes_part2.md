# Change History for transportation.json (Part 2)

### Changes from 31606f9 to dd2190f (Part 1/9)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
diff --git a/transportation.json b/transportation.json
index c263285..809c94e 100644
--- a/transportation.json
+++ b/transportation.json
@@ -3,26 +3,16 @@
     "@id": "https://data.transportation.gov/data.json",
     "@type": "dcat:Catalog",
     "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
-    "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json",
     "dataset": [
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/225h-8raq",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/225h-8raq",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "Cities",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30,70 +20,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/225h-8raq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/225h-8raq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/225h-8raq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/225h-8raq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/225h-8raq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/225h-8raq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/225h-8raq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/225h-8raq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/225h-8raq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/225h-8raq",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/225h-8raq",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Cities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/bridge/nbi/ascii.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
+            "analysisUnit": "Bridge structure",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/22t5-qr6u",
-            "issued": "1992-12-31",
-            "temporal": "R/1992-12-31/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "National Bridge Inventory Database System.",
-            "modified": "2024-05-08",
-            "references": [
-                "http://www.fhwa.dot.gov/bridge/mtguide.pdf"
-            ],
-            "keyword": [
-                "bridge",
-                "condition",
-                "deck",
-                "inspection",
-                "structure"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "693.6",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
             "description": "The NBI System is the collection of bridge inspection information and costs associated with bridge replacements of structurally deficient bridges on and off the NHS. This data is collected under the auspices of the National Bridge Inspection Standards (NBIS) as prescribed by law. The NBI System collects the information that is used to determine eligibility for NHS projects, performance measure reporting, NHS penalty determination, and reporting to Congress.  It supports oversight of the NBIS through various report tools, and provides data reporting that supports agency strategic goals.",
-            "title": "National Bridge Inventory System (NBI) - 1997",
-            "isPartOf": "DOT-693",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
-            "primaryITInvestmentUII": "021-012940226",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -102,54 +82,54 @@
                     "title": "1997"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
-            "dataQuality": true,
+            "identifier": "693.6",
+            "isPartOf": "DOT-693",
+            "issued": "1992-12-31",
+            "keyword": [
+                "bridge",
+                "condition",
+                "deck",
+                "inspection",
+                "structure"
+            ],
+            "landingPage": "https://data.transportation.gov/d/22t5-qr6u",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/bridge/nbi/ascii.cfm",
+            "modified": "2024-05-08",
+            "phone": "202-366-1575",
+            "primaryITInvestmentUII": "021-012940226",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "references": [
+                "http://www.fhwa.dot.gov/bridge/mtguide.pdf"
+            ],
+            "spatial": "Point",
+            "temporal": "R/1992-12-31/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Bridge structure",
-            "phone": "202-366-1575",
-            "language": [
-                "en-US"
-            ]
+            "title": "National Bridge Inventory System (NBI) - 1997"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2022-07-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "highway",
-                "highway performance monitoring",
-                "highway performance monitoring system",
-                "highways",
-                "hpms",
-                "sample"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/23ec-e7bt",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 1993",
-            "title": "Historic HPMS Data (Sample) - 1993",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -157,82 +137,120 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/23ec-e7bt/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/23ec-e7bt/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/23ec-e7bt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/23ec-e7bt/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/23ec-e7bt/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/23ec-e7bt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/23ec-e7bt/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/23ec-e7bt/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/23ec-e7bt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/23ec-e7bt",
+            "issued": "2022-07-08",
+            "keyword": [
+                "highway",
+                "highway performance monitoring",
+                "highway performance monitoring system",
+                "highways",
+                "hpms",
+                "sample"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-08",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
             "spatial": "United States",
-            "dataQuality": true,
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Historic HPMS Data (Sample) - 1993"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/23mg-e8r7",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Employment in transportation by industry and occupation",
+            "identifier": "https://data.transportation.gov/api/views/23mg-e8r7",
             "issued": "2020-04-22",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
             "keyword": [
                 "transportation employment",
                 "transportation occupations",
                 "transportation workforce"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/23mg-e8r7",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-18",
+            "phone": "202-366-DATA(3282)",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/23mg-e8r7",
-            "description": "Employment in transportation by industry and occupation",
-            "title": "Transportation Economic Trends: Transportation Employment - Industry and Occupation",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Transportation Economic Trends: Transportation Employment - Industry and Occupation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/23qp-cgz2",
-            "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": false,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
+            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "2011 Oregon HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/oregon2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Oregon"
+                }
+            ],
+            "identifier": "678.39",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -246,107 +264,69 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.39",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Oregon",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/23qp-cgz2",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5035",
             "primaryITInvestmentUII": "021-099281808",
             "programCode": [
                 "021:009"
             ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/oregon2011.zip",
-                    "description": "2011 Oregon HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Oregon"
-                }
-            ],
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "temporal": "R/1981-11-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
-            "categoryDesignation": "Administrative",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-5035"
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Oregon"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/23ys-sisy",
-            "issued": "2022-09-23",
             "@type": "dcat:Dataset",
-            "modified": "2022-09-27",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/23ys-sisy",
+            "issued": "2022-09-23",
+            "landingPage": "https://data.transportation.gov/d/23ys-sisy",
+            "modified": "2022-09-27",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
-            "title": "Vehicles and Drivers",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "Vehicles and Drivers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/bridge/nbi/ascii.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
+            "analysisUnit": "Bridge structure",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/249k-pctu",
-            "issued": "1992-12-31",
-            "temporal": "R/1992-12-31/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "National Bridge Inventory Database System.",
-            "modified": "2024-05-08",
-            "references": [
-                "http://www.fhwa.dot.gov/bridge/mtguide.pdf"
-            ],
-            "keyword": [
-                "bridge",
-                "condition",
-                "deck",
-                "inspection",
-                "structure"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "693.15",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
             "description": "The NBI System is the collection of bridge inspection information and costs associated with bridge replacements of structurally deficient bridges on and off the NHS. This data is collected under the auspices of the National Bridge Inspection Standards (NBIS) as prescribed by law. The NBI System collects the information that is used to determine eligibility for NHS projects, performance measure reporting, NHS penalty determination, and reporting to Congress.  It supports oversight of the NBIS through various report tools, and provides data reporting that supports agency strategic goals.",
-            "title": "National Bridge Inventory System (NBI) - 2006",
-            "isPartOf": "DOT-693",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
-            "primaryITInvestmentUII": "021-012940226",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -355,32 +335,63 @@
                     "title": "2006"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
-            "dataQuality": true,
+            "identifier": "693.15",
+            "isPartOf": "DOT-693",
+            "issued": "1992-12-31",
+            "keyword": [
+                "bridge",
+                "condition",
+                "deck",
+                "inspection",
+                "structure"
+            ],
+            "landingPage": "https://data.transportation.gov/d/249k-pctu",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/bridge/nbi/ascii.cfm",
+            "modified": "2024-05-08",
+            "phone": "202-366-1575",
+            "primaryITInvestmentUII": "021-012940226",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "references": [
+                "http://www.fhwa.dot.gov/bridge/mtguide.pdf"
+            ],
+            "spatial": "Point",
+            "temporal": "R/1992-12-31/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Bridge structure",
-            "phone": "202-366-1575",
-            "language": [
-                "en-US"
-            ]
+            "title": "National Bridge Inventory System (NBI) - 2006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/2577-gpny",
             "bureauCode": [
                 "021:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kate Hartman",
+                "hasEmail": "mailto:kate.hartman@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "As part of the Federal Highway Administration\u2019s (FHWA) Next Generation Simulation (NGSIM) project, video data was collected on a segment of Interstate 80 located in Emeryville, California on April 13, 2005. A total of 45 minutes of video data are available, segmented into three 15 minute periods: 1) 4:00 p.m. to 4:15 p.m.; 2) 5:00 p.m. to 5:15 p.m.; and 3) 5:15 p.m. to 5:30 p.m. The dataset includes files for both raw and processed video data from each of the seven cameras for the three time periods available for download. Camera numbering is in order of southern-most (1) to northern-most (7). The raw videos give the original vehicle movement data and offer users a view of how the section was observed. The processed video files provide videos of the vehicles along with a superimposition of the vehicle identification numbers. These videos can be used alone or can be used for cross referencing of the textual vehicle trajectory data provided in the NGSIM trajectory data with the corresponding video.\n\nFor related datasets please see the following:\n- NGSIM Vehicle Trajectories and Supporting Data: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Vehicle-Trajector/8ect-6jqj\n- NGSIM US-101 Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-US-101-Vi/4qzi-thur\n- NGSIM Lankershim Boulevard Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-Lankershi/uv3e-y54k\n- NGSIM Peachtree Street Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-Peachtree/mupt-aksf",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/download/2577-gpny/application/pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/2577-gpny",
             "issued": "2016-01-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2005-04-13",
-            "modified": "2016-01-01",
             "keyword": [
                 "california",
                 "emeryville",
@@ -392,62 +403,38 @@
                 "san francisco bay area",
                 "video"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/2577-gpny",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://creativecommons.org/licenses/by-sa/4.0/legalcode",
+            "modified": "2016-01-01",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Department of Transportation"
             },
-            "identifier": "https://data.transportation.gov/api/views/2577-gpny",
-            "description": "As part of the Federal Highway Administration\u2019s (FHWA) Next Generation Simulation (NGSIM) project, video data was collected on a segment of Interstate 80 located in Emeryville, California on April 13, 2005. A total of 45 minutes of video data are available, segmented into three 15 minute periods: 1) 4:00 p.m. to 4:15 p.m.; 2) 5:00 p.m. to 5:15 p.m.; and 3) 5:15 p.m. to 5:30 p.m. The dataset includes files for both raw and processed video data from each of the seven cameras for the three time periods available for download. Camera numbering is in order of southern-most (1) to northern-most (7). The raw videos give the original vehicle movement data and offer users a view of how the section was observed. The processed video files provide videos of the vehicles along with a superimposition of the vehicle identification numbers. These videos can be used alone or can be used for cross referencing of the textual vehicle trajectory data provided in the NGSIM trajectory data with the corresponding video.\n\nFor related datasets please see the following:\n- NGSIM Vehicle Trajectories and Supporting Data: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Vehicle-Trajector/8ect-6jqj\n- NGSIM US-101 Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-US-101-Vi/4qzi-thur\n- NGSIM Lankershim Boulevard Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-Lankershi/uv3e-y54k\n- NGSIM Peachtree Street Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-Peachtree/mupt-aksf",
-            "title": "Next Generation Simulation (NGSIM) Program I-80 Videos",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/download/2577-gpny/application/pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
             "spatial": "Emeryville, California",
-            "dataQuality": true,
-            "license": "http://creativecommons.org/licenses/by-sa/4.0/legalcode",
+            "temporal": "2005-04-13",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Next Generation Simulation (NGSIM) Program I-80 Videos"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/25e5-bvnb",
-            "issued": "2021-03-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-02-12",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Chambers",
                 "hasEmail": "mailto:matthew.chambers@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/25e5-bvnb",
             "description": "",
-            "title": "Air Drafts by Limiting Bridge for Select Container Ports",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -455,39 +442,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/25e5-bvnb/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/25e5-bvnb/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/25e5-bvnb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/25e5-bvnb/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/25e5-bvnb/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/25e5-bvnb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/25e5-bvnb/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/25e5-bvnb/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/25e5-bvnb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "https://data.transportation.gov/api/views/25e5-bvnb",
+            "issued": "2021-03-18",
+            "landingPage": "https://data.transportation.gov/d/25e5-bvnb",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-02-12",
+            "programCode": [
+                "021:042"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Air Drafts by Limiting Bridge for Select Container Ports"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/25r8-p3cy",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "021:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kate Hartman",
+                "hasEmail": "mailto:kate.hartman@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The ATDM Trajectory Validation project developed a validation framework and a trajectory computational engine to compare and validate simulated and observed vehicle trajectories and dynamics. The field data were used to demonstrate how on-site instrumented vehicle data can be used to validate simulated vehicle dynamics using the validation framework. \n\nThe vehicle trajectory data were collected in a separate task of the Active Transportation Demand Management (ATDM) Trajectory Level Validation project. The primary project objective was to develop a methodology to validate simulated vehicle dynamics at the trajectory level. Microscopic and macroscopic performance measures were calculated from the trajectory data and used in a number of validation tests related to safety, vehicle limits, driver comfort levels, and traffic flow",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/download/25r8-p3cy/application/msword",
+                    "mediaType": "application/msword"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/25r8-p3cy",
             "issued": "2017-12-31",
-            "@type": "dcat:Dataset",
-            "temporal": "2016-04-11/2016-05-16",
-            "modified": "2017-12-31",
             "keyword": [
                 "active transportation demand management (atdm)",
                 "arterial",
@@ -509,79 +521,46 @@
                 "trajectories",
                 "vehicle data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/25r8-p3cy",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
+            "modified": "2017-12-31",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Department of Transportation"
             },
-            "identifier": "https://data.transportation.gov/api/views/25r8-p3cy",
-            "description": "The ATDM Trajectory Validation project developed a validation framework and a trajectory computational engine to compare and validate simulated and observed vehicle trajectories and dynamics. The field data were used to demonstrate how on-site instrumented vehicle data can be used to validate simulated vehicle dynamics using the validation framework. \n\nThe vehicle trajectory data were collected in a separate task of the Active Transportation Demand Management (ATDM) Trajectory Level Validation project. The primary project objective was to develop a methodology to validate simulated vehicle dynamics at the trajectory level. Microscopic and macroscopic performance measures were calculated from the trajectory data and used in a number of validation tests related to safety, vehicle limits, driver comfort levels, and traffic flow",
-            "title": "Active Transportation Demand Management (ATDM) Trajectory Level Validation",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/download/25r8-p3cy/application/msword",
-                    "mediaType": "application/msword"
-                }
-            ],
             "spatial": "San Francisco, California",
-            "dataQuality": true,
-            "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "irregular",
+            "temporal": "2016-04-11/2016-05-16",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Active Transportation Demand Management (ATDM) Trajectory Level Validation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Protected under the Privacy Act of 1974; see System of Records Notice for more information.",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.civilrights.dot.gov/node/3828",
+            "agencyProgramURL": "http://www.civilrights.dot.gov",
+            "analysisUnit": "complaint",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/26cx-qsdq",
-            "issued": "2014-11-03",
-            "temporal": "R/2010-01-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "references": [
-                "https://www.civilrights.dot.gov/node/3828"
-            ],
-            "keyword": [
-                "discrminiation",
-                "employment",
-                "equal",
-                "no fear act",
-                "opportunity",
-                "whistleblower"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "557.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
-            "description": "Data related to the management of EEO complaint processing.  Due to the presence of PII, the raw data is not available for public consumption.  However, aggregated data is available in the DOT's NoFEAR Act report and Form 462 Report.  Both are located on the DOT Office of Civil Rights' public website.",
-            "title": "EEO Complaint Processing Data - 2010 No FEAR Act Report",
-            "isPartOf": "DOT-557",
-            "agencyProgramURL": "http://www.civilrights.dot.gov",
-            "programCode": [
-                "021:058"
-            ],
+            "dataQuality": false,
+            "describedBy": "https://www.civilrights.dot.gov/node/3828",
+            "description": "Data related to the management of EEO complaint processing.  Due to the presence of PII, the raw data is not available for public consumption.  However, aggregated data is available in the DOT's NoFEAR Act report and Form 462 Report.  Both are located on the DOT Office of Civil Rights' public website.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -590,58 +569,62 @@
                     "title": "2010 No FEAR Act Report"
                 }
             ],
-            "describedBy": "https://www.civilrights.dot.gov/node/3828",
-            "dataQuality": false,
+            "identifier": "557.1",
+            "isPartOf": "DOT-557",
+            "issued": "2014-11-03",
+            "keyword": [
+                "discrminiation",
+                "employment",
+                "equal",
+                "no fear act",
+                "opportunity",
+                "whistleblower"
+            ],
+            "landingPage": "https://data.transportation.gov/d/26cx-qsdq",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "https://www.civilrights.dot.gov/node/3828",
+            "modified": "2024-11-14",
+            "phone": "202-366-8741",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "references": [
+                "https://www.civilrights.dot.gov/node/3828"
+            ],
+            "rights": "Protected under the Privacy Act of 1974; see System of Records Notice for more information.",
+            "temporal": "R/2010-01-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "complaint",
-            "phone": "202-366-8741",
-            "language": [
-                "en-US"
-            ]
+            "title": "EEO Complaint Processing Data - 2010 No FEAR Act Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.dot.gov/individuals/foia/dot-annual-foia-reports-congress",
+            "agencyProgramURL": "http://www.dot.gov/foia",
+            "analysisUnit": "FOIA Request",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/26pp-ei3z",
-            "issued": "2013-02-01",
-            "temporal": "R/2012-01-01/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "modified": "2024-11-14",
-            "references": [
-                "http://www.justice.gov/oip/docs/doj-handbook-for-agency-annual-freedom-of-information-act-reports.pdf"
-            ],
-            "keyword": [
-                "backlog",
-                "freedom of information act",
-                "requests"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "372.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
-            "description": "The FOIA requires each federal agency to submit an Annual Report to the Attorney General each year. These reports contain detailed statistics on the numbers of requests received and processed by each agency, the time taken to respond, and the outcome of each request, as well as many other vital statistics regarding the administration of the FOIA at federal departments and agencies.",
-            "title": "Freedom of Information Act Annual Report - 2012 Report",
-            "isPartOf": "DOT-372",
-            "agencyProgramURL": "http://www.dot.gov/foia",
+            "dataQuality": true,
+            "describedBy": "http://www.justice.gov/oip/docs/doj-handbook-for-agency-annual-freedom-of-information-act-reports.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "021:058"
-            ],
+            "description": "The FOIA requires each federal agency to submit an Annual Report to the Attorney General each year. These reports contain detailed statistics on the numbers of requests received and processed by each agency, the time taken to respond, and the outcome of each request, as well as many other vital statistics regarding the administration of the FOIA at federal departments and agencies.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -650,36 +633,68 @@
                     "title": "2012 Report"
                 }
             ],
-            "spatial": "not applicable",
-            "describedBy": "http://www.justice.gov/oip/docs/doj-handbook-for-agency-annual-freedom-of-information-act-reports.pdf",
-            "dataQuality": true,
+            "identifier": "372.1",
+            "isPartOf": "DOT-372",
+            "issued": "2013-02-01",
+            "keyword": [
+                "backlog",
+                "freedom of information act",
+                "requests"
+            ],
+            "landingPage": "https://data.transportation.gov/d/26pp-ei3z",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.dot.gov/individuals/foia/dot-annual-foia-reports-congress",
+            "modified": "2024-11-14",
+            "phone": "202-366-5546",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "references": [
+                "http://www.justice.gov/oip/docs/doj-handbook-for-agency-annual-freedom-of-information-act-reports.pdf"
+            ],
+            "spatial": "not applicable",
+            "temporal": "R/2012-01-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "analysisUnit": "FOIA Request",
-            "phone": "202-366-5546",
-            "language": [
-                "en-US"
-            ]
+            "title": "Freedom of Information Act Annual Report - 2012 Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www-nrd.nhtsa.dot.gov/Pubs/812038.pdf",
+            "agencyProgramURL": "http://www-nrd.nhtsa.dot.gov/Pubs/812038.pdf",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/27e2-avkg",
-            "issued": "2014-06-30",
-            "temporal": "2005-01-01/2009-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www-nrd.nhtsa.dot.gov/Pubs/812038.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": false,
+            "description": "Fuel System Integrity-Rear, FMVSS 301R. Results from crash tests were conducted in 2012 on 16 older vehicles, in order to find out if the older vehicles could pass tests currently used to determine if new vehicles were compliance with FMVSS 301R.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "NOTE: Request test numbers 8667 through 8682.",
+                    "downloadURL": "http://www-nrd.nhtsa.dot.gov/database/VSR/veh/QueryTest.aspx",
+                    "mediaType": "text/html",
+                    "title": "Vehicle Database Test Parameters Query Results"
+                }
             ],
+            "identifier": "1837.2",
+            "isPartOf": "DOT-1837",
+            "issued": "2014-06-30",
             "keyword": [
                 "benefit",
                 "effectiveness",
@@ -688,57 +703,56 @@
                 "fuel system integrity",
                 "post-crash fires"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "1837.2",
+            "landingPage": "https://data.transportation.gov/d/27e2-avkg",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-4696",
+            "programCode": [
+                "021:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Highway Traffic Safety Administration"
             },
-            "description": "Fuel System Integrity-Rear, FMVSS 301R. Results from crash tests were conducted in 2012 on 16 older vehicles, in order to find out if the older vehicles could pass tests currently used to determine if new vehicles were compliance with FMVSS 301R.",
-            "title": "Fuel System Integrity-Rear, FMVSS 301R - Vehicle Database Test Parameters Query Results",
-            "isPartOf": "DOT-1837",
-            "agencyProgramURL": "http://www-nrd.nhtsa.dot.gov/Pubs/812038.pdf",
-            "programCode": [
-                "021:031"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www-nrd.nhtsa.dot.gov/database/VSR/veh/QueryTest.aspx",
-                    "description": "NOTE: Request test numbers 8667 through 8682.",
-                    "@type": "dcat:Distribution",
-                    "title": "Vehicle Database Test Parameters Query Results"
-                }
+            "references": [
+                "http://www-nrd.nhtsa.dot.gov/Pubs/812038.pdf"
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www-nrd.nhtsa.dot.gov/Pubs/812038.pdf",
+            "temporal": "2005-01-01/2009-12-31",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4696",
-            "language": [
-                "en-US"
-            ]
+            "title": "Fuel System Integrity-Rear, FMVSS 301R - Vehicle Database Test Parameters Query Results"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Data set contains controlled unclassified information (Draft rules and polices). Some public reports are available.",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/27g2-gf8g",
-            "issued": "2018-12-18",
-            "temporal": "R/2013-01-01/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "modified": "2024-11-14",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DOT Socrata",
+                "hasEmail": "mailto:Socrata@dot.gov"
+            },
+            "dataQuality": false,
+            "description": "RMS is a DOT-wide system developed for the Office of the General Counsel (OGC) to track the status of rulemakings, document required concurrences, serve as a repository for documents under development, and generate management and compliance reports from the data within the system.  The system allows senior leaders throughout DOT to identify not only the status of rulemakings, but areas where steps can be taken to streamline rulemaking operations at DOT.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.dot.gov/regulations/significant-rulemaking-report-archive",
+                    "mediaType": "text/html",
+                    "title": "Public Reports on Significant Rulemaking"
+                }
+            ],
+            "identifier": "458.4",
+            "isPartOf": "DOT-458",
+            "issued": "2018-12-18",
             "keyword": [
                 "economically significant",
                 "effects",
@@ -761,57 +775,59 @@
                 "tribalism",
                 "unfunded mandate"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DOT Socrata",
-                "hasEmail": "mailto:Socrata@dot.gov"
-            },
-            "identifier": "458.4",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
-            "description": "RMS is a DOT-wide system developed for the Office of the General Counsel (OGC) to track the status of rulemakings, document required concurrences, serve as a repository for documents under development, and generate management and compliance reports from the data within the system.  The system allows senior leaders throughout DOT to identify not only the status of rulemakings, but areas where steps can be taken to streamline rulemaking operations at DOT.",
-            "title": "Rulemaking Management System (RMS) - Public Reports on Significant Rulemaking",
-            "isPartOf": "DOT-458",
+            "landingPage": "https://data.transportation.gov/d/27g2-gf8g",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-14",
+            "phone": "202-366-6322",
             "primaryITInvestmentUII": "021-110391689",
             "programCode": [
                 "021:058"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.dot.gov/regulations/significant-rulemaking-report-archive",
-                    "mediaType": "text/html",
-                    "title": "Public Reports on Significant Rulemaking"
-                }
-            ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "rights": "Data set contains controlled unclassified information (Draft rules and polices). Some public reports are available.",
+            "temporal": "R/2013-01-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-6322"
+            "title": "Rulemaking Management System (RMS) - Public Reports on Significant Rulemaking"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "https://www.phmsa.dot.gov/data-and-statistics/pipeline/distribution-transmission-gathering-lng-and-liquid-accident-and-incident-data",
+            "agencyProgramURL": "http://www.phmsa.dot.gov/pipeline",
+            "analysisUnit": "Accident/Incident Report information from pipeline operators",
             "bureauCode": [
                 "021:50"
             ],
-            "landingPage": "https://data.transportation.gov/d/27nc-rsge",
-            "issued": "2006-10-20",
-            "temporal": "R/1970-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-24",
+            "categoryDesignation": "Administrative - Regulatory",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.phmsa.dot.gov/pipeline"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Muhammed Jamil",
+                "hasEmail": "mailto:PHMSAPHPDataandStatistics@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Title 49 of the Code of Federal Regulations (49 CFR Parts 191, 195) requires pipeline operators to submit incident reports within 30 days of a pipeline incident or accident. The CFR defines accidents and incidents, as well as criteria for submitting reports to the Office of Pipeline Safety. Specific information includes the time and location of the incident(s), number of any injuries and/ or fatalities, commodity spilled/gas released, causes of failure and evacuation procedures. The reports are used for identifying long- and short-term trends at the national, state and operator-specific levels.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Gas Distribution System Incident Reports from 03.2004 to 12.2009 data submitted to PHMSA by pipeline operators",
+                    "downloadURL": "http://phmsa.dot.gov/staticfiles/PHMSA/DownloadableFiles/Files/Pipeline/data/incident_gas_distribution_mar2004_dec2009.zip",
+                    "mediaType": "text/tab",
+                    "title": "Natural Gas Distribution Incident Data - March 2004 to December 2009 (ZIP)"
+                }
             ],
+            "identifier": "34.2",
+            "isPartOf": "DOT-34",
+            "issued": "2006-10-20",
             "keyword": [
                 "accident",
                 "distribution",
@@ -824,84 +840,44 @@
                 "safety",
                 "transmission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Muhammed Jamil",
-                "hasEmail": "mailto:PHMSAPHPDataandStatistics@dot.gov"
-            },
-            "identifier": "34.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Pipeline and Hazardous Materials Safety Administration"
-            },
-            "description": "Title 49 of the Code of Federal Regulations (49 CFR Parts 191, 195) requires pipeline operators to submit incident reports within 30 days of a pipeline incident or accident. The CFR defines accidents and incidents, as well as criteria for submitting reports to the Office of Pipeline Safety. Specific information includes the time and location of the incident(s), number of any injuries and/ or fatalities, commodity spilled/gas released, causes of failure and evacuation procedures. The reports are used for identifying long- and short-term trends at the national, state and operator-specific levels.",
-            "title": "Gas Distribution, Gas Transmission & Gathering, LNG incidents and Hazardous Liquid Accident Data",
-            "isPartOf": "DOT-34",
-            "agencyProgramURL": "http://www.phmsa.dot.gov/pipeline",
+            "landingPage": "https://data.transportation.gov/d/27nc-rsge",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-07-24",
+            "phone": "202-366-1878",
             "primaryITInvestmentUII": "021-339943484",
             "programCode": [
                 "021:044"
             ],
-            "distribution": [
-                {
-                    "mediaType": "text/tab",
-                    "downloadURL": "http://phmsa.dot.gov/staticfiles/PHMSA/DownloadableFiles/Files/Pipeline/data/incident_gas_distribution_mar2004_dec2009.zip",
-                    "description": "Gas Distribution System Incident Reports from 03.2004 to 12.2009 data submitted to PHMSA by pipeline operators",
-                    "@type": "dcat:Distribution",
-                    "title": "Natural Gas Distribution Incident Data - March 2004 to December 2009 (ZIP)"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Pipeline and Hazardous Materials Safety Administration"
+            },
+            "references": [
+                "http://www.phmsa.dot.gov/pipeline"
             ],
             "spatial": "operator-specific",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "https://www.phmsa.dot.gov/data-and-statistics/pipeline/distribution-transmission-gathering-lng-and-liquid-accident-and-incident-data",
+            "temporal": "R/1970-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative - Regulatory",
-            "analysisUnit": "Accident/Incident Report information from pipeline operators",
-            "phone": "202-366-1878",
-            "language": [
-                "en-US"
-            ]
+            "title": "Gas Distribution, Gas Transmission & Gathering, LNG incidents and Hazardous Liquid Accident Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/285w-yjf5",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2020-07-22",
-            "@type": "dcat:Dataset",
-            "temporal": "2013-06-17/2013-08-30",
-            "modified": "2020-07-22",
-            "keyword": [
-                "car-following",
-                "freeway",
-                "instrumented research vehicle (irv)",
-                "living laboratory (ll)",
-                "mclean virginia",
-                "microscopic modeling",
-                "microsimulation",
-                "traffic simulation",
-                "work zone"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:Volpe_Dataset_POCs@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "US Department of Transportation"
-            },
-            "identifier": "https://data.transportation.gov/api/views/285w-yjf5",
+            "dataQuality": true,
             "description": "The data describe freeway car-following behavior (such as velocity, acceleration, and relative position) for the car-following instances observed during 59 data collection runs, performed through the Federal Highway Administration (FHWA) Turner Fairbank Highway Research Center\u2019s (TFHRC) Living Laboratory (LL). Data were collected using an Instrumented Research Vehicle (IRV) along freeways in northern Virginia to better understand work zone driver behaviors. The USDOT Volpe National Transportation Systems Center (Volpe Center) identified, isolated, and classified individual car following instances from within the raw datasets (classification parameters included roadway type, level of congestion, and speed limit), then processed, refined, and cleaned the dataset. \n\nThis table contains metadata about each data collection run. See also the instances table (https://datahub.transportation.gov/Automobiles/Enhancing-Microsimulation-Models-for-Improved-Work/k74u-yqu6) and radar table (https://datahub.transportation.gov/Automobiles/Enhancing-Microsimulation-Models-for-Improved-Work/uvrt-varj).",
-            "title": "Enhancing Microsimulation Models for Improved Work Zone Planning: Car-Following Data from Northern Virginia (Runs)",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -909,155 +885,163 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/285w-yjf5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/285w-yjf5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/285w-yjf5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/285w-yjf5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/285w-yjf5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/285w-yjf5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/285w-yjf5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/285w-yjf5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/285w-yjf5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "-77.0573,38.7046,-77.2278,38.9563",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/285w-yjf5",
+            "issued": "2020-07-22",
+            "keyword": [
+                "car-following",
+                "freeway",
+                "instrumented research vehicle (irv)",
+                "living laboratory (ll)",
+                "mclean virginia",
+                "microscopic modeling",
+                "microsimulation",
+                "traffic simulation",
+                "work zone"
+            ],
+            "landingPage": "https://data.transportation.gov/d/285w-yjf5",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2020-07-22",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
+            "spatial": "-77.0573,38.7046,-77.2278,38.9563",
+            "temporal": "2013-06-17/2013-08-30",
             "theme": [
                 "Automobiles"
-            ]
+            ],
+            "title": "Enhancing Microsimulation Models for Improved Work Zone Planning: Car-Following Data from Northern Virginia (Runs)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/28tb-cpjy",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Transportation Economic Trends table of contents",
+            "identifier": "https://data.transportation.gov/api/views/28tb-cpjy",
             "issued": "2019-12-09",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-21",
             "keyword": [
                 "statistics",
                 "transportation",
                 "transportation economics"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/28tb-cpjy",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-08-21",
+            "phone": "202-366-DATA(3282)",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/28tb-cpjy",
-            "description": "Transportation Economic Trends table of contents",
-            "title": "Transportation Economic Trends Table of Contents",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Transportation Economic Trends Table of Contents"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.bts.gov/stories/s/28xr-p3t9",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2020-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
-            "keyword": [
-                "transportation unemployment",
-                "unemployment"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/28xr-p3t9",
             "description": "This page shows total unemployment rates in the U.S., transportation and warehousing sector, transportation and material moving occupations, and men and women.",
-            "title": "Unemployment Rates - U.S. Transportation Sector or Occupations, Men and  Women",
+            "identifier": "https://data.transportation.gov/api/views/28xr-p3t9",
+            "issued": "2020-09-10",
+            "keyword": [
+                "transportation unemployment",
+                "unemployment"
+            ],
+            "landingPage": "https://data.bts.gov/stories/s/28xr-p3t9",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-18",
+            "phone": "202-366-DATA(3282)",
             "programCode": [
                 "021:053"
             ],
-            "license": "https://www.usa.gov/government-works",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Unemployment Rates - U.S. Transportation Sector or Occupations, Men and  Women"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/28ys-vdwp",
-            "issued": "2021-05-17",
             "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sean Jahanmir",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/28ys-vdwp",
+            "issued": "2021-05-17",
+            "landingPage": "https://data.transportation.gov/d/28ys-vdwp",
+            "modified": "2024-05-01",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Environment"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Contains details about carrier safety status and corrective action plans.",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.fmcsa.dot.gov/foia",
+            "agencyProgramURL": "http://www.fmcsa.dot.gov/foia",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/29dg-xxfp",
-            "issued": "2015-01-21",
-            "temporal": "R/2015-01-21/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "audit",
-                "carrier",
-                "safety"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO",
                 "hasEmail": "mailto:fmcsa.cdo@dot.gov"
             },
-            "identifier": "274.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": true,
             "description": "Contains data on new entrant safety audits performed by FMCSA and State grantees.",
-            "title": "Motor Carrier Safety Audits -",
-            "agencyProgramURL": "http://www.fmcsa.dot.gov/foia",
-            "programCode": [
-                "021:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1065,61 +1049,53 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "State, Carrier,",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fmcsa.dot.gov/foia",
-            "theme": [
-                "Transportation"
+            "identifier": "274.0",
+            "issued": "2015-01-21",
+            "keyword": [
+                "audit",
+                "carrier",
+                "safety"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "phone": "202-493-0215",
+            "landingPage": "https://data.transportation.gov/d/29dg-xxfp",
             "language": [
                 "en-US"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "bureauCode": [
-                "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/29pj-75z5",
-            "issued": "2013-10-31",
-            "temporal": "2012-07-12/2012-11-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
-            "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.nhtsa.gov/nti/811841"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-24",
+            "phone": "202-493-0215",
+            "programCode": [
+                "021:020"
             ],
-            "keyword": [
-                "activity",
-                "attitude",
-                "behavior",
-                "bicyclist",
-                "bike lane",
-                "bike path",
-                "electronic devices",
-                "knowledge",
-                "pedestrian"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "rights": "Contains details about carrier safety status and corrective action plans.",
+            "spatial": "State, Carrier,",
+            "temporal": "R/2015-01-21/P1Y",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Motor Carrier Safety Audits -"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.nhtsa.gov/nti/811841",
+            "agencyProgramURL": "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/National+Telephone+Surveys",
+            "bureauCode": [
+                "021:18"
             ],
+            "categoryDesignation": "Research",
+            "collectionInstrument": "Transportation",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "DOT-415",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
             "description": "Information from the public to ascertain the current frequency and characteristics of bicyclist and pedestrian activity, and identify deterrents to bicycling and walking. The data will also be compared to data collected by a previous NHTSA survey, conducted in 2002, to determine if major changes have occurred over that 10-year span. The information will be used to help update and refine safety programs. A national telephone survey will be administered to 9,000 randomly selected respondents 16 and older drawn from all 50 States and the District of Columbia. The survey will ask about the characteristics of bicycling and walking trips, conspicuity, community design for bicycling and walking, bicycle helmet use, and general opinions about bicycling and walking. Interview length will average 20 minutes.",
-            "title": "National Survey of Pedestrian and Bicyclist Attitudes, Knowledge, and Behaviors",
-            "agencyProgramURL": "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/National+Telephone+Surveys",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1128,33 +1104,72 @@
                     "title": "2012 Survey"
                 }
             ],
-            "dataQuality": false,
+            "identifier": "DOT-415",
+            "issued": "2013-10-31",
+            "keyword": [
+                "activity",
+                "attitude",
+                "behavior",
+                "bicyclist",
+                "bike lane",
+                "bike path",
+                "electronic devices",
+                "knowledge",
+                "pedestrian"
+            ],
+            "landingPage": "https://data.transportation.gov/d/29pj-75z5",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-6401",
+            "programCode": [
+                "021:032"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "http://www.nhtsa.gov/nti/811841"
+            ],
+            "temporal": "2012-07-12/2012-11-18",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "agencyDataSeriesURL": "http://www.nhtsa.gov/nti/811841",
-            "categoryDesignation": "Research",
-            "phone": "202-366-6401",
-            "language": [
-                "en-US"
-            ]
+            "title": "National Survey of Pedestrian and Bicyclist Attitudes, Knowledge, and Behaviors"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/2aqt-qens",
-            "issued": "1970-01-01",
-            "temporal": "R/1970-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "State Traffic Monitoring Systems (TMS)",
-            "references": [
-                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/10juntvt/10juntvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "June 2010"
+                }
             ],
+            "identifier": "18.21",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -1164,55 +1179,44 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.21",
+            "landingPage": "https://data.transportation.gov/d/2aqt-qens",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-1067",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - June 2010",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/10juntvt/10juntvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "June 2010"
-                }
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
             ],
             "spatial": "Vehicles by type of functional classified roadway",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "temporal": "R/1970-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
-            "phone": "202-366-1067",
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Traffic Volume Trends - June 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/2cyr-4k8j",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Congress has passed three appropriations bills since the start of the COVID-19 pandemic to provide stimulus relief and emergency funding to the economy, including the transportation industry",
+            "identifier": "https://data.transportation.gov/api/views/2cyr-4k8j",
             "issued": "2021-04-19",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
             "keyword": [
                 "airports",
                 "arp",
@@ -1226,63 +1230,41 @@
                 "emergency funding",
                 "stimulus"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/2cyr-4k8j",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-18",
+            "phone": "202-366-DATA(3282)",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/2cyr-4k8j",
-            "description": "Congress has passed three appropriations bills since the start of the COVID-19 pandemic to provide stimulus relief and emergency funding to the economy, including the transportation industry",
-            "title": "COVID-19 Stimulus Funding for Transportation in the CARES Act and other Supplemental Bills",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "COVID-19 Stimulus Funding for Transportation in the CARES Act and other Supplemental Bills"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://www.nhtsa.gov",
+            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
+            "analysisUnit": "Test",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/2d3m-by69",
-            "issued": "1998-12-24",
-            "temporal": "R/1998-12-14/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.nhtsa.gov/Research/Databases+and+Software/NHTSA+Test+Reference+Guides"
-            ],
-            "keyword": [
-                "nhtsa crash test database",
-                "nhtsa vehicle crash test database"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "364.29",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2011",
-            "isPartOf": "DOT-364",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
-            "primaryITInvestmentUII": "021-621341357",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1291,35 +1273,68 @@
                     "title": "Event Data Records Reports - 2011"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.29",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/2d3m-by69",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.nhtsa.gov",
+            "modified": "2024-05-01",
+            "phone": "202-366-4712",
+            "primaryITInvestmentUII": "021-621341357",
+            "programCode": [
+                "021:035"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "http://www.nhtsa.gov/Research/Databases+and+Software/NHTSA+Test+Reference+Guides"
+            ],
+            "spatial": "N/A",
+            "temporal": "R/1998-12-14/P1D",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Test",
-            "phone": "202-366-4712",
-            "language": [
-                "en-US"
-            ]
+            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/2dkr-h55a",
-            "issued": "1970-01-01",
-            "temporal": "R/1970-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "State Traffic Monitoring Systems (TMS)",
-            "references": [
-                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/02septvt/tvtsep02.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "September 2002"
+                }
             ],
+            "identifier": "18.144",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -1329,58 +1344,55 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.144",
+            "landingPage": "https://data.transportation.gov/d/2dkr-h55a",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-1067",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - September 2002",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/02septvt/tvtsep02.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "September 2002"
-                }
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
             ],
             "spatial": "Vehicles by type of functional classified roadway",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "temporal": "R/1970-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
-            "phone": "202-366-1067",
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Traffic Volume Trends - September 2002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "This data set may contain security-sensitive information and Personally Identifiable Information (PII) protected under the Privacy Act of 1974",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/2e9v-m7te",
-            "issued": "2015-01-26",
-            "temporal": "R/2015-01-26/PT1S",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Other",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DOT Socrata",
+                "hasEmail": "mailto:Socrata@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This data set contains username, proper name, office location, telephone number, organizational and various account details such as group membership and profile information for DOT employees, contractors, and guests that have access to the USDOT network. The data set does not include users that are part of the FAA, OIG, or STB.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.transportation.gov/mission/data-inventory-not-available",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "1653.0",
+            "issued": "2015-01-26",
             "keyword": [
                 "account",
                 "account options",
@@ -1399,67 +1411,40 @@
                 "profile",
                 "telephone number"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DOT Socrata",
-                "hasEmail": "mailto:Socrata@dot.gov"
-            },
-            "identifier": "1653.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
-            "description": "This data set contains username, proper name, office location, telephone number, organizational and various account details such as group membership and profile information for DOT employees, contractors, and guests that have access to the USDOT network. The data set does not include users that are part of the FAA, OIG, or STB.",
-            "title": "Active Directory -",
+            "landingPage": "https://data.transportation.gov/d/2e9v-m7te",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-14",
+            "phone": "202-366-6998",
             "primaryITInvestmentUII": "021-542850483",
             "programCode": [
                 "021:058"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.transportation.gov/mission/data-inventory-not-available",
-                    "mediaType": "text/html"
-                }
-            ],
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "rights": "This data set may contain security-sensitive information and Personally Identifiable Information (PII) protected under the Privacy Act of 1974",
+            "temporal": "R/2015-01-26/PT1S",
             "theme": [
                 "Other"
             ],
-            "accrualPeriodicity": "R/PT1S",
-            "categoryDesignation": "Administrative",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-6998"
+            "title": "Active Directory -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/2emp-mxtb",
             "bureauCode": [
                 "021:17"
             ],
-            "issued": "2024-02-02",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
-            "keyword": [
-                "boc3",
-                "motor carrier",
-                "process agent"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO Office",
                 "hasEmail": "mailto:FMCSA.CDO@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/2emp-mxtb",
             "description": "*Dataset*  Records for each BOC3 agent hired by a carrier/broker/freight forwarder. Each entity must hire a BOC3 agent to represent them in legal matters to obtain operating authority. In some cases, entities may act as their own BOC3 agent. The records in the dataset contain the BOC3 agent\u2019s name and address. The dataset also contains the DOT number and docket number of the represented entity. See dataset attachment \"FMCSA Dataset Description and Data Definitions - Select Datasets\" for more information.",
-            "title": "BOC3 - All With History",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1467,49 +1452,79 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2emp-mxtb/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2emp-mxtb/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2emp-mxtb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/2emp-mxtb/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2emp-mxtb/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2emp-mxtb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2emp-mxtb/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2emp-mxtb/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2emp-mxtb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/2emp-mxtb",
+            "issued": "2024-02-02",
+            "keyword": [
+                "boc3",
+                "motor carrier",
+                "process agent"
+            ],
+            "landingPage": "https://data.transportation.gov/d/2emp-mxtb",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2025-02-01",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
             "theme": [
                 "Trucking and Motorcoaches"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOC3 - All With History"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/2evq-c66r",
-            "issued": "1970-01-01",
-            "temporal": "R/1970-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "State Traffic Monitoring Systems (TMS)",
-            "references": [
-                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/11aprtvt/11aprtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "April 2011"
+                }
             ],
+            "identifier": "18.11",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -1519,104 +1534,63 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.11",
+            "landingPage": "https://data.transportation.gov/d/2evq-c66r",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-1067",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - April 2011",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/11aprtvt/11aprtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "April 2011"
-                }
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
             ],
             "spatial": "Vehicles by type of functional classified roadway",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "temporal": "R/1970-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
-            "phone": "202-366-1067",
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Traffic Volume Trends - April 2011"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/2f74-px6z",
-            "issued": "2022-10-31",
             "@type": "dcat:Dataset",
-            "modified": "2022-11-21",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joe McGill",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "These graphs show the value, tons and ton-miles for the years 1997, 2002, 2007, 2012, and 2017. They are filterable by commodity and mode",
             "identifier": "https://data.transportation.gov/api/views/2f74-px6z",
+            "issued": "2022-10-31",
+            "landingPage": "https://data.transportation.gov/d/2f74-px6z",
+            "modified": "2022-11-21",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "These graphs show the value, tons and ton-miles for the years 1997, 2002, 2007, 2012, and 2017. They are filterable by commodity and mode",
             "title": "Value, Tons and Ton-Miles over time."
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/2f79-bkh3",
+            "accrualPeriodicity": "R/PT0.1S",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2015-11-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2015-03-02/2015-03-04",
-            "modified": "2015-11-01",
-            "keyword": [
-                "anthem",
-                "arizona",
-                "field test",
-                "freight",
-                "freight signal priority (fsp)",
-                "global positioning system (gps)",
-                "intelligent transportation systems (its)",
-                "i-sig",
-                "its joint program office (jpo)",
-                "multi-modal intelligent traffic signal system (mmitss)",
-                "trajectories",
-                "transit signal priority (tsp)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kate Hartman",
                 "hasEmail": "mailto:kate.hartman@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "US Department of Transportation"
-            },
-            "identifier": "https://data.transportation.gov/api/views/2f79-bkh3",
+            "dataQuality": true,
             "description": "Data were collected during the Multi-Modal Intelligent Transportation Signal Systems (MMITSS) study. MMITSS is a next-generation traffic signal system that seeks to provide a comprehensive traffic information framework to service all modes of transportation. The GPS data set catalogs the vehicle operation data of the test vehicles that used for the MMITSS field testing. The data contains the performance and operation details of vehicles. This file contains a number of fields detailing elements such as vehicle position and speed, fidelity measures of GPS-based data elements, and vehicle operation data.\r\n\r\nNOTE: All extra attachments are located in Multi-Modal Intelligent Traffic Signal Systems Basic Safety Message",
-            "title": "Multi-Modal Intelligent Traffic Signal Systems GPS",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1624,90 +1598,106 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2f79-bkh3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2f79-bkh3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2f79-bkh3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/2f79-bkh3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2f79-bkh3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2f79-bkh3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2f79-bkh3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2f79-bkh3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2f79-bkh3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Anthem, Arizona",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/2f79-bkh3",
+            "issued": "2015-11-01",
+            "keyword": [
+                "anthem",
+                "arizona",
+                "field test",
+                "freight",
+                "freight signal priority (fsp)",
+                "global positioning system (gps)",
+                "intelligent transportation systems (its)",
+                "i-sig",
+                "its joint program office (jpo)",
+                "multi-modal intelligent traffic signal system (mmitss)",
+                "trajectories",
+                "transit signal priority (tsp)"
+            ],
+            "landingPage": "https://data.transportation.gov/d/2f79-bkh3",
+            "language": [
+                "en-US"
+            ],
             "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "R/PT0.1S",
+            "modified": "2015-11-01",
+            "programCode": [
+                "021:013"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
+            "spatial": "Anthem, Arizona",
+            "temporal": "2015-03-02/2015-03-04",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Multi-Modal Intelligent Traffic Signal Systems GPS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/2g5j-egmt",
-            "issued": "2025-01-03",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-03",
-            "keyword": [
-                "monthly transportation statistics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:answers@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/2g5j-egmt",
             "description": "On-highway diesel price is the average retail price for diesel used in motor vehicles. The U.S. Energy Information Administration releases weekly gasoline and diesel price estimates.",
-            "title": "Fuel Prices - On-highway Diesel",
+            "identifier": "https://data.transportation.gov/api/views/2g5j-egmt",
+            "issued": "2025-01-03",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/2g5j-egmt",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-03",
             "programCode": [
                 "021:053"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Research and Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Fuel Prices - On-highway Diesel"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/2gdh-ejmg",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/2gdh-ejmg",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "Commuter Rail",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1715,59 +1705,53 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2gdh-ejmg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2gdh-ejmg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2gdh-ejmg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/2gdh-ejmg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2gdh-ejmg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2gdh-ejmg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2gdh-ejmg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2gdh-ejmg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2gdh-ejmg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/2gdh-ejmg",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/2gdh-ejmg",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Commuter Rail"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2021-04-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "traffic",
-                "traffic volume trends"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/2hya-qc6x",
+            "dataQuality": true,
             "description": "2019 Traffic Volume Data - FHWA's TMAS Data Program (based on unweighted raw continuous traffic count information collected by state highway agencies)",
-            "title": "TMAS 2019",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1775,76 +1759,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2hya-qc6x/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2hya-qc6x/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2hya-qc6x/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/2hya-qc6x/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2hya-qc6x/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2hya-qc6x/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2hya-qc6x/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2hya-qc6x/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2hya-qc6x/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/2hya-qc6x",
+            "issued": "2021-04-30",
+            "keyword": [
+                "traffic",
+                "traffic volume trends"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-05-08",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "spatial": "United States",
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TMAS 2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "https://www.civilrights.dot.gov/disadvantaged-business-enterprise/search-dbe-appeals-and-denials",
+            "agencyProgramURL": "https://www.civilrights.dot.gov/disadvantaged-business-enterprise",
+            "analysisUnit": "Disadvantaged Business Enterprise",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/2idi-42vf",
-            "issued": "2014-10-31",
-            "temporal": "R/2008-07-01/P1D",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-11-14",
-            "references": [
-                "https://www.civilrights.dot.gov/disadvantaged-business-enterprise"
-            ],
-            "keyword": [
-                "appeal",
-                "certification",
-                "dbe",
-                "decertification",
-                "disadvantaged business enterprise"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "559.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": true,
+            "describedBy": "https://www.civilrights.dot.gov/disadvantaged-business-enterprise/search-dbe-appeals-and-denials",
             "description": "List of DBEs and ACDBEs that have been rejected DBE status by state UCP officials. The information in this database, along with the decision to deny, decertify or reject an application, is maintained by State administered Unified Certification Programs (UCP). Firms identified in this database are ineligible for Federal Transportation grants made available specifically for DBEs.  Currently, the data set is available on the web at: https://www.civilrights.dot.gov/disadvantaged-business-enterprise/search-dbe-appeals-and-denials",
-            "title": "Decertified Disadvantaged Business Enterprises (DBE) and Airport Concession DBE List - Search Appeals and Decisions",
-            "isPartOf": "DOT-559",
-            "agencyProgramURL": "https://www.civilrights.dot.gov/disadvantaged-business-enterprise",
-            "primaryITInvestmentUII": "021-908746511",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1853,40 +1833,50 @@
                     "title": "Search Appeals and Decisions"
                 }
             ],
-            "spatial": "Address",
-            "describedBy": "https://www.civilrights.dot.gov/disadvantaged-business-enterprise/search-dbe-appeals-and-denials",
-            "dataQuality": true,
+            "identifier": "559.2",
+            "isPartOf": "DOT-559",
+            "issued": "2014-10-31",
+            "keyword": [
+                "appeal",
+                "certification",
+                "dbe",
+                "decertification",
+                "disadvantaged business enterprise"
+            ],
+            "landingPage": "https://data.transportation.gov/d/2idi-42vf",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "https://www.civilrights.dot.gov/disadvantaged-business-enterprise/search-dbe-appeals-and-denials",
+            "modified": "2024-11-14",
+            "phone": "202-366-8741",
+            "primaryITInvestmentUII": "021-908746511",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "references": [
+                "https://www.civilrights.dot.gov/disadvantaged-business-enterprise"
+            ],
+            "spatial": "Address",
+            "temporal": "R/2008-07-01/P1D",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Disadvantaged Business Enterprise",
-            "phone": "202-366-8741",
-            "language": [
-                "en-US"
-            ]
+            "title": "Decertified Disadvantaged Business Enterprises (DBE) and Airport Concession DBE List - Search Appeals and Decisions"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/2iue-rr78",
-            "issued": "2023-11-06",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-28",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
-            "identifier": "https://data.transportation.gov/api/views/2iue-rr78",
             "description": "",
-            "title": "Defects and Violations",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1894,98 +1884,88 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2iue-rr78/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2iue-rr78/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2iue-rr78/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/2iue-rr78/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2iue-rr78/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2iue-rr78/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2iue-rr78/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2iue-rr78/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2iue-rr78/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/2iue-rr78",
+            "issued": "2023-11-06",
+            "landingPage": "https://data.transportation.gov/d/2iue-rr78",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-08-28",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Defects and Violations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/2iwc-fgn4",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2025-01-02",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-02",
-            "keyword": [
-                "monthly transportation statistics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:answers@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/2iwc-fgn4",
             "description": "Heavy trucks include trucks with more than 14,000 pounds gross vehicle weight. Prior to the 2003 Benchmark Revision heavy trucks were more than 10,000 pounds. The U.S. Bureau of Economic Analysis releases auto and truck sales data, which are used in the preparation of estimates of personal consumption expenditures.",
-            "title": "Heavy Truck Sales",
+            "identifier": "https://data.transportation.gov/api/views/2iwc-fgn4",
+            "issued": "2025-01-02",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/2iwc-fgn4",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-02",
             "programCode": [
                 "021:053"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Research and Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Heavy Truck Sales"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/2j3q-2taz",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2019-05-08",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-29",
-            "keyword": [
-                "connectivity",
-                "passengers",
-                "passenger travel",
-                "transportation",
-                "transportation facilities"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NTL_Data_Curator",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/2j3q-2taz",
             "description": "Overview\nThe IPCD is a nationwide database of passenger transportation terminals, with data on the availability of connections among the various scheduled public transportation modes at each facility. The IPCD data covers the following types of passenger transportation terminals/stops: 1. Scheduled airline service airports. 2. Intercity bus stations (includes stations served by regular scheduled intercity bus service such as Greyhound, Trailways, code sharing buses such as Amtrak Thruway feeder buses, supplemental buses that provide additional frequencies along rail routes, and airport bus services from locations that are outside of the airport metropolitan area). 3. Intercity and transit ferry terminals. 4. Light-rail transit stations. 5. Heavy-rail transit stations. 6. Passenger-rail stations on the national rail network served by intercity rail and/or commuter rail services. 7. Bike-share stations belonging to bike-share systems that are open to the general public, IT-automated, and station based (contain hubs to which users can grab and return a bike). The data elements describe the location of the above types of terminals as well as the availability of intercity, commuter, and transit rail; scheduled air service; intercity and transit bus; intercity and transit ferry services; and bike-share availability. Transit bus service locations are not specifically included in the database. However, the status of transit bus as a connecting mode is included for each bike-share facility in the database.",
-            "title": "Intermodal Passenger Connectivity Database",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1993,25 +1973,61 @@
                     "mediaType": "text/html"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/2j3q-2taz",
+            "issued": "2019-05-08",
+            "keyword": [
+                "connectivity",
+                "passengers",
+                "passenger travel",
+                "transportation",
+                "transportation facilities"
+            ],
+            "landingPage": "https://data.transportation.gov/d/2j3q-2taz",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-29",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Intermodal Passenger Connectivity Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.ntdprogram.gov/ntdprogram/data.htm",
+            "agencyProgramURL": "http://www.ntdprogram.gov",
+            "analysisUnit": "Transit Agency, some data by Mode and Type of Service",
             "bureauCode": [
                 "021:36"
             ],
-            "landingPage": "https://data.transportation.gov/d/2j9c-wqx6",
-            "issued": "2010-10-01",
-            "temporal": "R/1996-12-31/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-05",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.ntdprogram.gov"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John D. Giorgis",
+                "hasEmail": "mailto:john.giorgis@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www.ntdprogram.gov/ntdprogram/data.htm",
+            "description": "Data reported to the NTD by urbanized area transit systems in their annual reports.   Includes contact information, contractural relationshps, subrecipient informatino, service area, sources of funds, operating expenditures by object class and function, capital expenditures by object class and function, fixed guideway information, revenue vehicle inventory, fuel consumption, employees, and labor hours, and urbanized area allocation information.   Also includes service supplied and consumed by annual total, average weekday, average saturday, and average sunday.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2010_database/NTD_database_2010.exe",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2010 Database"
+                }
             ],
+            "identifier": "21.14",
+            "isPartOf": "DOT-21",
+            "issued": "2010-10-01",
             "keyword": [
                 "agency",
                 "allocation",
@@ -2030,77 +2046,43 @@
                 "urbanized",
                 "vehicles"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John D. Giorgis",
-                "hasEmail": "mailto:john.giorgis@dot.gov"
-            },
-            "identifier": "21.14",
+            "landingPage": "https://data.transportation.gov/d/2j9c-wqx6",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-03-05",
+            "phone": "202-366-5430",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Transit Administration"
             },
-            "description": "Data reported to the NTD by urbanized area transit systems in their annual reports.   Includes contact information, contractural relationshps, subrecipient informatino, service area, sources of funds, operating expenditures by object class and function, capital expenditures by object class and function, fixed guideway information, revenue vehicle inventory, fuel consumption, employees, and labor hours, and urbanized area allocation information.   Also includes service supplied and consumed by annual total, average weekday, average saturday, and average sunday.",
-            "title": "NTD Annual Module Data Set - 2010 Database",
-            "isPartOf": "DOT-21",
-            "agencyProgramURL": "http://www.ntdprogram.gov",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2010_database/NTD_database_2010.exe",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "2010 Database"
-                }
+            "references": [
+                "http://www.ntdprogram.gov"
             ],
             "spatial": "Urbanized Areas",
-            "describedBy": "http://www.ntdprogram.gov/ntdprogram/data.htm",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.ntdprogram.gov/ntdprogram/data.htm",
+            "temporal": "R/1996-12-31/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Transit Agency, some data by Mode and Type of Service",
-            "phone": "202-366-5430",
-            "language": [
-                "en-US"
-            ]
+            "title": "NTD Annual Module Data Set - 2010 Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2022-07-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "highway",
-                "highway performance monitoring",
-                "highway performance monitoring system",
-                "highways"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/2m53-wgng",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 1985",
-            "title": "Historic HPMS Data (Universe) - 1985",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2108,82 +2090,118 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2m53-wgng/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2m53-wgng/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2m53-wgng/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/2m53-wgng/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2m53-wgng/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2m53-wgng/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2m53-wgng/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2m53-wgng/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2m53-wgng/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/2m53-wgng",
+            "issued": "2022-07-06",
+            "keyword": [
+                "highway",
+                "highway performance monitoring",
+                "highway performance monitoring system",
+                "highways"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-08",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
             "spatial": "United States",
-            "dataQuality": true,
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Historic HPMS Data (Universe) - 1985"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/2mc2-ud7r",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2025-01-03",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-03",
-            "keyword": [
-                "monthly transportation statistics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:answers@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/2mc2-ud7r",
             "description": "The U.S. Census Bureau provides monthly estimates of the total dollar value of construction work done in the United States as part of the Value of Construction Put in Place Survey (VIP). Includes construction related to pavement, lighting, retaining walls, tunnels, bridges, toll/weigh facilities, maintenance buildings, and rest facilities.",
-            "title": "State and Local Government Construction Spending - Highway and Street",
+            "identifier": "https://data.transportation.gov/api/views/2mc2-ud7r",
+            "issued": "2025-01-03",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/2mc2-ud7r",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-03",
             "programCode": [
                 "021:053"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Research and Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "State and Local Government Construction Spending - Highway and Street"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/2p8c-yq58",
-            "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": false,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
+            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "2012 Mississippi HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/mississippi2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Mississippi"
+                }
+            ],
+            "identifier": "678.78",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -2197,85 +2215,39 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.78",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Mississippi",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/2p8c-yq58",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5035",
             "primaryITInvestmentUII": "021-099281808",
             "programCode": [
                 "021:009"
             ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/mississippi2012.zip",
-                    "description": "2012 Mississippi HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Mississippi"
-                }
-            ],
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "temporal": "R/1981-11-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
-            "categoryDesignation": "Administrative",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-5035"
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Mississippi"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/2pc4-cx48",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2024-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-28",
-            "keyword": [
-                "connected equipment",
-                "connected vehicle",
-                "connected vehicle data",
-                "connected vehicle environment",
-                "connected vehicle message",
-                "connected vehicles",
-                "on-board equipment",
-                "on-board unit",
-                "roadside equipment",
-                "road side unit",
-                "vehicle data",
-                "vehicle to infrastructure",
-                "vehicle to vehicle"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kate Hartman",
                 "hasEmail": "mailto:kate.hartman@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/2pc4-cx48",
             "description": "Part of Wyoming Department of Transportation Connected Vehicle Pilot Phase 4. Test case WV2VMCT-1 Verify V2V communication of BSMs vehicle 1 data",
-            "title": "LTE-V2X Wyoming Connected Vehicle Pilot test ID WV2VMCT-1 vehicle 1",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2283,63 +2255,76 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2pc4-cx48/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2pc4-cx48/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2pc4-cx48/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/2pc4-cx48/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2pc4-cx48/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2pc4-cx48/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2pc4-cx48/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2pc4-cx48/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2pc4-cx48/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Wyoming",
+            "identifier": "https://data.transportation.gov/api/views/2pc4-cx48",
+            "issued": "2024-07-19",
+            "keyword": [
+                "connected equipment",
+                "connected vehicle",
+                "connected vehicle data",
+                "connected vehicle environment",
+                "connected vehicle message",
+                "connected vehicles",
+                "on-board equipment",
+                "on-board unit",
+                "roadside equipment",
+                "road side unit",
+                "vehicle data",
+                "vehicle to infrastructure",
+                "vehicle to vehicle"
+            ],
+            "landingPage": "https://data.transportation.gov/d/2pc4-cx48",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-09-28",
+            "programCode": [
+                "021:042"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "spatial": "Wyoming",
             "theme": [
                 "Automobiles"
-            ]
+            ],
+            "title": "LTE-V2X Wyoming Connected Vehicle Pilot test ID WV2VMCT-1 vehicle 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://data.transportation.gov/d/2pmx-f3b7",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:18"
             ],
-            "rights": "Internal interfaces only - content may be FOIA-ble",
-            "issued": "2018-12-18",
-            "@type": "dcat:Dataset",
-            "temporal": "R/2014/P1Y",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-01",
-            "keyword": [
-                "correspondence"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "identifier": "476.0",
+            "dataQuality": false,
             "description": "The CCMMercury System IS a correspondence tracking (or control) system which (l) provides a central repository for agency correspondence, (2) tracks and manages correspondence, and (3) tracks and manages correspondence letters.",
-            "title": "CCMMercury System -",
-            "programCode": [
-                "021:031"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2347,32 +2332,62 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
+            "identifier": "476.0",
+            "issued": "2018-12-18",
+            "keyword": [
+                "correspondence"
+            ],
+            "landingPage": "https://data.transportation.gov/d/2pmx-f3b7",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-05-01",
+            "phone": "202-366-5649",
+            "programCode": [
+                "021:031"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "rights": "Internal interfaces only - content may be FOIA-ble",
+            "temporal": "R/2014/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "categoryDesignation": "Research",
-            "phone": "202-366-5649",
-            "language": [
-                "en-US"
-            ]
+            "title": "CCMMercury System -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/2pp8-rphe",
-            "issued": "1970-01-01",
-            "temporal": "R/1970-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "State Traffic Monitoring Systems (TMS)",
-            "references": [
-                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/05aprtvt/05aprtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "April 2005"
+                }
             ],
+            "identifier": "18.113",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -2382,82 +2397,48 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.113",
+            "landingPage": "https://data.transportation.gov/d/2pp8-rphe",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-1067",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - April 2005",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/05aprtvt/05aprtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "April 2005"
-                }
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
             ],
             "spatial": "Vehicles by type of functional classified roadway",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "temporal": "R/1970-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
-            "phone": "202-366-1067",
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Traffic Volume Trends - April 2005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://hepgis.fhwa.dot.gov/hepgismaps11/#",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/2qg9-g4hf",
-            "issued": "2007-01-01",
-            "temporal": "2007-01-01/2014-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Geospatial",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "arra planning",
-                "fhwa",
-                "geographic",
-                "geospatial",
-                "map"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "692.15",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - 2009 Fatal Crashes",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "primaryITInvestmentUII": "021-845083703",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2466,53 +2447,87 @@
                     "title": "2009 Fatal Crashes"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.15",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/2qg9-g4hf",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://hepgis.fhwa.dot.gov/hepgismaps11/#",
+            "modified": "2024-05-08",
+            "phone": "708-283-3554",
+            "primaryITInvestmentUII": "021-845083703",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "spatial": "National, State, County",
+            "temporal": "2007-01-01/2014-12-31",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Geospatial",
-            "phone": "708-283-3554",
-            "language": [
-                "en-US"
-            ]
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - 2009 Fatal Crashes"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/2qgq-ic2u",
-            "issued": "2022-11-03",
             "@type": "dcat:Dataset",
-            "modified": "2023-01-19",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joe McGill",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "Downloadable Tables by Origin or Destination. Filterable by Year, Commodity and Mode.",
             "identifier": "https://data.transportation.gov/api/views/2qgq-ic2u",
+            "issued": "2022-11-03",
+            "landingPage": "https://data.transportation.gov/d/2qgq-ic2u",
+            "modified": "2023-01-19",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "Downloadable Tables by Origin or Destination. Filterable by Year, Commodity and Mode.",
             "title": "CFS Data Tables"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/2qq3-bhyt",
-            "issued": "1970-01-01",
-            "temporal": "R/1970-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "State Traffic Monitoring Systems (TMS)",
-            "references": [
-                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/02juntvt/tvtjun02.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "June 2002"
+                }
             ],
+            "identifier": "18.147",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -2522,64 +2537,39 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.147",
+            "landingPage": "https://data.transportation.gov/d/2qq3-bhyt",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-1067",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - June 2002",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/02juntvt/tvtjun02.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "June 2002"
-                }
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
             ],
             "spatial": "Vehicles by type of functional classified roadway",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "temporal": "R/1970-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
-            "phone": "202-366-1067",
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Traffic Volume Trends - June 2002"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/2r82-tsmp",
-            "issued": "2023-02-04",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/2r82-tsmp",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "CPRS",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2587,67 +2577,54 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2r82-tsmp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2r82-tsmp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2r82-tsmp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/2r82-tsmp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2r82-tsmp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2r82-tsmp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2r82-tsmp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2r82-tsmp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2r82-tsmp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/2r82-tsmp",
+            "issued": "2023-02-04",
+            "landingPage": "https://data.transportation.gov/d/2r82-tsmp",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "CPRS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/2rdx-wgpx",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2018-01-12",
-            "@type": "dcat:Dataset",
-            "modified": "2018-01-12",
-            "keyword": [
-                "connected vehicle message",
-                "connected vehicle pilot (cvp)",
-                "field test",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "traveler information message (tim)",
-                "wyoming",
-                "wyoming connected vehicle (cv) pilot",
-                "wyoming cv pilot",
-                "wyoming department of transportation (wydot)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kate Hartman",
                 "hasEmail": "mailto:kate.hartman@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "US Department of Transportation"
-            },
-            "identifier": "https://data.transportation.gov/api/views/2rdx-wgpx",
+            "dataQuality": true,
             "description": "This dataset contains a sample of the broadcast Traveler Information Messages (TIM) being generated by the Wyoming Connected Vehicle (CV) Pilot. The full set of TIMs can be found in the <a href='http://usdot-its-cvpilot-publicdata.s3.amazonaws.com/index.html' target=\"_blank\">ITS DataHub data sandbox</a>.\n</n></n>\nRevision Note: This dataset only contains TIM sample data prior to December 18, 2018. For the most recent sample of TIM data, please refer to the <a href=\"https://data.transportation.gov/Automobiles/-Dev-Wyoming-CV-Pilot-Traveler-Information-Message/6nxx-nmxk\" target=\"_blank\">Schema Version 6 dataset</a> or retrieve the data from the <a href='http://usdot-its-cvpilot-publicdata.s3.amazonaws.com/index.html' target=\"_blank\">ITS DataHub data sandbox</a>.",
-            "title": "Wyoming CV Pilot Traveler Information Message Sample (Schema Version 5)",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2655,73 +2632,76 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2rdx-wgpx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2rdx-wgpx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2rdx-wgpx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/2rdx-wgpx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2rdx-wgpx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2rdx-wgpx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2rdx-wgpx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2rdx-wgpx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2rdx-wgpx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Wyoming",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/2rdx-wgpx",
+            "issued": "2018-01-12",
+            "keyword": [
+                "connected vehicle message",
+                "connected vehicle pilot (cvp)",
+                "field test",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "traveler information message (tim)",
+                "wyoming",
+                "wyoming connected vehicle (cv) pilot",
+                "wyoming cv pilot",
+                "wyoming department of transportation (wydot)"
+            ],
+            "landingPage": "https://data.transportation.gov/d/2rdx-wgpx",
+            "language": [
+                "English"
+            ],
             "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "irregular",
+            "modified": "2018-01-12",
+            "programCode": [
+                "021:013"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
+            "spatial": "Wyoming",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Wyoming CV Pilot Traveler Information Message Sample (Schema Version 5)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Access restricted under the Privacy Act of 1974; various SORNs apply \u2013 see Privacy Impact Assessment at http://www.dot.gov/individuals/privacy/pia-security-operations-systems-sos",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/2rew-e42k",
-            "issued": "2014-09-16",
-            "temporal": "R/2014-09-16/PT1S",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Other",
-            "keyword": [
-                "circuit",
-                "closed",
-                "personnel",
-                "security",
-                "television"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "431.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
             "description": "This data set contains information closed circuit television camera locations, setups, and a 30-day archive of video captured by the cameras.",
-            "title": "DOT Headquarters Closed Circuit Television -",
-            "primaryITInvestmentUII": "021-686225834",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2729,50 +2709,50 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Other"
+            "identifier": "431.0",
+            "issued": "2014-09-16",
+            "keyword": [
+                "circuit",
+                "closed",
+                "personnel",
+                "security",
+                "television"
             ],
-            "accrualPeriodicity": "R/PT1S",
-            "categoryDesignation": "Administrative",
+            "landingPage": "https://data.transportation.gov/d/2rew-e42k",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-8020"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-11-14",
+            "phone": "202-366-8020",
+            "primaryITInvestmentUII": "021-686225834",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "rights": "Access restricted under the Privacy Act of 1974; various SORNs apply \u2013 see Privacy Impact Assessment at http://www.dot.gov/individuals/privacy/pia-security-operations-systems-sos",
+            "temporal": "R/2014-09-16/PT1S",
+            "theme": [
+                "Other"
+            ],
+            "title": "DOT Headquarters Closed Circuit Television -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2022-07-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "highway",
-                "highway performance monitoring",
-                "highway performance monitoring system",
-                "highways",
-                "hpms",
-                "sample"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/2rn3-qyzt",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 1999",
-            "title": "Historic HPMS Data (Sample) - 1999",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2780,81 +2760,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2rn3-qyzt/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2rn3-qyzt/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2rn3-qyzt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/2rn3-qyzt/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2rn3-qyzt/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2rn3-qyzt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2rn3-qyzt/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2rn3-qyzt/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2rn3-qyzt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/2rn3-qyzt",
+            "issued": "2022-07-08",
+            "keyword": [
+                "highway",
+                "highway performance monitoring",
+                "highway performance monitoring system",
+                "highways",
+                "hpms",
+                "sample"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-08",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
             "spatial": "United States",
-            "dataQuality": true,
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Historic HPMS Data (Sample) - 1999"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/2s2m-b2uv",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2024-06-27",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-17",
-            "keyword": [
-                "analysis of trends",
-                "charging stations",
-                "e-commerce",
-                "fhwa",
-                "forecasting",
-                "gdp",
-                "ghg",
-                "lane miles",
-                "modeling",
-                "on-demand service revenue",
-                "population",
-                "population density",
-                "telework",
-                "tms",
-                "transportation demand",
-                "unemployment rate",
-                "unlinked passenger trips",
-                "vmt",
-                "what if"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Heather Rose",
                 "hasEmail": "mailto:heather.rose@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/2s2m-b2uv",
             "description": "This dataset allows the Mobility Trends team to understand and interpret transportation trends and performance metrics based off the forecasts. These interpretations include VMT Forecasts, Vehicle Types/Fuel use Forecasts, and Emissions forecasts with various Geographic breakouts.",
-            "title": "Mobility Trends What if Analysis",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2862,97 +2828,111 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2s2m-b2uv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2s2m-b2uv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2s2m-b2uv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/2s2m-b2uv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2s2m-b2uv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2s2m-b2uv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2s2m-b2uv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2s2m-b2uv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2s2m-b2uv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/2s2m-b2uv",
+            "issued": "2024-06-27",
+            "keyword": [
+                "analysis of trends",
+                "charging stations",
+                "e-commerce",
+                "fhwa",
+                "forecasting",
+                "gdp",
+                "ghg",
+                "lane miles",
+                "modeling",
+                "on-demand service revenue",
+                "population",
+                "population density",
+                "telework",
+                "tms",
+                "transportation demand",
+                "unemployment rate",
+                "unlinked passenger trips",
+                "vmt",
+                "what if"
+            ],
+            "landingPage": "https://data.transportation.gov/d/2s2m-b2uv",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-07-17",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "Mobility Trends What if Analysis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/2ub2-svfq",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2023-09-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-12",
-            "keyword": [
-                "aff",
-                "aviation facts & figures"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810 "
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/2ub2-svfq",
             "description": "Aviation Facts and Figures",
-            "title": "Aviation Facts and Figures",
+            "identifier": "https://data.transportation.gov/api/views/2ub2-svfq",
+            "issued": "2023-09-20",
+            "keyword": [
+                "aff",
+                "aviation facts & figures"
+            ],
+            "landingPage": "https://data.transportation.gov/d/2ub2-svfq",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-12-12",
             "programCode": [
                 "021:053"
             ],
-            "license": "https://www.usa.gov/government-works",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Aviation"
-            ]
+            ],
+            "title": "Aviation Facts and Figures"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2022-07-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "highway",
-                "highway performance monitoring",
-                "highway performance monitoring system",
-                "highways",
-                "hpms",
-                "sample"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/2uwh-rvw4",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System data sample for the year 1997",
-            "title": "Historic HPMS Data (Sample) - 1997",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2960,60 +2940,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2uwh-rvw4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2uwh-rvw4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2uwh-rvw4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/2uwh-rvw4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2uwh-rvw4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2uwh-rvw4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2uwh-rvw4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2uwh-rvw4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2uwh-rvw4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/2uwh-rvw4",
+            "issued": "2022-07-08",
+            "keyword": [
+                "highway",
+                "highway performance monitoring",
+                "highway performance monitoring system",
+                "highways",
+                "hpms",
+                "sample"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-08",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
             "spatial": "United States",
-            "dataQuality": true,
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Historic HPMS Data (Sample) - 1997"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/2vuh-bi35",
-            "issued": "2024-05-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-02",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joe McGill",
                 "hasEmail": "mailto:joseph.mcgill@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/2vuh-bi35",
             "description": "",
-            "title": "vius2test",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3021,40 +3008,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2vuh-bi35/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2vuh-bi35/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2vuh-bi35/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/2vuh-bi35/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2vuh-bi35/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2vuh-bi35/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/2vuh-bi35/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/2vuh-bi35/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/2vuh-bi35/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "https://data.transportation.gov/api/views/2vuh-bi35",
+            "issued": "2024-05-02",
+            "landingPage": "https://data.transportation.gov/d/2vuh-bi35",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-02",
+            "programCode": [
+                "021:042"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "vius2test"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/2wsj-6j7i",
-            "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": false,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
+            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "2012 Pennsylvania HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/pennsylvania2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Pennsylvania"
+                }
+            ],
+            "identifier": "678.92",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -3068,100 +3086,64 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.92",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Pennsylvania",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/2wsj-6j7i",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5035",
             "primaryITInvestmentUII": "021-099281808",
             "programCode": [
                 "021:009"
             ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/pennsylvania2012.zip",
-                    "description": "2012 Pennsylvania HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Pennsylvania"
-                }
-            ],
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "temporal": "R/1981-11-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
-            "categoryDesignation": "Administrative",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-5035"
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Pennsylvania"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/2xug-93pv",
-            "issued": "2021-05-13",
             "@type": "dcat:Dataset",
-            "modified": "2024-03-04",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sean Jahanmir",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/2xug-93pv",
+            "issued": "2021-05-13",
+            "landingPage": "https://data.transportation.gov/d/2xug-93pv",
+            "modified": "2024-03-04",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Safety"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/goshrp2/Solutions/All/C01/PlanWorks__Better_planning_Better_projects",
+            "agencyProgramURL": "https://fhwaapps.fhwa.dot.gov/planworks/",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/2ykb-hgzy",
-            "issued": "2014-12-29",
-            "temporal": "2014-12-29/2014-12-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "collaboration",
-                "decision",
-                "fhwa",
-                "planning",
-                "policy",
-                "transportation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "DOT-717",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "PlanWorks is a Web resource that supports collaborative decision making in transportation planning and project development. PlanWorks is built around key decision points in long-range planning, programming, corridor planning, and environmental review. PlanWorks suggests when and how to engage cross-disciplinary partners and stakeholder groups. PlanWorks has four major components:-A troubleshooting guide describing the common decision points and opportunities for cooperation in the transportation planning and environmental review process. For each of the key decision points, PlanWorks provides policy and stakeholder questions, data needs, case studies and examples, and links to tools that can help support the decision.-Interactive assessments that enable project stakeholders to identify opportunities to work together, improve interagency cooperation, and expedite project delivery.",
-            "title": "PlanWorks",
-            "agencyProgramURL": "https://fhwaapps.fhwa.dot.gov/planworks/",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3170,175 +3152,180 @@
                     "title": "PlanWorks: Better Planning. Better Projects"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "DOT-717",
+            "issued": "2014-12-29",
+            "keyword": [
+                "collaboration",
+                "decision",
+                "fhwa",
+                "planning",
+                "policy",
+                "transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/goshrp2/Solutions/All/C01/PlanWorks__Better_planning_Better_projects",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/2ykb-hgzy",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-2048"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-2048",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "temporal": "2014-12-29/2014-12-29",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "PlanWorks"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/2yqq-baqd",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2020-03-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
-            "keyword": [
-                "producer price index",
-                "transportation cost"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/2yqq-baqd",
             "description": "Transportation costs faced by businesses",
-            "title": "Transportation Economic Trends: Transportation Costs - Businesses",
+            "identifier": "https://data.transportation.gov/api/views/2yqq-baqd",
+            "issued": "2020-03-01",
+            "keyword": [
+                "producer price index",
+                "transportation cost"
+            ],
+            "landingPage": "https://data.transportation.gov/d/2yqq-baqd",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-18",
+            "phone": "202-366-DATA(3282)",
             "programCode": [
                 "021:053"
             ],
-            "license": "https://www.usa.gov/government-works",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Transportation Economic Trends: Transportation Costs - Businesses"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.bts.gov/stories/s/2z63-wprv",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2020-09-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
-            "keyword": [
-                "employment",
-                "transportation employment"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/2z63-wprv",
             "description": "This page focuses on monthly employment in the transportation and warehousing sector and breaks them down by transportation mode and by women workers.",
-            "title": "Employment-Transportation and Warehousing Sector Total, by Mode, and by Women workers",
+            "identifier": "https://data.transportation.gov/api/views/2z63-wprv",
+            "issued": "2020-09-23",
+            "keyword": [
+                "employment",
+                "transportation employment"
+            ],
+            "landingPage": "https://data.bts.gov/stories/s/2z63-wprv",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-18",
+            "phone": "202-366-DATA(3282)",
             "programCode": [
                 "021:053"
             ],
-            "license": "https://www.usa.gov/government-works",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Employment-Transportation and Warehousing Sector Total, by Mode, and by Women workers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/325k-p93b",
-            "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
-            "keyword": [
-                "aadt",
-                "condition",
-                "highway",
-                "iri",
-                "ownership",
-                "pavement",
-                "performance",
-                "traffic",
-                "travel",
-                "use",
-                "vmt"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "678.77",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": false,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
             "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Minnesota",
-            "isPartOf": "DOT-678",
-            "primaryITInvestmentUII": "021-099281808",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/minnesota2012.zip",
-                    "description": "2012 Minnesota HPMS Shapefile",
                     "@type": "dcat:Distribution",
+                    "description": "2012 Minnesota HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/minnesota2012.zip",
+                    "mediaType": "application/zip",
                     "title": "2012 Minnesota"
                 }
             ],
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "678.77",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
+            "keyword": [
+                "aadt",
+                "condition",
+                "highway",
+                "iri",
+                "ownership",
+                "pavement",
+                "performance",
+                "traffic",
+                "travel",
+                "use",
+                "vmt"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
-            "categoryDesignation": "Administrative",
+            "landingPage": "https://data.transportation.gov/d/325k-p93b",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-5035"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5035",
+            "primaryITInvestmentUII": "021-099281808",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "temporal": "R/1981-11-01/P1Y",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Minnesota"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/33as-hyfa",
-            "issued": "2023-03-16",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-16",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Robert Nazareth",
                 "hasEmail": "mailto:robert.nazareth@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/33as-hyfa",
             "description": "January - March 2022",
-            "title": "Jan_Mar_2022_Part234",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3346,55 +3333,55 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/33as-hyfa/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/33as-hyfa/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/33as-hyfa/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/33as-hyfa/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/33as-hyfa/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/33as-hyfa/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/33as-hyfa/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/33as-hyfa/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/33as-hyfa/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/33as-hyfa",
+            "issued": "2023-03-16",
+            "landingPage": "https://data.transportation.gov/d/33as-hyfa",
+            "modified": "2023-03-16",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Aviation"
-            ]
+            ],
+            "title": "Jan_Mar_2022_Part234"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/33xp-y9fx",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-12-09",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:answers@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/33xp-y9fx",
             "description": "",
-            "title": "AFF - P12a - Fuel Consumption by Carrier Group",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3402,46 +3389,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/33xp-y9fx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/33xp-y9fx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/33xp-y9fx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/33xp-y9fx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/33xp-y9fx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/33xp-y9fx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/33xp-y9fx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/33xp-y9fx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/33xp-y9fx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/33xp-y9fx",
+            "issued": "2024-12-09",
+            "landingPage": "https://data.transportation.gov/d/33xp-y9fx",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-13",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Aviation"
-            ]
+            ],
+            "title": "AFF - P12a - Fuel Consumption by Carrier Group"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/346p-qmg8",
-            "issued": "1970-01-01",
-            "temporal": "R/1970-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "State Traffic Monitoring Systems (TMS)",
-            "references": [
-                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/08martvt/08martvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "March 2008"
+                }
             ],
+            "identifier": "18.78",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -3451,88 +3466,51 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.78",
+            "landingPage": "https://data.transportation.gov/d/346p-qmg8",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-1067",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - March 2008",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/08martvt/08martvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "March 2008"
-                }
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
             ],
             "spatial": "Vehicles by type of functional classified roadway",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "temporal": "R/1970-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
-            "phone": "202-366-1067",
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Traffic Volume Trends - March 2008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/downloads/folders/Investigations/FLAT_INV.zip",
+            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
+            "analysisUnit": "Vehicles , Tires, Child Safety Seats, Equipment",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/347b-4786",
-            "issued": "2002-12-16",
-            "temporal": "R/1965-01-01/P1D",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-01",
-            "references": [
-                "http://www-odi.nhtsa.dot.gov/downloads/folders/Investigations/INV.txt"
-            ],
-            "keyword": [
-                "car",
-                "complaint",
-                "defect",
-                "investigation",
-                "manufacturer",
-                "recall",
-                "safercar.gov"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "84.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "The National Highway Traffic Safety Administration (NHTSA) has the right to investigate reports of defective products. Information about defective products can come from manufacturers, consumers or law enforcement agencies. NHTSA stores defect investigation information in a database. It uses this information to generate monthly defect reports. It also makes this information available to consumers through the NHTSA web site. You can search for defect investigation information for the following product categories: -\tVehicles -\tEquipment -\tChild Restraints -\tTires",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Investigations - Monthly Defect Investigations Reports (last 6 months)",
-            "isPartOf": "DOT-84",
-            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
+            "dataQuality": true,
+            "describedBy": "http://www-odi.nhtsa.dot.gov/downloads/folders/Investigations/INV.txt",
             "describedByType": "text/plain",
-            "primaryITInvestmentUII": "021-777552743",
-            "programCode": [
-                "021:000"
-            ],
+            "description": "The National Highway Traffic Safety Administration (NHTSA) has the right to investigate reports of defective products. Information about defective products can come from manufacturers, consumers or law enforcement agencies. NHTSA stores defect investigation information in a database. It uses this information to generate monthly defect reports. It also makes this information available to consumers through the NHTSA web site. You can search for defect investigation information for the following product categories: -\tVehicles -\tEquipment -\tChild Restraints -\tTires",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3541,35 +3519,74 @@
                     "title": "Monthly Defect Investigations Reports (last 6 months)"
                 }
             ],
-            "describedBy": "http://www-odi.nhtsa.dot.gov/downloads/folders/Investigations/INV.txt",
-            "dataQuality": true,
+            "identifier": "84.2",
+            "isPartOf": "DOT-84",
+            "issued": "2002-12-16",
+            "keyword": [
+                "car",
+                "complaint",
+                "defect",
+                "investigation",
+                "manufacturer",
+                "recall",
+                "safercar.gov"
+            ],
+            "landingPage": "https://data.transportation.gov/d/347b-4786",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/downloads/folders/Investigations/FLAT_INV.zip",
+            "modified": "2024-05-01",
+            "phone": "202-366-0154",
+            "primaryITInvestmentUII": "021-777552743",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "http://www-odi.nhtsa.dot.gov/downloads/folders/Investigations/INV.txt"
+            ],
+            "temporal": "R/1965-01-01/P1D",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Vehicles , Tires, Child Safety Seats, Equipment",
-            "phone": "202-366-0154",
-            "language": [
-                "en-US"
-            ]
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Investigations - Monthly Defect Investigations Reports (last 6 months)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.nhtsa.dot.gov/STSI",
+            "agencyProgramURL": "http://www-nrd.nhtsa.dot.gov/departments/nrd-30/ncsa/STSI/USA%20WEB%20REPORT.HTM",
+            "analysisUnit": "Incident",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/34up-ii43",
-            "issued": "2009-09-01",
-            "temporal": "R/2007-01-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/812214",
-            "references": [
-                "https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/812214"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://go.usa.gov/kfnh",
+            "description": "The State Traffic Safety Information (STSI) portal is part of the larger Fatality Analysis Reporting System (FARS) Encyclopedia. STSI provides state-by-state traffic safety profiles, including: crash data, lives saved/savable, legislation, economic costs, grant funding, alcohol related crash data, performance measures, and geographic maps of crash data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "2010-2015 FARS Accident File data available on publically accessible BTS managed ArcGIS Cloud Server",
+                    "downloadURL": "https://maps.bts.dot.gov/services/rest/services/NHTSA",
+                    "mediaType": "text/html",
+                    "title": "2010-2015 FARS Accident File data"
+                }
             ],
+            "identifier": "266.2",
+            "isPartOf": "DOT-266",
+            "issued": "2009-09-01",
             "keyword": [
                 "crash",
                 "data",
@@ -3581,86 +3598,49 @@
                 "safety",
                 "vehicle"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "266.2",
+            "landingPage": "https://data.transportation.gov/d/34up-ii43",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-5358",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Highway Traffic Safety Administration"
             },
-            "description": "The State Traffic Safety Information (STSI) portal is part of the larger Fatality Analysis Reporting System (FARS) Encyclopedia. STSI provides state-by-state traffic safety profiles, including: crash data, lives saved/savable, legislation, economic costs, grant funding, alcohol related crash data, performance measures, and geographic maps of crash data.",
-            "title": "State Traffic Safety Information - 2010-2015 FARS Accident File data",
-            "isPartOf": "DOT-266",
-            "agencyProgramURL": "http://www-nrd.nhtsa.dot.gov/departments/nrd-30/ncsa/STSI/USA%20WEB%20REPORT.HTM",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://maps.bts.dot.gov/services/rest/services/NHTSA",
-                    "description": "2010-2015 FARS Accident File data available on publically accessible BTS managed ArcGIS Cloud Server",
-                    "@type": "dcat:Distribution",
-                    "title": "2010-2015 FARS Accident File data"
-                }
+            "references": [
+                "https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/812214"
             ],
             "spatial": "Latitude, Longitude",
-            "describedBy": "http://go.usa.gov/kfnh",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.nhtsa.dot.gov/STSI",
+            "temporal": "R/2007-01-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Incident",
-            "phone": "202-366-5358",
-            "language": [
-                "en-US"
-            ]
+            "title": "State Traffic Safety Information - 2010-2015 FARS Accident File data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "ftp://ftp.nhtsa.dot.gov/Ped/,  ftp://ftp.nhtsa.dot.gov/Ped/96PedMan.pdf",
+            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
+            "analysisUnit": "Motor vehicle vs Pedestrian crash",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/353r-6dhf",
-            "issued": "1999-09-17",
-            "temporal": "1994-06-01/1998-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "ftp://ftp.nhtsa.dot.gov/Ped/"
-            ],
-            "keyword": [
-                "crash",
-                "injury",
-                "motor vehicle",
-                "pedestrian",
-                "vehicle"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "289.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "The Pedestrian Crash Data Study (PCDS) collected detailed data on motor vehicle vs pedestrian crashes.",
-            "title": "The Pedestrian Crash Data Study (PCDS) - ASCII File",
-            "isPartOf": "DOT-289",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3669,49 +3649,53 @@
                     "title": "ASCII File"
                 }
             ],
-            "spatial": "United States",
-            "dataQuality": true,
+            "identifier": "289.2",
+            "isPartOf": "DOT-289",
+            "issued": "1999-09-17",
+            "keyword": [
+                "crash",
+                "injury",
+                "motor vehicle",
+                "pedestrian",
+                "vehicle"
+            ],
+            "landingPage": "https://data.transportation.gov/d/353r-6dhf",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "ftp://ftp.nhtsa.dot.gov/Ped/,  ftp://ftp.nhtsa.dot.gov/Ped/96PedMan.pdf",
+            "modified": "2024-05-01",
+            "phone": "202-366-4998",
+            "programCode": [
+                "021:032"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "ftp://ftp.nhtsa.dot.gov/Ped/"
+            ],
+            "spatial": "United States",
+            "temporal": "1994-06-01/1998-12-31",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Motor vehicle vs Pedestrian crash",
-            "phone": "202-366-4998",
-            "language": [
-                "en-US"
-            ]
+            "title": "The Pedestrian Crash Data Study (PCDS) - ASCII File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2021-05-11",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "traffic",
-                "traffic volume trends"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/354n-8ysa",
+            "dataQuality": true,
             "description": "2017 Traffic Volume Data - FHWA's TMAS Data Program (based on unweighted raw continuous traffic count information collected by state highway agencies)",
-            "title": "TMAS 2017",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3719,97 +3703,93 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/354n-8ysa/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/354n-8ysa/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/354n-8ysa/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/354n-8ysa/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/354n-8ysa/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/354n-8ysa/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/354n-8ysa/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/354n-8ysa/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/354n-8ysa/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/354n-8ysa",
+            "issued": "2021-05-11",
+            "keyword": [
+                "traffic",
+                "traffic volume trends"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-05-08",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "spatial": "United States",
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TMAS 2017"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/35nd-2jfs",
-            "issued": "2023-04-25",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/35nd-2jfs",
+            "issued": "2023-04-25",
+            "landingPage": "https://data.transportation.gov/d/35nd-2jfs",
+            "modified": "2025-01-08",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
-            "title": "NHS Traffic Speed Trends",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "NHS Traffic Speed Trends"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://www.nhtsa.gov/cps/cpsfitting/index.cfm",
+            "agencyProgramURL": "http://www.nhtsa.gov/cps/cpsfitting/index.cfm",
+            "analysisUnit": "N/A",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/35sv-c5e6",
-            "issued": "2010-01-05",
-            "temporal": "R/2000-01-01/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.nhtsa.gov/webapi/Default.aspx%3FCSSIStations/Metadata/80"
-            ],
-            "keyword": [
-                "child seat",
-                "inspection",
-                "safety",
-                "station",
-                "stations"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "80.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
             "description": "The Child Safety Seat Inspection Station Locations are used to make it easier for all citizens to get their Child Safety Seats properly installed. Car crashes are the largest cause of fatalities and serious injuries for children between ages 2 and 15.  Also, surveys indicate that a high percentage of Child Safety Seats are not installed properly.  Information updates for each station are reported to NHTSA and enterred by NHTSA staff.  NHTSA staff will also attempt to validate the station locations using a comercial Geographic database so this data will, in most cases, be able to be used for driving directions.",
-            "title": "NHTSA Child Safety Seat Inspection Station Locator - NCSSISL - NHTSA API",
-            "isPartOf": "DOT-80",
-            "agencyProgramURL": "http://www.nhtsa.gov/cps/cpsfitting/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3818,89 +3798,125 @@
                     "title": "NHTSA API"
                 }
             ],
-            "spatial": "Zip, State, Geo co-ordinates",
-            "dataQuality": false,
+            "identifier": "80.2",
+            "isPartOf": "DOT-80",
+            "issued": "2010-01-05",
+            "keyword": [
+                "child seat",
+                "inspection",
+                "safety",
+                "station",
+                "stations"
+            ],
+            "landingPage": "https://data.transportation.gov/d/35sv-c5e6",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.nhtsa.gov/cps/cpsfitting/index.cfm",
+            "modified": "2024-05-01",
+            "phone": "202-366-4945",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "http://www.nhtsa.gov/webapi/Default.aspx%3FCSSIStations/Metadata/80"
+            ],
+            "spatial": "Zip, State, Geo co-ordinates",
+            "temporal": "R/2000-01-01/P1D",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "categoryDesignation": "Research",
-            "analysisUnit": "N/A",
-            "phone": "202-366-4945",
-            "language": [
-                "en-US"
-            ]
+            "title": "NHTSA Child Safety Seat Inspection Station Locator - NCSSISL - NHTSA API"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/36uy-g6wc",
-            "issued": "2020-12-10",
             "@type": "dcat:Dataset",
-            "modified": "2020-12-10",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alpha Wingfield",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/36uy-g6wc",
+            "issued": "2020-12-10",
+            "landingPage": "https://data.transportation.gov/d/36uy-g6wc",
+            "modified": "2020-12-10",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "FFF for TRB"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/36vv-umxp",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2025-01-21",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-21",
-            "keyword": [
-                "monthly transportation statistics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:answers@bts.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/36vv-umxp",
             "description": "An estimate of tonnage transported on navigational channels of the United States. Estimates for the most recent month are based on lock performance management data and will be superseded by actual data as it becomes available. The Waterborne Commerce Statistics Center estimates tonnage based on tonnage reported through the lock performance monitoring system.",
-            "title": "U.S. Waterway Tonnage",
+            "identifier": "https://data.transportation.gov/api/views/36vv-umxp",
+            "issued": "2025-01-21",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/36vv-umxp",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-21",
             "programCode": [
                 "021:053"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Research and Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "U.S. Waterway Tonnage"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.infopave.com/",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/research/tfhrc/programs/infrastructure/pavements/ltpp/",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/379j-qyix",
-            "issued": "1993-07-01",
-            "temporal": "R/1993-07-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Research",
             "collectionInstrument": "https://infopave.fhwa.dot.gov",
-            "references": [
-                "https://infopave.fhwa.dot.gov/%3FGoto=Library"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://infopave.fhwa.dot.gov/Page/Index/IMS_USER_GUIDE",
+            "description": "Long-term Pavement performance, construction, traffic, and environmental data for more than 2500 pavement sections in the United States and Canada. More than a dozen experimental designs address specially constructed and existing asphalt and concrete pavements, and maintenance and rehabilitation strategies. Data collection has been on-going since 1990. About one third of the pavement sections are still under study. New warm-mix asphalt concrete pavement overlay sections are currently being recruited and constructed.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "This access point provides access to the LTPP InfoPave data features including section summary report, data selection and download, standard data release, ancillary data selection and download, visual data selection and download, table export and SQL export.",
+                    "downloadURL": "https://infopave.fhwa.dot.gov/%3FGoto=Data",
+                    "mediaType": "text/html",
+                    "title": "Data"
+                }
             ],
+            "identifier": "679.1",
+            "isPartOf": "DOT-679",
+            "issued": "1993-07-01",
             "keyword": [
                 "asphalt concrete",
                 "continuously reinforced concrete pavement",
@@ -3917,64 +3933,38 @@
                 "texture",
                 "traffic loading"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "679.1",
+            "landingPage": "https://data.transportation.gov/d/379j-qyix",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-493-3149",
+            "programCode": [
+                "021:009"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "Long-term Pavement performance, construction, traffic, and environmental data for more than 2500 pavement sections in the United States and Canada. More than a dozen experimental designs address specially constructed and existing asphalt and concrete pavements, and maintenance and rehabilitation strategies. Data collection has been on-going since 1990. About one third of the pavement sections are still under study. New warm-mix asphalt concrete pavement overlay sections are currently being recruited and constructed.",
-            "title": "Long-Term Pavement Performance (LTPP) - Data",
-            "isPartOf": "DOT-679",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/research/tfhrc/programs/infrastructure/pavements/ltpp/",
-            "programCode": [
-                "021:009"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://infopave.fhwa.dot.gov/%3FGoto=Data",
-                    "description": "This access point provides access to the LTPP InfoPave data features including section summary report, data selection and download, standard data release, ancillary data selection and download, visual data selection and download, table export and SQL export.",
-                    "@type": "dcat:Distribution",
-                    "title": "Data"
-                }
+            "references": [
+                "https://infopave.fhwa.dot.gov/%3FGoto=Library"
             ],
-            "describedBy": "https://infopave.fhwa.dot.gov/Page/Index/IMS_USER_GUIDE",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.infopave.com/",
+            "temporal": "R/1993-07-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "phone": "202-493-3149",
-            "language": [
-                "en-US"
-            ]
+            "title": "Long-Term Pavement Performance (LTPP) - Data"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/37uf-u3ey",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/37uf-u3ey",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "CSXT Ownership",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3982,117 +3972,111 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/37uf-u3ey/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/37uf-u3ey/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/37uf-u3ey/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/37uf-u3ey/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/37uf-u3ey/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/37uf-u3ey/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/37uf-u3ey/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/37uf-u3ey/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/37uf-u3ey/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/37uf-u3ey",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/37uf-u3ey",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "CSXT Ownership"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/38mw-dp8u",
-            "issued": "2021-06-30",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-12",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/38mw-dp8u",
+            "issued": "2021-06-30",
+            "landingPage": "https://data.transportation.gov/d/38mw-dp8u",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-08-12",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
-            "title": "NHTSA Recalls by Manufacturer",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "theme": [
                 "Automobiles"
-            ]
+            ],
+            "title": "NHTSA Recalls by Manufacturer"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/38t4-dnq3",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:answers@bts.gov"
+            },
+            "description": "Statistics on the commodities that are exported by US ports via containers.  Applies 2023 USA Trade Online data.",
+            "identifier": "https://data.transportation.gov/api/views/38t4-dnq3",
             "issued": "2024-09-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-03",
             "keyword": [
                 "containerized",
                 "exports",
                 "ports",
                 "supply chain"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:answers@bts.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/38t4-dnq3",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-10-03",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/38t4-dnq3",
-            "description": "Statistics on the commodities that are exported by US ports via containers.  Applies 2023 USA Trade Online data.",
-            "title": "Containerized Exports at US Ports",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
             "theme": [
                 "Maritime and Waterways"
-            ]
+            ],
+            "title": "Containerized Exports at US Ports"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/39cr-5x89",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2021-12-23",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-02",
-            "keyword": [
-                "busstops"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Derald Dudley",
                 "hasEmail": "mailto:NationalTransitMap@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/39cr-5x89",
             "description": "",
-            "title": "National Transit Map - All Stop Locations",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4100,59 +4084,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/39cr-5x89/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/39cr-5x89/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/39cr-5x89/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/39cr-5x89/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/39cr-5x89/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/39cr-5x89/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/39cr-5x89/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/39cr-5x89/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/39cr-5x89/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/39cr-5x89",
+            "issued": "2021-12-23",
+            "keyword": [
+                "busstops"
+            ],
+            "landingPage": "https://data.transportation.gov/d/39cr-5x89",
             "license": "https://creativecommons.org/licenses/by/4.0/",
+            "modified": "2022-02-02",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "National Transit Map - All Stop Locations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/39wk-vhst",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2020-12-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "references": [
-                "https://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/39wk-vhst",
+            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
             "description": "This data is the road section attribute data for HPMS. The HPMS Field Manual and HPMS 8.0 identifies a record by its Data Item.  This data contains approximately 70 data items that is linked to ARNOLD through a Dynamic Segmentation process using the linear referencing components. Table 4.2 contains a list of the current Data Items.",
-            "title": "Roadway Samples 2018",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4160,86 +4145,116 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/39wk-vhst/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/39wk-vhst/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/39wk-vhst/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/39wk-vhst/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/39wk-vhst/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/39wk-vhst/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/39wk-vhst/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/39wk-vhst/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/39wk-vhst/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "USA",
-            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
+            "identifier": "https://data.transportation.gov/api/views/39wk-vhst",
+            "issued": "2020-12-28",
+            "landingPage": "https://data.transportation.gov/d/39wk-vhst",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-05-08",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "references": [
+                "https://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/"
+            ],
+            "spatial": "USA",
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Roadway Samples 2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/39zs-tyww",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2025-01-02",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-02",
-            "keyword": [
-                "monthly transportation statistics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:answers@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/39zs-tyww",
             "description": "Personal spending on gasoline and other energy goods includes spending on motor vehicle fuels, lubricants, and fluids; fuel oil; and other fuels. The Bureau of Economic Analysis estimates personal consumption expenditures, the primary measure of consumer spending on goods and services in the U.S. economy, for each quarter and releases new statistics every month. Quarterly PCE data are seasonally adjusted at annual rates to remove the effects of normal seasonal variation.",
-            "title": "Gasoline and Other Energy Goods - Seasonally Adjusted",
+            "identifier": "https://data.transportation.gov/api/views/39zs-tyww",
+            "issued": "2025-01-02",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/39zs-tyww",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-02",
             "programCode": [
                 "021:053"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Research and Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Gasoline and Other Energy Goods - Seasonally Adjusted"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/3bs4-8sp6",
-            "issued": "1970-01-01",
-            "temporal": "R/1970-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "State Traffic Monitoring Systems (TMS)",
-            "references": [
-                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/06aprtvt/06aprtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "April 2006"
+                }
             ],
+            "identifier": "18.101",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -4249,82 +4264,48 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.101",
+            "landingPage": "https://data.transportation.gov/d/3bs4-8sp6",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-1067",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - April 2006",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/06aprtvt/06aprtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "April 2006"
-                }
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
             ],
             "spatial": "Vehicles by type of functional classified roadway",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "temporal": "R/1970-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
-            "phone": "202-366-1067",
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Traffic Volume Trends - April 2006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/goshrp2/Solutions/All/C01/PlanWorks__Better_planning_Better_projects",
+            "agencyProgramURL": "https://fhwaapps.fhwa.dot.gov/planworks/",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/3c7z-wpk5",
-            "issued": "2014-12-29",
-            "temporal": "2014-12-29/2014-12-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "collaboration",
-                "decision",
-                "fhwa",
-                "planning",
-                "policy",
-                "transportation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "717.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "PlanWorks is a Web resource that supports collaborative decision making in transportation planning and project development. PlanWorks is built around key decision points in long-range planning, programming, corridor planning, and environmental review. PlanWorks suggests when and how to engage cross-disciplinary partners and stakeholder groups. PlanWorks has four major components:-A troubleshooting guide describing the common decision points and opportunities for cooperation in the transportation planning and environmental review process. For each of the key decision points, PlanWorks provides policy and stakeholder questions, data needs, case studies and examples, and links to tools that can help support the decision.-Interactive assessments that enable project stakeholders to identify opportunities to work together, improve interagency cooperation, and expedite project delivery.",
-            "title": "PlanWorks - PlanWorks: Better Planning. Better Projects",
-            "isPartOf": "DOT-717",
-            "agencyProgramURL": "https://fhwaapps.fhwa.dot.gov/planworks/",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4333,157 +4314,155 @@
                     "title": "PlanWorks: Better Planning. Better Projects"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "717.1",
+            "isPartOf": "DOT-717",
+            "issued": "2014-12-29",
+            "keyword": [
+                "collaboration",
+                "decision",
+                "fhwa",
+                "planning",
+                "policy",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/3c7z-wpk5",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-2048",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "temporal": "2014-12-29/2014-12-29",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/goshrp2/Solutions/All/C01/PlanWorks__Better_planning_Better_projects",
-            "categoryDesignation": "Research",
-            "phone": "202-366-2048",
-            "language": [
-                "en-US"
-            ]
+            "title": "PlanWorks - PlanWorks: Better Planning. Better Projects"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/3e5h-rxb3",
-            "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
-            "keyword": [
-                "aadt",
-                "condition",
-                "highway",
-                "iri",
-                "ownership",
-                "pavement",
-                "performance",
-                "traffic",
-                "travel",
-                "use",
-                "vmt"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "678.45",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": false,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
             "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Texas",
-            "isPartOf": "DOT-678",
-            "primaryITInvestmentUII": "021-099281808",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/texas2011.zip",
-                    "description": "2011 Texas HPMS Shapefile",
                     "@type": "dcat:Distribution",
+                    "description": "2011 Texas HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/texas2011.zip",
+                    "mediaType": "application/zip",
                     "title": "2011 Texas"
                 }
             ],
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "678.45",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
+            "keyword": [
+                "aadt",
+                "condition",
+                "highway",
+                "iri",
+                "ownership",
+                "pavement",
+                "performance",
+                "traffic",
+                "travel",
+                "use",
+                "vmt"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
-            "categoryDesignation": "Administrative",
+            "landingPage": "https://data.transportation.gov/d/3e5h-rxb3",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-5035"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5035",
+            "primaryITInvestmentUII": "021-099281808",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "temporal": "R/1981-11-01/P1Y",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Texas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/3eq6-c7tv",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2025-01-02",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-02",
-            "keyword": [
-                "monthly transportation statistics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:answers@bts.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/3eq6-c7tv",
             "description": "Unemployment rate is the number of unemployed persons as a percent of the labor force. The Bureau of Labor Statistics produces industry estimates of nonfarm payroll employment as part of the Current Population Survey. Employment data are seasonally adjusted to remove the effects of normal seasonal variation.",
-            "title": "Unemployment Rate - Seasonally Adjusted",
+            "identifier": "https://data.transportation.gov/api/views/3eq6-c7tv",
+            "issued": "2025-01-02",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/3eq6-c7tv",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-02",
             "programCode": [
                 "021:053"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Research and Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Unemployment Rate - Seasonally Adjusted"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "ftp://ftp.nhtsa.dot.gov/GES/",
+            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/3fpd-9nx4",
-            "issued": "1988-12-31",
-            "temporal": "R/1988-01-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType"
-            ],
-            "keyword": [
-                "crashworthiness",
-                "estimation",
-                "fars",
-                "general",
-                "nass",
-                "system"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "524.14",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
             "description": "STATE DATA REPORTING SYSTEMS. Annual reports on the Fatality Analysis Reporting System (FARS) which is data regarding fatalities that is collected by a FARS analyst from each State and provided to NHTSA.",
-            "title": "GES Reports - 1998",
-            "isPartOf": "DOT-524",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4492,32 +4471,71 @@
                     "title": "1998"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
-            "dataQuality": true,
+            "identifier": "524.14",
+            "isPartOf": "DOT-524",
+            "issued": "1988-12-31",
+            "keyword": [
+                "crashworthiness",
+                "estimation",
+                "fars",
+                "general",
+                "nass",
+                "system"
+            ],
+            "landingPage": "https://data.transportation.gov/d/3fpd-9nx4",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "ftp://ftp.nhtsa.dot.gov/GES/",
+            "modified": "2024-05-01",
+            "phone": "202-366-4998",
+            "programCode": [
+                "021:032"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType"
+            ],
+            "spatial": "Point",
+            "temporal": "R/1988-01-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Administrative",
-            "phone": "202-366-4998",
-            "language": [
-                "en-US"
-            ]
+            "title": "GES Reports - 1998"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/3g5d-epk7",
-            "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": false,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
+            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "2013 Georgia HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/georgia2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Georgia"
+                }
+            ],
+            "identifier": "678.114",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -4531,105 +4549,69 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.114",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Georgia",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/3g5d-epk7",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5035",
             "primaryITInvestmentUII": "021-099281808",
             "programCode": [
                 "021:009"
             ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/georgia2013.zip",
-                    "description": "2013 Georgia HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Georgia"
-                }
-            ],
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "temporal": "R/1981-11-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
-            "categoryDesignation": "Administrative",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-5035"
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Georgia"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/3g63-ik4u",
-            "issued": "2020-09-23",
             "@type": "dcat:Dataset",
-            "modified": "2023-06-02",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
+            "description": "Estimates the vehicle miles traveled (VMT) for interstate highways and how the total travel measured by VMT compares with travel that occurred in the same week of the previous year.",
             "identifier": "https://data.transportation.gov/api/views/3g63-ik4u",
+            "issued": "2020-09-23",
+            "landingPage": "https://data.transportation.gov/d/3g63-ik4u",
+            "modified": "2023-06-02",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "Estimates the vehicle miles traveled (VMT) for interstate highways and how the total travel measured by VMT compares with travel that occurred in the same week of the previous year.",
-            "title": "Weekly Traffic Volume Report",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "Weekly Traffic Volume Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/motorfuelhwy_trustfund.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/motorfueldata.cfm",
+            "analysisUnit": "Gallons",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/3hgd-fes4",
-            "issued": "1998-01-01",
-            "temporal": "R/1998-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative - Financial",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.fhwa.dot.gov/policyinformation/hss/guide"
-            ],
-            "keyword": [
-                "diesel",
-                "fuel tax",
-                "gallons",
-                "gasoline",
-                "motor fuel"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "DOT-698",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hss/guide/ch2.cfm",
             "description": "On a monthly basis, each State is required to report to the Federal Highway Administration (FHWA), the amount of gallons taxed by that state. This data is analyzed and compiled by FHWA staff. The data on the amount of on-highway fuel use for each State is then used to attribute federal revenue to each State. Yearly, the FHWA, Office of Policy, provides data from the previous year's data for use in the attribution process. The previous year data is used to provide States added time to review, allowing them to verify that the data report is correct and ready to be used in attribution.",
-            "title": "Monthly Motor Fuel",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/motorfueldata.cfm",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4638,36 +4620,70 @@
                     "title": "Monthly Motor Fuel Reports"
                 }
             ],
-            "spatial": "National, State",
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hss/guide/ch2.cfm",
-            "dataQuality": true,
+            "identifier": "DOT-698",
+            "issued": "1998-01-01",
+            "keyword": [
+                "diesel",
+                "fuel tax",
+                "gallons",
+                "gasoline",
+                "motor fuel"
+            ],
+            "landingPage": "https://data.transportation.gov/d/3hgd-fes4",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/motorfuelhwy_trustfund.cfm",
+            "modified": "2024-05-08",
+            "phone": "202-366-5026",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "references": [
+                "http://www.fhwa.dot.gov/policyinformation/hss/guide"
+            ],
+            "spatial": "National, State",
+            "temporal": "R/1998-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative - Financial",
-            "analysisUnit": "Gallons",
-            "phone": "202-366-5026",
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Motor Fuel"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/FLAT_RCL.zip",
+            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
+            "analysisUnit": "Vehicles , Tires, Child Safety Seats, Equipment",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/3hpp-hxtf",
-            "issued": "2002-12-16",
-            "temporal": "R/1949-01-01/P1D",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "N/A",
-            "modified": "2024-05-01",
-            "references": [
-                "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/RCL.txt"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/RCL.txt",
+            "describedByType": "text/plain",
+            "description": "Manufacturers who determine that a product or piece of original equipment either has a safety defect or is not in compliance with Federal safety standards are required to notify the National Highway Traffic Safety Administration (NHTSA) within 5 business days. NHTSA requires that manufacturers file a Defect and Noncompliance report as well as quarterly recall status reports, in compliance with Federal Regulation 49 (the National Traffic and Motor Safety Act) Part 573, which identifies the requirements for safety recalls. This information is stored in the NHTSA database. Use this data to search for recall information related to:-\tSpecific NHTSA campaigns -\tProduct types Access to public searches of NHTSA recall databases for tires, vehicles, car seats and equipment.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/FLAT_RCL.zip",
+                    "mediaType": "application/zip",
+                    "title": "Recalls Flat File"
+                }
             ],
+            "identifier": "DOT-83",
+            "issued": "2002-12-16",
             "keyword": [
                 "air bag",
                 "air bags",
@@ -4694,89 +4710,43 @@
                 "vin",
                 "vin search"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "DOT-83",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Manufacturers who determine that a product or piece of original equipment either has a safety defect or is not in compliance with Federal safety standards are required to notify the National Highway Traffic Safety Administration (NHTSA) within 5 business days. NHTSA requires that manufacturers file a Defect and Noncompliance report as well as quarterly recall status reports, in compliance with Federal Regulation 49 (the National Traffic and Motor Safety Act) Part 573, which identifies the requirements for safety recalls. This information is stored in the NHTSA database. Use this data to search for recall information related to:-\tSpecific NHTSA campaigns -\tProduct types Access to public searches of NHTSA recall databases for tires, vehicles, car seats and equipment.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls",
-            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
-            "describedByType": "text/plain",
+            "landingPage": "https://data.transportation.gov/d/3hpp-hxtf",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-2315",
             "primaryITInvestmentUII": "021-777552743",
             "programCode": [
                 "021:035"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/FLAT_RCL.zip",
-                    "mediaType": "application/zip",
-                    "title": "Recalls Flat File"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/RCL.txt"
             ],
             "spatial": "N/A",
-            "describedBy": "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/RCL.txt",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/FLAT_RCL.zip",
+            "temporal": "R/1949-01-01/P1D",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Vehicles , Tires, Child Safety Seats, Equipment",
-            "phone": "202-366-2315",
-            "language": [
-                "en-US"
-            ]
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/3i8a-8wnf",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2024-09-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
-            "keyword": [
-                "connected equipment",
-                "connected vehicle",
-                "connected vehicle data",
-                "connected vehicle environment",
-                "connected vehicle message",
-                "connected vehicles",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "on-board equipment",
-                "on-board unit",
-                "roadside equipment",
-                "road side unit",
-                "vehicle data",
-                "vehicle to infrastructure",
-                "vehicle to vehicle"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kate Hartman",
                 "hasEmail": "mailto:kate.hartman@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/3i8a-8wnf",
             "description": "WFCW-3 FCW Slow Moving Vehicle Rep 2",
-            "title": "LTE-V2X Wyoming Connected Vehicle Pilot test ID WFCW-3 Rep 2",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4784,73 +4754,81 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/3i8a-8wnf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/3i8a-8wnf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/3i8a-8wnf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/3i8a-8wnf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/3i8a-8wnf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/3i8a-8wnf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/3i8a-8wnf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/3i8a-8wnf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/3i8a-8wnf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Wyoming",
+            "identifier": "https://data.transportation.gov/api/views/3i8a-8wnf",
+            "issued": "2024-09-06",
+            "keyword": [
+                "connected equipment",
+                "connected vehicle",
+                "connected vehicle data",
+                "connected vehicle environment",
+                "connected vehicle message",
+                "connected vehicles",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "on-board equipment",
+                "on-board unit",
+                "roadside equipment",
+                "road side unit",
+                "vehicle data",
+                "vehicle to infrastructure",
+                "vehicle to vehicle"
+            ],
+            "landingPage": "https://data.transportation.gov/d/3i8a-8wnf",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-07",
+            "programCode": [
+                "021:042"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "spatial": "Wyoming",
             "theme": [
                 "Automobiles"
-            ]
+            ],
+            "title": "LTE-V2X Wyoming Connected Vehicle Pilot test ID WFCW-3 Rep 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/3j6s-p6g8",
-            "issued": "1970-01-01",
-            "temporal": "R/1970-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "State Traffic Monitoring Systems (TMS)",
-            "references": [
-                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
-            ],
-            "keyword": [
-                "aadt",
-                "'fhwa",
-                "traffic volume trends",
-                "tvt",
-                "vehicle miles traveled",
-                "vmt",
-                "volume data"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "18.152",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - January 2002",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4859,35 +4837,74 @@
                     "title": "January 2002"
                 }
             ],
-            "spatial": "Vehicles by type of functional classified roadway",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
-            "theme": [
-                "Transportation"
+            "identifier": "18.152",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
+            "keyword": [
+                "aadt",
+                "'fhwa",
+                "traffic volume trends",
+                "tvt",
+                "vehicle miles traveled",
+                "vmt",
+                "volume data"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
-            "phone": "202-366-1067",
+            "landingPage": "https://data.transportation.gov/d/3j6s-p6g8",
             "language": [
                 "en-US"
-            ]
-        },
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-1067",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
+            ],
+            "spatial": "Vehicles by type of functional classified roadway",
+            "temporal": "R/1970-01-01/P1M",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Monthly Traffic Volume Trends - January 2002"
+        },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/FLAT_RCL.zip",
+            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
+            "analysisUnit": "Vehicles , Tires, Child Safety Seats, Equipment",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/3j8r-p6nv",
-            "issued": "2002-12-16",
-            "temporal": "R/1949-01-01/P1D",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "N/A",
-            "modified": "2024-05-01",
-            "references": [
-                "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/RCL.txt"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/RCL.txt",
+            "describedByType": "text/plain",
+            "description": "Manufacturers who determine that a product or piece of original equipment either has a safety defect or is not in compliance with Federal safety standards are required to notify the National Highway Traffic Safety Administration (NHTSA) within 5 business days. NHTSA requires that manufacturers file a Defect and Noncompliance report as well as quarterly recall status reports, in compliance with Federal Regulation 49 (the National Traffic and Motor Safety Act) Part 573, which identifies the requirements for safety recalls. This information is stored in the NHTSA database. Use this data to search for recall information related to:-\tSpecific NHTSA campaigns -\tProduct types Access to public searches of NHTSA recall databases for tires, vehicles, car seats and equipment.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www-odi.nhtsa.dot.gov/owners/SearchSafetyIssues%3FprodType=C",
+                    "mediaType": "text/html",
+                    "title": "Recalls - Car Seats"
+                }
             ],
+            "identifier": "83.12",
+            "isPartOf": "DOT-83",
+            "issued": "2002-12-16",
             "keyword": [
                 "air bag",
                 "air bags",
@@ -4914,63 +4931,61 @@
                 "vin",
                 "vin search"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "83.12",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Manufacturers who determine that a product or piece of original equipment either has a safety defect or is not in compliance with Federal safety standards are required to notify the National Highway Traffic Safety Administration (NHTSA) within 5 business days. NHTSA requires that manufacturers file a Defect and Noncompliance report as well as quarterly recall status reports, in compliance with Federal Regulation 49 (the National Traffic and Motor Safety Act) Part 573, which identifies the requirements for safety recalls. This information is stored in the NHTSA database. Use this data to search for recall information related to:-\tSpecific NHTSA campaigns -\tProduct types Access to public searches of NHTSA recall databases for tires, vehicles, car seats and equipment.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - Recalls - Car Seats",
-            "isPartOf": "DOT-83",
-            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
-            "describedByType": "text/plain",
+            "landingPage": "https://data.transportation.gov/d/3j8r-p6nv",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-0154",
             "primaryITInvestmentUII": "021-777552743",
             "programCode": [
                 "021:035"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www-odi.nhtsa.dot.gov/owners/SearchSafetyIssues%3FprodType=C",
-                    "mediaType": "text/html",
-                    "title": "Recalls - Car Seats"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/RCL.txt"
             ],
             "spatial": "N/A",
-            "describedBy": "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/RCL.txt",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/FLAT_RCL.zip",
+            "temporal": "R/1949-01-01/P1D",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Vehicles , Tires, Child Safety Seats, Equipment",
-            "phone": "202-366-0154",
-            "language": [
-                "en-US"
-            ]
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - Recalls - Car Seats"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/PT1S",
+            "agencyDataSeriesURL": "http://www.nhtsa.gov/Vehicle+Safety",
+            "agencyProgramURL": "http://vpic.nhtsa.dot.gov/",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/3jdz-9gqq",
-            "issued": "2015-10-05",
-            "temporal": "R/2015-10-05/PT1S",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Administrative - Regulatory",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://vpic.nhtsa.dot.gov/"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The NHTSA Product Information Catalog and Vehicle Listing (vPIC) is a consolidated platform that presents data collected within the manufacturer reported data from CFR 49 Parts 551 - 574 for use in a variety of modern tools. NHTSA's vPIC platform is intended to serve as a centralized source for basic Vehicle Identification Number (VIN) decoding, Manufacturer Information Database (MID), Manufacturer Equipment Plant Identification and associated data. vPIC is intended to support the Open Data and Transparency initiatives of the agency by allowing the data to be freely used by the public without the burden of manual retrieval from a library of electronic documents (PDFs). While these documents will still be available online for viewing within the Manufacturer Information Database (MID) module of vPIC one can view and use the actual data through the VIN Decoder and Application Programming Interface (API) modules.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "APIs for use by developers, programmers or researchers interested in obtaining raw Vehicle or Manufacturer data from vPIC.",
+                    "downloadURL": "http://vpic.nhtsa.dot.gov/api/",
+                    "mediaType": "application/jsv",
+                    "title": "Vehicle API JSV"
+                }
             ],
+            "identifier": "65.7",
+            "isPartOf": "DOT-65",
+            "issued": "2015-10-05",
             "keyword": [
                 "49",
                 "551",
@@ -5007,56 +5022,45 @@
                 "vin",
                 "vpic"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "65.7",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "The NHTSA Product Information Catalog and Vehicle Listing (vPIC) is a consolidated platform that presents data collected within the manufacturer reported data from CFR 49 Parts 551 - 574 for use in a variety of modern tools. NHTSA's vPIC platform is intended to serve as a centralized source for basic Vehicle Identification Number (VIN) decoding, Manufacturer Information Database (MID), Manufacturer Equipment Plant Identification and associated data. vPIC is intended to support the Open Data and Transparency initiatives of the agency by allowing the data to be freely used by the public without the burden of manual retrieval from a library of electronic documents (PDFs). While these documents will still be available online for viewing within the Manufacturer Information Database (MID) module of vPIC one can view and use the actual data through the VIN Decoder and Application Programming Interface (API) modules.",
-            "title": "NHTSA Product Information Catalog and Vehicle Listing (vPIC) - Vehicle API JSV",
-            "isPartOf": "DOT-65",
-            "agencyProgramURL": "http://vpic.nhtsa.dot.gov/",
+            "landingPage": "https://data.transportation.gov/d/3jdz-9gqq",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-01",
+            "phone": "202-366-2622",
             "primaryITInvestmentUII": "021-430297065",
             "programCode": [
                 "021:031"
             ],
-            "distribution": [
-                {
-                    "mediaType": "application/jsv",
-                    "downloadURL": "http://vpic.nhtsa.dot.gov/api/",
-                    "description": "APIs for use by developers, programmers or researchers interested in obtaining raw Vehicle or Manufacturer data from vPIC.",
-                    "@type": "dcat:Distribution",
-                    "title": "Vehicle API JSV"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "http://vpic.nhtsa.dot.gov/"
             ],
             "spatial": "NA",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.nhtsa.gov/Vehicle+Safety",
+            "temporal": "R/2015-10-05/PT1S",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/PT1S",
-            "categoryDesignation": "Administrative - Regulatory",
-            "phone": "202-366-2622",
-            "language": [
-                "en-US"
-            ]
+            "title": "NHTSA Product Information Catalog and Vehicle Listing (vPIC) - Vehicle API JSV"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:36"
             ],
-            "landingPage": "https://data.transportation.gov/d/3ksw-c9bv",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NTD Program Support",
+                "hasEmail": "mailto:NTDHelp@dot.gov"
+            },
+            "description": "A national summary of key transit performance metrics based on data reported by transit agencies to the National Transit Database (NTD) in Report Year 2023.\r\n\r\nNTD Data Summaries organize and summarize data from the 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. \r\n\r\nThis summary is based on the 2023 Service, Operating Expenses, and Federal Funding Allocation database files on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
+            "identifier": "https://data.transportation.gov/api/views/3ksw-c9bv",
             "issued": "2024-10-16",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-17",
             "keyword": [
                 "cost per hour",
                 "cost per trip",
@@ -5064,51 +5068,30 @@
                 "mile per trip",
                 "transit fares"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NTD Program Support",
-                "hasEmail": "mailto:NTDHelp@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/3ksw-c9bv",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-10-17",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Transit Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/3ksw-c9bv",
-            "description": "A national summary of key transit performance metrics based on data reported by transit agencies to the National Transit Database (NTD) in Report Year 2023.\r\n\r\nNTD Data Summaries organize and summarize data from the 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. \r\n\r\nThis summary is based on the 2023 Service, Operating Expenses, and Federal Funding Allocation database files on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
-            "title": "2023 NTD Annual Data Summary - Metrics",
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "2023 NTD Annual Data Summary - Metrics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/3kum-6vpd",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-12-18",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-29",
-            "keyword": [
-                "county",
-                "demand response",
-                "geographic",
-                "geospatial",
-                "public transit"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NTD Program Support",
                 "hasEmail": "mailto:NTDHelp@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Transit Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/3kum-6vpd",
             "description": "This dataset details places and counties served by Demand Response (DR) modes for each applicable agency and type of service (TOS) reported to the National Transit Database for Report Year 2023.\n\nNTD Data Tables organize and summarize data from the 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. \n\nThis data is a part of new reporting requirements as of 2023. Other datasets describing aspects of Demand Response Geographical Area Coverage can be found at the following links:\nPassenger Eligibility and Requirements: https://data.transportation.gov/dataset/Demand-Response-Geographic-Area-Coverage-Passenger/h9qc-expu/about_data\nService Schedules: https://data.transportation.gov/dataset/Demand-Response-Geographic-Area-Coverage-Service-S/4p55-emkp/about_data\n\nIf you have any other questions about this table, please contact the NTD Help Desk at NTDHelp@dot.gov.",
-            "title": "2023 NTD Annual Data - Demand Response Geographic Area Coverage (Counties and Places)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5116,71 +5099,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/3kum-6vpd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/3kum-6vpd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/3kum-6vpd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/3kum-6vpd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/3kum-6vpd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/3kum-6vpd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/3kum-6vpd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/3kum-6vpd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/3kum-6vpd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/3kum-6vpd",
+            "issued": "2024-12-18",
+            "keyword": [
+                "county",
+                "demand response",
+                "geographic",
+                "geospatial",
+                "public transit"
+            ],
+            "landingPage": "https://data.transportation.gov/d/3kum-6vpd",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-29",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Transit Administration"
+            },
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "2023 NTD Annual Data - Demand Response Geographic Area Coverage (Counties and Places)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/3m3f-mtsf",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2024-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-28",
-            "keyword": [
-                "connected equipment",
-                "connected vehicle",
-                "connected vehicle data",
-                "connected vehicle environment",
-                "connected vehicle message",
-                "connected vehicles",
-                "on-board equipment",
-                "on-board unit",
-                "roadside equipment",
-                "road side unit",
-                "vehicle data",
-                "vehicle to infrastructure",
-                "vehicle to vehicle"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kate Hartman",
                 "hasEmail": "mailto:kate.hartman@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/3m3f-mtsf",
             "description": "Part of Wyoming Department of Transportation Connected Vehicle Pilot Phase 4. Verify that OBUs use different LTE-V2X Configuration Profiles based on the vehicle's speed.\nHost and remote vehicles travelling below 120 kmph\nHost and remote vehicles travelling above 120 kmph",
-            "title": "LTE-V2X Wyoming Connected Vehicle Pilot test ID WV2IMCT-1 Vehicle 1 80 mph",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5188,64 +5160,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/3m3f-mtsf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/3m3f-mtsf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/3m3f-mtsf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/3m3f-mtsf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/3m3f-mtsf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/3m3f-mtsf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/3m3f-mtsf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/3m3f-mtsf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/3m3f-mtsf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Wyoming",
+            "identifier": "https://data.transportation.gov/api/views/3m3f-mtsf",
+            "issued": "2024-07-19",
+            "keyword": [
+                "connected equipment",
+                "connected vehicle",
+                "connected vehicle data",
+                "connected vehicle environment",
+                "connected vehicle message",
+                "connected vehicles",
+                "on-board equipment",
+                "on-board unit",
+                "roadside equipment",
+                "road side unit",
+                "vehicle data",
+                "vehicle to infrastructure",
+                "vehicle to vehicle"
+            ],
+            "landingPage": "https://data.transportation.gov/d/3m3f-mtsf",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-09-28",
+            "programCode": [
+                "021:042"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "spatial": "Wyoming",
             "theme": [
                 "Automobiles"
-            ]
+            ],
+            "title": "LTE-V2X Wyoming Connected Vehicle Pilot test ID WV2IMCT-1 Vehicle 1 80 mph"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2022-07-07",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "highway",
-                "highway performance monitoring",
-                "highway performance monitoring system",
-                "highways",
-                "hpms"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/3n3x-bbb4",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 1995",
-            "title": "Historic HPMS Data (Universe) - 1995",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5253,74 +5234,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/3n3x-bbb4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/3n3x-bbb4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/3n3x-bbb4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/3n3x-bbb4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/3n3x-bbb4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/3n3x-bbb4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/3n3x-bbb4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/3n3x-bbb4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/3n3x-bbb4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/3n3x-bbb4",
+            "issued": "2022-07-07",
+            "keyword": [
+                "highway",
+                "highway performance monitoring",
+                "highway performance monitoring system",
+                "highways",
+                "hpms"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-08",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
             "spatial": "United States",
-            "dataQuality": true,
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Historic HPMS Data (Universe) - 1995"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "rights": "Personal privacy information has been redacted based on FOIA Exemption 6",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.dot.gov/foia/foia-electronic-reading-room-category-four",
+            "agencyProgramURL": "http://www.dot.gov/foia",
+            "analysisUnit": "FOIA Request",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/3nq5-bp29",
-            "issued": "2007-12-31",
-            "temporal": "R/2007-01-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.dot.gov/sites/dot.gov/files/docs/Responding%20to%20FOIA%20Requests%20for%20FOIA%20Case%20Logs_04_2008.pdf"
-            ],
-            "keyword": [
-                "foia",
-                "freedom of information act",
-                "log",
-                "request"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "373.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": true,
             "description": "Each Freedom of Information Act office uses a case log to track FOIA requests. The logs typically include the dates on which requests were received and closed, control numbers, requester names and descriptions of the requested records.",
-            "title": "Freedom of Information Act Logs for the Office of the Secretary of Transportation - 2007",
-            "isPartOf": "DOT-373",
-            "agencyProgramURL": "http://www.dot.gov/foia",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5329,57 +5309,58 @@
                     "title": "2007"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "373.1",
+            "isPartOf": "DOT-373",
+            "issued": "2007-12-31",
+            "keyword": [
+                "foia",
+                "freedom of information act",
+                "log",
+                "request"
+            ],
+            "landingPage": "https://data.transportation.gov/d/3nq5-bp29",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.dot.gov/foia/foia-electronic-reading-room-category-four",
+            "modified": "2024-11-14",
+            "phone": "202-366-5546",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "references": [
+                "http://www.dot.gov/sites/dot.gov/files/docs/Responding%20to%20FOIA%20Requests%20for%20FOIA%20Case%20Logs_04_2008.pdf"
+            ],
+            "rights": "Personal privacy information has been redacted based on FOIA Exemption 6",
+            "spatial": "N/A",
+            "temporal": "R/2007-01-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "analysisUnit": "FOIA Request",
-            "phone": "202-366-5546",
-            "language": [
-                "en-US"
-            ]
+            "title": "Freedom of Information Act Logs for the Office of the Secretary of Transportation - 2007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://hepgis.fhwa.dot.gov/hepgismaps11/#",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/3q2p-n887",
-            "issued": "2007-01-01",
-            "temporal": "2007-01-01/2014-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Geospatial",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "arra planning",
-                "fhwa",
-                "geographic",
-                "geospatial",
-                "map"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "692.10",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - Draft National Primary Freight Network",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "primaryITInvestmentUII": "021-845083703",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5388,51 +5369,51 @@
                     "title": "Draft National Primary Freight Network"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.10",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/3q2p-n887",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://hepgis.fhwa.dot.gov/hepgismaps11/#",
+            "modified": "2024-05-08",
+            "phone": "708-283-3554",
+            "primaryITInvestmentUII": "021-845083703",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "spatial": "National, State, County",
+            "temporal": "2007-01-01/2014-12-31",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Geospatial",
-            "phone": "708-283-3554",
-            "language": [
-                "en-US"
-            ]
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - Draft National Primary Freight Network"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/3qgg-2u2a",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2022-05-03",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-21",
-            "keyword": [
-                "gas tax",
-                "motor fuel",
-                "revenue",
-                "sales tax",
-                "taxes"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/3qgg-2u2a",
             "description": "Monthly state sales tax collections is an experimental dataset published by the U.S. Census Bureau. It provides data for collections from sales taxes including motor fuel taxes. Data reported for a specific month generally represent sales taxes collected on sales made during the prior month.\n\nTax collections primarily rely on unaudited data collected from existing state reports or state data sources available from and posted on the Internet. Secondarily, states report the data via the Quarterly Survey of State and Local Tax Revenue. Data are updated monthly, but due to differing reporting cycles data for some states may lag.",
-            "title": "Sales Tax Collections by State",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5440,48 +5421,82 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/3qgg-2u2a/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/3qgg-2u2a/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/3qgg-2u2a/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/3qgg-2u2a/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/3qgg-2u2a/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/3qgg-2u2a/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/3qgg-2u2a/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/3qgg-2u2a/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/3qgg-2u2a/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/3qgg-2u2a",
+            "issued": "2022-05-03",
+            "keyword": [
+                "gas tax",
+                "motor fuel",
+                "revenue",
+                "sales tax",
+                "taxes"
+            ],
+            "landingPage": "https://data.transportation.gov/d/3qgg-2u2a",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2024-08-21",
+            "phone": "202-366-DATA(3282) ",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282) "
+            "title": "Sales Tax Collections by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/3rrh-sazm",
-            "issued": "1970-01-01",
-            "temporal": "R/1970-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "State Traffic Monitoring Systems (TMS)",
-            "references": [
-                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/06novtvt/06novtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "November 2006"
+                }
             ],
+            "identifier": "18.94",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -5491,82 +5506,49 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.94",
+            "landingPage": "https://data.transportation.gov/d/3rrh-sazm",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-1067",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - November 2006",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/06novtvt/06novtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "November 2006"
-                }
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
             ],
             "spatial": "Vehicles by type of functional classified roadway",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "temporal": "R/1970-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
-            "phone": "202-366-1067",
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Traffic Volume Trends - November 2006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://mutcd.fhwa.dot.gov/orsearch.asp",
+            "agencyProgramURL": "http://mutcd.fhwa.dot.gov",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/3s6b-tub8",
-            "issued": "2011-06-01",
-            "temporal": "2011-06-01/2014-12-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://mutcd.fhwa.dot.gov/orsearch.asp"
-            ],
-            "keyword": [
-                "experiment",
-                "interpretation",
-                "mutcd",
-                "official ruling"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "DOT-694",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": false,
+            "describedBy": "http://mutcd.fhwa.dot.gov/orsearch.asp",
             "description": "The MUTCD Official Rulings is a resource that allows web site visitors to obtain information about requests for changes, experiments, and interpretations related to the MUTCD that have been received by the FHWA. Copies of various documents (such as incoming request letters, response letters from the FHWA, progress reports, and final reports) that are available in both pdf and html formats may be viewed on this web site. The current status of experiments, as well as any contact information for the requestor that has been made a part of the public record, is also available.",
-            "title": "Manual on Uniform Traffic Control Devices (MUTCD)",
-            "agencyProgramURL": "http://mutcd.fhwa.dot.gov",
-            "programCode": [
-                "021:011"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5575,34 +5557,67 @@
                     "title": "Search Official Rulings"
                 }
             ],
-            "describedBy": "http://mutcd.fhwa.dot.gov/orsearch.asp",
-            "dataQuality": false,
+            "identifier": "DOT-694",
+            "issued": "2011-06-01",
+            "keyword": [
+                "experiment",
+                "interpretation",
+                "mutcd",
+                "official ruling"
+            ],
+            "landingPage": "https://data.transportation.gov/d/3s6b-tub8",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://mutcd.fhwa.dot.gov/orsearch.asp",
+            "modified": "2024-05-08",
+            "phone": "202-366-8043",
+            "programCode": [
+                "021:011"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "references": [
+                "http://mutcd.fhwa.dot.gov/orsearch.asp"
+            ],
+            "temporal": "2011-06-01/2014-12-29",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "phone": "202-366-8043",
-            "language": [
-                "en-US"
-            ]
+            "title": "Manual on Uniform Traffic Control Devices (MUTCD)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/3sff-ymj6",
-            "issued": "1970-01-01",
-            "temporal": "R/1970-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "State Traffic Monitoring Systems (TMS)",
-            "references": [
-                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/06juntvt/06juntvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "June 2006"
+                }
             ],
+            "identifier": "18.99",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -5612,121 +5627,78 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.99",
+            "landingPage": "https://data.transportation.gov/d/3sff-ymj6",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-1067",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - June 2006",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/06juntvt/06juntvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "June 2006"
-                }
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
             ],
             "spatial": "Vehicles by type of functional classified roadway",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "temporal": "R/1970-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
-            "phone": "202-366-1067",
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Traffic Volume Trends - June 2006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/3tj4-7wf5",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2020-03-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
-            "keyword": [
-                "transportation economics",
-                "transportation spending"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/3tj4-7wf5",
             "description": "Economic concepts related to transportation spending.",
-            "title": "Transportation Economic  Concepts: Transportation Spending",
+            "identifier": "https://data.transportation.gov/api/views/3tj4-7wf5",
+            "issued": "2020-03-02",
+            "keyword": [
+                "transportation economics",
+                "transportation spending"
+            ],
+            "landingPage": "https://data.transportation.gov/d/3tj4-7wf5",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-18",
+            "phone": "202-366-DATA(3282)",
             "programCode": [
                 "021:053"
             ],
-            "license": "https://www.usa.gov/government-works",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Transportation Economic  Concepts: Transportation Spending"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/3trh-hz5x",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2015-01-31",
-            "@type": "dcat:Dataset",
-            "temporal": "2014-09-08/2014-09-10",
-            "modified": "2015-01-31",
-            "keyword": [
-                "2014 its world congress (itswc) connected vehicle (cv) test bed demonstration",
-                "application message",
-                "arterial",
-                "connected equipment",
-                "connected vehicle message",
-                "detroit",
-                "field test",
-                "intelligent transportation systems (its)",
-                "intersection situation data (isd)",
-                "its joint program office (jpo)",
-                "its world congress",
-                "map",
-                "michigan",
-                "signal phase and timing (spat)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kate Hartman",
                 "hasEmail": "mailto:kate.hartman@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "USDOT"
-            },
-            "identifier": "https://data.transportation.gov/api/views/3trh-hz5x",
+            "dataQuality": true,
             "description": "During the 2014 ITS World Congress a demonstration of the connected vehicle infrastructure in the City of Detroit was conducted.  The test site included approximately 14 intersections around Detroit\u2019s COBO convention center and involved 9 equipped vehicles.Intersection Situation Data (ISD) data set communicates MAP and signal phase and timing (SPaT) information. MAP information communicates an intersection\u2019s location (latitude and longitude), elevation, and geometric features such as approaches and lane configuration. SPaT data communicates the (current) state of the intersection\u2019s signal indication(s). The data is composed of discrete Row Groups. A Row Group is a collection of (approximately 3-4) consecutive rows with common attribute.\r\n\r\nNOTE: All Extra Files are attached in 2014 ITS World Congress Connected Vehicle Test Bed Demonstration Vehicle Situation Data",
-            "title": "2014 ITS World Congress Connected Vehicle Test Bed Demonstration Intersection Situation Data",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5734,133 +5706,177 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/3trh-hz5x/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/3trh-hz5x/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/3trh-hz5x/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/3trh-hz5x/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/3trh-hz5x/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/3trh-hz5x/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/3trh-hz5x/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/3trh-hz5x/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/3trh-hz5x/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Detroit, Michigan",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/3trh-hz5x",
+            "issued": "2015-01-31",
+            "keyword": [
+                "2014 its world congress (itswc) connected vehicle (cv) test bed demonstration",
+                "application message",
+                "arterial",
+                "connected equipment",
+                "connected vehicle message",
+                "detroit",
+                "field test",
+                "intelligent transportation systems (its)",
+                "intersection situation data (isd)",
+                "its joint program office (jpo)",
+                "its world congress",
+                "map",
+                "michigan",
+                "signal phase and timing (spat)"
+            ],
+            "landingPage": "https://data.transportation.gov/d/3trh-hz5x",
+            "language": [
+                "English"
+            ],
             "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "irregular",
+            "modified": "2015-01-31",
+            "programCode": [
+                "021:013"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "USDOT"
+            },
+            "spatial": "Detroit, Michigan",
+            "temporal": "2014-09-08/2014-09-10",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "2014 ITS World Congress Connected Vehicle Test Bed Demonstration Intersection Situation Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/3udb-p7vc",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2023-01-24",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-24",
-            "keyword": [
-                "monthly transportation statistics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "BTS Open Data",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/3udb-p7vc",
             "description": "Total value of merchandise freight for United States exports to and imports from Canada. The Bureau of Transportation Statistics releases freight data using a special tabulation of official international trade statistics that are collected by the U.S. Customs and Border Protection and processed and validated by the U.S. Census Bureau, Foreign Trade Division.",
-            "title": "U.S.-Canada Freight",
+            "identifier": "https://data.transportation.gov/api/views/3udb-p7vc",
+            "issued": "2023-01-24",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/3udb-p7vc",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-24",
             "programCode": [
                 "021:053"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Research and Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "U.S.-Canada Freight"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/3uu4-47sa",
-            "issued": "2020-10-28",
             "@type": "dcat:Dataset",
-            "modified": "2023-03-29",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/3uu4-47sa",
+            "issued": "2020-10-28",
+            "landingPage": "https://data.transportation.gov/d/3uu4-47sa",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-03-29",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
-            "title": "Data Access for Highway Performance Monitoring System (HPMS)",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "Data Access for Highway Performance Monitoring System (HPMS)"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/3v3y-yit3",
-            "issued": "2020-09-22",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
+            "description": "Offers insight on weekly fluctuation of the gasoline product supply, which is an important part of any analysis of construction trends. These data come directly from the Energy Information Administration (EIA) website.",
             "identifier": "https://data.transportation.gov/api/views/3v3y-yit3",
+            "issued": "2020-09-22",
+            "landingPage": "https://data.transportation.gov/d/3v3y-yit3",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-15",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "Offers insight on weekly fluctuation of the gasoline product supply, which is an important part of any analysis of construction trends. These data come directly from the Energy Information Administration (EIA) website.",
-            "title": "Weekly Gasoline Product Supplied Report",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "Weekly Gasoline Product Supplied Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/on_the_fly_download.aspx",
+            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
+            "analysisUnit": "Form 54 Filing",
             "bureauCode": [
                 "021:27"
             ],
-            "landingPage": "https://data.transportation.gov/d/3vpt-t4hz",
-            "issued": "2010-09-29",
-            "temporal": "R/1975-01-31/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-09",
+            "categoryDesignation": "Research",
             "collectionInstrument": "FORM FRA F 6180.54 (OMB No. 2130-0500)",
-            "references": [
-                "https://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Newregulation.aspx%3Fdoc=FRAGuideforPreparingAccIncReportspubMay2011.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/DownloadFStructure.aspx",
+            "description": "\"This file contains reported cases of collisions, derailments, fires, explosions, acts of God, or other events involving the operation of railroad on-track equipment and involving damages exceeding the reporting threshold for the year reported. National files from 1975 through the current year are available for download. In addition, individual files by State are available for the years 1991 through the current year.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/rrinctab.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Accident Table By Railroad"
+                }
             ],
+            "identifier": "199.18",
+            "isPartOf": "DOT-199",
+            "issued": "2010-09-29",
             "keyword": [
                 "acts of god",
                 "collisions",
@@ -5871,124 +5887,95 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "199.18",
+            "landingPage": "https://data.transportation.gov/d/3vpt-t4hz",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-10-09",
+            "phone": "202-493-6483",
+            "programCode": [
+                "021:036"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Railroad Administration"
             },
-            "description": "\"This file contains reported cases of collisions, derailments, fires, explosions, acts of God, or other events involving the operation of railroad on-track equipment and involving damages exceeding the reporting threshold for the year reported. National files from 1975 through the current year are available for download. In addition, individual files by State are available for the years 1991 through the current year.",
-            "title": "Rail Equipment Accidents - Accident Table By Railroad",
-            "isPartOf": "DOT-199",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:036"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/rrinctab.aspx",
-                    "mediaType": "text/csv",
-                    "title": "Accident Table By Railroad"
-                }
+            "references": [
+                "https://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Newregulation.aspx%3Fdoc=FRAGuideforPreparingAccIncReportspubMay2011.pdf"
             ],
             "spatial": "Latitude/Longitude, County, State",
-            "describedBy": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/DownloadFStructure.aspx",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/on_the_fly_download.aspx",
+            "temporal": "R/1975-01-31/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Form 54 Filing",
-            "phone": "202-493-6483",
-            "language": [
-                "en-US"
-            ]
+            "title": "Rail Equipment Accidents - Accident Table By Railroad"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/3w43-avfz",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2020-03-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
-            "keyword": [
-                "transportation cost",
-                "transportation economics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/3w43-avfz",
             "description": "Economic concepts related to the cost of transportation",
-            "title": "Transportation Economic Concepts: Transportation Costs",
+            "identifier": "https://data.transportation.gov/api/views/3w43-avfz",
+            "issued": "2020-03-01",
+            "keyword": [
+                "transportation cost",
+                "transportation economics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/3w43-avfz",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-18",
+            "phone": "202-366-DATA(3282)",
             "programCode": [
                 "021:053"
             ],
-            "license": "https://www.usa.gov/government-works",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Transportation Economic Concepts: Transportation Costs"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/3wd5-w3z4",
-            "issued": "2021-03-24",
             "@type": "dcat:Dataset",
-            "modified": "2021-06-25",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sean Jahanmir",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "The BTS Pocket Guide to Transportation is a popular, quick reference guide that provides transportation statistics at your fingertips. It provides key information and highlights major trends on the U.S. transportation system. The Pocket Guide is available in both web and print editions. It includes dynamic data updates to highlight the latest statistics, enhanced navigation, and sharable data to social media.",
             "identifier": "https://data.transportation.gov/api/views/3wd5-w3z4",
+            "issued": "2021-03-24",
+            "landingPage": "https://data.transportation.gov/d/3wd5-w3z4",
+            "modified": "2021-06-25",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "The BTS Pocket Guide to Transportation is a popular, quick reference guide that provides transportation statistics at your fingertips. It provides key information and highlights major trends on the U.S. transportation system. The Pocket Guide is available in both web and print editions. It includes dynamic data updates to highlight the latest statistics, enhanced navigation, and sharable data to social media.",
             "title": "Pocket Guide to Transportation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/3xj5-daif",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-11-19",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:answers@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/3xj5-daif",
             "description": "",
-            "title": "T100 - Preliminary Estimates",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5996,46 +5983,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/3xj5-daif/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/3xj5-daif/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/3xj5-daif/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/3xj5-daif/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/3xj5-daif/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/3xj5-daif/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/3xj5-daif/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/3xj5-daif/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/3xj5-daif/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/3xj5-daif",
+            "issued": "2024-11-19",
+            "landingPage": "https://data.transportation.gov/d/3xj5-daif",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-13",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Aviation"
-            ]
+            ],
+            "title": "T100 - Preliminary Estimates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/3xwn-gxgk",
-            "issued": "1970-01-01",
-            "temporal": "R/1970-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "State Traffic Monitoring Systems (TMS)",
-            "references": [
-                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/05martvt/05martvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "March 2005"
+                }
             ],
+            "identifier": "18.114",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -6045,57 +6060,60 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.114",
+            "landingPage": "https://data.transportation.gov/d/3xwn-gxgk",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-1067",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - March 2005",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/05martvt/05martvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "March 2005"
-                }
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
             ],
             "spatial": "Vehicles by type of functional classified roadway",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "temporal": "R/1970-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
-            "phone": "202-366-1067",
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Traffic Volume Trends - March 2005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/3yta-xtvs",
-            "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": false,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
+            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "2012 Alabama HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/alabama2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Alabama"
+                }
+            ],
+            "identifier": "678.54",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -6109,60 +6127,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.54",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Alabama",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/3yta-xtvs",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5035",
             "primaryITInvestmentUII": "021-099281808",
             "programCode": [
                 "021:009"
             ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/alabama2012.zip",
-                    "description": "2012 Alabama HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Alabama"
-                }
-            ],
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "temporal": "R/1981-11-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
-            "categoryDesignation": "Administrative",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-5035"
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Alabama"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/SafetyProgram/Review.aspx",
+            "agencyProgramURL": "https://www.fmcsa.dot.gov/safety/new-entrant-safety-assurance-program, https://ai.fmcsa.dot.gov/Grants/MCSAP.aspx",
+            "analysisUnit": "Motor Carrier",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/3znp-cqjm",
-            "issued": "2018-12-17",
-            "temporal": "2009-01-01/2013-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-11",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://ai.fmcsa.dot.gov/InfoCenter/Default.aspx#question402"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Contains data on compliance reviews and new entrant safety audits performed by FMCSA and State grantees.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://ai.fmcsa.dot.gov/SafetyProgram/Review.aspx",
+                    "mediaType": "text/html",
+                    "title": "Data Mining Tool"
+                }
             ],
+            "identifier": "95.1",
+            "isPartOf": "DOT-95",
+            "issued": "2018-12-17",
             "keyword": [
                 "bus",
                 "compliance reviews",
@@ -6181,60 +6196,60 @@
                 "safety audits",
                 "safety rating"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "95.1",
+            "landingPage": "https://data.transportation.gov/d/3znp-cqjm",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-07-11",
+            "phone": "202-493-0215",
+            "programCode": [
+                "021:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Motor Carrier Safety Administration"
             },
-            "description": "Contains data on compliance reviews and new entrant safety audits performed by FMCSA and State grantees.",
-            "title": "Motor Carrier Compliance Reviews and Safety Audits - Data Mining Tool",
-            "isPartOf": "DOT-95",
-            "agencyProgramURL": "https://www.fmcsa.dot.gov/safety/new-entrant-safety-assurance-program, https://ai.fmcsa.dot.gov/Grants/MCSAP.aspx",
-            "programCode": [
-                "021:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://ai.fmcsa.dot.gov/SafetyProgram/Review.aspx",
-                    "mediaType": "text/html",
-                    "title": "Data Mining Tool"
-                }
+            "references": [
+                "http://ai.fmcsa.dot.gov/InfoCenter/Default.aspx#question402"
             ],
             "spatial": "National, State",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/SafetyProgram/Review.aspx",
+            "temporal": "2009-01-01/2013-12-31",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Motor Carrier",
-            "phone": "202-493-0215",
-            "language": [
-                "en-US"
-            ]
+            "title": "Motor Carrier Compliance Reviews and Safety Audits - Data Mining Tool"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/42a3-rtnp",
-            "issued": "1970-01-01",
-            "temporal": "R/1970-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "State Traffic Monitoring Systems (TMS)",
-            "references": [
-                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12maytvt/12maytvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "May 2012"
+                }
             ],
+            "identifier": "18.38",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -6244,112 +6259,114 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.38",
+            "landingPage": "https://data.transportation.gov/d/42a3-rtnp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-1067",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - May 2012",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12maytvt/12maytvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "May 2012"
-                }
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
             ],
             "spatial": "Vehicles by type of functional classified roadway",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "temporal": "R/1970-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
-            "phone": "202-366-1067",
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Traffic Volume Trends - May 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/435g-4p74",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2020-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
-            "keyword": [
-                "transportation investment"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/435g-4p74",
             "description": "Investment in transportation",
-            "title": "Transportation Economic Trends: Value of Transportation - Investment",
+            "identifier": "https://data.transportation.gov/api/views/435g-4p74",
+            "issued": "2020-02-23",
+            "keyword": [
+                "transportation investment"
+            ],
+            "landingPage": "https://data.transportation.gov/d/435g-4p74",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-18",
+            "phone": "202-366-DATA(3282)",
             "programCode": [
                 "021:053"
             ],
-            "license": "https://www.usa.gov/government-works",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Transportation Economic Trends: Value of Transportation - Investment"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/43fv-s7h4",
-            "issued": "2023-01-19",
             "@type": "dcat:Dataset",
-            "modified": "2023-01-19",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joe McGill",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/43fv-s7h4",
+            "issued": "2023-01-19",
+            "landingPage": "https://data.transportation.gov/d/43fv-s7h4",
+            "modified": "2023-01-19",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Historical CFS Visualizations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/FLAT_RCL.zip",
+            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
+            "analysisUnit": "Vehicles , Tires, Child Safety Seats, Equipment",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/43xc-kybk",
-            "issued": "2002-12-16",
-            "temporal": "R/1949-01-01/P1D",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "N/A",
-            "modified": "2024-05-01",
-            "references": [
-                "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/RCL.txt"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/RCL.txt",
+            "describedByType": "text/plain",
+            "description": "Manufacturers who determine that a product or piece of original equipment either has a safety defect or is not in compliance with Federal safety standards are required to notify the National Highway Traffic Safety Administration (NHTSA) within 5 business days. NHTSA requires that manufacturers file a Defect and Noncompliance report as well as quarterly recall status reports, in compliance with Federal Regulation 49 (the National Traffic and Motor Safety Act) Part 573, which identifies the requirements for safety recalls. This information is stored in the NHTSA database. Use this data to search for recall information related to:-\tSpecific NHTSA campaigns -\tProduct types Access to public searches of NHTSA recall databases for tires, vehicles, car seats and equipment.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://vinrcl.safercar.gov/vin/",
+                    "mediaType": "text/html",
+                    "title": "Recalls Lookup by VIN"
+                }
             ],
+            "identifier": "83.6",
+            "isPartOf": "DOT-83",
+            "issued": "2002-12-16",
             "keyword": [
                 "air bag",
                 "air bags",
@@ -6376,89 +6393,50 @@
                 "vin",
                 "vin search"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "83.6",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Manufacturers who determine that a product or piece of original equipment either has a safety defect or is not in compliance with Federal safety standards are required to notify the National Highway Traffic Safety Administration (NHTSA) within 5 business days. NHTSA requires that manufacturers file a Defect and Noncompliance report as well as quarterly recall status reports, in compliance with Federal Regulation 49 (the National Traffic and Motor Safety Act) Part 573, which identifies the requirements for safety recalls. This information is stored in the NHTSA database. Use this data to search for recall information related to:-\tSpecific NHTSA campaigns -\tProduct types Access to public searches of NHTSA recall databases for tires, vehicles, car seats and equipment.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - Recalls Lookup by VIN",
-            "isPartOf": "DOT-83",
-            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
-            "describedByType": "text/plain",
+            "landingPage": "https://data.transportation.gov/d/43xc-kybk",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-2315",
             "primaryITInvestmentUII": "021-777552743",
             "programCode": [
                 "021:035"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://vinrcl.safercar.gov/vin/",
-                    "mediaType": "text/html",
-                    "title": "Recalls Lookup by VIN"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/RCL.txt"
             ],
             "spatial": "N/A",
-            "describedBy": "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/RCL.txt",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/FLAT_RCL.zip",
+            "temporal": "R/1949-01-01/P1D",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Vehicles , Tires, Child Safety Seats, Equipment",
-            "phone": "202-366-2315",
-            "language": [
-                "en-US"
-            ]
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - Recalls Lookup by VIN"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/44vu-u4yp",
-            "issued": "1970-01-01",
-            "temporal": "R/1970-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "State Traffic Monitoring Systems (TMS)",
-            "references": [
-                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
-            ],
-            "keyword": [
-                "aadt",
-                "'fhwa",
-                "traffic volume trends",
-                "tvt",
-                "vehicle miles traveled",
-                "vmt",
-                "volume data"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "18.98",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - July 2006",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6467,35 +6445,9 @@
                     "title": "July 2006"
                 }
             ],
-            "spatial": "Vehicles by type of functional classified roadway",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
-            "theme": [
-                "Transportation"
-            ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
-            "phone": "202-366-1067",
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "bureauCode": [
-                "021:15"
-            ],
-            "landingPage": "https://data.transportation.gov/d/44xk-gexr",
+            "identifier": "18.98",
+            "isPartOf": "DOT-18",
             "issued": "1970-01-01",
-            "temporal": "R/1970-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "collectionInstrument": "State Traffic Monitoring Systems (TMS)",
-            "references": [
-                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
-            ],
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -6505,23 +6457,49 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.51",
+            "landingPage": "https://data.transportation.gov/d/44vu-u4yp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-1067",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - June 2013",
-            "isPartOf": "DOT-18",
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
+            ],
+            "spatial": "Vehicles by type of functional classified roadway",
+            "temporal": "R/1970-01-01/P1M",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Monthly Traffic Volume Trends - July 2006"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
             "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
+            "bureauCode": [
+                "021:15"
             ],
+            "categoryDesignation": "Administrative",
+            "collectionInstrument": "State Traffic Monitoring Systems (TMS)",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6530,35 +6508,73 @@
                     "title": "June 2013"
                 }
             ],
-            "spatial": "Vehicles by type of functional classified roadway",
-            "dataQuality": true,
+            "identifier": "18.51",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
+            "keyword": [
+                "aadt",
+                "'fhwa",
+                "traffic volume trends",
+                "tvt",
+                "vehicle miles traveled",
+                "vmt",
+                "volume data"
+            ],
+            "landingPage": "https://data.transportation.gov/d/44xk-gexr",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "modified": "2024-05-08",
+            "phone": "202-366-1067",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
+            ],
+            "spatial": "Vehicles by type of functional classified roadway",
+            "temporal": "R/1970-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
-            "phone": "202-366-1067",
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Traffic Volume Trends - June 2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.infopave.com/",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/research/tfhrc/programs/infrastructure/pavements/ltpp/",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/45cf-eg6f",
-            "issued": "1993-07-01",
-            "temporal": "R/1993-07-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Research",
             "collectionInstrument": "https://infopave.fhwa.dot.gov",
-            "references": [
-                "https://infopave.fhwa.dot.gov/%3FGoto=Library"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://infopave.fhwa.dot.gov/Page/Index/IMS_USER_GUIDE",
+            "description": "Long-term Pavement performance, construction, traffic, and environmental data for more than 2500 pavement sections in the United States and Canada. More than a dozen experimental designs address specially constructed and existing asphalt and concrete pavements, and maintenance and rehabilitation strategies. Data collection has been on-going since 1990. About one third of the pavement sections are still under study. New warm-mix asphalt concrete pavement overlay sections are currently being recruited and constructed.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "This access point provides access to the LTPP InfoPave data features including section summary report, data selection and download, standard data release, ancillary data selection and download, visual data selection and download, table export and SQL export.",
+                    "downloadURL": "https://infopave.fhwa.dot.gov/%3FGoto=Data",
+                    "mediaType": "text/html",
+                    "title": "Data"
+                }
             ],
+            "identifier": "679.2",
+            "isPartOf": "DOT-679",
+            "issued": "1993-07-01",
             "keyword": [
                 "asphalt concrete",
                 "continuously reinforced concrete pavement",
@@ -6575,60 +6591,59 @@
                 "texture",
                 "traffic loading"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "679.2",
+            "landingPage": "https://data.transportation.gov/d/45cf-eg6f",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-493-3149",
+            "programCode": [
+                "021:009"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "Long-term Pavement performance, construction, traffic, and environmental data for more than 2500 pavement sections in the United States and Canada. More than a dozen experimental designs address specially constructed and existing asphalt and concrete pavements, and maintenance and rehabilitation strategies. Data collection has been on-going since 1990. About one third of the pavement sections are still under study. New warm-mix asphalt concrete pavement overlay sections are currently being recruited and constructed.",
-            "title": "Long-Term Pavement Performance (LTPP) - Data",
-            "isPartOf": "DOT-679",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/research/tfhrc/programs/infrastructure/pavements/ltpp/",
-            "programCode": [
-                "021:009"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://infopave.fhwa.dot.gov/%3FGoto=Data",
-                    "description": "This access point provides access to the LTPP InfoPave data features including section summary report, data selection and download, standard data release, ancillary data selection and download, visual data selection and download, table export and SQL export.",
-                    "@type": "dcat:Distribution",
-                    "title": "Data"
-                }
+            "references": [
+                "https://infopave.fhwa.dot.gov/%3FGoto=Library"
             ],
-            "describedBy": "https://infopave.fhwa.dot.gov/Page/Index/IMS_USER_GUIDE",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.infopave.com/",
+            "temporal": "R/1993-07-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "phone": "202-493-3149",
-            "language": [
-                "en-US"
-            ]
+            "title": "Long-Term Pavement Performance (LTPP) - Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
+            "agencyDataSeriesURL": "http://www.fmcsa.dot.gov/regulations/enforcement/civil-penalties",
+            "agencyProgramURL": "http://www.fmcsa.dot.gov/regulations/enforcement/civil-penalties",
+            "analysisUnit": "Enforcement Case",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/45ey-hc8w",
-            "issued": "2018-12-17",
-            "temporal": "R/2005-01-01/P3M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.fmcsa.dot.gov/regulations/enforcement/civil-penalties"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Contains data on civil penalties (fines) assessed by FMCSA against motor carriers, brokers and other entities.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://cms.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/docs/closedByEnforcement_FY2007_04-26-2013.xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Fiscal Year 2007"
+                }
             ],
+            "identifier": "96.4",
+            "isPartOf": "DOT-96",
+            "issued": "2018-12-17",
             "keyword": [
                 "bus",
                 "civil penalties",
@@ -6641,81 +6656,46 @@
                 "motor carrier",
                 "truck"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "96.4",
+            "landingPage": "https://data.transportation.gov/d/45ey-hc8w",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-24",
+            "phone": "202-366-4869",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Motor Carrier Safety Administration"
             },
-            "description": "Contains data on civil penalties (fines) assessed by FMCSA against motor carriers, brokers and other entities.",
-            "title": "Closed Enforcement Cases - Fiscal Year 2007",
-            "isPartOf": "DOT-96",
-            "agencyProgramURL": "http://www.fmcsa.dot.gov/regulations/enforcement/civil-penalties",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://cms.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/docs/closedByEnforcement_FY2007_04-26-2013.xlsx",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "Fiscal Year 2007"
-                }
+            "references": [
+                "http://www.fmcsa.dot.gov/regulations/enforcement/civil-penalties"
             ],
             "spatial": "National, State",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fmcsa.dot.gov/regulations/enforcement/civil-penalties",
+            "temporal": "R/2005-01-01/P3M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P3M",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Enforcement Case",
-            "phone": "202-366-4869",
-            "language": [
-                "en-US"
-            ]
+            "title": "Closed Enforcement Cases - Fiscal Year 2007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "The data system is not publicly available because it is related solely to internal agency management and may contain sensitive data.",
+            "accrualPeriodicity": "irregular",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/foia/",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/45rz-cdpz",
-            "issued": "2014-12-29",
-            "temporal": "2014-12-29/2014-12-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "annual report",
-                "fhwa",
-                "freedom of information act",
-                "report to congress"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "690.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "This system manages FHWA FOIA requests and is used to better meet the extensive annual reporting requirements imposed by statute (5 USC \u00a7 552). The FOIA Management System has approximately 110 FHWA Headquarters and Field users, and is also used by FMCSA, PHMSA, OST, FTA, OIG, and NHTSA, with separate reimbursable agreements in place for each Operating Administration.",
-            "title": "Freedom of Information Act Request Log System -",
-            "primaryITInvestmentUII": "021-553598490",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/foia/",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6723,26 +6703,50 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "690.0",
+            "issued": "2014-12-29",
+            "keyword": [
+                "annual report",
+                "fhwa",
+                "freedom of information act",
+                "report to congress"
             ],
-            "accrualPeriodicity": "irregular",
+            "landingPage": "https://data.transportation.gov/d/45rz-cdpz",
             "language": [
                 "en-US"
             ],
-            "phone": "202-493-0618"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-493-0618",
+            "primaryITInvestmentUII": "021-553598490",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "rights": "The data system is not publicly available because it is related solely to internal agency management and may contain sensitive data.",
+            "temporal": "2014-12-29/2014-12-29",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Freedom of Information Act Request Log System -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/45xw-qksz",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Transportation Analysis",
+                "hasEmail": "mailto:long.nguyen@dot.gov"
+            },
+            "description": "Freight Facts and Figures, developed by the Bureau of Transportation Statistics, is a collection of charts and statistical tables about freight transportation in the United States. These visualizations provide a snapshot of freight movement; the extent, condition, and performance of the freight transportation system; the economic characteristics of the transportation industry and its contribution to the U.S. economy; and the safety, energy, and environmental impacts of freight transportation.",
+            "identifier": "https://data.transportation.gov/api/views/45xw-qksz",
             "issued": "2019-06-05",
-            "@type": "dcat:Dataset",
-            "modified": "2021-06-08",
             "keyword": [
                 "bts",
                 "bureau of transportation statistics",
@@ -6752,39 +6756,51 @@
                 "freight facts & figures",
                 "freight transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Transportation Analysis",
-                "hasEmail": "mailto:long.nguyen@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/45xw-qksz",
+            "modified": "2021-06-08",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/45xw-qksz",
-            "description": "Freight Facts and Figures, developed by the Bureau of Transportation Statistics, is a collection of charts and statistical tables about freight transportation in the United States. These visualizations provide a snapshot of freight movement; the extent, condition, and performance of the freight transportation system; the economic characteristics of the transportation industry and its contribution to the U.S. economy; and the safety, energy, and environmental impacts of freight transportation.",
-            "title": "Freight Facts and Figures",
-            "programCode": [
-                "021:053"
-            ],
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Freight Facts and Figures"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.ntdprogram.gov/ntdprogram/data.htm",
+            "agencyProgramURL": "http://www.ntdprogram.gov",
+            "analysisUnit": "Transit Agency, some data by Mode and Type of Service",
             "bureauCode": [
                 "021:36"
             ],
-            "landingPage": "https://data.transportation.gov/d/46gk-9d3u",
-            "issued": "2010-10-01",
-            "temporal": "R/1996-12-31/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-05",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.ntdprogram.gov"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John D. Giorgis",
+                "hasEmail": "mailto:john.giorgis@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www.ntdprogram.gov/ntdprogram/data.htm",
+            "description": "Data reported to the NTD by urbanized area transit systems in their annual reports.   Includes contact information, contractural relationshps, subrecipient informatino, service area, sources of funds, operating expenditures by object class and function, capital expenditures by object class and function, fixed guideway information, revenue vehicle inventory, fuel consumption, employees, and labor hours, and urbanized area allocation information.   Also includes service supplied and consumed by annual total, average weekday, average saturday, and average sunday.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2012_database/NTD_database_2012.exe",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2012 Database"
+                }
             ],
+            "identifier": "21.16",
+            "isPartOf": "DOT-21",
+            "issued": "2010-10-01",
             "keyword": [
                 "agency",
                 "allocation",
@@ -6803,85 +6819,50 @@
                 "urbanized",
                 "vehicles"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John D. Giorgis",
-                "hasEmail": "mailto:john.giorgis@dot.gov"
-            },
-            "identifier": "21.16",
+            "landingPage": "https://data.transportation.gov/d/46gk-9d3u",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-03-05",
+            "phone": "202-366-5430",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Transit Administration"
             },
-            "description": "Data reported to the NTD by urbanized area transit systems in their annual reports.   Includes contact information, contractural relationshps, subrecipient informatino, service area, sources of funds, operating expenditures by object class and function, capital expenditures by object class and function, fixed guideway information, revenue vehicle inventory, fuel consumption, employees, and labor hours, and urbanized area allocation information.   Also includes service supplied and consumed by annual total, average weekday, average saturday, and average sunday.",
-            "title": "NTD Annual Module Data Set - 2012 Database",
-            "isPartOf": "DOT-21",
-            "agencyProgramURL": "http://www.ntdprogram.gov",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2012_database/NTD_database_2012.exe",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "2012 Database"
-                }
+            "references": [
+                "http://www.ntdprogram.gov"
             ],
             "spatial": "Urbanized Areas",
-            "describedBy": "http://www.ntdprogram.gov/ntdprogram/data.htm",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.ntdprogram.gov/ntdprogram/data.htm",
+            "temporal": "R/1996-12-31/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Transit Agency, some data by Mode and Type of Service",
-            "phone": "202-366-5430",
-            "language": [
-                "en-US"
-            ]
+            "title": "NTD Annual Module Data Set - 2012 Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/motorfuelhwy_trustfund.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/motorfueldata.cfm",
+            "analysisUnit": "Gallons",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/47xu-mhsh",
-            "issued": "1998-01-01",
-            "temporal": "R/1998-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative - Financial",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.fhwa.dot.gov/policyinformation/hss/guide"
-            ],
-            "keyword": [
-                "diesel",
-                "fuel tax",
-                "gallons",
-                "gasoline",
-                "motor fuel"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "698.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hss/guide/ch2.cfm",
             "description": "On a monthly basis, each State is required to report to the Federal Highway Administration (FHWA), the amount of gallons taxed by that state. This data is analyzed and compiled by FHWA staff. The data on the amount of on-highway fuel use for each State is then used to attribute federal revenue to each State. Yearly, the FHWA, Office of Policy, provides data from the previous year's data for use in the attribution process. The previous year data is used to provide States added time to review, allowing them to verify that the data report is correct and ready to be used in attribution.",
-            "title": "Monthly Motor Fuel - Monthly Motor Fuel Reports",
-            "isPartOf": "DOT-698",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/motorfueldata.cfm",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6890,36 +6871,70 @@
                     "title": "Monthly Motor Fuel Reports"
                 }
             ],
-            "spatial": "National, State",
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hss/guide/ch2.cfm",
-            "dataQuality": true,
+            "identifier": "698.1",
+            "isPartOf": "DOT-698",
+            "issued": "1998-01-01",
+            "keyword": [
+                "diesel",
+                "fuel tax",
+                "gallons",
+                "gasoline",
+                "motor fuel"
+            ],
+            "landingPage": "https://data.transportation.gov/d/47xu-mhsh",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/motorfuelhwy_trustfund.cfm",
+            "modified": "2024-05-08",
+            "phone": "202-366-5026",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "references": [
+                "http://www.fhwa.dot.gov/policyinformation/hss/guide"
+            ],
+            "spatial": "National, State",
+            "temporal": "R/1998-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative - Financial",
-            "analysisUnit": "Gallons",
-            "phone": "202-366-5026",
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Motor Fuel - Monthly Motor Fuel Reports"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
+            "agencyDataSeriesURL": "http://www.fmcsa.dot.gov/regulations/enforcement/civil-penalties",
+            "agencyProgramURL": "http://www.fmcsa.dot.gov/regulations/enforcement/civil-penalties",
+            "analysisUnit": "Enforcement Case",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/485m-yfxs",
-            "issued": "2018-12-17",
-            "temporal": "R/2005-01-01/P3M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.fmcsa.dot.gov/regulations/enforcement/civil-penalties"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Contains data on civil penalties (fines) assessed by FMCSA against motor carriers, brokers and other entities.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://cms.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/docs/closedByEnforcement_FY2011_04-26-2013.xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Fiscal Year 2011"
+                }
             ],
+            "identifier": "96.7",
+            "isPartOf": "DOT-96",
+            "issued": "2018-12-17",
             "keyword": [
                 "bus",
                 "civil penalties",
@@ -6932,57 +6947,60 @@
                 "motor carrier",
                 "truck"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "96.7",
+            "landingPage": "https://data.transportation.gov/d/485m-yfxs",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-24",
+            "phone": "202-366-4869",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Motor Carrier Safety Administration"
             },
-            "description": "Contains data on civil penalties (fines) assessed by FMCSA against motor carriers, brokers and other entities.",
-            "title": "Closed Enforcement Cases - Fiscal Year 2011",
-            "isPartOf": "DOT-96",
-            "agencyProgramURL": "http://www.fmcsa.dot.gov/regulations/enforcement/civil-penalties",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://cms.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/docs/closedByEnforcement_FY2011_04-26-2013.xlsx",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "Fiscal Year 2011"
-                }
+            "references": [
+                "http://www.fmcsa.dot.gov/regulations/enforcement/civil-penalties"
             ],
             "spatial": "National, State",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fmcsa.dot.gov/regulations/enforcement/civil-penalties",
+            "temporal": "R/2005-01-01/P3M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P3M",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Enforcement Case",
-            "phone": "202-366-4869",
-            "language": [
-                "en-US"
-            ]
+            "title": "Closed Enforcement Cases - Fiscal Year 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/48ah-qrwd",
-            "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": false,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
+            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "2012 Missouri HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/missouri2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Missouri"
+                }
+            ],
+            "identifier": "678.79",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -6996,60 +7014,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.79",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Missouri",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/48ah-qrwd",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5035",
             "primaryITInvestmentUII": "021-099281808",
             "programCode": [
                 "021:009"
             ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/missouri2012.zip",
-                    "description": "2012 Missouri HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Missouri"
-                }
-            ],
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "temporal": "R/1981-11-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
-            "categoryDesignation": "Administrative",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-5035"
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Missouri"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/48kf-u8he",
-            "issued": "1970-01-01",
-            "temporal": "R/1970-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "State Traffic Monitoring Systems (TMS)",
-            "references": [
-                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12septvt/12septvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "September 2012"
+                }
             ],
+            "identifier": "18.42",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -7059,60 +7074,59 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.42",
+            "landingPage": "https://data.transportation.gov/d/48kf-u8he",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-1067",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - September 2012",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12septvt/12septvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "September 2012"
-                }
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
             ],
             "spatial": "Vehicles by type of functional classified roadway",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "temporal": "R/1970-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
-            "phone": "202-366-1067",
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Traffic Volume Trends - September 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/SMS/Data/Downloads.aspx",
+            "agencyProgramURL": "http://ai.fmcsa.dot.gov/SMS",
+            "analysisUnit": "Motor Carrier",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/4a2k-zf79",
-            "issued": "2011-12-15",
-            "temporal": "R/1974-06-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://ai.fmcsa.dot.gov/sms/Data/Downloads.aspx"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Registration information on interstate, intrastate non-hazmat, and intrastate truck and bus companies that operate in the United States and have registered with FMCSA.  Contains contact information and demographic information (number of drivers, vehicles, commodities carried, etc).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://ai.fmcsa.dot.gov/SMS/Tools/Downloads.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Census Files"
+                }
             ],
+            "identifier": "92.0",
+            "issued": "2011-12-15",
             "keyword": [
                 "address",
                 "bus",
@@ -7128,77 +7142,46 @@
                 "truck",
                 "trucking"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "92.0",
+            "landingPage": "https://data.transportation.gov/d/4a2k-zf79",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-24",
+            "phone": "202-366-4869",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Motor Carrier Safety Administration"
             },
-            "description": "Registration information on interstate, intrastate non-hazmat, and intrastate truck and bus companies that operate in the United States and have registered with FMCSA.  Contains contact information and demographic information (number of drivers, vehicles, commodities carried, etc).",
-            "title": "Motor Carrier Registrations - Census Files",
-            "agencyProgramURL": "http://ai.fmcsa.dot.gov/SMS",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://ai.fmcsa.dot.gov/SMS/Tools/Downloads.aspx",
-                    "mediaType": "text/csv",
-                    "title": "Census Files"
-                }
+            "references": [
+                "http://ai.fmcsa.dot.gov/sms/Data/Downloads.aspx"
             ],
             "spatial": "Data contains street addresses.",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/SMS/Data/Downloads.aspx",
+            "temporal": "R/1974-06-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "analysisUnit": "Motor Carrier",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4869",
-            "language": [
-                "en-US"
-            ]
+            "title": "Motor Carrier Registrations - Census Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "The data set contains controlled unclassified procurement information, confidential business information, and information protected by statute or regulation.",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/4af8-nmau",
-            "issued": "2014-12-29",
-            "temporal": "R/2014-12-29/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "application performance",
-                "temporary data"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "735.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
             "description": "Delphi FND Application Object Library contains the following data elements, but are not limited to temporary data tables for the logged in session, information about application module pool operations and is mainly intended for performance diagnostics, attachments, audit information, and information about on-line help documents.",
-            "title": "Delphi FND Application Object Library -",
-            "primaryITInvestmentUII": "021-105731835",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7206,48 +7189,48 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "theme": [
-                "Transportation"
+            "identifier": "735.0",
+            "issued": "2014-12-29",
+            "keyword": [
+                "application performance",
+                "temporary data"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/4af8-nmau",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-9646"
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-14",
+            "phone": "202-366-9646",
+            "primaryITInvestmentUII": "021-105731835",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "rights": "The data set contains controlled unclassified procurement information, confidential business information, and information protected by statute or regulation.",
+            "temporal": "R/2014-12-29/P1Y",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Delphi FND Application Object Library -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.bts.dot.gov/congressionaldistricts",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2023-10-11",
-            "@type": "dcat:Dataset",
-            "temporal": "118th Congress (2023-2024)",
-            "modified": "2023-10-17",
-            "keyword": [
-                "congressional district",
-                "counties",
-                "statistics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kyle Titlow",
                 "hasEmail": "mailto:kyle.titlow@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/4bf2-3jcw",
+            "dataQuality": true,
             "description": "These are the congressional district-specific transportation statistics currently contained in the dashboard visible at https://www.bts.dot.gov/congressionaldistricts.\n\nData are available for all attributes for the 118th Congress (2023-2024).",
-            "title": "Citizen Connect - Congressional District data (live)",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7255,49 +7238,84 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/4bf2-3jcw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/4bf2-3jcw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/4bf2-3jcw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/4bf2-3jcw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/4bf2-3jcw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/4bf2-3jcw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/4bf2-3jcw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/4bf2-3jcw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/4bf2-3jcw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/4bf2-3jcw",
+            "issued": "2023-10-11",
+            "keyword": [
+                "congressional district",
+                "counties",
+                "statistics"
+            ],
+            "landingPage": "https://www.bts.dot.gov/congressionaldistricts",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-10-17",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "spatial": "United States",
+            "temporal": "118th Congress (2023-2024)",
             "theme": [
                 "Research and Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Citizen Connect - Congressional District data (live)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/4bqd-4w57",
-            "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": false,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
+            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "2013 Ohio HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/ohio2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Ohio"
+                }
+            ],
+            "identifier": "678.139",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -7311,57 +7329,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.139",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Ohio",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/4bqd-4w57",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5035",
             "primaryITInvestmentUII": "021-099281808",
             "programCode": [
                 "021:009"
             ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/ohio2013.zip",
-                    "description": "2013 Ohio HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Ohio"
-                }
-            ],
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "temporal": "R/1981-11-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
-            "categoryDesignation": "Administrative",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-5035"
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Ohio"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/4btu-pc2g",
-            "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": false,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
+            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "2013 Mississippi HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/mississippi2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Mississippi"
+                }
+            ],
+            "identifier": "678.128",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -7375,86 +7393,46 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.128",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Mississippi",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/4btu-pc2g",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5035",
             "primaryITInvestmentUII": "021-099281808",
             "programCode": [
                 "021:009"
             ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/mississippi2013.zip",
-                    "description": "2013 Mississippi HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Mississippi"
-                }
-            ],
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "temporal": "R/1981-11-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
-            "categoryDesignation": "Administrative",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-5035"
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Mississippi"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/4cf4-dpju",
-            "issued": "1970-01-01",
-            "temporal": "R/1970-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "State Traffic Monitoring Systems (TMS)",
-            "references": [
-                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
-            ],
-            "keyword": [
-                "aadt",
-                "'fhwa",
-                "traffic volume trends",
-                "tvt",
-                "vehicle miles traveled",
-                "vmt",
-                "volume data"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "18.71",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - October 2008",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7463,32 +7441,70 @@
                     "title": "October 2008"
                 }
             ],
-            "spatial": "Vehicles by type of functional classified roadway",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
-            "theme": [
-                "Transportation"
+            "identifier": "18.71",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
+            "keyword": [
+                "aadt",
+                "'fhwa",
+                "traffic volume trends",
+                "tvt",
+                "vehicle miles traveled",
+                "vmt",
+                "volume data"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
-            "phone": "202-366-1067",
+            "landingPage": "https://data.transportation.gov/d/4cf4-dpju",
             "language": [
                 "en-US"
-            ]
-        },
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-1067",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
+            ],
+            "spatial": "Vehicles by type of functional classified roadway",
+            "temporal": "R/1970-01-01/P1M",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Monthly Traffic Volume Trends - October 2008"
+        },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/4dez-3n4e",
-            "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": false,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
+            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/pa_nhs.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 NHS"
+                }
+            ],
+            "identifier": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -7502,55 +7518,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "DOT-678",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS)",
+            "landingPage": "https://data.transportation.gov/d/4dez-3n4e",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5035",
             "primaryITInvestmentUII": "021-099281808",
             "programCode": [
                 "021:009"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/pa_nhs.zip",
-                    "mediaType": "application/zip",
-                    "title": "2011 NHS"
-                }
-            ],
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "temporal": "R/1981-11-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
-            "categoryDesignation": "Administrative",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-5035"
+            "title": "Highway Performance Monitoring System (HPMS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/4enp-mcdu",
-            "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": false,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
+            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "2011 Mississippi HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/mississippi2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Mississippi"
+                }
+            ],
+            "identifier": "678.26",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -7564,60 +7582,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.26",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Mississippi",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/4enp-mcdu",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5035",
             "primaryITInvestmentUII": "021-099281808",
             "programCode": [
                 "021:009"
             ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/mississippi2011.zip",
-                    "description": "2011 Mississippi HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Mississippi"
-                }
-            ],
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "temporal": "R/1981-11-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
-            "categoryDesignation": "Administrative",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-5035"
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Mississippi"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/PT1S",
+            "agencyDataSeriesURL": "http://www.nhtsa.gov/Vehicle+Safety",
+            "agencyProgramURL": "http://vpic.nhtsa.dot.gov/",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/4eui-jxfx",
-            "issued": "2015-10-05",
-            "temporal": "R/2015-10-05/PT1S",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Administrative - Regulatory",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://vpic.nhtsa.dot.gov/"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The NHTSA Product Information Catalog and Vehicle Listing (vPIC) is a consolidated platform that presents data collected within the manufacturer reported data from CFR 49 Parts 551 - 574 for use in a variety of modern tools. NHTSA's vPIC platform is intended to serve as a centralized source for basic Vehicle Identification Number (VIN) decoding, Manufacturer Information Database (MID), Manufacturer Equipment Plant Identification and associated data. vPIC is intended to support the Open Data and Transparency initiatives of the agency by allowing the data to be freely used by the public without the burden of manual retrieval from a library of electronic documents (PDFs). While these documents will still be available online for viewing within the Manufacturer Information Database (MID) module of vPIC one can view and use the actual data through the VIN Decoder and Application Programming Interface (API) modules.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "49 CFR Part 595.6, Modifier identification, ",
+                    "downloadURL": "http://vpic.nhtsa.dot.gov/mid/home/ModifierSearch",
+                    "mediaType": "text/html",
+                    "title": "Modifier DB"
+                }
             ],
+            "identifier": "65.10",
+            "isPartOf": "DOT-65",
+            "issued": "2015-10-05",
             "keyword": [
                 "49",
                 "551",
@@ -7654,80 +7669,81 @@
                 "vin",
                 "vpic"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "65.10",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "The NHTSA Product Information Catalog and Vehicle Listing (vPIC) is a consolidated platform that presents data collected within the manufacturer reported data from CFR 49 Parts 551 - 574 for use in a variety of modern tools. NHTSA's vPIC platform is intended to serve as a centralized source for basic Vehicle Identification Number (VIN) decoding, Manufacturer Information Database (MID), Manufacturer Equipment Plant Identification and associated data. vPIC is intended to support the Open Data and Transparency initiatives of the agency by allowing the data to be freely used by the public without the burden of manual retrieval from a library of electronic documents (PDFs). While these documents will still be available online for viewing within the Manufacturer Information Database (MID) module of vPIC one can view and use the actual data through the VIN Decoder and Application Programming Interface (API) modules.",
-            "title": "NHTSA Product Information Catalog and Vehicle Listing (vPIC) - Modifier DB",
-            "isPartOf": "DOT-65",
-            "agencyProgramURL": "http://vpic.nhtsa.dot.gov/",
+            "landingPage": "https://data.transportation.gov/d/4eui-jxfx",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-01",
+            "phone": "202-366-2622",
             "primaryITInvestmentUII": "021-430297065",
             "programCode": [
                 "021:031"
             ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://vpic.nhtsa.dot.gov/mid/home/ModifierSearch",
-                    "description": "49 CFR Part 595.6, Modifier identification, ",
-                    "@type": "dcat:Distribution",
-                    "title": "Modifier DB"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "http://vpic.nhtsa.dot.gov/"
             ],
             "spatial": "NA",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.nhtsa.gov/Vehicle+Safety",
+            "temporal": "R/2015-10-05/PT1S",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/PT1S",
-            "categoryDesignation": "Administrative - Regulatory",
-            "phone": "202-366-2622",
-            "language": [
-                "en-US"
-            ]
+            "title": "NHTSA Product Information Catalog and Vehicle Listing (vPIC) - Modifier DB"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/4fgg-apek",
-            "issued": "2023-10-18",
             "@type": "dcat:Dataset",
-            "modified": "2024-07-16",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sean Jahanmir",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/4fgg-apek",
+            "issued": "2023-10-18",
+            "landingPage": "https://data.transportation.gov/d/4fgg-apek",
+            "modified": "2024-07-16",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Maps"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://fhwaapps.fhwa.dot.gov/vtris-wp/",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/travelmonitoring.cfm",
+            "analysisUnit": "Weight-in-motion (WIM) station",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/4fnh-p38h",
-            "issued": "1990-01-01",
-            "temporal": "R/1990-01-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Web site",
-            "references": [
-                "http://www.fhwa.dot.gov/ohim/ohimvtis.cfm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www.fhwa.dot.gov/ohim/ohimvtis.cfm",
+            "description": "The VTRIS W-Tables are designed to provide a standard format for presenting the outcome of the Vehicle Weighing and Classification efforts at truck weigh sites. The data that appears in the W-Tables comes from the Summary files that are generated by the Summary subsystem.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://fhwaapps.fhwa.dot.gov/vtris-wp/",
+                    "mediaType": "text/html",
+                    "title": "Data Download Tool"
+                }
             ],
+            "identifier": "285.2",
+            "isPartOf": "DOT-285",
+            "issued": "1990-01-01",
             "keyword": [
                 "axle load",
                 "carried load",
@@ -7743,61 +7759,62 @@
                 "weight-in-motion",
                 "wim"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "285.2",
+            "landingPage": "https://data.transportation.gov/d/4fnh-p38h",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5053",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "The VTRIS W-Tables are designed to provide a standard format for presenting the outcome of the Vehicle Weighing and Classification efforts at truck weigh sites. The data that appears in the W-Tables comes from the Summary files that are generated by the Summary subsystem.",
-            "title": "Vehicle Travel Information System (VTRIS) - Data Download Tool",
-            "isPartOf": "DOT-285",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/travelmonitoring.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://fhwaapps.fhwa.dot.gov/vtris-wp/",
-                    "mediaType": "text/html",
-                    "title": "Data Download Tool"
-                }
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/ohimvtis.cfm"
             ],
             "spatial": "Point",
-            "describedBy": "http://www.fhwa.dot.gov/ohim/ohimvtis.cfm",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "https://fhwaapps.fhwa.dot.gov/vtris-wp/",
+            "temporal": "R/1990-01-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Weight-in-motion (WIM) station",
-            "phone": "202-366-5053",
-            "language": [
-                "en-US"
-            ]
+            "title": "Vehicle Travel Information System (VTRIS) - Data Download Tool"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/FLAT_RCL.zip",
+            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
+            "analysisUnit": "Vehicles , Tires, Child Safety Seats, Equipment",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/4fsp-igku",
-            "issued": "2002-12-16",
-            "temporal": "R/1949-01-01/P1D",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "N/A",
-            "modified": "2024-05-01",
-            "references": [
-                "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/RCL.txt"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/RCL.txt",
+            "describedByType": "text/plain",
+            "description": "Manufacturers who determine that a product or piece of original equipment either has a safety defect or is not in compliance with Federal safety standards are required to notify the National Highway Traffic Safety Administration (NHTSA) within 5 business days. NHTSA requires that manufacturers file a Defect and Noncompliance report as well as quarterly recall status reports, in compliance with Federal Regulation 49 (the National Traffic and Motor Safety Act) Part 573, which identifies the requirements for safety recalls. This information is stored in the NHTSA database. Use this data to search for recall information related to:-\tSpecific NHTSA campaigns -\tProduct types Access to public searches of NHTSA recall databases for tires, vehicles, car seats and equipment.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www-odi.nhtsa.dot.gov/owners/SearchSafetyIssues",
+                    "mediaType": "text/html",
+                    "title": "Recalls - Safety Issues for Vehicles, Child Restraints, Tires, and Equipment."
+                }
             ],
+            "identifier": "83.9",
+            "isPartOf": "DOT-83",
+            "issued": "2002-12-16",
             "keyword": [
                 "air bag",
                 "air bags",
@@ -7824,82 +7841,79 @@
                 "vin",
                 "vin search"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "83.9",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Manufacturers who determine that a product or piece of original equipment either has a safety defect or is not in compliance with Federal safety standards are required to notify the National Highway Traffic Safety Administration (NHTSA) within 5 business days. NHTSA requires that manufacturers file a Defect and Noncompliance report as well as quarterly recall status reports, in compliance with Federal Regulation 49 (the National Traffic and Motor Safety Act) Part 573, which identifies the requirements for safety recalls. This information is stored in the NHTSA database. Use this data to search for recall information related to:-\tSpecific NHTSA campaigns -\tProduct types Access to public searches of NHTSA recall databases for tires, vehicles, car seats and equipment.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - Recalls - Safety Issues for Vehicles, Child Restraints, Tires, and Equipment.",
-            "isPartOf": "DOT-83",
-            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
-            "describedByType": "text/plain",
+            "landingPage": "https://data.transportation.gov/d/4fsp-igku",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-0154",
             "primaryITInvestmentUII": "021-777552743",
             "programCode": [
                 "021:035"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www-odi.nhtsa.dot.gov/owners/SearchSafetyIssues",
-                    "mediaType": "text/html",
-                    "title": "Recalls - Safety Issues for Vehicles, Child Restraints, Tires, and Equipment."
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/RCL.txt"
             ],
             "spatial": "N/A",
-            "describedBy": "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/RCL.txt",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/FLAT_RCL.zip",
+            "temporal": "R/1949-01-01/P1D",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Vehicles , Tires, Child Safety Seats, Equipment",
-            "phone": "202-366-0154",
-            "language": [
-                "en-US"
-            ]
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - Recalls - Safety Issues for Vehicles, Child Restraints, Tires, and Equipment."
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/4hvq-je54",
-            "issued": "2020-12-08",
             "@type": "dcat:Dataset",
-            "modified": "2022-01-10",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alpha Wingfield",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/4hvq-je54",
+            "issued": "2020-12-08",
+            "landingPage": "https://data.transportation.gov/d/4hvq-je54",
+            "modified": "2022-01-10",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Noise  Map for TRB"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://safer.fmcsa.dot.gov/CompanySnapshot.aspx",
+            "agencyProgramURL": "http://safer.fmcsa.dot.gov/CompanySnapshot.aspx",
+            "analysisUnit": "Motor Carrier",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/4kcp-cfmm",
-            "issued": "2000-01-01",
-            "temporal": "R/1974-06-01/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://safer.fmcsa.dot.gov/CompanySnapshot.aspx"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Company Snapshot is a concise electronic record of company identification, size, commodity information, and safety record, including the safety rating (if any), a roadside out-of-service inspection summary, and crash information. The Company Snapshot is available via an ad-hoc query (one carrier at a time) free of charge.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://safer.fmcsa.dot.gov/CompanySnapshot.aspx",
+                    "mediaType": "text/html",
+                    "title": "SAFER - Company Snapshot"
+                }
             ],
+            "identifier": "DOT-122",
+            "issued": "2000-01-01",
             "keyword": [
                 "bus",
                 "company safety profile",
@@ -7920,91 +7934,62 @@
                 "safety and fitness electronic records",
                 "safety rating"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "DOT-122",
+            "landingPage": "https://data.transportation.gov/d/4kcp-cfmm",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-24",
+            "phone": "202-493-0215",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Motor Carrier Safety Administration"
             },
-            "description": "The Company Snapshot is a concise electronic record of company identification, size, commodity information, and safety record, including the safety rating (if any), a roadside out-of-service inspection summary, and crash information. The Company Snapshot is available via an ad-hoc query (one carrier at a time) free of charge.",
-            "title": "SAFER - Company Snapshot",
-            "agencyProgramURL": "http://safer.fmcsa.dot.gov/CompanySnapshot.aspx",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safer.fmcsa.dot.gov/CompanySnapshot.aspx",
-                    "mediaType": "text/html",
-                    "title": "SAFER - Company Snapshot"
-                }
+            "references": [
+                "http://safer.fmcsa.dot.gov/CompanySnapshot.aspx"
             ],
             "spatial": "Physical and mailing addresses.",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://safer.fmcsa.dot.gov/CompanySnapshot.aspx",
+            "temporal": "R/1974-06-01/P1D",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "analysisUnit": "Motor Carrier",
-            "categoryDesignation": "Research",
-            "phone": "202-493-0215",
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFER - Company Snapshot"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/4kd6-2t87",
-            "issued": "2021-05-19",
             "@type": "dcat:Dataset",
-            "modified": "2024-02-06",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Chambers",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/4kd6-2t87",
+            "issued": "2021-05-19",
+            "landingPage": "https://data.transportation.gov/d/4kd6-2t87",
+            "modified": "2024-02-06",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Vessel Dwell Times"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/4kzx-kud8",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2020-12-21",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "references": [
-                "https://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/4kzx-kud8",
+            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
             "description": "State DOTs provide the location limits of highway sections to be used to represent statewide aggregations based on a statistically valid Sample Panel.\nThe South contains data for the following States: Alabama, Arkansas, Florida, Georgia, Kentucky, Louisiana, Mississippi, North Carolina, South Carolina, Tennessee, Virginia, West Virginia, and Puerto Rico.",
-            "title": "Roadway Sections South 2018",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8012,70 +7997,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/4kzx-kud8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/4kzx-kud8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/4kzx-kud8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/4kzx-kud8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/4kzx-kud8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/4kzx-kud8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/4kzx-kud8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/4kzx-kud8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/4kzx-kud8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "USA",
-            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
-            "license": "https://www.usa.gov/government-works",
-            "theme": [
-                "Roadways and Bridges"
-            ],
+            "identifier": "https://data.transportation.gov/api/views/4kzx-kud8",
+            "issued": "2020-12-21",
+            "landingPage": "https://data.transportation.gov/d/4kzx-kud8",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-05-08",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "references": [
+                "https://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/"
+            ],
+            "spatial": "USA",
+            "theme": [
+                "Roadways and Bridges"
+            ],
+            "title": "Roadway Sections South 2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Access restricted under the Privacy Act of 1974; SORN issued by OPM; see reference on DOT Privacy Act page www.dot.gov/privacy under Government-wide System of Records",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/4mah-mzw6",
-            "issued": "2014-11-21",
-            "temporal": "R/2014-11-21/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "hr",
-                "payroll",
-                "personnel"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "DOT-1634",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
             "description": "This data set contains payroll and personnel data for current and past DOT employees.  This data is produced by the current HR and payroll provider (Department of Interior's IBC) with historical data also maintained in the dataset produced by DOT's CUPS, CPMIS and IPPS systems.  The data contains PII (Employee Name, SSN, Date of Birth, Home Address, Financial information, etc.), Civil Rights (Disability, Gender, Race) and other sensitive data (Background Investigations and Security Clearance).",
-            "title": "Personnel and Payroll Data (FPPS and associated systems FPPS Datamart, WebPrinting System) and eOPF",
-            "primaryITInvestmentUII": "021-999991221",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8084,57 +8066,47 @@
                     "title": "Workforce Statistics Archive"
                 }
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "theme": [
-                "Transportation"
+            "identifier": "DOT-1634",
+            "issued": "2014-11-21",
+            "keyword": [
+                "hr",
+                "payroll",
+                "personnel"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Administrative",
+            "landingPage": "https://data.transportation.gov/d/4mah-mzw6",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-5140"
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-14",
+            "phone": "202-366-5140",
+            "primaryITInvestmentUII": "021-999991221",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "rights": "Access restricted under the Privacy Act of 1974; SORN issued by OPM; see reference on DOT Privacy Act page www.dot.gov/privacy under Government-wide System of Records",
+            "temporal": "R/2014-11-21/P1Y",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Personnel and Payroll Data (FPPS and associated systems FPPS Datamart, WebPrinting System) and eOPF"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/4mym-8uef",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2024-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-28",
-            "keyword": [
-                "connected equipment",
-                "connected vehicle",
-                "connected vehicle data",
-                "connected vehicle environment",
-                "connected vehicle message",
-                "connected vehicles",
-                "on-board equipment",
-                "on-board unit",
-                "roadside equipment",
-                "road side unit",
-                "vehicle data",
-                "vehicle to infrastructure",
-                "vehicle to vehicle"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kate Hartman",
                 "hasEmail": "mailto:kate.hartman@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/4mym-8uef",
             "description": "Part of Wyoming Department of Transportation Connected Vehicle Pilot Phase 4. Test case WV2VMCT-1 Verify V2V communication of BSMs vehicle 2 data",
-            "title": "LTE-V2X Wyoming Connected Vehicle Pilot test ID WV2VMCT-1 vehicle 2",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8142,61 +8114,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/4mym-8uef/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/4mym-8uef/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/4mym-8uef/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/4mym-8uef/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/4mym-8uef/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/4mym-8uef/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/4mym-8uef/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/4mym-8uef/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/4mym-8uef/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Wyoming",
+            "identifier": "https://data.transportation.gov/api/views/4mym-8uef",
+            "issued": "2024-07-19",
+            "keyword": [
+                "connected equipment",
+                "connected vehicle",
+                "connected vehicle data",
+                "connected vehicle environment",
+                "connected vehicle message",
+                "connected vehicles",
+                "on-board equipment",
+                "on-board unit",
+                "roadside equipment",
+                "road side unit",
+                "vehicle data",
+                "vehicle to infrastructure",
+                "vehicle to vehicle"
+            ],
+            "landingPage": "https://data.transportation.gov/d/4mym-8uef",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-09-28",
+            "programCode": [
+                "021:042"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "spatial": "Wyoming",
             "theme": [
                 "Automobiles"
-            ]
+            ],
+            "title": "LTE-V2X Wyoming Connected Vehicle Pilot test ID WV2VMCT-1 vehicle 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/4p55-emkp",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-12-27",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-29",
-            "keyword": [
-                "demand response",
-                "geographic",
-                "geospatial",
-                "public transit",
-                "scheduled service"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NTD Program Support",
                 "hasEmail": "mailto:NTDHelp@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Transit Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/4p55-emkp",
             "description": "This dataset details service schedules for Demand Response (DR) modes for each applicable agency and type of service (TOS) reported to the National Transit Database for Report Year 2023.\n\nNTD Data Tables organize and summarize data from the 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. \n\nThis data is a part of new reporting requirements as of 2023. Other datasets describing aspects of Demand Response Geographical Area Coverage can be found at the following links:\nCounties and Places: https://data.transportation.gov/Public-Transit/Demand-Response-Geographic-Area-Coverage-Counties-/3kum-6vpd/about_data\nPassenger Eligibility and Requirements: https://data.transportation.gov/dataset/Demand-Response-Geographic-Area-Coverage-Passenger/h9qc-expu/about_data\n\nIf you have any other questions about this table, please contact the NTD Help Desk at NTDHelp@dot.gov.",
-            "title": "2023 NTD Annual Data - Demand Response Geographic Area Coverage (Service Schedules)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8204,46 +8187,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/4p55-emkp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/4p55-emkp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/4p55-emkp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/4p55-emkp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/4p55-emkp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/4p55-emkp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/4p55-emkp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/4p55-emkp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/4p55-emkp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/4p55-emkp",
+            "issued": "2024-12-27",
+            "keyword": [
+                "demand response",
+                "geographic",
+                "geospatial",
+                "public transit",
+                "scheduled service"
+            ],
+            "landingPage": "https://data.transportation.gov/d/4p55-emkp",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-29",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Transit Administration"
+            },
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "2023 NTD Annual Data - Demand Response Geographic Area Coverage (Service Schedules)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.ntdprogram.gov/ntdprogram/data.htm",
+            "agencyProgramURL": "http://www.ntdprogram.gov/",
+            "analysisUnit": "transit agency, mode, type of service",
             "bureauCode": [
                 "021:36"
             ],
-            "landingPage": "https://data.transportation.gov/d/4pyy-eqpe",
-            "issued": "2002-01-01",
-            "temporal": "R/2002-01-31/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-05",
+            "categoryDesignation": "Research",
             "collectionInstrument": "http://www.ntdprogram.gov/ntdprogram/safety.htm",
-            "references": [
-                "www.transit.dot.gov/ntd"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NTD Program Support",
+                "hasEmail": "mailto:NTDHelp@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Summary (\"count\") data submitted to the Safety & Security Module of the NTD.   Reflects counts of incidents, fatalities, injuries, fires, collisions, etc.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/pubs/MonthlyData/S&STimeSeriesDecember2011-04032012.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Time Series"
+                }
             ],
+            "identifier": "22.1",
+            "isPartOf": "DOT-22",
+            "issued": "2002-01-01",
             "keyword": [
                 "bicyclist",
                 "collision",
@@ -8262,81 +8277,43 @@
                 "transit",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NTD Program Support",
-                "hasEmail": "mailto:NTDHelp@dot.gov"
-            },
-            "identifier": "22.1",
+            "landingPage": "https://data.transportation.gov/d/4pyy-eqpe",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-03-05",
+            "phone": "202-366-5430",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Transit Administration"
             },
-            "description": "Summary (\"count\") data submitted to the Safety & Security Module of the NTD.   Reflects counts of incidents, fatalities, injuries, fires, collisions, etc.",
-            "title": "NTD Safety & Security Summary Data Set - Time Series",
-            "isPartOf": "DOT-22",
-            "agencyProgramURL": "http://www.ntdprogram.gov/",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/pubs/MonthlyData/S&STimeSeriesDecember2011-04032012.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "Time Series"
-                }
+            "references": [
+                "www.transit.dot.gov/ntd"
             ],
             "spatial": "Urbanized Zone",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.ntdprogram.gov/ntdprogram/data.htm",
+            "temporal": "R/2002-01-31/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Research",
-            "analysisUnit": "transit agency, mode, type of service",
-            "phone": "202-366-5430",
-            "language": [
-                "en-US"
-            ]
+            "title": "NTD Safety & Security Summary Data Set - Time Series"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/4qbx-egtn",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2020-07-23",
-            "@type": "dcat:Dataset",
-            "temporal": "2016-07-18/2016-07-25",
-            "modified": "2020-07-23",
-            "keyword": [
-                "car-following",
-                "freeway",
-                "instrumented research vehicle (irv)",
-                "microscopic modeling",
-                "microsimulation",
-                "springfield massachusetts",
-                "traffic simulation",
-                "work zone"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:Volpe_Dataset_POCs@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "US Department of Transportation"
-            },
-            "identifier": "https://data.transportation.gov/api/views/4qbx-egtn",
+            "dataQuality": true,
             "description": "The data describe freeway car-following behavior (such as velocity, acceleration, and relative position) for the car-following instances observed during 6 data collection runs, collected using an Instrumented Research Vehicle (IRV) along freeways and arterials in western Massachusetts in the summer of 2016 to better understand work zone driver behaviors. The USDOT Volpe National Transportation Systems Center (Volpe Center) identified, isolated, and classified individual car following instances from within the raw datasets (classification parameters included roadway type, level of congestion, and speed limit), then processed, refined, and cleaned the dataset.\n\nThis table contains the instantaneous data processed from radar and GPS. See also the instances table (https://datahub.transportation.gov/Automobiles/Enhancing-Microsimulation-Models-for-Improved-Work/b3k6-qwyh) and runs table (https://datahub.transportation.gov/Automobiles/Enhancing-Microsimulation-Models-for-Improved-Work/74ug-57tr).",
-            "title": "Enhancing Microsimulation Models for Improved Work Zone Planning: Car-Following Data from Western Massachusetts (Radar Points)",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8344,79 +8321,113 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/4qbx-egtn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/4qbx-egtn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/4qbx-egtn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/4qbx-egtn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/4qbx-egtn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/4qbx-egtn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/4qbx-egtn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/4qbx-egtn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/4qbx-egtn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "-72.5339,42.0211,-72.6494,42.3927",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/4qbx-egtn",
+            "issued": "2020-07-23",
+            "keyword": [
+                "car-following",
+                "freeway",
+                "instrumented research vehicle (irv)",
+                "microscopic modeling",
+                "microsimulation",
+                "springfield massachusetts",
+                "traffic simulation",
+                "work zone"
+            ],
+            "landingPage": "https://data.transportation.gov/d/4qbx-egtn",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2020-07-23",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
+            "spatial": "-72.5339,42.0211,-72.6494,42.3927",
+            "temporal": "2016-07-18/2016-07-25",
             "theme": [
                 "Automobiles"
-            ]
+            ],
+            "title": "Enhancing Microsimulation Models for Improved Work Zone Planning: Car-Following Data from Western Massachusetts (Radar Points)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/4qdb-2zsm",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2025-01-02",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-02",
-            "keyword": [
-                "monthly transportation statistics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:answers@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/4qdb-2zsm",
             "description": "Light trucks include trucks with up to 14,000 pounds gross vehicle weight, including minivans and sport utility vehicles. Prior to the 2003 Benchmark Revision, light trucks were up to 10,000 pounds. The U.S. Bureau of Economic Analysis releases auto and truck sales data, which are used in the preparation of estimates of personal consumption expenditures.",
-            "title": "Light Truck Sales",
+            "identifier": "https://data.transportation.gov/api/views/4qdb-2zsm",
+            "issued": "2025-01-02",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/4qdb-2zsm",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-02",
             "programCode": [
                 "021:053"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Research and Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Light Truck Sales"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/4qzi-thur",
             "bureauCode": [
                 "021:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kate Hartman",
+                "hasEmail": "mailto:kate.hartman@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "As part of the Federal Highway Administration\u2019s (FHWA) Next Generation Simulation (NGSIM) project, video data was collected on a freeway segment of US 101 (Hollywood Freeway) located in Los Angeles, California on June 15th, 2005. A total of 45 minutes of transcribed data are included in this full data set, segmented into three 15 minute periods representing: 1) 7:50 a.m. to 8:05 a.m., 2) 8:05 a.m. to 8:20 a.m., and 3) 8:20 a.m. to 8:35 a.m. on June 15th, 2005. The dataset includes files for both raw and processed video data from each of the eight cameras for the three time periods available for download. Camera numbering is in order of southern-most (1) to northern-most (8). The raw video files give the original vehicle movement data and offer users a view of how the section was observed. The processed video files provide videos of the vehicles along with a superimposition of the vehicle identification numbers. These videos can be used alone or can be used for cross referencing of the textual vehicle trajectory data provided in the NGSIM trajectory data with the corresponding video.\n\nFor related datasets please see the following:\n- NGSIM Vehicle Trajectories and Supporting Data: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Vehicle-Trajector/8ect-6jqj\n- NGSIM I-80 Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-I-80-Vide/2577-gpny\n- NGSIM Lankershim Boulevard Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-Lankershi/uv3e-y54k\n- NGSIM Peachtree Street Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-Peachtree/mupt-aksf",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/download/4qzi-thur/application/pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/4qzi-thur",
             "issued": "2016-01-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2005-06-15",
-            "modified": "2016-01-01",
             "keyword": [
                 "california",
                 "freeway",
@@ -8427,49 +8438,56 @@
                 "us 101",
                 "video"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/4qzi-thur",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://creativecommons.org/licenses/by-sa/4.0/legalcode",
+            "modified": "2016-01-01",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Department of Transportation"
             },
-            "identifier": "https://data.transportation.gov/api/views/4qzi-thur",
-            "description": "As part of the Federal Highway Administration\u2019s (FHWA) Next Generation Simulation (NGSIM) project, video data was collected on a freeway segment of US 101 (Hollywood Freeway) located in Los Angeles, California on June 15th, 2005. A total of 45 minutes of transcribed data are included in this full data set, segmented into three 15 minute periods representing: 1) 7:50 a.m. to 8:05 a.m., 2) 8:05 a.m. to 8:20 a.m., and 3) 8:20 a.m. to 8:35 a.m. on June 15th, 2005. The dataset includes files for both raw and processed video data from each of the eight cameras for the three time periods available for download. Camera numbering is in order of southern-most (1) to northern-most (8). The raw video files give the original vehicle movement data and offer users a view of how the section was observed. The processed video files provide videos of the vehicles along with a superimposition of the vehicle identification numbers. These videos can be used alone or can be used for cross referencing of the textual vehicle trajectory data provided in the NGSIM trajectory data with the corresponding video.\n\nFor related datasets please see the following:\n- NGSIM Vehicle Trajectories and Supporting Data: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Vehicle-Trajector/8ect-6jqj\n- NGSIM I-80 Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-I-80-Vide/2577-gpny\n- NGSIM Lankershim Boulevard Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-Lankershi/uv3e-y54k\n- NGSIM Peachtree Street Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-Peachtree/mupt-aksf",
-            "title": "Next Generation Simulation (NGSIM) Program US-101 Videos",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/download/4qzi-thur/application/pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
             "spatial": "Los Angeles, California",
-            "dataQuality": true,
-            "license": "http://creativecommons.org/licenses/by-sa/4.0/legalcode",
+            "temporal": "2005-06-15",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Next Generation Simulation (NGSIM) Program US-101 Videos"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/4r5p-2hwx",
-            "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": false,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
+            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "2013 Pennsylvania HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/pennsylvania2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Pennsylvania"
+                }
+            ],
+            "identifier": "678.142",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -8483,60 +8501,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.142",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Pennsylvania",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/4r5p-2hwx",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5035",
             "primaryITInvestmentUII": "021-099281808",
             "programCode": [
                 "021:009"
             ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/pennsylvania2013.zip",
-                    "description": "2013 Pennsylvania HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Pennsylvania"
-                }
-            ],
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "temporal": "R/1981-11-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
-            "categoryDesignation": "Administrative",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-5035"
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Pennsylvania"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/PT1S",
+            "agencyDataSeriesURL": "http://www.nhtsa.gov/Vehicle+Safety",
+            "agencyProgramURL": "http://vpic.nhtsa.dot.gov/",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/4s54-783t",
-            "issued": "2015-10-05",
-            "temporal": "R/2015-10-05/PT1S",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Administrative - Regulatory",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://vpic.nhtsa.dot.gov/"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The NHTSA Product Information Catalog and Vehicle Listing (vPIC) is a consolidated platform that presents data collected within the manufacturer reported data from CFR 49 Parts 551 - 574 for use in a variety of modern tools. NHTSA's vPIC platform is intended to serve as a centralized source for basic Vehicle Identification Number (VIN) decoding, Manufacturer Information Database (MID), Manufacturer Equipment Plant Identification and associated data. vPIC is intended to support the Open Data and Transparency initiatives of the agency by allowing the data to be freely used by the public without the burden of manual retrieval from a library of electronic documents (PDFs). While these documents will still be available online for viewing within the Manufacturer Information Database (MID) module of vPIC one can view and use the actual data through the VIN Decoder and Application Programming Interface (API) modules.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Manufacturer Information Database",
+                    "downloadURL": "http://vpic.nhtsa.dot.gov/mid",
+                    "mediaType": "text/html",
+                    "title": "MID"
+                }
             ],
+            "identifier": "65.2",
+            "isPartOf": "DOT-65",
+            "issued": "2015-10-05",
             "keyword": [
                 "49",
                 "551",
@@ -8573,56 +8588,45 @@
                 "vin",
                 "vpic"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "65.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "The NHTSA Product Information Catalog and Vehicle Listing (vPIC) is a consolidated platform that presents data collected within the manufacturer reported data from CFR 49 Parts 551 - 574 for use in a variety of modern tools. NHTSA's vPIC platform is intended to serve as a centralized source for basic Vehicle Identification Number (VIN) decoding, Manufacturer Information Database (MID), Manufacturer Equipment Plant Identification and associated data. vPIC is intended to support the Open Data and Transparency initiatives of the agency by allowing the data to be freely used by the public without the burden of manual retrieval from a library of electronic documents (PDFs). While these documents will still be available online for viewing within the Manufacturer Information Database (MID) module of vPIC one can view and use the actual data through the VIN Decoder and Application Programming Interface (API) modules.",
-            "title": "NHTSA Product Information Catalog and Vehicle Listing (vPIC) - MID",
-            "isPartOf": "DOT-65",
-            "agencyProgramURL": "http://vpic.nhtsa.dot.gov/",
+            "landingPage": "https://data.transportation.gov/d/4s54-783t",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-01",
+            "phone": "202-366-2622",
             "primaryITInvestmentUII": "021-430297065",
             "programCode": [
                 "021:031"
             ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://vpic.nhtsa.dot.gov/mid",
-                    "description": "Manufacturer Information Database",
-                    "@type": "dcat:Distribution",
-                    "title": "MID"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "http://vpic.nhtsa.dot.gov/"
             ],
             "spatial": "NA",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.nhtsa.gov/Vehicle+Safety",
+            "temporal": "R/2015-10-05/PT1S",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/PT1S",
-            "categoryDesignation": "Administrative - Regulatory",
-            "phone": "202-366-2622",
-            "language": [
-                "en-US"
-            ]
+            "title": "NHTSA Product Information Catalog and Vehicle Listing (vPIC) - MID"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/4s7k-yxvu",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Transportation Analysis",
+                "hasEmail": "mailto:long.nguyen@dot.gov"
+            },
+            "description": "Freight Facts and Figures - International Freight Gateways in the United States",
+            "identifier": "https://data.transportation.gov/api/views/4s7k-yxvu",
             "issued": "2019-09-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-02-14",
             "keyword": [
                 "bts",
                 "bureau of transportation statistics",
@@ -8633,57 +8637,38 @@
                 "freight transportation",
                 "international trade"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Transportation Analysis",
-                "hasEmail": "mailto:long.nguyen@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/4s7k-yxvu",
+            "modified": "2024-02-14",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statisitics"
             },
-            "identifier": "https://data.transportation.gov/api/views/4s7k-yxvu",
-            "description": "Freight Facts and Figures - International Freight Gateways in the United States",
-            "title": "International Freight Gateways",
-            "programCode": [
-                "021:053"
-            ],
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "International Freight Gateways"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://nhts.ornl.gov/index.shtml",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/4scv-3egc",
-            "issued": "1969-01-01",
-            "temporal": "1969-01-01/2014-12-29",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
-            "keyword": [
-                "demographics",
-                "driver",
-                "travel"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "682.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": false,
+            "describedBy": "http://nhts.ornl.gov/publications.shtml",
             "description": "The National Household Travel Survey provides information to assist transportation planners and policy makers who need comprehensive data on travel and transportation patterns in the United States",
-            "title": "National Household Travel Survey - Download data",
-            "isPartOf": "DOT-682",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8692,59 +8677,54 @@
                     "title": "Download data"
                 }
             ],
-            "describedBy": "http://nhts.ornl.gov/publications.shtml",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "682.1",
+            "isPartOf": "DOT-682",
+            "issued": "1969-01-01",
+            "keyword": [
+                "demographics",
+                "driver",
+                "travel"
             ],
-            "accrualPeriodicity": "irregular",
-            "agencyDataSeriesURL": "http://nhts.ornl.gov/index.shtml",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/4scv-3egc",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-5021"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5021",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "temporal": "1969-01-01/2014-12-29",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "National Household Travel Survey - Download data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Protected under the Privacy Act of 1974; see System of Records Notice for more information.",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.civilrights.dot.gov/node/3828",
+            "agencyProgramURL": "http://www.civilrights.dot.gov",
+            "analysisUnit": "complaint",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/4srv-g9em",
-            "issued": "2014-11-03",
-            "temporal": "R/2010-01-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "references": [
-                "https://www.civilrights.dot.gov/node/3828"
-            ],
-            "keyword": [
-                "discrminiation",
-                "employment",
-                "equal",
-                "no fear act",
-                "opportunity",
-                "whistleblower"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "DOT-557",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
+            "describedBy": "https://www.civilrights.dot.gov/node/3828",
             "description": "Data related to the management of EEO complaint processing.  Due to the presence of PII, the raw data is not available for public consumption.  However, aggregated data is available in the DOT's NoFEAR Act report and Form 462 Report.  Both are located on the DOT Office of Civil Rights' public website.",
-            "title": "EEO Complaint Processing Data",
-            "agencyProgramURL": "http://www.civilrights.dot.gov",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8753,30 +8733,54 @@
                     "title": "2010 No FEAR Act Report"
                 }
             ],
-            "describedBy": "https://www.civilrights.dot.gov/node/3828",
-            "dataQuality": false,
+            "identifier": "DOT-557",
+            "issued": "2014-11-03",
+            "keyword": [
+                "discrminiation",
+                "employment",
+                "equal",
+                "no fear act",
+                "opportunity",
+                "whistleblower"
+            ],
+            "landingPage": "https://data.transportation.gov/d/4srv-g9em",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "https://www.civilrights.dot.gov/node/3828",
+            "modified": "2024-11-14",
+            "phone": "202-366-8741",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "references": [
+                "https://www.civilrights.dot.gov/node/3828"
+            ],
+            "rights": "Protected under the Privacy Act of 1974; see System of Records Notice for more information.",
+            "temporal": "R/2010-01-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "complaint",
-            "phone": "202-366-8741",
-            "language": [
-                "en-US"
-            ]
+            "title": "EEO Complaint Processing Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/4t5g-bu96",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Tool to view data from the Transportation Satellite Accounts (TSAs). The TSAs provide a comprehensive means for measuring the contribution of transportation services to the national economy. The TSAs capture transportation activities carried out by: (1) the for-hire transportation sector for a fee, (2) non-transportation industries for their own purposes, and (3) households using a personal vehicle.",
+            "identifier": "https://data.transportation.gov/api/views/4t5g-bu96",
             "issued": "2024-07-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-05",
             "keyword": [
                 "contribution of transportation",
                 "economics",
@@ -8785,52 +8789,33 @@
                 "transportation",
                 "value of transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/4t5g-bu96",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-12-05",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/4t5g-bu96",
-            "description": "Tool to view data from the Transportation Satellite Accounts (TSAs). The TSAs provide a comprehensive means for measuring the contribution of transportation services to the national economy. The TSAs capture transportation activities carried out by: (1) the for-hire transportation sector for a fee, (2) non-transportation industries for their own purposes, and (3) households using a personal vehicle.",
-            "title": "Transportation Satellite Accounts Tables",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Transportation Satellite Accounts Tables"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/4tmr-gwuu",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-09-05",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
-            "keyword": [
-                "capital expenses",
-                "funding",
-                "operating expenses"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NTD Program Support",
                 "hasEmail": "mailto:NTDHelp@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Transit Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/4tmr-gwuu",
             "description": "This dataset details funding sources for each applicable agency reporting to the National Transit Database in the 2022 and 2023 report years, split by fund expenditure type: capital and operating.\n\nNTD Data Tables organize and summarize data from the 2022 and 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. This dataset is based on the 2022 and 2023 Revenue Sources database files.\n\nIn years 2015-2021, you can find this data in the \"Funding Sources\" data table on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.\n\nIf you have any other questions about this table, please contact the NTD Help Desk at NTDHelp@dot.gov.",
-            "title": "2022 - 2023 NTD Annual Data - Funding Sources (by Expense Type)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8838,46 +8823,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/4tmr-gwuu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/4tmr-gwuu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/4tmr-gwuu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/4tmr-gwuu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/4tmr-gwuu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/4tmr-gwuu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/4tmr-gwuu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/4tmr-gwuu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/4tmr-gwuu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/4tmr-gwuu",
+            "issued": "2024-09-05",
+            "keyword": [
+                "capital expenses",
+                "funding",
+                "operating expenses"
+            ],
+            "landingPage": "https://data.transportation.gov/d/4tmr-gwuu",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-12-16",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Transit Administration"
+            },
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "2022 - 2023 NTD Annual Data - Funding Sources (by Expense Type)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www.dot.gov/foia/foia-electronic-reading-room-category-one",
+            "agencyProgramURL": "http://www.dot.gov/foia/foia-electronic-reading-room-category-one",
+            "analysisUnit": "Regulated Entity",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/4uc4-5jfk",
-            "issued": "2011-01-18",
-            "temporal": "1996-01-01/2011-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.dot.gov/foia/foia-electronic-reading-room-category-one"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DOT Socrata",
+                "hasEmail": "mailto:Socrata@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Administrative Law Judge Opinions from the Office of the Secretary of Transportation may include, but are not limited to, Aviation Safety Civil Penalty Decisions, Hazardous Materials Safety Civil Penalty Decisions, Motor Carrier Safety Civil Penalty Decisions, Airport-Airline Fees/Rates and Charges Decisions, Aviation Economic Violation Enforcement Proceedings, Aviation Economic Orders and Decisions, Airline Prices/Routes/Services Preemption Decisions, Aviation Enforcement Consent Orders, and Aviation Economic Decisions",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.dot.gov/foia/foia-electronic-reading-room-category-one",
+                    "mediaType": "text/html"
+                }
             ],
+            "identifier": "DOT-322",
+            "issued": "2011-01-18",
             "keyword": [
                 "administrative law judge opinions",
                 "airline citizenship",
@@ -8894,57 +8907,60 @@
                 "motor carriers",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DOT Socrata",
-                "hasEmail": "mailto:Socrata@dot.gov"
-            },
-            "identifier": "DOT-322",
+            "landingPage": "https://data.transportation.gov/d/4uc4-5jfk",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-14",
+            "phone": "202-366-4308",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Secretary of Transportation"
             },
-            "description": "Administrative Law Judge Opinions from the Office of the Secretary of Transportation may include, but are not limited to, Aviation Safety Civil Penalty Decisions, Hazardous Materials Safety Civil Penalty Decisions, Motor Carrier Safety Civil Penalty Decisions, Airport-Airline Fees/Rates and Charges Decisions, Aviation Economic Violation Enforcement Proceedings, Aviation Economic Orders and Decisions, Airline Prices/Routes/Services Preemption Decisions, Aviation Enforcement Consent Orders, and Aviation Economic Decisions",
-            "title": "Administrative Law Judge Opinions issued by the Office of the Secretary of Transportation",
-            "agencyProgramURL": "http://www.dot.gov/foia/foia-electronic-reading-room-category-one",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.dot.gov/foia/foia-electronic-reading-room-category-one",
-                    "mediaType": "text/html"
-                }
+            "references": [
+                "http://www.dot.gov/foia/foia-electronic-reading-room-category-one"
             ],
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.dot.gov/foia/foia-electronic-reading-room-category-one",
+            "temporal": "1996-01-01/2011-01-18",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "analysisUnit": "Regulated Entity",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4308",
-            "language": [
-                "en-US"
-            ]
+            "title": "Administrative Law Judge Opinions issued by the Office of the Secretary of Transportation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.ntdprogram.gov/ntdprogram/data.htm",
+            "agencyProgramURL": "http://www.ntdprogram.gov",
+            "analysisUnit": "Transit Agency, some data by Mode and Type of Service",
             "bureauCode": [
                 "021:36"
             ],
-            "landingPage": "https://data.transportation.gov/d/4whr-qn3u",
-            "issued": "2010-10-01",
-            "temporal": "R/1996-12-31/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-05",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.ntdprogram.gov"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John D. Giorgis",
+                "hasEmail": "mailto:john.giorgis@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www.ntdprogram.gov/ntdprogram/data.htm",
+            "description": "Data reported to the NTD by urbanized area transit systems in their annual reports.   Includes contact information, contractural relationshps, subrecipient informatino, service area, sources of funds, operating expenditures by object class and function, capital expenditures by object class and function, fixed guideway information, revenue vehicle inventory, fuel consumption, employees, and labor hours, and urbanized area allocation information.   Also includes service supplied and consumed by annual total, average weekday, average saturday, and average sunday.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2009_database/NTD_database_2009.exe",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2009 Database"
+                }
             ],
+            "identifier": "21.13",
+            "isPartOf": "DOT-21",
+            "issued": "2010-10-01",
             "keyword": [
                 "agency",
                 "allocation",
@@ -8963,58 +8979,60 @@
                 "urbanized",
                 "vehicles"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John D. Giorgis",
-                "hasEmail": "mailto:john.giorgis@dot.gov"
-            },
-            "identifier": "21.13",
+            "landingPage": "https://data.transportation.gov/d/4whr-qn3u",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-03-05",
+            "phone": "202-366-5430",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Transit Administration"
             },
-            "description": "Data reported to the NTD by urbanized area transit systems in their annual reports.   Includes contact information, contractural relationshps, subrecipient informatino, service area, sources of funds, operating expenditures by object class and function, capital expenditures by object class and function, fixed guideway information, revenue vehicle inventory, fuel consumption, employees, and labor hours, and urbanized area allocation information.   Also includes service supplied and consumed by annual total, average weekday, average saturday, and average sunday.",
-            "title": "NTD Annual Module Data Set - 2009 Database",
-            "isPartOf": "DOT-21",
-            "agencyProgramURL": "http://www.ntdprogram.gov",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2009_database/NTD_database_2009.exe",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "2009 Database"
-                }
+            "references": [
+                "http://www.ntdprogram.gov"
             ],
             "spatial": "Urbanized Areas",
-            "describedBy": "http://www.ntdprogram.gov/ntdprogram/data.htm",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.ntdprogram.gov/ntdprogram/data.htm",
+            "temporal": "R/1996-12-31/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Transit Agency, some data by Mode and Type of Service",
-            "phone": "202-366-5430",
-            "language": [
-                "en-US"
-            ]
+            "title": "NTD Annual Module Data Set - 2009 Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/4xcs-96jz",
-            "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": false,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
+            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "2013 Tennessee HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/tennessee2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Tennessee"
+                }
+            ],
+            "identifier": "678.146",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -9028,60 +9046,58 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.146",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Tennessee",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/4xcs-96jz",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5035",
             "primaryITInvestmentUII": "021-099281808",
             "programCode": [
                 "021:009"
             ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/tennessee2013.zip",
-                    "description": "2013 Tennessee HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Tennessee"
-                }
-            ],
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "temporal": "R/1981-11-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
-            "categoryDesignation": "Administrative",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-5035"
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Tennessee"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/on_the_fly_download.aspx",
+            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
+            "analysisUnit": "57 Filing",
             "bureauCode": [
                 "021:27"
             ],
-            "landingPage": "https://data.transportation.gov/d/4xwn-zpj5",
-            "issued": "2010-09-29",
-            "temporal": "R/1975-01-31/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-09",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "https://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Newregulation.aspx%3Fdoc=FRAGuideforPreparingAccIncReportspubMay2011.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/DownloadFStructure.aspx",
+            "description": "This file contains reported cases of impacts between on-track equipment and any user of a public or private highway-rail intersection. National files from 1975 through the current year are available for download. In addition, individual files by State are available for the years 1991 through the current year.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/gxrtally1.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Highway-Rail Crossings"
+                }
             ],
+            "identifier": "214.8",
+            "isPartOf": "DOT-214",
+            "issued": "2010-09-29",
             "keyword": [
                 "accident",
                 "casualty",
@@ -9094,75 +9110,43 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "214.8",
+            "landingPage": "https://data.transportation.gov/d/4xwn-zpj5",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-10-09",
+            "phone": "202-493-6483",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Railroad Administration"
             },
-            "description": "This file contains reported cases of impacts between on-track equipment and any user of a public or private highway-rail intersection. National files from 1975 through the current year are available for download. In addition, individual files by State are available for the years 1991 through the current year.",
-            "title": "Highway Rail Accidents - Highway-Rail Crossings",
-            "isPartOf": "DOT-214",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/gxrtally1.aspx",
-                    "mediaType": "text/csv",
-                    "title": "Highway-Rail Crossings"
-                }
+            "references": [
+                "https://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Newregulation.aspx%3Fdoc=FRAGuideforPreparingAccIncReportspubMay2011.pdf"
             ],
             "spatial": "Latitude/Longitude, County, State",
-            "describedBy": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/DownloadFStructure.aspx",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/on_the_fly_download.aspx",
+            "temporal": "R/1975-01-31/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Research",
-            "analysisUnit": "57 Filing",
-            "phone": "202-493-6483",
-            "language": [
-                "en-US"
-            ]
+            "title": "Highway Rail Accidents - Highway-Rail Crossings"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2021-04-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "traffic",
-                "traffic volume trends"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/4z2n-nkpd",
+            "dataQuality": true,
             "description": "2018 Traffic Volume Data - FHWA's TMAS Data Program (based on unweighted raw continuous traffic count information collected by state highway agencies)",
-            "title": "TMAS 2018",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9170,67 +9154,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/4z2n-nkpd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/4z2n-nkpd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/4z2n-nkpd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/4z2n-nkpd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/4z2n-nkpd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/4z2n-nkpd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/4z2n-nkpd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/4z2n-nkpd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/4z2n-nkpd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/4z2n-nkpd",
+            "issued": "2021-04-29",
+            "keyword": [
+                "traffic",
+                "traffic volume trends"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-05-08",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "spatial": "United States",
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TMAS 2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/4zfz-amsd",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2017-01-03",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-28",
-            "keyword": [
-                "innovation",
-                "its joint program office",
-                "smart city challenge",
-                "technology"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kate Hartman",
                 "hasEmail": "mailto:kate.hartman@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "USDOT"
-            },
-            "identifier": "https://data.transportation.gov/api/views/4zfz-amsd",
+            "dataQuality": true,
             "description": "Analysis of the projects proposed by the seven finalists to USDOT's Smart City Challenge, including challenge addressed, proposed project category, and project description.\r\n\r\nThe time reported for the speed profiles are between 2:00PM to 8:00PM in increments of 10 minutes.",
-            "title": "Smart City Challenge Finalists Project Proposals - Calibration Data",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9238,45 +9221,80 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/4zfz-amsd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/4zfz-amsd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/4zfz-amsd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/4zfz-amsd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/4zfz-amsd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/4zfz-amsd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/4zfz-amsd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/4zfz-amsd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/4zfz-amsd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/4zfz-amsd",
+            "issued": "2017-01-03",
+            "keyword": [
+                "innovation",
+                "its joint program office",
+                "smart city challenge",
+                "technology"
+            ],
+            "landingPage": "https://data.transportation.gov/d/4zfz-amsd",
+            "modified": "2024-09-28",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "USDOT"
+            },
             "spatial": "I-15, San Diego, California",
-            "dataQuality": true,
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Smart City Challenge Finalists Project Proposals - Calibration Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/4zgf-h99c",
-            "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": false,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
+            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "2012 New York HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/newyork2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 New York"
+                }
+            ],
+            "identifier": "678.86",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -9290,73 +9308,40 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.86",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 New York",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/4zgf-h99c",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5035",
             "primaryITInvestmentUII": "021-099281808",
             "programCode": [
                 "021:009"
             ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/newyork2012.zip",
-                    "description": "2012 New York HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 New York"
-                }
-            ],
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "temporal": "R/1981-11-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
-            "categoryDesignation": "Administrative",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-5035"
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 New York"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/5228-kdbw",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2020-12-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "references": [
-                "https://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/5228-kdbw",
+            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
             "description": "State DOTs will provide Local and Rural Minor Collector Mileage summarized by county, ownership, and Paved and Unpaved. This data is provided in a direct input by the State DOTs.",
-            "title": "County Summary 2018",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9364,76 +9349,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5228-kdbw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5228-kdbw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5228-kdbw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/5228-kdbw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5228-kdbw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5228-kdbw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5228-kdbw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5228-kdbw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5228-kdbw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "USA",
-            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
+            "identifier": "https://data.transportation.gov/api/views/5228-kdbw",
+            "issued": "2020-12-08",
+            "landingPage": "https://data.transportation.gov/d/5228-kdbw",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-05-08",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "references": [
+                "https://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/"
+            ],
+            "spatial": "USA",
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "County Summary 2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www.fra.dot.gov/Pages/350.shtml",
+            "agencyProgramURL": "http://www.fra.dot.gov/Pages/350.shtml",
+            "analysisUnit": "Regulated Entity",
             "bureauCode": [
                 "021:27"
             ],
-            "landingPage": "https://data.transportation.gov/d/536g-avix",
-            "issued": "2011-01-18",
-            "temporal": "1996-01-01/2011-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-09",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.fra.dot.gov/Pages/350.shtml"
-            ],
-            "keyword": [
-                "data.gov",
-                "interpretation",
-                "law",
-                "railroad",
-                "safety",
-                "transportation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Railroad Safety",
                 "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
             },
-            "identifier": "308.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Railroad Administration"
-            },
+            "dataQuality": true,
             "description": "Railroad Safety Advisories issued by the Federal Railroad Administration",
-            "title": "Railroad Safety Advisories -",
-            "isPartOf": "DOT-308",
-            "agencyProgramURL": "http://www.fra.dot.gov/Pages/350.shtml",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9441,34 +9420,71 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "308.2",
+            "isPartOf": "DOT-308",
+            "issued": "2011-01-18",
+            "keyword": [
+                "data.gov",
+                "interpretation",
+                "law",
+                "railroad",
+                "safety",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/536g-avix",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.fra.dot.gov/Pages/350.shtml",
+            "modified": "2024-10-09",
+            "phone": "202-366-4308",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Railroad Administration"
+            },
+            "references": [
+                "http://www.fra.dot.gov/Pages/350.shtml"
+            ],
+            "temporal": "1996-01-01/2011-01-18",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "analysisUnit": "Regulated Entity",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4308",
-            "language": [
-                "en-US"
-            ]
+            "title": "Railroad Safety Advisories -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://www.fra.dot.gov/Page/P0604",
+            "agencyProgramURL": "http://www.fra.dot.gov/Page/P0068",
+            "analysisUnit": "Employee",
             "bureauCode": [
                 "021:27"
             ],
-            "landingPage": "https://data.transportation.gov/d/54jz-hfs6",
-            "issued": "2008-03-01",
-            "temporal": "2003-01-01/2010-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-09",
+            "categoryDesignation": "Research",
             "collectionInstrument": "http://www.fra.dot.gov/Page/P0604",
-            "references": [
-                "http://www.fra.dot.gov/Page/P0604"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www.fra.dot.gov/Page/P0604",
+            "description": "The Federal Railroad Administration (FRA) sponsored a study of the work schedules and sleep patterns of railroad employees. The purpose of the study was to understand work-schedule related fatigue that affects various categories of railroad employees by documenting a group's work/rest schedules and sleep patterns to ascertain their impact on the level of fatigue/alertness.Employees surveyed include: signalmen, maintenance of way (MOW) workers, dispatchers, and train & engine service workers (in both freight and passenger train service)",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fra.dot.gov/eLib/Details/L04109",
+                    "mediaType": "text/csv",
+                    "title": "Maintenance of Way Daily Log"
+                }
             ],
+            "identifier": "283.4",
+            "isPartOf": "DOT-283",
+            "issued": "2008-03-01",
             "keyword": [
                 "alertness",
                 "employee",
@@ -9479,59 +9495,54 @@
                 "sleep",
                 "work"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "283.4",
+            "landingPage": "https://data.transportation.gov/d/54jz-hfs6",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-10-09",
+            "phone": "202-493-6356",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Railroad Administration"
             },
-            "description": "The Federal Railroad Administration (FRA) sponsored a study of the work schedules and sleep patterns of railroad employees. The purpose of the study was to understand work-schedule related fatigue that affects various categories of railroad employees by documenting a group's work/rest schedules and sleep patterns to ascertain their impact on the level of fatigue/alertness.Employees surveyed include: signalmen, maintenance of way (MOW) workers, dispatchers, and train & engine service workers (in both freight and passenger train service)",
-            "title": "Work Schedules and Sleep Patterns of Railroad Employees - Maintenance of Way Daily Log",
-            "isPartOf": "DOT-283",
-            "agencyProgramURL": "http://www.fra.dot.gov/Page/P0068",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fra.dot.gov/eLib/Details/L04109",
-                    "mediaType": "text/csv",
-                    "title": "Maintenance of Way Daily Log"
-                }
+            "references": [
+                "http://www.fra.dot.gov/Page/P0604"
             ],
             "spatial": "N/A",
-            "describedBy": "http://www.fra.dot.gov/Page/P0604",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fra.dot.gov/Page/P0604",
+            "temporal": "2003-01-01/2010-12-31",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Employee",
-            "phone": "202-493-6356",
-            "language": [
-                "en-US"
-            ]
+            "title": "Work Schedules and Sleep Patterns of Railroad Employees - Maintenance of Way Daily Log"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.21949/1503767",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2014-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2016-12-21",
-            "references": [
-                "https://rosap.ntl.bts.gov/view/dot/3608"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Transportation Library Data Curator",
+                "hasEmail": "mailto:ntldatacurator@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The objective of this project was to develop system designs for programs to monitor travel time reliability and to prepare a guidebook that practitioners and others can use to design, build, operate, and maintain such systems. Generally, such travel time reliability monitoring systems will be built on top of existing traffic monitoring systems. The focus of this project was on travel time reliability. The data from the monitoring systems developed in this project \u2013 from both public and private sources \u2013included, wherever cost-effective, information on the seven sources of non-recurring congestion. This data was used to construct performance measures or to perform various types of analyses useful for operations management as well as performance measurement, planning, and programming.  The datasets in the attached ZIP file support SHRP 2 reliability project L38B, \"Pilot testing of SHRP 2 reliability data and analytical products: Minnesota.\" This report can be accessed via the following URL: https://rosap.ntl.bts.gov/view/dot/3608  This ZIP file package, which is 22.1 MB in size, contains 6 Microsoft Excel spreadsheet files (XLSX). This file package also contains 3 Comma Separated Value files (CSV). The XLSX and CSV files can be opened using Microsoft Excel 2010 and 2016. The CSV files can be opened using most available text editing programs.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The objective of this project was to develop system designs for programs to monitor travel time reliability and to prepare a guidebook that practitioners and others can use to design, build, operate, and maintain such systems. Generally, such travel time reliability monitoring systems will be built on top of existing traffic monitoring systems. The focus of this project was on travel time reliability. The data from the monitoring systems developed in this project \u2013 from both public and private sources \u2013included, wherever cost-effective, information on the seven sources of non-recurring congestion. This data was used to construct performance measures or to perform various types of analyses useful for operations management as well as performance measurement, planning, and programming.  The datasets in the attached ZIP file support SHRP 2 reliability project L38B, \"Pilot testing of SHRP 2 reliability data and analytical products: Minnesota.\" This report can be accessed via the following URL: https://rosap.ntl.bts.gov/view/dot/3608  This ZIP file package, which is 22.1 MB in size, contains 6 Microsoft Excel spreadsheet files (XLSX). This file package also contains 3 Comma Separated Value files (CSV). The XLSX and CSV files can be opened using Microsoft Excel 2010 and 2016. The CSV files can be opened using most available text editing programs.",
+                    "downloadURL": "https://doi.org/10.21949/1503767",
+                    "mediaType": "application/zip",
+                    "title": "Pilot Testing of SHRP 2 Reliability Data and Analytical Products: Minnesota [supporting datasets]"
+                }
             ],
+            "identifier": "https://data.transportation.gov/api/views/55c5-8teh",
+            "issued": "2014-01-01",
             "keyword": [
                 "business practices",
                 "data analysis",
@@ -9541,67 +9552,37 @@
                 "shrp2 project l38b",
                 "strategic highway research program 2"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Transportation Library Data Curator",
-                "hasEmail": "mailto:ntldatacurator@dot.gov"
-            },
+            "landingPage": "https://doi.org/10.21949/1503767",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2016-12-21",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/55c5-8teh",
-            "description": "The objective of this project was to develop system designs for programs to monitor travel time reliability and to prepare a guidebook that practitioners and others can use to design, build, operate, and maintain such systems. Generally, such travel time reliability monitoring systems will be built on top of existing traffic monitoring systems. The focus of this project was on travel time reliability. The data from the monitoring systems developed in this project \u2013 from both public and private sources \u2013included, wherever cost-effective, information on the seven sources of non-recurring congestion. This data was used to construct performance measures or to perform various types of analyses useful for operations management as well as performance measurement, planning, and programming.  The datasets in the attached ZIP file support SHRP 2 reliability project L38B, \"Pilot testing of SHRP 2 reliability data and analytical products: Minnesota.\" This report can be accessed via the following URL: https://rosap.ntl.bts.gov/view/dot/3608  This ZIP file package, which is 22.1 MB in size, contains 6 Microsoft Excel spreadsheet files (XLSX). This file package also contains 3 Comma Separated Value files (CSV). The XLSX and CSV files can be opened using Microsoft Excel 2010 and 2016. The CSV files can be opened using most available text editing programs.",
-            "title": "Pilot Testing of SHRP 2 Reliability Data and Analytical Products: Minnesota [supporting datasets]",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://doi.org/10.21949/1503767",
-                    "description": "The objective of this project was to develop system designs for programs to monitor travel time reliability and to prepare a guidebook that practitioners and others can use to design, build, operate, and maintain such systems. Generally, such travel time reliability monitoring systems will be built on top of existing traffic monitoring systems. The focus of this project was on travel time reliability. The data from the monitoring systems developed in this project \u2013 from both public and private sources \u2013included, wherever cost-effective, information on the seven sources of non-recurring congestion. This data was used to construct performance measures or to perform various types of analyses useful for operations management as well as performance measurement, planning, and programming.  The datasets in the attached ZIP file support SHRP 2 reliability project L38B, \"Pilot testing of SHRP 2 reliability data and analytical products: Minnesota.\" This report can be accessed via the following URL: https://rosap.ntl.bts.gov/view/dot/3608  This ZIP file package, which is 22.1 MB in size, contains 6 Microsoft Excel spreadsheet files (XLSX). This file package also contains 3 Comma Separated Value files (CSV). The XLSX and CSV files can be opened using Microsoft Excel 2010 and 2016. The CSV files can be opened using most available text editing programs.",
-                    "@type": "dcat:Distribution",
-                    "title": "Pilot Testing of SHRP 2 Reliability Data and Analytical Products: Minnesota [supporting datasets]"
-                }
+            "references": [
+                "https://rosap.ntl.bts.gov/view/dot/3608"
             ],
             "spatial": "United States, Minnesota",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "language": [
-                "en-US"
-            ]
+            "title": "Pilot Testing of SHRP 2 Reliability Data and Analytical Products: Minnesota [supporting datasets]"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/55zc-wayg",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2021-08-03",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
-            "keyword": [
-                "bridge",
-                "bridges",
-                "national transportation atlas database",
-                "ntad"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dominic Menegus",
                 "hasEmail": "mailto:dominic.menegus@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/55zc-wayg",
             "description": "The National Bridge Inventory (NBI) is a collection of information (database) describing the more than 615,000 of the Nation's bridges located on public roads as of December 31, 2020, including Interstate Highways, U.S. highways, State and county roads, as well as publicly-accessible bridges on Federal and Tribal lands. The inventory data present a complete picture of the location, description, classification, and general condition data for each bridge. Element condition data for bridges on the National Highway System (NHS) are contained in a separate layer. Bridges found to be located outside their respective state have been reassigned to coordinates 0, 0. Element condition data are contained in a separate layer.",
-            "title": "National Bridge Inventory -- Citizen Connect",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9609,41 +9590,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/55zc-wayg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/55zc-wayg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/55zc-wayg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/55zc-wayg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/55zc-wayg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/55zc-wayg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/55zc-wayg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/55zc-wayg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/55zc-wayg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/55zc-wayg",
+            "issued": "2021-08-03",
+            "keyword": [
+                "bridge",
+                "bridges",
+                "national transportation atlas database",
+                "ntad"
+            ],
+            "landingPage": "https://data.transportation.gov/d/55zc-wayg",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-13",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "National Bridge Inventory -- Citizen Connect"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/564e-eruw",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRA Safety Data Team",
+                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This is the report for Fatality, Injury, and Illness Map (4.07).",
+            "identifier": "https://data.transportation.gov/api/views/564e-eruw",
             "issued": "2024-08-19",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "casualties",
                 "casualty",
@@ -9661,41 +9666,54 @@
                 "trespassers",
                 "worker on duty"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRA Safety Data Team",
-                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/564e-eruw",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-27",
+            "programCode": [
+                "FRA Safety and Operations"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Railroad Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/564e-eruw",
-            "description": "This is the report for Fatality, Injury, and Illness Map (4.07).",
-            "title": "Fatality, Injury, and Illness Map (4.07)",
-            "programCode": [
-                "FRA Safety and Operations"
-            ],
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Railroads"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Fatality, Injury, and Illness Map (4.07)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/565y-ke6a",
-            "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": false,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
+            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "2013 Kansas HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/kansas2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Kansas"
+                }
+            ],
+            "identifier": "678.120",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -9709,79 +9727,75 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.120",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Kansas",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/565y-ke6a",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5035",
             "primaryITInvestmentUII": "021-099281808",
             "programCode": [
                 "021:009"
             ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/kansas2013.zip",
-                    "description": "2013 Kansas HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Kansas"
-                }
-            ],
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "temporal": "R/1981-11-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
-            "categoryDesignation": "Administrative",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-5035"
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Kansas"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/568r-4fsv",
-            "issued": "2020-06-26",
             "@type": "dcat:Dataset",
-            "modified": "2020-11-17",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alpha Wingfield",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/568r-4fsv",
+            "issued": "2020-06-26",
+            "landingPage": "https://data.transportation.gov/d/568r-4fsv",
+            "modified": "2020-11-17",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "What's a Decibel?"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
+            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/mapping/ssdq/",
+            "agencyProgramURL": "https://ai.fmcsa.dot.gov/DataQuality/",
+            "analysisUnit": "State data quality performance",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/568w-4dgg",
-            "issued": "2004-03-15",
-            "temporal": "R/2007-01-01/P3M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-29",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "https://ai.fmcsa.dot.gov/DataQuality/"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Data Quality identifies FMCSA resources for evaluating, monitoring, and improving the quality of data submitted by States to the Motor Carrier Management Information System (MCMIS).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://ai.fmcsa.dot.gov/mapping/ssdq/",
+                    "mediaType": "text/html",
+                    "title": "State Safety Data Quality Map"
+                }
             ],
+            "identifier": "DOT-113",
+            "issued": "2004-03-15",
             "keyword": [
                 "accuracy",
                 "completeness",
@@ -9798,94 +9812,95 @@
                 "state safety data quality map",
                 "timelines"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "DOT-113",
+            "landingPage": "https://data.transportation.gov/d/568w-4dgg",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-07-29",
+            "phone": "202-366-5387",
+            "programCode": [
+                "021:022"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Motor Carrier Safety Administration"
             },
-            "description": "Data Quality identifies FMCSA resources for evaluating, monitoring, and improving the quality of data submitted by States to the Motor Carrier Management Information System (MCMIS).",
-            "title": "A&I - Data Quality",
-            "agencyProgramURL": "https://ai.fmcsa.dot.gov/DataQuality/",
-            "programCode": [
-                "021:022"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://ai.fmcsa.dot.gov/mapping/ssdq/",
-                    "mediaType": "text/html",
-                    "title": "State Safety Data Quality Map"
-                }
+            "references": [
+                "https://ai.fmcsa.dot.gov/DataQuality/"
             ],
             "spatial": "State, National",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/mapping/ssdq/",
+            "temporal": "R/2007-01-01/P3M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P3M",
-            "analysisUnit": "State data quality performance",
-            "categoryDesignation": "Research",
-            "phone": "202-366-5387",
-            "language": [
-                "en-US"
-            ]
+            "title": "A&I - Data Quality"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/56fa-sf82",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2025-01-17",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
-            "keyword": [
-                "monthly transportation statistics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:answers@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/56fa-sf82",
             "description": "Percentage of flights arriving on-time. A flight is on-time if it arrives within 15 minutes of the schedule arrival time. Data are available for those carriers that had at least 1% of domestic enplanements in the previous year. The last 25 months of data include only carriers that reported in each of the last 25 months to retain comparability. Earlier data includes all reporting carriers. A scheduled operation consists of any nonstop segment of a flight.  The Bureau of Transportation Statistics air collects performance data from U.S. air carriers and international carriers operating within the U.S.",
-            "title": "U.S. Marketing Air Carriers On-time Performance",
+            "identifier": "https://data.transportation.gov/api/views/56fa-sf82",
+            "issued": "2025-01-17",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/56fa-sf82",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-17",
             "programCode": [
                 "021:053"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Research and Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "U.S. Marketing Air Carriers On-time Performance"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/56hp-d5bt",
-            "issued": "1970-01-01",
-            "temporal": "R/1970-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "State Traffic Monitoring Systems (TMS)",
-            "references": [
-                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/13augtvt/13augtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "August 2013"
+                }
             ],
+            "identifier": "18.53",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -9895,76 +9910,42 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.53",
+            "landingPage": "https://data.transportation.gov/d/56hp-d5bt",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-1067",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - August 2013",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/13augtvt/13augtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "August 2013"
-                }
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
             ],
             "spatial": "Vehicles by type of functional classified roadway",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "temporal": "R/1970-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
-            "phone": "202-366-1067",
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Traffic Volume Trends - August 2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/56rv-9p75",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2024-10-01",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-14",
-            "keyword": [
-                "aff",
-                "air carriers",
-                "aviation facts & figures",
-                "passengers"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/56rv-9p75",
             "description": "Commercial air passengers, seats, freight, and mail summary by destination/origin country from/to the United States.",
-            "title": "AFF - T100 Segment Summary By Country",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9972,43 +9953,80 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/56rv-9p75/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/56rv-9p75/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/56rv-9p75/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/56rv-9p75/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/56rv-9p75/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/56rv-9p75/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/56rv-9p75/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/56rv-9p75/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/56rv-9p75/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/56rv-9p75",
+            "issued": "2024-10-01",
+            "keyword": [
+                "aff",
+                "air carriers",
+                "aviation facts & figures",
+                "passengers"
+            ],
+            "landingPage": "https://data.transportation.gov/d/56rv-9p75",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-14",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Aviation"
-            ]
+            ],
+            "title": "AFF - T100 Segment Summary By Country"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/575z-rwqx",
-            "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": false,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
+            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "2011 Massachusetts HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/massachusetts2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Massachusetts"
+                }
+            ],
+            "identifier": "678.23",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -10022,97 +10040,64 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.23",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Massachusetts",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/575z-rwqx",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5035",
             "primaryITInvestmentUII": "021-099281808",
             "programCode": [
                 "021:009"
             ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/massachusetts2011.zip",
-                    "description": "2011 Massachusetts HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Massachusetts"
-                }
-            ],
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "temporal": "R/1981-11-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
-            "categoryDesignation": "Administrative",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-5035"
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Massachusetts"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/57sz-yj2t",
-            "issued": "2022-04-01",
             "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joe McGill",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "Facts and figures related to the individual vessels used in ferry operations.",
             "identifier": "https://data.transportation.gov/api/views/57sz-yj2t",
+            "issued": "2022-04-01",
+            "landingPage": "https://data.transportation.gov/d/57sz-yj2t",
+            "modified": "2022-04-28",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "Facts and figures related to the individual vessels used in ferry operations.",
             "title": "Ferry Vessels"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://nhts.ornl.gov/index.shtml",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/57u6-3u4f",
-            "issued": "1969-01-01",
-            "temporal": "1969-01-01/2014-12-29",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
-            "keyword": [
-                "demographics",
-                "driver",
-                "travel"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "682.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": false,
+            "describedBy": "http://nhts.ornl.gov/publications.shtml",
             "description": "The National Household Travel Survey provides information to assist transportation planners and policy makers who need comprehensive data on travel and transportation patterns in the United States",
-            "title": "National Household Travel Survey - Download data",
-            "isPartOf": "DOT-682",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10121,52 +10106,47 @@
                     "title": "Download data"
                 }
             ],
-            "describedBy": "http://nhts.ornl.gov/publications.shtml",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "682.2",
+            "isPartOf": "DOT-682",
+            "issued": "1969-01-01",
+            "keyword": [
+                "demographics",
+                "driver",
+                "travel"
             ],
-            "accrualPeriodicity": "irregular",
-            "agencyDataSeriesURL": "http://nhts.ornl.gov/index.shtml",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/57u6-3u4f",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-5021"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5021",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "temporal": "1969-01-01/2014-12-29",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "National Household Travel Survey - Download data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2022-07-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "highway",
-                "highway performance monitoring",
-                "highway performance monitoring system",
-                "highways",
-                "hpms",
-                "sample"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/58gj-eqs9",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 1985",
-            "title": "Historic HPMS Data (Sample) - 1985",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10174,68 +10154,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/58gj-eqs9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/58gj-eqs9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/58gj-eqs9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/58gj-eqs9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/58gj-eqs9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/58gj-eqs9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/58gj-eqs9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/58gj-eqs9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/58gj-eqs9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/58gj-eqs9",
+            "issued": "2022-07-08",
+            "keyword": [
+                "highway",
+                "highway performance monitoring",
+                "highway performance monitoring system",
+                "highways",
+                "hpms",
+                "sample"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-08",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
             "spatial": "United States",
-            "dataQuality": true,
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Historic HPMS Data (Sample) - 1985"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2022-07-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "highway",
-                "highway performance monitoring",
-                "highway performance monitoring system",
-                "highways",
-                "hpms",
-                "sample"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
-            "identifier": "https://data.transportation.gov/api/views/58wp-34h2",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 2005",
-            "title": "Historic HPMS Data (Sample) - 2005",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10243,54 +10223,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/58wp-34h2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/58wp-34h2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/58wp-34h2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/58wp-34h2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/58wp-34h2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/58wp-34h2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/58wp-34h2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/58wp-34h2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/58wp-34h2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/58wp-34h2",
+            "issued": "2022-07-08",
+            "keyword": [
+                "highway",
+                "highway performance monitoring",
+                "highway performance monitoring system",
+                "highways",
+                "hpms",
+                "sample"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-08",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "spatial": "United States",
-            "dataQuality": true,
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Historic HPMS Data (Sample) - 2005"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/598u-4exz",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/598u-4exz",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "FRA Regions",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10298,97 +10288,87 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/598u-4exz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/598u-4exz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/598u-4exz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/598u-4exz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/598u-4exz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/598u-4exz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/598u-4exz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/598u-4exz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/598u-4exz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/598u-4exz",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/598u-4exz",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "FRA Regions"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/59f3-d4qy",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2025-01-13",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
-            "keyword": [
-                "bikeshare",
-                "monthly transportation statistics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/59f3-d4qy",
             "description": "The Bureau of Transportation Statistics calculates this value using system data provided by CitiBike NY/JC (New York, NY and Jersey City, NJ), Capital Bikeshare (Washington, DC area), Divvy (Chicago, IL), Bay Wheels (San Francisco, CA), and Blue Bikes (Boston, MA area).",
-            "title": "Docked Bikeshare Trips: Largest 6 Systems",
+            "identifier": "https://data.transportation.gov/api/views/59f3-d4qy",
+            "issued": "2025-01-13",
+            "keyword": [
+                "bikeshare",
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/59f3-d4qy",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-13",
+            "phone": "202-366-DATA(3282) ",
             "programCode": [
                 "021:053"
             ],
-            "license": "https://www.usa.gov/government-works",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282) "
+            "title": "Docked Bikeshare Trips: Largest 6 Systems"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2022-07-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "highway",
-                "highway performance monitoring",
-                "highway performance monitoring system",
-                "highways",
-                "hpms",
-                "sample"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/5b2v-t5k8",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 1980.",
-            "title": "Historic HPMS Data (Sample) - 1980",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10396,106 +10376,142 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5b2v-t5k8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5b2v-t5k8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5b2v-t5k8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/5b2v-t5k8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5b2v-t5k8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5b2v-t5k8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5b2v-t5k8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5b2v-t5k8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5b2v-t5k8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/5b2v-t5k8",
+            "issued": "2022-07-08",
+            "keyword": [
+                "highway",
+                "highway performance monitoring",
+                "highway performance monitoring system",
+                "highways",
+                "hpms",
+                "sample"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-08",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
             "spatial": "United States",
-            "dataQuality": true,
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Historic HPMS Data (Sample) - 1980"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/5b8w-n6ik",
-            "issued": "2023-04-06",
             "@type": "dcat:Dataset",
-            "modified": "2023-07-12",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/5b8w-n6ik",
+            "issued": "2023-04-06",
+            "landingPage": "https://data.transportation.gov/d/5b8w-n6ik",
+            "modified": "2023-07-12",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
-            "title": "Using OData Connections with Excel and Access",
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Using OData Connections with Excel and Access"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/5bfv-z8ek",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Cost of fuel for transportation by year and type. Annual price is average of monthly values.",
+            "identifier": "https://data.transportation.gov/api/views/5bfv-z8ek",
             "issued": "2020-04-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
             "keyword": [
                 "cost",
                 "fuel",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/5bfv-z8ek",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-18",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/5bfv-z8ek",
-            "description": "Cost of fuel for transportation by year and type. Annual price is average of monthly values.",
-            "title": "Transportation Economic Trends: Transportation Costs - Fuel",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Transportation Economic Trends: Transportation Costs - Fuel"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/on_the_fly_download.aspx",
+            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
+            "analysisUnit": "Form 54 Filing",
             "bureauCode": [
                 "021:27"
             ],
-            "landingPage": "https://data.transportation.gov/d/5bt5-eguz",
-            "issued": "2010-09-29",
-            "temporal": "R/1975-01-31/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-09",
+            "categoryDesignation": "Research",
             "collectionInstrument": "FORM FRA F 6180.54 (OMB No. 2130-0500)",
-            "references": [
-                "https://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Newregulation.aspx%3Fdoc=FRAGuideforPreparingAccIncReportspubMay2011.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/DownloadFStructure.aspx",
+            "description": "\"This file contains reported cases of collisions, derailments, fires, explosions, acts of God, or other events involving the operation of railroad on-track equipment and involving damages exceeding the reporting threshold for the year reported. National files from 1975 through the current year are available for download. In addition, individual files by State are available for the years 1991 through the current year.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/incabbr.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Accidents By State/Railroad"
+                }
             ],
+            "identifier": "199.13",
+            "isPartOf": "DOT-199",
+            "issued": "2010-09-29",
             "keyword": [
                 "acts of god",
                 "collisions",
@@ -10506,61 +10522,60 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "199.13",
+            "landingPage": "https://data.transportation.gov/d/5bt5-eguz",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-10-09",
+            "phone": "202-493-6483",
+            "programCode": [
+                "021:036"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Railroad Administration"
             },
-            "description": "\"This file contains reported cases of collisions, derailments, fires, explosions, acts of God, or other events involving the operation of railroad on-track equipment and involving damages exceeding the reporting threshold for the year reported. National files from 1975 through the current year are available for download. In addition, individual files by State are available for the years 1991 through the current year.",
-            "title": "Rail Equipment Accidents - Accidents By State/Railroad",
-            "isPartOf": "DOT-199",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:036"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/incabbr.aspx",
-                    "mediaType": "text/csv",
-                    "title": "Accidents By State/Railroad"
-                }
+            "references": [
+                "https://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Newregulation.aspx%3Fdoc=FRAGuideforPreparingAccIncReportspubMay2011.pdf"
             ],
             "spatial": "Latitude/Longitude, County, State",
-            "describedBy": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/DownloadFStructure.aspx",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/on_the_fly_download.aspx",
+            "temporal": "R/1975-01-31/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Form 54 Filing",
-            "phone": "202-493-6483",
-            "language": [
-                "en-US"
-            ]
+            "title": "Rail Equipment Accidents - Accidents By State/Railroad"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://fhwaapps.fhwa.dot.gov/vtris-wp/",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/travelmonitoring.cfm",
+            "analysisUnit": "Weight-in-motion (WIM) station",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/5caj-2y8j",
-            "issued": "1990-01-01",
-            "temporal": "R/1990-01-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Web site",
-            "references": [
-                "http://www.fhwa.dot.gov/ohim/ohimvtis.cfm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www.fhwa.dot.gov/ohim/ohimvtis.cfm",
+            "description": "The VTRIS W-Tables are designed to provide a standard format for presenting the outcome of the Vehicle Weighing and Classification efforts at truck weigh sites. The data that appears in the W-Tables comes from the Summary files that are generated by the Summary subsystem.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://fhwaapps.fhwa.dot.gov/vtris-wp/",
+                    "mediaType": "text/html",
+                    "title": "Data Download Tool"
+                }
             ],
+            "identifier": "DOT-285",
+            "issued": "1990-01-01",
             "keyword": [
                 "axle load",
                 "carried load",
@@ -10576,77 +10591,43 @@
                 "weight-in-motion",
                 "wim"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "DOT-285",
+            "landingPage": "https://data.transportation.gov/d/5caj-2y8j",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5053",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "The VTRIS W-Tables are designed to provide a standard format for presenting the outcome of the Vehicle Weighing and Classification efforts at truck weigh sites. The data that appears in the W-Tables comes from the Summary files that are generated by the Summary subsystem.",
-            "title": "Vehicle Travel Information System (VTRIS)",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/travelmonitoring.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://fhwaapps.fhwa.dot.gov/vtris-wp/",
-                    "mediaType": "text/html",
-                    "title": "Data Download Tool"
-                }
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/ohimvtis.cfm"
             ],
             "spatial": "Point",
-            "describedBy": "http://www.fhwa.dot.gov/ohim/ohimvtis.cfm",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "https://fhwaapps.fhwa.dot.gov/vtris-wp/",
+            "temporal": "R/1990-01-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Weight-in-motion (WIM) station",
-            "phone": "202-366-5053",
-            "language": [
-                "en-US"
-            ]
+            "title": "Vehicle Travel Information System (VTRIS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2022-07-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "highway",
-                "highway performance monitoring",
-                "highway performance monitoring system",
-                "highways",
-                "hpms"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/5cn3-yynq",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 1992",
-            "title": "Historic HPMS Data (Universe) - 1992",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10654,50 +10635,83 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5cn3-yynq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5cn3-yynq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5cn3-yynq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/5cn3-yynq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5cn3-yynq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5cn3-yynq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5cn3-yynq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5cn3-yynq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5cn3-yynq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/5cn3-yynq",
+            "issued": "2022-07-06",
+            "keyword": [
+                "highway",
+                "highway performance monitoring",
+                "highway performance monitoring system",
+                "highways",
+                "hpms"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-08",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
             "spatial": "United States",
-            "dataQuality": true,
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Historic HPMS Data (Universe) - 1992"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/PT1S",
+            "agencyDataSeriesURL": "http://www.nhtsa.gov/Vehicle+Safety",
+            "agencyProgramURL": "http://vpic.nhtsa.dot.gov/",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/5da4-r9g8",
-            "issued": "2015-10-05",
-            "temporal": "R/2015-10-05/PT1S",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Administrative - Regulatory",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://vpic.nhtsa.dot.gov/"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The NHTSA Product Information Catalog and Vehicle Listing (vPIC) is a consolidated platform that presents data collected within the manufacturer reported data from CFR 49 Parts 551 - 574 for use in a variety of modern tools. NHTSA's vPIC platform is intended to serve as a centralized source for basic Vehicle Identification Number (VIN) decoding, Manufacturer Information Database (MID), Manufacturer Equipment Plant Identification and associated data. vPIC is intended to support the Open Data and Transparency initiatives of the agency by allowing the data to be freely used by the public without the burden of manual retrieval from a library of electronic documents (PDFs). While these documents will still be available online for viewing within the Manufacturer Information Database (MID) module of vPIC one can view and use the actual data through the VIN Decoder and Application Programming Interface (API) modules.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Manufacturer Information Database",
+                    "downloadURL": "http://vpic.nhtsa.dot.gov/mid",
+                    "mediaType": "text/html",
+                    "title": "MID"
+                }
             ],
+            "identifier": "DOT-65",
+            "issued": "2015-10-05",
             "keyword": [
                 "49",
                 "551",
@@ -10734,74 +10748,65 @@
                 "vin",
                 "vpic"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "DOT-65",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "The NHTSA Product Information Catalog and Vehicle Listing (vPIC) is a consolidated platform that presents data collected within the manufacturer reported data from CFR 49 Parts 551 - 574 for use in a variety of modern tools. NHTSA's vPIC platform is intended to serve as a centralized source for basic Vehicle Identification Number (VIN) decoding, Manufacturer Information Database (MID), Manufacturer Equipment Plant Identification and associated data. vPIC is intended to support the Open Data and Transparency initiatives of the agency by allowing the data to be freely used by the public without the burden of manual retrieval from a library of electronic documents (PDFs). While these documents will still be available online for viewing within the Manufacturer Information Database (MID) module of vPIC one can view and use the actual data through the VIN Decoder and Application Programming Interface (API) modules.",
-            "title": "NHTSA Product Information Catalog and Vehicle Listing (vPIC)",
-            "agencyProgramURL": "http://vpic.nhtsa.dot.gov/",
+            "landingPage": "https://data.transportation.gov/d/5da4-r9g8",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-01",
+            "phone": "202-366-2622",
             "primaryITInvestmentUII": "021-430297065",
             "programCode": [
                 "021:031"
             ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://vpic.nhtsa.dot.gov/mid",
-                    "description": "Manufacturer Information Database",
-                    "@type": "dcat:Distribution",
-                    "title": "MID"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "http://vpic.nhtsa.dot.gov/"
             ],
             "spatial": "NA",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.nhtsa.gov/Vehicle+Safety",
+            "temporal": "R/2015-10-05/PT1S",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/PT1S",
-            "categoryDesignation": "Administrative - Regulatory",
-            "phone": "202-366-2622",
-            "language": [
-                "en-US"
-            ]
+            "title": "NHTSA Product Information Catalog and Vehicle Listing (vPIC)"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/5dqg-uz62",
-            "issued": "2022-03-29",
             "@type": "dcat:Dataset",
-            "modified": "2022-04-26",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joe McGill",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/5dqg-uz62",
+            "issued": "2022-03-29",
+            "landingPage": "https://data.transportation.gov/d/5dqg-uz62",
+            "modified": "2022-04-26",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "National Census of Ferry Operators (NCFO) 2020: Landing Page"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/5ef2-mid7",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRA Safety Data Team",
+                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This is the page for Accident Type (including Highway-Rail Crossings) (3.08).",
+            "identifier": "https://data.transportation.gov/api/views/5ef2-mid7",
             "issued": "2024-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "collision",
                 "derailment",
@@ -10809,92 +10814,74 @@
                 "train",
                 "train accident"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRA Safety Data Team",
-                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Railroad Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/5ef2-mid7",
-            "description": "This is the page for Accident Type (including Highway-Rail Crossings) (3.08).",
-            "title": "Accident Type (including Highway-Rail Crossings) (3.08)",
+            "landingPage": "https://data.transportation.gov/d/5ef2-mid7",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-27",
             "programCode": [
                 "FRA Safety and Operations"
             ],
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Railroad Administration"
+            },
             "theme": [
                 "Railroads"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accident Type (including Highway-Rail Crossings) (3.08)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/5ehw-9fxn",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This report contains a detailed summary of all open highway-rail crossings, broken out by crossing type, crossing position, and crossing purpose. There are four views of data: by (1) state, (2) county, (3) city, and (4) railroad.",
+            "identifier": "https://data.transportation.gov/api/views/5ehw-9fxn",
             "issued": "2023-10-11",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "crossing",
                 "crossing inventory",
                 "highway-rail crossing",
                 "highway-rail grade crossing"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/5ehw-9fxn",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-27",
+            "programCode": [
+                "021:036"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Railroad Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/5ehw-9fxn",
-            "description": "This report contains a detailed summary of all open highway-rail crossings, broken out by crossing type, crossing position, and crossing purpose. There are four views of data: by (1) state, (2) county, (3) city, and (4) railroad.",
-            "title": "Crossing Inventory Detailed Summary",
-            "programCode": [
-                "021:036"
-            ],
-            "dataQuality": true,
             "theme": [
                 "Railroads"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Crossing Inventory Detailed Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/5ekk-irbi",
-            "issued": "2024-05-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-14",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joe McGill",
                 "hasEmail": "mailto:joseph.mcgill@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/5ekk-irbi",
             "description": "",
-            "title": "extraLongPUFVius",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10902,59 +10889,90 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5ekk-irbi/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5ekk-irbi/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5ekk-irbi/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/5ekk-irbi/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5ekk-irbi/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5ekk-irbi/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5ekk-irbi/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5ekk-irbi/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5ekk-irbi/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "https://data.transportation.gov/api/views/5ekk-irbi",
+            "issued": "2024-05-14",
+            "landingPage": "https://data.transportation.gov/d/5ekk-irbi",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-14",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "extraLongPUFVius"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/5er7-y3zn",
-            "issued": "2021-06-07",
             "@type": "dcat:Dataset",
-            "modified": "2023-08-24",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sean Jahanmir",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/5er7-y3zn",
+            "issued": "2021-06-07",
+            "landingPage": "https://data.transportation.gov/d/5er7-y3zn",
+            "modified": "2023-08-24",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Major Trends"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/5f73-8nr2",
-            "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": false,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
+            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "2012 Wisconsin HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/wisconsin2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Wisconsin"
+                }
+            ],
+            "identifier": "678.103",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -10968,75 +10986,40 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.103",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Wisconsin",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/5f73-8nr2",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5035",
             "primaryITInvestmentUII": "021-099281808",
             "programCode": [
                 "021:009"
             ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/wisconsin2012.zip",
-                    "description": "2012 Wisconsin HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Wisconsin"
-                }
-            ],
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "temporal": "R/1981-11-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
-            "categoryDesignation": "Administrative",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-5035"
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Wisconsin"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/5g3r-xnzv",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-10-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-01",
-            "keyword": [
-                "containerized",
-                "exports",
-                "ports"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:answers@bts.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/5g3r-xnzv",
             "description": "Source: U.S. Department of Transportation, Bureau of Transportation Statistics, based upon U.S. Department of Commerce, U.S. Census Bureau, Foreign Trade Division, USA Trade Online, \"HS Port-level Data\", available at https://usatrade.census.gov/ as of Oct 2024.",
-            "title": "Top 10 Containerized Export Commodities in Short Tons by Coast, 2023",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11044,50 +11027,82 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5g3r-xnzv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5g3r-xnzv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5g3r-xnzv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/5g3r-xnzv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5g3r-xnzv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5g3r-xnzv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5g3r-xnzv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5g3r-xnzv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5g3r-xnzv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/5g3r-xnzv",
+            "issued": "2024-10-01",
+            "keyword": [
+                "containerized",
+                "exports",
+                "ports"
+            ],
+            "landingPage": "https://data.transportation.gov/d/5g3r-xnzv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-10-01",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Maritime and Waterways"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Top 10 Containerized Export Commodities in Short Tons by Coast, 2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/5gvk-x5g6",
-            "issued": "1970-01-01",
-            "temporal": "R/1970-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "State Traffic Monitoring Systems (TMS)",
-            "references": [
-                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/10novtvt/10novtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "November 2010"
+                }
             ],
+            "identifier": "18.16",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -11097,84 +11112,50 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.16",
+            "landingPage": "https://data.transportation.gov/d/5gvk-x5g6",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-1067",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - November 2010",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/10novtvt/10novtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "November 2010"
-                }
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
             ],
             "spatial": "Vehicles by type of functional classified roadway",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "temporal": "R/1970-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
-            "phone": "202-366-1067",
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Traffic Volume Trends - November 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/PT1S",
+            "agencyDataSeriesURL": "http://www.fra.dot.gov/eLib/Find",
+            "agencyProgramURL": "http://www.fra.dot.gov/eLib/Find",
+            "analysisUnit": "document",
             "bureauCode": [
                 "021:27"
             ],
-            "landingPage": "https://data.transportation.gov/d/5h3f-chys",
-            "issued": "2014-11-21",
-            "temporal": "R/2014-11-21/PT1S",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-09",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.fra.dot.gov/eLib/Find"
-            ],
-            "keyword": [
-                "fra elibrary",
-                "fra e-library",
-                "fra library",
-                "library fra"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Railroad Safety",
                 "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
             },
-            "identifier": "671.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Railroad Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.fra.dot.gov/eLib/Find",
             "description": "Collection of documents",
-            "title": "eLibrary - Search Tool",
-            "isPartOf": "DOT-671",
-            "agencyProgramURL": "http://www.fra.dot.gov/eLib/Find",
-            "primaryITInvestmentUII": "021-255678806",
-            "programCode": [
-                "021:036"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11183,119 +11164,153 @@
                     "title": "Search Tool"
                 }
             ],
-            "describedBy": "http://www.fra.dot.gov/eLib/Find",
-            "dataQuality": true,
+            "identifier": "671.1",
+            "isPartOf": "DOT-671",
+            "issued": "2014-11-21",
+            "keyword": [
+                "fra elibrary",
+                "fra e-library",
+                "fra library",
+                "library fra"
+            ],
+            "landingPage": "https://data.transportation.gov/d/5h3f-chys",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.fra.dot.gov/eLib/Find",
+            "modified": "2024-10-09",
+            "phone": "202-366-1299",
+            "primaryITInvestmentUII": "021-255678806",
+            "programCode": [
+                "021:036"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Railroad Administration"
+            },
+            "references": [
+                "http://www.fra.dot.gov/eLib/Find"
+            ],
+            "temporal": "R/2014-11-21/PT1S",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/PT1S",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "document",
-            "phone": "202-366-1299",
-            "language": [
-                "en-US"
-            ]
+            "title": "eLibrary - Search Tool"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/5h3f-jnbe",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2020-03-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
-            "keyword": [
-                "transportation cost",
-                "transportation fare"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/5h3f-jnbe",
             "description": "Transportation costs faced by households.",
-            "title": "Transportation Economic Trends: Transportation Costs - Households",
+            "identifier": "https://data.transportation.gov/api/views/5h3f-jnbe",
+            "issued": "2020-03-01",
+            "keyword": [
+                "transportation cost",
+                "transportation fare"
+            ],
+            "landingPage": "https://data.transportation.gov/d/5h3f-jnbe",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-18",
+            "phone": "202-366-DATA(3282)",
             "programCode": [
                 "021:053"
             ],
-            "license": "https://www.usa.gov/government-works",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Transportation Economic Trends: Transportation Costs - Households"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/5hyy-bjct",
-            "issued": "2020-12-15",
             "@type": "dcat:Dataset",
-            "modified": "2020-12-16",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alpha Wingfield",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/5hyy-bjct",
+            "issued": "2020-12-15",
+            "landingPage": "https://data.transportation.gov/d/5hyy-bjct",
+            "modified": "2020-12-16",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Port Performance for TRB"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/5iup-ekpn",
-            "issued": "2025-01-02",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-02",
-            "keyword": [
-                "monthly transportation statistics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:answers@bts.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/5iup-ekpn",
             "description": "Gross domestic product is the market value of goods and services produced by labor and property in the United States. The U.S. Bureau of Economic Analysis estimates GDP for each quarter and releases new statistics every month. Quarterly GDP data are seasonally adjusted at annual rates.",
-            "title": "Real Gross Domestic Product - Seasonally Adjusted",
+            "identifier": "https://data.transportation.gov/api/views/5iup-ekpn",
+            "issued": "2025-01-02",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/5iup-ekpn",
+            "modified": "2025-01-02",
             "programCode": [
                 "021:053"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Real Gross Domestic Product - Seasonally Adjusted"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/5k2v-pyru",
-            "issued": "1970-01-01",
-            "temporal": "R/1970-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "State Traffic Monitoring Systems (TMS)",
-            "references": [
-                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/02jultvt/tvtjul02.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "July 2002"
+                }
             ],
+            "identifier": "18.146",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -11305,86 +11320,50 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.146",
+            "landingPage": "https://data.transportation.gov/d/5k2v-pyru",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-1067",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - July 2002",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/02jultvt/tvtjul02.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "July 2002"
-                }
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
             ],
             "spatial": "Vehicles by type of functional classified roadway",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "temporal": "R/1970-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
-            "phone": "202-366-1067",
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Traffic Volume Trends - July 2002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www.safercar.gov/parents/Car-Seat-Safety.htm",
+            "agencyProgramURL": "http://www.safercar.gov/parents/CarSeats/Car-Seat-Safety.htm",
+            "analysisUnit": "Child Safety Seats",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/5kf2-jq7y",
-            "issued": "2008-02-01",
-            "temporal": "2008-01-01/2015-04-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.nhtsa.gov/DOT/NHTSA/Communication%20&%20Consumer%20Information/Articles/CPS%20files/faq.pdf"
-            ],
-            "keyword": [
-                "child",
-                "css",
-                "ease of use",
-                "passenger",
-                "ratings",
-                "safety",
-                "seat"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "2.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.safercar.gov/parents/CarSeats/Car-Seat-Glossary-of-Terms.htm",
             "description": "To assist consumers purchasing child safety seats, NHTSA has rated car seats which meet Federal Safety Standards and strict crash performance standards. While all rates seats are safe, they do differ in their ease of use in the following four basic categories: Evaluation of Instructions, Evaluation of Labels, Vehicle Installation Features, Securing the Child",
-            "title": "Child Safety Seat Ease of Use Rating - Child Safety Seat Ease of Use Ratings",
-            "isPartOf": "DOT-2",
-            "agencyProgramURL": "http://www.safercar.gov/parents/CarSeats/Car-Seat-Safety.htm",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11393,57 +11372,60 @@
                     "title": "Child Safety Seat Ease of Use Ratings"
                 }
             ],
-            "spatial": "N/A",
-            "describedBy": "http://www.safercar.gov/parents/CarSeats/Car-Seat-Glossary-of-Terms.htm",
-            "dataQuality": true,
+            "identifier": "2.2",
+            "isPartOf": "DOT-2",
+            "issued": "2008-02-01",
+            "keyword": [
+                "child",
+                "css",
+                "ease of use",
+                "passenger",
+                "ratings",
+                "safety",
+                "seat"
+            ],
+            "landingPage": "https://data.transportation.gov/d/5kf2-jq7y",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.safercar.gov/parents/Car-Seat-Safety.htm",
+            "modified": "2024-05-01",
+            "phone": "202-493-0188",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "http://www.nhtsa.gov/DOT/NHTSA/Communication%20&%20Consumer%20Information/Articles/CPS%20files/faq.pdf"
+            ],
+            "spatial": "N/A",
+            "temporal": "2008-01-01/2015-04-01",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Child Safety Seats",
-            "phone": "202-493-0188",
-            "language": [
-                "en-US"
-            ]
+            "title": "Child Safety Seat Ease of Use Rating - Child Safety Seat Ease of Use Ratings"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://hepgis.fhwa.dot.gov/hepgismaps11/#",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/5kih-wu4c",
-            "issued": "2007-01-01",
-            "temporal": "2007-01-01/2014-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Geospatial",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "arra planning",
-                "fhwa",
-                "geographic",
-                "geospatial",
-                "map"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "DOT-692",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS)",
-            "primaryITInvestmentUII": "021-845083703",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11452,34 +11434,67 @@
                     "title": "MAP-21 National Highway System"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/5kih-wu4c",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://hepgis.fhwa.dot.gov/hepgismaps11/#",
+            "modified": "2024-05-08",
+            "phone": "708-283-3554",
+            "primaryITInvestmentUII": "021-845083703",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "spatial": "National, State, County",
+            "temporal": "2007-01-01/2014-12-31",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Geospatial",
-            "phone": "708-283-3554",
-            "language": [
-                "en-US"
-            ]
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/5kjt-7c79",
-            "issued": "1970-01-01",
-            "temporal": "R/1970-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "State Traffic Monitoring Systems (TMS)",
-            "references": [
-                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/10dectvt/10dectvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "December 2010"
+                }
             ],
+            "identifier": "18.15",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -11489,82 +11504,44 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.15",
+            "landingPage": "https://data.transportation.gov/d/5kjt-7c79",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-1067",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - December 2010",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/10dectvt/10dectvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "December 2010"
-                }
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
             ],
             "spatial": "Vehicles by type of functional classified roadway",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "temporal": "R/1970-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
-            "phone": "202-366-1067",
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Traffic Volume Trends - December 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.bts.dot.gov/surveys/national-census-ferry-operators-ncfo/national-census-ferry-operators-ncfo",
             "bureauCode": [
                 "021:04"
             ],
-            "rights": "Business-sensitive data has been removed from this dataset",
-            "issued": "2017-09-20",
-            "@type": "dcat:Dataset",
-            "temporal": "2015-01-01/2015-12-31",
-            "modified": "2018-05-16",
-            "keyword": [
-                "ferry",
-                "freight",
-                "maritime",
-                "passenger",
-                "terminals",
-                "transit",
-                "travel",
-                "vessels"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Janine McFadden",
                 "hasEmail": "mailto:janine.mcfadden@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statisitics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/5kxy-j6hw",
+            "dataQuality": true,
+            "describedBy": "https://www.bts.dot.gov/surveys/national-census-ferry-operators-ncfo/statement-methodology",
             "description": "The 2016 NCFO dataset is comprised of the responses of all operators who completed the 2016 NCFO.  The dataset is made up of ferry operator, vessel, terminal and segment data for the 2015 calendar year.",
-            "title": "2016 National Census of Ferry Operators (NCFO)",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11572,70 +11549,76 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5kxy-j6hw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5kxy-j6hw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5kxy-j6hw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/5kxy-j6hw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5kxy-j6hw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5kxy-j6hw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5kxy-j6hw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5kxy-j6hw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5kxy-j6hw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S., U.S. Territories, and applicable Canadian providences",
-            "describedBy": "https://www.bts.dot.gov/surveys/national-census-ferry-operators-ncfo/statement-methodology",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/5kxy-j6hw",
+            "issued": "2017-09-20",
+            "keyword": [
+                "ferry",
+                "freight",
+                "maritime",
+                "passenger",
+                "terminals",
+                "transit",
+                "travel",
+                "vessels"
+            ],
+            "landingPage": "https://www.bts.dot.gov/surveys/national-census-ferry-operators-ncfo/national-census-ferry-operators-ncfo",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2018-05-16",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statisitics"
+            },
+            "rights": "Business-sensitive data has been removed from this dataset",
+            "spatial": "U.S., U.S. Territories, and applicable Canadian providences",
+            "temporal": "2015-01-01/2015-12-31",
             "theme": [
                 "Ferry Transit"
-            ]
+            ],
+            "title": "2016 National Census of Ferry Operators (NCFO)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Transaction+Data+and+Reports",
+            "agencyProgramURL": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Officially+Ended",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/5m53-446v",
-            "issued": "2018-12-17",
-            "temporal": "2009-07-01/2011-09-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Transaction+Data+and+Reports"
-            ],
-            "keyword": [
-                "cars",
-                "transactions"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "10.4",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
+            "describedBy": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Transaction+Data+and+Reports",
             "description": "The Car Allowance Rebate System (CARS), otherwise known as Cash for Clunkers, was a program intended to provide economic incentives to United States residents to purchase a new and more fuel efficient vehicle when trading in a less full efficient vehicle. The program was promoted as providing stimulus to the economy by boosting auto sales, while putting safer, cleaner and more fuel efficient vehicles on the road.",
-            "title": "Car Allowance Rebate System (CARS) - Transactions - Cancelled Transaction Database mdb file",
-            "isPartOf": "DOT-10",
-            "agencyProgramURL": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Officially+Ended",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11644,35 +11627,66 @@
                     "title": "Cancelled Transaction Database mdb file"
                 }
             ],
-            "spatial": "N/A",
-            "describedBy": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Transaction+Data+and+Reports",
-            "dataQuality": false,
+            "identifier": "10.4",
+            "isPartOf": "DOT-10",
+            "issued": "2018-12-17",
+            "keyword": [
+                "cars",
+                "transactions"
+            ],
+            "landingPage": "https://data.transportation.gov/d/5m53-446v",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Transaction+Data+and+Reports",
+            "modified": "2024-05-01",
+            "phone": "202-366-0641",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Transaction+Data+and+Reports"
+            ],
+            "spatial": "N/A",
+            "temporal": "2009-07-01/2011-09-30",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "categoryDesignation": "Research",
-            "phone": "202-366-0641",
-            "language": [
-                "en-US"
-            ]
+            "title": "Car Allowance Rebate System (CARS) - Transactions - Cancelled Transaction Database mdb file"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/pe/home.aspx",
+            "agencyProgramURL": "http://ai.fmcsa.dot.gov/pe/Home.aspx",
+            "analysisUnit": "FMCSA program",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/5mdj-8z89",
-            "issued": "2005-08-09",
-            "temporal": "2002-01-01/2008-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://ai.fmcsa.dot.gov/CarrierResearchResults/PDFs/IntModel_07/IM%20Technical%20Documentation.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The objective of the FMCSA's Program Effectiveness research is to measure the effectiveness of the FMCSA Safety Programs. The Compliance Review Effectiveness Model and the Intervention Model provide estimates of the beneficial impact of these programs on reducing crashes resulting in lives saved and injuries avoided. The Resource Allocation model utilizes the results of these two models to analyze the allocation of state resources.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://ai.fmcsa.dot.gov/pe/CompliancePg.aspx",
+                    "mediaType": "text/html",
+                    "title": "Compliance Review Effectiveness Model"
+                }
             ],
+            "identifier": "DOT-115",
+            "issued": "2005-08-09",
             "keyword": [
                 "compliance review",
                 "compliance review effectiveness model",
@@ -11682,115 +11696,82 @@
                 "program effectiveness",
                 "roadside inspection traffic enforcement"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "DOT-115",
+            "landingPage": "https://data.transportation.gov/d/5mdj-8z89",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-24",
+            "phone": "202-366-2959",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Motor Carrier Safety Administration"
             },
-            "description": "The objective of the FMCSA's Program Effectiveness research is to measure the effectiveness of the FMCSA Safety Programs. The Compliance Review Effectiveness Model and the Intervention Model provide estimates of the beneficial impact of these programs on reducing crashes resulting in lives saved and injuries avoided. The Resource Allocation model utilizes the results of these two models to analyze the allocation of state resources.",
-            "title": "A&I - Program Effectiveness",
-            "agencyProgramURL": "http://ai.fmcsa.dot.gov/pe/Home.aspx",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://ai.fmcsa.dot.gov/pe/CompliancePg.aspx",
-                    "mediaType": "text/html",
-                    "title": "Compliance Review Effectiveness Model"
-                }
+            "references": [
+                "http://ai.fmcsa.dot.gov/CarrierResearchResults/PDFs/IntModel_07/IM%20Technical%20Documentation.pdf"
             ],
             "spatial": "National",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/pe/home.aspx",
+            "temporal": "2002-01-01/2008-12-31",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "analysisUnit": "FMCSA program",
-            "categoryDesignation": "Research",
-            "phone": "202-366-2959",
-            "language": [
-                "en-US"
-            ]
+            "title": "A&I - Program Effectiveness"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/5mkb-pzzy",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2025-01-29",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-29",
-            "keyword": [
-                "monthly transportation statistics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:answers@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/5mkb-pzzy",
             "description": "Number of trucks entering the United States from Canada. The Bureau of Transportation of Statistics releases incoming border crossing statistics using data collected at ports of entry by U.S. Customs and Border Protection.",
-            "title": "U.S.-Canada Incoming Truck Crossings",
+            "identifier": "https://data.transportation.gov/api/views/5mkb-pzzy",
+            "issued": "2025-01-29",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/5mkb-pzzy",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-29",
             "programCode": [
                 "021:053"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Research and Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "U.S.-Canada Incoming Truck Crossings"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/infrastructure/history.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/infrastructure/history.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/5mye-eub5",
-            "issued": "2014-12-29",
-            "temporal": "2014-12-29/2014-12-29",
-            "@type": "dcat:Dataset",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
-            "keyword": [
-                "articles",
-                "documents",
-                "fhwa",
-                "history",
-                "legislation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "696.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "A compilation of historic documents and articles on the Interstate System, Federal-Aid Highway Program, FHWA, and transportation.",
-            "title": "Highway History - Highway History",
-            "isPartOf": "DOT-696",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/infrastructure/history.cfm",
-            "programCode": [
-                "021:011"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11799,48 +11780,50 @@
                     "title": "Highway History"
                 }
             ],
-            "spatial": "National",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "696.1",
+            "isPartOf": "DOT-696",
+            "issued": "2014-12-29",
+            "keyword": [
+                "articles",
+                "documents",
+                "fhwa",
+                "history",
+                "legislation"
             ],
-            "accrualPeriodicity": "irregular",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/infrastructure/history.cfm",
+            "landingPage": "https://data.transportation.gov/d/5mye-eub5",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-4856"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-4856",
+            "programCode": [
+                "021:011"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "spatial": "National",
+            "temporal": "2014-12-29/2014-12-29",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Highway History - Highway History"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2024-05-24",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-21",
-            "keyword": [
-                "fuel",
-                "motor fuel",
-                "special fuel"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/5n49-mh85",
+            "dataQuality": true,
             "description": "Volume of taxed special fuel, primarily diesel, but including alternative fuels, reported by the States each month, based on reports from suppliers and distributors. These amounts are reported in various Office of Highway Policy Information (OHPI) products including the longstanding Monthly Motor Fuel Report, and the annual Highway Statistics publications.",
-            "title": "Special Fuel Volumes Distributed",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11848,70 +11831,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5n49-mh85/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5n49-mh85/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5n49-mh85/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/5n49-mh85/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5n49-mh85/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5n49-mh85/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5n49-mh85/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5n49-mh85/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5n49-mh85/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "dataQuality": true,
-            "theme": [
-                "Roadways and Bridges"
-            ],
-            "language": [
-                "en-US"
-            ]
-        },
+            "identifier": "https://data.transportation.gov/api/views/5n49-mh85",
+            "issued": "2024-05-24",
+            "keyword": [
+                "fuel",
+                "motor fuel",
+                "special fuel"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-21",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "spatial": "United States",
+            "theme": [
+                "Roadways and Bridges"
+            ],
+            "title": "Special Fuel Volumes Distributed"
+        },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/infrastructure/history.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/infrastructure/history.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/5qbd-qagm",
-            "issued": "2014-12-29",
-            "temporal": "2014-12-29/2014-12-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "articles",
-                "documents",
-                "fhwa",
-                "history",
-                "legislation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "DOT-696",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "A compilation of historic documents and articles on the Interstate System, Federal-Aid Highway Program, FHWA, and transportation.",
-            "title": "Highway History",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/infrastructure/history.cfm",
-            "programCode": [
-                "021:011"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -11920,30 +11902,66 @@
                     "title": "Highway History"
                 }
             ],
-            "spatial": "National",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "DOT-696",
+            "issued": "2014-12-29",
+            "keyword": [
+                "articles",
+                "documents",
+                "fhwa",
+                "history",
+                "legislation"
             ],
-            "accrualPeriodicity": "irregular",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/infrastructure/history.cfm",
+            "landingPage": "https://data.transportation.gov/d/5qbd-qagm",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-4856"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-4856",
+            "programCode": [
+                "021:011"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "spatial": "National",
+            "temporal": "2014-12-29/2014-12-29",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Highway History"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/5qih-enei",
-            "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": false,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
+            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "2013 Alaska HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/alaska2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Alaska"
+                }
+            ],
+            "identifier": "678.106",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -11957,70 +11975,39 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.106",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Alaska",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/5qih-enei",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5035",
             "primaryITInvestmentUII": "021-099281808",
             "programCode": [
                 "021:009"
             ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/alaska2013.zip",
-                    "description": "2013 Alaska HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Alaska"
-                }
-            ],
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "temporal": "R/1981-11-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
-            "categoryDesignation": "Administrative",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-5035"
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Alaska"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/5qik-smay",
             "bureauCode": [
                 "021:17"
             ],
-            "issued": "2024-04-25",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
-            "keyword": [
-                "study"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO Office",
                 "hasEmail": "mailto:FMCSA.CDO@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/5qik-smay",
             "description": "Identifies the study field and study results that arise from ad hoc examination of items, usually inspected in support of a particular study or verification/refutation of a specific trend. This inspection type is a Level IV inspection.",
-            "title": "Special Studies",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12028,64 +12015,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5qik-smay/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5qik-smay/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5qik-smay/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/5qik-smay/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5qik-smay/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5qik-smay/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5qik-smay/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5qik-smay/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5qik-smay/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/5qik-smay",
+            "issued": "2024-04-25",
+            "keyword": [
+                "study"
+            ],
+            "landingPage": "https://data.transportation.gov/d/5qik-smay",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2025-02-01",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
             "theme": [
                 "Trucking and Motorcoaches"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Special Studies"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2024-05-24",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-21",
-            "keyword": [
-                "distribution",
-                "gasoline",
-                "volume"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/5qxh-t94v",
+            "dataQuality": true,
             "description": "Volume of gasoline reported by the States each month, based on reports from suppliers and distributors. These amounts are reported in various Office of Highway Policy Information (OHPI) products including the longstanding Monthly Motor Fuel Report, and the annual Highway Statistics publications.",
-            "title": "Motor Fuel - Gasoline Volumes Distributed",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12093,60 +12076,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5qxh-t94v/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5qxh-t94v/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5qxh-t94v/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/5qxh-t94v/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5qxh-t94v/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5qxh-t94v/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5qxh-t94v/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5qxh-t94v/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5qxh-t94v/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/5qxh-t94v",
+            "issued": "2024-05-24",
+            "keyword": [
+                "distribution",
+                "gasoline",
+                "volume"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-21",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
             "spatial": "United States",
-            "dataQuality": true,
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Motor Fuel - Gasoline Volumes Distributed"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/5rpz-kgm9",
-            "issued": "2021-07-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-02-20",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Chambers",
                 "hasEmail": "mailto:matthew.chambers@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/5rpz-kgm9",
             "description": "",
-            "title": "Port Data",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12154,60 +12141,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5rpz-kgm9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5rpz-kgm9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5rpz-kgm9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/5rpz-kgm9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5rpz-kgm9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5rpz-kgm9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5rpz-kgm9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5rpz-kgm9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5rpz-kgm9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "https://data.transportation.gov/api/views/5rpz-kgm9",
+            "issued": "2021-07-28",
+            "landingPage": "https://data.transportation.gov/d/5rpz-kgm9",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-02-20",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Port Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://nhts.ornl.gov/index.shtml",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/5s24-6sya",
-            "issued": "1969-01-01",
-            "temporal": "1969-01-01/2014-12-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "demographics",
-                "driver",
-                "travel"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "DOT-682",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": false,
+            "describedBy": "http://nhts.ornl.gov/publications.shtml",
             "description": "The National Household Travel Survey provides information to assist transportation planners and policy makers who need comprehensive data on travel and transportation patterns in the United States",
-            "title": "National Household Travel Survey",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12216,34 +12202,63 @@
                     "title": "Download data"
                 }
             ],
-            "describedBy": "http://nhts.ornl.gov/publications.shtml",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "DOT-682",
+            "issued": "1969-01-01",
+            "keyword": [
+                "demographics",
+                "driver",
+                "travel"
             ],
-            "accrualPeriodicity": "irregular",
-            "agencyDataSeriesURL": "http://nhts.ornl.gov/index.shtml",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/5s24-6sya",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-5021"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5021",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "temporal": "1969-01-01/2014-12-29",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "National Household Travel Survey"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/5shu-9pn5",
-            "issued": "1970-01-01",
-            "temporal": "R/1970-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "State Traffic Monitoring Systems (TMS)",
-            "references": [
-                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/11septvt/11septvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "September 2011"
+                }
             ],
+            "identifier": "18.6",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -12253,60 +12268,60 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.6",
+            "landingPage": "https://data.transportation.gov/d/5shu-9pn5",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-1067",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - September 2011",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/11septvt/11septvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "September 2011"
-                }
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
             ],
             "spatial": "Vehicles by type of functional classified roadway",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "temporal": "R/1970-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
-            "phone": "202-366-1067",
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Traffic Volume Trends - September 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/5sqb-w2tj",
-            "issued": "1970-01-01",
-            "temporal": "R/1970-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "State Traffic Monitoring Systems (TMS)",
-            "references": [
-                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/13febtvt/13febtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "February 2013"
+                }
             ],
+            "identifier": "18.47",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -12316,82 +12331,44 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.47",
+            "landingPage": "https://data.transportation.gov/d/5sqb-w2tj",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-1067",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - February 2013",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/13febtvt/13febtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "February 2013"
-                }
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
             ],
             "spatial": "Vehicles by type of functional classified roadway",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "temporal": "R/1970-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
-            "phone": "202-366-1067",
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Traffic Volume Trends - February 2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/5ti2-5uiv",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-11-22",
-            "temporal": "R/2014-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-23",
-            "keyword": [
-                "collisions",
-                "ridership",
-                "safety",
-                "security",
-                "service",
-                "time series",
-                "unlinked passenger trips",
-                "vehicle revenue hours",
-                "vehicle revenue miles"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NTD Program Support",
                 "hasEmail": "mailto:NTDHelp@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Transit Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/5ti2-5uiv",
+            "dataQuality": true,
             "description": "Modal Service data and Safety & Security (S&S) public transit time series data delineated by transit/agency/mode/year/month. Includes all Full Reporters--transit agencies operating modes with more than 30 vehicles in maximum service--to the National Transit Database (NTD). This dataset will be updated monthly. The S&S statistics provided include both Major and Non-Major Events where applicable. This is the only NTD publication in which these totals are combined without any transformation for historical continuity.",
-            "title": "Monthly Modal Time Series",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12399,79 +12376,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5ti2-5uiv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5ti2-5uiv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5ti2-5uiv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/5ti2-5uiv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5ti2-5uiv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5ti2-5uiv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5ti2-5uiv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5ti2-5uiv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5ti2-5uiv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1M",
-            "theme": [
-                "Public Transit"
+            "identifier": "https://data.transportation.gov/api/views/5ti2-5uiv",
+            "issued": "2024-11-22",
+            "keyword": [
+                "collisions",
+                "ridership",
+                "safety",
+                "security",
+                "service",
+                "time series",
+                "unlinked passenger trips",
+                "vehicle revenue hours",
+                "vehicle revenue miles"
             ],
+            "landingPage": "https://data.transportation.gov/d/5ti2-5uiv",
             "language": [
                 "en-US"
-            ]
+            ],
+            "modified": "2025-01-23",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Transit Administration"
+            },
+            "spatial": "United States",
+            "temporal": "R/2014-01-01/P1M",
+            "theme": [
+                "Public Transit"
+            ],
+            "title": "Monthly Modal Time Series"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/5tsh-j288",
+            "accrualPeriodicity": "R/PT0.1S",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2015-11-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2015-03-02/2015-03-04",
-            "modified": "2015-11-01",
-            "keyword": [
-                "anthem",
-                "arizona",
-                "basic safety message (bsm)",
-                "connected vehicle message",
-                "dedicated short range communication (dsrc)",
-                "field test",
-                "freight signal priority (fsp)",
-                "intelligent transportation systems (its)",
-                "i-sig",
-                "its joint program office (jpo)",
-                "map",
-                "multi-modal intelligent traffic signal system (mmitss)",
-                "roadside equipment (rse)",
-                "simulation data",
-                "transit signal priority (tsp)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kate Hartman",
                 "hasEmail": "mailto:kate.hartman@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "US Department of Transportation"
-            },
-            "identifier": "https://data.transportation.gov/api/views/5tsh-j288",
+            "dataQuality": true,
             "description": "The data attached and/or displayed were collected during the Multi-Modal Intelligent Transportation Signal Systems (MMITSS) study. MMITSS is a next-generation traffic signal system that seeks to provide a comprehensive traffic information framework to service all modes of transportation.\n\nA BSM is one of the messages belonging to the Society of Automotive Engineers (SAE) J2735 Standard. This standard is geared toward supporting the interoperability of DSRC applications through the use of a standardized message set and its data frames and data elements. A BSM, which is at times referred to as a \u201cheartbeat\u201d message, is a frequently transmitted message (usually at approximately 10Hz) that is meant to increase a vehicle\u2019s situational awareness. These messages are intended to be used for a variety of applications to exchange safety data regarding a vehicle\u2019s state. \n\n\tA typical BSM contains up to two parts. Part I, the binary large object (blob), is included in every BSM. It contains the fundamental data elements that describe a vehicle\u2019s position (latitude, longitude, elevation) and motion (heading, speed, acceleration). Part II of a BSM contains optional data that is transmitted when required or in response to an event. Typically Part II contains data that serves as an extension of vehicle safety information (path history, path prediction, event flags) and data pertaining to the status of a vehicle\u2019s components, such as lights, wipers, and brakes. \n\nNOTE: All extra attachments are located in Multi-Modal Intelligent Traffic Signal Systems Basic Safety Messages such as MAP, Detectors, and Simulation results",
-            "title": "Multi-Modal Intelligent Traffic Signal Systems Basic Safety Message",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12479,49 +12450,77 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5tsh-j288/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5tsh-j288/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5tsh-j288/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/5tsh-j288/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5tsh-j288/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5tsh-j288/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5tsh-j288/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5tsh-j288/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5tsh-j288/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Anthem, Arizona",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/5tsh-j288",
+            "issued": "2015-11-01",
+            "keyword": [
+                "anthem",
+                "arizona",
+                "basic safety message (bsm)",
+                "connected vehicle message",
+                "dedicated short range communication (dsrc)",
+                "field test",
+                "freight signal priority (fsp)",
+                "intelligent transportation systems (its)",
+                "i-sig",
+                "its joint program office (jpo)",
+                "map",
+                "multi-modal intelligent traffic signal system (mmitss)",
+                "roadside equipment (rse)",
+                "simulation data",
+                "transit signal priority (tsp)"
+            ],
+            "landingPage": "https://data.transportation.gov/d/5tsh-j288",
+            "language": [
+                "en-US"
+            ],
             "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "R/PT0.1S",
+            "modified": "2015-11-01",
+            "programCode": [
+                "021:013"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
+            "spatial": "Anthem, Arizona",
+            "temporal": "2015-03-02/2015-03-04",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Multi-Modal Intelligent Traffic Signal Systems Basic Safety Message"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/5tut-fj6e",
-            "issued": "2021-12-15",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Chambers",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "2024 Annual Report",
+            "identifier": "https://data.transportation.gov/api/views/5tut-fj6e",
+            "issued": "2021-12-15",
             "keyword": [
                 "bureau",
                 "container",
@@ -12539,28 +12538,43 @@
                 "transportation",
                 "vessel"
             ],
-            "identifier": "https://data.transportation.gov/api/views/5tut-fj6e",
+            "landingPage": "https://data.transportation.gov/d/5tut-fj6e",
+            "modified": "2025-01-17",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "2024 Annual Report",
             "title": "Supply-Chain Challenges"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyProgramURL": "http://www.nhtsa.gov/fuel-economy",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/5unf-wehy",
-            "issued": "2015-12-16",
-            "temporal": "2015/2016",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative - Regulatory",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-01",
-            "references": [
-                "http://www.nhtsa.gov/fuel-economy"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": false,
+            "description": "NHTSA's Corporate Average Fuel Economy (CAFE) program requires manufacturers of passenger cars and light trucks, produced for sale in the U.S., to meet CAFE standards, expressed in miles per gallon (mpg). The purpose of the CAFE program is to reduce the nation's energy consumption by increasing the fuel economy of cars and light trucks.  The CAFE Public Information Center (PIC) is the authoritative source for Corporate Average Fuel Economy (CAFE) program data. This site allows fuel economy data to be viewed in report and/or graph format. The data can be sorted and filtered to produce custom reports which can also be downloaded as Excel or pdf files. NHTSA periodically updates the CAFE data in the PIC and, therefore, each report and graph is date stamped to indicate the last time NHTSA made updates.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": " The data in this report are projected values based, in accordance with 49 CFR 537.7, on each manufacturer\u2019s Pre- and Mid-Model Year Reports and have not been validated or verified for NHTSA or EPA",
+                    "downloadURL": "http://www.nhtsa.gov/CAFE_PIC/MY%202014%20and%202015%20Projected%20Fuel%20Economy%20Performance%20Report.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "MYs 2014 and 2015 Projected Fuel Economy Performance Report"
+                }
             ],
+            "identifier": "1862.11",
+            "isPartOf": "DOT-1862",
+            "issued": "2015-12-16",
             "keyword": [
                 "amfa",
                 "civil penalties",
@@ -12577,80 +12591,48 @@
                 "report",
                 "shortfall"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "1862.11",
+            "landingPage": "https://data.transportation.gov/d/5unf-wehy",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-4936",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Highway Traffic Safety Administration"
             },
-            "description": "NHTSA's Corporate Average Fuel Economy (CAFE) program requires manufacturers of passenger cars and light trucks, produced for sale in the U.S., to meet CAFE standards, expressed in miles per gallon (mpg). The purpose of the CAFE program is to reduce the nation's energy consumption by increasing the fuel economy of cars and light trucks.  The CAFE Public Information Center (PIC) is the authoritative source for Corporate Average Fuel Economy (CAFE) program data. This site allows fuel economy data to be viewed in report and/or graph format. The data can be sorted and filtered to produce custom reports which can also be downloaded as Excel or pdf files. NHTSA periodically updates the CAFE data in the PIC and, therefore, each report and graph is date stamped to indicate the last time NHTSA made updates.",
-            "title": "CAFE (Corporate Average Fuel Economy) - MYs 2014 and 2015 Projected Fuel Economy Performance Report",
-            "isPartOf": "DOT-1862",
-            "agencyProgramURL": "http://www.nhtsa.gov/fuel-economy",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.nhtsa.gov/CAFE_PIC/MY%202014%20and%202015%20Projected%20Fuel%20Economy%20Performance%20Report.pdf",
-                    "description": " The data in this report are projected values based, in accordance with 49 CFR 537.7, on each manufacturer\u2019s Pre- and Mid-Model Year Reports and have not been validated or verified for NHTSA or EPA",
-                    "@type": "dcat:Distribution",
-                    "title": "MYs 2014 and 2015 Projected Fuel Economy Performance Report"
-                }
+            "references": [
+                "http://www.nhtsa.gov/fuel-economy"
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "temporal": "2015/2016",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Administrative - Regulatory",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-4936"
+            "title": "CAFE (Corporate Average Fuel Economy) - MYs 2014 and 2015 Projected Fuel Economy Performance Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://portal.phmsa.dot.gov/PDMPublicReport/?url=https://portal.phmsa.dot.gov/analytics/saw.dll?Portalpages&PortalPath=%2Fshared%2FPublic%20Website%20Pages%2F_portal%2F10%20Year%20Incident%20Summary%20Reports",
+            "agencyProgramURL": "http://www.phmsa.dot.gov/hazmat/incident-report",
+            "analysisUnit": "Incident",
             "bureauCode": [
                 "021:50"
             ],
-            "landingPage": "https://data.transportation.gov/d/5vv3-mqcv",
-            "issued": "2012-01-18",
-            "temporal": "R/2002-01-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-31",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "https://portal.phmsa.dot.gov/PDMPublicReport/?url=https://portal.phmsa.dot.gov/analytics/saw.dll?Portalpages&PortalPath=%2Fshared%2FPublic%20Website%20Pages%2F_portal%2F10%20Year%20Incident%20Summary%20Reports"
-            ],
-            "keyword": [
-                "hazardous material incidents",
-                "hazmat incidents",
-                "incidents"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Serita McKoy",
                 "hasEmail": "mailto:hmrequests@dot.gov"
             },
-            "identifier": "268.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Pipeline and Hazardous Materials Safety Administration"
-            },
+            "dataQuality": true,
             "description": "Series of Incident data and summary statistics reports produced which provide statistical information on incidents by type, year, geographical location, and others.   The data provided is that from the Hazardous Materials Incident Report Form 5800.1",
-            "title": "Hazmat 10 Year Incident Summary Reports - Data Mining Tool",
-            "isPartOf": "DOT-268",
-            "agencyProgramURL": "http://www.phmsa.dot.gov/hazmat/incident-report",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12659,50 +12641,52 @@
                     "title": "Data Mining Tool"
                 }
             ],
-            "spatial": "City",
-            "dataQuality": true,
+            "identifier": "268.1",
+            "isPartOf": "DOT-268",
+            "issued": "2012-01-18",
+            "keyword": [
+                "hazardous material incidents",
+                "hazmat incidents",
+                "incidents"
+            ],
+            "landingPage": "https://data.transportation.gov/d/5vv3-mqcv",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "https://portal.phmsa.dot.gov/PDMPublicReport/?url=https://portal.phmsa.dot.gov/analytics/saw.dll?Portalpages&PortalPath=%2Fshared%2FPublic%20Website%20Pages%2F_portal%2F10%20Year%20Incident%20Summary%20Reports",
+            "modified": "2024-07-31",
+            "phone": "202-366-3373",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Pipeline and Hazardous Materials Safety Administration"
+            },
+            "references": [
+                "https://portal.phmsa.dot.gov/PDMPublicReport/?url=https://portal.phmsa.dot.gov/analytics/saw.dll?Portalpages&PortalPath=%2Fshared%2FPublic%20Website%20Pages%2F_portal%2F10%20Year%20Incident%20Summary%20Reports"
+            ],
+            "spatial": "City",
+            "temporal": "R/2002-01-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Incident",
-            "phone": "202-366-3373",
-            "language": [
-                "en-US"
-            ]
+            "title": "Hazmat 10 Year Incident Summary Reports - Data Mining Tool"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/5x22-djnv",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-12-16",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-23",
-            "keyword": [
-                "allocation",
-                "funding",
-                "transit"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NTD Program Support",
                 "hasEmail": "mailto:NTDHelp@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Transit Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/5x22-djnv",
+            "dataQuality": true,
             "description": "Dataset containing all of the Federal Funding Allocation inputs submitted by reporting transit agencies to the National Transit Database in the 2022 and 2023 report years. This reflects the most recently published data within the Federal Transit Administration's NTD Data website.",
-            "title": "2022 - 2023 NTD Annual Data - Federal Funding Allocation",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12710,48 +12694,82 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5x22-djnv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5x22-djnv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5x22-djnv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/5x22-djnv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5x22-djnv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5x22-djnv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5x22-djnv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5x22-djnv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5x22-djnv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/5x22-djnv",
+            "issued": "2024-12-16",
+            "keyword": [
+                "allocation",
+                "funding",
+                "transit"
+            ],
+            "landingPage": "https://data.transportation.gov/d/5x22-djnv",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-23",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Transit Administration"
+            },
             "spatial": "United States",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1M",
             "theme": [
                 "Public Transit"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2022 - 2023 NTD Annual Data - Federal Funding Allocation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/5xs4-x86w",
-            "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": false,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
+            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "2011 New Hampshire HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/newhampshire2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 New Hampshire"
+                }
+            ],
+            "identifier": "678.31",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -12765,60 +12783,56 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 New Hampshire",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/5xs4-x86w",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5035",
             "primaryITInvestmentUII": "021-099281808",
             "programCode": [
                 "021:009"
             ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/newhampshire2011.zip",
-                    "description": "2011 New Hampshire HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 New Hampshire"
-                }
-            ],
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "temporal": "R/1981-11-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
-            "categoryDesignation": "Administrative",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-5035"
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 New Hampshire"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/SafetyProgram/home.aspx",
+            "agencyProgramURL": "http://ai.fmcsa.dot.gov/SafetyProgram/Home.aspx",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/5yi3-ymwv",
-            "issued": "2018-12-17",
-            "temporal": "R/2009-10-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://ai.fmcsa.dot.gov/InfoCenter/Default.aspx#question402"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This area of the website provides information on three of the safety programs established by FMCSA to support this mission.  The three programs covered by this area include reviews, roadside inspections of commercial vehicles and drivers, and traffic enforcement stops of CMVs operating in an unsafe manner. Each program is implemented in conjunction with the states and devoted to improving motor carrier safety by reducing the number and severity of crashes involving large trucks and buses.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://ai.fmcsa.dot.gov/SafetyProgram/home.aspx",
+                    "mediaType": "text/html",
+                    "title": "Data Mining Tool"
+                }
             ],
+            "identifier": "114.2",
+            "isPartOf": "DOT-114",
+            "issued": "2018-12-17",
             "keyword": [
                 "a&i",
                 "a&i online",
@@ -12838,56 +12852,60 @@
                 "safety programs",
                 "traffic enforcement"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "114.2",
+            "landingPage": "https://data.transportation.gov/d/5yi3-ymwv",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-24",
+            "phone": "202-366-4869",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Motor Carrier Safety Administration"
             },
-            "description": "This area of the website provides information on three of the safety programs established by FMCSA to support this mission.  The three programs covered by this area include reviews, roadside inspections of commercial vehicles and drivers, and traffic enforcement stops of CMVs operating in an unsafe manner. Each program is implemented in conjunction with the states and devoted to improving motor carrier safety by reducing the number and severity of crashes involving large trucks and buses.",
-            "title": "A&I - Safety Programs - Data Mining Tool",
-            "isPartOf": "DOT-114",
-            "agencyProgramURL": "http://ai.fmcsa.dot.gov/SafetyProgram/Home.aspx",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://ai.fmcsa.dot.gov/SafetyProgram/home.aspx",
-                    "mediaType": "text/html",
-                    "title": "Data Mining Tool"
-                }
+            "references": [
+                "http://ai.fmcsa.dot.gov/InfoCenter/Default.aspx#question402"
             ],
             "spatial": "National and State level statistics.",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/SafetyProgram/home.aspx",
+            "temporal": "R/2009-10-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4869",
-            "language": [
-                "en-US"
-            ]
+            "title": "A&I - Safety Programs - Data Mining Tool"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/5yir-bnfe",
-            "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": false,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
+            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "2013 Wyoming HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/wyoming2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Wyoming"
+                }
+            ],
+            "identifier": "678.153",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -12901,78 +12919,40 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.153",
+            "landingPage": "https://data.transportation.gov/d/5yir-bnfe",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5035",
+            "primaryITInvestmentUII": "021-099281808",
+            "programCode": [
+                "021:009"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Wyoming",
-            "isPartOf": "DOT-678",
-            "primaryITInvestmentUII": "021-099281808",
-            "programCode": [
-                "021:009"
+            "temporal": "R/1981-11-01/P1Y",
+            "theme": [
+                "Transportation"
             ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/wyoming2013.zip",
-                    "description": "2013 Wyoming HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Wyoming"
-                }
-            ],
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
-            ],
-            "accrualPeriodicity": "R/P1Y",
-            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
-            "categoryDesignation": "Administrative",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-5035"
-        },
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Wyoming"
+        },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/5yqg-88j3",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2020-04-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-25",
-            "keyword": [
-                "contribution of transportation",
-                "economics",
-                "gross domestic product",
-                "satellite accounts",
-                "transportation",
-                "value of transportation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/5yqg-88j3",
             "description": "The Transportation Satellite Accounts (TSAs) provide a means for measuring the contribution of transportation services to the national economy. Prior to the TSAs, the magnitude of transportation services had long been underestimated, as most national measures counted only the value of for-hire services. Measurement of services provided only by for-hire firms misses the sizable contribution of transportation services that take place within nontransportation industries, termed as in-house transportation.\r\n\r\nTo more accurately measure transportation services, the Bureau of Transportation Statistics (BTS) of the U.S. Department of Transportation and the Bureau of Economic Analysis (BEA) of the U.S. Department of Commerce, jointly developed the Transportation Satellite Accounts (TSAs). The TSAs, as a supplement to the U.S. Input-Output (I-O) Accounts, measure the contribution of both for-hire and in-house transportation. The TSAs include all seven of the for-hire transportation industries reported in the U.S. I-O accounts and four in-house transportation modes.",
-            "title": "Transportation Satellite Accounts Table",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12980,66 +12960,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5yqg-88j3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5yqg-88j3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5yqg-88j3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/5yqg-88j3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5yqg-88j3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5yqg-88j3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5yqg-88j3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5yqg-88j3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5yqg-88j3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/5yqg-88j3",
+            "issued": "2020-04-02",
+            "keyword": [
+                "contribution of transportation",
+                "economics",
+                "gross domestic product",
+                "satellite accounts",
+                "transportation",
+                "value of transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/5yqg-88j3",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-11-25",
+            "phone": "202-366-DATA(3282)",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Transportation Satellite Accounts Table"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2022-07-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "highway",
-                "highway performance monitoring",
-                "highway performance monitoring system",
-                "highways",
-                "hpms",
-                "sample"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/5yyw-77w8",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 2001",
-            "title": "Historic HPMS Data (Sample) - 2001",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13047,50 +13027,86 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5yyw-77w8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5yyw-77w8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5yyw-77w8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/5yyw-77w8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5yyw-77w8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5yyw-77w8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/5yyw-77w8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/5yyw-77w8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/5yyw-77w8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/5yyw-77w8",
+            "issued": "2022-07-08",
+            "keyword": [
+                "highway",
+                "highway performance monitoring",
+                "highway performance monitoring system",
+                "highways",
+                "hpms",
+                "sample"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-08",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
             "spatial": "United States",
-            "dataQuality": true,
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Historic HPMS Data (Sample) - 2001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/on_the_fly_download.aspx",
+            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
+            "analysisUnit": "Form 54 Filing",
             "bureauCode": [
                 "021:27"
             ],
-            "landingPage": "https://data.transportation.gov/d/5zq6-fmjj",
-            "issued": "2010-09-29",
-            "temporal": "R/1975-01-31/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-09",
+            "categoryDesignation": "Research",
             "collectionInstrument": "FORM FRA F 6180.54 (OMB No. 2130-0500)",
-            "references": [
-                "https://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Newregulation.aspx%3Fdoc=FRAGuideforPreparingAccIncReportspubMay2011.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/DownloadFStructure.aspx",
+            "description": "\"This file contains reported cases of collisions, derailments, fires, explosions, acts of God, or other events involving the operation of railroad on-track equipment and involving damages exceeding the reporting threshold for the year reported. National files from 1975 through the current year are available for download. In addition, individual files by State are available for the years 1991 through the current year.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/graphs.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Accident Trends - Graphs & Charts"
+                }
             ],
+            "identifier": "199.12",
+            "isPartOf": "DOT-199",
+            "issued": "2010-09-29",
             "keyword": [
                 "acts of god",
                 "collisions",
@@ -13101,65 +13117,39 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "199.12",
+            "landingPage": "https://data.transportation.gov/d/5zq6-fmjj",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-10-09",
+            "phone": "202-493-6483",
+            "programCode": [
+                "021:036"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Railroad Administration"
             },
-            "description": "\"This file contains reported cases of collisions, derailments, fires, explosions, acts of God, or other events involving the operation of railroad on-track equipment and involving damages exceeding the reporting threshold for the year reported. National files from 1975 through the current year are available for download. In addition, individual files by State are available for the years 1991 through the current year.",
-            "title": "Rail Equipment Accidents - Accident Trends - Graphs & Charts",
-            "isPartOf": "DOT-199",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:036"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/graphs.aspx",
-                    "mediaType": "text/csv",
-                    "title": "Accident Trends - Graphs & Charts"
-                }
+            "references": [
+                "https://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Newregulation.aspx%3Fdoc=FRAGuideforPreparingAccIncReportspubMay2011.pdf"
             ],
             "spatial": "Latitude/Longitude, County, State",
-            "describedBy": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/DownloadFStructure.aspx",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/on_the_fly_download.aspx",
+            "temporal": "R/1975-01-31/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Form 54 Filing",
-            "phone": "202-493-6483",
-            "language": [
-                "en-US"
-            ]
+            "title": "Rail Equipment Accidents - Accident Trends - Graphs & Charts"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/627w-fm4v",
-            "issued": "2023-08-08",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
-            "identifier": "https://data.transportation.gov/api/views/627w-fm4v",
             "description": "",
-            "title": "Data Release Schedule",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13167,65 +13157,55 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/627w-fm4v/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/627w-fm4v/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/627w-fm4v/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/627w-fm4v/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/627w-fm4v/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/627w-fm4v/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/627w-fm4v/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/627w-fm4v/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/627w-fm4v/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/627w-fm4v",
+            "issued": "2023-08-08",
+            "landingPage": "https://data.transportation.gov/d/627w-fm4v",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Data Release Schedule"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/motorfuelhwy_trustfund.cfm",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2019-01-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "diesel",
-                "gallons",
-                "gasoline/gasohol",
-                "month",
-                "special fuel",
-                "year"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/6376-ubwf",
+            "dataQuality": true,
             "description": "Summary monthly motor fuel data on the amount of on-highway fuel used at the national level.  Includes the amount of gallons of gasoline/gasohol and special fuel (primarily diesel) taxed each month.",
-            "title": "Monthly Motor Fuel - National",
-            "isPartOf": "Monthly Motor Fuel",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13233,68 +13213,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6376-ubwf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6376-ubwf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6376-ubwf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/6376-ubwf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6376-ubwf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6376-ubwf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6376-ubwf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6376-ubwf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6376-ubwf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/6376-ubwf",
+            "isPartOf": "Monthly Motor Fuel",
+            "issued": "2019-01-08",
+            "keyword": [
+                "diesel",
+                "gallons",
+                "gasoline/gasohol",
+                "month",
+                "special fuel",
+                "year"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/motorfuelhwy_trustfund.cfm",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
+            "modified": "2024-05-08",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Monthly Motor Fuel - National"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/63me-zi7c",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2024-05-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-30",
-            "keyword": [
-                "ferry",
-                "ferry operators",
-                "ferry transit",
-                "ncfo",
-                "passenger ferry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joe McGill",
                 "hasEmail": "mailto:joseph.mcgill@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/63me-zi7c",
             "description": "A data base of responses to the 2022 National Census of Ferries.\n\nThis file gives information about ferry operators.",
-            "title": "2022 NCFO Operators File",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13302,66 +13282,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/63me-zi7c/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/63me-zi7c/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/63me-zi7c/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/63me-zi7c/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/63me-zi7c/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/63me-zi7c/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/63me-zi7c/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/63me-zi7c/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/63me-zi7c/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/63me-zi7c",
+            "issued": "2024-05-01",
+            "keyword": [
+                "ferry",
+                "ferry operators",
+                "ferry transit",
+                "ncfo",
+                "passenger ferry"
+            ],
+            "landingPage": "https://data.transportation.gov/d/63me-zi7c",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-05-30",
+            "programCode": [
+                "021:042"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Maritime and Waterways"
-            ]
+            ],
+            "title": "2022 NCFO Operators File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "The data system is not publicly available because it is related solely to internal agency management and may contain sensitive data.",
+            "accrualPeriodicity": "R/PT1S",
+            "agencyDataSeriesURL": "https://apps.fhwa.dot.gov/",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/63pf-8mej",
-            "issued": "2014-12-29",
-            "temporal": "R/2014-12-29/PT1S",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative - Financial",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
-            "keyword": [
-                "eis",
-                "environmental",
-                "nepa",
-                "project"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "689.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://our.dot.gov/office/fhwa.init/papai/PAPAI%20Documentation/Forms/AllItems.aspx",
             "description": "EDTS/PAPAI is a monitoring system that tracks NEPA project progress between major milestones, and helps accurately determine the total processing time from initiation of an Environmental Impact Statement (EIS) or Environmental Assessment (EA) to the approval of the final decision document, one component of the Every Day Counts Initiative. This information is used for regular reports to the Council on Environmental Quality (CEQ) as well as FHWA and US DOT leadership. EDTS is being upgraded to add project and action tracking, with the enhanced system being renamed PAPAI.%3F",
-            "title": "Project And Program Action Information System (PAPAI) -",
-            "primaryITInvestmentUII": "021-072162563",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13369,52 +13352,49 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "National, State, County, Project",
-            "describedBy": "http://our.dot.gov/office/fhwa.init/papai/PAPAI%20Documentation/Forms/AllItems.aspx",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "https://apps.fhwa.dot.gov/",
-            "theme": [
-                "Transportation"
+            "identifier": "689.0",
+            "issued": "2014-12-29",
+            "keyword": [
+                "eis",
+                "environmental",
+                "nepa",
+                "project"
             ],
-            "accrualPeriodicity": "R/PT1S",
-            "categoryDesignation": "Administrative - Financial",
+            "landingPage": "https://data.transportation.gov/d/63pf-8mej",
             "language": [
                 "en-US"
             ],
-            "phone": "360-753-9413"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "360-753-9413",
+            "primaryITInvestmentUII": "021-072162563",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "rights": "The data system is not publicly available because it is related solely to internal agency management and may contain sensitive data.",
+            "spatial": "National, State, County, Project",
+            "temporal": "R/2014-12-29/PT1S",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Project And Program Action Information System (PAPAI) -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/63rf-6igh",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-09-06",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-07",
-            "keyword": [
-                "fra",
-                "public safety",
-                "public transit",
-                "rail",
-                "railroad employee",
-                "safety",
-                "security events",
-                "transportation security"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NTD Program Support",
                 "hasEmail": "mailto:NTDHelp@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Transit Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/63rf-6igh",
             "description": "Counts of Non-Major Safety and Security Events are reported to the National Transit Database on a monthly basis, by transit agency and transit mode. These include minor fires on transit property requiring suppression, transit worker assaults not involving transport for medical attention, and other safety events that are not reportable as Major Events because a Major Event reporting threshold is not met (see Safety and Security Events dataset for a list of Major Events).\n\nThis file includes event data reported to the National Transit Database (NTD) for Commuter Rail (CR) and Alaska Railroad (AR) modes, as well as Heavy Rail (HR) service reported for Port Authority Trans Hudson (NTD ID: 20098), Hybrid Rail (YR) service for the Tri-County Metropolitan Transportation District of Oregon (NTD ID: 00008), Hybrid Rail (YR) service for Denton County Transportation Authority (NTD ID: 60101), and Hybrid Rail (YR) service for Capital Metropolitan Transportation Authority (NTD ID: 60048). Because these services fall under the safety oversight of the Federal Railroad Administration, the agencies are not required to report Safety Events (e.g., collisions, derailments, etc.) to the Federal Transit Administration through the NTD. Security events occurring on transit-owned property for these entities are reported to NTD, but excluded from other files to preserve the integrity of those datasets. They are presented in this file for completeness and should be considered by any user attempting to understand the scope and scale of reportable Security Events reported by public transit operators.",
-            "title": "Non-Major Safety and Security Events (FRA Commuter Rail Only)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13422,50 +13402,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/63rf-6igh/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/63rf-6igh/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/63rf-6igh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/63rf-6igh/rows.json?accessType=DOWNLOAD",
```

