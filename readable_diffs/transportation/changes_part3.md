# Change History for transportation.json (Part 3)

### Changes from 31606f9 to dd2190f (Part 2/9)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/63rf-6igh/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/63rf-6igh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/63rf-6igh/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/63rf-6igh/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/63rf-6igh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/63rf-6igh",
+            "issued": "2024-09-06",
+            "keyword": [
+                "fra",
+                "public safety",
+                "public transit",
+                "rail",
+                "railroad employee",
+                "safety",
+                "security events",
+                "transportation security"
+            ],
+            "landingPage": "https://data.transportation.gov/d/63rf-6igh",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-07",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Transit Administration"
+            },
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "Non-Major Safety and Security Events (FRA Commuter Rail Only)"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/63ub-atmy",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/63ub-atmy",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "All Passenger Rail",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13473,42 +13463,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/63ub-atmy/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/63ub-atmy/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/63ub-atmy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/63ub-atmy/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/63ub-atmy/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/63ub-atmy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/63ub-atmy/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/63ub-atmy/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/63ub-atmy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/63ub-atmy",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/63ub-atmy",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "All Passenger Rail"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/645r-xr7k",
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
+                    "description": "2013 Colorado HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/colorado2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Colorado"
+                }
+            ],
+            "identifier": "678.110",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -13522,85 +13540,47 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.110",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Colorado",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/645r-xr7k",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/colorado2013.zip",
-                    "description": "2013 Colorado HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Colorado"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Colorado"
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
-            "landingPage": "https://data.transportation.gov/d/64a8-jmz6",
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
-            "identifier": "693.11",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
             "description": "The NBI System is the collection of bridge inspection information and costs associated with bridge replacements of structurally deficient bridges on and off the NHS. This data is collected under the auspices of the National Bridge Inspection Standards (NBIS) as prescribed by law. The NBI System collects the information that is used to determine eligibility for NHS projects, performance measure reporting, NHS penalty determination, and reporting to Congress.  It supports oversight of the NBIS through various report tools, and provides data reporting that supports agency strategic goals.",
-            "title": "National Bridge Inventory System (NBI) - 2002",
-            "isPartOf": "DOT-693",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
-            "primaryITInvestmentUII": "021-012940226",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13609,60 +13589,59 @@
                     "title": "2002"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
-            "dataQuality": true,
+            "identifier": "693.11",
+            "isPartOf": "DOT-693",
+            "issued": "1992-12-31",
+            "keyword": [
+                "bridge",
+                "condition",
+                "deck",
+                "inspection",
+                "structure"
+            ],
+            "landingPage": "https://data.transportation.gov/d/64a8-jmz6",
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
+            "title": "National Bridge Inventory System (NBI) - 2002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "rights": "The data system is not available to the general public because it contains data related to recipients of Federal highway funding and limited access is integral to system controls.",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/travelmonitoring.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/64sm-qkis",
-            "issued": "2014-12-29",
-            "temporal": "R/2014-12-29/P1M",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
-            "references": [
-                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
-            ],
-            "keyword": [
-                "aadt",
-                "travel",
-                "vmt"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "700.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "Internal FHWA data program that assists in the collection and analysis of data on traffic volumes, vehicle classification, truck weights for traffic statistics, analysis; it is used for development of policies and regulations.  The monthly data are published in the Traffic Volume Trends (TVT) report.",
-            "title": "Travel Monitoring Analysis System (TMAS) - Travel Monitoring Analysis System",
-            "isPartOf": "DOT-700",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/travelmonitoring.cfm",
-            "primaryITInvestmentUII": "021-938741189",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13671,43 +13650,49 @@
                     "title": "Travel Monitoring Analysis System"
                 }
             ],
-            "spatial": "National, State, Urban, Rural",
-            "dataQuality": true,
+            "identifier": "700.1",
+            "isPartOf": "DOT-700",
+            "issued": "2014-12-29",
+            "keyword": [
+                "aadt",
+                "travel",
+                "vmt"
+            ],
+            "landingPage": "https://data.transportation.gov/d/64sm-qkis",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "modified": "2024-05-08",
+            "phone": "202-366-1874",
+            "primaryITInvestmentUII": "021-938741189",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
+            ],
+            "rights": "The data system is not available to the general public because it contains data related to recipients of Federal highway funding and limited access is integral to system controls.",
+            "spatial": "National, State, Urban, Rural",
+            "temporal": "R/2014-12-29/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Research",
-            "phone": "202-366-1874",
-            "language": [
-                "en-US"
-            ]
+            "title": "Travel Monitoring Analysis System (TMAS) - Travel Monitoring Analysis System"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/65fa-qbkf",
-            "issued": "2024-07-05",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-07",
-            "keyword": [
-                "alaska rail",
-                "commuter rail",
-                "security events"
-            ],
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FTA-NTD Data Team",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
-            "identifier": "https://data.transportation.gov/api/views/65fa-qbkf",
             "description": "This file includes event data reported to the National Transit Database (NTD) for Commuter Rail (CR) and Alaska Railroad (AR) modes, as well as Heavy Rail (HR) service reported for Port Authority Trans Hudson (NTD ID: 20098), Hybrid Rail (YR) service for the Tri-County Metropolitan Transportation District of Oregon (NTD ID: 00008),  Hybrid Rail (YR) service for Denton County Transportation Authority (NTD ID: 60101), and Hybrid Rail (YR) service for Capital Metropolitan Transportation Authority (NTD ID: 60048). Because these services fall under the safety oversight of the Federal Railroad Administration, the agencies are not required to report Safety Events (e.g., collisions, derailments, etc.) to the Federal Transit Administration through the NTD. Security events occurring on transit-owned property for these entities are reported to NTD, but excluded from other files to preserve the integrity of those datasets. They are presented in this file for completeness and should be considered by any user attempting to understand the scope and scale of reportable Security Events reported by public transit operators.",
-            "title": "FRA Regulated Mode Major Security Events",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13715,63 +13700,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/65fa-qbkf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/65fa-qbkf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/65fa-qbkf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/65fa-qbkf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/65fa-qbkf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/65fa-qbkf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/65fa-qbkf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/65fa-qbkf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/65fa-qbkf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/65fa-qbkf",
+            "issued": "2024-07-05",
+            "keyword": [
+                "alaska rail",
+                "commuter rail",
+                "security events"
+            ],
+            "landingPage": "https://data.transportation.gov/d/65fa-qbkf",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-07",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "FRA Regulated Mode Major Security Events"
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
-            "identifier": "https://data.transportation.gov/api/views/65pp-nswq",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 2008",
-            "title": "Historic HPMS Data (Universe) - 2008",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13779,68 +13760,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/65pp-nswq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/65pp-nswq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/65pp-nswq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/65pp-nswq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/65pp-nswq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/65pp-nswq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/65pp-nswq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/65pp-nswq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/65pp-nswq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/65pp-nswq",
+            "issued": "2022-07-08",
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
+            "title": "Historic HPMS Data (Universe) - 2008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://safer.fmcsa.dot.gov/UCRQueryForm.aspx",
+            "agencyProgramURL": "http://safer.fmcsa.dot.gov/",
+            "analysisUnit": "Carrier",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/664v-y7h2",
-            "issued": "1974-06-01",
-            "temporal": "R/1974-06-01/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "carrier",
-                "registration"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO",
                 "hasEmail": "mailto:fmcsa.cdo@dot.gov"
             },
-            "identifier": "102.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": true,
             "description": "Collects information from the State of Indiana's UCR Payment System.",
-            "title": "Unified Carrier Registration (UCR) - Online Form",
-            "isPartOf": "DOT-102",
-            "agencyProgramURL": "http://safer.fmcsa.dot.gov/",
-            "programCode": [
-                "021:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13849,35 +13835,65 @@
                     "title": "Online Form"
                 }
             ],
-            "spatial": "State",
-            "dataQuality": true,
+            "identifier": "102.2",
+            "isPartOf": "DOT-102",
+            "issued": "1974-06-01",
+            "keyword": [
+                "carrier",
+                "registration"
+            ],
+            "landingPage": "https://data.transportation.gov/d/664v-y7h2",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://safer.fmcsa.dot.gov/UCRQueryForm.aspx",
+            "modified": "2024-05-24",
+            "phone": "202-493-0215",
+            "programCode": [
+                "021:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "spatial": "State",
+            "temporal": "R/1974-06-01/P1D",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "analysisUnit": "Carrier",
-            "categoryDesignation": "Research",
-            "phone": "202-493-0215",
-            "language": [
-                "en-US"
-            ]
+            "title": "Unified Carrier Registration (UCR) - Online Form"
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
-            "landingPage": "https://data.transportation.gov/d/66v9-pq3s",
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
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/tenyr2a.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Ten Year Accident/Incident Overview by Railroad/Region/State/County"
+                }
             ],
+            "identifier": "199.7",
+            "isPartOf": "DOT-199",
+            "issued": "2010-09-29",
             "keyword": [
                 "acts of god",
                 "collisions",
@@ -13888,91 +13904,93 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "199.7",
+            "landingPage": "https://data.transportation.gov/d/66v9-pq3s",
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
-            "title": "Rail Equipment Accidents - Ten Year Accident/Incident Overview by Railroad/Region/State/County",
-            "isPartOf": "DOT-199",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:036"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/tenyr2a.aspx",
-                    "mediaType": "text/csv",
-                    "title": "Ten Year Accident/Incident Overview by Railroad/Region/State/County"
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
+            "title": "Rail Equipment Accidents - Ten Year Accident/Incident Overview by Railroad/Region/State/County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/67qi-gcuu",
             "bureauCode": [
                 "021:27"
             ],
-            "issued": "2024-12-17",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Data Team",
                 "hasEmail": "mailto:list-fra-safeteam@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Railroad Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/67qi-gcuu",
+            "dataQuality": true,
             "description": "This is the Train Accident/Incident (Form 54) PDF Generator report.",
-            "title": "Train Accident/Incident (Form 54) PDF Generator",
+            "identifier": "https://data.transportation.gov/api/views/67qi-gcuu",
+            "issued": "2024-12-17",
+            "landingPage": "https://data.transportation.gov/d/67qi-gcuu",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-27",
             "programCode": [
                 "021:036"
             ],
-            "license": "https://www.usa.gov/government-works",
-            "dataQuality": true,
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
+            "title": "Train Accident/Incident (Form 54) PDF Generator"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/67uc-9bwv",
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
+                    "description": "2012 New Mexico HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/newmexico2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 New Mexico"
+                }
+            ],
+            "identifier": "678.85",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -13986,107 +14004,69 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.85",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 New Mexico",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/67uc-9bwv",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/newmexico2012.zip",
-                    "description": "2012 New Mexico HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 New Mexico"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 New Mexico"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/68ki-z3wu",
-            "issued": "2022-03-10",
             "@type": "dcat:Dataset",
-            "modified": "2022-10-17",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/68ki-z3wu",
+            "issued": "2022-03-10",
+            "landingPage": "https://data.transportation.gov/d/68ki-z3wu",
+            "modified": "2022-10-17",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
-            "title": "THE TRANSPORTATION FUTURE: TRENDS, TRANSPORTATION, AND TRAVEL",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "THE TRANSPORTATION FUTURE: TRENDS, TRANSPORTATION, AND TRAVEL"
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
-            "landingPage": "https://data.transportation.gov/d/692z-xt44",
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
-            "identifier": "693.21",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
             "description": "The NBI System is the collection of bridge inspection information and costs associated with bridge replacements of structurally deficient bridges on and off the NHS. This data is collected under the auspices of the National Bridge Inspection Standards (NBIS) as prescribed by law. The NBI System collects the information that is used to determine eligibility for NHS projects, performance measure reporting, NHS penalty determination, and reporting to Congress.  It supports oversight of the NBIS through various report tools, and provides data reporting that supports agency strategic goals.",
-            "title": "National Bridge Inventory System (NBI) - 2012",
-            "isPartOf": "DOT-693",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
-            "primaryITInvestmentUII": "021-012940226",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14095,58 +14075,60 @@
                     "title": "2012"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
-            "dataQuality": true,
+            "identifier": "693.21",
+            "isPartOf": "DOT-693",
+            "issued": "1992-12-31",
+            "keyword": [
+                "bridge",
+                "condition",
+                "deck",
+                "inspection",
+                "structure"
+            ],
+            "landingPage": "https://data.transportation.gov/d/692z-xt44",
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
+            "title": "National Bridge Inventory System (NBI) - 2012"
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
-            "landingPage": "https://data.transportation.gov/d/69ca-qd7k",
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
-            "identifier": "364.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database - Vehicle Test Query by Vehicle Test Parameters",
-            "isPartOf": "DOT-364",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
-            "primaryITInvestmentUII": "021-621341357",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14155,34 +14137,80 @@
                     "title": "Vehicle Test Query by Vehicle Test Parameters"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.1",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/69ca-qd7k",
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
+            "title": "Vehicle Safety Research and Development Database - Vehicle Test Query by Vehicle Test Parameters"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://github.com/usdot-jpo-ode/jpo-wzdx",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2019-10-15",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-04",
-            "references": [
-                "http://usdot-its-workzone-publicdata.s3.amazonaws.com/index.html",
-                "https://github.com/usdot-jpo-ode/jpo-wzdx"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kate Hartman",
+                "hasEmail": "mailto:kate.hartman@dot.gov"
+            },
+            "description": "This dataset contains the up-to-date metadata on Work Zone feeds that meet the Work Zone Data Exchange (WZDx) specifications and is registered with USDOT ITS DataHub.  The current work zone data from each feed can be accessed through their respective API links. Some links provide direct access, while others require a user to create their own API access key first. Please see the attached API Key Instructions document to learn how to sign up for API keys for the requisite feeds.\n\nThe <a href=\"https://usdot-its-workzone-publicdata.s3.amazonaws.com/index.html\" target=\"_blank\" rel=\"noopener noreferrer\">ITS Work Zone Sandbox</a>, contains an archive of work zone data collected from each feed at a rate of at least every 15 minutes. This is not intended as a replacement for the work zone feeds and in many cases does not update as frequently as the feed does.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/api/views/69qe-yiui/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.transportation.gov/api/views/69qe-yiui/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.transportation.gov/api/views/69qe-yiui/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.transportation.gov/api/views/69qe-yiui/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.transportation.gov/api/views/69qe-yiui/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.transportation.gov/api/views/69qe-yiui/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.transportation.gov/api/views/69qe-yiui/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
             ],
+            "identifier": "https://data.transportation.gov/api/views/69qe-yiui",
+            "issued": "2019-10-15",
             "keyword": [
                 "arterial",
                 "automobiles",
@@ -14203,94 +14231,47 @@
                 "trucking & motorcoaches",
                 "work zone data exchange (wzdx)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "US Department of Transportation"
-            },
-            "identifier": "https://data.transportation.gov/api/views/69qe-yiui",
-            "description": "This dataset contains the up-to-date metadata on Work Zone feeds that meet the Work Zone Data Exchange (WZDx) specifications and is registered with USDOT ITS DataHub.  The current work zone data from each feed can be accessed through their respective API links. Some links provide direct access, while others require a user to create their own API access key first. Please see the attached API Key Instructions document to learn how to sign up for API keys for the requisite feeds.\n\nThe <a href=\"https://usdot-its-workzone-publicdata.s3.amazonaws.com/index.html\" target=\"_blank\" rel=\"noopener noreferrer\">ITS Work Zone Sandbox</a>, contains an archive of work zone data collected from each feed at a rate of at least every 15 minutes. This is not intended as a replacement for the work zone feeds and in many cases does not update as frequently as the feed does.",
-            "title": "Work Zone Data Exchange (WZDx) Feed Registry",
+            "landingPage": "https://github.com/usdot-jpo-ode/jpo-wzdx",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2020-06-04",
             "programCode": [
                 "021:042"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/api/views/69qe-yiui/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/69qe-yiui/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.transportation.gov/api/views/69qe-yiui/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/69qe-yiui/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.transportation.gov/api/views/69qe-yiui/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/69qe-yiui/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.transportation.gov/api/views/69qe-yiui/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
+            "references": [
+                "http://usdot-its-workzone-publicdata.s3.amazonaws.com/index.html",
+                "https://github.com/usdot-jpo-ode/jpo-wzdx"
             ],
             "spatial": "USA",
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Work Zone Data Exchange (WZDx) Feed Registry"
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
-            "landingPage": "https://data.transportation.gov/d/6a4j-9cse",
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
-            "identifier": "692.13",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - Cyclist Fatal Crashes 2009-2012",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "primaryITInvestmentUII": "021-845083703",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14299,56 +14280,50 @@
                     "title": "Cyclist Fatal Crashes 2009-2012"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.13",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/6a4j-9cse",
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
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - Cyclist Fatal Crashes 2009-2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/6a6e-vfvi",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2024-11-04",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-24",
-            "keyword": [
-                "aerial videography",
-                "automated vehicles",
-                "human-automated vehicle interactions",
-                "infrastructure-based videography",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "multi-modal trajectories",
-                "tgsim",
-                "third generation simulation",
-                "vehicle trajectory data"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyungjun Park",
                 "hasEmail": "mailto:hyungjun.park@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/6a6e-vfvi",
             "description": "The main dataset is a 130 MB file of trajectory data (I90_94_moving_final.csv) that contains position, speed, and acceleration data for small and large automated (L2) and non-automated vehicles on a highway in an urban environment. Supporting files include aerial reference images for four distinct data collection \u201cRuns\u201d (I90_94_moving_RunX_with_lanes.png, where X equals 1, 2, 3, and 4). Associated centerline files are also provided for each \u201cRun\u201d (I-90-moving-Run_X-geometry-with-ramps.csv). In each centerline file, x and y coordinates (in meters) marking each lane centerline are provided. The origin point of the reference image is located at the top left corner. Additionally, in each centerline file, an indicator variable is used for each lane to define the following types of road sections: 0=no ramp, 1=on-ramps, 2=off-ramps, and 3=weaving segments. The number attached to each column header is the numerical ID assigned for the specific lane (see \u201cTGSIM \u2013 Centerline Data Dictionary \u2013 I90_94moving.csv\u201d for more details). The dataset defines six northbound lanes using these centerline files. Images that map the lanes of interest to the numerical lane IDs referenced in the trajectory dataset are stored in the folder titled \u201cAnnotation on Regions.zip\u201d. The northbound lanes are shown visually from left to right in I90_94_moving_lane1.png through I90_94_moving_lane6.png.\n\nThis dataset was collected as part of the Third Generation Simulation Data (TGSIM): A Closer Look at the Impacts of Automated Driving Systems on Human Behavior project. During the project, six trajectory datasets capable of characterizing human-automated vehicle interactions under a diverse set of scenarios in highway and city environments were collected and processed. For more information, see the project report found here: https://rosap.ntl.bts.gov/view/dot/74647. This dataset, which is one of the six collected as part of the TGSIM project, contains data collected using one high-resolution 8K camera mounted on a helicopter that followed three SAE Level 2 ADAS-equipped vehicles (one at a time) northbound through the 4 km long segment at an altitude of 200 meters. Once a vehicle finished the segment, the helicopter would return to the beginning of the segment to follow the next SAE Level 2 ADAS-equipped vehicle to ensure continuous data collection. The segment was selected to study mandatory and discretionary lane changing and last-minute, forced lane-changing maneuvers. The segment has five off-ramps and three on-ramps to the right and one off-ramp and one on-ramp to the left. All roads have 88 kph (55 mph) speed limits. The camera captured footage during the evening rush hour (3:00 PM-5:00 PM CT) on a cloudy day.\n\nAs part of this dataset, the following files were provided:\n<ul><li>I90_94_moving_final.csv contains the numerical data to be used for analysis that includes vehicle level trajectory data at every 0.1 second. Vehicle size (small or large), width, length, and whether the vehicle was one of the automated test vehicles (\"yes\" or \"no\") are provided with instantaneous location, speed, and acceleration data. All distance measurements (width, length, location) were converted from pixels to meters using the following conversion factor: 1 pixel = 0.3-meter conversion.</li>\n<li>I90_94_moving_RunX_with_lanes.png are the aerial reference images that define the geographic region and associated roadway segments of interest (see bounding boxes on northbound lanes) for each run X.</li>\n<li>I-90-moving-Run_X-geometry-with-ramps.csv contain the coordinates that define the lane centerlines for each Run X. The \"x\" and \"y\" columns represent the horizontal and vertical locations in the reference image, respectively. The \"ramp\" columns define the type of roadway segment (0=no ramp, 1=on-ramps, 2=off-ramps, and 3=weaving segments). In total, the centerline files define six northbound lanes.</li>\n<li>Annotation on Regions.zip, which includes images that visually map lanes (I90_9",
-            "title": "Third Generation Simulation Data (TGSIM) I-90/I-94 Moving Trajectories",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14356,47 +14331,87 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6a6e-vfvi/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6a6e-vfvi/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6a6e-vfvi/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/6a6e-vfvi/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6a6e-vfvi/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6a6e-vfvi/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6a6e-vfvi/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6a6e-vfvi/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6a6e-vfvi/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "I-90/I94 in Chicago, IL; I-294 near Hinsdale, IL; I-395 in Washington DC; George Washington University Campus, Washington DC (Foggy Bottom)",
+            "identifier": "https://data.transportation.gov/api/views/6a6e-vfvi",
+            "issued": "2024-11-04",
+            "keyword": [
+                "aerial videography",
+                "automated vehicles",
+                "human-automated vehicle interactions",
+                "infrastructure-based videography",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "multi-modal trajectories",
+                "tgsim",
+                "third generation simulation",
+                "vehicle trajectory data"
+            ],
+            "landingPage": "https://data.transportation.gov/d/6a6e-vfvi",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-24",
+            "programCode": [
+                "021:042"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "spatial": "I-90/I94 in Chicago, IL; I-294 near Hinsdale, IL; I-395 in Washington DC; George Washington University Campus, Washington DC (Foggy Bottom)",
             "theme": [
                 "Automobiles"
-            ]
+            ],
+            "title": "Third Generation Simulation Data (TGSIM) I-90/I-94 Moving Trajectories"
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
-            "landingPage": "https://data.transportation.gov/d/6aay-dw5e",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/14juntvt/14juntvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "June 2014"
+                }
             ],
+            "identifier": "18.63",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -14406,72 +14421,42 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.63",
+            "landingPage": "https://data.transportation.gov/d/6aay-dw5e",
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
-            "title": "Monthly Traffic Volume Trends - June 2014",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/14juntvt/14juntvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "June 2014"
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
+            "title": "Monthly Traffic Volume Trends - June 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/6abt-uhgq",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-09-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
-            "keyword": [
-                "age by decade",
-                "transit vehicles",
-                "vehicle age"
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
-            "identifier": "https://data.transportation.gov/api/views/6abt-uhgq",
             "description": "This dataset details vehicle types and ages for each transit agency reporting to the NTD in the 2022 and 2023 report years. Non-dedicated fleets do not report Year of Manufacture and are thus excluded from the Age Distribution table.\n\nAgencies do not report Useful Life Benchmark for non-dedicated fleets or fleets for which the agency does not have capital replacement responsibility. These fleets are excluded from calculations of the percentage of vehicles meeting or exceeding their useful life.\n\nIn versions of the data tables from before 2014, you can find data on vehicles in the file called \"Age Distribution of Active Vehicle Inventory.\"\n\nIn years 2014-2021, you can find this data in the \"Vehicles\" data table on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.\n\nIf you have any other questions about this table, please contact the NTD Help Desk at NTDHelp@dot.gov.",
-            "title": "2022 - 2023 NTD Annual Data - Vehicles (Age Distribution)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14479,68 +14464,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6abt-uhgq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6abt-uhgq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6abt-uhgq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/6abt-uhgq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6abt-uhgq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6abt-uhgq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6abt-uhgq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6abt-uhgq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6abt-uhgq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/6abt-uhgq",
+            "issued": "2024-09-06",
+            "keyword": [
+                "age by decade",
+                "transit vehicles",
+                "vehicle age"
+            ],
+            "landingPage": "https://data.transportation.gov/d/6abt-uhgq",
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
+            "title": "2022 - 2023 NTD Annual Data - Vehicles (Age Distribution)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/6aiz-ybqx",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-06-05",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-19",
-            "keyword": [
-                "economics",
-                "finance",
-                "government expenditures",
-                "government funding",
-                "government revenue",
-                "government transportation expenditures",
-                "government transportation revenue",
-                "gtfs",
-                "transportation",
-                "transportation finance"
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
-            "identifier": "https://data.transportation.gov/api/views/6aiz-ybqx",
             "description": "Transportation Public Finance Statistics (TPFS) provides information on transportation-related revenue and expenditures for all levels of government, including federal, state, and local, and for all modes of transportation.",
-            "title": "Transportation Public Finance Statistics (TPFS)",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14548,42 +14523,100 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6aiz-ybqx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6aiz-ybqx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6aiz-ybqx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/6aiz-ybqx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6aiz-ybqx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6aiz-ybqx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6aiz-ybqx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6aiz-ybqx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6aiz-ybqx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works",
-            "theme": [
-                "Research and Statistics"
-            ],
-            "phone": "202-366-DATA(3282)"
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://nhtsa.gov/recalls",
-            "bureauCode": [
-                "021:18"
-            ],
-            "issued": "2023-02-28",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
+            "identifier": "https://data.transportation.gov/api/views/6aiz-ybqx",
+            "issued": "2024-06-05",
+            "keyword": [
+                "economics",
+                "finance",
+                "government expenditures",
+                "government funding",
+                "government revenue",
+                "government transportation expenditures",
+                "government transportation revenue",
+                "gtfs",
+                "transportation",
+                "transportation finance"
+            ],
+            "landingPage": "https://data.transportation.gov/d/6aiz-ybqx",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-12-19",
+            "phone": "202-366-DATA(3282)",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "theme": [
+                "Research and Statistics"
+            ],
+            "title": "Transportation Public Finance Statistics (TPFS)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "021:18"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "About the Data:\nThe dataset includes recall information related to specific NHTSA campaigns. Users can filter based on characteristics like manufacturer and component. The dataset can also be filtered by recall type: tires, vehicles, car seats, and equipment. The earliest campaign data is from 1966. The dataset displays the completion rate from the latest Recall Quarterly Report or Annual Report data from Year 2015 Quarter 1 (2015-1) onward.\n\nData Reporting Requirement:\nManufacturers who determine that a product or piece of original equipment either contains a safety defect or is not in compliance with Federal safety standards are required to notify NHTSA within 5 business days. NHTSA requires that manufacturers file a Defect and Noncompliance Report in compliance with Federal Regulation 49 (the National Traffic and Motor Safety Act) Part 573, which identifies the requirements for safety recalls. This information is stored in the NHTSA database referenced above.\n\nNotes:\nThe default visualization depicted here represents only the top 12 manufacturers for the current calendar year. Please use the Filters for specific data requests. For a complete historical perspective, please visit:\nhttps://www.nhtsa.gov/sites/nhtsa.gov/files/2023-03/2022-Recalls-Annual-Report_030223-tag.pdf.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/api/views/6axg-epim/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.transportation.gov/api/views/6axg-epim/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.transportation.gov/api/views/6axg-epim/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.transportation.gov/api/views/6axg-epim/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.transportation.gov/api/views/6axg-epim/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.transportation.gov/api/views/6axg-epim/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.transportation.gov/api/views/6axg-epim/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/6axg-epim",
+            "issued": "2023-02-28",
             "keyword": [
                 "air bag",
                 "air bags",
@@ -14611,82 +14644,37 @@
                 "vin",
                 "vin search"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/6axg-epim",
-            "description": "About the Data:\nThe dataset includes recall information related to specific NHTSA campaigns. Users can filter based on characteristics like manufacturer and component. The dataset can also be filtered by recall type: tires, vehicles, car seats, and equipment. The earliest campaign data is from 1966. The dataset displays the completion rate from the latest Recall Quarterly Report or Annual Report data from Year 2015 Quarter 1 (2015-1) onward.\n\nData Reporting Requirement:\nManufacturers who determine that a product or piece of original equipment either contains a safety defect or is not in compliance with Federal safety standards are required to notify NHTSA within 5 business days. NHTSA requires that manufacturers file a Defect and Noncompliance Report in compliance with Federal Regulation 49 (the National Traffic and Motor Safety Act) Part 573, which identifies the requirements for safety recalls. This information is stored in the NHTSA database referenced above.\n\nNotes:\nThe default visualization depicted here represents only the top 12 manufacturers for the current calendar year. Please use the Filters for specific data requests. For a complete historical perspective, please visit:\nhttps://www.nhtsa.gov/sites/nhtsa.gov/files/2023-03/2022-Recalls-Annual-Report_030223-tag.pdf.",
-            "title": "Recalls Data",
+            "landingPage": "https://nhtsa.gov/recalls",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-02-01",
             "programCode": [
                 "021:031"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/api/views/6axg-epim/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6axg-epim/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.transportation.gov/api/views/6axg-epim/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/6axg-epim/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.transportation.gov/api/views/6axg-epim/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6axg-epim/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.transportation.gov/api/views/6axg-epim/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Recalls Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/6bch-d3uv",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2021-01-05",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/6bch-d3uv",
+            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMSS",
             "description": "State DOTs provide the location limits of highway sections to be used to represent statewide aggregations based on a statistically valid Sample Panel.\nThe Mid-America contains data for the following States: Illinois, Indiana, Iowa, Kansas, Michigan, Minnesota, Missouri, Nebraska, North Dakota, Oklahoma, South Dakota, Texas, and Wisconsin.",
-            "title": "Roadway Sections Mid-America 2018",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14694,112 +14682,96 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6bch-d3uv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6bch-d3uv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6bch-d3uv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/6bch-d3uv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6bch-d3uv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6bch-d3uv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6bch-d3uv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6bch-d3uv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6bch-d3uv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "USA",
-            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMSS",
+            "identifier": "https://data.transportation.gov/api/views/6bch-d3uv",
+            "issued": "2021-01-05",
+            "landingPage": "https://data.transportation.gov/d/6bch-d3uv",
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
+            "spatial": "USA",
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Roadway Sections Mid-America 2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.bts.gov/stories/s/6bdc-i7mh",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2021-01-11",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
-            "keyword": [
-                "highway trust fund",
-                "transit trust fund"
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
-            "identifier": "https://data.transportation.gov/api/views/6bdc-i7mh",
             "description": "Data and visualizations showing highway and transit trust fund balance, receipts, and outlays.",
-            "title": "Transportation Economic Trends: Government Transportation Revenue - Trust Funds",
+            "identifier": "https://data.transportation.gov/api/views/6bdc-i7mh",
+            "issued": "2021-01-11",
+            "keyword": [
+                "highway trust fund",
+                "transit trust fund"
+            ],
+            "landingPage": "https://data.bts.gov/stories/s/6bdc-i7mh",
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
+            "title": "Transportation Economic Trends: Government Transportation Revenue - Trust Funds"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/6bhp-rgk2",
+            "accrualPeriodicity": "R/PT60S",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2012-04-16",
-            "@type": "dcat:Dataset",
-            "temporal": "2011-09-15/2011-11-15",
-            "modified": "2012-04-16",
-            "keyword": [
-                "flow data",
-                "freeway",
-                "i-205",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "loop detector",
-                "occupancy data",
-                "oregon",
-                "portland",
-                "portland oregon test data set",
-                "portland state university (psu)",
-                "sensor data",
-                "speed data",
-                "usdot data capture and management program (dcm)"
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
-            "identifier": "https://data.transportation.gov/api/views/6bhp-rgk2",
+            "dataQuality": true,
             "description": "This set of data files was acquired under USDOT FHWA cooperative agreement DTFH61-11-H-00025 as one of the four test data sets acquired by the USDOT Data Capture and Management program.The freeway data consists of two months of data (Sept 15 2011 through Nov 15 2011) from dual-loop detectors deployed in the main line and on-ramps of a Portland-area freeway.  The section of I-205 NB covered by this test data set is 10.09 miles long and the section of I-205 SB covered by this test data set is 12.01 miles long   The data includes: flow, occupancy, and speed.",
-            "title": "Portland, Oregon Test Data Set Freeway Loop Detector Data",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14807,70 +14779,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6bhp-rgk2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6bhp-rgk2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6bhp-rgk2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/6bhp-rgk2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6bhp-rgk2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6bhp-rgk2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6bhp-rgk2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6bhp-rgk2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6bhp-rgk2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Portland, Oregon",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/6bhp-rgk2",
+            "issued": "2012-04-16",
+            "keyword": [
+                "flow data",
+                "freeway",
+                "i-205",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "loop detector",
+                "occupancy data",
+                "oregon",
+                "portland",
+                "portland oregon test data set",
+                "portland state university (psu)",
+                "sensor data",
+                "speed data",
+                "usdot data capture and management program (dcm)"
+            ],
+            "landingPage": "https://data.transportation.gov/d/6bhp-rgk2",
+            "language": [
+                "English"
+            ],
             "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "R/PT60S",
+            "modified": "2012-04-16",
+            "programCode": [
+                "021:013"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "USDOT"
+            },
+            "spatial": "Portland, Oregon",
+            "temporal": "2011-09-15/2011-11-15",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Portland, Oregon Test Data Set Freeway Loop Detector Data"
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
-            "identifier": "https://data.transportation.gov/api/views/6brt-ucwr",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 1980",
-            "title": "Historic HPMS Data (Sample) - 1987",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14878,64 +14858,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6brt-ucwr/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6brt-ucwr/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6brt-ucwr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/6brt-ucwr/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6brt-ucwr/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6brt-ucwr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6brt-ucwr/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6brt-ucwr/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6brt-ucwr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/6brt-ucwr",
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
+            "title": "Historic HPMS Data (Sample) - 1987"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/6cfa-ipzd",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2023-06-19",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
-            "keyword": [
-                "bikeshare",
-                "docked bikeshare"
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
-            "identifier": "https://data.transportation.gov/api/views/6cfa-ipzd",
             "description": "Historic data updated on 07/14/2023. Q4 of 2023 and data for all years on systems allowing parking outside of a docking station updated on 06/04/2024.\r\n\r\nBikeshare ridership by system for bikeshare systems with docking stations. Data summarized for each system by: (1) month, (2) day, and (3) hour. Data starting in January 2019. In monthly summary, months are rearranged to include the same number of days of the week across years (see below). \r\n\r\nRidership data not available for all docked bikeshare systems. Only docked bikeshare systems with ridership data shown. Some systems included in the data permit users to leave a bicycle outside of a docking station; these trips are indicated by the trip type. Trips defined as rides from point A to B. If user makes trip from B to A on same day, counted as a second trip. Trips labeled as round trips in Metro Bike Share and Indego trip files counted as 2 trips. Trips with no trip time are not counted. For trips starting and ending at a docking station or on systems where only docked trips are permitted, trips with no start station identifier and/or end station id are not counted in totals. Trips shorter than 1 minute or greater than 2 hours excluded. In monthly summary, days aligned to include the same days of weeks across years. \r\n\r\nDays included in each month  can be found in the attachments (https://data.bts.gov/api/views/6cfa-ipzd/files/36fde1b8-57c3-4d31-b9dc-bbc896ba346e?download=true&filename=days_included_in_docked_bikeshare_monthly_summaries.xlsx)\r\n\r\nData visualizations available at: https://data.bts.gov/stories/s/Summary-of-Docked-Bikeshare-Trips-by-System-and-Ot/7fgy-2zkf/",
-            "title": "Docked Bikeshare Ridership",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14943,48 +14927,80 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6cfa-ipzd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6cfa-ipzd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6cfa-ipzd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/6cfa-ipzd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6cfa-ipzd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6cfa-ipzd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6cfa-ipzd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6cfa-ipzd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6cfa-ipzd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/6cfa-ipzd",
+            "issued": "2023-06-19",
+            "keyword": [
+                "bikeshare",
+                "docked bikeshare"
+            ],
+            "landingPage": "https://data.transportation.gov/d/6cfa-ipzd",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2025-01-13",
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
+            "title": "Docked Bikeshare Ridership"
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
-            "landingPage": "https://data.transportation.gov/d/6cx4-8fs4",
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
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/tenyr2a.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Ten Year Accident/Incident Overview by Railroad/Region/State/County"
+                }
             ],
+            "identifier": "214.7",
+            "isPartOf": "DOT-214",
+            "issued": "2010-09-29",
             "keyword": [
                 "accident",
                 "casualty",
@@ -14997,61 +15013,61 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "214.7",
+            "landingPage": "https://data.transportation.gov/d/6cx4-8fs4",
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
-            "title": "Highway Rail Accidents - Ten Year Accident/Incident Overview by Railroad/Region/State/County",
-            "isPartOf": "DOT-214",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/tenyr2a.aspx",
-                    "mediaType": "text/csv",
-                    "title": "Ten Year Accident/Incident Overview by Railroad/Region/State/County"
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
+            "title": "Highway Rail Accidents - Ten Year Accident/Incident Overview by Railroad/Region/State/County"
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
-            "landingPage": "https://data.transportation.gov/d/6dmg-4sy3",
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
+                    "description": "This access point provides access to the LTPP InfoPave tools features including MEPDG inputs for local calibration, rigid pavement design, WIM cost analysis, payment loading user guide, pavement performance forecast, LTPP dynamic modulus prediction, LTPPBind, LTPP distress identification manual, and LTPP InfoPave mobile.",
+                    "downloadURL": "https://infopave.fhwa.dot.gov/%3FGoto=Tools",
+                    "mediaType": "application/atom+xml",
+                    "title": "Tools"
+                }
             ],
+            "identifier": "679.9",
+            "isPartOf": "DOT-679",
+            "issued": "1993-07-01",
             "keyword": [
                 "asphalt concrete",
                 "continuously reinforced concrete pavement",
@@ -15068,58 +15084,53 @@
                 "texture",
                 "traffic loading"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "679.9",
+            "landingPage": "https://data.transportation.gov/d/6dmg-4sy3",
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
-            "title": "Long-Term Pavement Performance (LTPP) - Tools",
-            "isPartOf": "DOT-679",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/research/tfhrc/programs/infrastructure/pavements/ltpp/",
-            "programCode": [
-                "021:009"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/atom+xml",
-                    "downloadURL": "https://infopave.fhwa.dot.gov/%3FGoto=Tools",
-                    "description": "This access point provides access to the LTPP InfoPave tools features including MEPDG inputs for local calibration, rigid pavement design, WIM cost analysis, payment loading user guide, pavement performance forecast, LTPP dynamic modulus prediction, LTPPBind, LTPP distress identification manual, and LTPP InfoPave mobile.",
-                    "@type": "dcat:Distribution",
-                    "title": "Tools"
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
+            "title": "Long-Term Pavement Performance (LTPP) - Tools"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.21949/1503768",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2014-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2016-12-15",
-            "references": [
-                "https://rosap.ntl.bts.gov/view/dot/3611"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Transportation Library Data Curator",
+                "hasEmail": "mailto:ntldatacurator@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The objective of this project was to develop system designs for programs to monitor travel time reliability and to prepare a guidebook that practitioners and others can use to design, build, operate, and maintain such systems. Generally, such travel time reliability monitoring systems will be built on top of existing traffic monitoring systems. The focus of this project was on travel time reliability. The data from the monitoring systems developed in this project \u2013 from both public and private sources \u2013included, wherever cost-effective, information on the seven sources of non-recurring congestion. This data was used to construct performance measures or to perform various types of analyses useful for operations management as well as performance measurement, planning, and programming.  The datasets in this zip file, which is 338.39 MB in size, are in support of SHRP 2 reliability project L38A, \"Pilot testing of SHRP 2 reliability data and analytical products: Southern California.\" This report can be accessed via the following URL: https://rosap.ntl.bts.gov/view/dot/3611  This zip file contains 11 files, including 8 Microsoft Excel worksheets (XLSX), 2 Comma Separated Values (CSV), and 1 Zip Package (PKZIP) files. The Microsoft Excel worksheets can be opened using the 2010 and 2016 versions of Microsoft Word, the CSV files can be opened using most text editors, and the PKZIP files can be opened using most zip file extraction programs.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The objective of this project was to develop system designs for programs to monitor travel time reliability and to prepare a guidebook that practitioners and others can use to design, build, operate, and maintain such systems. Generally, such travel time reliability monitoring systems will be built on top of existing traffic monitoring systems. The focus of this project was on travel time reliability. The data from the monitoring systems developed in this project \u2013 from both public and private sources \u2013included, wherever cost-effective, information on the seven sources of non-recurring congestion. This data was used to construct performance measures or to perform various types of analyses useful for operations management as well as performance measurement, planning, and programming.  The datasets in this zip file, which is 338.39 MB in size, are in support of SHRP 2 reliability project L38A, \"Pilot testing of SHRP 2 reliability data and analytical products: Southern California.\" This report can be accessed via the following URL: https://rosap.ntl.bts.gov/view/dot/3611  This zip file contains 11 files, including 8 Microsoft Excel worksheets (XLSX), 2 Comma Separated Values (CSV), and 1 Zip Package (PKZIP) files. The Microsoft Excel worksheets can be opened using the 2010 and 2016 versions of Microsoft Word, the CSV files can be opened using most text editors, and the PKZIP files can be opened using most zip file extraction programs.",
+                    "downloadURL": "https://doi.org/10.21949/1503768",
+                    "mediaType": "application/zip",
+                    "title": "Pilot Testing of SHRP 2 Reliability Data and Analytical Products: Southern California [supporting datasets]"
+                }
             ],
+            "identifier": "https://data.transportation.gov/api/views/6ex2-pnmk",
+            "issued": "2014-01-01",
             "keyword": [
                 "business practices",
                 "data analysis",
@@ -15133,64 +15144,37 @@
                 "travel time",
                 "travel time reliability"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Transportation Library Data Curator",
-                "hasEmail": "mailto:ntldatacurator@dot.gov"
-            },
+            "landingPage": "https://doi.org/10.21949/1503768",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2016-12-15",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/6ex2-pnmk",
-            "description": "The objective of this project was to develop system designs for programs to monitor travel time reliability and to prepare a guidebook that practitioners and others can use to design, build, operate, and maintain such systems. Generally, such travel time reliability monitoring systems will be built on top of existing traffic monitoring systems. The focus of this project was on travel time reliability. The data from the monitoring systems developed in this project \u2013 from both public and private sources \u2013included, wherever cost-effective, information on the seven sources of non-recurring congestion. This data was used to construct performance measures or to perform various types of analyses useful for operations management as well as performance measurement, planning, and programming.  The datasets in this zip file, which is 338.39 MB in size, are in support of SHRP 2 reliability project L38A, \"Pilot testing of SHRP 2 reliability data and analytical products: Southern California.\" This report can be accessed via the following URL: https://rosap.ntl.bts.gov/view/dot/3611  This zip file contains 11 files, including 8 Microsoft Excel worksheets (XLSX), 2 Comma Separated Values (CSV), and 1 Zip Package (PKZIP) files. The Microsoft Excel worksheets can be opened using the 2010 and 2016 versions of Microsoft Word, the CSV files can be opened using most text editors, and the PKZIP files can be opened using most zip file extraction programs.",
-            "title": "Pilot Testing of SHRP 2 Reliability Data and Analytical Products: Southern California [supporting datasets]",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://doi.org/10.21949/1503768",
-                    "description": "The objective of this project was to develop system designs for programs to monitor travel time reliability and to prepare a guidebook that practitioners and others can use to design, build, operate, and maintain such systems. Generally, such travel time reliability monitoring systems will be built on top of existing traffic monitoring systems. The focus of this project was on travel time reliability. The data from the monitoring systems developed in this project \u2013 from both public and private sources \u2013included, wherever cost-effective, information on the seven sources of non-recurring congestion. This data was used to construct performance measures or to perform various types of analyses useful for operations management as well as performance measurement, planning, and programming.  The datasets in this zip file, which is 338.39 MB in size, are in support of SHRP 2 reliability project L38A, \"Pilot testing of SHRP 2 reliability data and analytical products: Southern California.\" This report can be accessed via the following URL: https://rosap.ntl.bts.gov/view/dot/3611  This zip file contains 11 files, including 8 Microsoft Excel worksheets (XLSX), 2 Comma Separated Values (CSV), and 1 Zip Package (PKZIP) files. The Microsoft Excel worksheets can be opened using the 2010 and 2016 versions of Microsoft Word, the CSV files can be opened using most text editors, and the PKZIP files can be opened using most zip file extraction programs.",
-                    "@type": "dcat:Distribution",
-                    "title": "Pilot Testing of SHRP 2 Reliability Data and Analytical Products: Southern California [supporting datasets]"
-                }
+            "references": [
+                "https://rosap.ntl.bts.gov/view/dot/3611"
             ],
             "spatial": "United States, California, Southern California",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "language": [
-                "en-US"
-            ]
+            "title": "Pilot Testing of SHRP 2 Reliability Data and Analytical Products: Southern California [supporting datasets]"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/6eyk-hxee",
             "bureauCode": [
                 "021:17"
             ],
-            "issued": "2024-02-02",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
-            "keyword": [
-                "motor carrier",
-                "operating authority",
-                "broker",
-                "insurance"
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
-            "identifier": "https://data.transportation.gov/api/views/6eyk-hxee",
             "description": "*Dataset*  Records for all carriers/brokers/freight forwarders with active, inactive, or pending authorities (common or contract). It includes the DOT number and MC/FF/MX number for the carrier/broker/freight forwarder, along with company census data (e.g., types of authority, address, types of insurance on file, and amounts of insurance on file). See dataset attachment \"FMCSA Dataset Description and Data Definitions - Select Datasets\" for more information.",
-            "title": "Carrier - All With History",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15198,49 +15182,80 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6eyk-hxee/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6eyk-hxee/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6eyk-hxee/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/6eyk-hxee/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6eyk-hxee/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6eyk-hxee/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6eyk-hxee/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6eyk-hxee/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6eyk-hxee/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/6eyk-hxee",
+            "issued": "2024-02-02",
+            "keyword": [
+                "motor carrier",
+                "operating authority",
+                "broker",
+                "insurance"
+            ],
+            "landingPage": "https://data.transportation.gov/d/6eyk-hxee",
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
+            "title": "Carrier - All With History"
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
-            "landingPage": "https://data.transportation.gov/d/6fg7-kywe",
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
+            "identifier": "115.1",
+            "isPartOf": "DOT-115",
+            "issued": "2005-08-09",
             "keyword": [
                 "compliance review",
                 "compliance review effectiveness model",
@@ -15250,87 +15265,42 @@
                 "program effectiveness",
                 "roadside inspection traffic enforcement"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "115.1",
+            "landingPage": "https://data.transportation.gov/d/6fg7-kywe",
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
-            "title": "A&I - Program Effectiveness - Compliance Review Effectiveness Model",
-            "isPartOf": "DOT-115",
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
-            "categoryDesignation": "Research",
-            "analysisUnit": "FMCSA program",
-            "phone": "202-366-2959",
-            "language": [
-                "en-US"
-            ]
+            "title": "A&I - Program Effectiveness - Compliance Review Effectiveness Model"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/6g4k-h3cv",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2024-09-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
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
                 "fn": "Elina Zlotchenko",
                 "hasEmail": "mailto:elina.zlotchenko@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/6g4k-h3cv",
             "description": "WFCW-3 FCW Slow Moving Vehicle Rep 1",
-            "title": "LTE-V2X Wyoming Connected Vehicle Pilot test ID WFCW-3 Rep 1",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15338,44 +15308,92 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6g4k-h3cv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6g4k-h3cv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6g4k-h3cv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/6g4k-h3cv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6g4k-h3cv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6g4k-h3cv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6g4k-h3cv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6g4k-h3cv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6g4k-h3cv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Wyoming",
+            "identifier": "https://data.transportation.gov/api/views/6g4k-h3cv",
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
+            "landingPage": "https://data.transportation.gov/d/6g4k-h3cv",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-20",
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
+            "title": "LTE-V2X Wyoming Connected Vehicle Pilot test ID WFCW-3 Rep 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/6g52-2faw",
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
+                    "description": "2013 Kentucky HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/kentucky2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Kentucky"
+                }
+            ],
+            "identifier": "678.121",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -15389,82 +15407,45 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.121",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Kentucky",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/6g52-2faw",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/kentucky2013.zip",
-                    "description": "2013 Kentucky HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Kentucky"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Kentucky"
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
-            "landingPage": "https://data.transportation.gov/d/6giu-i87m",
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
-            "identifier": "692.26",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - Federal Lands",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "primaryITInvestmentUII": "021-845083703",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15473,57 +15454,56 @@
                     "title": "Federal Lands"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.26",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/6giu-i87m",
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
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - Federal Lands"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "https://safer.fmcsa.dot.gov/mcs150t/pkg_ct_public.prc_ct_public_search",
+            "agencyProgramURL": "https://safer.fmcsa.dot.gov/mcs150t/pkg_ct_public.prc_ct_public_search",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/6har-i44u",
-            "issued": "2010-01-26",
-            "temporal": "R/1974-06-01/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-29",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://safer.fmcsa.dot.gov/"
-            ],
-            "keyword": [
-                "cargo tank",
-                "safer",
-                "tank registration.",
-                "usdot number"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO",
                 "hasEmail": "mailto:fmcsa.cdo@dot.gov"
             },
-            "identifier": "125.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": true,
             "description": "Searchable list of cargo tank manufacturers and repair facilities.",
-            "title": "SAFER - Cargo Tank Facility - SAFER - Cargo Tank Facility",
-            "isPartOf": "DOT-125",
-            "agencyProgramURL": "https://safer.fmcsa.dot.gov/mcs150t/pkg_ct_public.prc_ct_public_search",
-            "programCode": [
-                "021:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15532,38 +15512,48 @@
                     "title": "SAFER - Cargo Tank Facility"
                 }
             ],
-            "spatial": "State, National",
-            "dataQuality": true,
+            "identifier": "125.2",
+            "isPartOf": "DOT-125",
+            "issued": "2010-01-26",
+            "keyword": [
+                "cargo tank",
+                "safer",
+                "tank registration.",
+                "usdot number"
+            ],
+            "landingPage": "https://data.transportation.gov/d/6har-i44u",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "https://safer.fmcsa.dot.gov/mcs150t/pkg_ct_public.prc_ct_public_search",
+            "modified": "2024-07-29",
+            "phone": "202-493-0215",
+            "programCode": [
+                "021:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "references": [
+                "http://safer.fmcsa.dot.gov/"
+            ],
+            "spatial": "State, National",
+            "temporal": "R/1974-06-01/P1D",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "categoryDesignation": "Research",
-            "phone": "202-493-0215",
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFER - Cargo Tank Facility - SAFER - Cargo Tank Facility"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/6hbz-etpg",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/6hbz-etpg",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "College & Universities",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15571,68 +15561,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6hbz-etpg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6hbz-etpg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6hbz-etpg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/6hbz-etpg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6hbz-etpg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6hbz-etpg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6hbz-etpg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6hbz-etpg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6hbz-etpg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/6hbz-etpg",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/6hbz-etpg",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "College & Universities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "https://www.fmcsa.dot.gov/guidance",
+            "agencyProgramURL": "https://www.fmcsa.dot.gov/guidance",
+            "analysisUnit": "Regulations",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/6ht8-ha4e",
-            "issued": "2011-01-18",
-            "temporal": "2007-01-01/2011-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-29",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "https://www.fmcsa.dot.gov/guidance"
-            ],
-            "keyword": [
-                "data.gov",
-                "law",
-                "significant guidance",
-                "transportation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO",
                 "hasEmail": "mailto:fmcsa.cdo@dot.gov"
             },
-            "identifier": "305.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": true,
             "description": "A list of Significant Guidance documents, which include guidance document disseminated to regulated entities or the general public that may reasonably be anticipated to lead to an annual effect on the economy of $100 million or more or adversely affect in a material way the economy, a sector of the economy, productivity, competition, jobs, the environment, public health or safety, or State, local, or tribal governments or communities; create a serious inconsistency or otherwise interfere with an action taken or planned by another agency; materially alter the budgetary impact of entitlements, grants, user fees, or loan programs or the rights and obligations of recipients thereof; or raise novel legal or policy issues arising out of legal mandates, the President's priorities, or the principles set forth in Executive Order 12866, as further amended.",
-            "title": "Significant Guidance Issued by the Federal Motor Carrier Safety Administration -",
-            "isPartOf": "DOT-305",
-            "agencyProgramURL": "https://www.fmcsa.dot.gov/guidance",
-            "programCode": [
-                "021:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15640,31 +15621,68 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "305.1",
+            "isPartOf": "DOT-305",
+            "issued": "2011-01-18",
+            "keyword": [
+                "data.gov",
+                "law",
+                "significant guidance",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/6ht8-ha4e",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "https://www.fmcsa.dot.gov/guidance",
+            "modified": "2024-07-29",
+            "phone": "202-493-0215",
+            "programCode": [
+                "021:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "references": [
+                "https://www.fmcsa.dot.gov/guidance"
+            ],
+            "temporal": "2007-01-01/2011-01-18",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "analysisUnit": "Regulations",
-            "categoryDesignation": "Research",
-            "phone": "202-493-0215",
-            "language": [
-                "en-US"
-            ]
+            "title": "Significant Guidance Issued by the Federal Motor Carrier Safety Administration -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/6idq-i3bc",
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
+                    "description": "2013 Michigan HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/michigan2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Michigan"
+                }
+            ],
+            "identifier": "678.126",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -15678,102 +15696,66 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.126",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Michigan",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/6idq-i3bc",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/michigan2013.zip",
-                    "description": "2013 Michigan HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Michigan"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Michigan"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/6it8-mz4h",
-            "issued": "2025-01-02",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-02",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:answers@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/6it8-mz4h",
             "description": "The Great Lakes St. Lawrence Seaway\u2019s navigation season generally begins in late March and closes in late December. Opening and closing dates vary from year to year.",
-            "title": "Great Lakes St. Lawrence Seaway - U.S. Sector Reliability Rate",
+            "identifier": "https://data.transportation.gov/api/views/6it8-mz4h",
+            "issued": "2025-01-02",
+            "landingPage": "https://data.transportation.gov/d/6it8-mz4h",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-02",
             "programCode": [
                 "021:053"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Great Lakes St. Lawrence Seaway - U.S. Sector Reliability Rate"
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
-            "identifier": "https://data.transportation.gov/api/views/6itn-mw5q",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 1983",
-            "title": "Historic HPMS Data (Universe) - 1983",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15781,45 +15763,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6itn-mw5q/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6itn-mw5q/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6itn-mw5q/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/6itn-mw5q/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6itn-mw5q/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6itn-mw5q/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6itn-mw5q/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6itn-mw5q/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6itn-mw5q/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/6itn-mw5q",
+            "issued": "2022-07-06",
+            "keyword": [
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
+            "title": "Historic HPMS Data (Universe) - 1983"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/6ix2-c8dn",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Transportation Analysis",
+                "hasEmail": "mailto:long.nguyen@dot.gov"
+            },
+            "description": "Freight Facts and Figures - Freight Transportation and the Economy",
+            "identifier": "https://data.transportation.gov/api/views/6ix2-c8dn",
             "issued": "2019-09-24",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-02",
             "keyword": [
                 "bts",
                 "bureau of transportation statistics",
@@ -15831,39 +15835,52 @@
                 "freight facts & figures",
                 "freight transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Transportation Analysis",
-                "hasEmail": "mailto:long.nguyen@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/6ix2-c8dn",
+            "modified": "2024-10-02",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statisitics"
             },
-            "identifier": "https://data.transportation.gov/api/views/6ix2-c8dn",
-            "description": "Freight Facts and Figures - Freight Transportation and the Economy",
-            "title": "Freight Transportation & the Economy",
-            "programCode": [
-                "021:053"
-            ],
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Freight Transportation & the Economy"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
+            "agencyDataSeriesURL": "http://www.dot.gov/data.json",
+            "agencyProgramURL": "https://www.transportation.gov/data",
+            "analysisUnit": "Dataset",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/6j26-pr32",
-            "issued": "2013-11-27",
-            "temporal": "R/2013-11-30/P3M",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Metadata Registry",
-            "modified": "2024-11-14",
-            "references": [
-                "https://project-open-data.cio.gov"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DOT Socrata",
+                "hasEmail": "mailto:Socrata@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://project-open-data.cio.gov/v1.1/schema/",
+            "description": "United States Department of Transportation Public Data Listing. The file is formatted to comply with project open data common core metadata requirements (http://project-open-data.github.io/schema/) and conforms to schema version 1.1",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "This is the DOT Public Data Listing that gets harvested by data.gov",
+                    "downloadURL": "https://www.transportation.gov/data-nonspatial-harvest.json",
+                    "mediaType": "application/json",
+                    "title": "Public Data Listing - harvested to data.gov"
+                }
             ],
+            "identifier": "336.2",
+            "isPartOf": "DOT-336",
+            "issued": "2013-11-27",
             "keyword": [
                 "api",
                 "data",
@@ -15873,60 +15890,61 @@
                 "public data listing",
                 "raw data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DOT Socrata",
-                "hasEmail": "mailto:Socrata@dot.gov"
-            },
-            "identifier": "336.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
-            "description": "United States Department of Transportation Public Data Listing. The file is formatted to comply with project open data common core metadata requirements (http://project-open-data.github.io/schema/) and conforms to schema version 1.1",
-            "title": "Department of Transportation Public Data Listing - Public Data Listing - harvested to data.gov",
-            "isPartOf": "DOT-336",
-            "agencyProgramURL": "https://www.transportation.gov/data",
+            "landingPage": "https://data.transportation.gov/d/6j26-pr32",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-14",
+            "phone": "202-366-4308",
             "primaryITInvestmentUII": "021-748752384",
             "programCode": [
                 "021:058"
             ],
-            "distribution": [
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.transportation.gov/data-nonspatial-harvest.json",
-                    "description": "This is the DOT Public Data Listing that gets harvested by data.gov",
-                    "@type": "dcat:Distribution",
-                    "title": "Public Data Listing - harvested to data.gov"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "references": [
+                "https://project-open-data.cio.gov"
             ],
             "spatial": "N/A",
-            "describedBy": "https://project-open-data.cio.gov/v1.1/schema/",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.dot.gov/data.json",
+            "temporal": "R/2013-11-30/P3M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P3M",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Dataset",
-            "phone": "202-366-4308",
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Transportation Public Data Listing - Public Data Listing - harvested to data.gov"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/6jw7-jg6e",
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
+                    "description": "2012 Texas HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/texas2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Texas"
+                }
+            ],
+            "identifier": "678.97",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -15940,73 +15958,40 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.97",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Texas",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/6jw7-jg6e",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/texas2012.zip",
-                    "description": "2012 Texas HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Texas"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Texas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/6jw9-gfkw",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2020-11-02",
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
-            "identifier": "https://data.transportation.gov/api/views/6jw9-gfkw",
+            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
             "description": "State DOTs will provide Local and Rural Minor Collector Mileage summarized by county, ownership, and Paved and Unpaved. This data is provided in a direct input by the State DOTs.",
-            "title": "County Summary 2019",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16014,123 +15999,115 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6jw9-gfkw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6jw9-gfkw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6jw9-gfkw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/6jw9-gfkw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6jw9-gfkw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6jw9-gfkw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6jw9-gfkw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6jw9-gfkw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6jw9-gfkw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "USA",
-            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
+            "identifier": "https://data.transportation.gov/api/views/6jw9-gfkw",
+            "issued": "2020-11-02",
+            "landingPage": "https://data.transportation.gov/d/6jw9-gfkw",
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
-            ]
+            ],
+            "title": "County Summary 2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/6k7a-rwnz",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2025-01-15",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
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
-            "identifier": "https://data.transportation.gov/api/views/6k7a-rwnz",
             "description": "Other transit modes include demand response, demand response-taxi, vanpool, and ferryboat. The Federal Highway Administration estimates monthly transit ridership, released as part of the National Transit Database. Ridership estimates have been adjusted to account for changes in data collection over time. Starting in January 2012, data for Small System Waiver agencies that do not have a mode are reported under motor bus. Data reported under hybrid rail are reported under their classifications prior to January 2012.",
-            "title": "Transit Ridership - Other Transit Modes",
+            "identifier": "https://data.transportation.gov/api/views/6k7a-rwnz",
+            "issued": "2025-01-15",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/6k7a-rwnz",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-15",
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
+            "title": "Transit Ridership - Other Transit Modes"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/6kur-q9xk",
-            "issued": "2021-07-28",
             "@type": "dcat:Dataset",
-            "modified": "2024-07-25",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Chambers",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/6kur-q9xk",
+            "issued": "2021-07-28",
+            "landingPage": "https://data.transportation.gov/d/6kur-q9xk",
+            "modified": "2024-07-25",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Port Data Catalog"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://wzdx.massdot-swzm.com/index.html",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2021-06-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
-            "keyword": [
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "massachusetts",
-                "massachusetts department of transportation (massdot)",
-                "smart work zones manager (swzm)",
-                "smart work zones (swz)",
-                "work zone data exchange (wzdx)",
-                "work zones"
-            ],
             "conformsTo": "https://github.com/usdot-jpo-ode/jpo-wzdx/releases/tag/v3.1",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kate Hartman",
                 "hasEmail": "mailto:kate.hartman@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "US Department of Transportation"
-            },
-            "identifier": "https://data.transportation.gov/api/views/6m7q-g56h",
             "description": "This dataset provides information on work zones in the state of Massachusetts in a tabular format and is updated daily based on the <a href=\"https://wzdx.massdot-swzm.com/massdot_wzdx_v3.1.geojson\" target=\"_blank\" rel=\"noopener\">live MassDOT Work Zone Data Exchange (WZDx) Feed</a>.\n\nA continuously updating archive of the MassDOT WZDx feed data can be found at <a href=\"http://usdot-its-workzone-raw-publicdata.s3.amazonaws.com/index.html\" target=\"_blank\" rel=\"noopener\">ITS WorkZone Raw Data Sandbox</a> and the <a href=\"http://usdot-its-workzone-publicdata.s3.amazonaws.com/index.html\" target=\"_blank\" rel=\"noopener\">ITS WorkZone Semi-Processed Data Sandbox</a>.  This <a href=\"https://wzdx.massdot-swzm.com/massdot_wzdx_v3.1.geojson\" target=\"_blank\" rel=\"noopener\">live feed</a> is currently compliant with the <a href=\"https://github.com/usdot-jpo-ode/jpo-wzdx/tree/v3.1\" target=\"_blank\" rel=\"noopener\">WZDx Specification v3.1</a>.",
-            "title": "Massachusetts Department of Transportation (MassDOT) Work Zone Data Exchange (WZDx) v3.1 Feed Sample",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16138,52 +16115,89 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6m7q-g56h/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6m7q-g56h/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6m7q-g56h/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/6m7q-g56h/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6m7q-g56h/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6m7q-g56h/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6m7q-g56h/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6m7q-g56h/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6m7q-g56h/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Massachusetts",
+            "identifier": "https://data.transportation.gov/api/views/6m7q-g56h",
+            "issued": "2021-06-30",
+            "keyword": [
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "massachusetts",
+                "massachusetts department of transportation (massdot)",
+                "smart work zones manager (swzm)",
+                "smart work zones (swz)",
+                "work zone data exchange (wzdx)",
+                "work zones"
+            ],
+            "landingPage": "https://wzdx.massdot-swzm.com/index.html",
             "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
+            "modified": "2024-11-07",
+            "programCode": [
+                "021:013"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
+            "spatial": "Massachusetts",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "Massachusetts Department of Transportation (MassDOT) Work Zone Data Exchange (WZDx) v3.1 Feed Sample"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyProgramURL": "http://www.nhtsa.gov/fuel-economy",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/6m9s-7skc",
-            "issued": "2015-12-16",
-            "temporal": "2015/2016",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative - Regulatory",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-01",
-            "references": [
-                "http://www.nhtsa.gov/fuel-economy"
-            ],
-            "keyword": [
-                "amfa",
-                "civil penalties",
-                "credits",
-                "epa",
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
+                    "description": "This report provides three data elements for each fleet that includes vehicles that qualify as dual fuel under AMFA. Also available in PDF and XLS.",
+                    "downloadURL": "http://www.nhtsa.gov/CAFE_PIC/CAFE_PIC_AMFA_LIVE.html",
+                    "mediaType": "text/html",
+                    "title": "Flex Fuel/AMFA"
+                }
+            ],
+            "identifier": "1862.10",
+            "isPartOf": "DOT-1862",
+            "issued": "2015-12-16",
+            "keyword": [
+                "amfa",
+                "civil penalties",
+                "credits",
+                "epa",
                 "fleet",
                 "flex fuel",
                 "fuel economy",
@@ -16195,83 +16209,48 @@
                 "report",
                 "shortfall"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "1862.10",
+            "landingPage": "https://data.transportation.gov/d/6m9s-7skc",
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
-            "title": "CAFE (Corporate Average Fuel Economy) - Flex Fuel/AMFA",
-            "isPartOf": "DOT-1862",
-            "agencyProgramURL": "http://www.nhtsa.gov/fuel-economy",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.nhtsa.gov/CAFE_PIC/CAFE_PIC_AMFA_LIVE.html",
-                    "description": "This report provides three data elements for each fleet that includes vehicles that qualify as dual fuel under AMFA. Also available in PDF and XLS.",
-                    "@type": "dcat:Distribution",
-                    "title": "Flex Fuel/AMFA"
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
+            "title": "CAFE (Corporate Average Fuel Economy) - Flex Fuel/AMFA"
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
-            "landingPage": "https://data.transportation.gov/d/6mde-i8kk",
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
-            "identifier": "524.9",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
             "description": "STATE DATA REPORTING SYSTEMS. Annual reports on the Fatality Analysis Reporting System (FARS) which is data regarding fatalities that is collected by a FARS analyst from each State and provided to NHTSA.",
-            "title": "GES Reports - 2007",
-            "isPartOf": "DOT-524",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16280,52 +16259,54 @@
                     "title": "2007"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
-            "dataQuality": true,
+            "identifier": "524.9",
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
+            "landingPage": "https://data.transportation.gov/d/6mde-i8kk",
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
+            "title": "GES Reports - 2007"
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
-            "identifier": "https://data.transportation.gov/api/views/6mnf-74vh",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 1999",
-            "title": "Historic HPMS Data (Universe) - 1999",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16333,65 +16314,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6mnf-74vh/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6mnf-74vh/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6mnf-74vh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/6mnf-74vh/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6mnf-74vh/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6mnf-74vh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6mnf-74vh/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6mnf-74vh/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6mnf-74vh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/6mnf-74vh",
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
+            "title": "Historic HPMS Data (Universe) - 1999"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/6mpe-e53g",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2017-10-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-05",
-            "keyword": [
-                "aviation",
-                "form 41",
-                "majors",
-                "nationals",
-                "office fo the secretary of the transportation",
-                "quarterly financial review"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Randall Keizer",
                 "hasEmail": "mailto:Randall.Keizer@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "US Department of Transportation"
-            },
-            "identifier": "https://data.transportation.gov/api/views/6mpe-e53g",
+            "dataQuality": true,
             "description": "This report contains tables and charts on the financial condition of the U.S. major airlines. All data presented in this financial and traffic review are derived from data reported to the U.S. Department of Transportation on Form 41 Schedules by Large Certificated Air Carriers.\n\nThe data are presented on both a carrier group and an individual carrier basis, but the primary focus is on the individual major carrier and its performance. Data are presented for the most recent quarterly period and the comparable quarter a year earlier and also on a 12-month ended basis as at the end of the five most recent quarters. In addition, data on charges over comparable periods 12-months earlier are presented. A graphic presentation of comparative trends, on a carrier group basis, is made for several unit and overall financial indicators. In the case of merged carriers, data for the carriers involved have been combined and presented under the name of the surviving carrier so that meaningful comparisons could be made for the most recent 18 quarters.\n\nAlso, carriers can move between groupings (Majors and Nationals) based on the criteria listed below over time. Each report includes 18 quarters of data.  In the instance where a carrier falls into both groupings during the 18 quarters, a carrier will appear in both reports. The data from the Majors report and the data from the Nationals report should not be combined without ensuring any duplications are removed.\n\nCarrier Group Definitions\n\nMajors: Air carriers with annual operating revenues exceeding $1,000,000,000\nNationals: Air carriers with annual operating revenues between $100,000,000 and $1,000,000,000\nLarge Regionals: Air carriers with operating revenues between $20,000,000 and $99,000,000\nMedium Regionals: Carriers with annual operating revenues less than $19,999,999 or that operate only aircraft with 60 seats or less (or 18,000 lbs maximum payload)\n\nhttps://www.transportation.gov/policy/aviation-policy/airline-quarterly-financial-review",
-            "title": "Airline Quarterly Financial Review_Main_Both",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16399,48 +16383,82 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6mpe-e53g/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6mpe-e53g/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6mpe-e53g/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/6mpe-e53g/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6mpe-e53g/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6mpe-e53g/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6mpe-e53g/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6mpe-e53g/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6mpe-e53g/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/6mpe-e53g",
+            "issued": "2017-10-23",
+            "keyword": [
+                "aviation",
+                "form 41",
+                "majors",
+                "nationals",
+                "office fo the secretary of the transportation",
+                "quarterly financial review"
+            ],
+            "landingPage": "https://data.transportation.gov/d/6mpe-e53g",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2024-11-05",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
             "theme": [
                 "Aviation"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Airline Quarterly Financial Review_Main_Both"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/6nrf-i2js",
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
+                    "description": "2012 New Hampshire HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/newhampshire2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 New Hampshire"
+                }
+            ],
+            "identifier": "678.83",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -16454,82 +16472,41 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.83",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 New Hampshire",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/6nrf-i2js",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/newhampshire2012.zip",
-                    "description": "2012 New Hampshire HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 New Hampshire"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 New Hampshire"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/6nxx-nmxk",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2018-12-18",
-            "@type": "dcat:Dataset",
-            "modified": "2018-12-18",
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
-            "identifier": "https://data.transportation.gov/api/views/6nxx-nmxk",
+            "dataQuality": true,
             "description": "This dataset contains a sample of the broadcast Traveler Information Messages (TIM) being generated by the Wyoming Connected Vehicle (CV) Pilot. This dataset only contains SchemaVersion 6 TIM sample data from December 18, 2018 to present. It is updated hourly and will hold up to 3 million of the most recent TIM records. \n</n></n>\nThe Schema Version 6 data is described further <a href=\"https://github.com/usdot-its-jpo-data-portal/sandbox/wiki/DTG-WYDOT-Traveler-Information-Message-(TIM)-Schema-Version-6-Change-Notice\" target=\"_blank\">here</a>. For sample  TIM data prior to December 18, 2018, please refer to the <a href=\"https://data.transportation.gov/Automobiles/Wyoming-CV-Pilot-Traveler-Information-Message-Samp/2rdx-wgpx\" target=\"_blank\">Schema Version 5 dataset</a>. The full set of TIMs can be found in the <a href=\"http://usdot-its-cvpilot-publicdata.s3.amazonaws.com/index.html\" target=\"_blank\" >ITS Sandbox</a>.",
-            "title": "Wyoming CV Pilot Traveler Information Message Sample (Schema Version 6)",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16537,56 +16514,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6nxx-nmxk/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6nxx-nmxk/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6nxx-nmxk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/6nxx-nmxk/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6nxx-nmxk/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6nxx-nmxk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6nxx-nmxk/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6nxx-nmxk/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6nxx-nmxk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Wyoming",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/6nxx-nmxk",
+            "issued": "2018-12-18",
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
+            "landingPage": "https://data.transportation.gov/d/6nxx-nmxk",
+            "language": [
+                "English"
+            ],
             "license": "http://creativecommons.org/licenses/by-sa/4.0/legalcode",
-            "accrualPeriodicity": "irregular",
+            "modified": "2018-12-18",
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
+            "title": "Wyoming CV Pilot Traveler Information Message Sample (Schema Version 6)"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/6phk-249c",
-            "issued": "2023-08-08",
             "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
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
-            "identifier": "https://data.transportation.gov/api/views/6phk-249c",
             "description": "This a reference table for the Grade Crossing Inventory System, which is the application used to submit data for the Highway-Rail Grade Crossing Inventory (Form 71). The data dictionary for GCIS is attached as well. \n\nThe LookupType column contains the name of the field/column in the source GCIS/Form 71 dataset. The LookupValue column contains the submitted value and the LookupText field is the human-readable text description of that value (e.g. for LookupType=TypeXing; LookupValue=3 and LookupText=Public, which designates that a crossing is public). This reference table can be used for the Crossing Inventory Source Data Form 71 \u2013 Current: https://datahub.transportation.gov/dataset/Crossing-Inventory-Source-Data-Form-71-Current/xp92-5xme.",
-            "title": "Grade Crossing Inventory System - Highway-Rail Grade Crossing Inventory (Form 71) Field Reference Table",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16594,46 +16584,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6phk-249c/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6phk-249c/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6phk-249c/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/6phk-249c/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6phk-249c/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6phk-249c/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6phk-249c/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6phk-249c/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6phk-249c/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/6phk-249c",
+            "issued": "2023-08-08",
+            "landingPage": "https://data.transportation.gov/d/6phk-249c",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-02-01",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Grade Crossing Inventory System - Highway-Rail Grade Crossing Inventory (Form 71) Field Reference Table"
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
-            "landingPage": "https://data.transportation.gov/d/6pk8-pkam",
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
+                    "description": "JSAPI",
+                    "downloadURL": "https://maps.bts.dot.gov/services/rest/services/NHTSA/FARSCrashData/MapServer%3Ff=jsapi",
+                    "mediaType": "application/xhtml+xml",
+                    "title": "STSI FARS Crash Data Map"
+                }
             ],
+            "identifier": "266.1",
+            "isPartOf": "DOT-266",
+            "issued": "2009-09-01",
             "keyword": [
                 "crash",
                 "data",
@@ -16645,126 +16662,125 @@
                 "safety",
                 "vehicle"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "266.1",
+            "landingPage": "https://data.transportation.gov/d/6pk8-pkam",
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
-            "title": "State Traffic Safety Information - STSI FARS Crash Data Map",
-            "isPartOf": "DOT-266",
-            "agencyProgramURL": "http://www-nrd.nhtsa.dot.gov/departments/nrd-30/ncsa/STSI/USA%20WEB%20REPORT.HTM",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/xhtml+xml",
-                    "downloadURL": "https://maps.bts.dot.gov/services/rest/services/NHTSA/FARSCrashData/MapServer%3Ff=jsapi",
-                    "description": "JSAPI",
-                    "@type": "dcat:Distribution",
-                    "title": "STSI FARS Crash Data Map"
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
+            "title": "State Traffic Safety Information - STSI FARS Crash Data Map"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/6psf-8scu",
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
-            "identifier": "678.20",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": false,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
             "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Louisiana",
-            "isPartOf": "DOT-678",
-            "primaryITInvestmentUII": "021-099281808",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/zip",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/louisiana2011.zip",
-                    "description": "2011 Louisiana HPMS Shapefile",
                     "@type": "dcat:Distribution",
+                    "description": "2011 Louisiana HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/louisiana2011.zip",
+                    "mediaType": "application/zip",
                     "title": "2011 Louisiana"
                 }
             ],
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "678.20",
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
+            "landingPage": "https://data.transportation.gov/d/6psf-8scu",
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Louisiana"
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
-            "landingPage": "https://data.transportation.gov/d/6qbk-cnmv",
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
+                    "downloadURL": "http://www.fra.dot.gov/eLib/Details/L04114",
+                    "mediaType": "text/csv",
+                    "title": "Train and Engine Service (Railroad) Data"
+                }
             ],
+            "identifier": "283.7",
+            "isPartOf": "DOT-283",
+            "issued": "2008-03-01",
             "keyword": [
                 "alertness",
                 "employee",
@@ -16775,57 +16791,53 @@
                 "sleep",
                 "work"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "283.7",
+            "landingPage": "https://data.transportation.gov/d/6qbk-cnmv",
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
-            "title": "Work Schedules and Sleep Patterns of Railroad Employees - Train and Engine Service (Railroad) Data",
-            "isPartOf": "DOT-283",
-            "agencyProgramURL": "http://www.fra.dot.gov/Page/P0068",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fra.dot.gov/eLib/Details/L04114",
-                    "mediaType": "text/csv",
-                    "title": "Train and Engine Service (Railroad) Data"
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
+            "title": "Work Schedules and Sleep Patterns of Railroad Employees - Train and Engine Service (Railroad) Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/6qbu-yvq3",
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
+            "description": "This data set was acquired by the USDOT Data Capture and Management program. The purpose of the data set is to provide multi-modal data and contextual information (weather and incidents) that can be used to research and develop applications. Contains one full year (January \u2013 December 2010) of raw 30-second data for over 3,000 traffic detectors deployed along 1,250 lane miles of monitored roadway in San Diego. Cleaned and geographically referenced data for over 1,500 incidents and lane closures for the two sections of I-5 that experienced the greatest number of incidents during 2010. Complete trip (origin-to-destination) GPS \u201cbreadcrumbs\u201d collected by ALK Techonologies, containing latitude/longitude, vehicle heading and speed data, and time for individual in-vehicles devices updated at 3-second intervals for over 10,000 trips taken during 2010. A digital map shape file containing ALK\u2019s street-level network data for the San Diego Metropolitan area. And San Diego Weather data for 2010.\r\n\r\nThis legacy dataset was created before data.transportation.gov and is only currently available via the attached file(s). Please contact the dataset owner if there is a need for users to work with this data using the data.transportation.gov analysis features (online viewing, API, graphing, etc.) and the USDOT will consider modifying the dataset to fully integrate in data.transportation.gov.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/download/6qbu-yvq3/application/msword",
+                    "mediaType": "application/msword"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/6qbu-yvq3",
             "issued": "2012-02-22",
-            "@type": "dcat:Dataset",
-            "temporal": "2010-01-01/2010-12-31",
-            "modified": "2012-02-22",
             "keyword": [
                 "california",
                 "connected vehicle message",
@@ -16844,71 +16856,38 @@
                 "usdot data capture and management program (dcm)",
                 "weather"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/6qbu-yvq3",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
+            "modified": "2012-02-22",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Department of Transportation"
             },
-            "identifier": "https://data.transportation.gov/api/views/6qbu-yvq3",
-            "description": "This data set was acquired by the USDOT Data Capture and Management program. The purpose of the data set is to provide multi-modal data and contextual information (weather and incidents) that can be used to research and develop applications. Contains one full year (January \u2013 December 2010) of raw 30-second data for over 3,000 traffic detectors deployed along 1,250 lane miles of monitored roadway in San Diego. Cleaned and geographically referenced data for over 1,500 incidents and lane closures for the two sections of I-5 that experienced the greatest number of incidents during 2010. Complete trip (origin-to-destination) GPS \u201cbreadcrumbs\u201d collected by ALK Techonologies, containing latitude/longitude, vehicle heading and speed data, and time for individual in-vehicles devices updated at 3-second intervals for over 10,000 trips taken during 2010. A digital map shape file containing ALK\u2019s street-level network data for the San Diego Metropolitan area. And San Diego Weather data for 2010.\r\n\r\nThis legacy dataset was created before data.transportation.gov and is only currently available via the attached file(s). Please contact the dataset owner if there is a need for users to work with this data using the data.transportation.gov analysis features (online viewing, API, graphing, etc.) and the USDOT will consider modifying the dataset to fully integrate in data.transportation.gov.",
-            "title": "San Diego Test Data Sets",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/download/6qbu-yvq3/application/msword",
-                    "mediaType": "application/msword"
-                }
-            ],
             "spatial": "San Diego, California",
-            "dataQuality": true,
-            "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "irregular",
+            "temporal": "2010-01-01/2010-12-31",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "San Diego Test Data Sets"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/6qg9-x4f8",
             "bureauCode": [
                 "021:17"
             ],
-            "issued": "2023-04-14",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
-            "keyword": [
-                "active",
-                "for-hire motor carriers",
-                "operating authority",
-                "registration status",
-                "revoked",
-                "suspended"
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
-            "identifier": "https://data.transportation.gov/api/views/6qg9-x4f8",
             "description": "*This is a \"daily difference\" dataset.  See dataset attachment \"FMCSA Dataset Description and Data Definitions - Select Datasets\" for more information.*  Records for carriers/brokers/freight forwarders with active, inactive, or pending authorities (common or contract).  It includes the DOT number and MC/FF/MX number for the carrier/broker/freight forwarder, along with company census data, e.g., types of authority, address, types of insurance on file, and amounts of insurance on file.",
-            "title": "Carrier",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16916,23 +16895,48 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/6qg9-x4f8",
+            "issued": "2023-04-14",
+            "keyword": [
+                "active",
+                "for-hire motor carriers",
+                "operating authority",
+                "registration status",
+                "revoked",
+                "suspended"
+            ],
+            "landingPage": "https://data.transportation.gov/d/6qg9-x4f8",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-02-01",
+            "programCode": [
+                "021:000"
+            ],
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
+            "title": "Carrier"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/6r9f-bkkw",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Theresa Firestine",
+                "hasEmail": "mailto:theresa.firestine@dot.gov"
+            },
+            "description": "Page describes the U.S. Department of Transportation, Bureau of Transportation Statistics' bikeshare and e-scooter data offerings.",
+            "identifier": "https://data.transportation.gov/api/views/6r9f-bkkw",
             "issued": "2020-12-15",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-09",
             "keyword": [
                 "bikeshare",
                 "e-scooter",
@@ -16940,44 +16944,30 @@
                 "micromobility",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Theresa Firestine",
-                "hasEmail": "mailto:theresa.firestine@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/6r9f-bkkw",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-01-09",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/6r9f-bkkw",
-            "description": "Page describes the U.S. Department of Transportation, Bureau of Transportation Statistics' bikeshare and e-scooter data offerings.",
-            "title": "Bikeshare and Escooter for TRB",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Bicycles and Pedestrians"
-            ]
+            ],
+            "title": "Bikeshare and Escooter for TRB"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/6rg2-xpvd",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/6rg2-xpvd",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "Class 2's & 3's by Miles",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16985,42 +16975,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6rg2-xpvd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6rg2-xpvd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6rg2-xpvd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/6rg2-xpvd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6rg2-xpvd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6rg2-xpvd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6rg2-xpvd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6rg2-xpvd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6rg2-xpvd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/6rg2-xpvd",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/6rg2-xpvd",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Class 2's & 3's by Miles"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/6rij-vi8z",
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
+                    "description": "2011 Maryland HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/maryland2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Maryland"
+                }
+            ],
+            "identifier": "678.22",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -17034,90 +17052,58 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.22",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Maryland",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/6rij-vi8z",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/maryland2011.zip",
-                    "description": "2011 Maryland HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Maryland"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Maryland"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/6rt4-smhh",
-            "issued": "2023-10-18",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sean Jahanmir",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/6rt4-smhh",
+            "issued": "2023-10-18",
+            "landingPage": "https://data.transportation.gov/d/6rt4-smhh",
+            "modified": "2025-01-31",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Tables & Query Tool"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/6sqe-dvqs",
             "bureauCode": [
                 "021:17"
             ],
-            "issued": "2024-02-02",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
-            "keyword": [
-                "insurance",
-                "motor carrier"
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
-            "identifier": "https://data.transportation.gov/api/views/6sqe-dvqs",
             "description": "*Dataset*  This dataset contains information on a carrier\u2019s/broker\u2019s/freight forwarder\u2019s previous insurance policy(ies). This dataset contains the DOT number and docket number of the entity. Additionally, it contains the cancellation method (cancelled, replaced, name change, transferred), the type of policy, the policy number, and the effective and cancellation dates of the policy.  All insurance information is related to the insurance policy either being cancelled, being replaced, or prior to a name change.  It is not the subsequent (if applicable) policy.  See dataset attachment \"FMCSA Dataset Description and Data Definitions - Select Datasets\" for more information.",
-            "title": "InsHist - All With History",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17125,68 +17111,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6sqe-dvqs/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6sqe-dvqs/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6sqe-dvqs/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/6sqe-dvqs/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6sqe-dvqs/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6sqe-dvqs/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6sqe-dvqs/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6sqe-dvqs/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6sqe-dvqs/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/6sqe-dvqs",
+            "issued": "2024-02-02",
+            "keyword": [
+                "insurance",
+                "motor carrier"
+            ],
+            "landingPage": "https://data.transportation.gov/d/6sqe-dvqs",
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
+            "title": "InsHist - All With History"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/6t2m-6b8t",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2024-09-17",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
-            "keyword": [
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "speed data",
-                "traffic detectors",
-                "traffic flow",
-                "travel time",
-                "work zones"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elina Zlotchenko",
                 "hasEmail": "mailto:elina.zlotchenko@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/6t2m-6b8t",
             "description": "Data for Artificial Intelligence: Data-Centric AI for Transportation: Work Zone Use Case proposes a data integration pipeline that enhances the utilization of work zone and traffic data from diversified platforms and introduces a novel deep learning model to predict the traffic speed and traffic collision likelihood during planned work zone events. This dataset is raw Maryland 2019 Average Annual Daily Traffic data",
-            "title": "Data for Artificial Intelligence: Data-Centric AI for Transportation: Work Zone Use Case Raw Maryland Average Annual Daily Traffic 2019",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17194,43 +17172,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6t2m-6b8t/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6t2m-6b8t/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6t2m-6b8t/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/6t2m-6b8t/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6t2m-6b8t/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6t2m-6b8t/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6t2m-6b8t/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6t2m-6b8t/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6t2m-6b8t/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Maryland highway network",
+            "identifier": "https://data.transportation.gov/api/views/6t2m-6b8t",
+            "issued": "2024-09-17",
+            "keyword": [
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "speed data",
+                "traffic detectors",
+                "traffic flow",
+                "travel time",
+                "work zones"
+            ],
+            "landingPage": "https://data.transportation.gov/d/6t2m-6b8t",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-20",
+            "programCode": [
+                "021:042"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "spatial": "Maryland highway network",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "Data for Artificial Intelligence: Data-Centric AI for Transportation: Work Zone Use Case Raw Maryland Average Annual Daily Traffic 2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/",
             "bureauCode": [
                 "021:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "All FAF summary datasets",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The Freight Analysis Framework (FAF) integrates data from a variety of sources to create a comprehensive picture of freight movement among states and major metropolitan areas by all modes of transportation. With data from the Commodity Flow Survey and additional sources, the FAF version provides estimates for tonnage, value, and domestic ton-miles by region of origin and destination, commodity type, and mode for the most recent year, and long-term forecasts. Also included are state-to-state flows , summary statistics, and flows by truck assigned to the highway network.\n\n\nMore information on FAF is available at \u00a0https://ops.fhwa.dot.gov/freight/freight_analysis/faf/",
+                    "downloadURL": "https://ops.fhwa.dot.gov/freight/freight_analysis/faf/",
+                    "mediaType": "text/html",
+                    "title": "All FAF summary datasets"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/6tex-3tzx",
             "issued": "2023-05-23",
-            "temporal": "2012-01-01/2050-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
             "keyword": [
                 "commodity",
                 "consumption",
@@ -17255,50 +17268,53 @@
                 "value",
                 "wear"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
+            "landingPage": "http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-05-08",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/6tex-3tzx",
-            "description": "All FAF summary datasets",
-            "title": "Freight Analysis Framework",
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ops.fhwa.dot.gov/freight/freight_analysis/faf/",
-                    "description": "The Freight Analysis Framework (FAF) integrates data from a variety of sources to create a comprehensive picture of freight movement among states and major metropolitan areas by all modes of transportation. With data from the Commodity Flow Survey and additional sources, the FAF version provides estimates for tonnage, value, and domestic ton-miles by region of origin and destination, commodity type, and mode for the most recent year, and long-term forecasts. Also included are state-to-state flows , summary statistics, and flows by truck assigned to the highway network.\n\n\nMore information on FAF is available at \u00a0https://ops.fhwa.dot.gov/freight/freight_analysis/faf/",
-                    "@type": "dcat:Distribution",
-                    "title": "All FAF summary datasets"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2012-01-01/2050-12-31",
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Freight Analysis Framework"
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
-            "landingPage": "https://data.transportation.gov/d/6ti8-qkrf",
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
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2001NTDxls.exe",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2001 Database"
+                }
             ],
+            "identifier": "21.5",
+            "isPartOf": "DOT-21",
+            "issued": "2010-10-01",
             "keyword": [
                 "agency",
                 "allocation",
@@ -17317,76 +17333,44 @@
                 "urbanized",
                 "vehicles"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John D. Giorgis",
-                "hasEmail": "mailto:john.giorgis@dot.gov"
-            },
-            "identifier": "21.5",
+            "landingPage": "https://data.transportation.gov/d/6ti8-qkrf",
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
-            "title": "NTD Annual Module Data Set - 2001 Database",
-            "isPartOf": "DOT-21",
-            "agencyProgramURL": "http://www.ntdprogram.gov",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2001NTDxls.exe",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "2001 Database"
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
+            "title": "NTD Annual Module Data Set - 2001 Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/6u8d-47ih",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2022-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-23",
-            "keyword": [
-                "air carriers",
-                "airlines",
-                "passengers"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Todd Solomon",
                 "hasEmail": "mailto:todd.solomon@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/6u8d-47ih",
+            "dataQuality": true,
             "description": "Enplaned baggage and wheelchairs and scooters mishandled by commercial air carriers.",
-            "title": "Commercial Aviation - Mishandled Baggage and Mishandled Wheelchairs and Scooter",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17394,49 +17378,83 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6u8d-47ih/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6u8d-47ih/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6u8d-47ih/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/6u8d-47ih/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6u8d-47ih/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6u8d-47ih/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6u8d-47ih/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6u8d-47ih/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6u8d-47ih/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/6u8d-47ih",
+            "issued": "2022-02-23",
+            "keyword": [
+                "air carriers",
+                "airlines",
+                "passengers"
+            ],
+            "landingPage": "https://data.transportation.gov/d/6u8d-47ih",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2022-02-23",
+            "phone": "2023660573",
+            "programCode": [
+                "021:042"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Aviation"
             ],
-            "phone": "2023660573",
-            "language": [
-                "en-US"
-            ]
+            "title": "Commercial Aviation - Mishandled Baggage and Mishandled Wheelchairs and Scooter"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/6vgk-gsn3",
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
+                    "description": "2011 North Dakota HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/northdakota2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 North Dakota"
+                }
+            ],
+            "identifier": "678.36",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -17450,112 +17468,73 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.36",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 North Dakota",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/6vgk-gsn3",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/northdakota2011.zip",
-                    "description": "2011 North Dakota HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 North Dakota"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 North Dakota"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/6vnx-7g89",
-            "issued": "2025-01-16",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-16",
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
-            "identifier": "https://data.transportation.gov/api/views/6vnx-7g89",
             "description": "The Bureau of Transportation Statistics releases non-seasonally adjusted air traffic data based on monthly reports from commercial U.S. air carriers.",
-            "title": "Air Travel - Total",
+            "identifier": "https://data.transportation.gov/api/views/6vnx-7g89",
+            "issued": "2025-01-16",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/6vnx-7g89",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-16",
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
+            "title": "Air Travel - Total"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://catalog.data.faa.gov/dataset/sectional-vfr-charts",
             "bureauCode": [
                 "021:12"
             ],
-            "issued": "2020-11-14",
-            "@type": "dcat:Dataset",
-            "modified": "2021-11-09",
-            "keyword": [
-                "georeference",
-                "geospatial",
-                "raster",
-                "vfr",
-                "visual-chart"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Chief Data Office",
                 "hasEmail": "mailto:9-EIM-InfoLink@faa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Aviation Administration"
-            },
-            "identifier": "6cc8afc1-111c-4338-8d92-60c3d16c749d",
             "description": "The Federal Aviation Administration (FAA) digital-Visual Chart series is designed to meet the needs of users who require georeferenced raster images of FAA Visual Flight Rules (VFR) charts. An Aeronautical Raster Chart is a digital image of an FAA VFR Chart. All information that is part of the paper chart is included in the file. The area inside the neat line is georeferenced to the surface of the earth. Only the main body of the chart is accurately georeferenced. Each digital-Visual Chart is provided in one TIF file. The files are 300 dots per inch and 8-bit color.",
-            "title": "Sectional VFR Charts",
-            "primaryITInvestmentUII": "021-129509270",
-            "programCode": [
-                "021:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17564,26 +17543,65 @@
                     "title": "Aeronautical Information Services Digital Products"
                 }
             ],
-            "systemOfRecords": "https://www.govinfo.gov/content/pkg/FR-2016-08-15/pdf/2016-19354.pdf",
+            "identifier": "6cc8afc1-111c-4338-8d92-60c3d16c749d",
+            "issued": "2020-11-14",
+            "keyword": [
+                "georeference",
+                "geospatial",
+                "raster",
+                "vfr",
+                "visual-chart"
+            ],
+            "landingPage": "https://catalog.data.faa.gov/dataset/sectional-vfr-charts",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2021-11-09",
+            "primaryITInvestmentUII": "021-129509270",
+            "programCode": [
+                "021:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Aviation Administration"
+            },
+            "systemOfRecords": "https://www.govinfo.gov/content/pkg/FR-2016-08-15/pdf/2016-19354.pdf",
             "theme": [
                 "Aviation"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sectional VFR Charts"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/6wkh-3m7u",
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
+                    "description": "2013 Arizona HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/arizona2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Arizona"
+                }
+            ],
+            "identifier": "678.107",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -17597,57 +17615,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.107",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Arizona",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/6wkh-3m7u",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/arizona2013.zip",
-                    "description": "2013 Arizona HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Arizona"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Arizona"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/6x5e-z89b",
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
+                    "description": "2012 District of Columbia HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/district2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 District of Columbia"
+                }
+            ],
+            "identifier": "678.62",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -17661,83 +17679,46 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.62",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 District of Columbia",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/6x5e-z89b",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/district2012.zip",
-                    "description": "2012 District of Columbia HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 District of Columbia"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 District of Columbia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "The data system is not publicly available because it is related solely to internal agency management and may contain sensitive data.",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://safety.fhwa.dot.gov/tools/data_tools/",
+            "agencyProgramURL": "http://safety.fhwa.dot.gov/hsip/",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/6xdp-ibqz",
-            "issued": "2014-12-29",
-            "temporal": "R/2014-12-29/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative - Financial",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
-            "references": [
-                "http://safety.fhwa.dot.gov/tools/data_tools/memohsip072911/"
-            ],
-            "keyword": [
-                "highway",
-                "safety"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "687.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://safety.fhwa.dot.gov/tools/data_tools/memohsip072911/",
             "description": "The HSIP ORT establishes a standardized reporting process that promotes consistency among state reports while maintaining flexibility to meet states reporting needs. It allows States and Divisions to submit required annual HSIP reports through an easy to use web interface, and will be used for regular and special reports for the White House, Congress, FHWA management, OST, GAO and others.",
-            "title": "Highway Safety Improvement Program (HSIP) - Highway Safety Improvement Program",
-            "isPartOf": "DOT-687",
-            "agencyProgramURL": "http://safety.fhwa.dot.gov/hsip/",
-            "primaryITInvestmentUII": "021-133811186",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17746,54 +17727,55 @@
                     "title": "Highway Safety Improvement Program"
                 }
             ],
-            "spatial": "National, State",
-            "describedBy": "http://safety.fhwa.dot.gov/tools/data_tools/memohsip072911/",
-            "dataQuality": true,
+            "identifier": "687.2",
+            "isPartOf": "DOT-687",
+            "issued": "2014-12-29",
+            "keyword": [
+                "highway",
+                "safety"
+            ],
+            "landingPage": "https://data.transportation.gov/d/6xdp-ibqz",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://safety.fhwa.dot.gov/tools/data_tools/",
+            "modified": "2024-05-08",
+            "phone": "609-637-4207",
+            "primaryITInvestmentUII": "021-133811186",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "references": [
+                "http://safety.fhwa.dot.gov/tools/data_tools/memohsip072911/"
+            ],
+            "rights": "The data system is not publicly available because it is related solely to internal agency management and may contain sensitive data.",
+            "spatial": "National, State",
+            "temporal": "R/2014-12-29/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Administrative - Financial",
-            "phone": "609-637-4207",
-            "language": [
-                "en-US"
-            ]
+            "title": "Highway Safety Improvement Program (HSIP) - Highway Safety Improvement Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Contains proprietary carrier information.",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/6xk6-4x2r",
-            "issued": "2014-12-15",
-            "temporal": "R/2014-12-15/PT1S",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "cdl",
-                "commercial drivers licenses",
-                "enforcement."
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO",
                 "hasEmail": "mailto:fmcsa.cdo@dot.gov"
             },
-            "identifier": "368.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": true,
             "description": "CDLIS - Gateway is the clearinghouse for CDL information collected by all states, and provides a gateway for enforcement users to access CDL data. CDLIS Gateway was developed to provide authorized FMCSA users with access to CDLIS. This system is maintained exclusively by FMCSA using a contractor.",
-            "title": "Commercial Drivers License Information System - Gateway: (CDLIS - Gateway) -",
-            "primaryITInvestmentUII": "021-255033325",
-            "programCode": [
-                "021:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17801,56 +17783,54 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
-            ],
-            "accrualPeriodicity": "R/PT1S",
-            "categoryDesignation": "Research",
+            "identifier": "368.0",
+            "issued": "2014-12-15",
+            "keyword": [
+                "cdl",
+                "commercial drivers licenses",
+                "enforcement."
+            ],
+            "landingPage": "https://data.transportation.gov/d/6xk6-4x2r",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-7066"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-24",
+            "phone": "202-366-7066",
+            "primaryITInvestmentUII": "021-255033325",
+            "programCode": [
+                "021:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "rights": "Contains proprietary carrier information.",
+            "temporal": "R/2014-12-15/PT1S",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Commercial Drivers License Information System - Gateway: (CDLIS - Gateway) -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "https://www.nhtsa.gov/vehicle-safety",
+            "agencyProgramURL": "https://www.nhtsa.gov/vehicle-safety",
+            "analysisUnit": "N/A",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/6xxv-r986",
-            "issued": "2010-01-05",
-            "temporal": "R/2000-01-01/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "https://www.nhtsa.gov/vehicle-safety/car-seats-and-booster-seats"
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
-            "identifier": "80.3",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "The Child Safety Seat Inspection Station Locations are used to make it easier for all citizens to get their Child Safety Seats properly installed. Car crashes are the largest cause of fatalities and serious injuries for children between ages 2 and 15.  Also, surveys indicate that a high percentage of Child Safety Seats are not installed properly.  Information updates for each station are reported to NHTSA and entered by NHTSA staff.  NHTSA staff will also attempt to validate the station locations using a commercial geographic database so this data will, in most cases, be able to be used for driving directions.",
-            "title": "NHTSA Child Safety Seat Inspection Station Locator",
-            "isPartOf": "DOT-80",
-            "agencyProgramURL": "https://www.nhtsa.gov/vehicle-safety",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17859,57 +17839,58 @@
                     "title": "NHTSA API"
                 }
             ],
-            "spatial": "Zip, State, Geo co-ordinates",
-            "dataQuality": true,
+            "identifier": "80.3",
+            "isPartOf": "DOT-80",
+            "issued": "2010-01-05",
+            "keyword": [
+                "child seat",
+                "inspection",
+                "safety",
+                "station",
+                "stations"
+            ],
+            "landingPage": "https://data.transportation.gov/d/6xxv-r986",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "https://www.nhtsa.gov/vehicle-safety",
+            "modified": "2024-05-01",
+            "programCode": [
+                "021:032"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "https://www.nhtsa.gov/vehicle-safety/car-seats-and-booster-seats"
+            ],
+            "spatial": "Zip, State, Geo co-ordinates",
+            "temporal": "R/2000-01-01/P1D",
             "theme": [
                 "Transportation Car Seat Safety"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "categoryDesignation": "Research",
-            "analysisUnit": "N/A",
-            "language": [
-                "en-US"
-            ]
+            "title": "NHTSA Child Safety Seat Inspection Station Locator"
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
-            "landingPage": "https://data.transportation.gov/d/6y9x-x6u8",
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
-            "identifier": "694.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": false,
+            "describedBy": "http://mutcd.fhwa.dot.gov/orsearch.asp",
             "description": "The MUTCD Official Rulings is a resource that allows web site visitors to obtain information about requests for changes, experiments, and interpretations related to the MUTCD that have been received by the FHWA. Copies of various documents (such as incoming request letters, response letters from the FHWA, progress reports, and final reports) that are available in both pdf and html formats may be viewed on this web site. The current status of experiments, as well as any contact information for the requestor that has been made a part of the public record, is also available.",
-            "title": "Manual on Uniform Traffic Control Devices (MUTCD) - Search Official Rulings",
-            "isPartOf": "DOT-694",
-            "agencyProgramURL": "http://mutcd.fhwa.dot.gov",
-            "programCode": [
-                "021:011"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17918,47 +17899,51 @@
                     "title": "Search Official Rulings"
                 }
             ],
-            "describedBy": "http://mutcd.fhwa.dot.gov/orsearch.asp",
-            "dataQuality": false,
+            "identifier": "694.1",
+            "isPartOf": "DOT-694",
+            "issued": "2011-06-01",
+            "keyword": [
+                "experiment",
+                "interpretation",
+                "mutcd",
+                "official ruling"
+            ],
+            "landingPage": "https://data.transportation.gov/d/6y9x-x6u8",
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
+            "title": "Manual on Uniform Traffic Control Devices (MUTCD) - Search Official Rulings"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/6zs4-qsk2",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2021-01-05",
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
-            "identifier": "https://data.transportation.gov/api/views/6zs4-qsk2",
+            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
             "description": "State DOTs provide the location limits of highway sections to be used to represent statewide aggregations based on a statistically valid Sample Panel. \nThe North contains data for the following States: Maine, New Hampshire, Vermont, New York, Massachusetts, Rhode Island, Connecticut, New Jersey, Pennsylvania, Ohio, Maryland, District of Columbia, and Delaware.",
-            "title": "Roadway Sections North 2019",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17966,75 +17951,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6zs4-qsk2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6zs4-qsk2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6zs4-qsk2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/6zs4-qsk2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6zs4-qsk2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6zs4-qsk2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/6zs4-qsk2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/6zs4-qsk2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/6zs4-qsk2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "USA",
-            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
+            "identifier": "https://data.transportation.gov/api/views/6zs4-qsk2",
+            "issued": "2021-01-05",
+            "landingPage": "https://data.transportation.gov/d/6zs4-qsk2",
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
+            "title": "Roadway Sections North 2019"
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
-            "landingPage": "https://data.transportation.gov/d/725m-q8em",
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
-            "identifier": "671.2",
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
@@ -18043,35 +18024,69 @@
                     "title": "Search Tool"
                 }
             ],
-            "describedBy": "http://www.fra.dot.gov/eLib/Find",
-            "dataQuality": true,
+            "identifier": "671.2",
+            "isPartOf": "DOT-671",
+            "issued": "2014-11-21",
+            "keyword": [
+                "fra elibrary",
+                "fra e-library",
+                "fra library",
+                "library fra"
+            ],
+            "landingPage": "https://data.transportation.gov/d/725m-q8em",
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
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/735r-2ena",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/10maytvt/10maytvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "May 2010"
+                }
             ],
+            "identifier": "18.22",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -18081,60 +18096,60 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.22",
+            "landingPage": "https://data.transportation.gov/d/735r-2ena",
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
-            "title": "Monthly Traffic Volume Trends - May 2010",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/10maytvt/10maytvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "May 2010"
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
+            "title": "Monthly Traffic Volume Trends - May 2010"
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
-            "landingPage": "https://data.transportation.gov/d/73g2-rytk",
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
+                    "downloadURL": "https://cms.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/docs/closedByEnforcement_FY2008_04-26-2013a.xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Fiscal Year 2008"
+                }
             ],
+            "identifier": "96.3",
+            "isPartOf": "DOT-96",
+            "issued": "2018-12-17",
             "keyword": [
                 "bus",
                 "civil penalties",
@@ -18147,122 +18162,84 @@
                 "motor carrier",
                 "truck"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "96.3",
+            "landingPage": "https://data.transportation.gov/d/73g2-rytk",
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
-            "title": "Closed Enforcement Cases - Fiscal Year 2008",
-            "isPartOf": "DOT-96",
-            "agencyProgramURL": "http://www.fmcsa.dot.gov/regulations/enforcement/civil-penalties",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://cms.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/docs/closedByEnforcement_FY2008_04-26-2013a.xlsx",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "Fiscal Year 2008"
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
+            "title": "Closed Enforcement Cases - Fiscal Year 2008"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/73zm-qqf9",
-            "issued": "2022-09-28",
             "@type": "dcat:Dataset",
-            "modified": "2022-09-28",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/73zm-qqf9",
+            "issued": "2022-09-28",
+            "landingPage": "https://data.transportation.gov/d/73zm-qqf9",
+            "modified": "2022-09-28",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
-            "title": "Emerging Themes and Considerations",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "Emerging Themes and Considerations"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/74fq-gc77",
-            "issued": "2022-08-09",
             "@type": "dcat:Dataset",
-            "modified": "2023-05-15",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ong, Lisa CTR (OST)",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "A Description of data fields, data definitions, and some context on changes between the different Commodity Flow Surveys",
             "identifier": "https://data.transportation.gov/api/views/74fq-gc77",
+            "issued": "2022-08-09",
+            "landingPage": "https://data.transportation.gov/d/74fq-gc77",
+            "modified": "2023-05-15",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "A Description of data fields, data definitions, and some context on changes between the different Commodity Flow Surveys",
             "title": "CFS Data Cleaning and Organizing"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/74ug-57tr",
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
-            "identifier": "https://data.transportation.gov/api/views/74ug-57tr",
+            "dataQuality": true,
             "description": "The data describe freeway car-following behavior (such as velocity, acceleration, and relative position) for the car-following instances observed during 6 data collection runs, collected using an Instrumented Research Vehicle (IRV) along freeways and arterials in western Massachusetts in the summer of 2016 to better understand work zone driver behaviors. The USDOT Volpe National Transportation Systems Center (Volpe Center) identified, isolated, and classified individual car following instances from within the raw datasets (classification parameters included roadway type, level of congestion, and speed limit), then processed, refined, and cleaned the dataset.\n\nThis table contains the car-following instances recorded by Volpe staff. See also the runs table (https://datahub.transportation.gov/Automobiles/Enhancing-Microsimulation-Models-for-Improved-Work/b3k6-qwyh) and radar table (https://datahub.transportation.gov/Automobiles/Enhancing-Microsimulation-Models-for-Improved-Work/4qbx-egtn).",
-            "title": "Enhancing Microsimulation Models for Improved Work Zone Planning: Car-Following Data from Western Massachusetts (Instances)",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18270,75 +18247,77 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/74ug-57tr/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/74ug-57tr/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/74ug-57tr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/74ug-57tr/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/74ug-57tr/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/74ug-57tr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/74ug-57tr/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/74ug-57tr/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/74ug-57tr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "-72.5339,42.0211,-72.6494,42.3927",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/74ug-57tr",
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
+            "landingPage": "https://data.transportation.gov/d/74ug-57tr",
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
+            "title": "Enhancing Microsimulation Models for Improved Work Zone Planning: Car-Following Data from Western Massachusetts (Instances)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/ltccs/default.asp%3Fpage=data",
+            "agencyProgramURL": "http://ai.fmcsa.dot.gov/ltccs/default.asp",
+            "analysisUnit": "Crash / Vehicle / Driver / Person",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/74zb-wiyy",
-            "issued": "2006-07-14",
-            "temporal": "2003-01-01/2003-12-31",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "http://ai.fmcsa.dot.gov/ltccs/default.asp%3Fpage=data",
-            "modified": "2024-05-24",
-            "references": [
-                "http://ai.fmcsa.dot.gov/ltccs/data/documents/LTCCS_Manual_Public.pdf"
-            ],
-            "keyword": [
-                "crash",
-                "federal motor carrier safety administration",
-                "fmcsa",
-                "large truck",
-                "large truck crash causation study",
-                "ltccs"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO",
                 "hasEmail": "mailto:fmcsa.cdo@dot.gov"
             },
-            "identifier": "97.3",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
-            "description": "The Large Truck* Crash Causation Study (LTCCS) is based on a three-year data collection project conducted by the Federal Motor Carrier Safety Administration (FMCSA) and the National Highway Traffic Safety Administration (NHTSA) of the U.S. Department of Transportation (DOT). LTCCS is the first-ever national study to attempt to determine the critical events and associated factors that contribute to serious large truck crashes allowing DOT and others to implement effective countermeasures to reduce the occurrence and severity of these crashes.",
-            "title": "Large Truck Crash Causation Study (LTCCS) - File 1 (TXT)",
-            "isPartOf": "DOT-97",
-            "agencyProgramURL": "http://ai.fmcsa.dot.gov/ltccs/default.asp",
+            "dataQuality": true,
+            "describedBy": "http://ai.fmcsa.dot.gov/ltccs/data/documents/LTCCS_Codebook.pdf",
             "describedByType": "application/pdf",
-            "primaryITInvestmentUII": "021-155552608",
-            "programCode": [
-                "021:022"
-            ],
+            "description": "The Large Truck* Crash Causation Study (LTCCS) is based on a three-year data collection project conducted by the Federal Motor Carrier Safety Administration (FMCSA) and the National Highway Traffic Safety Administration (NHTSA) of the U.S. Department of Transportation (DOT). LTCCS is the first-ever national study to attempt to determine the critical events and associated factors that contribute to serious large truck crashes allowing DOT and others to implement effective countermeasures to reduce the occurrence and severity of these crashes.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18347,36 +18326,72 @@
                     "title": "File 1 (TXT)"
                 }
             ],
-            "spatial": "National estimates",
-            "describedBy": "http://ai.fmcsa.dot.gov/ltccs/data/documents/LTCCS_Codebook.pdf",
-            "dataQuality": true,
+            "identifier": "97.3",
+            "isPartOf": "DOT-97",
+            "issued": "2006-07-14",
+            "keyword": [
+                "crash",
+                "federal motor carrier safety administration",
+                "fmcsa",
+                "large truck",
+                "large truck crash causation study",
+                "ltccs"
+            ],
+            "landingPage": "https://data.transportation.gov/d/74zb-wiyy",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/ltccs/default.asp%3Fpage=data",
+            "modified": "2024-05-24",
+            "phone": "202-366-0324",
+            "primaryITInvestmentUII": "021-155552608",
+            "programCode": [
+                "021:022"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "references": [
+                "http://ai.fmcsa.dot.gov/ltccs/data/documents/LTCCS_Manual_Public.pdf"
+            ],
+            "spatial": "National estimates",
+            "temporal": "2003-01-01/2003-12-31",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Crash / Vehicle / Driver / Person",
-            "phone": "202-366-0324",
-            "language": [
-                "en-US"
-            ]
+            "title": "Large Truck Crash Causation Study (LTCCS) - File 1 (TXT)"
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
-            "landingPage": "https://data.transportation.gov/d/75ef-gwb7",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/04juntvt/04juntvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "June 2004"
+                }
             ],
+            "identifier": "18.123",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -18386,76 +18401,43 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.123",
+            "landingPage": "https://data.transportation.gov/d/75ef-gwb7",
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
-            "title": "Monthly Traffic Volume Trends - June 2004",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/04juntvt/04juntvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "June 2004"
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
+            "title": "Monthly Traffic Volume Trends - June 2004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://data.transportation.gov/d/75qq-qmj6",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2020-12-08",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-23",
-            "keyword": [
-                "freight",
-                "frieight trucking",
-                "maritime",
-                "ports"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Todd Solomon",
                 "hasEmail": "mailto:todd.solomon@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/75qq-qmj6",
             "description": "Weekly measures of freight activity during the COVID-19 pandemic",
-            "title": "Freight Activity",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18463,47 +18445,75 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/75qq-qmj6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/75qq-qmj6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/75qq-qmj6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/75qq-qmj6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/75qq-qmj6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/75qq-qmj6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/75qq-qmj6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/75qq-qmj6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/75qq-qmj6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1W",
-            "phone": "2023660573",
+            "identifier": "https://data.transportation.gov/api/views/75qq-qmj6",
+            "issued": "2020-12-08",
+            "keyword": [
+                "freight",
+                "frieight trucking",
+                "maritime",
+                "ports"
+            ],
+            "landingPage": "https://data.transportation.gov/d/75qq-qmj6",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2022-02-23",
+            "phone": "2023660573",
+            "programCode": [
+                "021:042"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Freight Activity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.21949/1503648",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2019-04-10",
-            "@type": "dcat:Dataset",
-            "temporal": "1995-01-01/1995-12-31",
-            "modified": "2019-04-10",
-            "references": [
-                "https://doi.org/10.21949/1503648"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Leighton L Christiansen",
+                "hasEmail": "mailto:ntldatacurator@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The 1995 American Travel Survey (ATS) was conducted by the Bureau of Transportation Statistics (BTS) to obtain information about the long-distance travel of persons living in the United States. The survey collected quarterly information related to the characteristics of persons, households, and trips of 100 miles or more for approximately 80,000 American households. The ATS data provide detailed information on state-to-state travel as well as travel to and from metropolitan areas by mode of transportation. Data are also available for subgroups defined in terms of characteristics related to travel, such as trip purpose, age, family type, income, and a variety of related characteristics. The data can be analyzed at the regional, state, metropolitan area, and county level. NOTE: In 2001, the National Household Travel Survey was carried out. This new survey is a combined Nationwide Personal Transportation Survey (NPTS) and ATS. Visit the National Household Travel Survey web site << https://nhts.ornl.gov/ >> for more details.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The 1995 American Travel Survey (ATS) was conducted by the Bureau of Transportation Statistics (BTS) to obtain information about the long-distance travel of persons living in the United States. The survey collected quarterly information related to the characteristics of persons, households, and trips of 100 miles or more for approximately 80,000 American households. The ATS data provide detailed information on state-to-state travel as well as travel to and from metropolitan areas by mode of transportation. Data are also available for subgroups defined in terms of characteristics related to travel, such as trip purpose, age, family type, income, and a variety of related characteristics. The data can be analyzed at the regional, state, metropolitan area, and county level. NOTE: In 2001, the National Household Travel Survey was carried out. This new survey is a combined Nationwide Personal Transportation Survey (NPTS) and ATS. Visit the National Household Travel Survey web site << https://nhts.ornl.gov/ >> for more details.",
+                    "downloadURL": "https://doi.org/10.21949/1503648",
+                    "mediaType": "application/zip",
+                    "title": "American Travel Survey (ATS) 1995 [dataset]"
+                }
             ],
+            "identifier": "https://data.transportation.gov/api/views/762v-n95h",
+            "issued": "2019-04-10",
             "keyword": [
                 "mode choice",
                 "origin and destination",
@@ -18513,54 +18523,57 @@
                 "trip length",
                 "trip purpose"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Leighton L Christiansen",
-                "hasEmail": "mailto:ntldatacurator@dot.gov"
-            },
+            "landingPage": "https://doi.org/10.21949/1503648",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2019-04-10",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statisitics"
             },
-            "identifier": "https://data.transportation.gov/api/views/762v-n95h",
-            "description": "The 1995 American Travel Survey (ATS) was conducted by the Bureau of Transportation Statistics (BTS) to obtain information about the long-distance travel of persons living in the United States. The survey collected quarterly information related to the characteristics of persons, households, and trips of 100 miles or more for approximately 80,000 American households. The ATS data provide detailed information on state-to-state travel as well as travel to and from metropolitan areas by mode of transportation. Data are also available for subgroups defined in terms of characteristics related to travel, such as trip purpose, age, family type, income, and a variety of related characteristics. The data can be analyzed at the regional, state, metropolitan area, and county level. NOTE: In 2001, the National Household Travel Survey was carried out. This new survey is a combined Nationwide Personal Transportation Survey (NPTS) and ATS. Visit the National Household Travel Survey web site << https://nhts.ornl.gov/ >> for more details.",
-            "title": "American Travel Survey (ATS) 1995 [datasets]",
-            "programCode": [
-                "021:053"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://doi.org/10.21949/1503648",
-                    "description": "The 1995 American Travel Survey (ATS) was conducted by the Bureau of Transportation Statistics (BTS) to obtain information about the long-distance travel of persons living in the United States. The survey collected quarterly information related to the characteristics of persons, households, and trips of 100 miles or more for approximately 80,000 American households. The ATS data provide detailed information on state-to-state travel as well as travel to and from metropolitan areas by mode of transportation. Data are also available for subgroups defined in terms of characteristics related to travel, such as trip purpose, age, family type, income, and a variety of related characteristics. The data can be analyzed at the regional, state, metropolitan area, and county level. NOTE: In 2001, the National Household Travel Survey was carried out. This new survey is a combined Nationwide Personal Transportation Survey (NPTS) and ATS. Visit the National Household Travel Survey web site << https://nhts.ornl.gov/ >> for more details.",
-                    "@type": "dcat:Distribution",
-                    "title": "American Travel Survey (ATS) 1995 [dataset]"
-                }
+            "references": [
+                "https://doi.org/10.21949/1503648"
             ],
             "spatial": "United States",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
+            "temporal": "1995-01-01/1995-12-31",
             "theme": [
                 "Research and Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "American Travel Survey (ATS) 1995 [datasets]"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "https://www.phmsa.dot.gov/data-and-statistics/pipeline/leading-indicators-srcr-and-im-notifications",
+            "agencyProgramURL": "http://www.phmsa.dot.gov/pipeline",
             "bureauCode": [
                 "021:50"
             ],
-            "landingPage": "https://data.transportation.gov/d/76qv-bk88",
-            "issued": "2003-01-01",
-            "temporal": "R/2002-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-29",
+            "categoryDesignation": "Administrative - Regulatory",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.phmsa.dot.gov/pipeline"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Liezl Gonzalez",
+                "hasEmail": "mailto:liezl.gonzalez@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "PHMSA tracks Safety-Related Condition Reports (SRCR) and Integrity Assurance (formerly IM) Notifications submitted by operators to monitor the effectiveness of integrity programs and safety management systems before accidents, damages, or failures happen. PHMSA regulations include several exemptions from SRCR reporting. These exemptions limit the usefulness of SRCR as a leading indicator.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.phmsa.dot.gov/staticfiles/PHMSA/DownloadableFiles/Files/Pipeline/Safety_Related_Condition_Reports(SRCRs)_2002_to_present.zip",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Safety Related Condition Reports (SRCRs) 2002 to present (ZIP)"
+                }
             ],
+            "identifier": "267.0",
+            "issued": "2003-01-01",
             "keyword": [
                 "condition",
                 "gas",
@@ -18570,53 +18583,45 @@
                 "report",
                 "safety"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Liezl Gonzalez",
-                "hasEmail": "mailto:liezl.gonzalez@dot.gov"
-            },
-            "identifier": "267.0",
+            "landingPage": "https://data.transportation.gov/d/76qv-bk88",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-07-29",
+            "phone": "202-366-1878",
+            "programCode": [
+                "021:044"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Pipeline and Hazardous Materials Safety Administration"
             },
-            "description": "PHMSA tracks Safety-Related Condition Reports (SRCR) and Integrity Assurance (formerly IM) Notifications submitted by operators to monitor the effectiveness of integrity programs and safety management systems before accidents, damages, or failures happen. PHMSA regulations include several exemptions from SRCR reporting. These exemptions limit the usefulness of SRCR as a leading indicator.",
-            "title": "Leading Indicators - SRCR and Integrity Assurance (formerly IM) Notifications",
-            "agencyProgramURL": "http://www.phmsa.dot.gov/pipeline",
-            "programCode": [
-                "021:044"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.phmsa.dot.gov/staticfiles/PHMSA/DownloadableFiles/Files/Pipeline/Safety_Related_Condition_Reports(SRCRs)_2002_to_present.zip",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "Safety Related Condition Reports (SRCRs) 2002 to present (ZIP)"
-                }
+            "references": [
+                "http://www.phmsa.dot.gov/pipeline"
             ],
             "spatial": "City",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "https://www.phmsa.dot.gov/data-and-statistics/pipeline/leading-indicators-srcr-and-im-notifications",
+            "temporal": "R/2002-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Administrative - Regulatory",
-            "phone": "202-366-1878",
-            "language": [
-                "en-US"
-            ]
+            "title": "Leading Indicators - SRCR and Integrity Assurance (formerly IM) Notifications"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://international.fhwa.dot.gov/",
             "bureauCode": [
                 "021:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The objective of this dataset is to create a location where there is a comprehensive list of all technologies, best practices and lessons learned from the Office of International Programs as a whole.",
+            "identifier": "https://data.transportation.gov/api/views/776k-x6rt",
             "issued": "2021-07-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-04",
             "keyword": [
                 "bridges",
                 "construction",
@@ -18624,65 +18629,43 @@
                 "transportation best practices",
                 "transportation technologies"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
+            "landingPage": "https://international.fhwa.dot.gov/",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-04",
+            "programCode": [
+                "021:009"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/776k-x6rt",
-            "description": "The objective of this dataset is to create a location where there is a comprehensive list of all technologies, best practices and lessons learned from the Office of International Programs as a whole.",
-            "title": "Transportation Technology and Best Practicies",
-            "programCode": [
-                "021:009"
-            ],
             "spatial": "United States",
-            "dataQuality": true,
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Transportation Technology and Best Practicies"
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
-            "landingPage": "https://data.transportation.gov/d/78fc-wvpd",
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
-                "trade-in"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "11.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
+            "describedBy": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Transaction+Data+and+Reports",
             "description": "The Car Allowance Rebate System (CARS), otherwise known as Cash for Clunkers, was a program intended to provide economic incentives to United States residents to purchase a new and more fuel efficient vehicle when trading in a less full efficient vehicle. The program was promoted as providing stimulus to the economy by boosting auto sales, while putting safer, cleaner and more fuel efficient vehicles on the road.",
-            "title": "Car Allowance Rebate System (CARS) - Trade-In Vehicles - Trade-In Vehicles xls file",
-            "isPartOf": "DOT-11",
-            "agencyProgramURL": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Officially+Ended",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18691,30 +18674,61 @@
                     "title": "Trade-In Vehicles xls file"
                 }
             ],
-            "spatial": "N/A",
-            "describedBy": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Transaction+Data+and+Reports",
-            "dataQuality": false,
+            "identifier": "11.2",
+            "isPartOf": "DOT-11",
+            "issued": "2018-12-17",
+            "keyword": [
+                "cars",
+                "trade-in"
+            ],
+            "landingPage": "https://data.transportation.gov/d/78fc-wvpd",
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
+            "title": "Car Allowance Rebate System (CARS) - Trade-In Vehicles - Trade-In Vehicles xls file"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/78r5-bm67",
             "bureauCode": [
                 "021:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kate Hartman",
+                "hasEmail": "mailto:kate.hartman@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Assessment of V2X technologies for safety, system efficiency, and mobility; and assessment of the safest and most efficient use of allocated spectrum to accommodate transportation needs requires transparent, comprehensive, and repeatable test results that assure that the technologies work under normal as well as varying traffic conditions that create \u201cedge-use\u201d cases. Below are data collected by the ITS JPO as part of V2X Testing, the blue button links to the ITS V2X Testing website and the Data Dictionary button links to a briefing on the LTE-V2X Testing Data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The goal of the U.S. DOT\u2019s LTE-V2X Test Program is to examine the radio performance of LTE-V2X technology under challenging, \u201cedge-use case\u201d conditions\u2014the type of conditions that result in some of the most common and fatal crashes. These challenging conditions are not exclusive to transportation. However, because the V2X communications and BSM transmissions are designed to provide 360-degree awareness around a vehicle of the threats and hazards forming on the roadway from nearby vehicles, pedestrians, motorcycles, bicyclists or others, examination of the radio environment\u2014its reliability and availability\u2014is equally as important. The test team designed scenarios to mimic the type of complex roadway conditions under which the radio or communications technology must perform reliably and consistently in a broadcast, non-networked mode. The radio performance must sustain communications under a variety of conditions. The blue button links to the ITS V2X Testing website and the Data Dictionary button links to a briefing on the LTE-V2X Testing Data.",
+                    "downloadURL": "https://its.dot.gov/research_areas/emerging_tech/htm/ITS_V2X_Testing.htm",
+                    "mediaType": "text/html",
+                    "title": "ITS Vehicle-To-Everything (V2X) Testing"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/78r5-bm67",
             "issued": "2023-11-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
             "keyword": [
                 "cellular",
                 "connected vehicles",
@@ -18726,79 +18740,43 @@
                 "radio spectrum",
                 "vehicle to everything (v2x)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/78r5-bm67",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-07",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Department of Transportation"
             },
-            "identifier": "https://data.transportation.gov/api/views/78r5-bm67",
-            "description": "Assessment of V2X technologies for safety, system efficiency, and mobility; and assessment of the safest and most efficient use of allocated spectrum to accommodate transportation needs requires transparent, comprehensive, and repeatable test results that assure that the technologies work under normal as well as varying traffic conditions that create \u201cedge-use\u201d cases. Below are data collected by the ITS JPO as part of V2X Testing, the blue button links to the ITS V2X Testing website and the Data Dictionary button links to a briefing on the LTE-V2X Testing Data.",
-            "title": "ITS Vehicle-To-Everything (V2X) Testing",
-            "programCode": [
-                "021:053"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://its.dot.gov/research_areas/emerging_tech/htm/ITS_V2X_Testing.htm",
-                    "description": "The goal of the U.S. DOT\u2019s LTE-V2X Test Program is to examine the radio performance of LTE-V2X technology under challenging, \u201cedge-use case\u201d conditions\u2014the type of conditions that result in some of the most common and fatal crashes. These challenging conditions are not exclusive to transportation. However, because the V2X communications and BSM transmissions are designed to provide 360-degree awareness around a vehicle of the threats and hazards forming on the roadway from nearby vehicles, pedestrians, motorcycles, bicyclists or others, examination of the radio environment\u2014its reliability and availability\u2014is equally as important. The test team designed scenarios to mimic the type of complex roadway conditions under which the radio or communications technology must perform reliably and consistently in a broadcast, non-networked mode. The radio performance must sustain communications under a variety of conditions. The blue button links to the ITS V2X Testing website and the Data Dictionary button links to a briefing on the LTE-V2X Testing Data.",
-                    "@type": "dcat:Distribution",
-                    "title": "ITS Vehicle-To-Everything (V2X) Testing"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ITS Vehicle-To-Everything (V2X) Testing"
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
-            "landingPage": "https://data.transportation.gov/d/79d4-etsr",
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
-            "identifier": "18.139",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - February 2003",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18807,39 +18785,51 @@
                     "title": "February 2003"
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
+            "identifier": "18.139",
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
+            "landingPage": "https://data.transportation.gov/d/79d4-etsr",
+            "language": [
                 "en-US"
-            ]
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
+            "title": "Monthly Traffic Volume Trends - February 2003"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/7a4q-c7c4",
-            "issued": "2023-08-09",
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
-            "identifier": "https://data.transportation.gov/api/views/7a4q-c7c4",
             "description": "",
-            "title": "Highway-Rail Grade Crossing Incident (Form 71) Reason for Update Field Reference Table",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18847,46 +18837,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/7a4q-c7c4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7a4q-c7c4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7a4q-c7c4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/7a4q-c7c4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7a4q-c7c4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7a4q-c7c4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/7a4q-c7c4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7a4q-c7c4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7a4q-c7c4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/7a4q-c7c4",
+            "issued": "2023-08-09",
+            "landingPage": "https://data.transportation.gov/d/7a4q-c7c4",
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
+            "title": "Highway-Rail Grade Crossing Incident (Form 71) Reason for Update Field Reference Table"
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
-            "landingPage": "https://data.transportation.gov/d/7a9e-ghr9",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/13aprtvt/13aprtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "April 2013"
+                }
             ],
+            "identifier": "18.49",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -18896,73 +18911,43 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.49",
+            "landingPage": "https://data.transportation.gov/d/7a9e-ghr9",
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
-            "title": "Monthly Traffic Volume Trends - April 2013",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/13aprtvt/13aprtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "April 2013"
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
+            "title": "Monthly Traffic Volume Trends - April 2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/7b9r-bf38",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2020-11-10",
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
-            "identifier": "https://data.transportation.gov/api/views/7b9r-bf38",
+            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
             "description": "State DOT will provide Local Vehicle-Miles-Traveled (VMT) summarized by FHWA Adjusted Urban Area.",
-            "title": "Urban Summaries 2019",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18970,74 +18955,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/7b9r-bf38/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7b9r-bf38/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7b9r-bf38/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/7b9r-bf38/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7b9r-bf38/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7b9r-bf38/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/7b9r-bf38/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7b9r-bf38/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7b9r-bf38/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "USA",
-            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
+            "identifier": "https://data.transportation.gov/api/views/7b9r-bf38",
+            "issued": "2020-11-10",
+            "landingPage": "https://data.transportation.gov/d/7b9r-bf38",
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
-            ]
+            ],
+            "title": "Urban Summaries 2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/foia/errpolicy.htm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/foia/errpolicy.htm",
+            "analysisUnit": "Regulations",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/7ck4-qdfe",
-            "issued": "2011-01-18",
-            "temporal": "1998-01-01/2011-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.fhwa.dot.gov/foia/errpolicy.htm"
-            ],
-            "keyword": [
-                "data.gov",
-                "highway",
-                "interpretation",
-                "law",
-                "policy",
-                "transportation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "303.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "Specific Federal Highway Administration Policy Statements",
-            "title": "Federal Highway Administration Policy Statements -",
-            "isPartOf": "DOT-303",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/foia/errpolicy.htm",
-            "primaryITInvestmentUII": "021-803057200",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19045,34 +19023,72 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "303.2",
+            "isPartOf": "DOT-303",
+            "issued": "2011-01-18",
+            "keyword": [
+                "data.gov",
+                "highway",
+                "interpretation",
+                "law",
+                "policy",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/7ck4-qdfe",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/foia/errpolicy.htm",
+            "modified": "2024-05-08",
+            "phone": "202-366-4308",
+            "primaryITInvestmentUII": "021-803057200",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "references": [
+                "http://www.fhwa.dot.gov/foia/errpolicy.htm"
+            ],
+            "temporal": "1998-01-01/2011-01-18",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Regulations",
-            "phone": "202-366-4308",
-            "language": [
-                "en-US"
-            ]
+            "title": "Federal Highway Administration Policy Statements -"
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
-            "landingPage": "https://data.transportation.gov/d/7cnt-i6d4",
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
+                    "description": "JSAPI",
+                    "downloadURL": "https://maps.bts.dot.gov/services/rest/services/NHTSA/FARSCrashData/MapServer%3Ff=jsapi",
+                    "mediaType": "application/xhtml+xml",
+                    "title": "STSI FARS Crash Data Map"
+                }
             ],
+            "identifier": "DOT-266",
+            "issued": "2009-09-01",
             "keyword": [
                 "crash",
                 "data",
@@ -19084,83 +19100,49 @@
                 "safety",
                 "vehicle"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "DOT-266",
+            "landingPage": "https://data.transportation.gov/d/7cnt-i6d4",
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
-            "title": "State Traffic Safety Information",
-            "agencyProgramURL": "http://www-nrd.nhtsa.dot.gov/departments/nrd-30/ncsa/STSI/USA%20WEB%20REPORT.HTM",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/xhtml+xml",
-                    "downloadURL": "https://maps.bts.dot.gov/services/rest/services/NHTSA/FARSCrashData/MapServer%3Ff=jsapi",
-                    "description": "JSAPI",
-                    "@type": "dcat:Distribution",
-                    "title": "STSI FARS Crash Data Map"
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
+            "title": "State Traffic Safety Information"
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
-            "landingPage": "https://data.transportation.gov/d/7cwh-eqhq",
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
-            "identifier": "364.5",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database - Vehicle Test Query by Vehicle Barrier Parameters",
-            "isPartOf": "DOT-364",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
-            "primaryITInvestmentUII": "021-621341357",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19169,35 +19151,68 @@
                     "title": "Vehicle Test Query by Vehicle Barrier Parameters"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.5",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/7cwh-eqhq",
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
+            "title": "Vehicle Safety Research and Development Database - Vehicle Test Query by Vehicle Barrier Parameters"
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
-            "landingPage": "https://data.transportation.gov/d/7dp6-8fad",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/09octtvt/09octtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "October 2009"
+                }
             ],
+            "identifier": "18.29",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -19207,85 +19222,44 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.29",
+            "landingPage": "https://data.transportation.gov/d/7dp6-8fad",
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
-            "title": "Monthly Traffic Volume Trends - October 2009",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/09octtvt/09octtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "October 2009"
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
+            "title": "Monthly Traffic Volume Trends - October 2009"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/7ee5-ppkq",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2016-09-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2016-11-14/2016-11-16",
-            "modified": "2016-09-01",
-            "keyword": [
-                "advanced messaging concept development (amcd)",
-                "arterial",
-                "blacksburg",
-                "connected vehicle message",
-                "dedicated short range communication (dsrc)",
-                "field test",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "northern virginia",
-                "on-board unit (obu)",
-                "probe vehicle data (pvd)",
-                "virginia tech transportation institute (vtti)"
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
-            "identifier": "https://data.transportation.gov/api/views/7ee5-ppkq",
+            "dataQuality": true,
             "description": "Contains all PVDs generated during the AMCD field testing program. The probe vehicle message is used to exchange status about a vehicle with other DSRC readers to allow the collection of information about a typical vehicle\u2019s traveling behaviors along a segment of road. The exchanges of this message as well as the event which caused the collection of various elements defined in the messages are in Annex B of the SAE J2735 standard.",
-            "title": "Advanced Messaging Concept Development: Probe Vehicle Data",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19293,46 +19267,90 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/7ee5-ppkq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7ee5-ppkq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7ee5-ppkq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/7ee5-ppkq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7ee5-ppkq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7ee5-ppkq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/7ee5-ppkq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7ee5-ppkq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7ee5-ppkq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Tyson\u2019s Corner, Fairfax County, Virginia",
-            "dataQuality": true,
-            "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "irregular",
-            "theme": [
-                "Automobiles"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "bureauCode": [
-                "021:15"
+            "identifier": "https://data.transportation.gov/api/views/7ee5-ppkq",
+            "issued": "2016-09-01",
+            "keyword": [
+                "advanced messaging concept development (amcd)",
+                "arterial",
+                "blacksburg",
+                "connected vehicle message",
+                "dedicated short range communication (dsrc)",
+                "field test",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "northern virginia",
+                "on-board unit (obu)",
+                "probe vehicle data (pvd)",
+                "virginia tech transportation institute (vtti)"
             ],
-            "landingPage": "https://data.transportation.gov/d/7f3r-7agx",
-            "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
+            "landingPage": "https://data.transportation.gov/d/7ee5-ppkq",
+            "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
+            "modified": "2016-09-01",
+            "programCode": [
+                "021:013"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
+            "spatial": "Tyson\u2019s Corner, Fairfax County, Virginia",
+            "temporal": "2016-11-14/2016-11-16",
+            "theme": [
+                "Automobiles"
+            ],
+            "title": "Advanced Messaging Concept Development: Probe Vehicle Data"
+        },
+        {
             "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
+            "bureauCode": [
+                "021:15"
+            ],
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
+                    "description": "2011 Michigan HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/michigan2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Michigan"
+                }
+            ],
+            "identifier": "678.24",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -19346,111 +19364,97 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.24",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Michigan",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/7f3r-7agx",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/michigan2011.zip",
-                    "description": "2011 Michigan HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Michigan"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Michigan"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.bts.gov/stories/s/7fgy-2zkf",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Interactive visualizations showing the long-term trends in docked bikeshare trips by system and type of trip, membership level, and time of day since 2019. Updated monthly.",
+            "identifier": "https://data.transportation.gov/api/views/7fgy-2zkf",
             "issued": "2021-04-30",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
             "keyword": [
                 "bikeshare",
                 "e-scooter",
                 "micromobility"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.bts.gov/stories/s/7fgy-2zkf",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-13",
+            "phone": "202-366-DATA(3282)",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/7fgy-2zkf",
-            "description": "Interactive visualizations showing the long-term trends in docked bikeshare trips by system and type of trip, membership level, and time of day since 2019. Updated monthly.",
-            "title": "Summary of Docked Bikeshare Trips by System and Other Attributes",
-            "programCode": [
-                "021:053"
-            ],
             "spatial": "United States",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1M",
             "theme": [
                 "Bicycles and Pedestrians"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Summary of Docked Bikeshare Trips by System and Other Attributes"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/7fhg-qii2",
-            "issued": "2021-05-17",
             "@type": "dcat:Dataset",
-            "modified": "2024-04-25",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sean Jahanmir",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/7fhg-qii2",
+            "issued": "2021-05-17",
+            "landingPage": "https://data.transportation.gov/d/7fhg-qii2",
+            "modified": "2024-04-25",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Economy"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/7fjw-dp4g",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "The Infrastructure Investment and Jobs Act also known as the Bipartisan Infrastructure Law contains billions in transportation funding. This report breaks that funding down by mode.",
+            "identifier": "https://data.transportation.gov/api/views/7fjw-dp4g",
             "issued": "2022-03-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-27",
             "keyword": [
                 "bil",
                 "bil transportation funds",
@@ -19459,41 +19463,53 @@
                 "iija transportation funds",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/7fjw-dp4g",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-08-27",
+            "phone": "202-366-DATA(3282)",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/7fjw-dp4g",
-            "description": "The Infrastructure Investment and Jobs Act also known as the Bipartisan Infrastructure Law contains billions in transportation funding. This report breaks that funding down by mode.",
-            "title": "Infrastructure Investment and Jobs Act (BIL) Transportation Funding by Mode",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Infrastructure Investment and Jobs Act (BIL) Transportation Funding by Mode"
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
-            "landingPage": "https://data.transportation.gov/d/7fke-aiwe",
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
+                    "downloadURL": "http://www.fra.dot.gov/eLib/Details/L04112",
+                    "mediaType": "text/csv",
+                    "title": "Signalmen Daily Log"
+                }
             ],
+            "identifier": "283.6",
+            "isPartOf": "DOT-283",
+            "issued": "2008-03-01",
             "keyword": [
                 "alertness",
                 "employee",
@@ -19504,65 +19520,39 @@
                 "sleep",
                 "work"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "283.6",
+            "landingPage": "https://data.transportation.gov/d/7fke-aiwe",
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
-            "title": "Work Schedules and Sleep Patterns of Railroad Employees - Signalmen Daily Log",
-            "isPartOf": "DOT-283",
-            "agencyProgramURL": "http://www.fra.dot.gov/Page/P0068",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fra.dot.gov/eLib/Details/L04112",
-                    "mediaType": "text/csv",
-                    "title": "Signalmen Daily Log"
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
+            "title": "Work Schedules and Sleep Patterns of Railroad Employees - Signalmen Daily Log"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/7fxu-rrf7",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/7fxu-rrf7",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "SMT 2 - PATRIOT RAIL",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19570,71 +19560,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/7fxu-rrf7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7fxu-rrf7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7fxu-rrf7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/7fxu-rrf7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7fxu-rrf7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7fxu-rrf7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/7fxu-rrf7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7fxu-rrf7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7fxu-rrf7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/7fxu-rrf7",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/7fxu-rrf7",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "SMT 2 - PATRIOT RAIL"
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
-            "landingPage": "https://data.transportation.gov/d/7ga4-7hek",
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
-            "identifier": "557.3",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
+            "describedBy": "https://www.civilrights.dot.gov/node/3828",
             "description": "Data related to the management of EEO complaint processing.  Due to the presence of PII, the raw data is not available for public consumption.  However, aggregated data is available in the DOT's NoFEAR Act report and Form 462 Report.  Both are located on the DOT Office of Civil Rights' public website.",
-            "title": "EEO Complaint Processing Data - FAA No FEAR Data",
-            "isPartOf": "DOT-557",
-            "agencyProgramURL": "http://www.civilrights.dot.gov",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19643,60 +19622,61 @@
                     "title": "FAA No FEAR Data"
                 }
             ],
-            "describedBy": "https://www.civilrights.dot.gov/node/3828",
-            "dataQuality": false,
+            "identifier": "557.3",
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
+            "landingPage": "https://data.transportation.gov/d/7ga4-7hek",
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
+            "title": "EEO Complaint Processing Data - FAA No FEAR Data"
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
-            "landingPage": "https://data.transportation.gov/d/7gnc-y8iv",
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
-            "identifier": "693.13",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
             "description": "The NBI System is the collection of bridge inspection information and costs associated with bridge replacements of structurally deficient bridges on and off the NHS. This data is collected under the auspices of the National Bridge Inspection Standards (NBIS) as prescribed by law. The NBI System collects the information that is used to determine eligibility for NHS projects, performance measure reporting, NHS penalty determination, and reporting to Congress.  It supports oversight of the NBIS through various report tools, and provides data reporting that supports agency strategic goals.",
-            "title": "National Bridge Inventory System (NBI) - 2004",
-            "isPartOf": "DOT-693",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
-            "primaryITInvestmentUII": "021-012940226",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19705,36 +19685,70 @@
                     "title": "2004"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
-            "dataQuality": true,
+            "identifier": "693.13",
+            "isPartOf": "DOT-693",
+            "issued": "1992-12-31",
+            "keyword": [
+                "bridge",
+                "condition",
+                "deck",
+                "inspection",
+                "structure"
+            ],
+            "landingPage": "https://data.transportation.gov/d/7gnc-y8iv",
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
+            "title": "National Bridge Inventory System (NBI) - 2004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/ProgramReport/PassengerCarrier.aspx",
+            "agencyProgramURL": "http://ai.fmcsa.dot.gov/ProgramReport/PassengerCarrier.aspx",
+            "analysisUnit": "Passenger Carriers",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/7gz5-f42x",
-            "issued": "2009-03-15",
-            "temporal": "R/2009-10-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://ai.fmcsa.dot.gov/ProgramReport/PassengerCarrier.aspx"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The reports listed below are designed to provide information focused on passenger vehicles and carriers. All reports provide options to choose fiscal or calendar year, and carrier domicile including United States, Canada, and Mexico.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://ai.fmcsa.dot.gov/ProgramReport/PassengerCarrier.aspx",
+                    "mediaType": "text/html",
+                    "title": "Pasenger Carrier Safety Data"
+                }
             ],
+            "identifier": "DOT-130",
+            "issued": "2009-03-15",
             "keyword": [
                 "authority grated",
                 "compliance review",
@@ -19746,93 +19760,49 @@
                 "safety audit",
                 "violation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "DOT-130",
+            "landingPage": "https://data.transportation.gov/d/7gz5-f42x",
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
-            "description": "The reports listed below are designed to provide information focused on passenger vehicles and carriers. All reports provide options to choose fiscal or calendar year, and carrier domicile including United States, Canada, and Mexico.",
-            "title": "A&I - Passenger Carrier Statistics",
-            "agencyProgramURL": "http://ai.fmcsa.dot.gov/ProgramReport/PassengerCarrier.aspx",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://ai.fmcsa.dot.gov/ProgramReport/PassengerCarrier.aspx",
-                    "mediaType": "text/html",
-                    "title": "Pasenger Carrier Safety Data"
-                }
+            "references": [
+                "http://ai.fmcsa.dot.gov/ProgramReport/PassengerCarrier.aspx"
             ],
             "spatial": "National and State",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/ProgramReport/PassengerCarrier.aspx",
+            "temporal": "R/2009-10-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "analysisUnit": "Passenger Carriers",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4869",
-            "language": [
-                "en-US"
-            ]
+            "title": "A&I - Passenger Carrier Statistics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/HazmatStat/Default.aspx",
+            "agencyProgramURL": "http://ai.fmcsa.dot.gov/HazmatStat/Default.aspx",
+            "analysisUnit": "Hazardous Materials Motor Carriers",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/7h34-ee79",
-            "issued": "2010-07-15",
-            "temporal": "R/2009-10-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://ai.fmcsa.dot.gov/HazmatStat/Default.aspx"
-            ],
-            "keyword": [
-                "bulk",
-                "compliance review",
-                "hazardous materials",
-                "hazardous materials safety permit",
-                "hm",
-                "hmsp",
-                "motor carriers",
-                "non-bulk",
-                "oos",
-                "out of service",
-                "registration",
-                "roadside inspection",
-                "shipper",
-                "violation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO",
                 "hasEmail": "mailto:fmcsa.cdo@dot.gov"
             },
-            "identifier": "120.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": true,
             "description": "The reports listed below are designed to provide information focused on hazardous materials and carriers and the hazardous materials safety permit program. All reports provide options to choose fiscal or calendar year, and carrier domicile including United States, Canada, and Mexico.",
-            "title": "A&I - Hazardous Materials Carrier - Hazardous Materials Safety Data",
-            "isPartOf": "DOT-120",
-            "agencyProgramURL": "http://ai.fmcsa.dot.gov/HazmatStat/Default.aspx",
-            "primaryITInvestmentUII": "021-534052663",
-            "programCode": [
-                "021:022"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19841,35 +19811,80 @@
                     "title": "Hazardous Materials Safety Data"
                 }
             ],
-            "spatial": "National, State",
-            "dataQuality": true,
+            "identifier": "120.2",
+            "isPartOf": "DOT-120",
+            "issued": "2010-07-15",
+            "keyword": [
+                "bulk",
+                "compliance review",
+                "hazardous materials",
+                "hazardous materials safety permit",
+                "hm",
+                "hmsp",
+                "motor carriers",
+                "non-bulk",
+                "oos",
+                "out of service",
+                "registration",
+                "roadside inspection",
+                "shipper",
+                "violation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/7h34-ee79",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/HazmatStat/Default.aspx",
+            "modified": "2024-05-24",
+            "phone": "202-366-2161",
+            "primaryITInvestmentUII": "021-534052663",
+            "programCode": [
+                "021:022"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "references": [
+                "http://ai.fmcsa.dot.gov/HazmatStat/Default.aspx"
+            ],
+            "spatial": "National, State",
+            "temporal": "R/2009-10-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Hazardous Materials Motor Carriers",
-            "phone": "202-366-2161",
-            "language": [
-                "en-US"
-            ]
+            "title": "A&I - Hazardous Materials Carrier - Hazardous Materials Safety Data"
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
-            "landingPage": "https://data.transportation.gov/d/7he8-gc8s",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12augtvt/12augtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "August 2012"
+                }
             ],
+            "identifier": "18.41",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -19879,81 +19894,48 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.41",
+            "landingPage": "https://data.transportation.gov/d/7he8-gc8s",
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
-            "title": "Monthly Traffic Volume Trends - August 2012",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12augtvt/12augtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "August 2012"
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
+            "title": "Monthly Traffic Volume Trends - August 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://hazmat.fmcsa.dot.gov/nhmrr/index.asp",
+            "agencyProgramURL": "http://hazmat.fmcsa.dot.gov/nhmrr/index.asp",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/7ieq-vihu",
-            "issued": "2015-04-29",
-            "temporal": "2015-04-29/2015-04-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.fmcsa.dot.gov/regulations/hazardous-materials"
-            ],
-            "keyword": [
-                "hazmat",
-                "hazmat routes",
-                "registered routes"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Paul Bomgardner",
                 "hasEmail": "mailto:paul.bomgardner@dot.gov"
             },
-            "identifier": "108.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": false,
             "description": "Information related to preferred and restricted routes for carrying hazardous materials.",
-            "title": "National HM Route Registry - National HM Route Registry",
-            "agencyProgramURL": "http://hazmat.fmcsa.dot.gov/nhmrr/index.asp",
-            "programCode": [
-                "021:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19962,34 +19944,68 @@
                     "title": "National HM Route Registry"
                 }
             ],
-            "spatial": "State",
-            "dataQuality": false,
+            "identifier": "108.0",
+            "issued": "2015-04-29",
+            "keyword": [
+                "hazmat",
+                "hazmat routes",
+                "registered routes"
+            ],
+            "landingPage": "https://data.transportation.gov/d/7ieq-vihu",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://hazmat.fmcsa.dot.gov/nhmrr/index.asp",
+            "modified": "2024-08-01",
+            "phone": "202-493-0001",
+            "programCode": [
+                "021:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "references": [
+                "http://www.fmcsa.dot.gov/regulations/hazardous-materials"
+            ],
+            "spatial": "State",
+            "temporal": "2015-04-29/2015-04-29",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "phone": "202-493-0001",
-            "language": [
-                "en-US"
-            ]
+            "title": "National HM Route Registry - National HM Route Registry"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://fhwaapps.fhwa.dot.gov/cmaq_pub/HomePage/default.aspx",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/environment/air_quality/cmaq/",
+            "analysisUnit": "Project",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/7j4t-9ckv",
-            "issued": "1992-01-01",
-            "temporal": "R/1992-01-01/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "N/A",
-            "modified": "2024-05-08",
-            "references": [
-                "https://fhwaapps.fhwa.dot.gov/cmaq_pub/"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://fhwaapps.fhwa.dot.gov/cmaq_pub/",
+            "description": "All 50 states and the District of Columbia submit annual reports of their CMAQ project obligations in March of   every year. The FHWA uses these yearly submissions to maintain an active database of CMAQ investments, trends within the program, and other anecdotal information focusing on the program's performance. This   database of CMAQ Project information has always been reserved for internal use by authorized FHWA personnel for Congressional reporting and made available to state DOTs and MPOs on a limited basis.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://fhwaapps.fhwa.dot.gov/cmaq_pub/",
+                    "mediaType": "text/html",
+                    "title": "Public Access System"
+                }
             ],
+            "identifier": "287.2",
+            "isPartOf": "DOT-287",
+            "issued": "1992-01-01",
             "keyword": [
                 "air",
                 "area",
@@ -20010,59 +20026,61 @@
                 "quality",
                 "voc"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "287.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "All 50 states and the District of Columbia submit annual reports of their CMAQ project obligations in March of   every year. The FHWA uses these yearly submissions to maintain an active database of CMAQ investments, trends within the program, and other anecdotal information focusing on the program's performance. This   database of CMAQ Project information has always been reserved for internal use by authorized FHWA personnel for Congressional reporting and made available to state DOTs and MPOs on a limited basis.",
-            "title": "Congestion Mitigation and Air Quality (CMAQ) - Public Access System",
-            "isPartOf": "DOT-287",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/environment/air_quality/cmaq/",
+            "landingPage": "https://data.transportation.gov/d/7j4t-9ckv",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-2076",
             "primaryITInvestmentUII": "021-856997945",
             "programCode": [
                 "021:000"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://fhwaapps.fhwa.dot.gov/cmaq_pub/",
-                    "mediaType": "text/html",
-                    "title": "Public Access System"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "references": [
+                "https://fhwaapps.fhwa.dot.gov/cmaq_pub/"
             ],
             "spatial": "Metropolitan Area",
-            "describedBy": "https://fhwaapps.fhwa.dot.gov/cmaq_pub/",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "https://fhwaapps.fhwa.dot.gov/cmaq_pub/HomePage/default.aspx",
+            "temporal": "R/1992-01-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Project",
-            "phone": "202-366-2076",
-            "language": [
-                "en-US"
-            ]
+            "title": "Congestion Mitigation and Air Quality (CMAQ) - Public Access System"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/7j9v-i3nv",
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
+                    "description": "2012 National Highway System Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/pa_nhs_2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 National Highway System"
+                }
+            ],
+            "identifier": "678.156",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -20076,79 +20094,40 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.156",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 National Highway System",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/7j9v-i3nv",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/pa_nhs_2012.zip",
-                    "description": "2012 National Highway System Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 National Highway System"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 National Highway System"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/7kx6-58yb",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2020-12-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "references": [
-                "https://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/hpms_field_manual_dec2016.pdf"
-            ],
-            "keyword": [
-                "2018",
-                "hpms",
-                "mid-america",
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
-            "identifier": "https://data.transportation.gov/api/views/7kx6-58yb",
+            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMSS",
             "description": "This data represents HPMS Sample limits that correspond to the HPMS Section Data. This dataset contains expansion factors that are used to expand the attributes to State wide aggregation. More information regarding the Sample dataset is contained in the HPMS Field Manual.\nThe Mid-America contains data for the following States: Illinois, Indiana, Iowa, Kansas, Michigan, Minnesota, Missouri, Nebraska, North Dakota, Oklahoma, South Dakota, Texas, and Wisconsin",
-            "title": "HPMS Sample Mid-America 2018",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20156,65 +20135,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/7kx6-58yb/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7kx6-58yb/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7kx6-58yb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/7kx6-58yb/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7kx6-58yb/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7kx6-58yb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/7kx6-58yb/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7kx6-58yb/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7kx6-58yb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "USA",
-            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMSS",
+            "identifier": "https://data.transportation.gov/api/views/7kx6-58yb",
+            "issued": "2020-12-08",
+            "keyword": [
+                "2018",
+                "hpms",
+                "mid-america",
+                "sample"
+            ],
+            "landingPage": "https://data.transportation.gov/d/7kx6-58yb",
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
+                "https://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/hpms_field_manual_dec2016.pdf"
+            ],
+            "spatial": "USA",
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "HPMS Sample Mid-America 2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/7m5x-ubud",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2023-07-11",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-21",
-            "keyword": [
-                "bikeshare",
-                "docked bikeshare"
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
-            "identifier": "https://data.transportation.gov/api/views/7m5x-ubud",
             "description": "Latitude and longitude for docked bikeshare stations by system and year. Data can be used to see the changes in the locations of docked bikeshare stations over time within a system. Only docked bikeshare systems open to the general public are included in the count. College, employer, and resident docked bikeshare systems are not counted.",
-            "title": "Locations of Docked Bikeshare Stations by System and Year",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20222,44 +20205,79 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/7m5x-ubud/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7m5x-ubud/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7m5x-ubud/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/7m5x-ubud/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7m5x-ubud/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7m5x-ubud/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/7m5x-ubud/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7m5x-ubud/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7m5x-ubud/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/7m5x-ubud",
+            "issued": "2023-07-11",
+            "keyword": [
+                "bikeshare",
+                "docked bikeshare"
+            ],
+            "landingPage": "https://data.transportation.gov/d/7m5x-ubud",
             "license": "https://www.usa.gov/government-works",
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
                 "Bicycles and Pedestrians"
             ],
-            "phone": "202-366-DATA(3282) "
+            "title": "Locations of Docked Bikeshare Stations by System and Year"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/7mqw-5tii",
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
+                    "description": "2012 California HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/california2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 California"
+                }
+            ],
+            "identifier": "678.58",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -20273,76 +20291,40 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.58",
+            "landingPage": "https://data.transportation.gov/d/7mqw-5tii",
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
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 California",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/california2012.zip",
-                    "description": "2012 California HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 California"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 California"
+        },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/7mzw-a8si",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-11-04",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-04",
-            "keyword": [
-                "air",
-                "exports",
-                "imports",
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
-            "identifier": "https://data.transportation.gov/api/views/7mzw-a8si",
             "description": "Annual value of U.S. imports and exports by water, air, and land.",
-            "title": "U.S. Imports and Exports Value by Year and Mode 2003 thru 2023",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20350,85 +20332,119 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/7mzw-a8si/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7mzw-a8si/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7mzw-a8si/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/7mzw-a8si/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7mzw-a8si/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7mzw-a8si/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/7mzw-a8si/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7mzw-a8si/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7mzw-a8si/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/7mzw-a8si",
+            "issued": "2024-11-04",
+            "keyword": [
+                "air",
+                "exports",
+                "imports",
+                "ports"
+            ],
+            "landingPage": "https://data.transportation.gov/d/7mzw-a8si",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-11-04",
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
+            "title": "U.S. Imports and Exports Value by Year and Mode 2003 thru 2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/7n6a-n5tz",
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
-            "identifier": "https://data.transportation.gov/api/views/7n6a-n5tz",
             "description": "Autos include all passenger cars, including station wagons. The U.S. Bureau of Economic Analysis releases auto and truck sales data, which are used in the preparation of estimates of personal consumption expenditures.",
-            "title": "Auto Sales",
+            "identifier": "https://data.transportation.gov/api/views/7n6a-n5tz",
+            "issued": "2025-01-02",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/7n6a-n5tz",
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
+            "title": "Auto Sales"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "ftp://ftp.nhtsa.dot.gov/Nits",
+            "agencyProgramURL": "http://www.nhtsa.gov/Data/State+Data+Programs",
+            "analysisUnit": "vehicle crash",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/7n7q-wu48",
-            "issued": "2009-01-27",
-            "temporal": "2008-01-01/2010-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "FARS/GES/NiTS Micro-Computer Data Entry System (MDE)",
-            "references": [
-                "http://www-nrd.nhtsa.dot.gov/Cats/listpublications.aspx%3FId=233&ShowBy=Category"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/Cats/listpublications.aspx%3FId=233&ShowBy=Category",
+            "description": "The Not-in-Traffic Surveillance (NiTS) system is a virtual data collection system designed to provide counts and details regarding fatalities and injuries that occur in non-traffic crashes and in non-crash incidents. NiTS non-traffic crash data is obtained through NHTSA's National Automotive Sampling System, General Estimates System (NASS GES) and the Fatality Analysis Reporting System (FARS). NiTS non-crash injury data is based upon emergency department records from a special study conducted by the Consumer Product Safety Commission's National Electronic Injury Surveillance System (NEISS) All Injury Program. NiTS non-crash fatality data is derived from death certificate information from the Centers for Disease Control's National Vital Statistics System.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/nits",
+                    "mediaType": "text/html",
+                    "title": "Browse FTP site"
+                }
             ],
+            "identifier": "288.5",
+            "isPartOf": "DOT-288",
+            "issued": "2009-01-27",
             "keyword": [
                 "crash",
                 "death",
@@ -20444,77 +20460,79 @@
                 "vehicle",
                 "victim"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "288.5",
+            "landingPage": "https://data.transportation.gov/d/7n7q-wu48",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-5391",
+            "programCode": [
+                "021:032"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Highway Traffic Safety Administration"
             },
-            "description": "The Not-in-Traffic Surveillance (NiTS) system is a virtual data collection system designed to provide counts and details regarding fatalities and injuries that occur in non-traffic crashes and in non-crash incidents. NiTS non-traffic crash data is obtained through NHTSA's National Automotive Sampling System, General Estimates System (NASS GES) and the Fatality Analysis Reporting System (FARS). NiTS non-crash injury data is based upon emergency department records from a special study conducted by the Consumer Product Safety Commission's National Electronic Injury Surveillance System (NEISS) All Injury Program. NiTS non-crash fatality data is derived from death certificate information from the Centers for Disease Control's National Vital Statistics System.",
-            "title": "Not in Traffic Surveillance (NiTS) - Browse FTP site",
-            "isPartOf": "DOT-288",
-            "agencyProgramURL": "http://www.nhtsa.gov/Data/State+Data+Programs",
-            "programCode": [
-                "021:032"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/nits",
-                    "mediaType": "text/html",
-                    "title": "Browse FTP site"
-                }
+            "references": [
+                "http://www-nrd.nhtsa.dot.gov/Cats/listpublications.aspx%3FId=233&ShowBy=Category"
             ],
             "spatial": "United States of America",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/Cats/listpublications.aspx%3FId=233&ShowBy=Category",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "ftp://ftp.nhtsa.dot.gov/Nits",
+            "temporal": "2008-01-01/2010-12-31",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "analysisUnit": "vehicle crash",
-            "phone": "202-366-5391",
-            "language": [
-                "en-US"
-            ]
+            "title": "Not in Traffic Surveillance (NiTS) - Browse FTP site"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/7ndw-2t3r",
-            "issued": "2021-05-17",
             "@type": "dcat:Dataset",
-            "modified": "2024-03-18",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sean Jahanmir",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/7ndw-2t3r",
+            "issued": "2021-05-17",
+            "landingPage": "https://data.transportation.gov/d/7ndw-2t3r",
+            "modified": "2024-03-18",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Performance"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/7ni3-gdc4",
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
+                    "description": "2013 Iowa HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/iowa2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Iowa"
+                }
+            ],
+            "identifier": "678.119",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -20528,60 +20546,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.119",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Iowa",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/7ni3-gdc4",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/iowa2013.zip",
-                    "description": "2013 Iowa HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Iowa"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Iowa"
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
-            "landingPage": "https://data.transportation.gov/d/7nmu-bsvv",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/13maytvt/13maytvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "May 2013"
+                }
             ],
+            "identifier": "18.50",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -20591,60 +20606,61 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.50",
+            "landingPage": "https://data.transportation.gov/d/7nmu-bsvv",
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
-            "title": "Monthly Traffic Volume Trends - May 2013",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/13maytvt/13maytvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "May 2013"
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
+            "title": "Monthly Traffic Volume Trends - May 2013"
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
-            "landingPage": "https://data.transportation.gov/d/7p7r-tcww",
-            "issued": "2008-02-01",
-            "temporal": "2008-01-01/2015-04-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.nhtsa.gov/DOT/NHTSA/Communication%20&%20Consumer%20Information/Articles/CPS%20files/faq.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www.safercar.gov/parents/CarSeats/Car-Seat-Glossary-of-Terms.htm",
+            "description": "To assist consumers purchasing child safety seats, NHTSA has rated car seats which meet Federal Safety Standards and strict crash performance standards. While all rates seats are safe, they do differ in their ease of use in the following four basic categories: Evaluation of Instructions, Evaluation of Labels, Vehicle Installation Features, Securing the Child",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.nhtsa.gov/nhtsa_eou/info.jsp%3Ftype=all",
+                    "mediaType": "text/html",
+                    "title": "Child Safety Seat Ease of Use Ratings"
+                }
             ],
+            "identifier": "2.1",
+            "isPartOf": "DOT-2",
+            "issued": "2008-02-01",
             "keyword": [
                 "child",
                 "css",
@@ -20654,61 +20670,58 @@
                 "safety",
                 "seat"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "2.1",
+            "landingPage": "https://data.transportation.gov/d/7p7r-tcww",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-493-0188",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Highway Traffic Safety Administration"
             },
-            "description": "To assist consumers purchasing child safety seats, NHTSA has rated car seats which meet Federal Safety Standards and strict crash performance standards. While all rates seats are safe, they do differ in their ease of use in the following four basic categories: Evaluation of Instructions, Evaluation of Labels, Vehicle Installation Features, Securing the Child",
-            "title": "Child Safety Seat Ease of Use Rating - Child Safety Seat Ease of Use Ratings",
-            "isPartOf": "DOT-2",
-            "agencyProgramURL": "http://www.safercar.gov/parents/CarSeats/Car-Seat-Safety.htm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.nhtsa.gov/nhtsa_eou/info.jsp%3Ftype=all",
-                    "mediaType": "text/html",
-                    "title": "Child Safety Seat Ease of Use Ratings"
-                }
+            "references": [
+                "http://www.nhtsa.gov/DOT/NHTSA/Communication%20&%20Consumer%20Information/Articles/CPS%20files/faq.pdf"
             ],
             "spatial": "N/A",
-            "describedBy": "http://www.safercar.gov/parents/CarSeats/Car-Seat-Glossary-of-Terms.htm",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.safercar.gov/parents/Car-Seat-Safety.htm",
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
+            "agencyProgramURL": "https://www.transportation.gov/transportation-health-tool",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/7pkz-zbs6",
-            "issued": "2015-10-26",
-            "temporal": "2013-01-01/2015-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "https://www.transportation.gov/mission/health/indicator-profiles"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.transportation.gov/mission/health/indicator-profiles",
+            "description": "The Transportation and Health Tool (THT) was developed by the U.S. Department of Transportation and the Centers for Disease Control and Prevention to provide easy access to data that practitioners can use to examine the health impacts of transportation systems. The tool provides data on a set of transportation and public health indicators for each U.S. state and metropolitan area that describe how the transportation environment affects safety, active transportation, air quality, and connectivity to destinations. You can use the tool to quickly see how your state or metropolitan area compares with others in addressing key transportation and health issues. It also provides information and resources to help agencies better understand the links between transportation and health and to identify strategies to improve public health through transportation planning and policy.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.transportation.gov/sites/dot.gov/files/docs/THT_Data_508.xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Data"
+                }
             ],
+            "identifier": "1860.0",
+            "issued": "2015-10-26",
             "keyword": [
                 "affordability",
                 "bicycle",
@@ -20723,56 +20736,57 @@
                 "transportation",
                 "travel"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "1860.0",
+            "landingPage": "https://data.transportation.gov/d/7pkz-zbs6",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-08",
+            "programCode": [
+                "021:058"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Secretary of Transportation"
             },
-            "description": "The Transportation and Health Tool (THT) was developed by the U.S. Department of Transportation and the Centers for Disease Control and Prevention to provide easy access to data that practitioners can use to examine the health impacts of transportation systems. The tool provides data on a set of transportation and public health indicators for each U.S. state and metropolitan area that describe how the transportation environment affects safety, active transportation, air quality, and connectivity to destinations. You can use the tool to quickly see how your state or metropolitan area compares with others in addressing key transportation and health issues. It also provides information and resources to help agencies better understand the links between transportation and health and to identify strategies to improve public health through transportation planning and policy.",
-            "title": "Transportation and Health Tool - Data",
-            "agencyProgramURL": "https://www.transportation.gov/transportation-health-tool",
-            "programCode": [
-                "021:058"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.transportation.gov/sites/dot.gov/files/docs/THT_Data_508.xlsx",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "Data"
-                }
+            "references": [
+                "https://www.transportation.gov/mission/health/indicator-profiles"
             ],
-            "describedBy": "https://www.transportation.gov/mission/health/indicator-profiles",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "temporal": "2013-01-01/2015-12-31",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "language": [
-                "en-US"
-            ]
+            "title": "Transportation and Health Tool - Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/SafetyProgram/RoadsideInspections.aspx",
+            "agencyProgramURL": "http://www.fmcsa.dot.gov/safety-security/grants/MCSAP-Basic-Incentive/index.aspx",
+            "analysisUnit": "Motor Carrier, Driver, Vehicle,",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/7qiy-7ws9",
-            "issued": "2011-09-14",
-            "temporal": "2009-01-01/2013-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Data are collected at the roadside, primarily through FMCSA-provided ASPEN software used to conduct roadside inspections.  The inspections are uploaded from State SAFETYNET systems into FMCSA's MCMIS database.",
-            "references": [
-                "http://ai.fmcsa.dot.gov/InfoCenter/Default.aspx#question402"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Contains data on roadside inspections of large trucks and buses, including violations discovered. The majority of this information comes from state police jurisdictions to FMCSA, although some Federally-conducted inspections are also included.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://ai.fmcsa.dot.gov/SafetyProgram/RoadsideInspections.aspx",
+                    "mediaType": "text/html",
+                    "title": "Data Mining Tool"
+                }
             ],
+            "identifier": "DOT-94",
+            "issued": "2011-09-14",
             "keyword": [
                 "bus",
                 "federal motor carrier safety administration",
@@ -20784,86 +20798,88 @@
                 "roadside inspections",
                 "truck"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "DOT-94",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
-            "description": "Contains data on roadside inspections of large trucks and buses, including violations discovered. The majority of this information comes from state police jurisdictions to FMCSA, although some Federally-conducted inspections are also included.",
-            "title": "Motor Carrier Inspections",
-            "agencyProgramURL": "http://www.fmcsa.dot.gov/safety-security/grants/MCSAP-Basic-Incentive/index.aspx",
+            "landingPage": "https://data.transportation.gov/d/7qiy-7ws9",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-24",
+            "phone": "202-366-4869",
             "primaryITInvestmentUII": "021-155552608",
             "programCode": [
                 "021:000"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://ai.fmcsa.dot.gov/SafetyProgram/RoadsideInspections.aspx",
-                    "mediaType": "text/html",
-                    "title": "Data Mining Tool"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "references": [
+                "http://ai.fmcsa.dot.gov/InfoCenter/Default.aspx#question402"
             ],
             "spatial": "National, State and county.",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/SafetyProgram/RoadsideInspections.aspx",
+            "temporal": "2009-01-01/2013-12-31",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Motor Carrier, Driver, Vehicle,",
-            "phone": "202-366-4869",
-            "language": [
-                "en-US"
-            ]
+            "title": "Motor Carrier Inspections"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/7qsd-4a2n",
-            "issued": "2024-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-31",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:answers@bts.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/7qsd-4a2n",
             "description": "The Great Lakes St. Lawrence Seaway\u2019s navigation season generally begins in late March and closes in late December. Opening and closing dates vary from year to year.",
-            "title": "Great Lakes St. Lawrence Seaway Vessel Transits",
+            "identifier": "https://data.transportation.gov/api/views/7qsd-4a2n",
+            "issued": "2024-12-31",
+            "landingPage": "https://data.transportation.gov/d/7qsd-4a2n",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-12-31",
             "programCode": [
                 "021:053"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Great Lakes St. Lawrence Seaway Vessel Transits"
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
-            "landingPage": "https://data.transportation.gov/d/7rsi-ixkw",
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
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2002NTDxls.exe",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2002 Database"
+                }
             ],
+            "identifier": "21.6",
+            "isPartOf": "DOT-21",
+            "issued": "2010-10-01",
             "keyword": [
                 "agency",
                 "allocation",
@@ -20882,59 +20898,55 @@
                 "urbanized",
                 "vehicles"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John D. Giorgis",
-                "hasEmail": "mailto:john.giorgis@dot.gov"
-            },
-            "identifier": "21.6",
+            "landingPage": "https://data.transportation.gov/d/7rsi-ixkw",
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
-            "title": "NTD Annual Module Data Set - 2002 Database",
-            "isPartOf": "DOT-21",
-            "agencyProgramURL": "http://www.ntdprogram.gov",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2002NTDxls.exe",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "2002 Database"
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
+            "title": "NTD Annual Module Data Set - 2002 Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Access restricted under the Privacy Act of 1974; see Privacy Impact Assessment at https://www.dot.gov/citizens/privacy/pia-case-tracking-system-cts.",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/7s7t-68xh",
-            "issued": "2014-09-24",
-            "temporal": "R/2014-09-24/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DOT Socrata",
+                "hasEmail": "mailto:Socrata@dot.gov"
+            },
+            "dataQuality": false,
+            "description": "This data set contains information on hearings conducted for the Department of Transportation or its modal administrations by administrative law judges in accordance with the Administrative Procedure Act APA and/or other statutes or regulations.  The data include identifying information for each case, including titles, docket numbers, original case numbers, and Federal Docket Management System (FDMS) numbers, as well as information about counsel; unrepresented parties; assigned judges, attorneys, and interns; filings; and dates of significant events. Documents for which public dissemination is not prohibited are available through FDMS at http://www.regulations.gov/.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.transportation.gov/mission/data-inventory-not-available",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "457.0",
+            "issued": "2014-09-24",
             "keyword": [
                 "administrative law judge",
                 "air carrier",
@@ -20953,55 +20965,57 @@
                 "regulatory compliance",
                 "travel agent"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DOT Socrata",
-                "hasEmail": "mailto:Socrata@dot.gov"
-            },
-            "identifier": "457.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
-            "description": "This data set contains information on hearings conducted for the Department of Transportation or its modal administrations by administrative law judges in accordance with the Administrative Procedure Act APA and/or other statutes or regulations.  The data include identifying information for each case, including titles, docket numbers, original case numbers, and Federal Docket Management System (FDMS) numbers, as well as information about counsel; unrepresented parties; assigned judges, attorneys, and interns; filings; and dates of significant events. Documents for which public dissemination is not prohibited are available through FDMS at http://www.regulations.gov/.",
-            "title": "Office of Hearings Case Tracking Data -",
+            "landingPage": "https://data.transportation.gov/d/7s7t-68xh",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-14",
+            "phone": "202-366-0437",
             "primaryITInvestmentUII": "021-014134515",
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
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "rights": "Access restricted under the Privacy Act of 1974; see Privacy Impact Assessment at https://www.dot.gov/citizens/privacy/pia-case-tracking-system-cts.",
+            "temporal": "R/2014-09-24/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-0437"
+            "title": "Office of Hearings Case Tracking Data -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://li-public.fmcsa.dot.gov/LIVIEW/pkg_oos_process.prc_oos_search",
+            "agencyProgramURL": "http://li-public.fmcsa.dot.gov/LIVIEW/pkg_oos_process.prc_oos_search",
+            "analysisUnit": "Out of Service Motor Carriers",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/7tvk-w6cf",
-            "issued": "2000-01-01",
-            "temporal": "R/1974-06-01/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://li-public.fmcsa.dot.gov/LIVIEW/pkg_oos_process.prc_oos_search"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Searchable list of carriers currently issued Out of Service Orders by the Federal Motor Carrier Safety Administration.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://li-public.fmcsa.dot.gov/LIVIEW/pkg_oos_process.prc_oos_search",
+                    "mediaType": "text/html",
+                    "title": "FMCSA Out of Service Orders"
+                }
             ],
+            "identifier": "DOT-124",
+            "issued": "2000-01-01",
             "keyword": [
                 "90 day failure to pay.",
                 "bus",
@@ -21020,59 +21034,60 @@
                 "safety and fitness electronic records",
                 "unsatifactory = unfit"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "DOT-124",
+            "landingPage": "https://data.transportation.gov/d/7tvk-w6cf",
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
-            "description": "Searchable list of carriers currently issued Out of Service Orders by the Federal Motor Carrier Safety Administration.",
-            "title": "SAFER - Out of Service Orders",
-            "agencyProgramURL": "http://li-public.fmcsa.dot.gov/LIVIEW/pkg_oos_process.prc_oos_search",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://li-public.fmcsa.dot.gov/LIVIEW/pkg_oos_process.prc_oos_search",
-                    "mediaType": "text/html",
-                    "title": "FMCSA Out of Service Orders"
-                }
+            "references": [
+                "http://li-public.fmcsa.dot.gov/LIVIEW/pkg_oos_process.prc_oos_search"
             ],
             "spatial": "Business address",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://li-public.fmcsa.dot.gov/LIVIEW/pkg_oos_process.prc_oos_search",
+            "temporal": "R/1974-06-01/P1D",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "analysisUnit": "Out of Service Motor Carriers",
-            "categoryDesignation": "Administrative",
-            "phone": "202-493-0215",
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFER - Out of Service Orders"
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
-            "landingPage": "https://data.transportation.gov/d/7tzw-z7mc",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/05maytvt/05maytvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "May 2005"
+                }
             ],
+            "identifier": "18.112",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -21082,60 +21097,60 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.112",
+            "landingPage": "https://data.transportation.gov/d/7tzw-z7mc",
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
-            "title": "Monthly Traffic Volume Trends - May 2005",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/05maytvt/05maytvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "May 2005"
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
+            "title": "Monthly Traffic Volume Trends - May 2005"
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
-            "landingPage": "https://data.transportation.gov/d/7w5b-q5mj",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/03juntvt/tvtjun03.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "June 2003"
+                }
             ],
+            "identifier": "18.135",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -21145,57 +21160,60 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.135",
+            "landingPage": "https://data.transportation.gov/d/7w5b-q5mj",
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
-            "title": "Monthly Traffic Volume Trends - June 2003",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/03juntvt/tvtjun03.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "June 2003"
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
+            "title": "Monthly Traffic Volume Trends - June 2003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://www.safercar.gov/Vehicle+Shoppers/Tires+Rating",
+            "agencyProgramURL": "http://www.safercar.gov/tires/index.html",
+            "analysisUnit": "Tires",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/7wch-zrff",
-            "issued": "2009-10-29",
-            "temporal": "R/2009-10-29/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "To assist consumers purchasing new vehicles or replacement tires, NHTSA has rated more than 2,400 lines of tires, including most used on passenger cars, minivans, SUVs and light pickup trucks using a grading system known as the Uniform Tire Quality Grading System (UTQGS). UTQGS allows consumers to compare tire tread wear, traction performance and temperature resistance.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.safercar.gov/Vehicle+Shoppers/Tires+Rating",
+                    "mediaType": "text/html",
+                    "title": "Tire Rating Lookup"
+                }
+            ],
+            "identifier": "4.2",
+            "isPartOf": "DOT-4",
+            "issued": "2009-10-29",
             "keyword": [
                 "grading",
                 "quality",
@@ -21207,104 +21225,63 @@
                 "uniform",
                 "utqgs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "4.2",
+            "landingPage": "https://data.transportation.gov/d/7wch-zrff",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-0307",
+            "programCode": [
+                "021:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Highway Traffic Safety Administration"
             },
-            "description": "To assist consumers purchasing new vehicles or replacement tires, NHTSA has rated more than 2,400 lines of tires, including most used on passenger cars, minivans, SUVs and light pickup trucks using a grading system known as the Uniform Tire Quality Grading System (UTQGS). UTQGS allows consumers to compare tire tread wear, traction performance and temperature resistance.",
-            "title": "Uniform Tire Quality Grading System (UTQGS) - Tire Rating Lookup",
-            "isPartOf": "DOT-4",
-            "agencyProgramURL": "http://www.safercar.gov/tires/index.html",
-            "programCode": [
-                "021:031"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.safercar.gov/Vehicle+Shoppers/Tires+Rating",
-                    "mediaType": "text/html",
-                    "title": "Tire Rating Lookup"
-                }
-            ],
             "spatial": "N/A",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.safercar.gov/Vehicle+Shoppers/Tires+Rating",
+            "temporal": "R/2009-10-29/P1D",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "analysisUnit": "Tires",
-            "categoryDesignation": "Research",
-            "phone": "202-366-0307",
-            "language": [
-                "en-US"
-            ]
+            "title": "Uniform Tire Quality Grading System (UTQGS) - Tire Rating Lookup"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/7wgr-qwgb",
-            "issued": "2021-05-21",
             "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/7wgr-qwgb",
+            "issued": "2021-05-21",
+            "landingPage": "https://data.transportation.gov/d/7wgr-qwgb",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-05-21",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
-            "title": "Wyoming Connected Vehicle Pilot Basic Safety Message Visualization",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "Wyoming Connected Vehicle Pilot Basic Safety Message Visualization"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/7wn6-i5b9",
             "bureauCode": [
                 "021:27"
             ],
-            "issued": "2023-06-21",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
-            "keyword": [
-                "accident",
-                "form 57",
-                "grade crossing",
-                "grade crossing incident",
-                "highway-rail",
-                "highway-rail grade crossing",
-                "highway-rail incident",
-                "incident",
-                "incidents"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Railroad Safety",
                 "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Railroad Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/7wn6-i5b9",
+            "dataQuality": true,
             "description": "This dataset is in a user-friendly human-readable format. To download the source dataset that contains raw data values, go here: https://data.transportation.gov/dataset/Form57-Source-Table/icqf-xf4w.",
-            "title": "Highway-Rail Grade Crossing Incident Data (Form 57)",
-            "programCode": [
-                "021:036"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21312,49 +21289,87 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/7wn6-i5b9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7wn6-i5b9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7wn6-i5b9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/7wn6-i5b9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7wn6-i5b9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7wn6-i5b9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/7wn6-i5b9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7wn6-i5b9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7wn6-i5b9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
-            "theme": [
-                "Railroads"
-            ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "bureauCode": [
-                "021:17"
+            "identifier": "https://data.transportation.gov/api/views/7wn6-i5b9",
+            "issued": "2023-06-21",
+            "keyword": [
+                "accident",
+                "form 57",
+                "grade crossing",
+                "grade crossing incident",
+                "highway-rail",
+                "highway-rail grade crossing",
+                "highway-rail incident",
+                "incident",
+                "incidents"
             ],
-            "landingPage": "https://data.transportation.gov/d/7wzc-z4zr",
-            "issued": "2011-09-14",
-            "temporal": "2009-01-01/2013-12-31",
+            "landingPage": "https://data.transportation.gov/d/7wn6-i5b9",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-02-01",
+            "programCode": [
+                "021:036"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Railroad Administration"
+            },
+            "theme": [
+                "Railroads"
+            ],
+            "title": "Highway-Rail Grade Crossing Incident Data (Form 57)"
+        },
+        {
             "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/SafetyProgram/RoadsideInspections.aspx",
+            "agencyProgramURL": "http://www.fmcsa.dot.gov/safety-security/grants/MCSAP-Basic-Incentive/index.aspx",
+            "analysisUnit": "Motor Carrier, Driver, Vehicle,",
+            "bureauCode": [
+                "021:17"
+            ],
+            "categoryDesignation": "Research",
             "collectionInstrument": "Data are collected at the roadside, primarily through FMCSA-provided ASPEN software used to conduct roadside inspections.  The inspections are uploaded from State SAFETYNET systems into FMCSA's MCMIS database.",
-            "references": [
-                "http://ai.fmcsa.dot.gov/InfoCenter/Default.aspx#question402"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Contains data on roadside inspections of large trucks and buses, including violations discovered. The majority of this information comes from state police jurisdictions to FMCSA, although some Federally-conducted inspections are also included.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://ai.fmcsa.dot.gov/SafetyProgram/RoadsideInspections.aspx",
+                    "mediaType": "text/html",
+                    "title": "Data Mining Tool"
+                }
             ],
+            "identifier": "94.1",
+            "isPartOf": "DOT-94",
+            "issued": "2011-09-14",
             "keyword": [
                 "bus",
                 "federal motor carrier safety administration",
@@ -21366,88 +21381,45 @@
                 "roadside inspections",
                 "truck"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "94.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
-            "description": "Contains data on roadside inspections of large trucks and buses, including violations discovered. The majority of this information comes from state police jurisdictions to FMCSA, although some Federally-conducted inspections are also included.",
-            "title": "Motor Carrier Inspections - Data Mining Tool",
-            "isPartOf": "DOT-94",
-            "agencyProgramURL": "http://www.fmcsa.dot.gov/safety-security/grants/MCSAP-Basic-Incentive/index.aspx",
+            "landingPage": "https://data.transportation.gov/d/7wzc-z4zr",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-24",
+            "phone": "202-366-4869",
             "primaryITInvestmentUII": "021-155552608",
             "programCode": [
                 "021:000"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://ai.fmcsa.dot.gov/SafetyProgram/RoadsideInspections.aspx",
-                    "mediaType": "text/html",
-                    "title": "Data Mining Tool"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "references": [
+                "http://ai.fmcsa.dot.gov/InfoCenter/Default.aspx#question402"
             ],
             "spatial": "National, State and county.",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/SafetyProgram/RoadsideInspections.aspx",
+            "temporal": "2009-01-01/2013-12-31",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Motor Carrier, Driver, Vehicle,",
-            "phone": "202-366-4869",
-            "language": [
-                "en-US"
-            ]
+            "title": "Motor Carrier Inspections - Data Mining Tool"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/7xqa-bpf3",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2018-12-13",
-            "@type": "dcat:Dataset",
-            "temporal": "2018-02-02/2018-08-03",
-            "modified": "2018-12-13",
-            "keyword": [
-                "application message",
-                "bus locations",
-                "cleveland",
-                "connected vehicle message",
-                "enhanced transit safety retrofit package (e-trp)",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "ohio",
-                "pedestrian detection",
-                "pedestrian in crosswalk warning (pcw)",
-                "roadside equipment (rse)",
-                "transit",
-                "transit signal priority (tsp)",
-                "vehicle turning right in front of bus warning (vtrw)"
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
-            "identifier": "https://data.transportation.gov/api/views/7xqa-bpf3",
+            "dataQuality": true,
             "description": "The\u00a0data\u00a0is\u00a0taken\u00a0from\u00a0three\u00a0intersections\u00a0and\u00a024\u00a0buses\u00a0over\u00a0a\u00a0six\u00a0month\u00a0period\u00a0in\u00a0Cleveland,\u00a0Ohio.\u00a0The\u00a0systems\u00a0at\u00a0the\u00a0intersections\u00a0provided\u00a0MAP\u00a0and\u00a0SPAT\u00a0messages\u00a0and\u00a0the\u00a0SPAT\u00a0message\u00a0contained\u00a0pedestrian\u00a0detections\u00a0from\u00a0a\u00a0series\u00a0of\u00a0cameras\u00a0at\u00a0the\u00a0intersection.\u00a0The\u00a0buses\u00a0received\u00a0these\u00a0messages\u00a0and\u00a0used\u00a0them\u00a0to\u00a0alert\u00a0the\u00a0vehicle\u00a0driver\u00a0when\u00a0pedestrians\u00a0were\u00a0about\u00a0to\u00a0enter\u00a0the\u00a0crosswalks\u00a0or\u00a0was\u00a0in\u00a0the\u00a0crosswalk.\u00a0The\u00a0buses\u00a0also\u00a0used\u00a0basic\u00a0safety\u00a0messages\u00a0from\u00a0external\u00a0vehicles\u00a0to\u00a0warn\u00a0the\u00a0driver\u00a0when\u00a0another\u00a0vehicle\u00a0had\u00a0the\u00a0potential\u00a0of\u00a0making\u00a0a\u00a0right\u00a0hand\u00a0turn\u00a0in\u00a0front\u00a0of\u00a0the\u00a0vehicle.\u00a0The\u00a0data\u00a0contains\u00a0bus\u00a0locations,\u00a0bus\u00a0state\u00a0changes,\u00a0pedestrian\u00a0detections\u00a0and\u00a0user\u00a0interface\u00a0state\u00a0changes.\u00a0",
-            "title": "Enhanced Transit Safety Retrofit Package (E-TRP)",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21455,70 +21427,83 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/7xqa-bpf3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7xqa-bpf3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7xqa-bpf3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/7xqa-bpf3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7xqa-bpf3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7xqa-bpf3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/7xqa-bpf3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7xqa-bpf3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7xqa-bpf3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Cleveland, Ohio",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/7xqa-bpf3",
+            "issued": "2018-12-13",
+            "keyword": [
+                "application message",
+                "bus locations",
+                "cleveland",
+                "connected vehicle message",
+                "enhanced transit safety retrofit package (e-trp)",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "ohio",
+                "pedestrian detection",
+                "pedestrian in crosswalk warning (pcw)",
+                "roadside equipment (rse)",
+                "transit",
+                "transit signal priority (tsp)",
+                "vehicle turning right in front of bus warning (vtrw)"
+            ],
+            "landingPage": "https://data.transportation.gov/d/7xqa-bpf3",
+            "language": [
+                "en-US"
+            ],
             "license": "http://creativecommons.org/licenses/by-sa/4.0/legalcode",
-            "accrualPeriodicity": "irregular",
+            "modified": "2018-12-13",
+            "programCode": [
+                "021:013"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
+            "spatial": "Cleveland, Ohio",
+            "temporal": "2018-02-02/2018-08-03",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Enhanced Transit Safety Retrofit Package (E-TRP)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://li.fmcsa.dot.gov/",
+            "agencyProgramURL": "http://li-public.fmcsa.dot.gov/",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/7xzn-4j4j",
-            "issued": "2018-12-17",
-            "temporal": "R/1974-06-01/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "driver insurance; carrier registration; carrier license"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO",
                 "hasEmail": "mailto:fmcsa.cdo@dot.gov"
             },
-            "identifier": "99.3",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": false,
             "description": "Data collected through FMCSA's Licensing and Insurance programs and information collections (BOC-3, OP-1, etc).",
-            "title": "Licensing and Insurance - QCMobile API",
-            "isPartOf": "DOT-99",
-            "agencyProgramURL": "http://li-public.fmcsa.dot.gov/",
-            "primaryITInvestmentUII": "021-000001001",
-            "programCode": [
-                "021:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21527,53 +21512,50 @@
                     "title": "QCMobile API"
                 }
             ],
-            "spatial": "Carrier, Driver",
-            "dataQuality": false,
+            "identifier": "99.3",
+            "isPartOf": "DOT-99",
+            "issued": "2018-12-17",
+            "keyword": [
+                "driver insurance; carrier registration; carrier license"
+            ],
+            "landingPage": "https://data.transportation.gov/d/7xzn-4j4j",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://li.fmcsa.dot.gov/",
+            "modified": "2024-05-24",
+            "phone": "202-366-3397",
+            "primaryITInvestmentUII": "021-000001001",
+            "programCode": [
+                "021:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "spatial": "Carrier, Driver",
+            "temporal": "R/1974-06-01/P1D",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "categoryDesignation": "Research",
-            "phone": "202-366-3397",
-            "language": [
-                "en-US"
-            ]
+            "title": "Licensing and Insurance - QCMobile API"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "The information is documented at the system level and may contain IT Security Sensitive information.",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/7y34-3m2p",
-            "issued": "2014-12-15",
-            "temporal": "R/2014-12-15/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-31",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "change request",
-                "configuration management",
-                "requirements"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO",
                 "hasEmail": "mailto:fmcsa.cdo@dot.gov"
             },
-            "identifier": "1641.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": true,
             "description": "IT Configuration Management: Borland Caliber is FMCSA's requirements management tool. It is a Client Server application, accessable internally and does not have a web",
-            "title": "CaliberRM -",
-            "primaryITInvestmentUII": "021-000001018",
-            "programCode": [
-                "021:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21581,54 +21563,53 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "1641.0",
+            "issued": "2014-12-15",
+            "keyword": [
+                "change request",
+                "configuration management",
+                "requirements"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Administrative",
+            "landingPage": "https://data.transportation.gov/d/7y34-3m2p",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-3397"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-31",
+            "phone": "202-366-3397",
+            "primaryITInvestmentUII": "021-000001018",
+            "programCode": [
+                "021:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "rights": "The information is documented at the system level and may contain IT Security Sensitive information.",
+            "temporal": "R/2014-12-15/P1Y",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "CaliberRM -"
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
-            "landingPage": "https://data.transportation.gov/d/7z89-339f",
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
-            "identifier": "692.31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - PM 10",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "primaryITInvestmentUII": "021-845083703",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21637,56 +21618,50 @@
                     "title": "PM 10"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.31",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/7z89-339f",
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
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - PM 10"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/7zjf-a4zf",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2024-11-04",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-24",
-            "keyword": [
-                "aerial videography",
-                "automated vehicles",
-                "human-automated vehicle interactions",
-                "infrastructure-based videography",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "multi-modal trajectories",
-                "tgsim",
-                "third generation simulation",
-                "vehicle trajectory data"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyungjun Park",
                 "hasEmail": "mailto:hyungjun.park@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/7zjf-a4zf",
             "description": "The main dataset is a 70 MB file of trajectory data (I294_L1_final.csv) that contains position, speed, and acceleration data for small and large automated (L1) vehicles and non-automated vehicles on a highway in a suburban environment. Supporting files include aerial reference images for ten distinct data collection \u201cRuns\u201d (I294_L1_RunX_with_lanes.png, where X equals 8, 18, and 20 for southbound runs and 1, 3, 7, 9, 11, 19, and 21 for northbound runs). Associated centerline files are also provided for each \u201cRun\u201d (I-294-L1-Run_X-geometry-with-ramps.csv). In each centerline file, x and y coordinates (in meters) marking each lane centerline are provided. The origin point of the reference image is located at the top left corner. Additionally, in each centerline file, an indicator variable is used for each lane to define the following types of road sections: 0=no ramp, 1=on-ramps, 2=off-ramps, and 3=weaving segments. The number attached to each column header is the numerical ID assigned for the specific lane (see \u201cTGSIM \u2013 Centerline Data Dictionary \u2013 I294 L1.csv\u201d for more details).  The dataset defines eight lanes (four lanes in each direction) using these centerline files. Images that map the lanes of interest to the numerical lane IDs referenced in the trajectory dataset are stored in the folder titled \u201cAnnotation on Regions.zip\u201d. The southbound lanes are shown visually in I294_L1_Lane-2.png through I294_L1_Lane-5.png and the northbound lanes are shown visually in I294_L1_Lane2.png through I294_L1_Lane5.png.\n\nThis dataset was collected as part of the Third Generation Simulation Data (TGSIM): A Closer Look at the Impacts of Automated Driving Systems on Human Behavior project. During the project, six trajectory datasets capable of characterizing human-automated vehicle interactions under a diverse set of scenarios in highway and city environments were collected and processed. For more information, see the project report found here: https://rosap.ntl.bts.gov/view/dot/74647.  This dataset, which is one of the six collected as part of the TGSIM project, contains data collected using one high-resolution 8K camera mounted on a helicopter that followed three SAE Level 1 ADAS-equipped vehicles with adaptive cruise control (ACC) enabled. The three vehicles manually entered the highway, moved to the second from left most lane, then enabled ACC with minimum following distance settings to initiate a string. The helicopter then followed the string of vehicles (which sometimes broke from the sting due to large following distances) northbound through the 4.8 km section of highway at an altitude of 300 meters. The goal of the data collection effort was to collect data related to human drivers' responses to vehicle strings. The road segment has four lanes in each direction and covers major on-ramp and an off-ramp in the southbound direction and one on-ramp in the northbound direction. The segment of highway is operated by Illinois Tollway and contains a high percentage of heavy vehicles. The camera captured footage during the evening rush hour (3:00 PM-5:00 PM CT) on a sunny day.\n\nAs part of this dataset, the following files were provided:\n<ul><li>I294_L1_final.csv contains the numerical data to be used for analysis that includes vehicle level trajectory data at every 0.1 second. Vehicle size (small or large), width, length, and whether the vehicle was one of the test vehicles with ACC engaged (\"yes\" or \"no\") are provided with instantaneous location, speed, and acceleration data. All distance measurements (width, length, location) were converted from pixels to meters using the following conversion factor: 1 pixel = 0.3-meter conversion.</li>\n<li>I294_L1_RunX_with_lanes.png are the aerial reference images that define the geographic region and associated roadway segments of interest (see bounding boxes on northbound and southbound lanes) for each run X.</li>\n<li>I-294-L1-Run_X-geometry-with-ramps.csv contain the coordinates that define the lane cent",
-            "title": "Third Generation Simulation Data (TGSIM) I-294 L1 Trajectories",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21694,69 +21669,75 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/7zjf-a4zf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7zjf-a4zf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7zjf-a4zf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/7zjf-a4zf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7zjf-a4zf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7zjf-a4zf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/7zjf-a4zf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/7zjf-a4zf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/7zjf-a4zf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "I-90/I94 in Chicago, IL; I-294 near Hinsdale, IL; I-395 in Washington DC; George Washington University Campus, Washington DC (Foggy Bottom)",
+            "identifier": "https://data.transportation.gov/api/views/7zjf-a4zf",
+            "issued": "2024-11-04",
+            "keyword": [
+                "aerial videography",
+                "automated vehicles",
+                "human-automated vehicle interactions",
+                "infrastructure-based videography",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "multi-modal trajectories",
+                "tgsim",
+                "third generation simulation",
+                "vehicle trajectory data"
+            ],
+            "landingPage": "https://data.transportation.gov/d/7zjf-a4zf",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-24",
+            "programCode": [
+                "021:042"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "spatial": "I-90/I94 in Chicago, IL; I-294 near Hinsdale, IL; I-395 in Washington DC; George Washington University Campus, Washington DC (Foggy Bottom)",
             "theme": [
                 "Automobiles"
-            ]
+            ],
+            "title": "Third Generation Simulation Data (TGSIM) I-294 L1 Trajectories"
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
-            "landingPage": "https://data.transportation.gov/d/823s-x24y",
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
-            "identifier": "692.25",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - Federal Lands",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "primaryITInvestmentUII": "021-845083703",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21765,56 +21746,56 @@
                     "title": "Federal Lands"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.25",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/823s-x24y",
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
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - Federal Lands"
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
-            "landingPage": "https://data.transportation.gov/d/82mn-8m73",
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
-            "identifier": "692.27",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - 8-Hour Ozone",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "primaryITInvestmentUII": "021-845083703",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21823,34 +21804,69 @@
                     "title": "8-Hour Ozone"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.27",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/82mn-8m73",
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
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - 8-Hour Ozone"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/",
+            "agencyProgramURL": "http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/",
+            "analysisUnit": "Region",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/833h-m7b4",
-            "issued": "2013-03-20",
-            "temporal": "2007-01-01/2040-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Forecast developed using commodity flow survey",
-            "references": [
-                "http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/faf3/userguide/index.htm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/faf3/userguide/index.htm#t5",
+            "description": "The Freight Analysis Framework (FAF) integrates data from a variety of sources to create a comprehensive picture of freight movement among states and major metropolitan areas by all modes of transportation. With data from the 2007 Commodity Flow Survey and additional sources, FAF version 3 (FAF3) provides estimates for tonnage, value, and domestic ton-miles by region of origin and destination, commodity type, and mode for 2007, the most recent year, and forecasts through 2040. Also included are state-to-state flows for these years plus 1997 and 2002, summary statistics, and flows by truck assigned to the highway network for 2007 and 2040.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/faf3/netwkdbflow/network/esri/faf3_4_esri.zip",
+                    "mediaType": "application/zip",
+                    "title": "Network"
+                }
             ],
+            "identifier": "286.3",
+            "isPartOf": "DOT-286",
+            "issued": "2013-03-20",
             "keyword": [
                 "commodity",
                 "consumption",
@@ -21875,111 +21891,78 @@
                 "value",
                 "wear"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "286.3",
+            "landingPage": "https://data.transportation.gov/d/833h-m7b4",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-6993",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "The Freight Analysis Framework (FAF) integrates data from a variety of sources to create a comprehensive picture of freight movement among states and major metropolitan areas by all modes of transportation. With data from the 2007 Commodity Flow Survey and additional sources, FAF version 3 (FAF3) provides estimates for tonnage, value, and domestic ton-miles by region of origin and destination, commodity type, and mode for 2007, the most recent year, and forecasts through 2040. Also included are state-to-state flows for these years plus 1997 and 2002, summary statistics, and flows by truck assigned to the highway network for 2007 and 2040.",
-            "title": "Freight Analysis Framework - Network",
-            "isPartOf": "DOT-286",
-            "agencyProgramURL": "http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/faf3/netwkdbflow/network/esri/faf3_4_esri.zip",
-                    "mediaType": "application/zip",
-                    "title": "Network"
-                }
+            "references": [
+                "http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/faf3/userguide/index.htm"
             ],
             "spatial": "Region. Domestic regions are defined here: http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/faf3/userguide/index.htm#t3 and foreign regions are defined here: http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/faf3/userguide/index.htm#t4",
-            "describedBy": "http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/faf3/userguide/index.htm#t5",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/",
+            "temporal": "2007-01-01/2040-12-31",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Region",
-            "phone": "202-366-6993",
-            "language": [
-                "en-US"
-            ]
+            "title": "Freight Analysis Framework - Network"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/84xd-726c",
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
-            "identifier": "https://data.transportation.gov/api/views/84xd-726c",
             "description": "Employed persons include people aged 16 years and older in the civilian noninstitutional population who did any work at all as paid employees; worked in their own business, profession, or on their own farm, or worked 15 hours or more as unpaid workers in an enterprise operated by a member of the family; and all those who were not working but who had jobs or businesses from which they were temporarily absent. The Bureau of Labor Statistics produces industry estimates of nonfarm payroll employment as part of the Current Population Survey.",
-            "title": "Transportation Employment - Water Transportation",
+            "identifier": "https://data.transportation.gov/api/views/84xd-726c",
+            "issued": "2025-01-02",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/84xd-726c",
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
+            "title": "Transportation Employment - Water Transportation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/85tf-25kj",
             "bureauCode": [
                 "021:27"
             ],
-            "issued": "2023-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
-            "keyword": [
-                "accident",
-                "form 54",
-                "rail equipment"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Railroad Safety",
                 "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Railroad Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/85tf-25kj",
+            "dataQuality": true,
             "description": "This dataset is in a user-friendly human-readable format. To download the source dataset that contains raw data values, go here: https://data.transportation.gov/dataset/Form-54-Source-Table/aqxq-n5hy.",
-            "title": "Rail Equipment Accident/Incident Data (Form 54)",
-            "programCode": [
-                "021:036"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21987,54 +21970,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/85tf-25kj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/85tf-25kj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/85tf-25kj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/85tf-25kj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/85tf-25kj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/85tf-25kj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/85tf-25kj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/85tf-25kj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/85tf-25kj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/85tf-25kj",
+            "issued": "2023-07-19",
+            "keyword": [
+                "accident",
+                "form 54",
+                "rail equipment"
+            ],
+            "landingPage": "https://data.transportation.gov/d/85tf-25kj",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-02-01",
+            "programCode": [
+                "021:036"
+            ],
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
+            "title": "Rail Equipment Accident/Incident Data (Form 54)"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/86nm-kdaj",
-            "issued": "2023-11-08",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/86nm-kdaj",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "US States",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22042,45 +22032,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/86nm-kdaj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/86nm-kdaj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/86nm-kdaj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/86nm-kdaj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/86nm-kdaj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/86nm-kdaj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/86nm-kdaj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/86nm-kdaj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/86nm-kdaj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/86nm-kdaj",
+            "issued": "2023-11-08",
+            "landingPage": "https://data.transportation.gov/d/86nm-kdaj",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "US States"
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
-            "landingPage": "https://data.transportation.gov/d/86zz-ue7u",
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
+                    "downloadURL": "http://www.nhtsa.gov/webapi/",
+                    "mediaType": "application/jsv",
+                    "title": "NHTSA API"
+                }
             ],
+            "identifier": "83.5",
+            "isPartOf": "DOT-83",
+            "issued": "2002-12-16",
             "keyword": [
                 "air bag",
                 "air bags",
@@ -22107,73 +22124,43 @@
                 "vin",
                 "vin search"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "83.5",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Manufacturers who determine that a product or piece of original equipment either has a safety defect or is not in compliance with Federal safety standards are required to notify the National Highway Traffic Safety Administration (NHTSA) within 5 business days. NHTSA requires that manufacturers file a Defect and Noncompliance report as well as quarterly recall status reports, in compliance with Federal Regulation 49 (the National Traffic and Motor Safety Act) Part 573, which identifies the requirements for safety recalls. This information is stored in the NHTSA database. Use this data to search for recall information related to:-\tSpecific NHTSA campaigns -\tProduct types Access to public searches of NHTSA recall databases for tires, vehicles, car seats and equipment.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - NHTSA API",
-            "isPartOf": "DOT-83",
-            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
-            "describedByType": "text/plain",
+            "landingPage": "https://data.transportation.gov/d/86zz-ue7u",
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
-                    "downloadURL": "http://www.nhtsa.gov/webapi/",
-                    "mediaType": "application/jsv",
-                    "title": "NHTSA API"
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
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - NHTSA API"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/876r-jsdb",
             "bureauCode": [
                 "021:17"
             ],
-            "issued": "2024-04-26",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
-            "keyword": [
-                "inspection"
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
-            "identifier": "https://data.transportation.gov/api/views/876r-jsdb",
             "description": "The report includes inspections involving violations of the FMCSR or HRM.",
-            "title": "Vehicle Inspections and Violations",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22181,49 +22168,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/876r-jsdb/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/876r-jsdb/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/876r-jsdb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/876r-jsdb/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/876r-jsdb/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/876r-jsdb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/876r-jsdb/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/876r-jsdb/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/876r-jsdb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/876r-jsdb",
+            "issued": "2024-04-26",
+            "keyword": [
+                "inspection"
+            ],
+            "landingPage": "https://data.transportation.gov/d/876r-jsdb",
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
+            "title": "Vehicle Inspections and Violations"
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
-            "landingPage": "https://data.transportation.gov/d/88h9-x6pz",
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
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/gxrtop50.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Frequency of Crossing Collisions"
+                }
             ],
+            "identifier": "214.10",
+            "isPartOf": "DOT-214",
+            "issued": "2010-09-29",
             "keyword": [
                 "accident",
                 "casualty",
@@ -22236,109 +22252,73 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "214.10",
+            "landingPage": "https://data.transportation.gov/d/88h9-x6pz",
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
-            "title": "Highway Rail Accidents - Frequency of Crossing Collisions",
-            "isPartOf": "DOT-214",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/gxrtop50.aspx",
-                    "mediaType": "text/csv",
-                    "title": "Frequency of Crossing Collisions"
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
+            "title": "Highway Rail Accidents - Frequency of Crossing Collisions"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/88zh-3rqb",
-            "issued": "2024-02-02",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-22",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
+            "description": "National Bicycle Network",
             "identifier": "https://data.transportation.gov/api/views/88zh-3rqb",
+            "issued": "2024-02-02",
+            "landingPage": "https://data.transportation.gov/d/88zh-3rqb",
+            "modified": "2024-08-22",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "National Bicycle Network",
-            "title": "National Bicycle Network",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "National Bicycle Network"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "https://safetydata.fra.dot.gov/MasterWebService/publicapi",
+            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
+            "analysisUnit": "Individual Crossing",
             "bureauCode": [
                 "021:27"
             ],
-            "landingPage": "https://data.transportation.gov/d/8agx-fghd",
-            "issued": "2010-09-29",
-            "temporal": "R/1975-01-31/P1M",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "https://safetydata.fra.dot.gov/Gcis/UserManagement/Login.aspx",
-            "modified": "2024-10-09",
-            "references": [
-                "http://safetydata.fra.dot.gov/OfficeofSafety/Documents/GCIS%20Electronic%20Submissions%20Instructions.pdfhttps://safetydata.fra.dot.gov/MasterWebService/PublicApi/Develop/QuickStartGuide"
-            ],
-            "keyword": [
-                "acts of god",
-                "collisions",
-                "derailments",
-                "explosions",
-                "fires",
-                "rail"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Railroad Safety",
                 "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
             },
-            "identifier": "224.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Railroad Administration"
-            },
-            "description": "The entire National Highway-Rail Crossing Inventory is available in three separate downloadble files. There is a file of all current Public-at-Grade crossings. There is a file of all current Private and grade-separated crossings. There is also a file which contains about 10 years of archival records for all types of crossings.",
-            "title": "Highway-Rail Crossings Inventory Data - Crossing Inventory - Public Site",
-            "isPartOf": "DOT-224",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
+            "dataQuality": true,
+            "describedBy": "http://safetydata.fra.dot.gov/OfficeofSafety/Documents/GCIS%20Electronic%20Submissions%20Instructions.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "021:036"
-            ],
+            "description": "The entire National Highway-Rail Crossing Inventory is available in three separate downloadble files. There is a file of all current Public-at-Grade crossings. There is a file of all current Private and grade-separated crossings. There is also a file which contains about 10 years of archival records for all types of crossings.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22347,55 +22327,88 @@
                     "title": "Crossing Inventory - Public Site"
                 }
             ],
-            "spatial": "Latitude/Longitude",
-            "describedBy": "http://safetydata.fra.dot.gov/OfficeofSafety/Documents/GCIS%20Electronic%20Submissions%20Instructions.pdf",
-            "dataQuality": true,
+            "identifier": "224.2",
+            "isPartOf": "DOT-224",
+            "issued": "2010-09-29",
+            "keyword": [
+                "acts of god",
+                "collisions",
+                "derailments",
+                "explosions",
+                "fires",
+                "rail"
+            ],
+            "landingPage": "https://data.transportation.gov/d/8agx-fghd",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "https://safetydata.fra.dot.gov/MasterWebService/publicapi",
+            "modified": "2024-10-09",
+            "phone": "202-493-6285",
+            "programCode": [
+                "021:036"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Railroad Administration"
+            },
+            "references": [
+                "http://safetydata.fra.dot.gov/OfficeofSafety/Documents/GCIS%20Electronic%20Submissions%20Instructions.pdfhttps://safetydata.fra.dot.gov/MasterWebService/PublicApi/Develop/QuickStartGuide"
+            ],
+            "spatial": "Latitude/Longitude",
+            "temporal": "R/1975-01-31/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Individual Crossing",
-            "phone": "202-493-6285",
-            "language": [
-                "en-US"
-            ]
+            "title": "Highway-Rail Crossings Inventory Data - Crossing Inventory - Public Site"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/8ara-8t8s",
-            "issued": "2021-05-12",
             "@type": "dcat:Dataset",
-            "modified": "2024-10-02",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sean Jahanmir",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/8ara-8t8s",
+            "issued": "2021-05-12",
+            "landingPage": "https://data.transportation.gov/d/8ara-8t8s",
+            "modified": "2024-10-02",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Moving Goods"
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
-            "landingPage": "https://data.transportation.gov/d/8az2-sgjk",
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
+            "identifier": "DOT-114",
+            "issued": "2018-12-17",
             "keyword": [
                 "a&i",
                 "a&i online",
@@ -22415,83 +22428,50 @@
                 "safety programs",
                 "traffic enforcement"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "DOT-114",
+            "landingPage": "https://data.transportation.gov/d/8az2-sgjk",
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
-            "title": "A&I - Safety Programs",
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
+            "title": "A&I - Safety Programs"
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
-            "landingPage": "https://data.transportation.gov/d/8chh-kqeq",
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
-            "identifier": "693.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
             "description": "The NBI System is the collection of bridge inspection information and costs associated with bridge replacements of structurally deficient bridges on and off the NHS. This data is collected under the auspices of the National Bridge Inspection Standards (NBIS) as prescribed by law. The NBI System collects the information that is used to determine eligibility for NHS projects, performance measure reporting, NHS penalty determination, and reporting to Congress.  It supports oversight of the NBIS through various report tools, and provides data reporting that supports agency strategic goals.",
-            "title": "National Bridge Inventory System (NBI) - 1992",
-            "isPartOf": "DOT-693",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
-            "primaryITInvestmentUII": "021-012940226",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22500,52 +22480,53 @@
                     "title": "1992"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
-            "dataQuality": true,
+            "identifier": "693.1",
+            "isPartOf": "DOT-693",
+            "issued": "1992-12-31",
+            "keyword": [
+                "bridge",
+                "condition",
+                "deck",
+                "inspection",
+                "structure"
+            ],
+            "landingPage": "https://data.transportation.gov/d/8chh-kqeq",
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
+            "title": "National Bridge Inventory System (NBI) - 1992"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/8cjz-h8bz",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2022-08-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-21",
-            "keyword": [
-                "bikeshare",
-                "dockless bikeshare",
-                "e-scooters",
-                "micromobility"
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
-            "identifier": "https://data.transportation.gov/api/views/8cjz-h8bz",
             "description": "List of cities served by a bikeshare (docked or dockless) and/or e-scooter system by month in 2020. Some systems serve more than one city. The layer lists just the primary city served. Bikeshare includes systems that are open to the general public, IT-automated, and station based (contain hubs to which users can grab and return a bike) as well as dockless systems. The layer includes a count of the number of docking stations, the number of dockless bikeshare systems, and the number of e-scooter systems serving a city (if applicable) in each month and the status of the system - whether temporarily suspended or closed. Many systems temporarily suspended operations and/or closed permanently in response to COVID-19.",
-            "title": "Bikeshare (Docked and Dockless) and E-scooter Systems 2020 by Month and System Status",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22553,47 +22534,81 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/8cjz-h8bz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/8cjz-h8bz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/8cjz-h8bz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/8cjz-h8bz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/8cjz-h8bz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/8cjz-h8bz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/8cjz-h8bz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/8cjz-h8bz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/8cjz-h8bz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/8cjz-h8bz",
+            "issued": "2022-08-18",
+            "keyword": [
+                "bikeshare",
+                "dockless bikeshare",
+                "e-scooters",
+                "micromobility"
+            ],
+            "landingPage": "https://data.transportation.gov/d/8cjz-h8bz",
             "license": "https://www.usa.gov/government-works",
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
                 "Bicycles and Pedestrians"
             ],
-            "phone": "202-366-DATA(3282) "
+            "title": "Bikeshare (Docked and Dockless) and E-scooter Systems 2020 by Month and System Status"
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
-            "landingPage": "https://data.transportation.gov/d/8cnp-t3ya",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/03octtvt/03octtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "October 2003"
+                }
             ],
+            "identifier": "18.131",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -22603,56 +22618,74 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.131",
+            "landingPage": "https://data.transportation.gov/d/8cnp-t3ya",
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
-            "title": "Monthly Traffic Volume Trends - October 2003",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/03octtvt/03octtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "October 2003"
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
+            "title": "Monthly Traffic Volume Trends - October 2003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/8ect-6jqj",
+            "accrualPeriodicity": "R/PT0.1S",
             "bureauCode": [
                 "021:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kate Hartman",
+                "hasEmail": "mailto:kate.hartman@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Click \u201cExport\u201d on the right to download the vehicle trajectory data. The associated metadata and additional data can be downloaded below under \"Attachments\".\n\nResearchers for the Next Generation Simulation (NGSIM)  program collected detailed vehicle trajectory data on southbound US 101 and Lankershim Boulevard in Los Angeles, CA, eastbound I-80 in Emeryville, CA and Peachtree Street in Atlanta, Georgia. Data was collected through a network of synchronized digital video cameras. NGVIDEO, a customized software application developed for the NGSIM program, transcribed the vehicle trajectory data from the video. This vehicle trajectory data provided the precise location of each vehicle within the study area every one-tenth of a second, resulting in detailed lane positions and locations relative to other vehicles. Click the \"Show More\" button below to find additional contextual data and metadata for this dataset. \n\nFor site-specific NGSIM video file datasets, please see the following:\n- NGSIM I-80 Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-I-80-Vide/2577-gpny\n- NGSIM US-101 Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-US-101-Vi/4qzi-thur\n- NGSIM Lankershim Boulevard Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-Lankershi/uv3e-y54k\n- NGSIM Peachtree Street Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-Peachtree/mupt-aksf",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/api/views/8ect-6jqj/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.transportation.gov/api/views/8ect-6jqj/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.transportation.gov/api/views/8ect-6jqj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.transportation.gov/api/views/8ect-6jqj/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.transportation.gov/api/views/8ect-6jqj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.transportation.gov/api/views/8ect-6jqj/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.transportation.gov/api/views/8ect-6jqj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/8ect-6jqj",
             "issued": "2016-01-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2005-04-20/2006-11-09",
-            "modified": "2016-01-01",
             "keyword": [
                 "arterial",
                 "atlanta",
@@ -22675,87 +22708,38 @@
                 "us 101",
                 "video"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/8ect-6jqj",
-            "description": "Click \u201cExport\u201d on the right to download the vehicle trajectory data. The associated metadata and additional data can be downloaded below under \"Attachments\".\n\nResearchers for the Next Generation Simulation (NGSIM)  program collected detailed vehicle trajectory data on southbound US 101 and Lankershim Boulevard in Los Angeles, CA, eastbound I-80 in Emeryville, CA and Peachtree Street in Atlanta, Georgia. Data was collected through a network of synchronized digital video cameras. NGVIDEO, a customized software application developed for the NGSIM program, transcribed the vehicle trajectory data from the video. This vehicle trajectory data provided the precise location of each vehicle within the study area every one-tenth of a second, resulting in detailed lane positions and locations relative to other vehicles. Click the \"Show More\" button below to find additional contextual data and metadata for this dataset. \n\nFor site-specific NGSIM video file datasets, please see the following:\n- NGSIM I-80 Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-I-80-Vide/2577-gpny\n- NGSIM US-101 Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-US-101-Vi/4qzi-thur\n- NGSIM Lankershim Boulevard Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-Lankershi/uv3e-y54k\n- NGSIM Peachtree Street Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-Peachtree/mupt-aksf",
-            "title": "Next Generation Simulation (NGSIM) Vehicle Trajectories and Supporting Data",
+            "landingPage": "https://data.transportation.gov/d/8ect-6jqj",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
+            "modified": "2016-01-01",
             "programCode": [
                 "021:013"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/api/views/8ect-6jqj/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/8ect-6jqj/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.transportation.gov/api/views/8ect-6jqj/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/8ect-6jqj/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.transportation.gov/api/views/8ect-6jqj/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/8ect-6jqj/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.transportation.gov/api/views/8ect-6jqj/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
             "spatial": "Los Angeles, California; Emeryville, California; Atlanta, Georgia",
-            "dataQuality": true,
-            "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "R/PT0.1S",
+            "temporal": "2005-04-20/2006-11-09",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Next Generation Simulation (NGSIM) Vehicle Trajectories and Supporting Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/8ehq-7his",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-11-25",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
-            "keyword": [
-                "diesel",
-                "electric",
-                "energy",
-                "fuel"
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
-            "identifier": "https://data.transportation.gov/api/views/8ehq-7his",
             "description": "This dataset details fuel mileage and gallons/kilowatt hours for each agency, mode, and type of service (TOS) as reported by agencies submitted data to the National Transit Database (NTD) for the 2022 and 2023 report years. This file is based on the 2022 and 2023 Energy Consumption database files available at https://transit.dot.gov/ntd/ntd-data\n\nData Tables organize and summarize data from the 2022 and 2023 NTD in a manner that is more useful for quick reference and summary analysis. \n\nOnly Full Reporters report energy consumption. Other reporter types do not appear in this dataset. Demand Response Taxi (DR/TX) mode and type of service combination does not report energy consumption and does not appear in this dataset. Finally, Non-dedicated fleets report energy consumption but not miles traveled. Thus for some agencies the given data for miles traveled are incomplete. Non-dedicated fleets represent about 7% of the data reflected in this dataset.\n\nIn versions of the data tables from 2014-2021, you can find data on fuel and energy in the file called \"Fuel and Energy\" available from the NTD program website.",
-            "title": "2022 - 2023 NTD Annual Data - Fuel and Energy",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22763,43 +22747,77 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/8ehq-7his/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/8ehq-7his/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/8ehq-7his/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/8ehq-7his/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/8ehq-7his/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/8ehq-7his/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/8ehq-7his/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/8ehq-7his/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/8ehq-7his/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/8ehq-7his",
+            "issued": "2024-11-25",
+            "keyword": [
+                "diesel",
+                "electric",
+                "energy",
+                "fuel"
+            ],
+            "landingPage": "https://data.transportation.gov/d/8ehq-7his",
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
+            "title": "2022 - 2023 NTD Annual Data - Fuel and Energy"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/8esj-a53k",
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
+                    "description": "2011 Idaho HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/idaho2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Idaho"
+                }
+            ],
+            "identifier": "678.14",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -22813,60 +22831,58 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.14",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Idaho",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/8esj-a53k",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/idaho2011.zip",
-                    "description": "2011 Idaho HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Idaho"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Idaho"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "ftp://ftp.nhtsa.dot.gov/Nits",
+            "agencyProgramURL": "http://www.nhtsa.gov/Data/State+Data+Programs",
+            "analysisUnit": "vehicle crash",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/8eua-u4wm",
-            "issued": "2009-01-27",
-            "temporal": "2008-01-01/2010-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "FARS/GES/NiTS Micro-Computer Data Entry System (MDE)",
-            "references": [
-                "http://www-nrd.nhtsa.dot.gov/Cats/listpublications.aspx%3FId=233&ShowBy=Category"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/Cats/listpublications.aspx%3FId=233&ShowBy=Category",
+            "description": "The Not-in-Traffic Surveillance (NiTS) system is a virtual data collection system designed to provide counts and details regarding fatalities and injuries that occur in non-traffic crashes and in non-crash incidents. NiTS non-traffic crash data is obtained through NHTSA's National Automotive Sampling System, General Estimates System (NASS GES) and the Fatality Analysis Reporting System (FARS). NiTS non-crash injury data is based upon emergency department records from a special study conducted by the Consumer Product Safety Commission's National Electronic Injury Surveillance System (NEISS) All Injury Program. NiTS non-crash fatality data is derived from death certificate information from the Centers for Disease Control's National Vital Statistics System.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/nits/Nontraffic%20crashes/2009/",
+                    "mediaType": "text/plain",
+                    "title": "2009 Nontraffic Crashes"
+                }
             ],
+            "identifier": "288.8",
+            "isPartOf": "DOT-288",
+            "issued": "2009-01-27",
             "keyword": [
                 "crash",
                 "death",
@@ -22882,95 +22898,61 @@
                 "vehicle",
                 "victim"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "288.8",
+            "landingPage": "https://data.transportation.gov/d/8eua-u4wm",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-5391",
+            "programCode": [
+                "021:032"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Highway Traffic Safety Administration"
             },
-            "description": "The Not-in-Traffic Surveillance (NiTS) system is a virtual data collection system designed to provide counts and details regarding fatalities and injuries that occur in non-traffic crashes and in non-crash incidents. NiTS non-traffic crash data is obtained through NHTSA's National Automotive Sampling System, General Estimates System (NASS GES) and the Fatality Analysis Reporting System (FARS). NiTS non-crash injury data is based upon emergency department records from a special study conducted by the Consumer Product Safety Commission's National Electronic Injury Surveillance System (NEISS) All Injury Program. NiTS non-crash fatality data is derived from death certificate information from the Centers for Disease Control's National Vital Statistics System.",
-            "title": "Not in Traffic Surveillance (NiTS) - 2009 Nontraffic Crashes",
-            "isPartOf": "DOT-288",
-            "agencyProgramURL": "http://www.nhtsa.gov/Data/State+Data+Programs",
-            "programCode": [
-                "021:032"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/nits/Nontraffic%20crashes/2009/",
-                    "mediaType": "text/plain",
-                    "title": "2009 Nontraffic Crashes"
-                }
+            "references": [
+                "http://www-nrd.nhtsa.dot.gov/Cats/listpublications.aspx%3FId=233&ShowBy=Category"
             ],
             "spatial": "United States of America",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/Cats/listpublications.aspx%3FId=233&ShowBy=Category",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "ftp://ftp.nhtsa.dot.gov/Nits",
+            "temporal": "2008-01-01/2010-12-31",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "analysisUnit": "vehicle crash",
-            "phone": "202-366-5391",
-            "language": [
-                "en-US"
-            ]
+            "title": "Not in Traffic Surveillance (NiTS) - 2009 Nontraffic Crashes"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/8fhu-iykf",
-            "issued": "2021-01-21",
             "@type": "dcat:Dataset",
-            "modified": "2021-01-21",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alpha Wingfield",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/8fhu-iykf",
+            "issued": "2021-01-21",
+            "landingPage": "https://data.transportation.gov/d/8fhu-iykf",
+            "modified": "2021-01-21",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "State Transportation Statistics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/8fiq-4cn6",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2020-07-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "toll",
-                "toll id",
-                "toll name"
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
-            "identifier": "https://data.transportation.gov/api/views/8fiq-4cn6",
             "description": "HPMS toll ID and facility name by state.",
-            "title": "Toll ID Elements",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -22978,47 +22960,83 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/8fiq-4cn6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/8fiq-4cn6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/8fiq-4cn6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/8fiq-4cn6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/8fiq-4cn6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/8fiq-4cn6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/8fiq-4cn6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/8fiq-4cn6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/8fiq-4cn6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "USA",
+            "identifier": "https://data.transportation.gov/api/views/8fiq-4cn6",
+            "issued": "2020-07-14",
+            "keyword": [
+                "toll",
+                "toll id",
+                "toll name"
+            ],
+            "landingPage": "https://data.transportation.gov/d/8fiq-4cn6",
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
+            "spatial": "USA",
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Toll ID Elements"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/8fni-ehdq",
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
+                    "description": "2012 Illinois HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/illinois2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Illinois"
+                }
+            ],
+            "identifier": "678.67",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -23032,60 +23050,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.67",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Illinois",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/8fni-ehdq",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/illinois2012.zip",
-                    "description": "2012 Illinois HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Illinois"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Illinois"
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
-            "landingPage": "https://data.transportation.gov/d/8gfa-vzbb",
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
+                    "downloadURL": "https://cms.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/docs/closedByEnforcement_FY2009_04-26-2013.xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Fiscal Year 2009"
+                }
             ],
+            "identifier": "96.2",
+            "isPartOf": "DOT-96",
+            "issued": "2018-12-17",
             "keyword": [
                 "bus",
                 "civil penalties",
@@ -23098,57 +23113,60 @@
                 "motor carrier",
                 "truck"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "96.2",
+            "landingPage": "https://data.transportation.gov/d/8gfa-vzbb",
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
-            "title": "Closed Enforcement Cases - Fiscal Year 2009",
-            "isPartOf": "DOT-96",
-            "agencyProgramURL": "http://www.fmcsa.dot.gov/regulations/enforcement/civil-penalties",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://cms.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/docs/closedByEnforcement_FY2009_04-26-2013.xlsx",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "Fiscal Year 2009"
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
+            "title": "Closed Enforcement Cases - Fiscal Year 2009"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/8grw-bjfc",
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
+                    "description": "2013 North Dakota HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/northdakota2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 North Dakota"
+                }
+            ],
+            "identifier": "678.138",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -23162,60 +23180,58 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.138",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 North Dakota",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/8grw-bjfc",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/northdakota2013.zip",
-                    "description": "2013 North Dakota HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 North Dakota"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 North Dakota"
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
-            "landingPage": "https://data.transportation.gov/d/8jdk-cepv",
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
+                    "description": "This access point provides access to the LTPP InfoPave visualization features including inspection videos, distress maps and images, manual distress surveys, pavement cross-section, section timeline, and data pivot",
+                    "downloadURL": "https://infopave.fhwa.dot.gov/%3FGoto=Visualization",
+                    "mediaType": "application/atom+xml",
+                    "title": "Visualization"
+                }
             ],
+            "identifier": "679.8",
+            "isPartOf": "DOT-679",
+            "issued": "1993-07-01",
             "keyword": [
                 "asphalt concrete",
                 "continuously reinforced concrete pavement",
@@ -23232,57 +23248,59 @@
                 "texture",
                 "traffic loading"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "679.8",
+            "landingPage": "https://data.transportation.gov/d/8jdk-cepv",
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
-            "title": "Long-Term Pavement Performance (LTPP) - Visualization",
-            "isPartOf": "DOT-679",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/research/tfhrc/programs/infrastructure/pavements/ltpp/",
-            "programCode": [
-                "021:009"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/atom+xml",
-                    "downloadURL": "https://infopave.fhwa.dot.gov/%3FGoto=Visualization",
-                    "description": "This access point provides access to the LTPP InfoPave visualization features including inspection videos, distress maps and images, manual distress surveys, pavement cross-section, section timeline, and data pivot",
-                    "@type": "dcat:Distribution",
-                    "title": "Visualization"
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
+            "title": "Long-Term Pavement Performance (LTPP) - Visualization"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/8jrq-t728",
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
+                    "description": "2013 Vermont HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/vermont2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Vermont"
+                }
+            ],
+            "identifier": "678.148",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -23296,55 +23314,41 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.148",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Vermont",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/8jrq-t728",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/vermont2013.zip",
-                    "description": "2013 Vermont HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Vermont"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Vermont"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/8jyh-rmwk",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Economic concepts related to transportation productivity",
+            "identifier": "https://data.transportation.gov/api/views/8jyh-rmwk",
             "issued": "2020-04-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
             "keyword": [
                 "labor productivity",
                 "multifactor productivity",
@@ -23352,59 +23356,35 @@
                 "transportation",
                 "transportation economics"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/8jyh-rmwk",
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
-            "identifier": "https://data.transportation.gov/api/views/8jyh-rmwk",
-            "description": "Economic concepts related to transportation productivity",
-            "title": "Transportation Economic Trends Concepts: Productivity",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Transportation Economic Trends Concepts: Productivity"
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
-                "name": "Federal Motor Carrier Safety Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/8kgi-8dcn",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System data sample for the year 1998",
-            "title": "Historic HPMS Data (Sample) - 1998",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23412,72 +23392,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/8kgi-8dcn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/8kgi-8dcn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/8kgi-8dcn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/8kgi-8dcn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/8kgi-8dcn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/8kgi-8dcn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/8kgi-8dcn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/8kgi-8dcn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/8kgi-8dcn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "dataQuality": true,
-            "theme": [
-                "Roadways and Bridges"
+            "identifier": "https://data.transportation.gov/api/views/8kgi-8dcn",
+            "issued": "2022-07-08",
+            "keyword": [
+                "highway",
+                "highway performance monitoring",
+                "highway performance monitoring system",
+                "highways",
+                "hpms",
+                "sample"
             ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "language": [
                 "en-US"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "bureauCode": [
-                "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/8mt4-y7ed",
-            "issued": "1998-12-24",
-            "temporal": "R/1998-12-14/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
-            "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.nhtsa.gov/Research/Databases+and+Software/NHTSA+Test+Reference+Guides"
+            "modified": "2024-05-08",
+            "programCode": [
+                "021:009"
             ],
-            "keyword": [
-                "nhtsa crash test database",
-                "nhtsa vehicle crash test database"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "spatial": "United States",
+            "theme": [
+                "Roadways and Bridges"
             ],
+            "title": "Historic HPMS Data (Sample) - 1998"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://www.nhtsa.gov",
+            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
+            "analysisUnit": "Test",
+            "bureauCode": [
+                "021:18"
+            ],
+            "categoryDesignation": "Research",
+            "collectionInstrument": "Transportation",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "364.24",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2006",
-            "isPartOf": "DOT-364",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
-            "primaryITInvestmentUII": "021-621341357",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23486,35 +23468,68 @@
                     "title": "Event Data Records Reports - 2006"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.24",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/8mt4-y7ed",
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
+            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2006"
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
-            "landingPage": "https://data.transportation.gov/d/8nvc-7c4i",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/03martvt/tvtmar03.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "March 2003"
+                }
             ],
+            "identifier": "18.138",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -23524,82 +23539,46 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.138",
+            "landingPage": "https://data.transportation.gov/d/8nvc-7c4i",
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
-            "title": "Monthly Traffic Volume Trends - March 2003",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/03martvt/tvtmar03.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "March 2003"
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
+            "title": "Monthly Traffic Volume Trends - March 2003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Access restricted under the Privacy Act of 1974; see SORN DOT/OST 035 http://www.gpo.gov/fdsys/pkg/FR-2000-04-11/pdf/00-8505.pdf#page=78",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/8p8x-y23y",
-            "issued": "2014-09-16",
-            "temporal": "R/2014-09-16/PT1S",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Federal Government Finances and Employment",
-            "keyword": [
-                "background",
-                "clearance",
-                "credential",
-                "investigation",
-                "personnel",
-                "security"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "428.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
             "description": "This data set contains the types of background investigations, decisions, level of security clearance, date of security clearance training, and credentials issued to non-FAA Federal employees, contractors, detailees, and interns.",
-            "title": "Personnel Security Investigations -",
-            "primaryITInvestmentUII": "021-683968199",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23607,55 +23586,57 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "theme": [
-                "Federal Government Finances and Employment"
+            "identifier": "428.0",
+            "issued": "2014-09-16",
+            "keyword": [
+                "background",
+                "clearance",
+                "credential",
+                "investigation",
+                "personnel",
+                "security"
             ],
-            "accrualPeriodicity": "R/PT1S",
-            "categoryDesignation": "Administrative",
+            "landingPage": "https://data.transportation.gov/d/8p8x-y23y",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-6514"
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-14",
+            "phone": "202-366-6514",
+            "primaryITInvestmentUII": "021-683968199",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "rights": "Access restricted under the Privacy Act of 1974; see SORN DOT/OST 035 http://www.gpo.gov/fdsys/pkg/FR-2000-04-11/pdf/00-8505.pdf#page=78",
+            "temporal": "R/2014-09-16/PT1S",
+            "theme": [
+                "Federal Government Finances and Employment"
+            ],
+            "title": "Personnel Security Investigations -"
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
-            "landingPage": "https://data.transportation.gov/d/8q8r-7v52",
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
-            "identifier": "DOT-80",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
             "description": "The Child Safety Seat Inspection Station Locations are used to make it easier for all citizens to get their Child Safety Seats properly installed. Car crashes are the largest cause of fatalities and serious injuries for children between ages 2 and 15.  Also, surveys indicate that a high percentage of Child Safety Seats are not installed properly.  Information updates for each station are reported to NHTSA and enterred by NHTSA staff.  NHTSA staff will also attempt to validate the station locations using a comercial Geographic database so this data will, in most cases, be able to be used for driving directions.",
-            "title": "NHTSA Child Safety Seat Inspection Station Locator - NCSSISL",
-            "agencyProgramURL": "http://www.nhtsa.gov/cps/cpsfitting/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23664,60 +23645,60 @@
                     "title": "NHTSA API"
                 }
             ],
-            "spatial": "Zip, State, Geo co-ordinates",
-            "dataQuality": false,
+            "identifier": "DOT-80",
+            "issued": "2010-01-05",
+            "keyword": [
+                "child seat",
+                "inspection",
+                "safety",
+                "station",
+                "stations"
+            ],
+            "landingPage": "https://data.transportation.gov/d/8q8r-7v52",
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
-            "analysisUnit": "N/A",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4945",
-            "language": [
-                "en-US"
-            ]
+            "title": "NHTSA Child Safety Seat Inspection Station Locator - NCSSISL"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
+            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/owners/SearchSafetyIssues",
+            "analysisUnit": "Vehicles , Tires, Child Safety Seats, Equipment",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/8qbs-9p4c",
-            "issued": "2002-12-16",
-            "temporal": "R/1949-01-01/P1D",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "N/A",
-            "modified": "2024-05-01",
-            "references": [
-                "http://www-odi.nhtsa.dot.gov/downloads/folders/Complaints/Import_Instructions.pdf"
-            ],
-            "keyword": [
-                "complaints",
-                "email",
-                "paper",
-                "phone",
-                "safercar.gov"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "DOT-81",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Complaint information entered into NHTSA-ODI's vehicle owner's complaint database is used with other data sources to identify safety issues that warrant investigation and to determine if a safety-related defect trend exists. Complaint information is also analyzed to monitor existing recalls for proper scope and adequacy.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Complaints",
-            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/owners/SearchSafetyIssues",
+            "dataQuality": true,
+            "describedBy": "http://www-odi.nhtsa.dot.gov/downloads/folders/Complaints/CMPL.txt",
             "describedByType": "text/plain",
-            "primaryITInvestmentUII": "021-777552743",
-            "programCode": [
-                "021:000"
-            ],
+            "description": "Complaint information entered into NHTSA-ODI's vehicle owner's complaint database is used with other data sources to identify safety issues that warrant investigation and to determine if a safety-related defect trend exists. Complaint information is also analyzed to monitor existing recalls for proper scope and adequacy.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23726,58 +23707,59 @@
                     "title": "Complaints Flat File"
                 }
             ],
-            "spatial": "N/A",
-            "describedBy": "http://www-odi.nhtsa.dot.gov/downloads/folders/Complaints/CMPL.txt",
-            "dataQuality": true,
+            "identifier": "DOT-81",
+            "issued": "2002-12-16",
+            "keyword": [
+                "complaints",
+                "email",
+                "paper",
+                "phone",
+                "safercar.gov"
+            ],
+            "landingPage": "https://data.transportation.gov/d/8qbs-9p4c",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
+            "modified": "2024-05-01",
+            "phone": "202-366-2315",
+            "primaryITInvestmentUII": "021-777552743",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "http://www-odi.nhtsa.dot.gov/downloads/folders/Complaints/Import_Instructions.pdf"
+            ],
+            "spatial": "N/A",
+            "temporal": "R/1949-01-01/P1D",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Vehicles , Tires, Child Safety Seats, Equipment",
-            "phone": "202-366-2315",
-            "language": [
-                "en-US"
-            ]
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Complaints"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://regs.dot.gov/OSTsignificantguiddocs.htm",
+            "agencyProgramURL": "http://regs.dot.gov/",
+            "analysisUnit": "Regulations",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/8qyf-q9wu",
-            "issued": "2011-01-18",
-            "temporal": "1995-01-01/2013-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Other",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://regs.dot.gov/"
-            ],
-            "keyword": [
-                "data.gov",
-                "law",
-                "significant guidance",
-                "transportation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "DOT-276",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": true,
             "description": "A list of Significant Guidance documents, which include guidance document disseminated to regulated entities or the general public that may reasonably be anticipated to lead to an annual effect on the economy of $100 million or more or adversely affect in a material way the economy, a sector of the economy, productivity, competition, jobs, the environment, public health or safety, or State, local, or tribal governments or communities; create a serious inconsistency or otherwise interfere with an action taken or planned by another agency; materially alter the budgetary impact of entitlements, grants, user fees, or loan programs or the rights and obligations of recipients thereof; or raise novel legal or policy issues arising out of legal mandates, the President's priorities, or the principles set forth in Executive Order 12866, as further amended.",
-            "title": "Significant Guidance Issued by the Office of the Secretary of Transportation",
-            "agencyProgramURL": "http://regs.dot.gov/",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23785,68 +23767,91 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "DOT-276",
+            "issued": "2011-01-18",
+            "keyword": [
+                "data.gov",
+                "law",
+                "significant guidance",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/8qyf-q9wu",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://regs.dot.gov/OSTsignificantguiddocs.htm",
+            "modified": "2024-11-14",
+            "phone": "202-366-4308",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "references": [
+                "http://regs.dot.gov/"
+            ],
+            "spatial": "N/A",
+            "temporal": "1995-01-01/2013-12-31",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "analysisUnit": "Regulations",
-            "categoryDesignation": "Other",
-            "phone": "202-366-4308",
-            "language": [
-                "en-US"
-            ]
+            "title": "Significant Guidance Issued by the Office of the Secretary of Transportation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/8qzs-s5wt",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRA Safety Data Team",
+                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This is the landing page for generating PDF reports for Form 6180.54 Rail Equipment Accident/Incident, Form 6180.55a Injury/Illness [Casualty], Form 6180.57 Highway-Rail Grade Crossing Accident/Incident and Form 6180.71 Crossing Inventory.",
+            "identifier": "https://data.transportation.gov/api/views/8qzs-s5wt",
             "issued": "2024-12-11",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "form 54",
                 "form 57",
                 "pdf"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRA Safety Data Team",
-                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/8qzs-s5wt",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-27",
+            "programCode": [
+                "021:036"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Railroad Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/8qzs-s5wt",
-            "description": "This is the landing page for generating PDF reports for Form 6180.54 Rail Equipment Accident/Incident, Form 6180.55a Injury/Illness [Casualty], Form 6180.57 Highway-Rail Grade Crossing Accident/Incident and Form 6180.71 Crossing Inventory.",
-            "title": "Form PDF Generator",
-            "programCode": [
-                "021:036"
-            ],
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Railroads"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Form PDF Generator"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/8r23-j2j7",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This report lists all highway-rail grade crossing incidents and key details, along with the ability to download reports for the form 57 (highway-rail grade crossing incidents), form 71 (highway-rail grade crossing inventory) and/or form 55a (injury/illness summary).",
+            "identifier": "https://data.transportation.gov/api/views/8r23-j2j7",
             "issued": "2023-08-04",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "crossing inventory",
                 "crossing inventory form",
@@ -23861,66 +23866,42 @@
                 "pdf",
                 "railroad"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/8r23-j2j7",
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
-            "identifier": "https://data.transportation.gov/api/views/8r23-j2j7",
-            "description": "This report lists all highway-rail grade crossing incidents and key details, along with the ability to download reports for the form 57 (highway-rail grade crossing incidents), form 71 (highway-rail grade crossing inventory) and/or form 55a (injury/illness summary).",
-            "title": "Highway-Rail Grade Crossing Incident Detail Listing (5.15)",
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
+            "title": "Highway-Rail Grade Crossing Incident Detail Listing (5.15)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www.phmsa.dot.gov/hazmat/guidance",
+            "agencyProgramURL": "http://www.phmsa.dot.gov/hazmat/guidance",
+            "analysisUnit": "Regulations",
             "bureauCode": [
                 "021:50"
             ],
-            "landingPage": "https://data.transportation.gov/d/8rdf-ak4w",
-            "issued": "2011-01-18",
-            "temporal": "2005-01-01/2011-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-23",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.phmsa.dot.gov/hazmat/guidance"
-            ],
-            "keyword": [
-                "data.gov",
-                "law",
-                "significant guidance",
-                "transportation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "PHMSA-Datahub",
                 "hasEmail": "mailto:PHMSA-Datahub@dot.gov"
             },
-            "identifier": "326.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Pipeline and Hazardous Materials Safety Administration"
-            },
+            "dataQuality": true,
             "description": "A list of Significant Guidance documents, which include guidance document disseminated to regulated entities or the general public that may reasonably be anticipated to lead to an annual effect on the economy of $100 million or more or adversely affect in a material way the economy, a sector of the economy, productivity, competition, jobs, the environment, public health or safety, or State, local, or tribal governments or communities; create a serious inconsistency or otherwise interfere with an action taken or planned by another agency; materially alter the budgetary impact of entitlements, grants, user fees, or loan programs or the rights and obligations of recipients thereof; or raise novel legal or policy issues arising out of legal mandates, the President's priorities, or the principles set forth in Executive Order 12866, as further amended.",
-            "title": "Significant Guidance on Hazardous Materials Safety Issued by the Pipeline and Hazardous Materials Safety Administration -",
-            "isPartOf": "DOT-326",
-            "agencyProgramURL": "http://www.phmsa.dot.gov/hazmat/guidance",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -23928,89 +23909,90 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.phmsa.dot.gov/hazmat/guidance",
-            "theme": [
-                "Transportation"
+            "identifier": "326.1",
+            "isPartOf": "DOT-326",
+            "issued": "2011-01-18",
+            "keyword": [
+                "data.gov",
+                "law",
+                "significant guidance",
+                "transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "analysisUnit": "Regulations",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4308",
+            "landingPage": "https://data.transportation.gov/d/8rdf-ak4w",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-10-23",
+            "phone": "202-366-4308",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Pipeline and Hazardous Materials Safety Administration"
+            },
+            "references": [
+                "http://www.phmsa.dot.gov/hazmat/guidance"
+            ],
+            "temporal": "2005-01-01/2011-01-18",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Significant Guidance on Hazardous Materials Safety Issued by the Pipeline and Hazardous Materials Safety Administration -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/8s3h-vvui",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Depicts the areas of the city accessible by docked bikeshare within a given amount of time (10 and 20 minutes) when starting and ending at a docking station.",
+            "identifier": "https://data.transportation.gov/api/views/8s3h-vvui",
             "issued": "2021-08-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-25",
             "keyword": [
                 "accessibility",
                 "bikeshare",
                 "micromobility",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/8s3h-vvui",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-10-25",
+            "phone": "202-366-DATA(3282)",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/8s3h-vvui",
-            "description": "Depicts the areas of the city accessible by docked bikeshare within a given amount of time (10 and 20 minutes) when starting and ending at a docking station.",
-            "title": "Areas Accessible by Docked Bikeshare",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Bicycles and Pedestrians"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Areas Accessible by Docked Bikeshare"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://data.transportation.gov/d/8sf3-b9fy",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:17"
             ],
-            "rights": "Driver PII and drug test results.",
-            "issued": "2018-12-17",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-24",
-            "keyword": [
-                "alcohol",
-                "driver",
-                "drug",
-                "results",
-                "test"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO",
                 "hasEmail": "mailto:fmcsa.cdo@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
-            "identifier": "100.0",
+            "dataQuality": false,
             "description": "Annual survey of appoximately 5,000 motor carriers used to set sampling rates for random drug and alcohol tests of commercial drivers.",
-            "title": "Drug and Alcohol \"MIS\" Survey -",
-            "programCode": [
-                "021:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24018,74 +24000,72 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
+            "identifier": "100.0",
+            "issued": "2018-12-17",
+            "keyword": [
+                "alcohol",
+                "driver",
+                "drug",
+                "results",
+                "test"
+            ],
+            "landingPage": "https://data.transportation.gov/d/8sf3-b9fy",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-05-24",
+            "programCode": [
+                "021:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "rights": "Driver PII and drug test results.",
             "theme": [
                 "Transportation"
             ],
-            "categoryDesignation": "Research",
-            "language": [
-                "en-US"
-            ]
+            "title": "Drug and Alcohol \"MIS\" Survey -"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/8sfc-juwb",
-            "issued": "2021-04-07",
             "@type": "dcat:Dataset",
-            "modified": "2022-01-14",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Chambers",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/8sfc-juwb",
+            "issued": "2021-04-07",
+            "landingPage": "https://data.transportation.gov/d/8sfc-juwb",
+            "modified": "2022-01-14",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Port Throughput Metrics"
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
-            "landingPage": "https://data.transportation.gov/d/8skz-jf9d",
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
-            "identifier": "373.4",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": true,
             "description": "Each Freedom of Information Act office uses a case log to track FOIA requests. The logs typically include the dates on which requests were received and closed, control numbers, requester names and descriptions of the requested records.",
-            "title": "Freedom of Information Act Logs for the Office of the Secretary of Transportation - 2010",
-            "isPartOf": "DOT-373",
-            "agencyProgramURL": "http://www.dot.gov/foia",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24094,35 +24074,70 @@
                     "title": "2010"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "373.4",
+            "isPartOf": "DOT-373",
+            "issued": "2007-12-31",
+            "keyword": [
+                "foia",
+                "freedom of information act",
+                "log",
+                "request"
+            ],
+            "landingPage": "https://data.transportation.gov/d/8skz-jf9d",
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
+            "title": "Freedom of Information Act Logs for the Office of the Secretary of Transportation - 2010"
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
-            "landingPage": "https://data.transportation.gov/d/8ta5-qycj",
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
+            "identifier": "65.9",
+            "isPartOf": "DOT-65",
+            "issued": "2015-10-05",
             "keyword": [
                 "49",
                 "551",
@@ -24159,87 +24174,50 @@
                 "vin",
                 "vpic"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "65.9",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "The NHTSA Product Information Catalog and Vehicle Listing (vPIC) is a consolidated platform that presents data collected within the manufacturer reported data from CFR 49 Parts 551 - 574 for use in a variety of modern tools. NHTSA's vPIC platform is intended to serve as a centralized source for basic Vehicle Identification Number (VIN) decoding, Manufacturer Information Database (MID), Manufacturer Equipment Plant Identification and associated data. vPIC is intended to support the Open Data and Transparency initiatives of the agency by allowing the data to be freely used by the public without the burden of manual retrieval from a library of electronic documents (PDFs). While these documents will still be available online for viewing within the Manufacturer Information Database (MID) module of vPIC one can view and use the actual data through the VIN Decoder and Application Programming Interface (API) modules.",
-            "title": "NHTSA Product Information Catalog and Vehicle Listing (vPIC) - Modifier DB",
-            "isPartOf": "DOT-65",
-            "agencyProgramURL": "http://vpic.nhtsa.dot.gov/",
+            "landingPage": "https://data.transportation.gov/d/8ta5-qycj",
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
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www.nhtsa.gov/Research/Databases+and+Software/NHTSA+Test+Reference+Guides",
+            "agencyProgramURL": "http://www.nhtsa.gov/Research",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/8tev-ydpe",
-            "issued": "1981-12-31",
-            "temporal": "1981/2015",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.nhtsa.gov/Research/Databases+and+Software/NHTSA+Test+Reference+Guides"
-            ],
-            "keyword": [
-                "compliance",
-                "crash",
-                "database",
-                "ncap",
-                "test",
-                "vehicle"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "1840.11",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/veh/vehdb-export-fields.htm",
             "description": "The NHTSA Vehicle Crash Test Database contains engineering data measured during various types of research, the New Car Assessment Program (NCAP), and compliance crash tests. Information in this database refers to the performance and response of vehicles and other structures in impacts. This database is not intended to support general consumer safety issues. For general consumer information please see the NHTSA's information on buying a safer car.",
-            "title": "Vehicle Crash Test Database - Zipped ASCII export",
-            "isPartOf": "DOT-1840",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research",
-            "primaryITInvestmentUII": "021-961265599",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24248,45 +24226,53 @@
                     "title": "Zipped ASCII export"
                 }
             ],
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/veh/vehdb-export-fields.htm",
-            "dataQuality": true,
+            "identifier": "1840.11",
+            "isPartOf": "DOT-1840",
+            "issued": "1981-12-31",
+            "keyword": [
+                "compliance",
+                "crash",
+                "database",
+                "ncap",
+                "test",
+                "vehicle"
+            ],
+            "landingPage": "https://data.transportation.gov/d/8tev-ydpe",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.nhtsa.gov/Research/Databases+and+Software/NHTSA+Test+Reference+Guides",
+            "modified": "2024-05-01",
+            "phone": "202-366-4712",
+            "primaryITInvestmentUII": "021-961265599",
+            "programCode": [
+                "021:032"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "http://www.nhtsa.gov/Research/Databases+and+Software/NHTSA+Test+Reference+Guides"
+            ],
+            "temporal": "1981/2015",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4712",
-            "language": [
-                "en-US"
-            ]
+            "title": "Vehicle Crash Test Database - Zipped ASCII export"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/8tvb-ywj3",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-09-05",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
-            "keyword": [
-                "funding",
-                "local funding"
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
-            "identifier": "https://data.transportation.gov/api/views/8tvb-ywj3",
             "description": "This dataset details local funding sources for each applicable agency reporting to the National Transit Database in the 2022 and 2023 report years.  Examples include Income, Sales, Property and Fuel taxes and Tolls.\n\nNTD Data Tables organize and summarize data from the 2022 and 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. This dataset is based on the 2022 and 2023 Revenue Sources database files.\n\nIn years 2015-2021, you can find this data in the \"Funding Sources\" data table on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.\n\nIf you have any other questions about this table, please contact the NTD Help Desk at NTDHelp@dot.gov.",
-            "title": "2022 - 2023 NTD Annual Data - Funding Sources (Local)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24294,61 +24280,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/8tvb-ywj3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/8tvb-ywj3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/8tvb-ywj3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/8tvb-ywj3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/8tvb-ywj3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/8tvb-ywj3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/8tvb-ywj3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/8tvb-ywj3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/8tvb-ywj3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/8tvb-ywj3",
+            "issued": "2024-09-05",
+            "keyword": [
+                "funding",
+                "local funding"
+            ],
+            "landingPage": "https://data.transportation.gov/d/8tvb-ywj3",
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
+            "title": "2022 - 2023 NTD Annual Data - Funding Sources (Local)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.nhtsa.gov/equipment/takata-recall-spotlight",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "021:18"
             ],
-            "issued": "2022-12-09",
-            "temporal": "R/1949-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-13",
-            "keyword": [
-                "takata"
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
-            "identifier": "https://data.transportation.gov/api/views/8u28-hw9f",
+            "dataQuality": true,
             "description": "Tens of millions of vehicles with Takata air bags are under recall. Long-term exposure to high heat and humidity can cause these air bags to explode when deployed. Such explosions have caused injuries and deaths. \n\nNHTSA urges vehicle owners to take a few simple steps to protect themselves and others from this very serious threat to safety.\n\nThis dataset tracks various progress indicators for the recall.",
-            "title": "Takata Recall",
-            "primaryITInvestmentUII": "021-777552743",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24356,51 +24340,82 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/8u28-hw9f/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/8u28-hw9f/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/8u28-hw9f/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/8u28-hw9f/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/8u28-hw9f/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/8u28-hw9f/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/8u28-hw9f/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/8u28-hw9f/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/8u28-hw9f/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/8u28-hw9f",
+            "issued": "2022-12-09",
+            "keyword": [
+                "takata"
+            ],
+            "landingPage": "https://www.nhtsa.gov/equipment/takata-recall-spotlight",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-08-13",
+            "primaryITInvestmentUII": "021-777552743",
+            "programCode": [
+                "021:035"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
             "spatial": "United States",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "R/1949-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Takata Recall"
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
-            "landingPage": "https://data.transportation.gov/d/8ubn-5mjw",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12dectvt/12dectvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "December 2012"
+                }
             ],
+            "identifier": "18.45",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -24410,64 +24425,39 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.45",
+            "landingPage": "https://data.transportation.gov/d/8ubn-5mjw",
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
-            "title": "Monthly Traffic Volume Trends - December 2012",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12dectvt/12dectvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "December 2012"
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
+            "title": "Monthly Traffic Volume Trends - December 2012"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/8uv2-y4is",
-            "issued": "2023-08-01",
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
-                "name": "Federal Railroad Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/8uv2-y4is",
             "description": "",
-            "title": "Crossing Inventory Source Data (Form 71) - Historical",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24475,67 +24465,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/8uv2-y4is/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/8uv2-y4is/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/8uv2-y4is/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/8uv2-y4is/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/8uv2-y4is/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/8uv2-y4is/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/8uv2-y4is/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/8uv2-y4is/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/8uv2-y4is/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/8uv2-y4is",
+            "issued": "2023-08-01",
+            "landingPage": "https://data.transportation.gov/d/8uv2-y4is",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-08-28",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Railroad Administration"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Crossing Inventory Source Data (Form 71) - Historical"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/tollpage/",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/tollpage/",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/8w43-6pw7",
-            "issued": "2013-09-01",
-            "temporal": "R/2013-09-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.fhwa.dot.gov/policyinformation/tollpage/"
-            ],
-            "keyword": [
-                "bridges",
-                "highways",
-                "toll facilities"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "DOT-684",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "Biennial report containing selected information on toll facilities in the United States that has been provided to FHWA by the States and/or various toll authorities regarding toll facilities in operation, financed, or under construction as of January 1.",
-            "title": "Toll Facilities in the United States",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/tollpage/",
-            "programCode": [
-                "021:011"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24544,29 +24526,51 @@
                     "title": "Toll Facilities in the United States"
                 }
             ],
-            "spatial": "National, State, Local",
-            "dataQuality": true,
+            "identifier": "DOT-684",
+            "issued": "2013-09-01",
+            "keyword": [
+                "bridges",
+                "highways",
+                "toll facilities"
+            ],
+            "landingPage": "https://data.transportation.gov/d/8w43-6pw7",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/tollpage/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5033",
+            "programCode": [
+                "021:011"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "references": [
+                "http://www.fhwa.dot.gov/policyinformation/tollpage/"
+            ],
+            "spatial": "National, State, Local",
+            "temporal": "R/2013-09-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Administrative",
-            "phone": "202-366-5033",
-            "language": [
-                "en-US"
-            ]
+            "title": "Toll Facilities in the United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:36"
             ],
-            "landingPage": "https://data.transportation.gov/d/8w6n-j4gk",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NTD Program Support",
+                "hasEmail": "mailto:NTDHelp@dot.gov"
+            },
+            "description": "A national summary of key transit performance metrics based on data reported by transit agencies to the National Transit Database (NTD) in Report Year 2022.\r\n\r\nNTD Data Summaries organize and summarize data from the 2022 National Transit Database in a manner that is more useful for quick reference and summary analysis. \r\n\r\nThis summary is based on the 2022 Service, Operating Expenses, and Federal Funding Allocation database files on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
+            "identifier": "https://data.transportation.gov/api/views/8w6n-j4gk",
             "issued": "2023-09-11",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-25",
             "keyword": [
                 "cost per hour",
                 "cost per trip",
@@ -24574,54 +24578,31 @@
                 "mile per trip",
                 "transit fares"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NTD Program Support",
-                "hasEmail": "mailto:NTDHelp@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/8w6n-j4gk",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-09-25",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Transit Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/8w6n-j4gk",
-            "description": "A national summary of key transit performance metrics based on data reported by transit agencies to the National Transit Database (NTD) in Report Year 2022.\r\n\r\nNTD Data Summaries organize and summarize data from the 2022 National Transit Database in a manner that is more useful for quick reference and summary analysis. \r\n\r\nThis summary is based on the 2022 Service, Operating Expenses, and Federal Funding Allocation database files on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
-            "title": "2022 NTD Annual Data Summary - Metrics",
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "2022 NTD Annual Data Summary - Metrics"
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
-            "identifier": "https://data.transportation.gov/api/views/8xu8-ax8r",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 2005",
-            "title": "Historic HPMS Data (Universe) - 2005",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24629,45 +24610,79 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/8xu8-ax8r/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/8xu8-ax8r/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/8xu8-ax8r/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/8xu8-ax8r/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/8xu8-ax8r/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/8xu8-ax8r/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/8xu8-ax8r/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/8xu8-ax8r/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/8xu8-ax8r/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/8xu8-ax8r",
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
+            "title": "Historic HPMS Data (Universe) - 2005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.itskrs.its.dot.gov",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "021:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kate Hartman",
+                "hasEmail": "mailto:kate.hartman@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Intelligent Transportation Systems Joint Program Office (ITS JPO) of the U.S. Department of Transportation (USDOT) has developed this ITS Lessons Learned Knowledge Resource (LLKR). Major objectives are: (1) capture experiences of stakeholders in their planning, deployment, operations, maintenance, and evaluation of ITS, (2) provide all ITS stakeholders with convenient access to the lessons learned knowledge so that they can make informed decisions in their future ITS actions.\n\nEach lesson captured in this knowledge resource is described in a concise format. A lesson description includes items such as a lesson title in the form of a recommendation, background and lesson learned narratives, as well as identifying information such as date, location, source, and contact.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Link to Intelligent Transportation Systems (ITS) Lessons Learned Database's Web User Interface.",
+                    "downloadURL": "https://www.itskrs.its.dot.gov/lessons",
+                    "mediaType": "text/html",
+                    "title": "Intelligent Transportation Systems (ITS) Lessons Learned"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/8y7u-tmga",
             "issued": "2019-05-02",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-02",
             "keyword": [
                 "arterial management",
                 "automated vehicles",
@@ -24683,105 +24698,74 @@
                 "road weather management",
                 "transportation management centers"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://www.itskrs.its.dot.gov",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2019-05-02",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Department of Transportation"
             },
-            "identifier": "https://data.transportation.gov/api/views/8y7u-tmga",
-            "description": "The Intelligent Transportation Systems Joint Program Office (ITS JPO) of the U.S. Department of Transportation (USDOT) has developed this ITS Lessons Learned Knowledge Resource (LLKR). Major objectives are: (1) capture experiences of stakeholders in their planning, deployment, operations, maintenance, and evaluation of ITS, (2) provide all ITS stakeholders with convenient access to the lessons learned knowledge so that they can make informed decisions in their future ITS actions.\n\nEach lesson captured in this knowledge resource is described in a concise format. A lesson description includes items such as a lesson title in the form of a recommendation, background and lesson learned narratives, as well as identifying information such as date, location, source, and contact.",
-            "title": "Intelligent Transportation Systems (ITS) Lessons Learned",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.itskrs.its.dot.gov/lessons",
-                    "description": "Link to Intelligent Transportation Systems (ITS) Lessons Learned Database's Web User Interface.",
-                    "@type": "dcat:Distribution",
-                    "title": "Intelligent Transportation Systems (ITS) Lessons Learned"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1M",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Intelligent Transportation Systems (ITS) Lessons Learned"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:36"
             ],
-            "landingPage": "https://data.transportation.gov/d/8yz5-d527",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NTD Program Support",
+                "hasEmail": "mailto:NTDHelp@dot.gov"
+            },
+            "description": "A national summary of Federal Funding Allocation data reported by transit agencies to the National Transit Database (NTD) in Report Year 2022.\r\n\r\nNTD Data Summaries organize and summarize data from the 2022 National Transit Database in a manner that is more useful for quick reference and summary analysis. \r\n\r\nThis summary is based on the 2022 Federal Funding Allocation database file on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
+            "identifier": "https://data.transportation.gov/api/views/8yz5-d527",
             "issued": "2023-09-11",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-10",
             "keyword": [
                 "ffa",
                 "ntd apportionment data",
                 "urbanized areas"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NTD Program Support",
-                "hasEmail": "mailto:NTDHelp@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/8yz5-d527",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-09-10",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Transit Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/8yz5-d527",
-            "description": "A national summary of Federal Funding Allocation data reported by transit agencies to the National Transit Database (NTD) in Report Year 2022.\r\n\r\nNTD Data Summaries organize and summarize data from the 2022 National Transit Database in a manner that is more useful for quick reference and summary analysis. \r\n\r\nThis summary is based on the 2022 Federal Funding Allocation database file on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
-            "title": "2022 NTD Data Summary - Federal Funding Allocation",
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "2022 NTD Data Summary - Federal Funding Allocation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "rights": "Access is restricted to authorized Federal or State inspector personnel.",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://hmpip.fmcsa.dot.gov/hmpip/",
+            "agencyProgramURL": "http://hmpip.fmcsa.dot.gov/hmpip/",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/8zt4-mm42",
-            "issued": "2014-10-17",
-            "temporal": "R/2014-10-17/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "carrier permit",
-                "hazardous material",
-                "permit"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jamie Vasser",
                 "hasEmail": "mailto:jamie.vasser@dot.gov"
             },
-            "identifier": "98.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": false,
+            "describedBy": "http://hmpip.fmcsa.dot.gov/hmpip/",
             "description": "Information related to the HMSP program. Located in the Hazardous Materials Package Inspection Program (HMPIP) application. HMPIP is FMCSA's legacy inspection and crash system, and supports Hazardous Materials Package Inspection.",
-            "title": "Hazardous Materials Safety Permit (HMSP) Program (HMPIP) - Hazardous Materials Safety Permit (HMSP) Program",
-            "agencyProgramURL": "http://hmpip.fmcsa.dot.gov/hmpip/",
-            "primaryITInvestmentUII": "021-000001003",
-            "programCode": [
-                "021:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24790,52 +24774,49 @@
                     "title": "Hazardous Materials Safety Permit (HMSP) Program"
                 }
             ],
-            "spatial": "Carrier, Vehicle",
-            "describedBy": "http://hmpip.fmcsa.dot.gov/hmpip/",
-            "dataQuality": false,
+            "identifier": "98.0",
+            "issued": "2014-10-17",
+            "keyword": [
+                "carrier permit",
+                "hazardous material",
+                "permit"
+            ],
+            "landingPage": "https://data.transportation.gov/d/8zt4-mm42",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://hmpip.fmcsa.dot.gov/hmpip/",
+            "modified": "2024-08-01",
+            "phone": "202-493-0215",
+            "primaryITInvestmentUII": "021-000001003",
+            "programCode": [
+                "021:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "rights": "Access is restricted to authorized Federal or State inspector personnel.",
+            "spatial": "Carrier, Vehicle",
+            "temporal": "R/2014-10-17/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "phone": "202-493-0215",
-            "language": [
-                "en-US"
-            ]
+            "title": "Hazardous Materials Safety Permit (HMSP) Program (HMPIP) - Hazardous Materials Safety Permit (HMSP) Program"
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
-            "identifier": "https://data.transportation.gov/api/views/922p-sj4m",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 1996",
-            "title": "Historic HPMS Data (Universe) - 1996",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -24843,50 +24824,84 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/922p-sj4m/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/922p-sj4m/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/922p-sj4m/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/922p-sj4m/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/922p-sj4m/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/922p-sj4m/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/922p-sj4m/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/922p-sj4m/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/922p-sj4m/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/922p-sj4m",
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
+            "title": "Historic HPMS Data (Universe) - 1996"
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
-            "landingPage": "https://data.transportation.gov/d/938g-fxvy",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/02febtvt/tvtfeb02.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "February 2002"
+                }
             ],
+            "identifier": "18.151",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -24896,119 +24911,83 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.151",
+            "landingPage": "https://data.transportation.gov/d/938g-fxvy",
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
-            "title": "Monthly Traffic Volume Trends - February 2002",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/02febtvt/tvtfeb02.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "February 2002"
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
+            "title": "Monthly Traffic Volume Trends - February 2002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/939q-bf5e",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2024-07-05",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-28",
-            "keyword": [
-                "aff",
-                "aviation facts & figures"
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
-            "identifier": "https://data.transportation.gov/api/views/939q-bf5e",
             "description": "Carrier on-time performance and causes of delay.",
-            "title": "Performance",
+            "identifier": "https://data.transportation.gov/api/views/939q-bf5e",
+            "issued": "2024-07-05",
+            "keyword": [
+                "aff",
+                "aviation facts & figures"
+            ],
+            "landingPage": "https://data.transportation.gov/d/939q-bf5e",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-28",
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
+            "title": "Performance"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.ntdprogram.gov/ntdprogram/data.htm",
+            "agencyProgramURL": "http://www.ntdprogram.gov; http://www.ntdprogram.gov/ntdprogram/data.htm",
+            "analysisUnit": "various",
             "bureauCode": [
                 "021:36"
             ],
-            "landingPage": "https://data.transportation.gov/d/947n-f8uz",
-            "issued": "2011-10-07",
-            "temporal": "R/2002-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-05",
+            "categoryDesignation": "Research",
             "collectionInstrument": "web-based reporting system",
-            "references": [
-                "http://www.ntdprogram.gov/ntdprogram/pubs/MonthlyRidership/2012/ridership.pdf"
-            ],
-            "keyword": [
-                "boardings",
-                "bus",
-                "miles",
-                "rail",
-                "riders",
-                "train",
-                "transit"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John D. Giorgis",
                 "hasEmail": "mailto:john.giorgis@dot.gov"
             },
-            "identifier": "19.6",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Transit Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.ntdprogram.gov/ntdprogram/Glossary.htm",
             "description": "Data collected monthly from urbanized area transit systems. The Monthly module includes a limited set of key indicators reported by transit properties. Data is reported on a monthly basis, by mode and type of service, for a calendar year. The four data items included are: Unlinked Passenger Trips, Vehicle Revenue Miles, Vehicle Revenue Hours, and Vehicles Operated in Maximum Service (Peak Vehicles). Monthly data are reported by mode and type of service.",
-            "title": "NTD Monthly Module Data Set - December 2015 Adjusted Data",
-            "isPartOf": "DOT-19",
-            "agencyProgramURL": "http://www.ntdprogram.gov; http://www.ntdprogram.gov/ntdprogram/data.htm",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25017,33 +24996,72 @@
                     "title": "December 2015 Adjusted Data"
                 }
             ],
-            "spatial": "Urbanized Area",
-            "describedBy": "http://www.ntdprogram.gov/ntdprogram/Glossary.htm",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.ntdprogram.gov/ntdprogram/data.htm",
-            "theme": [
-                "Transportation"
+            "identifier": "19.6",
+            "isPartOf": "DOT-19",
+            "issued": "2011-10-07",
+            "keyword": [
+                "boardings",
+                "bus",
+                "miles",
+                "rail",
+                "riders",
+                "train",
+                "transit"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Research",
-            "analysisUnit": "various",
-            "phone": "202-366-5430",
+            "landingPage": "https://data.transportation.gov/d/947n-f8uz",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-03-05",
+            "phone": "202-366-5430",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Transit Administration"
+            },
+            "references": [
+                "http://www.ntdprogram.gov/ntdprogram/pubs/MonthlyRidership/2012/ridership.pdf"
+            ],
+            "spatial": "Urbanized Area",
+            "temporal": "R/2002-01-01/P1M",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "NTD Monthly Module Data Set - December 2015 Adjusted Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/94sn-p439",
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
+                    "description": "2011 Connecticut HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/connecticut2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Connecticut"
+                }
+            ],
+            "identifier": "678.8",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -25057,82 +25075,46 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.8",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Connecticut",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/94sn-p439",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/connecticut2011.zip",
-                    "description": "2011 Connecticut HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Connecticut"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Connecticut"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "https://www.phmsa.dot.gov/guidance",
+            "agencyProgramURL": "https://www.phmsa.dot.gov/guidance",
+            "analysisUnit": "Regulations",
             "bureauCode": [
                 "021:50"
             ],
-            "landingPage": "https://data.transportation.gov/d/94sq-w3gp",
-            "issued": "2011-01-18",
-            "temporal": "2001-01-01/2011-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-23",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "https://www.phmsa.dot.gov/guidance"
-            ],
-            "keyword": [
-                "data.gov",
-                "law",
-                "significant guidance",
-                "transportation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Pipeline Safety",
                 "hasEmail": "mailto: PHMSA_Guidance@dot.gov"
             },
-            "identifier": "DOT-325",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Pipeline and Hazardous Materials Safety Administration"
-            },
+            "dataQuality": true,
             "description": "A list of Significant Guidance documents, which include guidance document disseminated to regulated entities or the general public that may reasonably be anticipated to lead to an annual effect on the economy of $100 million or more or adversely affect in a material way the economy, a sector of the economy, productivity, competition, jobs, the environment, public health or safety, or State, local, or tribal governments or communities; create a serious inconsistency or otherwise interfere with an action taken or planned by another agency; materially alter the budgetary impact of entitlements, grants, user fees, or loan programs or the rights and obligations of recipients thereof; or raise novel legal or policy issues arising out of legal mandates, the President's priorities, or the principles set forth in Executive Order 12866, as further amended.",
-            "title": "Significant Guidance on Pipeline Safety Issued by the Pipeline and Hazardous Materials Safety Administration",
-            "agencyProgramURL": "https://www.phmsa.dot.gov/guidance",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25140,86 +25122,115 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "DOT-325",
+            "issued": "2011-01-18",
+            "keyword": [
+                "data.gov",
+                "law",
+                "significant guidance",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/94sq-w3gp",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "https://www.phmsa.dot.gov/guidance",
+            "modified": "2024-10-23",
+            "phone": "202-366-4308",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Pipeline and Hazardous Materials Safety Administration"
+            },
+            "references": [
+                "https://www.phmsa.dot.gov/guidance"
+            ],
+            "temporal": "2001-01-01/2011-01-18",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "analysisUnit": "Regulations",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4308",
-            "language": [
-                "en-US"
-            ]
+            "title": "Significant Guidance on Pipeline Safety Issued by the Pipeline and Hazardous Materials Safety Administration"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/95pn-z8dk",
-            "issued": "2023-03-16",
             "@type": "dcat:Dataset",
-            "modified": "2023-03-16",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nazareth",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/95pn-z8dk",
+            "issued": "2023-03-16",
+            "landingPage": "https://data.transportation.gov/d/95pn-z8dk",
+            "modified": "2023-03-16",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "departures"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/96ee-pwhy",
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
-            "identifier": "https://data.transportation.gov/api/views/96ee-pwhy",
             "description": "Rail fatalities of persons who are on the part of railroad property used in railroad\r\noperation and whose presence is prohibited, forbidden, or unlawful. Fatalities may be reclassified upon subsequent reporting. The Federal Railroad Administration collects accident/incident and operational data from railroads.",
-            "title": "Rail Trespasser Fatalities Not at Highway-Rail Crossings",
+            "identifier": "https://data.transportation.gov/api/views/96ee-pwhy",
+            "issued": "2025-01-03",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/96ee-pwhy",
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
+            "title": "Rail Trespasser Fatalities Not at Highway-Rail Crossings"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.21949/1503755",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2015-05-31",
-            "@type": "dcat:Dataset",
-            "modified": "2017-01-18",
-            "references": [
-                "https://rosap.ntl.bts.gov/view/dot/3554"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Transportation Library Data Curator",
+                "hasEmail": "mailto:ntldatacurator@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The datasets in the .pdf and .zip attached to this record are in support of Intelligent Transportation Systems Joint Program Office (ITS JPO) report FHWA-JPO-15-222, \"Impacts Assessment of Dynamic Speed Harmonization with Queue Warning: Task 3, Impacts Assessment Report\". The files in these zip files are specifically related to the US-101 Testbed, near San Mateo, CA. The uncompressed and compressed files total 2.0265 GB in size. The files have been uploaded as-is; no further documentation was supplied by NTL. All located .docx files were converted to .pdf document files which are an open, archival format. These .pdfs were then added to the zip file alongside the original .docx files. The attached zip files can be unzipped using any zip compression/decompression software. These zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .xlsxm macro-enabled spreadsheet files which can be read in Microsoft Excel and some Tech Report spreadsheet programs; .accdb database files which may be opened with Microsoft Access Database software and Tech Report open database software applications ; as well as .db generic database files, often associated with thumbnail images in the Windows operating environment. [software requirements] These files were last accessed in 2017. File and .zip file names include: FHWA_JPO_15_222_INFLO_Performance_Measure_METADATA.pdf ; FHWA_JPO_15_222_INFLO_Performance_Measure_METADATA.docx ; FHWA_JPO_15_222_INFLO_VISSIM_Output_and_Analysis_Spreadsheets.zip ; FHWA_JPO_15_222_INFLO_Spreadsheet_PDFs.zip ; FHWA_JPO_15_222_DATA_CV50.zip ; and, FHWA_JPO_15_222_DATA_CV25.zip",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The datasets in the .pdf and .zip attached to this record are in support of Intelligent Transportation Systems Joint Program Office (ITS JPO) report FHWA-JPO-15-222, \"Impacts Assessment of Dynamic Speed Harmonization with Queue Warning: Task 3, Impacts Assessment Report\". The files in these zip files are specifically related to the US-101 Testbed, near San Mateo, CA. The uncompressed and compressed files total 2.0265 GB in size. The files have been uploaded as-is; no further documentation was supplied by NTL. All located .docx files were converted to .pdf document files which are an open, archival format. These .pdfs were then added to the zip file alongside the original .docx files. The attached zip files can be unzipped using any zip compression/decompression software. These zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .xlsxm macro-enabled spreadsheet files which can be read in Microsoft Excel and some Tech Report spreadsheet programs; .accdb database files which may be opened with Microsoft Access Database software and Tech Report open database software applications ; as well as .db generic database files, often associated with thumbnail images in the Windows operating environment. [software requirements] These files were last accessed in 2017. File and .zip file names include: FHWA_JPO_15_222_INFLO_Performance_Measure_METADATA.pdf ; FHWA_JPO_15_222_INFLO_Performance_Measure_METADATA.docx ; FHWA_JPO_15_222_INFLO_VISSIM_Output_and_Analysis_Spreadsheets.zip ; FHWA_JPO_15_222_INFLO_Spreadsheet_PDFs.zip ; FHWA_JPO_15_222_DATA_CV50.zip ; and, FHWA_JPO_15_222_DATA_CV25.zip",
+                    "downloadURL": "https://doi.org/10.21949/1503755",
+                    "mediaType": "application/zip",
+                    "title": "Impacts Assessment of Dynamic Speed Harmonization with Queue Warning: Task 3, Impacts Assessment Report [supporting datasets]"
+                }
             ],
+            "identifier": "https://data.transportation.gov/api/views/96k6-j8kv",
+            "issued": "2015-05-31",
             "keyword": [
                 "evaluation and assessment",
                 "intelligent network flow optimization simulation",
@@ -25229,63 +25240,37 @@
                 "traffic queuing",
                 "traffic simulation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Transportation Library Data Curator",
-                "hasEmail": "mailto:ntldatacurator@dot.gov"
-            },
+            "landingPage": "https://doi.org/10.21949/1503755",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2017-01-18",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/96k6-j8kv",
-            "description": "The datasets in the .pdf and .zip attached to this record are in support of Intelligent Transportation Systems Joint Program Office (ITS JPO) report FHWA-JPO-15-222, \"Impacts Assessment of Dynamic Speed Harmonization with Queue Warning: Task 3, Impacts Assessment Report\". The files in these zip files are specifically related to the US-101 Testbed, near San Mateo, CA. The uncompressed and compressed files total 2.0265 GB in size. The files have been uploaded as-is; no further documentation was supplied by NTL. All located .docx files were converted to .pdf document files which are an open, archival format. These .pdfs were then added to the zip file alongside the original .docx files. The attached zip files can be unzipped using any zip compression/decompression software. These zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .xlsxm macro-enabled spreadsheet files which can be read in Microsoft Excel and some Tech Report spreadsheet programs; .accdb database files which may be opened with Microsoft Access Database software and Tech Report open database software applications ; as well as .db generic database files, often associated with thumbnail images in the Windows operating environment. [software requirements] These files were last accessed in 2017. File and .zip file names include: FHWA_JPO_15_222_INFLO_Performance_Measure_METADATA.pdf ; FHWA_JPO_15_222_INFLO_Performance_Measure_METADATA.docx ; FHWA_JPO_15_222_INFLO_VISSIM_Output_and_Analysis_Spreadsheets.zip ; FHWA_JPO_15_222_INFLO_Spreadsheet_PDFs.zip ; FHWA_JPO_15_222_DATA_CV50.zip ; and, FHWA_JPO_15_222_DATA_CV25.zip",
-            "title": "Impacts Assessment of Dynamic Speed Harmonization with Queue Warning: Task 3, Impacts Assessment Report [supporting datasets]",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://doi.org/10.21949/1503755",
-                    "description": "The datasets in the .pdf and .zip attached to this record are in support of Intelligent Transportation Systems Joint Program Office (ITS JPO) report FHWA-JPO-15-222, \"Impacts Assessment of Dynamic Speed Harmonization with Queue Warning: Task 3, Impacts Assessment Report\". The files in these zip files are specifically related to the US-101 Testbed, near San Mateo, CA. The uncompressed and compressed files total 2.0265 GB in size. The files have been uploaded as-is; no further documentation was supplied by NTL. All located .docx files were converted to .pdf document files which are an open, archival format. These .pdfs were then added to the zip file alongside the original .docx files. The attached zip files can be unzipped using any zip compression/decompression software. These zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .xlsxm macro-enabled spreadsheet files which can be read in Microsoft Excel and some Tech Report spreadsheet programs; .accdb database files which may be opened with Microsoft Access Database software and Tech Report open database software applications ; as well as .db generic database files, often associated with thumbnail images in the Windows operating environment. [software requirements] These files were last accessed in 2017. File and .zip file names include: FHWA_JPO_15_222_INFLO_Performance_Measure_METADATA.pdf ; FHWA_JPO_15_222_INFLO_Performance_Measure_METADATA.docx ; FHWA_JPO_15_222_INFLO_VISSIM_Output_and_Analysis_Spreadsheets.zip ; FHWA_JPO_15_222_INFLO_Spreadsheet_PDFs.zip ; FHWA_JPO_15_222_DATA_CV50.zip ; and, FHWA_JPO_15_222_DATA_CV25.zip",
-                    "@type": "dcat:Distribution",
-                    "title": "Impacts Assessment of Dynamic Speed Harmonization with Queue Warning: Task 3, Impacts Assessment Report [supporting datasets]"
-                }
+            "references": [
+                "https://rosap.ntl.bts.gov/view/dot/3554"
             ],
             "spatial": "United States",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "language": [
-                "en-US"
-            ]
+            "title": "Impacts Assessment of Dynamic Speed Harmonization with Queue Warning: Task 3, Impacts Assessment Report [supporting datasets]"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/96tg-4mhf",
             "bureauCode": [
                 "021:17"
             ],
-            "issued": "2024-02-02",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
-            "keyword": [
-                "insurance",
-                "insurance rejection",
-                "motor carrier"
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
-            "identifier": "https://data.transportation.gov/api/views/96tg-4mhf",
             "description": "*Dataset* Information on insurance forms that were rejected by FMCSA. The dataset contains information on the insurance policy associated with the form, along with the date that the form was rejected and the reason for rejection (e.g., \u201cPolicy is already cancelled\u201d). The dataset contains the DOT number and docket number of the carrier/broker/freight forwarder associated with the policy. See dataset attachment \"FMCSA Dataset Description and Data Definitions - Select Datasets\" for more information.",
-            "title": "Rejected - All With History",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25293,64 +25278,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/96tg-4mhf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/96tg-4mhf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/96tg-4mhf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/96tg-4mhf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/96tg-4mhf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/96tg-4mhf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/96tg-4mhf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/96tg-4mhf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/96tg-4mhf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/96tg-4mhf",
+            "issued": "2024-02-02",
+            "keyword": [
+                "insurance",
+                "insurance rejection",
+                "motor carrier"
+            ],
+            "landingPage": "https://data.transportation.gov/d/96tg-4mhf",
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
+            "title": "Rejected - All With History"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.nhtsa.gov/equipment/takata-recall-spotlight",
             "bureauCode": [
                 "021:18"
             ],
-            "issued": "2022-05-23",
-            "temporal": "R/1949-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-13",
-            "keyword": [
-                "takata"
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
-            "identifier": "https://data.transportation.gov/api/views/97d8-fc99",
+            "dataQuality": true,
             "description": "",
-            "title": "Takata Recall \u2013 Net Air Bags Remaining",
-            "primaryITInvestmentUII": "021-777552743",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25358,72 +25341,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/97d8-fc99/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/97d8-fc99/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/97d8-fc99/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/97d8-fc99/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/97d8-fc99/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/97d8-fc99/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/97d8-fc99/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/97d8-fc99/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/97d8-fc99/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/97d8-fc99",
+            "issued": "2022-05-23",
+            "keyword": [
+                "takata"
+            ],
+            "landingPage": "https://www.nhtsa.gov/equipment/takata-recall-spotlight",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-08-13",
+            "primaryITInvestmentUII": "021-777552743",
+            "programCode": [
+                "021:035"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
             "spatial": "United States",
-            "dataQuality": true,
+            "temporal": "R/1949-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Takata Recall \u2013 Net Air Bags Remaining"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/97n2-kuqi",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2024-11-04",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-24",
-            "keyword": [
-                "aerial videography",
-                "automated vehicles",
-                "human-automated vehicle interactions",
-                "infrastructure-based videography",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "multi-modal trajectories",
-                "tgsim",
-                "third generation simulation",
-                "vehicle trajectory data"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyungjun Park",
                 "hasEmail": "mailto:hyungjun.park@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/97n2-kuqi",
             "description": "The main dataset is a 232 MB file of trajectory data (I395-final.csv) that contains position, speed, and acceleration data for non-automated passenger cars, trucks, buses, and automated vehicles on an expressway within an urban environment. Supporting files include an aerial reference image (I395_ref_image.png) and a list of polygon boundaries (I395_boundaries.csv) and associated images (I395_lane-1, I395_lane-2, \u2026, I395_lane-6) stored in a folder titled \u201cAnnotation on Regions.zip\u201d to map physical roadway segments to the numerical lane IDs referenced in the trajectory dataset. In the boundary file, columns \u201cx1\u201d to \u201cx5\u201d represent the horizontal pixel values in the reference image, with \u201cx1\u201d being the leftmost boundary line and \u201cx5\u201d being the rightmost boundary line, while the column \"y\" represents corresponding vertical pixel values. The origin point of the reference image is located at the top left corner. The dataset defines five lanes with five boundaries. Lane -6 corresponds to the area to the left of \u201cx1\u201d. Lane -5 corresponds to the area between \u201cx1\u201d and \u201cx2\u201d, and so forth to the rightmost lane, which is defined by the area to the right of \u201cx5\u201d (Lane -2). Lane -1 refers to vehicles that go onto the shoulder of the merging lane (Lane -2), which are manually separated by watching the videos.\n\nThis dataset was collected as part of the Third Generation Simulation Data (TGSIM): A Closer Look at the Impacts of Automated Driving Systems on Human Behavior project. During the project, six trajectory datasets capable of characterizing human-automated vehicle interactions under a diverse set of scenarios in highway and city environments were collected and processed. For more information, see the project report found here: https://rosap.ntl.bts.gov/view/dot/74647. This dataset, which was one of the six collected as part of the TGSIM project, contains data collected from six 4K cameras mounted on tripods, positioned on three overpasses along I-395 in Washington, D.C. The cameras captured distinct segments of the highway, and their combined overlapping and non-overlapping footage resulted in a continuous trajectory for the entire section covering 0.5 km. This section covers a major weaving/mandatory lane-changing between L'Enfant Plaza and 4th Street SW, with three lanes in the eastbound direction and a major on-ramp on the left side. In addition to the on-ramp, the section covers an off-ramp on the right side. The expressway includes one diverging lane at the beginning of the section on the right side and one merging lane in the middle of the section on the left side. For the purposes of data extraction, the shoulder of the merging lane is also considered a travel lane since some vehicles illegally use it as an extended on-ramp to pass other drivers (see I395_ref_image.png for details). The cameras captured continuous footage during the morning rush hour (8:30 AM-10:30 AM ET) on a sunny day. During this period, vehicles equipped with SAE Level 2 automation were deployed to travel through the designated section to capture the impact of SAE Level 2-equipped vehicles on adjacent vehicles and their behavior in congested areas, particularly in complex merging sections. These vehicles are indicated in the dataset.\n\nAs part of this dataset, the following files were provided:\n<ul><li>I395-final.csv contains the numerical data to be used for analysis that includes vehicle level trajectory data at every 0.1 second. Vehicle type, width, and length are provided with instantaneous location, speed, and acceleration data. All distance measurements (width, length, location) were converted from pixels to meters using the following conversion factor: 1 pixel = 0.3-meter conversion.</li>\n<li>I395_ref_image.png is the aerial reference image that defines the geographic region and the associated roadway segments.</li>\n<li>I395_boundaries.csv contains the coordinates that define the roadway segments (n=X). The columns \"x1\" to \"x5\" represent the horizontal pi",
-            "title": "Third Generation Simulation Data (TGSIM) I-395 Trajectories",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25431,47 +25406,87 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/97n2-kuqi/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/97n2-kuqi/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/97n2-kuqi/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/97n2-kuqi/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/97n2-kuqi/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/97n2-kuqi/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/97n2-kuqi/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/97n2-kuqi/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/97n2-kuqi/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "I-90/I94 in Chicago, IL; I-294 near Hinsdale, IL; I-395 in Washington DC; George Washington University Campus, Washington DC (Foggy Bottom)",
+            "identifier": "https://data.transportation.gov/api/views/97n2-kuqi",
+            "issued": "2024-11-04",
+            "keyword": [
+                "aerial videography",
+                "automated vehicles",
+                "human-automated vehicle interactions",
+                "infrastructure-based videography",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "multi-modal trajectories",
+                "tgsim",
+                "third generation simulation",
+                "vehicle trajectory data"
+            ],
+            "landingPage": "https://data.transportation.gov/d/97n2-kuqi",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-24",
+            "programCode": [
+                "021:042"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "spatial": "I-90/I94 in Chicago, IL; I-294 near Hinsdale, IL; I-395 in Washington DC; George Washington University Campus, Washington DC (Foggy Bottom)",
             "theme": [
                 "Automobiles"
-            ]
+            ],
+            "title": "Third Generation Simulation Data (TGSIM) I-395 Trajectories"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://www.safercar.gov/Safety+Ratings",
+            "agencyProgramURL": "http://www.safercar.gov/Vehicle+Shoppers",
+            "analysisUnit": "Vehicles",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/97pu-cz3y",
-            "issued": "2010-01-05",
-            "temporal": "R/1990-01-01/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Data is collected from a vehicle crash test conducted in a Laboratory facility.",
-            "references": [
-                "http://webapi.nhtsa.gov/Default.aspx%3FSafetyRatings/API/5"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": false,
+            "description": "NCAP rates vehicles to determine crash worthiness and rollover safety. The safety ratings are gathered during controlled crash and rollover tests conducted at NHTSA research facilities. Vehicles with a rating of five stars indicate the highest safety rating, whereas a one star indicates the lowest rating.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.safercar.gov/Vehicle+Shoppers/5-Star+Safety+Ratings/2011-Newer+Vehicles",
+                    "mediaType": "text/html",
+                    "title": "2011-Current Models"
+                }
             ],
+            "identifier": "248.8",
+            "isPartOf": "DOT-248",
+            "issued": "2010-01-05",
             "keyword": [
                 "5",
                 "assessment",
@@ -25485,81 +25500,46 @@
                 "safety",
                 "star"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "248.8",
+            "landingPage": "https://data.transportation.gov/d/97pu-cz3y",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-5269",
+            "programCode": [
+                "021:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Highway Traffic Safety Administration"
             },
-            "description": "NCAP rates vehicles to determine crash worthiness and rollover safety. The safety ratings are gathered during controlled crash and rollover tests conducted at NHTSA research facilities. Vehicles with a rating of five stars indicate the highest safety rating, whereas a one star indicates the lowest rating.",
-            "title": "New Car Assessment Program (NCAP) - 5 Star Safety Ratings - 2011-Current Models",
-            "isPartOf": "DOT-248",
-            "agencyProgramURL": "http://www.safercar.gov/Vehicle+Shoppers",
-            "programCode": [
-                "021:031"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.safercar.gov/Vehicle+Shoppers/5-Star+Safety+Ratings/2011-Newer+Vehicles",
-                    "mediaType": "text/html",
-                    "title": "2011-Current Models"
-                }
+            "references": [
+                "http://webapi.nhtsa.gov/Default.aspx%3FSafetyRatings/API/5"
             ],
             "spatial": "N/A",
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.safercar.gov/Safety+Ratings",
+            "temporal": "R/1990-01-01/P1D",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Vehicles",
-            "phone": "202-366-5269",
-            "language": [
-                "en-US"
-            ]
+            "title": "New Car Assessment Program (NCAP) - 5 Star Safety Ratings - 2011-Current Models"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "internal system with named users",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/97t5-j3wi",
-            "issued": "2018-12-18",
-            "temporal": "R/2013/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "applications",
-                "highway",
-                "hsp",
-                "plans",
-                "safety"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "535.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
             "description": "The Traffic Records Improvement Program Reporting System (TRIPRS) contains detailedinformation on all projects contained in the strategic plans submitted by the states and U.S.Territories for the NHTSA Section 408 grant application. Recently, it has been adopted byFMCSA, FHWA, and the US-DOT TRCC as a tool to track all safety data improvement fundsgiven to states. Reporting tool supported by NCSA. NATIONAL DRIVER REGISTER & TRAFFIC RECORDS (NVS-422).",
-            "title": "TRIPRS -",
-            "primaryITInvestmentUII": "021-302996647",
-            "programCode": [
-                "021:033"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25567,89 +25547,92 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
-            ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
+            "identifier": "535.0",
+            "issued": "2018-12-18",
+            "keyword": [
+                "applications",
+                "highway",
+                "hsp",
+                "plans",
+                "safety"
+            ],
+            "landingPage": "https://data.transportation.gov/d/97t5-j3wi",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-5649"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-01",
+            "phone": "202-366-5649",
+            "primaryITInvestmentUII": "021-302996647",
+            "programCode": [
+                "021:033"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "rights": "internal system with named users",
+            "temporal": "R/2013/P1Y",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "TRIPRS -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/98fi-ujit",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2025-01-16",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-16",
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
-            "identifier": "https://data.transportation.gov/api/views/98fi-ujit",
             "description": "Customer on-time performance is the percentage of customers who arrive at their detraining stations on time. An Acela train is late when it arrives at a station more than 10 minutes after its scheduled time; a Northeast Regional or State-Supported train is late when it arrives more than 15 minutes after its scheduled time. For years before FY 2018, on-time performance is the percentage of total train arrivals on-time at each station, with every arrival weighted equally. Amtrak reports system performance in monthly Host Railroad Reports.",
-            "title": "Amtrak On-Time Performance",
+            "identifier": "https://data.transportation.gov/api/views/98fi-ujit",
+            "issued": "2025-01-16",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/98fi-ujit",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-16",
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
+            "title": "Amtrak On-Time Performance"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "rights": "Login required. Review terms of use on Web page.",
+            "accrualPeriodicity": "R/P1W",
+            "agencyDataSeriesURL": "https://gradedec.fra.dot.gov/",
+            "agencyProgramURL": "https://gradedec.fra.dot.gov/",
+            "analysisUnit": "highway-rail grade crossing",
             "bureauCode": [
                 "021:27"
             ],
-            "landingPage": "https://data.transportation.gov/d/98vi-ci49",
-            "issued": "2014-11-21",
-            "temporal": "R/2014-11-21/P1W",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-10-09",
-            "references": [
-                "https://gradedec.fra.dot.gov/"
-            ],
-            "keyword": [
-                "fra system for highway-rail grade crossing",
-                "gade crossing invetment analysis"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Railroad Safety",
                 "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
             },
-            "identifier": "DOT-664",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Railroad Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "https://gradedec.fra.dot.gov/",
             "description": "General Purpose Data and Statistics.  GradeDEC.Net is a web-based tool for the investment analysis of highway-rail grade crossing improvements.  It provides state departments of transportation, local governments, metropolitan planning agencies, inspectors, and railroad companies with the online ability to conduct benefit-cost analysis of highway-rail grade crossing infrastructure investments. GradeDEC.Net allows users to divert highway traffic to and from closed or separated grade crossings to adjacent crossings, and calculate a full set of benefits including changes in accident risk associated with changes in traditional grade crossing technology. Users can also evaluate supplemental safety measures listed in the Notice of Proposed Rulemaking covering the use of locomotive horns at highway-rail grade crossing. Users are also able to save an analysis on-site for later revision and update and submit reports directly to the FRA.",
-            "title": "GradeDec.Net",
-            "agencyProgramURL": "https://gradedec.fra.dot.gov/",
-            "primaryITInvestmentUII": "021-092395457",
-            "programCode": [
-                "021:036"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25658,40 +25641,47 @@
                     "title": "Online Tool"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "https://gradedec.fra.dot.gov/",
-            "dataQuality": true,
+            "identifier": "DOT-664",
+            "issued": "2014-11-21",
+            "keyword": [
+                "fra system for highway-rail grade crossing",
+                "gade crossing invetment analysis"
+            ],
+            "landingPage": "https://data.transportation.gov/d/98vi-ci49",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "https://gradedec.fra.dot.gov/",
+            "modified": "2024-10-09",
+            "phone": "202-493-6417",
+            "primaryITInvestmentUII": "021-092395457",
+            "programCode": [
+                "021:036"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Railroad Administration"
+            },
+            "references": [
+                "https://gradedec.fra.dot.gov/"
+            ],
+            "rights": "Login required. Review terms of use on Web page.",
+            "spatial": "Point",
+            "temporal": "R/2014-11-21/P1W",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1W",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "highway-rail grade crossing",
-            "phone": "202-493-6417",
-            "language": [
-                "en-US"
-            ]
+            "title": "GradeDec.Net"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/99cm-4dgn",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-06",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/99cm-4dgn",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "Rail Crossings",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25699,65 +25689,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/99cm-4dgn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/99cm-4dgn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/99cm-4dgn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/99cm-4dgn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/99cm-4dgn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/99cm-4dgn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/99cm-4dgn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/99cm-4dgn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/99cm-4dgn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/99cm-4dgn",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/99cm-4dgn",
+            "modified": "2025-01-06",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Rail Crossings"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "rights": "Accessible to public as long as they register to receive data.",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www.itsforge.net",
+            "agencyProgramURL": "http://www.its.dot.gov/dma/",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/9ace-muef",
-            "issued": "2014-09-15",
-            "temporal": "2014-09-15/2014-09-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "code",
-                "open source",
-                "research"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "713.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": false,
             "description": "Open Source Application Development Portal (OSADP). The system provides a place for programmers to share software code and solutions.",
-            "title": "Open Source Application  Development Portal - Website",
-            "isPartOf": "DOT-713",
-            "agencyProgramURL": "http://www.its.dot.gov/dma/",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25766,33 +25749,64 @@
                     "title": "Website"
                 }
             ],
-            "dataQuality": false,
+            "identifier": "713.1",
+            "isPartOf": "DOT-713",
+            "issued": "2014-09-15",
+            "keyword": [
+                "code",
+                "open source",
+                "research"
+            ],
+            "landingPage": "https://data.transportation.gov/d/9ace-muef",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.itsforge.net",
+            "modified": "2024-05-08",
+            "phone": "202-366-6993",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "rights": "Accessible to public as long as they register to receive data.",
+            "temporal": "2014-09-15/2014-09-15",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "phone": "202-366-6993",
-            "language": [
-                "en-US"
-            ]
+            "title": "Open Source Application  Development Portal - Website"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyProgramURL": "http://www.nhtsa.gov/fuel-economy",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/9bix-dk6t",
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
+                    "description": "The NHTSA fleet and manufacturer reports provide comparisons of fuel economy performance data in relationship to the required fuel economy standards for each model year. Also available in PDF and XLS.",
+                    "downloadURL": "http://www.nhtsa.gov/CAFE_PIC/CAFE_PIC_fleet_LIVE.html",
+                    "mediaType": "text/html",
+                    "title": "Fleet Fuel Economy Performance Report"
+                }
             ],
+            "identifier": "1862.2",
+            "isPartOf": "DOT-1862",
+            "issued": "2015-12-16",
             "keyword": [
                 "amfa",
                 "civil penalties",
@@ -25809,58 +25823,59 @@
                 "report",
                 "shortfall"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "1862.2",
+            "landingPage": "https://data.transportation.gov/d/9bix-dk6t",
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
-            "title": "CAFE (Corporate Average Fuel Economy) - Fleet Fuel Economy Performance Report",
-            "isPartOf": "DOT-1862",
-            "agencyProgramURL": "http://www.nhtsa.gov/fuel-economy",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.nhtsa.gov/CAFE_PIC/CAFE_PIC_fleet_LIVE.html",
-                    "description": "The NHTSA fleet and manufacturer reports provide comparisons of fuel economy performance data in relationship to the required fuel economy standards for each model year. Also available in PDF and XLS.",
-                    "@type": "dcat:Distribution",
-                    "title": "Fleet Fuel Economy Performance Report"
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
+            "title": "CAFE (Corporate Average Fuel Economy) - Fleet Fuel Economy Performance Report"
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
-            "landingPage": "https://data.transportation.gov/d/9ccf-q6pv",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/11febtvt/11febtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "February 2011"
+                }
             ],
+            "identifier": "18.13",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -25870,57 +25885,60 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.13",
+            "landingPage": "https://data.transportation.gov/d/9ccf-q6pv",
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
-            "title": "Monthly Traffic Volume Trends - February 2011",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/11febtvt/11febtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "February 2011"
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
+            "title": "Monthly Traffic Volume Trends - February 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/9cmi-8uvr",
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
+                    "description": "2012 Colorado HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/colorado2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Colorado"
+                }
+            ],
+            "identifier": "678.59",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -25934,64 +25952,36 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.59",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Colorado",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/9cmi-8uvr",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/colorado2012.zip",
-                    "description": "2012 Colorado HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Colorado"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Colorado"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/9cve-7fcm",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/9cve-7fcm",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "Class 1s",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25999,100 +25989,93 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9cve-7fcm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9cve-7fcm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9cve-7fcm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/9cve-7fcm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9cve-7fcm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9cve-7fcm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9cve-7fcm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9cve-7fcm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9cve-7fcm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/9cve-7fcm",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/9cve-7fcm",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Class 1s"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/9czv-tjte",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Visualizations featuring BTS' Transportation Services Index (TSI). The TSI measures the monthly movement of freight and passengers .",
+            "identifier": "https://data.transportation.gov/api/views/9czv-tjte",
             "issued": "2020-02-12",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
             "keyword": [
                 "economic indicators",
                 "transportation",
                 "transportation services index"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/9czv-tjte",
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
-            "identifier": "https://data.transportation.gov/api/views/9czv-tjte",
-            "description": "Visualizations featuring BTS' Transportation Services Index (TSI). The TSI measures the monthly movement of freight and passengers .",
-            "title": "Transportation as an Economic Indicator",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Transportation as an Economic Indicator"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "rights": "Accessible to public as long as they register to receive data.",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www.itsforge.net",
+            "agencyProgramURL": "http://www.its.dot.gov/dma/",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/9dsi-k656",
-            "issued": "2014-09-15",
-            "temporal": "2014-09-15/2014-09-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "code",
-                "open source",
-                "research"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "713.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": false,
             "description": "Open Source Application Development Portal (OSADP). The system provides a place for programmers to share software code and solutions.",
-            "title": "Open Source Application  Development Portal - Website",
-            "isPartOf": "DOT-713",
-            "agencyProgramURL": "http://www.its.dot.gov/dma/",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26101,33 +26084,64 @@
                     "title": "Website"
                 }
             ],
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.itsforge.net",
-            "theme": [
-                "Transportation"
-            ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "phone": "202-366-6993",
+            "identifier": "713.2",
+            "isPartOf": "DOT-713",
+            "issued": "2014-09-15",
+            "keyword": [
+                "code",
+                "open source",
+                "research"
+            ],
+            "landingPage": "https://data.transportation.gov/d/9dsi-k656",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-6993",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "rights": "Accessible to public as long as they register to receive data.",
+            "temporal": "2014-09-15/2014-09-15",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Open Source Application  Development Portal - Website"
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
-            "landingPage": "https://data.transportation.gov/d/9f3r-vh4z",
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
+            "identifier": "114.1",
+            "isPartOf": "DOT-114",
+            "issued": "2018-12-17",
             "keyword": [
                 "a&i",
                 "a&i online",
@@ -26147,77 +26161,43 @@
                 "safety programs",
                 "traffic enforcement"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "114.1",
+            "landingPage": "https://data.transportation.gov/d/9f3r-vh4z",
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
```

