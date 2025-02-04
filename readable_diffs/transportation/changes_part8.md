# Change History for transportation.json (Part 8)

### Changes from 31606f9 to dd2190f (Part 7/9)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-                    "downloadURL": "https://data.transportation.gov/api/views/q4t7-b6y5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/q4t7-b6y5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/q4t7-b6y5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/q4t7-b6y5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/q4t7-b6y5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/q4t7-b6y5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/q4t7-b6y5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/q4t7-b6y5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/q4t7-b6y5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/q4t7-b6y5",
+            "issued": "2024-03-27",
+            "keyword": [
+                "air",
+                "cost",
+                "hwy"
+            ],
+            "landingPage": "https://maps.dot.gov/fhwa/iit/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-04-23",
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
-                "en-US"
-            ]
+            "title": "Inequity Identification Tool (IIT) Air Cost"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/q4tb-tbff",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2024-09-26",
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
-            "identifier": "https://data.transportation.gov/api/views/q4tb-tbff",
             "description": "Commercial air passengers, seats, freight, and mail by air carrier summary.",
-            "title": "AFF - T100 Segment Summary By Carrier",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79235,72 +79216,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/q4tb-tbff/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/q4tb-tbff/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/q4tb-tbff/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/q4tb-tbff/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/q4tb-tbff/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/q4tb-tbff/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/q4tb-tbff/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/q4tb-tbff/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/q4tb-tbff/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/q4tb-tbff",
+            "issued": "2024-09-26",
+            "keyword": [
+                "aff",
+                "air carriers",
+                "aviation facts & figures",
+                "passengers"
+            ],
+            "landingPage": "https://data.transportation.gov/d/q4tb-tbff",
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
+            "title": "AFF - T100 Segment Summary By Carrier"
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
-            "landingPage": "https://data.transportation.gov/d/q5ni-p38u",
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
-            "identifier": "18.35",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - April 2009",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79309,56 +79287,59 @@
                     "title": "April 2009"
                 }
             ],
-            "spatial": "Vehicles by type of functional classified roadway",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
-            "theme": [
-                "Transportation"
+            "identifier": "18.35",
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
+            "landingPage": "https://data.transportation.gov/d/q5ni-p38u",
             "language": [
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
             },
-        {
-            "accessLevel": "non-public",
-            "rights": "contact POC",
-            "bureauCode": [
-                "021:18"
+            "references": [
+                "http://www.fhwa.dot.gov/ohim/tvtw/tvtfaq.cfm"
             ],
-            "landingPage": "https://data.transportation.gov/d/q658-uq5q",
-            "issued": "2018-12-18",
-            "temporal": "R/2014/PT1S",
-            "@type": "dcat:Dataset",
-            "collectionInstrument": "Transportation",
-            "modified": "2024-05-01",
-            "keyword": [
-                "archives",
-                "disposition",
-                "nara",
-                "record schedules"
+            "spatial": "Vehicles by type of functional classified roadway",
+            "temporal": "R/1970-01-01/P1M",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Monthly Traffic Volume Trends - April 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "accrualPeriodicity": "R/PT1S",
+            "agencyProgramURL": "http://www.dot.gov/records",
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
-            "identifier": "DOT-484",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
             "description": "Contains NHTSA record schedules. SYSTEMS INTEGRATION (NPO-430)",
-            "title": "Comprehensive Records Schedule",
-            "primaryITInvestmentUII": "021-381281982",
-            "agencyProgramURL": "http://www.dot.gov/records",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79367,32 +79348,66 @@
                     "title": "Comprehensive Record Schedule"
                 }
             ],
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "DOT-484",
+            "issued": "2018-12-18",
+            "keyword": [
+                "archives",
+                "disposition",
+                "nara",
+                "record schedules"
             ],
-            "accrualPeriodicity": "R/PT1S",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/q658-uq5q",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-4939"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-01",
+            "phone": "202-366-4939",
+            "primaryITInvestmentUII": "021-381281982",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "rights": "contact POC",
+            "temporal": "R/2014/PT1S",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Comprehensive Records Schedule"
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
-            "landingPage": "https://data.transportation.gov/d/q88g-apk3",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/05novtvt/05novtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "November 2005"
+                }
             ],
+            "identifier": "18.106",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -79402,60 +79417,60 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.106",
+            "landingPage": "https://data.transportation.gov/d/q88g-apk3",
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
-            "title": "Monthly Traffic Volume Trends - November 2005",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/05novtvt/05novtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "November 2005"
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
+            "title": "Monthly Traffic Volume Trends - November 2005"
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
-            "landingPage": "https://data.transportation.gov/d/q8pj-vnpr",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/05dectvt/05dectvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "December 2005"
+                }
             ],
+            "identifier": "18.105",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -79465,64 +79480,39 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.105",
+            "landingPage": "https://data.transportation.gov/d/q8pj-vnpr",
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
-            "title": "Monthly Traffic Volume Trends - December 2005",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/05dectvt/05dectvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "December 2005"
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
+            "title": "Monthly Traffic Volume Trends - December 2005"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/q9r2-en22",
-            "issued": "2024-01-16",
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
-            "identifier": "https://data.transportation.gov/api/views/q9r2-en22",
             "description": "",
-            "title": "Railroad Master",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79530,57 +79520,53 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/q9r2-en22/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/q9r2-en22/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/q9r2-en22/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/q9r2-en22/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/q9r2-en22/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/q9r2-en22/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/q9r2-en22/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/q9r2-en22/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/q9r2-en22/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/q9r2-en22",
+            "issued": "2024-01-16",
+            "landingPage": "https://data.transportation.gov/d/q9r2-en22",
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
+            "title": "Railroad Master"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/qbt8-7vic",
             "bureauCode": [
                 "021:17"
             ],
-            "issued": "2024-04-25",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
-            "keyword": [
-                "citations",
-                "violation"
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
-            "identifier": "https://data.transportation.gov/api/views/qbt8-7vic",
             "description": "The report includes inspections and associated citations.",
-            "title": "Inspections and Citations",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79588,49 +79574,79 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/qbt8-7vic/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/qbt8-7vic/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/qbt8-7vic/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/qbt8-7vic/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/qbt8-7vic/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/qbt8-7vic/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/qbt8-7vic/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/qbt8-7vic/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/qbt8-7vic/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/qbt8-7vic",
+            "issued": "2024-04-25",
+            "keyword": [
+                "citations",
+                "violation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/qbt8-7vic",
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
+            "title": "Inspections and Citations"
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
-            "landingPage": "https://data.transportation.gov/d/qby7-8iab",
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
+                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/nits/Nontraffic%20crashes/2010/",
+                    "mediaType": "text/plain",
+                    "title": "2010 Nontraffic Crashes"
+                }
             ],
+            "identifier": "288.9",
+            "isPartOf": "DOT-288",
+            "issued": "2009-01-27",
             "keyword": [
                 "crash",
                 "death",
@@ -79646,86 +79662,49 @@
                 "vehicle",
                 "victim"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "288.9",
+            "landingPage": "https://data.transportation.gov/d/qby7-8iab",
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
-            "title": "Not in Traffic Surveillance (NiTS) - 2010 Nontraffic Crashes",
-            "isPartOf": "DOT-288",
-            "agencyProgramURL": "http://www.nhtsa.gov/Data/State+Data+Programs",
-            "programCode": [
-                "021:032"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/nits/Nontraffic%20crashes/2010/",
-                    "mediaType": "text/plain",
-                    "title": "2010 Nontraffic Crashes"
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
+            "title": "Not in Traffic Surveillance (NiTS) - 2010 Nontraffic Crashes"
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
-            "landingPage": "https://data.transportation.gov/d/qcu5-k7kx",
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
-            "identifier": "524.20",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
             "description": "STATE DATA REPORTING SYSTEMS. Annual reports on the Fatality Analysis Reporting System (FARS) which is data regarding fatalities that is collected by a FARS analyst from each State and provided to NHTSA.",
-            "title": "GES Reports - 1993",
-            "isPartOf": "DOT-524",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79734,35 +79713,71 @@
                     "title": "1993"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
-            "dataQuality": true,
+            "identifier": "524.20",
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
+            "landingPage": "https://data.transportation.gov/d/qcu5-k7kx",
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
+            "title": "GES Reports - 1993"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "https://www.phmsa.dot.gov/data-and-statistics/pipeline/pipeline-incident-flagged-files",
+            "agencyProgramURL": "http://www.phmsa.dot.gov/pipeline",
+            "analysisUnit": "Accident/Incident",
             "bureauCode": [
                 "021:50"
             ],
-            "landingPage": "https://data.transportation.gov/d/qdme-9bbm",
-            "issued": "1992-01-01",
-            "temporal": "R/1992-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-29",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.phmsa.dot.gov/pipeline"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Muhammed Jamil",
+                "hasEmail": "mailto:PHMSAPHPDataandStatistics@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "In the flagged files, PHMSA add data that are routinely used during data analysis and when presenting certain 20-year trends. Information includes: serious incidents (involving a fatality or injury requiring in-patient hospitalization), significant incidents (meet a number of predefined conditions, including inflation adjusted value of property damage, minimum threshold for volume spilled for hazardous liquid, fire and explosion for hazardous liquid), reported incidents (all pipeline incidents reported to PHMSA in accordance with reporting criterion which has changed over time), consequences (effects on both the general public and the pipeline industry), and state-based reports.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.phmsa.dot.gov/pipeline/library/datastatistics/pipelineincidenttrends",
+                    "mediaType": "text/html",
+                    "title": "Data Mining Tool"
+                }
             ],
+            "identifier": "32.2",
+            "isPartOf": "DOT-32",
+            "issued": "1992-01-01",
             "keyword": [
                 "consequence",
                 "damage",
@@ -79778,60 +79793,61 @@
                 "report",
                 "safety"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Muhammed Jamil",
-                "hasEmail": "mailto:PHMSAPHPDataandStatistics@dot.gov"
-            },
-            "identifier": "32.2",
+            "landingPage": "https://data.transportation.gov/d/qdme-9bbm",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-07-29",
+            "phone": "202-366-1878",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Pipeline and Hazardous Materials Safety Administration"
             },
-            "description": "In the flagged files, PHMSA add data that are routinely used during data analysis and when presenting certain 20-year trends. Information includes: serious incidents (involving a fatality or injury requiring in-patient hospitalization), significant incidents (meet a number of predefined conditions, including inflation adjusted value of property damage, minimum threshold for volume spilled for hazardous liquid, fire and explosion for hazardous liquid), reported incidents (all pipeline incidents reported to PHMSA in accordance with reporting criterion which has changed over time), consequences (effects on both the general public and the pipeline industry), and state-based reports.",
-            "title": "Pipeline Incident Flagged Files",
-            "isPartOf": "DOT-32",
-            "agencyProgramURL": "http://www.phmsa.dot.gov/pipeline",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.phmsa.dot.gov/pipeline/library/datastatistics/pipelineincidenttrends",
-                    "mediaType": "text/html",
-                    "title": "Data Mining Tool"
-                }
+            "references": [
+                "http://www.phmsa.dot.gov/pipeline"
             ],
             "spatial": "County",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "https://www.phmsa.dot.gov/data-and-statistics/pipeline/pipeline-incident-flagged-files",
+            "temporal": "R/1992-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Accident/Incident",
-            "phone": "202-366-1878",
-            "language": [
-                "en-US"
-            ]
+            "title": "Pipeline Incident Flagged Files"
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
-            "landingPage": "https://data.transportation.gov/d/qear-77qc",
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
+                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/nits/Noncrash%20fatalities/2003-2004/NiTS%202003-2004%20noncrash%20fatalities.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2003-2004 Noncrash Fatalities"
+                }
             ],
+            "identifier": "288.1",
+            "isPartOf": "DOT-288",
+            "issued": "2009-01-27",
             "keyword": [
                 "crash",
                 "death",
@@ -79847,144 +79863,114 @@
                 "vehicle",
                 "victim"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "288.1",
+            "landingPage": "https://data.transportation.gov/d/qear-77qc",
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
-            "title": "Not in Traffic Surveillance (NiTS) - 2003-2004 Noncrash Fatalities",
-            "isPartOf": "DOT-288",
-            "agencyProgramURL": "http://www.nhtsa.gov/Data/State+Data+Programs",
-            "programCode": [
-                "021:032"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/nits/Noncrash%20fatalities/2003-2004/NiTS%202003-2004%20noncrash%20fatalities.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "2003-2004 Noncrash Fatalities"
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
+            "title": "Not in Traffic Surveillance (NiTS) - 2003-2004 Noncrash Fatalities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/qeh3-a6ec",
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
-            "identifier": "https://data.transportation.gov/api/views/qeh3-a6ec",
             "description": "The Federal Highway Administration estimates vehicle miles traveled on all roads and streets in each month.",
-            "title": "Highway Travel - All Systems",
+            "identifier": "https://data.transportation.gov/api/views/qeh3-a6ec",
+            "issued": "2025-01-15",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/qeh3-a6ec",
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
+            "title": "Highway Travel - All Systems"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/qfc9-tapk",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This dataset is updated monthly, on the first of the month. Data is released on a three-month delay. Railroads have up to 59 days to report and then there is 30 days for processing data. For example, data for the month of January would become available on April 1.\r\nData is currently available through May 31, 2023.",
+            "identifier": "https://data.transportation.gov/api/views/qfc9-tapk",
             "issued": "2023-08-08",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-01",
             "keyword": [
                 "data",
                 "release",
                 "schedule"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/qfc9-tapk",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-01",
+            "programCode": [
+                "021:036"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Railroad Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/qfc9-tapk",
-            "description": "This dataset is updated monthly, on the first of the month. Data is released on a three-month delay. Railroads have up to 59 days to report and then there is 30 days for processing data. For example, data for the month of January would become available on April 1.\r\nData is currently available through May 31, 2023.",
-            "title": "Data Release Schedule",
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
+            "title": "Data Release Schedule"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/qh9u-swkp",
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
-            "identifier": "https://data.transportation.gov/api/views/qh9u-swkp",
             "description": "*Dataset*  Information on the implementation dates of an active or pending insurance policy (posted date, effective date and cancel effective date). In addition to these dates, the record contains the insurance company name, the BI&PD underlying limit and maximum limit amounts, and the DOT number and docket number of the carrier/broker/freight forwarder that holds the policy.\nSee dataset attachment \"FMCSA Dataset Description and Data Definitions - Select Datasets\" for more information.",
-            "title": "ActPendInsur - All With History",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79992,73 +79978,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/qh9u-swkp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/qh9u-swkp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/qh9u-swkp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/qh9u-swkp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/qh9u-swkp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/qh9u-swkp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/qh9u-swkp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/qh9u-swkp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/qh9u-swkp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/qh9u-swkp",
+            "issued": "2024-02-02",
+            "keyword": [
+                "insurance",
+                "motor carrier"
+            ],
+            "landingPage": "https://data.transportation.gov/d/qh9u-swkp",
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
+            "title": "ActPendInsur - All With History"
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
-            "landingPage": "https://data.transportation.gov/d/qhcq-ftng",
-            "issued": "2014-10-31",
-            "temporal": "R/2008-07-01/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
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
-            "identifier": "DOT-559",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": true,
+            "describedBy": "https://www.civilrights.dot.gov/disadvantaged-business-enterprise/search-dbe-appeals-and-denials",
             "description": "List of DBEs and ACDBEs that have been rejected DBE status by state UCP officials. The information in this database, along with the decision to deny, decertify or reject an application, is maintained by State administered Unified Certification Programs (UCP). Firms identified in this database are ineligible for Federal Transportation grants made available specifically for DBEs.  Currently, the data set is available on the web at: https://www.civilrights.dot.gov/disadvantaged-business-enterprise/search-dbe-appeals-and-denials",
-            "title": "Decertified Disadvantaged Business Enterprises (DBE) and Airport Concession DBE List",
-            "agencyProgramURL": "https://www.civilrights.dot.gov/disadvantaged-business-enterprise",
-            "primaryITInvestmentUII": "021-908746511",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80067,59 +80048,59 @@
                     "title": "Search Appeals and Decisions"
                 }
             ],
-            "spatial": "Address",
-            "describedBy": "https://www.civilrights.dot.gov/disadvantaged-business-enterprise/search-dbe-appeals-and-denials",
-            "dataQuality": true,
+            "identifier": "DOT-559",
+            "issued": "2014-10-31",
+            "keyword": [
+                "appeal",
+                "certification",
+                "dbe",
+                "decertification",
+                "disadvantaged business enterprise"
+            ],
+            "landingPage": "https://data.transportation.gov/d/qhcq-ftng",
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
+            "title": "Decertified Disadvantaged Business Enterprises (DBE) and Airport Concession DBE List"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/guidance/fhwaguidance.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/guidance/fhwaguidance.cfm",
+            "analysisUnit": "Regulations",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/qhsn-akq4",
-            "issued": "2011-01-18",
-            "temporal": "2007-01-01/2013-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.fhwa.dot.gov/guidance/fhwaguidance.cfm"
-            ],
-            "keyword": [
-                "data.gov",
-                "law",
-                "significant guidance",
-                "transportation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "DOT-302",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "A list of Significant Guidance documents, which include guidance document disseminated to regulated entities or the general public that may reasonably be anticipated to lead to an annual effect on the economy of $100 million or more or adversely affect in a material way the economy, a sector of the economy, productivity, competition, jobs, the environment, public health or safety, or State, local, or tribal governments or communities; create a serious inconsistency or otherwise interfere with an action taken or planned by another agency; materially alter the budgetary impact of entitlements, grants, user fees, or loan programs or the rights and obligations of recipients thereof; or raise novel legal or policy issues arising out of legal mandates, the President's priorities, or the principles set forth in Executive Order 12866, as further amended.",
-            "title": "Significant Guidance Issued by the Federal Highway Administration",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/guidance/fhwaguidance.cfm",
-            "primaryITInvestmentUII": "021-803057200",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80127,56 +80108,90 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "DOT-302",
+            "issued": "2011-01-18",
+            "keyword": [
+                "data.gov",
+                "law",
+                "significant guidance",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/qhsn-akq4",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/guidance/fhwaguidance.cfm",
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
+                "http://www.fhwa.dot.gov/guidance/fhwaguidance.cfm"
+            ],
+            "temporal": "2007-01-01/2013-12-31",
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
+            "title": "Significant Guidance Issued by the Federal Highway Administration"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/qi7d-992b",
-            "issued": "2020-09-01",
             "@type": "dcat:Dataset",
-            "modified": "2020-09-10",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Admin Team",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
+            "description": "This story provides an overview of Socrata's analytics datasets and describes them for users.",
             "identifier": "https://data.transportation.gov/api/views/qi7d-992b",
+            "issued": "2020-09-01",
+            "landingPage": "https://data.transportation.gov/d/qi7d-992b",
+            "modified": "2020-09-10",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "This story provides an overview of Socrata's analytics datasets and describes them for users.",
-            "title": "Site Analytics",
             "theme": [
                 "Administrative"
-            ]
+            ],
+            "title": "Site Analytics"
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
-            "landingPage": "https://data.transportation.gov/d/qia7-gy2z",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/02novtvt/02NOVtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "November 2003"
+                }
             ],
+            "identifier": "18.130",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -80186,60 +80201,60 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.130",
+            "landingPage": "https://data.transportation.gov/d/qia7-gy2z",
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
-            "title": "Monthly Traffic Volume Trends - November 2003",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/02novtvt/02NOVtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "November 2003"
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
+            "title": "Monthly Traffic Volume Trends - November 2003"
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
-            "landingPage": "https://data.transportation.gov/d/qj6e-5iig",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/11augtvt/11augtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "August 2011"
+                }
             ],
+            "identifier": "18.7",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -80249,74 +80264,43 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.7",
+            "landingPage": "https://data.transportation.gov/d/qj6e-5iig",
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
-            "title": "Monthly Traffic Volume Trends - August 2011",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/11augtvt/11augtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "August 2011"
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
+            "title": "Monthly Traffic Volume Trends - August 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2021-06-23",
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
-            "identifier": "https://data.transportation.gov/api/views/qjsn-7dw8",
+            "dataQuality": true,
             "description": "2016 Traffic Volume Data - FHWA's TMAS Data Program (based on unweighted raw continuous traffic count information collected by state highway agencies)",
-            "title": "TMAS 2016",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80324,67 +80308,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/qjsn-7dw8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/qjsn-7dw8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/qjsn-7dw8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/qjsn-7dw8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/qjsn-7dw8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/qjsn-7dw8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/qjsn-7dw8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/qjsn-7dw8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/qjsn-7dw8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/qjsn-7dw8",
+            "issued": "2021-06-23",
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
+            "title": "TMAS 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2025-01-30",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-30",
-            "keyword": [
-                "driver licenses",
-                "licensed drivers",
-                "roadways",
-                "travel"
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
-            "identifier": "https://data.transportation.gov/api/views/qkam-edtm",
+            "dataQuality": true,
             "description": "The table displays the total number of licensed drivers in each State. The table shows the number of male and female licensed drivers by sex and age group.",
-            "title": "Licensed Driver Dashboard Data",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80392,48 +80374,84 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/qkam-edtm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/qkam-edtm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/qkam-edtm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/qkam-edtm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/qkam-edtm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/qkam-edtm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/qkam-edtm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/qkam-edtm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/qkam-edtm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/qkam-edtm",
+            "issued": "2025-01-30",
+            "keyword": [
+                "driver licenses",
+                "licensed drivers",
+                "roadways",
+                "travel"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-30",
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
+            "title": "Licensed Driver Dashboard Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/qkkg-r24f",
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
+                    "description": "2011 New Jersey HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/newjersey2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 New Jersey"
+                }
+            ],
+            "identifier": "678.32",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -80447,94 +80465,91 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.32",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 New Jersey",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/qkkg-r24f",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/newjersey2011.zip",
-                    "description": "2011 New Jersey HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 New Jersey"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 New Jersey"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/qknb-4kie",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Data from the U.S. Department of Commerce, Bureau of Economic Analysis, National Income Product Accounts on real personal consumption expenditures on bicycles and accessories and data from the U.S. Department of Commerce, Census Bureau, USA Trade Online on U.S. imports of non-motorized bicycles and other cycles, including delivery tricycles. Data by month.",
+            "identifier": "https://data.transportation.gov/api/views/qknb-4kie",
             "issued": "2024-09-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-30",
             "keyword": [
                 "bicycle",
                 "expenditures",
                 "imports"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/qknb-4kie",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-09-30",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/qknb-4kie",
-            "description": "Data from the U.S. Department of Commerce, Bureau of Economic Analysis, National Income Product Accounts on real personal consumption expenditures on bicycles and accessories and data from the U.S. Department of Commerce, Census Bureau, USA Trade Online on U.S. imports of non-motorized bicycles and other cycles, including delivery tricycles. Data by month.",
-            "title": "Visualizations for National Expenditures on Bicycles and Accessories and U.S. Imports of Non-motorized Bicycles",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Visualizations for National Expenditures on Bicycles and Accessories and U.S. Imports of Non-motorized Bicycles"
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
-            "landingPage": "https://data.transportation.gov/d/qmpm-krhn",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/02martvt/tvtmar02.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "March 2002"
+                }
             ],
+            "identifier": "18.150",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -80544,57 +80559,60 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.150",
+            "landingPage": "https://data.transportation.gov/d/qmpm-krhn",
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
-            "title": "Monthly Traffic Volume Trends - March 2002",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/02martvt/tvtmar02.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "March 2002"
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
+            "title": "Monthly Traffic Volume Trends - March 2002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/qmqp-7bb4",
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
+                    "description": "2013 Louisiana HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/louisiana2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Louisiana"
+                }
+            ],
+            "identifier": "678.122",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -80608,81 +80626,46 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.122",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Louisiana",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/qmqp-7bb4",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/louisiana2013.zip",
-                    "description": "2013 Louisiana HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Louisiana"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Louisiana"
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
-            "landingPage": "https://data.transportation.gov/d/qn7e-jzkh",
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
-            "identifier": "10.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
+            "describedBy": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Transaction+Data+and+Reports",
             "description": "The Car Allowance Rebate System (CARS), otherwise known as Cash for Clunkers, was a program intended to provide economic incentives to United States residents to purchase a new and more fuel efficient vehicle when trading in a less full efficient vehicle. The program was promoted as providing stimulus to the economy by boosting auto sales, while putting safer, cleaner and more fuel efficient vehicles on the road.",
-            "title": "Car Allowance Rebate System (CARS) - Transactions - Final Paid Transaction Database text file (via ftp)",
-            "isPartOf": "DOT-10",
-            "agencyProgramURL": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Officially+Ended",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80691,61 +80674,58 @@
                     "title": "Final Paid Transaction Database text file (via ftp)"
                 }
             ],
-            "spatial": "N/A",
-            "describedBy": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Transaction+Data+and+Reports",
-            "dataQuality": false,
+            "identifier": "10.2",
+            "isPartOf": "DOT-10",
+            "issued": "2018-12-17",
+            "keyword": [
+                "cars",
+                "transactions"
+            ],
+            "landingPage": "https://data.transportation.gov/d/qn7e-jzkh",
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
+            "title": "Car Allowance Rebate System (CARS) - Transactions - Final Paid Transaction Database text file (via ftp)"
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
-            "landingPage": "https://data.transportation.gov/d/qnas-svfr",
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
-            "identifier": "81.4",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Complaint information entered into NHTSA-ODI's vehicle owner's complaint database is used with other data sources to identify safety issues that warrant investigation and to determine if a safety-related defect trend exists. Complaint information is also analyzed to monitor existing recalls for proper scope and adequacy.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Complaints - NHTSA API",
-            "isPartOf": "DOT-81",
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
@@ -80754,47 +80734,53 @@
                     "title": "NHTSA API"
                 }
             ],
-            "spatial": "N/A",
-            "describedBy": "http://www-odi.nhtsa.dot.gov/downloads/folders/Complaints/CMPL.txt",
-            "dataQuality": true,
+            "identifier": "81.4",
+            "isPartOf": "DOT-81",
+            "issued": "2002-12-16",
+            "keyword": [
+                "complaints",
+                "email",
+                "paper",
+                "phone",
+                "safercar.gov"
+            ],
+            "landingPage": "https://data.transportation.gov/d/qnas-svfr",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
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
-            "phone": "202-366-0154",
-            "language": [
-                "en-US"
-            ]
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Complaints - NHTSA API"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/qpjk-b3zw",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-09-05",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
-            "keyword": [
-                "federal funding",
-                "funding"
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
-            "identifier": "https://data.transportation.gov/api/views/qpjk-b3zw",
             "description": "This dataset details federal funding sources for each applicable agency reporting to the NTD in the 2022 and 2023 report years. Federal funding sources are financial assistance obtained from the Federal Government to assist with the costs of providing transit services.\n\nNTD Data Tables organize and summarize data from the 2022 and 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. This dataset is based on the 2022 and 2023 Revenue Sources database files. \n\nIn years 2015-2021, you can find this data in the \"Funding Sources\" data table on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.\n\nIf you have any other questions about this table, please contact the NTD Help Desk at NTDHelp@dot.gov.",
-            "title": "2022 - 2023 NTD Annual Data - Funding Sources (Federal)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80802,105 +80788,98 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/qpjk-b3zw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/qpjk-b3zw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/qpjk-b3zw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/qpjk-b3zw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/qpjk-b3zw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/qpjk-b3zw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/qpjk-b3zw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/qpjk-b3zw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/qpjk-b3zw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/qpjk-b3zw",
+            "issued": "2024-09-05",
+            "keyword": [
+                "federal funding",
+                "funding"
+            ],
+            "landingPage": "https://data.transportation.gov/d/qpjk-b3zw",
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
+            "title": "2022 - 2023 NTD Annual Data - Funding Sources (Federal)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/qrg5-7v5r",
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
-            "identifier": "https://data.transportation.gov/api/views/qrg5-7v5r",
             "description": "Rail fatalities at highway-rail grade crossings. Fatalities may be reclassified upon subsequent reporting. The Federal Railroad Administration collects accident/incident and operational data from railroads.",
-            "title": "Rail Fatalities at Highway-Rail Crossings",
+            "identifier": "https://data.transportation.gov/api/views/qrg5-7v5r",
+            "issued": "2025-01-03",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/qrg5-7v5r",
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
+            "title": "Rail Fatalities at Highway-Rail Crossings"
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
-            "landingPage": "https://data.transportation.gov/d/qrj8-7kpw",
-            "issued": "1999-04-26",
-            "temporal": "1999/2015",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.nhtsa.gov/Research/Databases+and+Software/NHTSA+Test+Reference+Guides"
-            ],
-            "keyword": [
-                "compliance",
-                "component",
-                "test",
-                "vehicle"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "1842.3",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "The NHTSA Component Test Database contains engineering data measured during various types of research.",
-            "title": "Component Test Database - Zipped ASCII Export",
-            "isPartOf": "DOT-1842",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research",
-            "primaryITInvestmentUII": "021-961265599",
-            "programCode": [
-                "021:032"
-            ],
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The NHTSA Component Test Database contains engineering data measured during various types of research.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80909,55 +80888,57 @@
                     "title": "Zipped ASCII Export"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "1842.3",
+            "isPartOf": "DOT-1842",
+            "issued": "1999-04-26",
+            "keyword": [
+                "compliance",
+                "component",
+                "test",
+                "vehicle"
+            ],
+            "landingPage": "https://data.transportation.gov/d/qrj8-7kpw",
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
+            "temporal": "1999/2015",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4712",
-            "language": [
-                "en-US"
-            ]
+            "title": "Component Test Database - Zipped ASCII Export"
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
-            "landingPage": "https://data.transportation.gov/d/qta9-ezqe",
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
-            "identifier": "692.5",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - 2007 AADT",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "primaryITInvestmentUII": "021-845083703",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -80966,34 +80947,69 @@
                     "title": "2007 AADT"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.5",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/qta9-ezqe",
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
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - 2007 AADT"
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
-            "landingPage": "https://data.transportation.gov/d/quwc-qbju",
-            "issued": "2011-10-07",
-            "temporal": "R/2002-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-05",
+            "categoryDesignation": "Research",
             "collectionInstrument": "web-based reporting system",
-            "references": [
-                "www.transit.dot.gov/ntd"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NTD Program Support",
+                "hasEmail": "mailto:NTDHelp@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www.ntdprogram.gov/ntdprogram/Glossary.htm",
+            "description": "Data collected monthly from urbanized area transit systems. The Monthly module includes a limited set of key indicators reported by transit properties. Data is reported on a monthly basis, by mode and type of service, for a calendar year. The four data items included are: Unlinked Passenger Trips, Vehicle Revenue Miles, Vehicle Revenue Hours, and Vehicles Operated in Maximum Service (Peak Vehicles). Monthly data are reported by mode and type of service.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://go.usa.gov/kfQP",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Raw Data Release"
+                }
             ],
+            "identifier": "19.1",
+            "isPartOf": "DOT-19",
+            "issued": "2011-10-07",
             "keyword": [
                 "boardings",
                 "bus",
@@ -81003,82 +81019,49 @@
                 "train",
                 "transit"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NTD Program Support",
-                "hasEmail": "mailto:NTDHelp@dot.gov"
-            },
-            "identifier": "19.1",
+            "landingPage": "https://data.transportation.gov/d/quwc-qbju",
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
-            "description": "Data collected monthly from urbanized area transit systems. The Monthly module includes a limited set of key indicators reported by transit properties. Data is reported on a monthly basis, by mode and type of service, for a calendar year. The four data items included are: Unlinked Passenger Trips, Vehicle Revenue Miles, Vehicle Revenue Hours, and Vehicles Operated in Maximum Service (Peak Vehicles). Monthly data are reported by mode and type of service.",
-            "title": "NTD Monthly Module Data Set - Raw Data Release",
-            "isPartOf": "DOT-19",
-            "agencyProgramURL": "http://www.ntdprogram.gov; http://www.ntdprogram.gov/ntdprogram/data.htm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://go.usa.gov/kfQP",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "Raw Data Release"
-                }
+            "references": [
+                "www.transit.dot.gov/ntd"
             ],
             "spatial": "Urbanized Area",
-            "describedBy": "http://www.ntdprogram.gov/ntdprogram/Glossary.htm",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.ntdprogram.gov/ntdprogram/data.htm",
+            "temporal": "R/2002-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Research",
-            "analysisUnit": "various",
-            "phone": "202-366-5430",
-            "language": [
-                "en-US"
-            ]
+            "title": "NTD Monthly Module Data Set - Raw Data Release"
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
-            "landingPage": "https://data.transportation.gov/d/qwiw-guz8",
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
-            "identifier": "DOT-364",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
-            "primaryITInvestmentUII": "021-621341357",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81087,35 +81070,67 @@
                     "title": "Vehicle Test Query by Vehicle Test Parameters"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/qwiw-guz8",
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
+            "title": "Vehicle Safety Research and Development Database"
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
-            "landingPage": "https://data.transportation.gov/d/qxdc-zr8j",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/14jantvt/14jantvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "January 2014"
+                }
             ],
+            "identifier": "18.58",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -81125,57 +81140,60 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.58",
+            "landingPage": "https://data.transportation.gov/d/qxdc-zr8j",
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
-            "title": "Monthly Traffic Volume Trends - January 2014",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/14jantvt/14jantvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "January 2014"
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
+            "title": "Monthly Traffic Volume Trends - January 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/qxik-g3k8",
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
+                    "description": "2011 Iowa HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/iowa2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Iowa"
+                }
+            ],
+            "identifier": "678.17",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -81189,60 +81207,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.17",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Iowa",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/qxik-g3k8",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/iowa2011.zip",
-                    "description": "2011 Iowa HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Iowa"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Iowa"
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
-            "landingPage": "https://data.transportation.gov/d/qz9s-mn7z",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/03septvt/03septvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "September 2003"
+                }
             ],
+            "identifier": "18.132",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -81252,56 +81267,53 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.132",
+            "landingPage": "https://data.transportation.gov/d/qz9s-mn7z",
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
-            "title": "Monthly Traffic Volume Trends - September 2003",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/03septvt/03septvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "September 2003"
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
+            "title": "Monthly Traffic Volume Trends - September 2003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/r2cx-w8z5",
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
+            "description": "Florida DOT (FDOT) installed Vehicle Awareness Devices (VADs) on a set of Lynx transit buses as part of a demonstration for the ITS World Congress held in Orlando in October 2011.  These VADs recorded vehicle data during the World Congress and continue to operate after the World Congress.  Periodically the VADs are removed from the vehicles and the data files are retrieved.  FHWA Has confirmed that the data do not contain identification of individual transit operators or any other forms for Personally Identifiable Information (PII).\r\n\r\nThis legacy dataset was created before data.transportation.gov and is only currently available via the attached file(s). Please contact the dataset owner if there is a need for users to work with this data using the data.transportation.gov analysis features (online viewing, API, graphing, etc.) and the USDOT will consider modifying the dataset to fully integrate in data.transportation.gov.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/download/r2cx-w8z5/application/msword",
+                    "mediaType": "application/msword"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/r2cx-w8z5",
             "issued": "2012-07-02",
-            "temporal": "2011-09-01/2011-10-22",
-            "@type": "dcat:Dataset",
-            "modified": "2012-07-02",
             "keyword": [
                 "arterial",
                 "basic safety message (bsm)",
@@ -81317,86 +81329,64 @@
                 "transit",
                 "vehicle awareness device (vad)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/r2cx-w8z5",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://creativecommons.org/licenses/by-nc-sa/3.0/legalcode",
+            "modified": "2012-07-02",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Department of Transportation"
             },
-            "identifier": "https://data.transportation.gov/api/views/r2cx-w8z5",
-            "description": "Florida DOT (FDOT) installed Vehicle Awareness Devices (VADs) on a set of Lynx transit buses as part of a demonstration for the ITS World Congress held in Orlando in October 2011.  These VADs recorded vehicle data during the World Congress and continue to operate after the World Congress.  Periodically the VADs are removed from the vehicles and the data files are retrieved.  FHWA Has confirmed that the data do not contain identification of individual transit operators or any other forms for Personally Identifiable Information (PII).\r\n\r\nThis legacy dataset was created before data.transportation.gov and is only currently available via the attached file(s). Please contact the dataset owner if there is a need for users to work with this data using the data.transportation.gov analysis features (online viewing, API, graphing, etc.) and the USDOT will consider modifying the dataset to fully integrate in data.transportation.gov.",
-            "title": "Florida DOT Orlando ITS World Congress Vehicle Awareness Device",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/download/r2cx-w8z5/application/msword",
-                    "mediaType": "application/msword"
-                }
-            ],
-            "dataQuality": true,
-            "license": "http://creativecommons.org/licenses/by-nc-sa/3.0/legalcode",
-            "accrualPeriodicity": "irregular",
+            "temporal": "2011-09-01/2011-10-22",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Florida DOT Orlando ITS World Congress Vehicle Awareness Device"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/r32h-32er",
-            "bureauCode": [
-                "021:00"
-            ],
-            "issued": "2020-05-28",
-            "temporal": "2017-01-01/2017-12-31",
             "@type": "dcat:Dataset",
-            "modified": "2020-07-06",
+            "accessLevel": "public",
+            "bureauCode": [
+                "021:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Janine McFadden",
                 "hasEmail": "mailto:janine.mcfadden@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/r32h-32er",
             "description": "Facts and figures on ferry operations",
-            "title": "National Census of Ferry Operators (NCFO) 2018: Ferry Operators",
+            "identifier": "https://data.transportation.gov/api/views/r32h-32er",
+            "issued": "2020-05-28",
+            "landingPage": "https://data.transportation.gov/d/r32h-32er",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2020-07-06",
             "programCode": [
                 "021:042"
             ],
-            "license": "https://www.usa.gov/government-works",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "temporal": "2017-01-01/2017-12-31",
             "theme": [
                 "Ferry Transit"
-            ]
+            ],
+            "title": "National Census of Ferry Operators (NCFO) 2018: Ferry Operators"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/r36b-eady",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/r36b-eady",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "Continent",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81404,59 +81394,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/r36b-eady/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/r36b-eady/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/r36b-eady/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/r36b-eady/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/r36b-eady/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/r36b-eady/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/r36b-eady/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/r36b-eady/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/r36b-eady/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/r36b-eady",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/r36b-eady",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Continent"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/r3bp-uzdb",
-            "issued": "2021-03-18",
             "@type": "dcat:Dataset",
-            "modified": "2024-02-06",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Chambers",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/r3bp-uzdb",
+            "issued": "2021-03-18",
+            "landingPage": "https://data.transportation.gov/d/r3bp-uzdb",
+            "modified": "2024-02-06",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Container Cranes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/r3vy-npqd",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Transportation Analysis",
+                "hasEmail": "mailto:long.nguyen@dot.gov"
+            },
+            "description": "Freight Facts and Figures - Freight Transportation System Extent and Use",
+            "identifier": "https://data.transportation.gov/api/views/r3vy-npqd",
             "issued": "2019-07-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-26",
             "keyword": [
                 "bts",
                 "bureau of transportation statistics",
@@ -81468,36 +81472,50 @@
                 "freight transportation",
                 "use"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Transportation Analysis",
-                "hasEmail": "mailto:long.nguyen@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/r3vy-npqd",
+            "modified": "2024-09-26",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statisitics"
             },
-            "identifier": "https://data.transportation.gov/api/views/r3vy-npqd",
-            "description": "Freight Facts and Figures - Freight Transportation System Extent and Use",
-            "title": "Freight Transportation System Extent & Use",
-            "programCode": [
-                "021:053"
-            ],
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Freight Transportation System Extent & Use"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/r432-5j7v",
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
+                    "description": "2013 Idaho HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/idaho2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Idaho"
+                }
+            ],
+            "identifier": "678.116",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -81511,76 +81529,39 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.116",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Idaho",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/r432-5j7v",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/idaho2013.zip",
-                    "description": "2013 Idaho HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Idaho"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Idaho"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/r495-tyji",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2024-09-24",
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
-            "identifier": "https://data.transportation.gov/api/views/r495-tyji",
             "description": "Commercial air passengers, seats, freight, and mail by origin airport.",
-            "title": "AFF - T100 Segment Summary By Origin Airport",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81588,46 +81569,81 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/r495-tyji/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/r495-tyji/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/r495-tyji/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/r495-tyji/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/r495-tyji/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/r495-tyji/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/r495-tyji/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/r495-tyji/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/r495-tyji/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/r495-tyji",
+            "issued": "2024-09-24",
+            "keyword": [
+                "aff",
+                "air carriers",
+                "aviation facts & figures",
+                "passengers"
+            ],
+            "landingPage": "https://data.transportation.gov/d/r495-tyji",
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
+            "title": "AFF - T100 Segment Summary By Origin Airport"
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
-            "landingPage": "https://data.transportation.gov/d/r5k4-hj4u",
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
+                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/nits/Noncrash%20injuries/2008-2010/2008-2010%20Noncrash%20Injuries.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2008-2010 Noncrash injuries"
+                }
             ],
+            "identifier": "288.3",
+            "isPartOf": "DOT-288",
+            "issued": "2009-01-27",
             "keyword": [
                 "crash",
                 "death",
@@ -81643,61 +81659,59 @@
                 "vehicle",
                 "victim"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "288.3",
+            "landingPage": "https://data.transportation.gov/d/r5k4-hj4u",
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
-            "title": "Not in Traffic Surveillance (NiTS) - 2008-2010 Noncrash injuries",
-            "isPartOf": "DOT-288",
-            "agencyProgramURL": "http://www.nhtsa.gov/Data/State+Data+Programs",
-            "programCode": [
-                "021:032"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/nits/Noncrash%20injuries/2008-2010/2008-2010%20Noncrash%20Injuries.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "2008-2010 Noncrash injuries"
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
+            "title": "Not in Traffic Surveillance (NiTS) - 2008-2010 Noncrash injuries"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/statistics.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "motor fuel, motor vehicle registrations, driver licenses, highway user taxation, highway mileage, travel, and highway finance",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/r6fg-b885",
-            "issued": "2018-12-17",
-            "temporal": "R/1992-01-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.fhwa.dot.gov/policyinformation/hss/guide/"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Highway Statistics Series consists of annual reports containing analyzed statistical information on motor fuel, motor vehicle registrations, driver licenses, highway user taxation, highway mileage, travel, and highway finance. These information are presented in tables as well as selected charts. It has been published annually since 1945.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/statistics.cfm",
+                    "mediaType": "application/rss+xml",
+                    "title": "Data Browser"
+                }
             ],
+            "identifier": "17.0",
+            "issued": "2018-12-17",
             "keyword": [
                 "driver licenses",
                 "highway finance",
@@ -81707,78 +81721,42 @@
                 "motor vehicle registrations",
                 "travel"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "17.0",
+            "landingPage": "https://data.transportation.gov/d/r6fg-b885",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-4631",
+            "programCode": [
+                "021:011"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "The Highway Statistics Series consists of annual reports containing analyzed statistical information on motor fuel, motor vehicle registrations, driver licenses, highway user taxation, highway mileage, travel, and highway finance. These information are presented in tables as well as selected charts. It has been published annually since 1945.",
-            "title": "Highway Statistics - Data Browser",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:011"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/statistics.cfm",
-                    "mediaType": "application/rss+xml",
-                    "title": "Data Browser"
-                }
+            "references": [
+                "http://www.fhwa.dot.gov/policyinformation/hss/guide/"
             ],
             "spatial": "county, state, national",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/statistics.cfm",
+            "temporal": "R/1992-01-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "analysisUnit": "motor fuel, motor vehicle registrations, driver licenses, highway user taxation, highway mileage, travel, and highway finance",
-            "categoryDesignation": "Administrative",
-            "phone": "202-366-4631",
-            "language": [
-                "en-US"
-            ]
+            "title": "Highway Statistics - Data Browser"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/r6ib-3rca",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2024-09-16",
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
-            "identifier": "https://data.transportation.gov/api/views/r6ib-3rca",
             "description": "Data for Artificial Intelligence: Data-Centric AI for Transportation: Work Zone Use Case proposes a data integration pipeline that enhances the utilization of work zone and traffic data from diversified platforms and introduces a novel deep learning model to predict the traffic speed and traffic collision likelihood during planned work zone events. This dataset is raw Maryland roadway incident data without rows where road_tmc and road are inconsistent.",
-            "title": "Data for Artificial Intelligence: Data-Centric AI for Transportation: Work Zone Use Case Raw Maryland Incidents Matched",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81786,47 +81764,84 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/r6ib-3rca/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/r6ib-3rca/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/r6ib-3rca/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/r6ib-3rca/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/r6ib-3rca/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/r6ib-3rca/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/r6ib-3rca/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/r6ib-3rca/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/r6ib-3rca/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Maryland highway network",
+            "identifier": "https://data.transportation.gov/api/views/r6ib-3rca",
+            "issued": "2024-09-16",
+            "keyword": [
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "speed data",
+                "traffic detectors",
+                "traffic flow",
+                "travel time",
+                "work zones"
+            ],
+            "landingPage": "https://data.transportation.gov/d/r6ib-3rca",
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
+            "title": "Data for Artificial Intelligence: Data-Centric AI for Transportation: Work Zone Use Case Raw Maryland Incidents Matched"
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
-            "landingPage": "https://data.transportation.gov/d/r6rj-agrf",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/07octtvt/07octtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "October 2007"
+                }
             ],
+            "identifier": "18.83",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -81836,61 +81851,57 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.83",
+            "landingPage": "https://data.transportation.gov/d/r6rj-agrf",
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
-            "title": "Monthly Traffic Volume Trends - October 2007",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/07octtvt/07octtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "October 2007"
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
+            "title": "Monthly Traffic Volume Trends - October 2007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Consumer and carrier details are private information.",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://nccdb.fmcsa.dot.gov/",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/r6z9-e9sk",
-            "issued": "2018-12-17",
-            "temporal": "R/2013/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-24",
-            "references": [
-                "http://nccdb.fmcsa.dot.gov/"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "NCCDB is a web-based information system for recording and reporting on household goods, safety violation, hazardous material, cargo tank and passenger complaints. NCCDB allows the public and FMCSA staff to submit complaints using an online form. The database contains, among other information, reports on inspection and test of cargo tanks and inventory of tanks. These reports are used in the development and amendment to regulations of cargo security which is the protection of cargo from theft.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://nccdb.fmcsa.dot.gov/Login.asp",
+                    "mediaType": "application/xhtml+xml",
+                    "title": "\tNational Consumer Complaint Database"
+                }
             ],
+            "identifier": "370.0",
+            "issued": "2018-12-17",
             "keyword": [
                 "cargo tank",
                 "complaints",
@@ -81898,77 +81909,50 @@
                 "hazardous material",
                 "passenger complaints."
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "370.0",
+            "landingPage": "https://data.transportation.gov/d/r6z9-e9sk",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-24",
+            "phone": "215-656-7251",
+            "primaryITInvestmentUII": "021-000001018",
+            "programCode": [
+                "021:026"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Motor Carrier Safety Administration"
             },
-            "description": "NCCDB is a web-based information system for recording and reporting on household goods, safety violation, hazardous material, cargo tank and passenger complaints. NCCDB allows the public and FMCSA staff to submit complaints using an online form. The database contains, among other information, reports on inspection and test of cargo tanks and inventory of tanks. These reports are used in the development and amendment to regulations of cargo security which is the protection of cargo from theft.",
-            "title": "National Consumer Complaint Database (NCCDB) - \tNational Consumer Complaint Database",
-            "primaryITInvestmentUII": "021-000001018",
-            "programCode": [
-                "021:026"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://nccdb.fmcsa.dot.gov/Login.asp",
-                    "mediaType": "application/xhtml+xml",
-                    "title": "\tNational Consumer Complaint Database"
-                }
+            "references": [
+                "http://nccdb.fmcsa.dot.gov/"
             ],
+            "rights": "Consumer and carrier details are private information.",
             "spatial": "Carrier, State",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://nccdb.fmcsa.dot.gov/",
+            "temporal": "R/2013/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "language": [
-                "en-US"
-            ],
-            "phone": "215-656-7251"
+            "title": "National Consumer Complaint Database (NCCDB) - \tNational Consumer Complaint Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Contains FMCSA staff contact information which may not be shared.",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://ai.fmcsa.dot.gov/FSAS/default.aspx",
+            "agencyProgramURL": "http://ai.fmcsa.dot.gov/default.aspx",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/r7qg-9ptj",
-            "issued": "2014-09-26",
-            "temporal": "R/2014-09-26/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "analysis and information",
-                "gotham",
-                "safety information"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO",
                 "hasEmail": "mailto:fmcsa.cdo@dot.gov"
             },
-            "identifier": "111.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": true,
             "description": "GOTHAM supports the field, state partners, service centers, and headquarter staff with information on FMCSA safety programs goals, activities, and performance measures. GOTHAM provides FMCSA personnel with key information to help them manage their programs and staff. This database is not public. It is an Internal FMCSA Tool.",
-            "title": "A&I - GOTHAM -",
-            "agencyProgramURL": "http://ai.fmcsa.dot.gov/default.aspx",
-            "programCode": [
-                "021:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -81976,82 +81960,80 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "State, Carrier",
-            "dataQuality": true,
+            "identifier": "111.0",
+            "issued": "2014-09-26",
+            "keyword": [
+                "analysis and information",
+                "gotham",
+                "safety information"
+            ],
+            "landingPage": "https://data.transportation.gov/d/r7qg-9ptj",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "https://ai.fmcsa.dot.gov/FSAS/default.aspx",
+            "modified": "2024-05-24",
+            "phone": "202-366-2161",
+            "programCode": [
+                "021:026"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "rights": "Contains FMCSA staff contact information which may not be shared.",
+            "spatial": "State, Carrier",
+            "temporal": "R/2014-09-26/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "phone": "202-366-2161",
-            "language": [
-                "en-US"
-            ]
+            "title": "A&I - GOTHAM -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/r82v-yvib",
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
-            "identifier": "https://data.transportation.gov/api/views/r82v-yvib",
+            "dataQuality": true,
             "description": "This is the page for Casualty (Form 55a) PDF Generator report",
-            "title": "Casualty (Form 55a) PDF Generator",
+            "identifier": "https://data.transportation.gov/api/views/r82v-yvib",
+            "issued": "2024-12-17",
+            "landingPage": "https://data.transportation.gov/d/r82v-yvib",
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
+            "title": "Casualty (Form 55a) PDF Generator"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/r8cc-5x95",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2021-06-09",
-            "@type": "dcat:Dataset",
-            "modified": "2021-06-09",
-            "keyword": [
-                "freight",
-                "passengers",
-                "tsi"
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
-            "identifier": "https://data.transportation.gov/api/views/r8cc-5x95",
             "description": "Transportation Services Index 2000-Present, including numbers and percent changes for TSI, Freight TSI, and Passenger TSI\nChained 2000=100",
-            "title": "Transportation Services Index 2000-Present",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82059,45 +82041,81 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/r8cc-5x95/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/r8cc-5x95/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/r8cc-5x95/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/r8cc-5x95/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/r8cc-5x95/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/r8cc-5x95/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/r8cc-5x95/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/r8cc-5x95/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/r8cc-5x95/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.transportation.gov/api/views/r8cc-5x95",
+            "issued": "2021-06-09",
+            "keyword": [
+                "freight",
+                "passengers",
+                "tsi"
+            ],
+            "landingPage": "https://data.transportation.gov/d/r8cc-5x95",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2021-06-09",
+            "phone": "2023660573",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "spatial": "United States",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "2023660573"
+            "title": "Transportation Services Index 2000-Present"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/r8vk-kzar",
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
+                    "description": "2011 Virginia HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/virginia2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Virginia"
+                }
+            ],
+            "identifier": "678.48",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -82111,79 +82129,40 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.48",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Virginia",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/r8vk-kzar",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/virginia2011.zip",
-                    "description": "2011 Virginia HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Virginia"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Virginia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policy/otps/nhcci/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2024-08-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-31",
-            "references": [
-                "https://www.fhwa.dot.gov/policy/otps/nhcci/methodology.cfm"
-            ],
-            "keyword": [
-                "construction",
-                "cost",
-                "highway",
-                "index"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thor Dodson",
                 "hasEmail": "mailto:thor.dodson@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/r94d-n4f9",
+            "dataQuality": true,
             "description": "The National Highway Construction Cost Index (NHCCI) is a price index that can be used both to track price changes associated with highway construction costs, and to convert current dollar expenditures on highway construction to real or constant dollar expenditures. This dataset contains the quarterly NHCCI estimates as well as the Seasonally Adjusted NHCCI and Component Contributions to Changes in NHCCI.\n\nVisit https://www.fhwa.dot.gov/policy/otps/nhcci/ for more information regarding the NHCCI.",
-            "title": "NHCCI",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82191,45 +82170,80 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/r94d-n4f9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/r94d-n4f9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/r94d-n4f9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/r94d-n4f9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/r94d-n4f9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/r94d-n4f9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/r94d-n4f9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/r94d-n4f9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/r94d-n4f9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/r94d-n4f9",
+            "issued": "2024-08-13",
+            "keyword": [
+                "construction",
+                "cost",
+                "highway",
+                "index"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policy/otps/nhcci/",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-12-31",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "references": [
+                "https://www.fhwa.dot.gov/policy/otps/nhcci/methodology.cfm"
+            ],
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "NHCCI"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Data set contains controlled unclassified information (Draft rules and polices). Some public reports are available.",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/r94j-e897",
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
+            "identifier": "458.3",
+            "isPartOf": "DOT-458",
+            "issued": "2018-12-18",
             "keyword": [
                 "economically significant",
                 "effects",
@@ -82252,75 +82266,41 @@
                 "tribalism",
                 "unfunded mandate"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DOT Socrata",
-                "hasEmail": "mailto:Socrata@dot.gov"
-            },
-            "identifier": "458.3",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
-            "description": "RMS is a DOT-wide system developed for the Office of the General Counsel (OGC) to track the status of rulemakings, document required concurrences, serve as a repository for documents under development, and generate management and compliance reports from the data within the system.  The system allows senior leaders throughout DOT to identify not only the status of rulemakings, but areas where steps can be taken to streamline rulemaking operations at DOT.",
-            "title": "Rulemaking Management System (RMS) - Public Reports on Significant Rulemaking",
-            "isPartOf": "DOT-458",
+            "landingPage": "https://data.transportation.gov/d/r94j-e897",
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
-            "identifier": "https://data.transportation.gov/api/views/r9j3-4j7m",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 1983",
-            "title": "Historic HPMS Data (Sample) - 1983",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82328,60 +82308,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/r9j3-4j7m/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/r9j3-4j7m/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/r9j3-4j7m/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/r9j3-4j7m/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/r9j3-4j7m/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/r9j3-4j7m/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/r9j3-4j7m/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/r9j3-4j7m/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/r9j3-4j7m/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/r9j3-4j7m",
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
+            "title": "Historic HPMS Data (Sample) - 1983"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2023-04-25",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-08",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/ra4w-8xud",
+            "dataQuality": true,
             "description": "This dataset reports the historical National Highway System 50th percentile median speeds for various roadway types, months, and vehicles on US roads.",
-            "title": "Monthly NHS Traffic Speed",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82389,67 +82377,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ra4w-8xud/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ra4w-8xud/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ra4w-8xud/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ra4w-8xud/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ra4w-8xud/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ra4w-8xud/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ra4w-8xud/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ra4w-8xud/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ra4w-8xud/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/ra4w-8xud",
+            "issued": "2023-04-25",
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "dataQuality": true,
+            "modified": "2025-01-08",
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
-                "en-US"
-            ]
+            "title": "Monthly NHS Traffic Speed"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2022-05-24",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "cumulative vmt",
-                "roadways",
-                "seasonally adjusted vmt",
-                "vehicle miles traveled",
-                "vmt"
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
-            "identifier": "https://data.transportation.gov/api/views/rads-c3b7",
+            "dataQuality": true,
             "description": "Monthly VMT/12-month VMT average/Cumulative 12-month VMT",
-            "title": "Monthly Travel Trends Dashboard Data",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82457,70 +82438,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/rads-c3b7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/rads-c3b7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/rads-c3b7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/rads-c3b7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/rads-c3b7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/rads-c3b7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/rads-c3b7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/rads-c3b7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/rads-c3b7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/rads-c3b7",
+            "issued": "2022-05-24",
+            "keyword": [
+                "cumulative vmt",
+                "roadways",
+                "seasonally adjusted vmt",
+                "vehicle miles traveled",
+                "vmt"
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
+            "title": "Monthly Travel Trends Dashboard Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/rash-pd2d",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2023-07-10",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
-            "keyword": [
-                "casualty",
-                "fatality",
-                "illness",
-                "injury",
-                "railroad employee",
-                "trespasser",
-                "worker on duty"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Railroad Safety",
                 "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
-            "identifier": "https://data.transportation.gov/api/views/rash-pd2d",
+            "dataQuality": true,
             "description": "This dataset is in a user-friendly human-readable format. To download the source dataset that contains raw data values, go here: https://data.transportation.gov/dataset/Form55a-Source-Table/kuvg-3uwp.",
-            "title": "Injury/Illness Summary - Casualty Data (Form 55a)",
-            "programCode": [
-                "021:036"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82528,46 +82507,81 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/rash-pd2d/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/rash-pd2d/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/rash-pd2d/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/rash-pd2d/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/rash-pd2d/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/rash-pd2d/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/rash-pd2d/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/rash-pd2d/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/rash-pd2d/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/rash-pd2d",
+            "issued": "2023-07-10",
+            "keyword": [
+                "casualty",
+                "fatality",
+                "illness",
+                "injury",
+                "railroad employee",
+                "trespasser",
+                "worker on duty"
+            ],
+            "landingPage": "https://data.transportation.gov/d/rash-pd2d",
+            "modified": "2025-02-01",
+            "programCode": [
+                "021:036"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Injury/Illness Summary - Casualty Data (Form 55a)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/frecalls/",
+            "agencyProgramURL": "http://www.safercar.gov/",
+            "analysisUnit": "Vehicles , Tires, Child Safety Seats, Equipment",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/rbc7-i9sy",
-            "issued": "2002-12-16",
-            "temporal": "R/2000-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www-odi.nhtsa.dot.gov/help/foreigncampaign.html"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Foreign Campaigns data contains data on current and past NHTSA foreign campaigns including the Data Received and the specific manufacturer. You can search the database for foreign campaign information using any or all of the following search criteria: -\tThe dates when NHTSA received the foreign campaign information. -\tThe name of the domestic manufacturer involved in the campaign.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www-odi.nhtsa.dot.gov/frecalls/",
+                    "mediaType": "text/html",
+                    "title": "Foreign Recalls Search"
+                }
             ],
+            "identifier": "DOT-258",
+            "issued": "2002-12-16",
             "keyword": [
                 "campaign",
                 "car",
@@ -82579,96 +82593,94 @@
                 "tire",
                 "vehicle"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "DOT-258",
+            "landingPage": "https://data.transportation.gov/d/rbc7-i9sy",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-8089",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Highway Traffic Safety Administration"
             },
-            "description": "The Foreign Campaigns data contains data on current and past NHTSA foreign campaigns including the Data Received and the specific manufacturer. You can search the database for foreign campaign information using any or all of the following search criteria: -\tThe dates when NHTSA received the foreign campaign information. -\tThe name of the domestic manufacturer involved in the campaign.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Foreign Campaigns",
-            "agencyProgramURL": "http://www.safercar.gov/",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www-odi.nhtsa.dot.gov/frecalls/",
-                    "mediaType": "text/html",
-                    "title": "Foreign Recalls Search"
-                }
+            "references": [
+                "http://www-odi.nhtsa.dot.gov/help/foreigncampaign.html"
             ],
             "spatial": "N/A",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/frecalls/",
+            "temporal": "R/2000-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "analysisUnit": "Vehicles , Tires, Child Safety Seats, Equipment",
-            "categoryDesignation": "Research",
-            "phone": "202-366-8089",
-            "language": [
-                "en-US"
-            ]
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Foreign Campaigns"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.bts.gov/stories/s/rbec-3xcx",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Data and visualizations showing Airport and Airway Trust Fund and Harbor Maintenance and Inland Waterways Trust Fund balance.",
+            "identifier": "https://data.transportation.gov/api/views/rbec-3xcx",
             "issued": "2021-06-08",
-            "temporal": "annual",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-31",
             "keyword": [
                 "air",
                 "trust fund",
                 "water"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.bts.gov/stories/s/rbec-3xcx",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-12-31",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/rbec-3xcx",
-            "description": "Data and visualizations showing Airport and Airway Trust Fund and Harbor Maintenance and Inland Waterways Trust Fund balance.",
-            "title": "Transportation Economic Trends: Government Transportation Revenue - Other Trust Funds",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "annual",
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Transportation Economic Trends: Government Transportation Revenue - Other Trust Funds"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Contains driver PII.",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "https://ai.fmcsa.dot.gov/DSMS/driver_search.asp",
+            "agencyProgramURL": "https://ai.fmcsa.dot.gov/DSMS/driver_search.asp",
+            "analysisUnit": "Driver",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/rc4v-7fdu",
-            "issued": "2010-12-15",
-            "temporal": "R/2010-12-15/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "https://ai.fmcsa.dot.gov/DSMS/driver_search.asp"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "NOT PUBLICALLY AVAILABLE - The Driver Safety Measurement System is designed to identify drivers with a history of safety violations. The information is used to target enforcement when an investigator visits a motor carrier during a compliance review or other intervention. This information is not provided to the public.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.transportation.gov/mission/data-inventory-not-available",
+                    "mediaType": "text/html"
+                }
             ],
+            "identifier": "107.0",
+            "issued": "2010-12-15",
             "keyword": [
                 "bus",
                 "cdl",
@@ -82682,74 +82694,43 @@
                 "sms",
                 "violation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "107.0",
+            "landingPage": "https://data.transportation.gov/d/rc4v-7fdu",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-24",
+            "phone": "202-366-5241",
+            "programCode": [
+                "021:026"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Motor Carrier Safety Administration"
             },
-            "description": "NOT PUBLICALLY AVAILABLE - The Driver Safety Measurement System is designed to identify drivers with a history of safety violations. The information is used to target enforcement when an investigator visits a motor carrier during a compliance review or other intervention. This information is not provided to the public.",
-            "title": "Driver Safety Measurement System (DSMS) -",
-            "agencyProgramURL": "https://ai.fmcsa.dot.gov/DSMS/driver_search.asp",
-            "programCode": [
-                "021:026"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.transportation.gov/mission/data-inventory-not-available",
-                    "mediaType": "text/html"
-                }
+            "references": [
+                "https://ai.fmcsa.dot.gov/DSMS/driver_search.asp"
             ],
+            "rights": "Contains driver PII.",
             "spatial": "None",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "https://ai.fmcsa.dot.gov/DSMS/driver_search.asp",
+            "temporal": "R/2010-12-15/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Driver",
-            "phone": "202-366-5241",
-            "language": [
-                "en-US"
-            ]
+            "title": "Driver Safety Measurement System (DSMS) -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/rd72-aq8r",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2022-08-03",
-            "@type": "dcat:Dataset",
-            "modified": "2022-12-06",
-            "keyword": [
-                "freight",
-                "maritime",
-                "port",
-                "port performance"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Chambers",
                 "hasEmail": "mailto:portstatistics@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/rd72-aq8r",
             "description": "",
-            "title": "Monthly TEU Data",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -82757,43 +82738,80 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/rd72-aq8r/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/rd72-aq8r/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/rd72-aq8r/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/rd72-aq8r/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/rd72-aq8r/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/rd72-aq8r/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/rd72-aq8r/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/rd72-aq8r/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/rd72-aq8r/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/rd72-aq8r",
+            "issued": "2022-08-03",
+            "keyword": [
+                "freight",
+                "maritime",
+                "port",
+                "port performance"
+            ],
+            "landingPage": "https://data.transportation.gov/d/rd72-aq8r",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2022-12-06",
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
+            "title": "Monthly TEU Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/rdai-x3uv",
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
+                    "description": "2013 Nevada HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/nevada2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Nevada"
+                }
+            ],
+            "identifier": "678.132",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -82807,95 +82825,93 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.132",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Nevada",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/rdai-x3uv",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/nevada2013.zip",
-                    "description": "2013 Nevada HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Nevada"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Nevada"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/rdsi-pmvz",
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
-            "identifier": "https://data.transportation.gov/api/views/rdsi-pmvz",
             "description": "The Bureau of Transportation Statistics releases non-seasonally adjusted air traffic data based on monthly reports from commercial U.S. air carriers.",
-            "title": "Air Travel - International",
+            "identifier": "https://data.transportation.gov/api/views/rdsi-pmvz",
+            "issued": "2025-01-16",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/rdsi-pmvz",
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
+            "title": "Air Travel - International"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.phmsa.dot.gov/data-and-statistics/pipeline/mechanical-fitting-failure-data-gas-distribution-operators",
+            "agencyProgramURL": "http://www.phmsa.dot.gov/pipeline",
+            "analysisUnit": "Annual Report information from pipeline operators",
             "bureauCode": [
                 "021:50"
             ],
-            "landingPage": "https://data.transportation.gov/d/rdxy-82ey",
-            "issued": "2000-03-15",
-            "temporal": "R/1970-01-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-29",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.phmsa.dot.gov/pipeline"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "PHMSA-Datahub",
+                "hasEmail": "mailto:PHMSAPHPDataandStatistics@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Mechanical Fitting Failure (MFF) reports from Gas Distribution Operators are no longer required by PHMSA. Zip file include 2011-2021 submissions.  While individual MFF reports are no longer required, the Gas Distribution Annual Report form PHMSA F-7100.1-1 includes a count of mechanical joint failures resulting in a hazardous leak starting with calendar year 2021 reports.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Mechanical Fitting Failure Data from Gas Distribution Operators",
+                    "downloadURL": "http://www.phmsa.dot.gov/staticfiles/PHMSA/DownloadableFiles/Files/Pipeline/data/mechanical_fitting_failures_2011_present.zip",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Mechanical Fitting Failures - 2011 to Present (zip)"
+                }
             ],
+            "identifier": "33.1",
+            "isPartOf": "DOT-33",
+            "issued": "2000-03-15",
             "keyword": [
                 "annual",
                 "distribution",
@@ -82906,62 +82922,61 @@
                 "safety",
                 "transmission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "PHMSA-Datahub",
-                "hasEmail": "mailto:PHMSAPHPDataandStatistics@dot.gov"
-            },
-            "identifier": "33.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Pipeline and Hazardous Materials Safety Administration"
-            },
-            "description": "Mechanical Fitting Failure (MFF) reports from Gas Distribution Operators are no longer required by PHMSA. Zip file include 2011-2021 submissions.  While individual MFF reports are no longer required, the Gas Distribution Annual Report form PHMSA F-7100.1-1 includes a count of mechanical joint failures resulting in a hazardous leak starting with calendar year 2021 reports.",
-            "title": "Mechanical Fitting Failure Data from Gas Distribution Operators (2011-2021)",
-            "isPartOf": "DOT-33",
-            "agencyProgramURL": "http://www.phmsa.dot.gov/pipeline",
+            "landingPage": "https://data.transportation.gov/d/rdxy-82ey",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-07-29",
+            "phone": "202-366-1878",
             "primaryITInvestmentUII": "021-339943484",
             "programCode": [
                 "021:044"
             ],
-            "distribution": [
-                {
-                    "mediaType": "application/vnd.ms-excel",
-                    "downloadURL": "http://www.phmsa.dot.gov/staticfiles/PHMSA/DownloadableFiles/Files/Pipeline/data/mechanical_fitting_failures_2011_present.zip",
-                    "description": "Mechanical Fitting Failure Data from Gas Distribution Operators",
-                    "@type": "dcat:Distribution",
-                    "title": "Mechanical Fitting Failures - 2011 to Present (zip)"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Pipeline and Hazardous Materials Safety Administration"
+            },
+            "references": [
+                "http://www.phmsa.dot.gov/pipeline"
             ],
             "spatial": "Operator-specifc",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "https://www.phmsa.dot.gov/data-and-statistics/pipeline/mechanical-fitting-failure-data-gas-distribution-operators",
+            "temporal": "R/1970-01-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Annual Report information from pipeline operators",
-            "phone": "202-366-1878",
-            "language": [
-                "en-US"
-            ]
+            "title": "Mechanical Fitting Failure Data from Gas Distribution Operators (2011-2021)"
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
-            "landingPage": "https://data.transportation.gov/d/re2h-6m3s",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/10octtvt/10octtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "October 2010"
+                }
             ],
+            "identifier": "18.17",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -82971,57 +82986,59 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.17",
+            "landingPage": "https://data.transportation.gov/d/re2h-6m3s",
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
-            "title": "Monthly Traffic Volume Trends - October 2010",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/10octtvt/10octtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "October 2010"
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
+            "title": "Monthly Traffic Volume Trends - October 2010"
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
-            "landingPage": "https://data.transportation.gov/d/rfqx-2vcg",
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
+            "identifier": "DOT-4",
+            "issued": "2009-10-29",
             "keyword": [
                 "grading",
                 "quality",
@@ -83033,119 +83050,81 @@
                 "uniform",
                 "utqgs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "DOT-4",
+            "landingPage": "https://data.transportation.gov/d/rfqx-2vcg",
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
-            "title": "Uniform Tire Quality Grading System (UTQGS)",
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
+            "title": "Uniform Tire Quality Grading System (UTQGS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/rfw9-fja8",
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
-            "identifier": "https://data.transportation.gov/api/views/rfw9-fja8",
             "description": "The U.S. Census Bureau provides monthly estimates of the total dollar value of construction work done in the United States as part of the Value of Construction Put in Place Survey (VIP). Includes construction related to passenger terminals, runways, pavement and lighting, hangars, air freight terminals, space facilities, air traffic towers, aircraft storage and maintenance buildings.",
-            "title": "State and Local Government Construction Spending - Air Transportation",
+            "identifier": "https://data.transportation.gov/api/views/rfw9-fja8",
+            "issued": "2025-01-03",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/rfw9-fja8",
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
+            "title": "State and Local Government Construction Spending - Air Transportation"
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
-            "landingPage": "https://data.transportation.gov/d/rgbj-8uad",
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
-            "identifier": "524.13",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
             "description": "STATE DATA REPORTING SYSTEMS. Annual reports on the Fatality Analysis Reporting System (FARS) which is data regarding fatalities that is collected by a FARS analyst from each State and provided to NHTSA.",
-            "title": "GES Reports - 2012",
-            "isPartOf": "DOT-524",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83154,32 +83133,71 @@
                     "title": "2012"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
-            "dataQuality": true,
+            "identifier": "524.13",
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
+            "landingPage": "https://data.transportation.gov/d/rgbj-8uad",
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
+            "title": "GES Reports - 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/rgxr-p9zb",
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
+                    "description": "2011 North Carolina HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/northcarolina2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 North Carolina"
+                }
+            ],
+            "identifier": "678.35",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -83193,88 +83211,41 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.35",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 North Carolina",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/rgxr-p9zb",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/northcarolina2011.zip",
-                    "description": "2011 North Carolina HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 North Carolina"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 North Carolina"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/rh2j-ihhy",
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
-                "connected equipment",
-                "connected vehicle message",
-                "field test",
-                "freight",
-                "freight signal priority (fsp)",
-                "intelligent transportation systems (its)",
-                "i-sig",
-                "its joint program office (jpo)",
-                "multi-modal intelligent traffic signal system (mmitss)",
-                "roadside equipment (rse)",
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
-            "identifier": "https://data.transportation.gov/api/views/rh2j-ihhy",
+            "dataQuality": true,
             "description": "Data were collected during the Multi-Modal Intelligent Transportation Signal Systems (MMITSS) study. MMITSS is a next-generation traffic signal system that seeks to provide a comprehensive traffic information framework to service all modes of transportation. The Vehicle Trajectories file is populated with basic safety messages received from equipped vehicle within the communication range of an Roadside Equipment (RSEs).  The data also contains elements that communicate additional details about the vehicle that is used for vehicle safety applications, and elements that communicate specific items of a vehicle\u2018s status that are used in data event snapshots which are gathered and periodically reported to an RSEs. These data are transmitted at a rate of 10 Hz.\r\n\r\nNOTE: All extra attachments are located in Multi-Modal Intelligent Traffic Signal Systems Basic Safety Message",
-            "title": "Multi-Modal Intelligent Traffic Signal Systems Vehicle Trajectories for Roadside Equipment",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83282,52 +83253,96 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/rh2j-ihhy/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/rh2j-ihhy/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/rh2j-ihhy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/rh2j-ihhy/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/rh2j-ihhy/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/rh2j-ihhy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/rh2j-ihhy/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/rh2j-ihhy/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/rh2j-ihhy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Anthem, Arizona",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/rh2j-ihhy",
+            "issued": "2015-11-01",
+            "keyword": [
+                "anthem",
+                "arizona",
+                "basic safety message (bsm)",
+                "connected equipment",
+                "connected vehicle message",
+                "field test",
+                "freight",
+                "freight signal priority (fsp)",
+                "intelligent transportation systems (its)",
+                "i-sig",
+                "its joint program office (jpo)",
+                "multi-modal intelligent traffic signal system (mmitss)",
+                "roadside equipment (rse)",
+                "trajectories",
+                "transit signal priority (tsp)"
+            ],
+            "landingPage": "https://data.transportation.gov/d/rh2j-ihhy",
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
+            "title": "Multi-Modal Intelligent Traffic Signal Systems Vehicle Trajectories for Roadside Equipment"
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
-            "landingPage": "https://data.transportation.gov/d/rhnj-cjkt",
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
+                    "downloadURL": "http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/faf3/faf3_5.zip",
+                    "mediaType": "application/zip",
+                    "title": "Regional Data base for 2007 with forecasts through 2040"
+                }
             ],
+            "identifier": "DOT-286",
+            "issued": "2013-03-20",
             "keyword": [
                 "commodity",
                 "consumption",
@@ -83352,86 +83367,85 @@
                 "value",
                 "wear"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "DOT-286",
+            "landingPage": "https://data.transportation.gov/d/rhnj-cjkt",
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
-            "title": "Freight Analysis Framework",
-            "agencyProgramURL": "http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/faf3/faf3_5.zip",
-                    "mediaType": "application/zip",
-                    "title": "Regional Data base for 2007 with forecasts through 2040"
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
+            "title": "Freight Analysis Framework"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/ri89-bhxh",
-            "issued": "2020-07-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-23",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "TBD",
                 "hasEmail": "mailto:TBD"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/ri89-bhxh",
             "description": "",
-            "title": "National Transportation Noise Map",
+            "identifier": "https://data.transportation.gov/api/views/ri89-bhxh",
+            "issued": "2020-07-10",
+            "landingPage": "https://data.transportation.gov/d/ri89-bhxh",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-01-23",
             "programCode": [
                 "021:053"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "National Transportation Noise Map"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://safer.fmcsa.dot.gov/CSP_Order.asp",
+            "agencyProgramURL": "http://safer.fmcsa.dot.gov/CSP_Order.asp",
+            "analysisUnit": "Motor Carrier",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/rj9z-7m2d",
-            "issued": "2000-01-01",
-            "temporal": "R/1974-06-01/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://mcmiscatalog.fmcsa.dot.gov/d_profile_contents.asp"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Company Safety Profile (CSP) contains safety-related information on an individual Company's operation, including selected items from inspection reports and crash reports and the results of any reviews or enforcement actions involving the requested company. For a more detailed description of the CSP and the information it contains, please select the CSP Definition Document link shown to the right. As an aid to performing a successful CSP Request, please select the CSP Help link shown to the right, particularly if you have not previously used this service. ProVu is a viewer which allows users to electronically analyze standard company safety profile reports. Data are available in a PDF as well as XML.  FMCSA provides a tool, called ProVu, in order to read the XML data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://safer.fmcsa.dot.gov/CSP_Order.asp",
+                    "mediaType": "text/html",
+                    "title": "Company Safety Profile (CSP)"
+                }
             ],
+            "identifier": "DOT-123",
+            "issued": "2000-01-01",
             "keyword": [
                 "bus",
                 "company safety profile",
@@ -83448,83 +83462,49 @@
                 "safersys",
                 "safety and fitness electronic records"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "DOT-123",
+            "landingPage": "https://data.transportation.gov/d/rj9z-7m2d",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-24",
+            "phone": "202-493-0215",
+            "programCode": [
+                "021:026"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Motor Carrier Safety Administration"
             },
-            "description": "The Company Safety Profile (CSP) contains safety-related information on an individual Company's operation, including selected items from inspection reports and crash reports and the results of any reviews or enforcement actions involving the requested company. For a more detailed description of the CSP and the information it contains, please select the CSP Definition Document link shown to the right. As an aid to performing a successful CSP Request, please select the CSP Help link shown to the right, particularly if you have not previously used this service. ProVu is a viewer which allows users to electronically analyze standard company safety profile reports. Data are available in a PDF as well as XML.  FMCSA provides a tool, called ProVu, in order to read the XML data.",
-            "title": "SAFER - Company Safety Profile",
-            "agencyProgramURL": "http://safer.fmcsa.dot.gov/CSP_Order.asp",
-            "programCode": [
-                "021:026"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safer.fmcsa.dot.gov/CSP_Order.asp",
-                    "mediaType": "text/html",
-                    "title": "Company Safety Profile (CSP)"
-                }
+            "references": [
+                "http://mcmiscatalog.fmcsa.dot.gov/d_profile_contents.asp"
             ],
             "spatial": "Physical and Mailing addresses.",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://safer.fmcsa.dot.gov/CSP_Order.asp",
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
+            "title": "SAFER - Company Safety Profile"
         },
         {
-            "accessLevel": "public",
-            "bureauCode": [
-                "021:18"
-            ],
-            "landingPage": "https://data.transportation.gov/d/rjtv-hha2",
-            "issued": "2014-06-27",
-            "temporal": "R/2005-01-01/PT1S",
             "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
-            "collectionInstrument": "NASSMAIN, CIRENapp",
-            "references": [
-                "http://www.nhtsa.gov/Research/Crash+Injury+Research+%28CIREN%29/Data:"
-            ],
-            "keyword": [
-                "accident",
-                "crash",
-                "injury",
-                "motor vehicle",
-                "occupant"
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/PT1S",
+            "agencyDataSeriesURL": "http://www.nhtsa.gov/Research/Crash+Injury+Research+%28CIREN%29/Data:",
+            "agencyProgramURL": "http://www.nhtsa.gov/CIREN",
+            "analysisUnit": "Motor vehicle crash",
+            "bureauCode": [
+                "021:18"
             ],
+            "categoryDesignation": "Research",
+            "collectionInstrument": "NASSMAIN, CIRENapp",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "240.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
             "description": "The CIREN process combines prospective data collection with professional multidisciplinary analysis of medical and engineering evidence to determine injury causation in every crash investigation conducted.The mission of the CIREN is to improve the prevention, treatment, and rehabilitation of motor vehicle crash injuries to reduce deaths, disabilities, and human and economic costs.",
-            "title": "Crash Injury Research and Engineering Network (CIREN) - CIREN data files",
-            "agencyProgramURL": "http://www.nhtsa.gov/CIREN",
-            "primaryITInvestmentUII": "021-175812085",
-            "programCode": [
-                "021:031"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83533,52 +83513,52 @@
                     "title": "CIREN data files"
                 }
             ],
-            "spatial": "Trauma Medical Centers",
-            "dataQuality": false,
+            "identifier": "240.0",
+            "issued": "2014-06-27",
+            "keyword": [
+                "accident",
+                "crash",
+                "injury",
+                "motor vehicle",
+                "occupant"
+            ],
+            "landingPage": "https://data.transportation.gov/d/rjtv-hha2",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.nhtsa.gov/Research/Crash+Injury+Research+%28CIREN%29/Data:",
+            "modified": "2024-05-01",
+            "phone": "202-366-5078",
+            "primaryITInvestmentUII": "021-175812085",
+            "programCode": [
+                "021:031"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "http://www.nhtsa.gov/Research/Crash+Injury+Research+%28CIREN%29/Data:"
+            ],
+            "spatial": "Trauma Medical Centers",
+            "temporal": "R/2005-01-01/PT1S",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/PT1S",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Motor vehicle crash",
-            "phone": "202-366-5078",
-            "language": [
-                "en-US"
-            ]
+            "title": "Crash Injury Research and Engineering Network (CIREN) - CIREN data files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/rjzd-p9xx",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2021-05-27",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-13",
-            "keyword": [
-                "marine",
-                "maritime",
-                "ports",
-                "vessel",
-                "water transportation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Chambers",
                 "hasEmail": "mailto:matthew.chambers@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/rjzd-p9xx",
             "description": "",
-            "title": "2020 PM",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83586,46 +83566,81 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/rjzd-p9xx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/rjzd-p9xx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/rjzd-p9xx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/rjzd-p9xx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/rjzd-p9xx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/rjzd-p9xx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/rjzd-p9xx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/rjzd-p9xx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/rjzd-p9xx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/rjzd-p9xx",
+            "issued": "2021-05-27",
+            "keyword": [
+                "marine",
+                "maritime",
+                "ports",
+                "vessel",
+                "water transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/rjzd-p9xx",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2023-01-13",
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
+            "title": "2020 PM"
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
-            "landingPage": "https://data.transportation.gov/d/rkcn-92a8",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12aprtvt/12aprtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "April 2012"
+                }
             ],
+            "identifier": "18.37",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -83635,96 +83650,85 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.37",
+            "landingPage": "https://data.transportation.gov/d/rkcn-92a8",
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
-            "title": "Monthly Traffic Volume Trends - April 2012",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12aprtvt/12aprtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "April 2012"
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
+            "title": "Monthly Traffic Volume Trends - April 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/rki6-jcxp",
+            "accrualPeriodicity": "Daily",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2021-08-02",
-            "temporal": "Ongoing",
-            "@type": "dcat:Dataset",
-            "modified": "2021-08-02",
-            "keyword": [
-                "analytics",
-                "site analytics",
-                "usage metrics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Daniel Morgan",
                 "hasEmail": "mailto:OpenData@DOT.gov "
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "USDOT"
-            },
-            "identifier": "https://data.transportation.gov/api/views/rki6-jcxp",
+            "dataQuality": true,
             "description": "Information about the use of Department of Transportation data assets, including how many assets are created, which sub-agency has the most assets, and which asset is accessed the most.",
-            "title": "Department of Transportation Data Analytics",
+            "identifier": "https://data.transportation.gov/api/views/rki6-jcxp",
+            "issued": "2021-08-02",
+            "keyword": [
+                "analytics",
+                "site analytics",
+                "usage metrics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/rki6-jcxp",
+            "language": [
+                "English"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2021-08-02",
             "primaryITInvestmentUII": "021-040221200",
             "programCode": [
                 "021:000"
             ],
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Daily",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "USDOT"
+            },
+            "temporal": "Ongoing",
             "theme": [
                 "Administrative"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Department of Transportation Data Analytics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/rkrk-b6ad",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Households earn and spend different amounts due in part to differences in composition. This page uses the Consumer Expenditure Survey to show the characteristics households in each income quintile and their income sources.",
+            "identifier": "https://data.transportation.gov/api/views/rkrk-b6ad",
             "issued": "2023-11-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
             "keyword": [
                 "burden",
                 "consumer expenditure survey",
@@ -83734,53 +83738,34 @@
                 "socioeconomics",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/rkrk-b6ad",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-18",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/rkrk-b6ad",
-            "description": "Households earn and spend different amounts due in part to differences in composition. This page uses the Consumer Expenditure Survey to show the characteristics households in each income quintile and their income sources.",
-            "title": "Transportation Cost Burden: Household Characteristics and Income Sources",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Transportation Cost Burden: Household Characteristics and Income Sources"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/rkzg-z7ht",
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
-            "identifier": "https://data.transportation.gov/api/views/rkzg-z7ht",
+            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
             "description": "State DOTs provide the location limits of highway sections to be used to represent statewide aggregations based on a statistically valid Sample Panel.",
-            "title": "Roadway Sections West 2019",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83788,95 +83773,90 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/rkzg-z7ht/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/rkzg-z7ht/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/rkzg-z7ht/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/rkzg-z7ht/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/rkzg-z7ht/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/rkzg-z7ht/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/rkzg-z7ht/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/rkzg-z7ht/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/rkzg-z7ht/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "USA",
-            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
+            "identifier": "https://data.transportation.gov/api/views/rkzg-z7ht",
+            "issued": "2020-12-21",
+            "landingPage": "https://data.transportation.gov/d/rkzg-z7ht",
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
+            "title": "Roadway Sections West 2019"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/rm53-5ubr",
-            "issued": "2020-12-10",
             "@type": "dcat:Dataset",
-            "modified": "2022-01-10",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alpha Wingfield",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/rm53-5ubr",
+            "issued": "2020-12-10",
+            "landingPage": "https://data.transportation.gov/d/rm53-5ubr",
+            "modified": "2022-01-10",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "CFS for TRB"
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
-            "landingPage": "https://data.transportation.gov/d/rn9n-qngc",
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
-            "identifier": "693.18",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
             "description": "The NBI System is the collection of bridge inspection information and costs associated with bridge replacements of structurally deficient bridges on and off the NHS. This data is collected under the auspices of the National Bridge Inspection Standards (NBIS) as prescribed by law. The NBI System collects the information that is used to determine eligibility for NHS projects, performance measure reporting, NHS penalty determination, and reporting to Congress.  It supports oversight of the NBIS through various report tools, and provides data reporting that supports agency strategic goals.",
-            "title": "National Bridge Inventory System (NBI) - 2009",
-            "isPartOf": "DOT-693",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
-            "primaryITInvestmentUII": "021-012940226",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -83885,70 +83865,105 @@
                     "title": "2009"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
-            "dataQuality": true,
+            "identifier": "693.18",
+            "isPartOf": "DOT-693",
+            "issued": "1992-12-31",
+            "keyword": [
+                "bridge",
+                "condition",
+                "deck",
+                "inspection",
+                "structure"
+            ],
+            "landingPage": "https://data.transportation.gov/d/rn9n-qngc",
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
+            "title": "National Bridge Inventory System (NBI) - 2009"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/rpax-fyz5",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Economic concepts related to employment in transportation",
+            "identifier": "https://data.transportation.gov/api/views/rpax-fyz5",
             "issued": "2020-03-09",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
             "keyword": [
                 "transportation economics",
                 "transportation employment",
                 "transportation workforce"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/rpax-fyz5",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-18",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/rpax-fyz5",
-            "description": "Economic concepts related to employment in transportation",
-            "title": "Transportation Economic Concepts: Transportation Employment",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Transportation Economic Concepts: Transportation Employment"
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
-            "landingPage": "https://data.transportation.gov/d/rq7e-ds5e",
-            "issued": "1992-01-01",
-            "temporal": "R/1992-01-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Research",
             "collectionInstrument": "N/A",
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
+            "identifier": "DOT-287",
+            "issued": "1992-01-01",
             "keyword": [
                 "air",
                 "area",
@@ -83969,61 +83984,61 @@
                 "quality",
                 "voc"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "DOT-287",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "All 50 states and the District of Columbia submit annual reports of their CMAQ project obligations in March of   every year. The FHWA uses these yearly submissions to maintain an active database of CMAQ investments, trends within the program, and other anecdotal information focusing on the program's performance. This   database of CMAQ Project information has always been reserved for internal use by authorized FHWA personnel for Congressional reporting and made available to state DOTs and MPOs on a limited basis.",
-            "title": "Congestion Mitigation and Air Quality (CMAQ)",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/environment/air_quality/cmaq/",
+            "landingPage": "https://data.transportation.gov/d/rq7e-ds5e",
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
+            "title": "Congestion Mitigation and Air Quality (CMAQ)"
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
-            "landingPage": "https://data.transportation.gov/d/rqek-6qwq",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/07jantvt/07jantvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "January 2007"
+                }
             ],
+            "identifier": "18.92",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -84033,86 +84048,49 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.92",
+            "landingPage": "https://data.transportation.gov/d/rqek-6qwq",
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
-            "title": "Monthly Traffic Volume Trends - January 2007",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/07jantvt/07jantvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "January 2007"
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
+            "title": "Monthly Traffic Volume Trends - January 2007"
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
-            "landingPage": "https://data.transportation.gov/d/rqir-4h6p",
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
-            "identifier": "1840.9",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/veh/vehdb-export-fields.htm",
             "description": "The NHTSA Vehicle Crash Test Database contains engineering data measured during various types of research, the New Car Assessment Program (NCAP), and compliance crash tests. Information in this database refers to the performance and response of vehicles and other structures in impacts. This database is not intended to support general consumer safety issues. For general consumer information please see the NHTSA's information on buying a safer car.",
-            "title": "Vehicle Crash Test Database - Query by barrier parameters",
-            "isPartOf": "DOT-1840",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research",
-            "primaryITInvestmentUII": "021-961265599",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84121,31 +84099,71 @@
                     "title": "Query by barrier parameters"
                 }
             ],
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/veh/vehdb-export-fields.htm",
-            "dataQuality": true,
+            "identifier": "1840.9",
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
+            "landingPage": "https://data.transportation.gov/d/rqir-4h6p",
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
+            "title": "Vehicle Crash Test Database - Query by barrier parameters"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/rseq-83xg",
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
+                    "description": "2012 North Carolina HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/northcarolina2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 North Carolina"
+                }
+            ],
+            "identifier": "678.87",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -84159,60 +84177,58 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.87",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 North Carolina",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/rseq-83xg",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/northcarolina2012.zip",
-                    "description": "2012 North Carolina HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 North Carolina"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 North Carolina"
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
-            "landingPage": "https://data.transportation.gov/d/rskk-gec3",
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
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/inccaus.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Accident Causes"
+                }
             ],
+            "identifier": "199.16",
+            "isPartOf": "DOT-199",
+            "issued": "2010-09-29",
             "keyword": [
                 "acts of god",
                 "collisions",
@@ -84223,61 +84239,60 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "199.16",
+            "landingPage": "https://data.transportation.gov/d/rskk-gec3",
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
-            "title": "Rail Equipment Accidents - Accident Causes",
-            "isPartOf": "DOT-199",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:036"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/inccaus.aspx",
-                    "mediaType": "text/csv",
-                    "title": "Accident Causes"
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
+            "title": "Rail Equipment Accidents - Accident Causes"
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
-            "landingPage": "https://data.transportation.gov/d/rthr-cpxe",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/04augtvt/04augtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "August 2004"
+                }
             ],
+            "identifier": "18.121",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -84287,60 +84302,61 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.121",
+            "landingPage": "https://data.transportation.gov/d/rthr-cpxe",
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
-            "title": "Monthly Traffic Volume Trends - August 2004",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/04augtvt/04augtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "August 2004"
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
+            "title": "Monthly Traffic Volume Trends - August 2004"
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
-            "landingPage": "https://data.transportation.gov/d/ru3g-qx7d",
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
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/1997NTDxls.exe",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "1997 Database"
+                }
             ],
+            "identifier": "21.1",
+            "isPartOf": "DOT-21",
+            "issued": "2010-10-01",
             "keyword": [
                 "agency",
                 "allocation",
@@ -84359,83 +84375,49 @@
                 "urbanized",
                 "vehicles"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John D. Giorgis",
-                "hasEmail": "mailto:john.giorgis@dot.gov"
-            },
-            "identifier": "21.1",
+            "landingPage": "https://data.transportation.gov/d/ru3g-qx7d",
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
-            "title": "NTD Annual Module Data Set - 1997 Database",
-            "isPartOf": "DOT-21",
-            "agencyProgramURL": "http://www.ntdprogram.gov",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/1997NTDxls.exe",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "1997 Database"
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
+            "title": "NTD Annual Module Data Set - 1997 Database"
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
-            "landingPage": "https://data.transportation.gov/d/ru63-rbt9",
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
-            "identifier": "364.10",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database - Vehicle Event Data Recorder Reports",
-            "isPartOf": "DOT-364",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
-            "primaryITInvestmentUII": "021-621341357",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84444,57 +84426,90 @@
                     "title": "Vehicle Event Data Recorder Reports"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.10",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ru63-rbt9",
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
+            "title": "Vehicle Safety Research and Development Database - Vehicle Event Data Recorder Reports"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/rusp-usez",
-            "issued": "2022-01-18",
             "@type": "dcat:Dataset",
-            "modified": "2022-09-20",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/rusp-usez",
+            "issued": "2022-01-18",
+            "landingPage": "https://data.transportation.gov/d/rusp-usez",
+            "modified": "2022-09-20",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
-            "title": "Technology Trends",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "Technology Trends"
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
-            "landingPage": "https://data.transportation.gov/d/rvwr-yjsd",
-            "issued": "1988-12-31",
-            "temporal": "R/1988-01-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
+            "description": "STATE DATA REPORTING SYSTEMS. Annual reports on the Fatality Analysis Reporting System (FARS) which is data regarding fatalities that is collected by a FARS analyst from each State and provided to NHTSA.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/GES/GES89",
+                    "mediaType": "text/plain",
+                    "title": "1989"
+                }
             ],
+            "identifier": "524.15",
+            "isPartOf": "DOT-524",
+            "issued": "1988-12-31",
             "keyword": [
                 "crashworthiness",
                 "estimation",
@@ -84503,83 +84518,49 @@
                 "nass",
                 "system"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "524.15",
+            "landingPage": "https://data.transportation.gov/d/rvwr-yjsd",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-4998",
+            "programCode": [
+                "021:032"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Highway Traffic Safety Administration"
             },
-            "description": "STATE DATA REPORTING SYSTEMS. Annual reports on the Fatality Analysis Reporting System (FARS) which is data regarding fatalities that is collected by a FARS analyst from each State and provided to NHTSA.",
-            "title": "GES Reports - 1989",
-            "isPartOf": "DOT-524",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:032"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/GES/GES89",
-                    "mediaType": "text/plain",
-                    "title": "1989"
-                }
+            "references": [
+                "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType"
             ],
             "spatial": "Point",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "ftp://ftp.nhtsa.dot.gov/GES/",
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
+            "title": "GES Reports - 1989"
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
-            "landingPage": "https://data.transportation.gov/d/rvyy-fhds",
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
-            "identifier": "276.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": true,
             "description": "A list of Significant Guidance documents, which include guidance document disseminated to regulated entities or the general public that may reasonably be anticipated to lead to an annual effect on the economy of $100 million or more or adversely affect in a material way the economy, a sector of the economy, productivity, competition, jobs, the environment, public health or safety, or State, local, or tribal governments or communities; create a serious inconsistency or otherwise interfere with an action taken or planned by another agency; materially alter the budgetary impact of entitlements, grants, user fees, or loan programs or the rights and obligations of recipients thereof; or raise novel legal or policy issues arising out of legal mandates, the President's priorities, or the principles set forth in Executive Order 12866, as further amended.",
-            "title": "Significant Guidance Issued by the Office of the Secretary of Transportation -",
-            "isPartOf": "DOT-276",
-            "agencyProgramURL": "http://regs.dot.gov/",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84587,153 +84568,151 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "276.1",
+            "isPartOf": "DOT-276",
+            "issued": "2011-01-18",
+            "keyword": [
+                "data.gov",
+                "law",
+                "significant guidance",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/rvyy-fhds",
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
-            "categoryDesignation": "Other",
-            "analysisUnit": "Regulations",
-            "phone": "202-366-4308",
-            "language": [
-                "en-US"
-            ]
+            "title": "Significant Guidance Issued by the Office of the Secretary of Transportation -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "rights": "Information is subject to Privacy Act",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyProgramURL": "http://www.nhtsa.gov/About+NHTSA/NHTSA+Electronic+Reading+Room+(ERR)",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/rw76-e64b",
-            "issued": "2015-09-15",
-            "temporal": "R/2013/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "annual",
-                "dot",
-                "foia",
-                "log",
-                "logs",
-                "nhtsa",
-                "rpoert"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "475.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
             "description": "Personal privacy information has been redacted based on FOIA Exemption 6",
-            "title": "NHTSA FOIA Logs - Annual FOIA Report",
-            "agencyProgramURL": "http://www.nhtsa.gov/About+NHTSA/NHTSA+Electronic+Reading+Room+(ERR)",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.nhtsa.gov/staticfiles/laws_regs/pdf/FY2014-NHTSA-FOIA-Log.pdf",
-                    "description": "FOIA REPORT FROM OCTOBER 1, 2013 - SEPTEMBER 30, 2014",
                     "@type": "dcat:Distribution",
+                    "description": "FOIA REPORT FROM OCTOBER 1, 2013 - SEPTEMBER 30, 2014",
+                    "downloadURL": "http://www.nhtsa.gov/staticfiles/laws_regs/pdf/FY2014-NHTSA-FOIA-Log.pdf",
+                    "mediaType": "application/pdf",
                     "title": "Annual FOIA Report"
                 }
             ],
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "475.0",
+            "issued": "2015-09-15",
+            "keyword": [
+                "annual",
+                "dot",
+                "foia",
+                "log",
+                "logs",
+                "nhtsa",
+                "rpoert"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Administrative",
+            "landingPage": "https://data.transportation.gov/d/rw76-e64b",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-1834"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-01",
+            "phone": "202-366-1834",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "rights": "Information is subject to Privacy Act",
+            "temporal": "R/2013/P1Y",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "NHTSA FOIA Logs - Annual FOIA Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/rw9i-mdin",
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
-            "identifier": "https://data.transportation.gov/api/views/rw9i-mdin",
             "description": "Urban rail includes heavy rail, commuter rail, light rail, streetcar rail, and hybrid rail. The Federal Highway Administration estimates monthly transit ridership, released as part of the National Transit Database. Ridership estimates have been adjusted to account for changes in data collection over time. Starting in January 2012, data for Small System Waiver agencies that do not have a mode are reported under motor bus. Data reported under hybrid rail are reported under their classifications prior to January 2012.",
-            "title": "Transit Ridership - Urban Rail",
+            "identifier": "https://data.transportation.gov/api/views/rw9i-mdin",
+            "issued": "2025-01-15",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/rw9i-mdin",
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
+            "title": "Transit Ridership - Urban Rail"
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
-            "landingPage": "https://data.transportation.gov/d/rwfz-5n92",
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
-            "identifier": "524.6",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
             "description": "STATE DATA REPORTING SYSTEMS. Annual reports on the Fatality Analysis Reporting System (FARS) which is data regarding fatalities that is collected by a FARS analyst from each State and provided to NHTSA.",
-            "title": "GES Reports - 2004",
-            "isPartOf": "DOT-524",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84742,47 +84721,53 @@
                     "title": "2004"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
-            "dataQuality": true,
+            "identifier": "524.6",
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
+            "landingPage": "https://data.transportation.gov/d/rwfz-5n92",
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
+            "title": "GES Reports - 2004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/rwr4-5nkg",
             "bureauCode": [
                 "021:17"
             ],
-            "issued": "2023-12-06",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
-            "keyword": [
-                "revocation",
-                "motor carrier",
-                "operating authority"
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
-            "identifier": "https://data.transportation.gov/api/views/rwr4-5nkg",
             "description": "Information on carrier/broker/freight forwarder authorities that have been revoked by FMCSA. The dataset includes the DOT number and docket number of the entity, the type of authority revoked, and the reason.  See dataset attachment \"FMCSA Dataset Description and Data Definitions - Select Datasets\" for more information.",
-            "title": "Revocation - All With History",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84790,32 +84775,37 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/rwr4-5nkg",
+            "issued": "2023-12-06",
+            "keyword": [
+                "revocation",
+                "motor carrier",
+                "operating authority"
+            ],
+            "landingPage": "https://data.transportation.gov/d/rwr4-5nkg",
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
+            "title": "Revocation - All With History"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/rx2s-7tqf",
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
-            "identifier": "https://data.transportation.gov/api/views/rx2s-7tqf",
             "description": "This a list of active and inactive railroads, companies, and other organizations related to railroad operations. Organization Type ID = 1 designates a railroad; 4 designates a non-railroad organization (e.g. company, shipper, public entity, etc.). If a code has a blank EndDate, this means the organization is active; a populated EndDate field means the organization is no longer active.",
-            "title": "Railroad, Company and Organization List",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84823,44 +84813,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/rx2s-7tqf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/rx2s-7tqf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/rx2s-7tqf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/rx2s-7tqf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/rx2s-7tqf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/rx2s-7tqf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/rx2s-7tqf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/rx2s-7tqf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/rx2s-7tqf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/rx2s-7tqf",
+            "issued": "2023-08-08",
+            "landingPage": "https://data.transportation.gov/d/rx2s-7tqf",
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
+            "title": "Railroad, Company and Organization List"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Data set contains controlled unclassified information (Draft rules and polices). Some public reports are available.",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/rx94-i33j",
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
+                    "downloadURL": "http://www.dot.gov/regulations/effects-report-archive",
+                    "mediaType": "text/html",
+                    "title": "Public Effects Reports"
+                }
+            ],
+            "identifier": "458.1",
+            "isPartOf": "DOT-458",
+            "issued": "2018-12-18",
             "keyword": [
                 "economically significant",
                 "effects",
@@ -84883,78 +84897,47 @@
                 "tribalism",
                 "unfunded mandate"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DOT Socrata",
-                "hasEmail": "mailto:Socrata@dot.gov"
-            },
-            "identifier": "458.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
-            "description": "RMS is a DOT-wide system developed for the Office of the General Counsel (OGC) to track the status of rulemakings, document required concurrences, serve as a repository for documents under development, and generate management and compliance reports from the data within the system.  The system allows senior leaders throughout DOT to identify not only the status of rulemakings, but areas where steps can be taken to streamline rulemaking operations at DOT.",
-            "title": "Rulemaking Management System (RMS) - Public Effects Reports",
-            "isPartOf": "DOT-458",
+            "landingPage": "https://data.transportation.gov/d/rx94-i33j",
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
-                    "downloadURL": "http://www.dot.gov/regulations/effects-report-archive",
-                    "mediaType": "text/html",
-                    "title": "Public Effects Reports"
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
+            "title": "Rulemaking Management System (RMS) - Public Effects Reports"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "https://www.phmsa.dot.gov/hazmat-program-management-data-and-statistics/data-operations/incident-statistics",
+            "agencyProgramURL": "http://www.phmsa.dot.gov/hazmat/incident-report",
+            "analysisUnit": "Incident",
             "bureauCode": [
                 "021:50"
             ],
-            "landingPage": "https://data.transportation.gov/d/rxrf-q3m4",
-            "issued": "2008-07-01",
-            "temporal": "R/1971-01-01/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-29",
+            "categoryDesignation": "Research",
             "collectionInstrument": "5800.1 Form",
-            "references": [
-                "https://portal.phmsa.dot.gov/PDMPublicReport/?url=https://portal.phmsa.dot.gov/analytics/saw.dll?Portalpages&PortalPath=%2Fshared%2FPublic%20Website%20Pages%2F_portal%2FHazmat%20Incident%20Report%20Search"
-            ],
-            "keyword": [
-                "hazardous materials incident",
-                "hazmat incident"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Serita McKoy",
                 "hasEmail": "mailto:hmrequests@dot.gov"
             },
-            "identifier": "27.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Pipeline and Hazardous Materials Safety Administration"
-            },
+            "dataQuality": true,
             "description": "Hazmat Incident Report Search tool allows users to search for incidents involving hazardous material while in transportation and export the results to a text file for further analysis.",
-            "title": "Hazmat Incident Reports - Data Mining Tool",
-            "isPartOf": "DOT-27",
-            "agencyProgramURL": "http://www.phmsa.dot.gov/hazmat/incident-report",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -84963,32 +84946,48 @@
                     "title": "Data Mining Tool"
                 }
             ],
-            "spatial": "Street Address",
-            "dataQuality": true,
+            "identifier": "27.2",
+            "isPartOf": "DOT-27",
+            "issued": "2008-07-01",
+            "keyword": [
+                "hazardous materials incident",
+                "hazmat incident"
+            ],
+            "landingPage": "https://data.transportation.gov/d/rxrf-q3m4",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "https://www.phmsa.dot.gov/hazmat-program-management-data-and-statistics/data-operations/incident-statistics",
+            "modified": "2024-07-29",
+            "phone": "202-366-3373",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Pipeline and Hazardous Materials Safety Administration"
+            },
+            "references": [
+                "https://portal.phmsa.dot.gov/PDMPublicReport/?url=https://portal.phmsa.dot.gov/analytics/saw.dll?Portalpages&PortalPath=%2Fshared%2FPublic%20Website%20Pages%2F_portal%2FHazmat%20Incident%20Report%20Search"
+            ],
+            "spatial": "Street Address",
+            "temporal": "R/1971-01-01/P1D",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Incident",
-            "phone": "202-366-3373",
-            "language": [
-                "en-US"
-            ]
+            "title": "Hazmat Incident Reports - Data Mining Tool"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ryjr-58ty",
-            "issued": "2022-02-28",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Chambers",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "2024",
+            "identifier": "https://data.transportation.gov/api/views/ryjr-58ty",
+            "issued": "2022-02-28",
             "keyword": [
                 "bureau",
                 "container",
@@ -85006,46 +85005,27 @@
                 "transportation",
                 "vessel"
             ],
-            "identifier": "https://data.transportation.gov/api/views/ryjr-58ty",
+            "landingPage": "https://data.transportation.gov/d/ryjr-58ty",
+            "modified": "2025-01-17",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "2024",
             "title": "Record Low Water on the Mississippi and Ohio Rivers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/bridge/nbi.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2022-06-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
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
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/ryrf-hyeh",
+            "describedBy": "https://www.fhwa.dot.gov/bridge/mtguide.pdf,  https://www.fhwa.dot.gov/bridge/errata.cfm",
             "description": "The NBI is an aggregation of State, Federal agency and Tribal government bridge and associated highway data submitted to and maintained by the Federal Highway Administration (FHWA). It contains inspection and appraisal data of more than 600,000 of the Nation\u2019s highway bridges located on public roads in accordance with the National Bridge Inspection Standards. The NBI data is used to determine the condition of the Nation\u2019s bridges that is included in reports to Congress, as a data source for executing various sections of the Federal-aid program which involve highway bridges, for assessing the bridge penalty provisions of Title 23 United States Code (U.S.C.) section 119, as the data source for the evaluation of bridge performance measures established in Title 23 U.S.C. section 150, to assist in the oversight of the National Bridge Inspection Program, as a data source to assess and inform the condition and funding needs of highway bridges, and for strategic national defense needs.",
-            "title": "National Bridge Inventory System (NBI)",
-            "primaryITInvestmentUII": "021-012940226",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85054,55 +85034,54 @@
                     "title": "Main Page for National Bridge Inventory"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/ryrf-hyeh",
+            "issued": "2022-06-13",
+            "keyword": [
+                "bridge",
+                "condition",
+                "deck",
+                "inspection",
+                "structure"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/bridge/nbi.cfm",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-05-08",
+            "primaryITInvestmentUII": "021-012940226",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
             "spatial": "United States",
-            "describedBy": "https://www.fhwa.dot.gov/bridge/mtguide.pdf,  https://www.fhwa.dot.gov/bridge/errata.cfm",
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "National Geospatial Data Asset Transportation"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "National Bridge Inventory System (NBI)"
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
-            "landingPage": "https://data.transportation.gov/d/ryxu-um4r",
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
-            "identifier": "524.18",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
             "description": "STATE DATA REPORTING SYSTEMS. Annual reports on the Fatality Analysis Reporting System (FARS) which is data regarding fatalities that is collected by a FARS analyst from each State and provided to NHTSA.",
-            "title": "GES Reports - 1995",
-            "isPartOf": "DOT-524",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85111,32 +85090,71 @@
                     "title": "1995"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
-            "dataQuality": true,
+            "identifier": "524.18",
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
+            "landingPage": "https://data.transportation.gov/d/ryxu-um4r",
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
+            "title": "GES Reports - 1995"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/rza7-4ckb",
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
+                    "description": "2011 Utah HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/utah2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Utah"
+                }
+            ],
+            "identifier": "678.46",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -85150,55 +85168,50 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.46",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Utah",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/rza7-4ckb",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/utah2011.zip",
-                    "description": "2011 Utah HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Utah"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Utah"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/s255-yvnt",
             "bureauCode": [
                 "021:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kate Hartman",
+                "hasEmail": "mailto:kate.hartman@dot.gov"
+            },
+            "description": "This dataset contains data collected from the IHP2 testing conducted in Florida. This data set contains up 3 different vehicle types with data saved in ROS bag format. The goal of this project is to develop and enable the bundled applications (Platooning, Cooperative Merge, and Speed Harmonization) on the CARMA3 vehicles and demonstrate with CARMA partners.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "This dataset contains data collected from the IHP2 testing conducted in Florida. This data set contains up 3 different vehicle types with data saved in ROS bag format.\n",
+                    "downloadURL": "https://connected-automated-vehicles-integrated-highway-prototype.s3.amazonaws.com/index.html",
+                    "mediaType": "text/html",
+                    "title": "Connected Automated Vehicles \u2013 Integrated Highway Prototype"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/s255-yvnt",
             "issued": "2024-07-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
             "keyword": [
                 "carma",
                 "connected automated vehicles",
@@ -85214,72 +85227,38 @@
                 "vehicle to infrastructure (v2i)",
                 "vehicle to vehicle (v2v)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/s255-yvnt",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-07",
+            "programCode": [
+                "021:042"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/s255-yvnt",
-            "description": "This dataset contains data collected from the IHP2 testing conducted in Florida. This data set contains up 3 different vehicle types with data saved in ROS bag format. The goal of this project is to develop and enable the bundled applications (Platooning, Cooperative Merge, and Speed Harmonization) on the CARMA3 vehicles and demonstrate with CARMA partners.",
-            "title": "Connected Automated Vehicles \u2013 Integrated Highway Prototype II (IHP2)",
-            "programCode": [
-                "021:042"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://connected-automated-vehicles-integrated-highway-prototype.s3.amazonaws.com/index.html",
-                    "description": "This dataset contains data collected from the IHP2 testing conducted in Florida. This data set contains up 3 different vehicle types with data saved in ROS bag format.\n",
-                    "@type": "dcat:Distribution",
-                    "title": "Connected Automated Vehicles \u2013 Integrated Highway Prototype"
-                }
-            ],
             "spatial": "Auburndale, FL",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "theme": [
                 "Automobiles"
-            ]
+            ],
+            "title": "Connected Automated Vehicles \u2013 Integrated Highway Prototype II (IHP2)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "contains sensitive information",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/s2xt-bk5v",
-            "issued": "2018-12-18",
-            "temporal": "2004-01-01/2015-01-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "classification",
-                "data collection",
-                "drug",
-                "evaluation",
-                "impaired driving",
-                "law enforcement"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "533.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
             "description": "NATIONAL DRIVER REGISTER & TRAFFIC RECORDS (NVS-422). National Sobriety Testing Resource Center and  DRE Data system. National Sobriety Testing Resource Center & DRE Data System (hereatfer referred to as the DRE Data System), a NHTSA data system used to collect drug impaired driving evaluation and toxicology data from the system's end-users: Drug Recognition Experts (DREs) from across the nation. To ensure that law enforcement officers apply DEC procedures correctly and uniformly, officers must undergo IACP-approved training in how to conduct evaluations of suspects prior to being certified as a Drug Recognition Expert (DRE).  The DRE Data System serves as a respository for the evualtion records created by certifies DREs.",
-            "title": "National Sobriety Testing Resource Center and DRE Data System -",
-            "primaryITInvestmentUII": "021-802932942",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85287,43 +85266,48 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "533.0",
+            "issued": "2018-12-18",
+            "keyword": [
+                "classification",
+                "data collection",
+                "drug",
+                "evaluation",
+                "impaired driving",
+                "law enforcement"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/s2xt-bk5v",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-0546"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-01",
+            "phone": "202-366-0546",
+            "primaryITInvestmentUII": "021-802932942",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "rights": "contains sensitive information",
+            "temporal": "2004-01-01/2015-01-31",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "National Sobriety Testing Resource Center and DRE Data System -"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://international.fhwa.dot.gov/",
-            "issued": "2021-07-08",
             "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "bridges",
-                "construction",
-                "transportation asset management",
-                "transportation best practices",
-                "transportation technologies"
-            ],
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/s379-pwfw",
+            "dataQuality": true,
             "description": "The objective of this dataset is to create a location where there is a comprehensive list of all technologies, best practices and lessons learned from the Office of International Programs as a whole.",
-            "title": "Transportation Technologies and Best Practices",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85331,51 +85315,82 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/s379-pwfw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/s379-pwfw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/s379-pwfw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/s379-pwfw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/s379-pwfw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/s379-pwfw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/s379-pwfw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/s379-pwfw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/s379-pwfw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.transportation.gov/api/views/s379-pwfw",
+            "issued": "2021-07-08",
+            "keyword": [
+                "bridges",
+                "construction",
+                "transportation asset management",
+                "transportation best practices",
+                "transportation technologies"
+            ],
+            "landingPage": "https://international.fhwa.dot.gov/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "dataQuality": true,
+            "modified": "2024-05-08",
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
+            "title": "Transportation Technologies and Best Practices"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/frecalls/",
+            "agencyProgramURL": "http://www.safercar.gov/",
+            "analysisUnit": "Vehicles , Tires, Child Safety Seats, Equipment",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/s3ee-9xx9",
-            "issued": "2002-12-16",
-            "temporal": "R/2000-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www-odi.nhtsa.dot.gov/help/foreigncampaign.html"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Foreign Campaigns data contains data on current and past NHTSA foreign campaigns including the Data Received and the specific manufacturer. You can search the database for foreign campaign information using any or all of the following search criteria: -\tThe dates when NHTSA received the foreign campaign information. -\tThe name of the domestic manufacturer involved in the campaign.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www-odi.nhtsa.dot.gov/frecalls/",
+                    "mediaType": "text/html",
+                    "title": "Foreign Recalls Search"
+                }
             ],
+            "identifier": "258.1",
+            "isPartOf": "DOT-258",
+            "issued": "2002-12-16",
             "keyword": [
                 "campaign",
                 "car",
@@ -85387,82 +85402,46 @@
                 "tire",
                 "vehicle"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "258.1",
+            "landingPage": "https://data.transportation.gov/d/s3ee-9xx9",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-8089",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Highway Traffic Safety Administration"
             },
-            "description": "The Foreign Campaigns data contains data on current and past NHTSA foreign campaigns including the Data Received and the specific manufacturer. You can search the database for foreign campaign information using any or all of the following search criteria: -\tThe dates when NHTSA received the foreign campaign information. -\tThe name of the domestic manufacturer involved in the campaign.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Foreign Campaigns - Foreign Recalls Search",
-            "isPartOf": "DOT-258",
-            "agencyProgramURL": "http://www.safercar.gov/",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www-odi.nhtsa.dot.gov/frecalls/",
-                    "mediaType": "text/html",
-                    "title": "Foreign Recalls Search"
-                }
+            "references": [
+                "http://www-odi.nhtsa.dot.gov/help/foreigncampaign.html"
             ],
             "spatial": "N/A",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/frecalls/",
+            "temporal": "R/2000-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Vehicles , Tires, Child Safety Seats, Equipment",
-            "phone": "202-366-8089",
-            "language": [
-                "en-US"
-            ]
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Foreign Campaigns - Foreign Recalls Search"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://data.transportation.gov/d/s4at-4na4",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "021:18"
             ],
-            "rights": "Public subsets of information contained in these systems is provided through other NHTSA systems and interfaces.",
-            "issued": "2018-12-17",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-01",
-            "keyword": [
-                "complaints",
-                "compliance",
-                "defects",
-                "investigations",
-                "recalls",
-                "regulations",
-                "safety"
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
-            "identifier": "26.0",
+            "dataQuality": false,
             "description": "Artemis provides an efficient means to identify serious safety defects early in the vehicle equipment and component production cycle and influences safety recalls promoting a safer environment for drivers and passengers across the nation. Artemis consists of the overall datasets that are defaulted to supported non-public internal use.",
-            "title": "Artemis-Vehicles Information System -",
-            "primaryITInvestmentUII": "021-777552743",
-            "programCode": [
-                "021:031"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85470,71 +85449,82 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
+            "identifier": "26.0",
+            "issued": "2018-12-17",
+            "keyword": [
+                "complaints",
+                "compliance",
+                "defects",
+                "investigations",
+                "recalls",
+                "regulations",
+                "safety"
+            ],
+            "landingPage": "https://data.transportation.gov/d/s4at-4na4",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2024-05-01",
+            "phone": "202-366-0154",
+            "primaryITInvestmentUII": "021-777552743",
+            "programCode": [
+                "021:031"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "rights": "Public subsets of information contained in these systems is provided through other NHTSA systems and interfaces.",
             "theme": [
                 "Transportation"
             ],
-            "categoryDesignation": "Research",
-            "phone": "202-366-0154",
-            "language": [
-                "en-US"
-            ]
+            "title": "Artemis-Vehicles Information System -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/s539-c8h7",
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
                 "fn": "Bureau of Trnasportation Statistics",
                 "hasEmail": "mailto:answers@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/s539-c8h7",
             "description": "A monthly measure of the volume of services performed by the for-hire transportation sector. The index covers the activities of local mass transit, intercity passenger rail, and passenger air transportation.",
-            "title": "Transportation Services Index - Passenger",
+            "identifier": "https://data.transportation.gov/api/views/s539-c8h7",
+            "issued": "2025-01-02",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/s539-c8h7",
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
+            "title": "Transportation Services Index - Passenger"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/s56a-9mv2",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/s56a-9mv2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "CSXT Trackage Rights",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85542,45 +85532,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/s56a-9mv2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/s56a-9mv2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/s56a-9mv2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/s56a-9mv2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/s56a-9mv2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/s56a-9mv2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/s56a-9mv2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/s56a-9mv2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/s56a-9mv2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/s56a-9mv2",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/s56a-9mv2",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "CSXT Trackage Rights"
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
-            "landingPage": "https://data.transportation.gov/d/s5dw-itpf",
+            "categoryDesignation": "Research",
+            "collectionInstrument": "Transportation",
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
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2006NTDxls.exe",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2006 Database"
+                }
+            ],
+            "identifier": "21.10",
+            "isPartOf": "DOT-21",
             "issued": "2010-10-01",
-            "temporal": "R/1996-12-31/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-05",
-            "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.ntdprogram.gov"
-            ],
             "keyword": [
                 "agency",
                 "allocation",
@@ -85599,83 +85615,48 @@
                 "urbanized",
                 "vehicles"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John D. Giorgis",
-                "hasEmail": "mailto:john.giorgis@dot.gov"
-            },
-            "identifier": "21.10",
+            "landingPage": "https://data.transportation.gov/d/s5dw-itpf",
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
-            "title": "NTD Annual Module Data Set - 2006 Database",
-            "isPartOf": "DOT-21",
-            "agencyProgramURL": "http://www.ntdprogram.gov",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2006NTDxls.exe",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "2006 Database"
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
+            "title": "NTD Annual Module Data Set - 2006 Database"
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
-            "landingPage": "https://data.transportation.gov/d/s5hw-75nr",
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
-            "identifier": "692.20",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - 2011 Fatal Crashes",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "primaryITInvestmentUII": "021-845083703",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85684,60 +85665,59 @@
                     "title": "2011 Fatal Crashes"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.20",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/s5hw-75nr",
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
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - 2011 Fatal Crashes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
+            "agencyProgramURL": "https://www.nhtsa.gov/recalls",
+            "analysisUnit": "Vehicles , Tires, Child Safety Seats, Equipment",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/s84w-cs4i",
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
-            "identifier": "81.5",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Complaint information entered into NHTSA-ODI's vehicle owner's complaint database is used with other data sources to identify safety issues that warrant investigation and to determine if a safety-related defect trend exists. Complaint information is also analyzed to monitor existing recalls for proper scope and adequacy.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Complaints - NHTSA API",
-            "isPartOf": "DOT-81",
-            "agencyProgramURL": "https://www.nhtsa.gov/recalls",
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
@@ -85746,58 +85726,59 @@
                     "title": "NHTSA API"
                 }
             ],
-            "spatial": "N/A",
-            "describedBy": "http://www-odi.nhtsa.dot.gov/downloads/folders/Complaints/CMPL.txt",
-            "dataQuality": true,
+            "identifier": "81.5",
+            "isPartOf": "DOT-81",
+            "issued": "2002-12-16",
+            "keyword": [
+                "complaints",
+                "email",
+                "paper",
+                "phone",
+                "safercar.gov"
+            ],
+            "landingPage": "https://data.transportation.gov/d/s84w-cs4i",
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
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Complaints - NHTSA API"
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
-            "landingPage": "https://data.transportation.gov/d/s8d5-7zeq",
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
-            "identifier": "692.32",
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
@@ -85806,69 +85787,106 @@
                     "title": "PM 10"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.32",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/s8d5-7zeq",
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
-            "landingPage": "https://data.transportation.gov/d/s8hj-vns8",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRA Safety Admin",
+                "hasEmail": "mailto:no-reply@data.transportation.gov"
+            },
+            "dataQuality": true,
+            "description": "This is a user guide for downloading, exporting, and printing FRA Safety data reports, form PDFs and datasets into csv, Microsoft Excel and PDF, among others.",
+            "identifier": "https://data.transportation.gov/api/views/s8hj-vns8",
             "issued": "2025-01-16",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "export",
                 "pdf",
                 "user guide"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRA Safety Admin",
-                "hasEmail": "mailto:no-reply@data.transportation.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/s8hj-vns8",
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
-            "identifier": "https://data.transportation.gov/api/views/s8hj-vns8",
-            "description": "This is a user guide for downloading, exporting, and printing FRA Safety data reports, form PDFs and datasets into csv, Microsoft Excel and PDF, among others.",
-            "title": "Download, Export and Print User Guide",
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
+            "title": "Download, Export and Print User Guide"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/s9jz-5xbm",
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
+                    "description": "2012 Virginia HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/virginia2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Virginia"
+                }
+            ],
+            "identifier": "678.100",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -85882,72 +85900,39 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.100",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Virginia",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/s9jz-5xbm",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/virginia2012.zip",
-                    "description": "2012 Virginia HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Virginia"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Virginia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/sa6p-acbp",
             "bureauCode": [
                 "021:17"
             ],
-            "issued": "2024-02-02",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
-            "keyword": [
-                "revocation",
-                "motor carrier",
-                "operating authority"
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
-            "identifier": "https://data.transportation.gov/api/views/sa6p-acbp",
             "description": "*Dataset*  Information on carrier/broker/freight forwarder authorities that have been revoked by FMCSA. The dataset includes the DOT number and docket number of the entity, the type of authority revoked, and the reason. See dataset attachment \"FMCSA Dataset Description and Data Definitions - Select Datasets\" for more information.",
-            "title": "Revocation - All With History",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -85955,103 +85940,99 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/sa6p-acbp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/sa6p-acbp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/sa6p-acbp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/sa6p-acbp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/sa6p-acbp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/sa6p-acbp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/sa6p-acbp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/sa6p-acbp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/sa6p-acbp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/sa6p-acbp",
+            "issued": "2024-02-02",
+            "keyword": [
+                "revocation",
+                "motor carrier",
+                "operating authority"
+            ],
+            "landingPage": "https://data.transportation.gov/d/sa6p-acbp",
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
+            "title": "Revocation - All With History"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/saea-dvwc",
             "bureauCode": [
                 "021:27"
             ],
-            "issued": "2023-10-11",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Railroad Safety",
                 "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Railroad Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/saea-dvwc",
+            "dataQuality": true,
             "description": "This report contains data for the highway-rail crossing inventory, broken out by the highest level of warning device present at the crossing. There are four views of data: by (1) state, (2) county, (3) city, and (4) railroad. The data is grouped by the type of warning devices present: four quad (full barrier) gates, all other gates, flashing lights, highway signals/bells, special active warning devices, stop signs, crossbucks, other signs or signals, or no signs or signals.",
-            "title": "Crossing Inventory Warning Device Equipment Summary (8.10)",
+            "identifier": "https://data.transportation.gov/api/views/saea-dvwc",
+            "issued": "2023-10-11",
+            "landingPage": "https://data.transportation.gov/d/saea-dvwc",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-27",
             "programCode": [
                 "021:036"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
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
+            "title": "Crossing Inventory Warning Device Equipment Summary (8.10)"
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
-            "landingPage": "https://data.transportation.gov/d/saq9-j4ua",
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
-            "identifier": "696.7",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "A compilation of historic documents and articles on the Interstate System, Federal-Aid Highway Program, FHWA, and transportation.",
-            "title": "Highway History - History of FHWA",
-            "isPartOf": "DOT-696",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/infrastructure/history.cfm",
-            "programCode": [
-                "021:011"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -86060,33 +86041,67 @@
                     "title": "History of FHWA"
                 }
             ],
-            "spatial": "National",
-            "dataQuality": true,
+            "identifier": "696.7",
+            "isPartOf": "DOT-696",
+            "issued": "2014-12-29",
+            "keyword": [
+                "articles",
+                "documents",
+                "fhwa",
+                "history",
+                "legislation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/saq9-j4ua",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
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
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/infrastructure/history.cfm",
-            "language": [
-                "en-US"
+            "title": "Highway History - History of FHWA"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/2007+Motor+Vehicle+Occupant+Safety+Survey+(MVOSS)",
+            "agencyProgramURL": "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/National+Telephone+Surveys",
+            "bureauCode": [
+                "021:18"
             ],
-            "phone": "202-366-4856"
+            "categoryDesignation": "Research",
+            "collectionInstrument": "telephone",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
+            "dataQuality": false,
+            "describedBy": "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/2007+Motor+Vehicle+Occupant+Safety+Survey",
+            "description": "Survey data the agency uses to track changes in public attitude, knowledge, and behavior related to occupant protection. The MVOSS also collects information related to Emergency Medical Services and crash experience. The survey is composed of two questionnaires, with one focusing on seat belt use and the other focusing on child occupant protection.",
+            "distribution": [
                 {
-            "accessLevel": "public",
-            "bureauCode": [
-                "021:18"
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.nhtsa.gov/DOT/NHTSA/Traffic%20Injury%20Control/Articles/2007MVOSS/2007MVOSS_SPSS_Combined.sav",
+                    "mediaType": "text/plain",
+                    "title": "Combined Questionnaire (v1&2) (SPSS)"
+                }
             ],
-            "landingPage": "https://data.transportation.gov/d/sbth-45qh",
+            "identifier": "408.5",
+            "isPartOf": "DOT-408",
             "issued": "2008-08-31",
-            "temporal": "2007-01-09/2007-04-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
-            "collectionInstrument": "telephone",
-            "references": [
-                "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/2007+Motor+Vehicle+Occupant+Safety+Survey"
-            ],
             "keyword": [
                 "air bag",
                 "child safety",
@@ -86097,59 +86112,60 @@
                 "protection",
                 "seat belt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "408.5",
+            "landingPage": "https://data.transportation.gov/d/sbth-45qh",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-6401",
+            "programCode": [
+                "021:032"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Highway Traffic Safety Administration"
             },
-            "description": "Survey data the agency uses to track changes in public attitude, knowledge, and behavior related to occupant protection. The MVOSS also collects information related to Emergency Medical Services and crash experience. The survey is composed of two questionnaires, with one focusing on seat belt use and the other focusing on child occupant protection.",
-            "title": "Motor Vehicle Occupant Safety Survey 2007 (MVOSS) - Combined Questionnaire (v1&2) (SPSS)",
-            "isPartOf": "DOT-408",
-            "agencyProgramURL": "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/National+Telephone+Surveys",
-            "programCode": [
-                "021:032"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.nhtsa.gov/DOT/NHTSA/Traffic%20Injury%20Control/Articles/2007MVOSS/2007MVOSS_SPSS_Combined.sav",
-                    "mediaType": "text/plain",
-                    "title": "Combined Questionnaire (v1&2) (SPSS)"
-                }
+            "references": [
+                "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/2007+Motor+Vehicle+Occupant+Safety+Survey"
             ],
-            "describedBy": "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/2007+Motor+Vehicle+Occupant+Safety+Survey",
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/2007+Motor+Vehicle+Occupant+Safety+Survey+(MVOSS)",
+            "temporal": "2007-01-09/2007-04-30",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "phone": "202-366-6401",
-            "language": [
-                "en-US"
-            ]
+            "title": "Motor Vehicle Occupant Safety Survey 2007 (MVOSS) - Combined Questionnaire (v1&2) (SPSS)"
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
-            "landingPage": "https://data.transportation.gov/d/scbx-56mz",
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
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/inctally1.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Train Accidents"
+                }
             ],
+            "identifier": "199.8",
+            "isPartOf": "DOT-199",
+            "issued": "2010-09-29",
             "keyword": [
                 "acts of god",
                 "collisions",
@@ -86160,58 +86176,60 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "199.8",
+            "landingPage": "https://data.transportation.gov/d/scbx-56mz",
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
-            "title": "Rail Equipment Accidents - Train Accidents",
-            "isPartOf": "DOT-199",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:036"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/inctally1.aspx",
-                    "mediaType": "text/csv",
-                    "title": "Train Accidents"
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
+            "title": "Rail Equipment Accidents - Train Accidents"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/schz-tb6z",
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
+                    "description": "2013 Indiana HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/indiana2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Indiana"
+                }
+            ],
+            "identifier": "678.118",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -86225,60 +86243,58 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.118",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Indiana",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/schz-tb6z",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/indiana2013.zip",
-                    "description": "2013 Indiana HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Indiana"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Indiana"
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
-            "landingPage": "https://data.transportation.gov/d/se9z-67ty",
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
+                    "downloadURL": "http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/faf3/netwkdbflow/regboundary/faf3_zone_esri.zip",
+                    "mediaType": "application/zip",
+                    "title": "Regions Boundary Layer"
+                }
             ],
+            "identifier": "286.2",
+            "isPartOf": "DOT-286",
+            "issued": "2013-03-20",
             "keyword": [
                 "commodity",
                 "consumption",
@@ -86303,78 +86319,43 @@
                 "value",
                 "wear"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "286.2",
+            "landingPage": "https://data.transportation.gov/d/se9z-67ty",
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
-            "title": "Freight Analysis Framework - Regions Boundary Layer",
-            "isPartOf": "DOT-286",
-            "agencyProgramURL": "http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/faf3/netwkdbflow/regboundary/faf3_zone_esri.zip",
-                    "mediaType": "application/zip",
-                    "title": "Regions Boundary Layer"
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
+            "title": "Freight Analysis Framework - Regions Boundary Layer"
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
-            "identifier": "https://data.transportation.gov/api/views/sgat-h8mv",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 1997",
-            "title": "Historic HPMS Data (Universe) - 1997",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -86382,50 +86363,85 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/sgat-h8mv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/sgat-h8mv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/sgat-h8mv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/sgat-h8mv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/sgat-h8mv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/sgat-h8mv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/sgat-h8mv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/sgat-h8mv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/sgat-h8mv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/sgat-h8mv",
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
+            "title": "Historic HPMS Data (Universe) - 1997"
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
-            "landingPage": "https://data.transportation.gov/d/sijg-yxm5",
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
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2005NTDxls.exe",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2005 Database"
+                }
             ],
+            "identifier": "21.9",
+            "isPartOf": "DOT-21",
+            "issued": "2010-10-01",
             "keyword": [
                 "agency",
                 "allocation",
@@ -86444,61 +86460,59 @@
                 "urbanized",
                 "vehicles"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John D. Giorgis",
-                "hasEmail": "mailto:john.giorgis@dot.gov"
-            },
-            "identifier": "21.9",
+            "landingPage": "https://data.transportation.gov/d/sijg-yxm5",
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
-            "title": "NTD Annual Module Data Set - 2005 Database",
-            "isPartOf": "DOT-21",
-            "agencyProgramURL": "http://www.ntdprogram.gov",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2005NTDxls.exe",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "2005 Database"
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
+            "title": "NTD Annual Module Data Set - 2005 Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "https://ai.fmcsa.dot.gov/SMS/Tools/Downloads.aspx",
+            "agencyProgramURL": "https://ai.fmcsa.dot.gov/SMS/Tools/Downloads.aspx",
+            "analysisUnit": "Motor Carrier",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/sjpe-nzai",
-            "issued": "2010-12-15",
-            "temporal": "R/2012-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "SMS uses a wide range of data submitted to FMCSA from Federal field enfocement staff, State law enforcement agencies and motor carriers (truck and bus companies).",
-            "references": [
-                "https://ai.fmcsa.dot.gov/SMS/Tools/Downloads.aspx"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Federal Motor Carrier Safety Administration's (FMCSA) Safety Management System (SMS) is an automated data system used by FMCSA to monitor motor carrier on-road safety performance. FMCSA analyzes safety performance by grouping carrier data in the SMS into seven Behavioral Analysis and Safety Improvement Categories (BASICs) which are, in turn, used to identify potential safety  problems with individual carriers and determine when an enforcement intervention might be appropriate.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://ai.fmcsa.dot.gov/SMS/Tools/Downloads.aspx",
+                    "mediaType": "text/html",
+                    "title": "Download Current Data"
+                }
             ],
+            "identifier": "DOT-106",
+            "issued": "2010-12-15",
             "keyword": [
                 "basic",
                 "basics",
@@ -86526,57 +86540,55 @@
                 "unsafe driving",
                 "vehicle maintenance"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "DOT-106",
+            "landingPage": "https://data.transportation.gov/d/sjpe-nzai",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-24",
+            "phone": "202-366-5797",
+            "programCode": [
+                "021:026"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Motor Carrier Safety Administration"
             },
-            "description": "The Federal Motor Carrier Safety Administration's (FMCSA) Safety Management System (SMS) is an automated data system used by FMCSA to monitor motor carrier on-road safety performance. FMCSA analyzes safety performance by grouping carrier data in the SMS into seven Behavioral Analysis and Safety Improvement Categories (BASICs) which are, in turn, used to identify potential safety  problems with individual carriers and determine when an enforcement intervention might be appropriate.",
-            "title": "Carrier Safety Measurement System (CSMS, or SMS) - Raw Data",
-            "agencyProgramURL": "https://ai.fmcsa.dot.gov/SMS/Tools/Downloads.aspx",
-            "programCode": [
-                "021:026"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://ai.fmcsa.dot.gov/SMS/Tools/Downloads.aspx",
-                    "mediaType": "text/html",
-                    "title": "Download Current Data"
-                }
+            "references": [
+                "https://ai.fmcsa.dot.gov/SMS/Tools/Downloads.aspx"
             ],
             "spatial": "National and State",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "https://ai.fmcsa.dot.gov/SMS/Tools/Downloads.aspx",
+            "temporal": "R/2012-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "analysisUnit": "Motor Carrier",
-            "categoryDesignation": "Research",
-            "phone": "202-366-5797",
-            "language": [
-                "en-US"
-            ]
+            "title": "Carrier Safety Measurement System (CSMS, or SMS) - Raw Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "contains sensitive information",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/sjwh-jkqn",
-            "issued": "2018-12-18",
-            "temporal": "R/2013/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": false,
+            "description": "Information regarding individuals who have had their driver licenses revoked, suspended or otherwise denied for cause, or who have been convicted of certain traffic violations, etc.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.transportation.gov/mission/data-inventory-not-available",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "421.0",
+            "issued": "2018-12-18",
             "keyword": [
                 "convictions",
                 "denied",
@@ -86589,73 +86601,41 @@
                 "traffic violations",
                 "withdrawn"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "421.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Information regarding individuals who have had their driver licenses revoked, suspended or otherwise denied for cause, or who have been convicted of certain traffic violations, etc.",
-            "title": "National Driver Register (NDR) -",
+            "landingPage": "https://data.transportation.gov/d/sjwh-jkqn",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-01",
+            "phone": "202-366-4128",
             "primaryITInvestmentUII": "021-165719668",
             "programCode": [
                 "021:035"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.transportation.gov/mission/data-inventory-not-available",
-                    "mediaType": "text/html"
-                }
-            ],
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "rights": "contains sensitive information",
+            "temporal": "R/2013/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-4128"
+            "title": "National Driver Register (NDR) -"
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
-            "identifier": "https://data.transportation.gov/api/views/skf6-dsky",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 1982",
-            "title": "Historic HPMS Data (Sample) - 1982",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -86663,47 +86643,85 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/skf6-dsky/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/skf6-dsky/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/skf6-dsky/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/skf6-dsky/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/skf6-dsky/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/skf6-dsky/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/skf6-dsky/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/skf6-dsky/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/skf6-dsky/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/skf6-dsky",
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
+            "title": "Historic HPMS Data (Sample) - 1982"
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
-            "landingPage": "https://data.transportation.gov/d/sku7-utyd",
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
+            "identifier": "4.1",
+            "isPartOf": "DOT-4",
+            "issued": "2009-10-29",
             "keyword": [
                 "grading",
                 "quality",
@@ -86715,131 +86733,92 @@
                 "uniform",
                 "utqgs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "4.1",
+            "landingPage": "https://data.transportation.gov/d/sku7-utyd",
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
-            "landingPage": "https://data.transportation.gov/d/smay-dskr",
-            "issued": "2021-05-10",
             "@type": "dcat:Dataset",
-            "modified": "2021-07-13",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Chambers",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/smay-dskr",
+            "issued": "2021-05-10",
+            "landingPage": "https://data.transportation.gov/d/smay-dskr",
+            "modified": "2021-07-13",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "2020 Atlantic Hurricane Season"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/smrm-36nv",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2019-12-07",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-05",
-            "keyword": [
-                "contribution of transportation",
-                "transportation satellite accounts"
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
-            "identifier": "https://data.transportation.gov/api/views/smrm-36nv",
             "description": "Contribution of transportation services to the economy and the Transportation Satellite Accounts",
-            "title": "Transportation Economic Trends: Contribution of Transportation - to the Economy",
+            "identifier": "https://data.transportation.gov/api/views/smrm-36nv",
+            "issued": "2019-12-07",
+            "keyword": [
+                "contribution of transportation",
+                "transportation satellite accounts"
+            ],
+            "landingPage": "https://data.transportation.gov/d/smrm-36nv",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-12-05",
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
+            "title": "Transportation Economic Trends: Contribution of Transportation - to the Economy"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/sn3k-dnx7",
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
-            "identifier": "https://data.transportation.gov/api/views/sn3k-dnx7",
             "description": "*This is a \"daily difference\" dataset.  See dataset attachment \"FMCSA Dataset Description and Data Definitions - Select Datasets\" for more information.*  Records showing the history of each authority granted to a carrier/broker/freight forwarder, along with the dates of the original authority action (e.g., \u201cgranted\u201d) and the final authority action (e.g., \u201crevoked\u201d). The dataset contains the DOT number and docket number of the entity that holds or held the authority. As there can be multiple authorities for a single entity, there may be multiple records for an entity.",
-            "title": "AuthHist",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -86847,35 +86826,43 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/sn3k-dnx7",
+            "issued": "2023-04-14",
+            "keyword": [
+                "active",
+                "for-hire motor carriers",
+                "operating authority",
+                "registration status",
+                "revoked",
+                "suspended"
+            ],
+            "landingPage": "https://data.transportation.gov/d/sn3k-dnx7",
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
-            ]
+            ],
+            "title": "AuthHist"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/sn74-xpkp",
-            "issued": "2024-01-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-26",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "TBD",
                 "hasEmail": "mailto:sean.jahanmir@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/sn74-xpkp",
             "description": "",
-            "title": "Top 25 Container Ports by TEU",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -86883,62 +86870,91 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/sn74-xpkp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/sn74-xpkp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/sn74-xpkp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/sn74-xpkp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/sn74-xpkp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/sn74-xpkp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/sn74-xpkp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/sn74-xpkp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/sn74-xpkp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "https://data.transportation.gov/api/views/sn74-xpkp",
+            "issued": "2024-01-10",
+            "landingPage": "https://data.transportation.gov/d/sn74-xpkp",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-07-26",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Top 25 Container Ports by TEU"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/spjd-xkeg",
-            "issued": "2022-01-10",
             "@type": "dcat:Dataset",
-            "modified": "2022-01-10",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Todd Solomon",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/spjd-xkeg",
+            "issued": "2022-01-10",
+            "landingPage": "https://data.transportation.gov/d/spjd-xkeg",
+            "modified": "2022-01-10",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "WZDx for TRB"
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
-            "landingPage": "https://data.transportation.gov/d/sqd9-uqzd",
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
+                    "downloadURL": "http://www.fra.dot.gov/eLib/Details/L03039",
+                    "mediaType": "text/csv",
+                    "title": "Fatigue Accident Validation Database"
+                }
             ],
+            "identifier": "283.9",
+            "isPartOf": "DOT-283",
+            "issued": "2008-03-01",
             "keyword": [
                 "alertness",
                 "employee",
@@ -86949,61 +86965,61 @@
                 "sleep",
                 "work"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "283.9",
+            "landingPage": "https://data.transportation.gov/d/sqd9-uqzd",
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
-            "title": "Work Schedules and Sleep Patterns of Railroad Employees - Fatigue Accident Validation Database",
-            "isPartOf": "DOT-283",
-            "agencyProgramURL": "http://www.fra.dot.gov/Page/P0068",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fra.dot.gov/eLib/Details/L03039",
-                    "mediaType": "text/csv",
-                    "title": "Fatigue Accident Validation Database"
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
+            "title": "Work Schedules and Sleep Patterns of Railroad Employees - Fatigue Accident Validation Database"
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
-            "landingPage": "https://data.transportation.gov/d/sqfg-2qsw",
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
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2000NTDxls.exe",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2000 Database"
+                }
             ],
+            "identifier": "21.4",
+            "isPartOf": "DOT-21",
+            "issued": "2010-10-01",
             "keyword": [
                 "agency",
                 "allocation",
@@ -87022,65 +87038,39 @@
                 "urbanized",
                 "vehicles"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John D. Giorgis",
-                "hasEmail": "mailto:john.giorgis@dot.gov"
-            },
-            "identifier": "21.4",
+            "landingPage": "https://data.transportation.gov/d/sqfg-2qsw",
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
-            "title": "NTD Annual Module Data Set - 2000 Database",
-            "isPartOf": "DOT-21",
-            "agencyProgramURL": "http://www.ntdprogram.gov",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2000NTDxls.exe",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "2000 Database"
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
+            "title": "NTD Annual Module Data Set - 2000 Database"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/sqhc-f96h",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-15",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/sqhc-f96h",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "FRA develop a spatial point layer of the rail bridges over road and water. The bridges are a snapshot and is not an offical or complete inventory of all bridges. Railroads change ownership, railroads are abandoned, bridges are replaced, etc. therefore it cannot be relied upon as being accurate.",
-            "title": "Railroad Bridges",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87088,67 +87078,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/sqhc-f96h/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/sqhc-f96h/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/sqhc-f96h/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/sqhc-f96h/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/sqhc-f96h/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/sqhc-f96h/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/sqhc-f96h/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/sqhc-f96h/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/sqhc-f96h/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/sqhc-f96h",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/sqhc-f96h",
+            "modified": "2024-06-15",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Railroad Bridges"
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
-            "landingPage": "https://data.transportation.gov/d/sqs6-eugv",
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
-            "identifier": "692.6",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - 2007 AADT",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "primaryITInvestmentUII": "021-845083703",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87157,34 +87138,68 @@
                     "title": "2007 AADT"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://hepgis.fhwa.dot.gov/hepgismaps11/#",
-            "theme": [
-                "Transportation"
+            "identifier": "692.6",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Geospatial",
-            "phone": "708-283-3554",
+            "landingPage": "https://data.transportation.gov/d/sqs6-eugv",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
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
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - 2007 AADT"
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
-            "landingPage": "https://data.transportation.gov/d/ss3v-fgyx",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/07novtvt/07novtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "November 2007"
+                }
             ],
+            "identifier": "18.82",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -87194,60 +87209,60 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.82",
+            "landingPage": "https://data.transportation.gov/d/ss3v-fgyx",
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
-            "title": "Monthly Traffic Volume Trends - November 2007",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/07novtvt/07novtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "November 2007"
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
+            "title": "Monthly Traffic Volume Trends - November 2007"
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
-            "landingPage": "https://data.transportation.gov/d/ssyz-77gf",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/11jantvt/11jantvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "January 2011"
+                }
             ],
+            "identifier": "18.14",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -87257,76 +87272,79 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.14",
+            "landingPage": "https://data.transportation.gov/d/ssyz-77gf",
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
-            "title": "Monthly Traffic Volume Trends - January 2011",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/11jantvt/11jantvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "January 2011"
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
+            "title": "Monthly Traffic Volume Trends - January 2011"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/st4i-q58d",
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
             "identifier": "https://data.transportation.gov/api/views/st4i-q58d",
+            "issued": "2021-01-21",
+            "landingPage": "https://data.transportation.gov/d/st4i-q58d",
+            "modified": "2021-01-21",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "COVID"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/su5a-d6gg",
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
+                    "description": "2012 Idaho HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/idaho2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Idaho"
+                }
+            ],
+            "identifier": "678.66",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -87340,83 +87358,46 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.66",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Idaho",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/su5a-d6gg",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/idaho2012.zip",
-                    "description": "2012 Idaho HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Idaho"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Idaho"
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
-            "landingPage": "https://data.transportation.gov/d/sv7d-cas3",
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
-            "identifier": "694.2",
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
@@ -87425,61 +87406,52 @@
                     "title": "Search Official Rulings"
                 }
             ],
-            "describedBy": "http://mutcd.fhwa.dot.gov/orsearch.asp",
-            "dataQuality": false,
+            "identifier": "694.2",
+            "isPartOf": "DOT-694",
+            "issued": "2011-06-01",
+            "keyword": [
+                "experiment",
+                "interpretation",
+                "mutcd",
+                "official ruling"
+            ],
+            "landingPage": "https://data.transportation.gov/d/sv7d-cas3",
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
-            "landingPage": "https://data.transportation.gov/d/swef-k9yw",
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
-                "its joint program office (jpo)",
-                "its world congress",
-                "map",
-                "michigan",
-                "signal phase and timing (spat)",
-                "traveler situation data (tsd)"
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
-            "identifier": "https://data.transportation.gov/api/views/swef-k9yw",
+            "dataQuality": true,
             "description": "During the 2014 ITS World Congress a demonstration of the connected vehicle infrastructure in the City of Detroit was conducted.  The test site included approximately 14 intersections around Detroit\u2019s COBO convention center and involved 9 equipped vehicles. Traveler Situation Data (TSD) was obtained from the data warehouse, and not the data clearinghouse. Only 19 messages were obtained from our query as the current mode of operation of the Test Bed is that the warehouse only contains a few static messages, which are meant to serve as a proxy for future operation in which query submissions will only return message(s) relevant to the context in which the query was submitted. The messages that returned per a query submission communicates a pertinent advisor message which is in part contextualized by location and content.\r\n\r\nNOTE: All Extra Files are attached in 2014 ITS World Congress Connected Vehicle Test Bed Demonstration Vehicle Situation Data",
-            "title": "2014 ITS World Congress Connected Vehicle Test Bed Demonstration Traveler Situation Data",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87487,76 +87459,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/swef-k9yw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/swef-k9yw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/swef-k9yw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/swef-k9yw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/swef-k9yw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/swef-k9yw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/swef-k9yw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/swef-k9yw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/swef-k9yw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Detroit, Michigan",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/swef-k9yw",
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
+                "its joint program office (jpo)",
+                "its world congress",
+                "map",
+                "michigan",
+                "signal phase and timing (spat)",
+                "traveler situation data (tsd)"
+            ],
+            "landingPage": "https://data.transportation.gov/d/swef-k9yw",
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
+            "title": "2014 ITS World Congress Connected Vehicle Test Bed Demonstration Traveler Situation Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/swpm-impx",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2021-08-11",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
-            "keyword": [
-                "commercial tonnage",
-                "gls",
-                "great lakes-st. lawrence seaway",
-                "great lakes st. lawrence seaway development corporation",
-                "reliability",
-                "saint lawrence seaway",
-                "seaway",
-                "sls",
-                "slsdc",
-                "st. lawrence seaway",
-                "tonnage",
-                "vessel transits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:ramond.robinson@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/swpm-impx",
             "description": "This dataset contains monthly performance statistics for the Great Lakes-St. Lawrence Seaway system.",
-            "title": "Great Lakes St. Lawrence Seaway Performance",
-            "programCode": [
-                "021:051"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87564,85 +87538,126 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/swpm-impx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/swpm-impx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/swpm-impx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/swpm-impx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/swpm-impx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/swpm-impx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/swpm-impx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/swpm-impx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/swpm-impx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/swpm-impx",
+            "issued": "2021-08-11",
+            "keyword": [
+                "commercial tonnage",
+                "gls",
+                "great lakes-st. lawrence seaway",
+                "great lakes st. lawrence seaway development corporation",
+                "reliability",
+                "saint lawrence seaway",
+                "seaway",
+                "sls",
+                "slsdc",
+                "st. lawrence seaway",
+                "tonnage",
+                "vessel transits"
+            ],
+            "landingPage": "https://data.transportation.gov/d/swpm-impx",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2025-01-27",
+            "programCode": [
+                "021:051"
+            ],
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
+            "title": "Great Lakes St. Lawrence Seaway Performance"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/sy5r-9hn6",
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
-            "identifier": "https://data.transportation.gov/api/views/sy5r-9hn6",
             "description": "Total reportable fatalities. Fatalities may be reclassified upon subsequent reporting. The Federal Railroad Administration collects accident/incident and operational data from railroads.",
-            "title": "Rail Fatalities",
+            "identifier": "https://data.transportation.gov/api/views/sy5r-9hn6",
+            "issued": "2025-01-03",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/sy5r-9hn6",
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
+            "title": "Rail Fatalities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
+            "accrualPeriodicity": "R/P3M",
+            "agencyDataSeriesURL": "https://www.nhtsa.gov/vehicle-manufacturers/early-warning-reporting#early-warning-reporting-ewr-data-search",
+            "agencyProgramURL": "https://www.nhtsa.gov/vehicle-manufacturers/early-warning-reporting",
+            "analysisUnit": "Vehicles , Tires, Child Safety Seats, Equipment",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/t36j-z9s8",
-            "issued": "2008-09-10",
-            "temporal": "R/2000-10-01/P3M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www-odi.nhtsa.dot.gov/help/ewrSearch.html"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www-odi.nhtsa.dot.gov/help/ewrSearch.html#searchresults",
+            "description": "Manufacturers of motor vehicles, motor vehicle equipment, child safety systems, and tires are required to submit Early Warning Reporting (EWR) information and documentation to NHTSA in order to comply with the Transportation Recall, Enhancement, Accountability and Documentation (TREAD) act. Public or non-confidential manufacturer EWR data is accessible from the web site.Use the EWR Data Search pages to search for manufacturer EWR data associated with Production (for Light Vehicles only), Property Damage, and Death and Injury records.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www-odi.nhtsa.dot.gov/ewr/qb/index.cfm",
+                    "mediaType": "text/plain",
+                    "title": "EWR"
+                }
             ],
+            "identifier": "257.0",
+            "issued": "2008-09-10",
             "keyword": [
                 "automaker",
                 "child safety seats",
@@ -87657,77 +87672,44 @@
                 "vehicles",
                 "warning"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "257.0",
+            "landingPage": "https://data.transportation.gov/d/t36j-z9s8",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-2315",
+            "primaryITInvestmentUII": "021-777552743",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Highway Traffic Safety Administration"
             },
-            "description": "Manufacturers of motor vehicles, motor vehicle equipment, child safety systems, and tires are required to submit Early Warning Reporting (EWR) information and documentation to NHTSA in order to comply with the Transportation Recall, Enhancement, Accountability and Documentation (TREAD) act. Public or non-confidential manufacturer EWR data is accessible from the web site.Use the EWR Data Search pages to search for manufacturer EWR data associated with Production (for Light Vehicles only), Property Damage, and Death and Injury records.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Early Warning Reporting - EWR",
-            "agencyProgramURL": "https://www.nhtsa.gov/vehicle-manufacturers/early-warning-reporting",
-            "primaryITInvestmentUII": "021-777552743",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www-odi.nhtsa.dot.gov/ewr/qb/index.cfm",
-                    "mediaType": "text/plain",
-                    "title": "EWR"
-                }
+            "references": [
+                "http://www-odi.nhtsa.dot.gov/help/ewrSearch.html"
             ],
             "spatial": "N/A",
-            "describedBy": "http://www-odi.nhtsa.dot.gov/help/ewrSearch.html#searchresults",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "https://www.nhtsa.gov/vehicle-manufacturers/early-warning-reporting#early-warning-reporting-ewr-data-search",
+            "temporal": "R/2000-10-01/P3M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P3M",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Vehicles , Tires, Child Safety Seats, Equipment",
-            "phone": "202-366-2315",
-            "language": [
-                "en-US"
-            ]
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Early Warning Reporting - EWR"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.bts.gov/ctp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2021-04-28",
-            "@type": "dcat:Dataset",
-            "temporal": "2015-2019",
-            "modified": "2020-01-01",
-            "keyword": [
-                "bureau of transportation statistics",
-                "counties",
-                "county"
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
-            "identifier": "https://data.transportation.gov/api/views/t3kh-5nek",
             "description": "These are the county-centric transportation statistics currently contained in the dashboard visible at bts.gov/ctp. Data are available for all attributes for each year, 2015 to 2019. Data will soon be added for 2020 and 2021.",
-            "title": "Citizen Connect - County data (live)",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87735,51 +87717,86 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/t3kh-5nek/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/t3kh-5nek/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/t3kh-5nek/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/t3kh-5nek/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/t3kh-5nek/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/t3kh-5nek/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/t3kh-5nek/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/t3kh-5nek/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/t3kh-5nek/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
+            "identifier": "https://data.transportation.gov/api/views/t3kh-5nek",
+            "issued": "2021-04-28",
+            "keyword": [
+                "bureau of transportation statistics",
+                "counties",
+                "county"
+            ],
+            "landingPage": "https://www.bts.gov/ctp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-01-01",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "spatial": "United States",
+            "temporal": "2015-2019",
             "theme": [
                 "County Transportation Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Citizen Connect - County data (live)"
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
-            "landingPage": "https://data.transportation.gov/d/t3z2-hzsy",
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
+                    "description": "This is the DOT Enterprise Data Inventory, which includes the DOT Public Data Listing as well as geospatial metadata harvested to data.gov via geoplatform.gov",
+                    "downloadURL": "https://www.transportation.gov/data.json",
+                    "mediaType": "application/json",
+                    "title": "Enterprise Data Inventory"
+                }
             ],
+            "identifier": "336.1",
+            "isPartOf": "DOT-336",
+            "issued": "2013-11-27",
             "keyword": [
                 "api",
                 "data",
@@ -87789,81 +87806,43 @@
                 "public data listing",
                 "raw data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DOT Socrata",
-                "hasEmail": "mailto:Socrata@dot.gov"
-            },
-            "identifier": "336.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
-            "description": "United States Department of Transportation Public Data Listing. The file is formatted to comply with project open data common core metadata requirements (http://project-open-data.github.io/schema/) and conforms to schema version 1.1",
-            "title": "Department of Transportation Public Data Listing - Enterprise Data Inventory",
-            "isPartOf": "DOT-336",
-            "agencyProgramURL": "https://www.transportation.gov/data",
+            "landingPage": "https://data.transportation.gov/d/t3z2-hzsy",
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
-                    "downloadURL": "https://www.transportation.gov/data.json",
-                    "description": "This is the DOT Enterprise Data Inventory, which includes the DOT Public Data Listing as well as geospatial metadata harvested to data.gov via geoplatform.gov",
-                    "@type": "dcat:Distribution",
-                    "title": "Enterprise Data Inventory"
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
+            "title": "Department of Transportation Public Data Listing - Enterprise Data Inventory"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/t3zq-c6n3",
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
-            "identifier": "https://data.transportation.gov/api/views/t3zq-c6n3",
             "description": "*This is a \"daily difference\" dataset.  See dataset attachment \"FMCSA Dataset Description and Data Definitions - Select Datasets\" for more information.*  Information on insurance forms that were rejected by FMCSA. The dataset contains information on the insurance policy associated with the form, along with the date that the form was rejected and the reason for rejection (e.g., \u201cPolicy is already cancelled\u201d). The dataset contains the DOT number and docket number of the carrier/broker/freight forwarder associated with the policy.",
-            "title": "Rejected",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87871,47 +87850,49 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/t3zq-c6n3",
+            "issued": "2023-04-14",
+            "keyword": [
+                "active",
+                "for-hire motor carriers",
+                "operating authority",
+                "registration status",
+                "revoked",
+                "suspended"
+            ],
+            "landingPage": "https://data.transportation.gov/d/t3zq-c6n3",
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
-            ]
+            ],
+            "title": "Rejected"
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
-            "landingPage": "https://data.transportation.gov/d/t4mr-vbzj",
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
-            "identifier": "692.36",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - Lead",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "primaryITInvestmentUII": "021-845083703",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -87920,31 +87901,68 @@
                     "title": "Lead"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.36",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/t4mr-vbzj",
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
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - Lead"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/t4ud-vrqi",
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
+                    "description": "2011 New York HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/newyork2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 New York"
+                }
+            ],
+            "identifier": "678.34",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -87958,76 +87976,40 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.34",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 New York",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/t4ud-vrqi",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/newyork2011.zip",
-                    "description": "2011 New York HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 New York"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 New York"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2020-09-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "fhwa",
-                "gallons",
-                "gasoline",
-                "weekly"
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
-            "identifier": "https://data.transportation.gov/api/views/t4xw-qp9u",
+            "dataQuality": true,
             "description": "This dataset offers insight on weekly fluctuation of the gasoline product supply, which is an important part of any analysis of construction trends, materials and operating costs associated with highway repair and construction, and changes in traffic volume. These data come directly from the Energy Information Administration (EIA) website. The EIA publishes the average daily amount of gasoline supplied in barrels, which HPPI converts to an average number of gallons of gasoline per week.",
-            "title": "Weekly Gasoline Product Supplied",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88035,50 +88017,83 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/t4xw-qp9u/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/t4xw-qp9u/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/t4xw-qp9u/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/t4xw-qp9u/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/t4xw-qp9u/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/t4xw-qp9u/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/t4xw-qp9u/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/t4xw-qp9u/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/t4xw-qp9u/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/t4xw-qp9u",
+            "issued": "2020-09-30",
+            "keyword": [
+                "fhwa",
+                "gallons",
+                "gasoline",
+                "weekly"
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
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Weekly Gasoline Product Supplied"
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
-            "landingPage": "https://data.transportation.gov/d/t4z4-tp5w",
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
+            "identifier": "122.1",
+            "isPartOf": "DOT-122",
+            "issued": "2000-01-01",
             "keyword": [
                 "bus",
                 "company safety profile",
@@ -88099,55 +88114,45 @@
                 "safety and fitness electronic records",
                 "safety rating"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "122.1",
+            "landingPage": "https://data.transportation.gov/d/t4z4-tp5w",
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
-            "title": "SAFER - Company Snapshot - SAFER - Company Snapshot",
-            "isPartOf": "DOT-122",
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
-            "categoryDesignation": "Research",
-            "analysisUnit": "Motor Carrier",
-            "phone": "202-493-0215",
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFER - Company Snapshot - SAFER - Company Snapshot"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/t59a-58y9",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRA Safety Data Team",
+                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This is the landing page for data for Form 6180.55a Injury/Illness Continuation Sheet.",
+            "identifier": "https://data.transportation.gov/api/views/t59a-58y9",
             "issued": "2024-08-19",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "casualties",
                 "casualty",
@@ -88165,41 +88170,54 @@
                 "trespassers",
                 "worker on duty"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRA Safety Data Team",
-                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/t59a-58y9",
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
-            "identifier": "https://data.transportation.gov/api/views/t59a-58y9",
-            "description": "This is the landing page for data for Form 6180.55a Injury/Illness Continuation Sheet.",
-            "title": "Casualty Reports - Landing Page",
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
+            "title": "Casualty Reports - Landing Page"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
+            "bureauCode": [
+                "021:15"
+            ],
+            "categoryDesignation": "Administrative",
+            "collectionInstrument": "Transportation",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
             },
+            "dataQuality": false,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
+            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
+            "distribution": [
                 {
-            "accessLevel": "public",
-            "bureauCode": [
-                "021:15"
+                    "@type": "dcat:Distribution",
+                    "description": "2013 Arkansas HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/arkansas2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Arkansas"
+                }
             ],
-            "landingPage": "https://data.transportation.gov/d/t5gh-f45y",
+            "identifier": "678.108",
+            "isPartOf": "DOT-678",
             "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
-            "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
             "keyword": [
                 "aadt",
                 "condition",
@@ -88213,85 +88231,41 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.108",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Arkansas",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/t5gh-f45y",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/arkansas2013.zip",
-                    "description": "2013 Arkansas HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Arkansas"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Arkansas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/t6ey-ykqh",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2017-09-20",
-            "@type": "dcat:Dataset",
-            "temporal": "2013-06-01/2014-04-29",
-            "modified": "2017-09-20",
-            "keyword": [
-                "ams pasadena testbed",
-                "analysis modeling and simulation (ams) testbed development",
-                "arterial",
-                "california",
-                "cluster analysis",
-                "freeway",
-                "i-210",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "pasadena",
-                "precipitation data",
-                "sr 134"
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
-            "identifier": "https://data.transportation.gov/api/views/t6ey-ykqh",
+            "dataQuality": true,
             "description": "The data in this data environment was collected from the Pasadena, California testbed, namely I-210, SR 134, and nearby arterials.  The source of these data is from the National Center for Environmental Information \u2013 National Oceanic and Atmospheric Administration. Precipitation information from this data source is used in the cluster analysis.",
-            "title": "AMS Pasadena Precipitation Data",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88299,73 +88273,79 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/t6ey-ykqh/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/t6ey-ykqh/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/t6ey-ykqh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/t6ey-ykqh/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/t6ey-ykqh/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/t6ey-ykqh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/t6ey-ykqh/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/t6ey-ykqh/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/t6ey-ykqh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "I-210, SR 134, Pasadena, California, Los Angeles County",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/t6ey-ykqh",
+            "issued": "2017-09-20",
+            "keyword": [
+                "ams pasadena testbed",
+                "analysis modeling and simulation (ams) testbed development",
+                "arterial",
+                "california",
+                "cluster analysis",
+                "freeway",
+                "i-210",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "pasadena",
+                "precipitation data",
+                "sr 134"
+            ],
+            "landingPage": "https://data.transportation.gov/d/t6ey-ykqh",
             "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "irregular",
+            "modified": "2017-09-20",
+            "programCode": [
+                "021:013"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
+            "spatial": "I-210, SR 134, Pasadena, California, Los Angeles County",
+            "temporal": "2013-06-01/2014-04-29",
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "AMS Pasadena Precipitation Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyProgramURL": "https://www.transportation.gov/tiger",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/t7pd-z8fz",
-            "issued": "2015-10-29",
-            "temporal": "R/2009-01-01/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
-            "references": [
-                "https://www.transportation.gov/sites/dot.gov/files/docs/TIGER_ApplicationListing_2009-2015.xlsx"
-            ],
-            "keyword": [
-                "amount",
-                "applicant",
-                "application",
-                "grant",
-                "tiger"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "1859.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
-            "description": "This dataset provides a list of all applications received for the Transportation Investments Generating Economic Recovery (TIGER) discretionary grant program, whether or not those applications were selected for award.",
-            "title": "TIGER Application List - Raw Data",
+            "dataQuality": true,
+            "describedBy": "https://www.transportation.gov/sites/dot.gov/files/docs/TIGER_ApplicationListing_2009-2015.xlsx",
             "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "agencyProgramURL": "https://www.transportation.gov/tiger",
-            "programCode": [
-                "021:058"
-            ],
+            "description": "This dataset provides a list of all applications received for the Transportation Investments Generating Economic Recovery (TIGER) discretionary grant program, whether or not those applications were selected for award.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88374,33 +88354,69 @@
                     "title": "Raw Data"
                 }
             ],
-            "describedBy": "https://www.transportation.gov/sites/dot.gov/files/docs/TIGER_ApplicationListing_2009-2015.xlsx",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "theme": [
-                "Transportation"
+            "identifier": "1859.0",
+            "issued": "2015-10-29",
+            "keyword": [
+                "amount",
+                "applicant",
+                "application",
+                "grant",
+                "tiger"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Administrative",
+            "landingPage": "https://data.transportation.gov/d/t7pd-z8fz",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-0301"
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-08",
+            "phone": "202-366-0301",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "references": [
+                "https://www.transportation.gov/sites/dot.gov/files/docs/TIGER_ApplicationListing_2009-2015.xlsx"
+            ],
+            "temporal": "R/2009-01-01/P1Y",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "TIGER Application List - Raw Data"
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
-            "landingPage": "https://data.transportation.gov/d/t7wb-wcuq",
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
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/stateoverview.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Accident/Incident Overview by State/Region"
+                }
             ],
+            "identifier": "199.5",
+            "isPartOf": "DOT-199",
+            "issued": "2010-09-29",
             "keyword": [
                 "acts of god",
                 "collisions",
@@ -88411,61 +88427,59 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "199.5",
+            "landingPage": "https://data.transportation.gov/d/t7wb-wcuq",
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
-            "title": "Rail Equipment Accidents - Accident/Incident Overview by State/Region",
-            "isPartOf": "DOT-199",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:036"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/stateoverview.aspx",
-                    "mediaType": "text/csv",
-                    "title": "Accident/Incident Overview by State/Region"
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
+            "title": "Rail Equipment Accidents - Accident/Incident Overview by State/Region"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/2007+Motor+Vehicle+Occupant+Safety+Survey+(MVOSS)",
+            "agencyProgramURL": "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/National+Telephone+Surveys",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/t89b-jaxc",
-            "issued": "2008-08-31",
-            "temporal": "2007-01-09/2007-04-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "telephone",
-            "references": [
-                "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/2007+Motor+Vehicle+Occupant+Safety+Survey"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": false,
+            "describedBy": "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/2007+Motor+Vehicle+Occupant+Safety+Survey",
+            "description": "Survey data the agency uses to track changes in public attitude, knowledge, and behavior related to occupant protection. The MVOSS also collects information related to Emergency Medical Services and crash experience. The survey is composed of two questionnaires, with one focusing on seat belt use and the other focusing on child occupant protection.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.nhtsa.gov/DOT/NHTSA/Traffic%20Injury%20Control/Articles/2007MVOSS/2007MVOSS_SPSS_Version__A.sav",
+                    "mediaType": "text/plain",
+                    "title": "Seat Belt Issues (v1)  (SPSS)"
+                }
             ],
+            "identifier": "DOT-408",
+            "issued": "2008-08-31",
             "keyword": [
                 "air bag",
                 "child safety",
@@ -88476,100 +88490,76 @@
                 "protection",
                 "seat belt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "DOT-408",
+            "landingPage": "https://data.transportation.gov/d/t89b-jaxc",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-6401",
+            "programCode": [
+                "021:032"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Highway Traffic Safety Administration"
             },
-            "description": "Survey data the agency uses to track changes in public attitude, knowledge, and behavior related to occupant protection. The MVOSS also collects information related to Emergency Medical Services and crash experience. The survey is composed of two questionnaires, with one focusing on seat belt use and the other focusing on child occupant protection.",
-            "title": "Motor Vehicle Occupant Safety Survey 2007 (MVOSS)",
-            "agencyProgramURL": "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/National+Telephone+Surveys",
-            "programCode": [
-                "021:032"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.nhtsa.gov/DOT/NHTSA/Traffic%20Injury%20Control/Articles/2007MVOSS/2007MVOSS_SPSS_Version__A.sav",
-                    "mediaType": "text/plain",
-                    "title": "Seat Belt Issues (v1)  (SPSS)"
-                }
+            "references": [
+                "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/2007+Motor+Vehicle+Occupant+Safety+Survey"
             ],
-            "describedBy": "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/2007+Motor+Vehicle+Occupant+Safety+Survey",
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/2007+Motor+Vehicle+Occupant+Safety+Survey+(MVOSS)",
+            "temporal": "2007-01-09/2007-04-30",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "phone": "202-366-6401",
-            "language": [
-                "en-US"
-            ]
+            "title": "Motor Vehicle Occupant Safety Survey 2007 (MVOSS)"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/t9hk-f4es",
-            "issued": "2020-09-24",
             "@type": "dcat:Dataset",
-            "modified": "2024-01-23",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Justyna Goworowska",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/t9hk-f4es",
+            "issued": "2020-09-24",
+            "landingPage": "https://data.transportation.gov/d/t9hk-f4es",
+            "modified": "2024-01-23",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "National Transportation Noise Map FAQs"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ta7r-c25k",
-            "issued": "2021-09-14",
             "@type": "dcat:Dataset",
-            "modified": "2024-01-02",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sean Jahanmir",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/ta7r-c25k",
+            "issued": "2021-09-14",
+            "landingPage": "https://data.transportation.gov/d/ta7r-c25k",
+            "modified": "2024-01-02",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Information"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/tawn-fkc2",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/tawn-fkc2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "SMT 2 - SHORTLINE EAST",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88577,154 +88567,143 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/tawn-fkc2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/tawn-fkc2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/tawn-fkc2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/tawn-fkc2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/tawn-fkc2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/tawn-fkc2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/tawn-fkc2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/tawn-fkc2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/tawn-fkc2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/tawn-fkc2",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/tawn-fkc2",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "SMT 2 - SHORTLINE EAST"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/tb7x-7n7g",
-            "issued": "2021-04-09",
             "@type": "dcat:Dataset",
-            "modified": "2024-02-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Chambers",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/tb7x-7n7g",
+            "issued": "2021-04-09",
+            "landingPage": "https://data.transportation.gov/d/tb7x-7n7g",
+            "modified": "2024-02-08",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Types of Ports"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/tb8s-sy2t",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2020-02-24",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
-            "keyword": [
-                "transportation assets",
-                "transportation infrastructure"
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
-            "identifier": "https://data.transportation.gov/api/views/tb8s-sy2t",
             "description": "List of subtopics related to the value of transportation infrastructure and other assets",
-            "title": "Transportation Economic Trends: Value of Transportation - Subtopic List",
+            "identifier": "https://data.transportation.gov/api/views/tb8s-sy2t",
+            "issued": "2020-02-24",
+            "keyword": [
+                "transportation assets",
+                "transportation infrastructure"
+            ],
+            "landingPage": "https://data.transportation.gov/d/tb8s-sy2t",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-18",
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
-            ]
+            ],
+            "title": "Transportation Economic Trends: Value of Transportation - Subtopic List"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:36"
             ],
-            "landingPage": "https://data.transportation.gov/d/tbj4-ehsu",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NTD Program Support",
+                "hasEmail": "mailto:NTDHelp@dot.gov"
+            },
+            "description": "A national summary of transit Vehicles and Energy Consumption based on data reported by transit agencies to the National Transit Database (NTD) in Report Year 2023. Only Full Reporters report energy consumption, while other reporter types report vehicles.\r\n\r\n\r\nNTD Data Tables organize and summarize data from the 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. This dataset is based on the 2023 Energy Consumption database file and Revenue Vehicles Inventory database file.",
+            "identifier": "https://data.transportation.gov/api/views/tbj4-ehsu",
             "issued": "2024-10-17",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-17",
             "keyword": [
                 "energy source",
                 "fuel source",
                 "gallons consumed",
                 "transit vehicles"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NTD Program Support",
-                "hasEmail": "mailto:NTDHelp@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/tbj4-ehsu",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-10-17",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Transit Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/tbj4-ehsu",
-            "description": "A national summary of transit Vehicles and Energy Consumption based on data reported by transit agencies to the National Transit Database (NTD) in Report Year 2023. Only Full Reporters report energy consumption, while other reporter types report vehicles.\r\n\r\n\r\nNTD Data Tables organize and summarize data from the 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. This dataset is based on the 2023 Energy Consumption database file and Revenue Vehicles Inventory database file.",
-            "title": "2023 NTD Annual Data Summary - Vehicles and Energy Consumption",
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "2023 NTD Annual Data Summary - Vehicles and Energy Consumption"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://isearch.nhtsa.gov/",
+            "agencyProgramURL": "http://isearch.nhtsa.gov/",
+            "analysisUnit": "Person",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/tbqx-2hnn",
-            "issued": "2011-01-18",
-            "temporal": "R/2002-01-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://isearch.nhtsa.gov/"
-            ],
-            "keyword": [
-                "data.gov",
-                "interpretation",
-                "law",
-                "motor vehicle",
-                "safety",
-                "transportation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "320.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "NHTSA's Chief Counsel interprets the statutes that the agency administers and the regulations that it promulgates. The Chief Counsel's interpretations, issued in the form of letters responding to questions from the motor vehicle industry and the public, represent the definitive view of the agency on the questions addressed and may be relied upon by the regulated industry and members of the public. These interpretations have always been available to the public in the agency's technical reference library in Washington. The World Wide Web enables us to make them available through the Internet.",
-            "title": "Federal Motor Vehicle Safety Standards Interpretations -",
-            "isPartOf": "DOT-320",
-            "agencyProgramURL": "http://isearch.nhtsa.gov/",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88732,34 +88711,70 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://isearch.nhtsa.gov/",
+            "identifier": "320.2",
+            "isPartOf": "DOT-320",
+            "issued": "2011-01-18",
+            "keyword": [
+                "data.gov",
+                "interpretation",
+                "law",
+                "motor vehicle",
+                "safety",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/tbqx-2hnn",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-4308",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "http://isearch.nhtsa.gov/"
+            ],
+            "temporal": "R/2002-01-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "analysisUnit": "Person",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4308",
-            "language": [
-                "en-US"
-            ]
+            "title": "Federal Motor Vehicle Safety Standards Interpretations -"
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
-            "landingPage": "https://data.transportation.gov/d/tbyj-u3ix",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/06augtvt/06augtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "August 2006"
+                }
             ],
+            "identifier": "18.97",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -88769,60 +88784,62 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.97",
+            "landingPage": "https://data.transportation.gov/d/tbyj-u3ix",
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
-            "title": "Monthly Traffic Volume Trends - August 2006",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/06augtvt/06augtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "August 2006"
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
+            "title": "Monthly Traffic Volume Trends - August 2006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.locationaffordability.info/lai.aspx%3Furl=download.php",
+            "agencyProgramURL": "http://www.locationaffordability.info/",
+            "analysisUnit": "Core Based Statistical Area (CBSA)",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/tch8-n4af",
-            "issued": "2013-11-19",
-            "temporal": "2006-01-01/2010-12-31",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
-            "references": [
-                "http://www.locationaffordability.info/downloads/ModelingCode.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://lai.locationaffordability.info/lai_data_dictionary.pdf",
+            "describedByType": "application/pdf",
+            "description": "The Location Affordability Index is an indicator of housing and transportation costs at the neighborhood level.  It gives the percentage of a given family's income estimated to be spent on housing and transportation costs in a given location for eight different household profiles.  It is calculated using actual and modeled data for Census block groups in all 942 Combined Base Statistical Areas, which cover 94% of the U.S. population.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.locationaffordability.info/lai.aspx%3Furl=download.php",
+                    "mediaType": "text/html",
+                    "title": "Get Block Groups by Core Based Statistical Area (CBSA)"
+                }
             ],
+            "identifier": "337.5",
+            "isPartOf": "DOT-337",
+            "issued": "2013-11-19",
             "keyword": [
                 "access",
                 "affordability",
@@ -88835,76 +88852,44 @@
                 "transit",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "337.5",
+            "landingPage": "https://data.transportation.gov/d/tch8-n4af",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-08",
+            "phone": "800-245-2691",
+            "programCode": [
+                "021:058"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Secretary of Transportation"
             },
-            "description": "The Location Affordability Index is an indicator of housing and transportation costs at the neighborhood level.  It gives the percentage of a given family's income estimated to be spent on housing and transportation costs in a given location for eight different household profiles.  It is calculated using actual and modeled data for Census block groups in all 942 Combined Base Statistical Areas, which cover 94% of the U.S. population.",
-            "title": "Location Affordability Index - Get Block Groups by Core Based Statistical Area (CBSA)",
-            "isPartOf": "DOT-337",
-            "agencyProgramURL": "http://www.locationaffordability.info/",
-            "describedByType": "application/pdf",
-            "programCode": [
-                "021:058"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.locationaffordability.info/lai.aspx%3Furl=download.php",
-                    "mediaType": "text/html",
-                    "title": "Get Block Groups by Core Based Statistical Area (CBSA)"
-                }
+            "references": [
+                "http://www.locationaffordability.info/downloads/ModelingCode.pdf"
             ],
             "spatial": "Core Based Statistical Area (CBSA)",
-            "describedBy": "http://lai.locationaffordability.info/lai_data_dictionary.pdf",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.locationaffordability.info/lai.aspx%3Furl=download.php",
+            "temporal": "2006-01-01/2010-12-31",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Core Based Statistical Area (CBSA)",
-            "phone": "800-245-2691",
-            "language": [
-                "en-US"
-            ]
+            "title": "Location Affordability Index - Get Block Groups by Core Based Statistical Area (CBSA)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/tchw-zxud",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2021-12-08",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-24",
-            "keyword": [
-                "covid-19",
-                "passenger"
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
-            "identifier": "https://data.transportation.gov/api/views/tchw-zxud",
+            "dataQuality": true,
             "description": "Five passenger travel indicators measured as percent change from pre-COVID-19  baseline, updated weekly (except for transit, updated monthly)",
-            "title": "Passenger Indicators (weekly)",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88912,67 +88897,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/tchw-zxud/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/tchw-zxud/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/tchw-zxud/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/tchw-zxud/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/tchw-zxud/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/tchw-zxud/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/tchw-zxud/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/tchw-zxud/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/tchw-zxud/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/tchw-zxud",
+            "issued": "2021-12-08",
+            "keyword": [
+                "covid-19",
+                "passenger"
+            ],
+            "landingPage": "https://data.transportation.gov/d/tchw-zxud",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1W",
+            "modified": "2023-01-24",
+            "phone": "2023660573",
+            "programCode": [
+                "021:042"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "2023660573",
-            "language": [
-                "en-US"
-            ]
+            "title": "Passenger Indicators (weekly)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.bts.gov/product/transportation-economic-trends",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2022-04-07",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-28",
-            "keyword": [
-                "economic activity",
-                "transportation",
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
-            "identifier": "https://data.transportation.gov/api/views/tcq5-4pgu",
             "description": "Data used in the Bureau of Transportation Statistics' new interactive version of Transportation Economic Trends (TET). TET highlights transportation's role in the economy and explores changes (trends) over time through a series of interactive charts. TET also explains related concepts and data sources for a general audience.\r\n\r\nInteractive visualizations available at: https://data.transportation.gov/stories/s/28tb-cpjy",
-            "title": "Transportation Economic Trends (TET) data",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -88980,47 +88962,79 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/tcq5-4pgu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/tcq5-4pgu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/tcq5-4pgu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/tcq5-4pgu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/tcq5-4pgu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/tcq5-4pgu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/tcq5-4pgu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/tcq5-4pgu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/tcq5-4pgu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/tcq5-4pgu",
+            "issued": "2022-04-07",
+            "keyword": [
+                "economic activity",
+                "transportation",
+                "transportation economics"
+            ],
+            "landingPage": "https://www.bts.gov/product/transportation-economic-trends",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-28",
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
+            "title": "Transportation Economic Trends (TET) data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.nhtsa.gov/About+NHTSA/NHTSA+Electronic+Reading+Room+(ERR)",
+            "agencyProgramURL": "http://www.nhtsa.gov/About+NHTSA/NHTSA+Electronic+Reading+Room+(ERR)",
+            "analysisUnit": "Regulated Entity",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/td9r-bwtp",
-            "issued": "2011-01-18",
-            "temporal": "R/2007-01-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.nhtsa.gov/About+NHTSA/NHTSA+Electronic+Reading+Room+(ERR)"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "NHTSA's issues statements of policy on traffic injury control",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.nhtsa.gov/About+NHTSA/NHTSA+Electronic+Reading+Room+(ERR)",
+                    "mediaType": "text/html"
+                }
             ],
+            "identifier": "321.1",
+            "isPartOf": "DOT-321",
+            "issued": "2011-01-18",
             "keyword": [
                 "control",
                 "data.gov",
@@ -89031,85 +89045,50 @@
                 "traffic",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "321.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "NHTSA's issues statements of policy on traffic injury control",
-            "title": "Traffic Injury Control Statements of Policy -",
-            "isPartOf": "DOT-321",
-            "agencyProgramURL": "http://www.nhtsa.gov/About+NHTSA/NHTSA+Electronic+Reading+Room+(ERR)",
+            "landingPage": "https://data.transportation.gov/d/td9r-bwtp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-01",
+            "phone": "202-366-4308",
             "primaryITInvestmentUII": "021-777552743",
             "programCode": [
                 "021:034"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.nhtsa.gov/About+NHTSA/NHTSA+Electronic+Reading+Room+(ERR)",
-                    "mediaType": "text/html"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "http://www.nhtsa.gov/About+NHTSA/NHTSA+Electronic+Reading+Room+(ERR)"
             ],
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.nhtsa.gov/About+NHTSA/NHTSA+Electronic+Reading+Room+(ERR)",
+            "temporal": "R/2007-01-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Regulated Entity",
-            "phone": "202-366-4308",
-            "language": [
-                "en-US"
-            ]
+            "title": "Traffic Injury Control Statements of Policy -"
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
-            "landingPage": "https://data.transportation.gov/d/tfbd-rkas",
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
-            "identifier": "557.4",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
+            "describedBy": "https://www.civilrights.dot.gov/node/3828",
             "description": "Data related to the management of EEO complaint processing.  Due to the presence of PII, the raw data is not available for public consumption.  However, aggregated data is available in the DOT's NoFEAR Act report and Form 462 Report.  Both are located on the DOT Office of Civil Rights' public website.",
-            "title": "EEO Complaint Processing Data - FHWA No FEAR Data",
-            "isPartOf": "DOT-557",
-            "agencyProgramURL": "http://www.civilrights.dot.gov",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89118,55 +89097,55 @@
                     "title": "FHWA No FEAR Data"
                 }
             ],
-            "describedBy": "https://www.civilrights.dot.gov/node/3828",
-            "dataQuality": false,
+            "identifier": "557.4",
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
+            "landingPage": "https://data.transportation.gov/d/tfbd-rkas",
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
+            "title": "EEO Complaint Processing Data - FHWA No FEAR Data"
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
-                "state",
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
-            "identifier": "https://data.transportation.gov/api/views/tfgg-254g",
+            "dataQuality": true,
             "description": "Summary monthly motor fuel data on the amount of on-highway fuel used at the state level.  Includes the amount of gallons of gasoline/gasohol and special fuel (primarily diesel) taxed each month.",
-            "title": "Monthly Motor Fuel - State",
-            "isPartOf": "Monthly Motor Fuel",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89174,133 +89153,130 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/tfgg-254g/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/tfgg-254g/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/tfgg-254g/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/tfgg-254g/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/tfgg-254g/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/tfgg-254g/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/tfgg-254g/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/tfgg-254g/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/tfgg-254g/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "State",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/tfgg-254g",
+            "isPartOf": "Monthly Motor Fuel",
+            "issued": "2019-01-08",
+            "keyword": [
+                "diesel",
+                "gallons",
+                "gasoline/gasohol",
+                "month",
+                "special fuel",
+                "state",
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
+            "spatial": "State",
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Monthly Motor Fuel - State"
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
-            "landingPage": "https://data.transportation.gov/d/tfnc-995b",
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
+            "dataQuality": true,
+            "description": "Biennial report containing selected information on toll facilities in the United States that has been provided to FHWA by the States and/or various toll authorities regarding toll facilities in operation, financed, or under construction as of January 1.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/tollpage/",
+                    "mediaType": "text/html",
+                    "title": "Toll Facilities in the United States"
+                }
+            ],
             "identifier": "684.2",
+            "isPartOf": "DOT-684",
+            "issued": "2013-09-01",
+            "keyword": [
+                "bridges",
+                "highways",
+                "toll facilities"
+            ],
+            "landingPage": "https://data.transportation.gov/d/tfnc-995b",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5033",
+            "programCode": [
+                "021:011"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "Biennial report containing selected information on toll facilities in the United States that has been provided to FHWA by the States and/or various toll authorities regarding toll facilities in operation, financed, or under construction as of January 1.",
-            "title": "Toll Facilities in the United States - Toll Facilities in the United States",
-            "isPartOf": "DOT-684",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/tollpage/",
-            "programCode": [
-                "021:011"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/tollpage/",
-                    "mediaType": "text/html",
-                    "title": "Toll Facilities in the United States"
-                }
+            "references": [
+                "http://www.fhwa.dot.gov/policyinformation/tollpage/"
             ],
             "spatial": "National, State, Local",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/tollpage/",
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
+            "title": "Toll Facilities in the United States - Toll Facilities in the United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/tfrh-tu9e",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2017-10-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
-            "keyword": [
-                "airfares",
-                "airport pair markets",
-                "aviation",
-                "aviation policy",
-                "city pair",
-                "consumer airfare report",
-                "fare levels",
-                "fares",
-                "office of aviation analysis",
-                "table 1a",
-                "top 1000"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Randall Keizer",
                 "hasEmail": "mailto:Randall.Keizer@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
-            "identifier": "https://data.transportation.gov/api/views/tfrh-tu9e",
+            "dataQuality": true,
             "description": "Available only on the web, provides information for airport pair markets rather than city pair markets. This table only lists airport markets where the origin or destination airport is an airport that has other commercial airports in the same city. Midway Airport (MDW) and O'Hare (ORD) are examples of this.  All records are aggregated as directionless markets.  The combination of Airport_1 and Airport_2 define the airport pair market.  All traffic traveling in both directions is added together.\n\nhttps://www.transportation.gov/policy/aviation-policy/competition-data-analysis/research-reports",
-            "title": "Consumer Airfare Report: Table 1a - All U.S. Airport Pair Markets",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89308,72 +89284,76 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/tfrh-tu9e/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/tfrh-tu9e/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/tfrh-tu9e/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/tfrh-tu9e/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/tfrh-tu9e/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/tfrh-tu9e/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/tfrh-tu9e/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/tfrh-tu9e/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/tfrh-tu9e/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/tfrh-tu9e",
+            "issued": "2017-10-31",
+            "keyword": [
+                "airfares",
+                "airport pair markets",
+                "aviation",
+                "aviation policy",
+                "city pair",
+                "consumer airfare report",
+                "fare levels",
+                "fares",
+                "office of aviation analysis",
+                "table 1a",
+                "top 1000"
+            ],
+            "landingPage": "https://data.transportation.gov/d/tfrh-tu9e",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2025-01-27",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
             "theme": [
                 "Aviation"
-            ]
+            ],
+            "title": "Consumer Airfare Report: Table 1a - All U.S. Airport Pair Markets"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/guidance/fhwaguidance.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/guidance/fhwaguidance.cfm",
+            "analysisUnit": "Regulations",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/tfyc-ma5u",
-            "issued": "2011-01-18",
-            "temporal": "2007-01-01/2013-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.fhwa.dot.gov/guidance/fhwaguidance.cfm"
-            ],
-            "keyword": [
-                "data.gov",
-                "law",
-                "significant guidance",
-                "transportation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "302.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "A list of Significant Guidance documents, which include guidance document disseminated to regulated entities or the general public that may reasonably be anticipated to lead to an annual effect on the economy of $100 million or more or adversely affect in a material way the economy, a sector of the economy, productivity, competition, jobs, the environment, public health or safety, or State, local, or tribal governments or communities; create a serious inconsistency or otherwise interfere with an action taken or planned by another agency; materially alter the budgetary impact of entitlements, grants, user fees, or loan programs or the rights and obligations of recipients thereof; or raise novel legal or policy issues arising out of legal mandates, the President's priorities, or the principles set forth in Executive Order 12866, as further amended.",
-            "title": "Significant Guidance Issued by the Federal Highway Administration -",
-            "isPartOf": "DOT-302",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/guidance/fhwaguidance.cfm",
-            "primaryITInvestmentUII": "021-803057200",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89381,59 +89361,58 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "302.1",
+            "isPartOf": "DOT-302",
+            "issued": "2011-01-18",
+            "keyword": [
+                "data.gov",
+                "law",
+                "significant guidance",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/tfyc-ma5u",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/guidance/fhwaguidance.cfm",
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
+                "http://www.fhwa.dot.gov/guidance/fhwaguidance.cfm"
+            ],
+            "temporal": "2007-01-01/2013-12-31",
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
+            "title": "Significant Guidance Issued by the Federal Highway Administration -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://flh.fhwa.dot.gov/policy/arra/projects.htm",
+            "agencyProgramURL": "http://flh.fhwa.dot.gov/",
+            "analysisUnit": "Project",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/thjn-ztt3",
-            "issued": "2010-11-15",
-            "temporal": "2009-02-01/2010-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Geospatial",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://flh.fhwa.dot.gov/"
-            ],
-            "keyword": [
-                "federal lands",
-                "fish",
-                "forest",
-                "park",
-                "recovery",
-                "wildlife"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "249.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "The map depicts Federal Lands Highway (FLH) American Recovery and Reinvestment Act (ARRA) projects, which are administered through the Federal Lands Divisions (FLD). These include projects that are funded by the Bureau of Land Management (BLM), Bureau of Reclamation (BOR), Fish and Wildlife Service (FWS), National Park Service (NPS), the US Forest Service (USFS) and other State-level projects.",
-            "title": "Map of Federal Lands Highway American Recovery and Reinvestment Act Projects -",
-            "agencyProgramURL": "http://flh.fhwa.dot.gov/",
-            "primaryITInvestmentUII": "021-803057200",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89441,33 +89420,68 @@
                     "mediaType": "application/vnd.google-earth.kmz"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "249.0",
+            "issued": "2010-11-15",
+            "keyword": [
+                "federal lands",
+                "fish",
+                "forest",
+                "park",
+                "recovery",
+                "wildlife"
+            ],
+            "landingPage": "https://data.transportation.gov/d/thjn-ztt3",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://flh.fhwa.dot.gov/policy/arra/projects.htm",
+            "modified": "2024-05-08",
+            "primaryITInvestmentUII": "021-803057200",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "references": [
+                "http://flh.fhwa.dot.gov/"
+            ],
+            "temporal": "2009-02-01/2010-11-15",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "analysisUnit": "Project",
-            "categoryDesignation": "Geospatial",
-            "language": [
-                "en-US"
-            ]
+            "title": "Map of Federal Lands Highway American Recovery and Reinvestment Act Projects -"
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
-            "landingPage": "https://data.transportation.gov/d/thmi-6nb8",
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
+            "identifier": "DOT-1837",
+            "issued": "2014-06-30",
             "keyword": [
                 "benefit",
                 "effectiveness",
@@ -89476,58 +89490,58 @@
                 "fuel system integrity",
                 "post-crash fires"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "DOT-1837",
+            "landingPage": "https://data.transportation.gov/d/thmi-6nb8",
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
-            "title": "Fuel System Integrity-Rear, FMVSS 301R",
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
+            "temporal": "2005-01-01/2009-12-31",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "agencyDataSeriesURL": "http://www-nrd.nhtsa.dot.gov/Pubs/812038.pdf",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4696",
-            "language": [
-                "en-US"
-            ]
+            "title": "Fuel System Integrity-Rear, FMVSS 301R"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyProgramURL": "http://www.nhtsa.gov/fuel-economy",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/tiu5-5k6h",
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
+                    "description": "The NHTSA fleet and manufacturer reports provide comparisons of fuel economy performance data in relationship to the required fuel economy standards for each model year.  These reports include manufacturer compliance information verified by EPA.  Future model year estimated data from manufacturer\u2019s pre- and mid-model year reports will be added at a later time. Also available in PDF and XLS.  ",
+                    "downloadURL": "http://www.nhtsa.gov/CAFE_PIC/CAFE_PIC_Mfr_LIVE.html",
+                    "mediaType": "text/html",
+                    "title": "Manufacturer Fuel Economy Performance Report"
+                }
             ],
+            "identifier": "1862.3",
+            "isPartOf": "DOT-1862",
+            "issued": "2015-12-16",
             "keyword": [
                 "amfa",
                 "civil penalties",
@@ -89544,80 +89558,48 @@
                 "report",
                 "shortfall"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "1862.3",
+            "landingPage": "https://data.transportation.gov/d/tiu5-5k6h",
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
-            "title": "CAFE (Corporate Average Fuel Economy) - Manufacturer Fuel Economy Performance Report",
-            "isPartOf": "DOT-1862",
-            "agencyProgramURL": "http://www.nhtsa.gov/fuel-economy",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.nhtsa.gov/CAFE_PIC/CAFE_PIC_Mfr_LIVE.html",
-                    "description": "The NHTSA fleet and manufacturer reports provide comparisons of fuel economy performance data in relationship to the required fuel economy standards for each model year.  These reports include manufacturer compliance information verified by EPA.  Future model year estimated data from manufacturer\u2019s pre- and mid-model year reports will be added at a later time. Also available in PDF and XLS.  ",
-                    "@type": "dcat:Distribution",
-                    "title": "Manufacturer Fuel Economy Performance Report"
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
+            "title": "CAFE (Corporate Average Fuel Economy) - Manufacturer Fuel Economy Performance Report"
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
-            "landingPage": "https://data.transportation.gov/d/tj37-auv9",
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
-            "identifier": "364.21",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2003",
-            "isPartOf": "DOT-364",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
-            "primaryITInvestmentUII": "021-621341357",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89626,53 +89608,50 @@
                     "title": "Event Data Records Reports - 2003"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.21",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/tj37-auv9",
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
+            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://catalog.data.faa.gov/dataset/terminal-area-vfr-charts",
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
-            "identifier": "845b3607-95c8-4d1e-a4e9-4437d76473a1",
             "description": "The Federal Aviation Administration (FAA) digital-Visual Chart series is designed to meet the needs of users who require georeferenced raster images of FAA Visual Flight Rules (VFR) Terminal Area charts. An Aeronautical Raster Chart is a digital image of an FAA VFR Chart. All information that is part of the paper chart is included in the file. The area inside the neat line is georeferenced to the surface of the earth. Only the main body of the chart is accurately georeferenced. Each digital-Visual Chart is provided in one TIF file. The files are 300 dots per inch and 8-bit color.",
-            "title": "Terminal Area VFR Charts",
-            "primaryITInvestmentUII": "021-129509270",
-            "programCode": [
-                "021:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89681,51 +89660,52 @@
                     "title": "Aeronautical Information Services Digital Products"
                 }
             ],
-            "systemOfRecords": "https://www.govinfo.gov/content/pkg/FR-2016-08-15/pdf/2016-19354.pdf",
+            "identifier": "845b3607-95c8-4d1e-a4e9-4437d76473a1",
+            "issued": "2020-11-14",
+            "keyword": [
+                "georeference",
+                "geospatial",
+                "raster",
+                "vfr",
+                "visual-chart"
+            ],
+            "landingPage": "https://catalog.data.faa.gov/dataset/terminal-area-vfr-charts",
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
+            "title": "Terminal Area VFR Charts"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "contact POC",
+            "accrualPeriodicity": "R/PT1S",
+            "agencyProgramURL": "http://www.dot.gov/records",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/tjf7-7ymz",
-            "issued": "2018-12-18",
-            "temporal": "R/2014/PT1S",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-01",
-            "keyword": [
-                "archives",
-                "disposition",
-                "nara",
-                "record schedules"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "484.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
             "description": "Contains NHTSA record schedules. SYSTEMS INTEGRATION (NPO-430)",
-            "title": "Comprehensive Records Schedule - Comprehensive Record Schedule",
-            "isPartOf": "DOT-484",
-            "primaryITInvestmentUII": "021-381281982",
-            "agencyProgramURL": "http://www.dot.gov/records",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89734,32 +89714,67 @@
                     "title": "Comprehensive Record Schedule"
                 }
             ],
-            "dataQuality": false,
+            "identifier": "484.2",
+            "isPartOf": "DOT-484",
+            "issued": "2018-12-18",
+            "keyword": [
+                "archives",
+                "disposition",
+                "nara",
+                "record schedules"
+            ],
+            "landingPage": "https://data.transportation.gov/d/tjf7-7ymz",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-01",
+            "phone": "202-366-4939",
+            "primaryITInvestmentUII": "021-381281982",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "rights": "contact POC",
+            "temporal": "R/2014/PT1S",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/PT1S",
-            "categoryDesignation": "Research",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-4939"
+            "title": "Comprehensive Records Schedule - Comprehensive Record Schedule"
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
-            "landingPage": "https://data.transportation.gov/d/tk78-97gv",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/03augtvt/03augtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "August 2003"
+                }
             ],
+            "identifier": "18.133",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -89769,60 +89784,60 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.133",
+            "landingPage": "https://data.transportation.gov/d/tk78-97gv",
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
-            "title": "Monthly Traffic Volume Trends - August 2003",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/03augtvt/03augtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "August 2003"
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
+            "title": "Monthly Traffic Volume Trends - August 2003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/NASS/NMVCCS/",
+            "analysisUnit": "automobile crash",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/tkhe-55ca",
-            "issued": "2008-12-05",
-            "temporal": "2005-01-01/2007-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "NMVCCS.exe",
-            "references": [
-                "http://www-nrd.nhtsa.dot.gov/Cats/listpublications.aspx%3FId=227&ShowBy=Category"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/Cats/listpublications.aspx%3FId=227&ShowBy=Category",
+            "description": "The National Motor Vehicle Crash Causation Survey (NMVVCS) was a nationwide survey of crashes involving light passenger vehicles, with a focus on the factors related to pre-crash events.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://crashviewer.nhtsa.dot.gov/LegacyNMVCCS/Search",
+                    "mediaType": "text/html",
+                    "title": "NMVCCS XML Case Viewer"
+                }
             ],
+            "identifier": "376.1",
+            "isPartOf": "DOT-376",
+            "issued": "2008-12-05",
             "keyword": [
                 "avoidance",
                 "causation",
@@ -89835,78 +89850,43 @@
                 "pre-crash",
                 "vehicle"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "376.1",
+            "landingPage": "https://data.transportation.gov/d/tkhe-55ca",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-4998",
+            "programCode": [
+                "021:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Highway Traffic Safety Administration"
             },
-            "description": "The National Motor Vehicle Crash Causation Survey (NMVVCS) was a nationwide survey of crashes involving light passenger vehicles, with a focus on the factors related to pre-crash events.",
-            "title": "National Motor Vehicle Crash Causation Survey (NMVCCS) - NMVCCS XML Case Viewer",
-            "isPartOf": "DOT-376",
-            "programCode": [
-                "021:031"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://crashviewer.nhtsa.dot.gov/LegacyNMVCCS/Search",
-                    "mediaType": "text/html",
-                    "title": "NMVCCS XML Case Viewer"
-                }
+            "references": [
+                "http://www-nrd.nhtsa.dot.gov/Cats/listpublications.aspx%3FId=227&ShowBy=Category"
             ],
             "spatial": "NASS CDS PSUs",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/Cats/listpublications.aspx%3FId=227&ShowBy=Category",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/NASS/NMVCCS/",
+            "temporal": "2005-01-01/2007-12-31",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "analysisUnit": "automobile crash",
-            "phone": "202-366-4998",
-            "language": [
-                "en-US"
-            ]
+            "title": "National Motor Vehicle Crash Causation Survey (NMVCCS) - NMVCCS XML Case Viewer"
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
-            "identifier": "https://data.transportation.gov/api/views/tmwr-mmw6",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 1986",
-            "title": "Historic HPMS Data (Sample) - 1986",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89914,64 +89894,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/tmwr-mmw6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/tmwr-mmw6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/tmwr-mmw6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/tmwr-mmw6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/tmwr-mmw6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/tmwr-mmw6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/tmwr-mmw6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/tmwr-mmw6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/tmwr-mmw6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/tmwr-mmw6",
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
+            "title": "Historic HPMS Data (Sample) - 1986"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/tnfy-euyi",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2023-12-05",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
-            "keyword": [
-                "public transit",
-                "ridership",
-                "unlinked passenger trips",
-                "vehicle revenue miles",
-                "weekly"
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
-            "identifier": "https://data.transportation.gov/api/views/tnfy-euyi",
             "description": "Beginning in 2023, certain agencies are required to submit one week of service data on a monthly basis to comply with FTA\u2019s Weekly Reference reporting requirement on form WE-20. This data release will therefore present the limited set of key indicators reported by transit agencies on this form and will be updated each month with the most current data.\n\nThe resulting dataset provides data users with data shortly after the transit service was provided and consumed, over one month in advance of FTA\u2019s routine update to the Monthly Ridership Time Series dataset. One use of this data is for reference in understanding ridership patterns (e.g., to develop to a full month estimate ahead of when the data reflecting the given month of service is released by FTA at the end of the following month). \n\nGenerally, FTA has defined the reference week to be the second or third full week of the month. All sampled agencies will report data referencing the same reference week. \n\nThe form collects the following service data points, as described in the metadata below: \n\u2022\tWeekday 5-day UPT total for the reference week; \n\u2022\tWeekday 5-day VRM total for the reference week; \n\u2022\tWeekend 2-day UPT total for either the weekend preceding or following the reference week; and \n\u2022\tWeekend 2-day VRM total for either the weekend preceding or following the reference week. \n\u2022\tVehicles Operated in Maximum Service (vanpool mode only) for the reference week.\n\nFTA has also derived the change from the prior month for the same agency/mode/type of service/data point. Users should take caution when aggregating this measure and are encouraged to use the dataset export to measure service trends at a higher level (i.e., by reporter or nationally).\n\nUpdates to this dataset have been temporarily paused. Data is current through November 2024. Please check back in February 2025 for potential updates. For any questions regarding this dataset, please contact the NTD helpdesk at ntdhelp@dot.gov .",
-            "title": "Weekly Transit Service Reference Data",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -89979,43 +89962,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/tnfy-euyi/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/tnfy-euyi/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/tnfy-euyi/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/tnfy-euyi/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/tnfy-euyi/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/tnfy-euyi/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/tnfy-euyi/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/tnfy-euyi/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/tnfy-euyi/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/tnfy-euyi",
+            "issued": "2023-12-05",
+            "keyword": [
+                "public transit",
+                "ridership",
+                "unlinked passenger trips",
+                "vehicle revenue miles",
+                "weekly"
+            ],
+            "landingPage": "https://data.transportation.gov/d/tnfy-euyi",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-27",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Transit Administration"
+            },
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "Weekly Transit Service Reference Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/tnrh-r6p5",
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
+                    "description": "2013 Oregon HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/oregon2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Oregon"
+                }
+            ],
+            "identifier": "678.141",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -90029,82 +90047,45 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.141",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Oregon",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/tnrh-r6p5",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/oregon2013.zip",
-                    "description": "2013 Oregon HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Oregon"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Oregon"
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
-            "landingPage": "https://data.transportation.gov/d/tpcf-qxcb",
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
-            "identifier": "692.9",
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
@@ -90113,56 +90094,50 @@
                     "title": "Draft National Primary Freight Network"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.9",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/tpcf-qxcb",
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
-            "landingPage": "https://data.transportation.gov/d/tpsq-zrwa",
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
-            "identifier": "https://data.transportation.gov/api/views/tpsq-zrwa",
             "description": "The main dataset is a 9 MB file of trajectory data (I294_L2_final.csv) that contains position, speed, and acceleration data for small and large automated (L2) and non-automated vehicles on a highway in a suburban environment. Supporting files include aerial reference images for twelve distinct data collection \u201cRuns\u201d (I294_L2_Run_X_ref_image_with_lanes.png, where X equals 5, 28, 30, 36, 38, and 42 for southbound runs and 23, 29, 31, 33, 35, and 41 for northbound runs). Associated centerline files are also provided for each \u201cRun\u201d (I-294-L2-Run_X-geometry-with-ramps.csv). In each centerline file, x and y coordinates (in meters) marking each lane centerline are provided. The origin point of the reference image is located at the top left corner. Additionally, in each centerline file, an indicator variable is used for each lane to define the following types of road sections: 0=no ramp, 1=on-ramps, 2=off-ramps, and 3=weaving segments. The number attached to each column header is the numerical ID assigned for the specific lane (see \u201cTGSIM \u2013 Centerline Data Dictionary \u2013 I294 L2.csv\u201d for more details).  The dataset defines eight lanes (four lanes in each direction) using these centerline files. Images that map the lanes of interest to the numerical lane IDs referenced in the trajectory dataset are stored in the folder titled \u201cAnnotation on Regions.zip\u201d. The southbound lanes are shown visually in I294_L2_lane-2.png through I294_L2_lane-5.png and the northbound lanes are shown visually in I294_L2_lane2.png through I294_L2_lane5.png.\n\nThis dataset was collected as part of the Third Generation Simulation Data (TGSIM): A Closer Look at the Impacts of Automated Driving Systems on Human Behavior project. During the project, six trajectory datasets capable of characterizing human-automated vehicle interactions under a diverse set of scenarios in highway and city environments were collected and processed. For more information, see the project report found here: https://rosap.ntl.bts.gov/view/dot/74647. This dataset, which is one of the six collected as part of the TGSIM project, contains data collected using one high-resolution 8K camera mounted on a helicopter that followed two SAE Level 2 ADAS-equipped vehicles through automated lane change maneuvers and as part of a string once the desired lane was achieved and ACC was enabled. The helicopter then followed the string of vehicles (which sometimes broke from the sting due to large following distances) northbound through the 4.8 km section of highway at an altitude of 300 meters. The goal of the data collection effort was to collect data related to human drivers' responses to automated lane changes and as part of a string. The road segment has four lanes in each direction and covers a major on-ramp and one off-ramp in the southbound direction and one on-ramp as well as two off-ramps in the northbound direction. The segment of highway is operated by Illinois Tollway and contains a high percentage of heavy vehicles. The camera captured footage during the evening rush hour (3:00 PM-5:00 PM CT) on a cloudy day.\n\nAs part of this dataset, the following files were provided:\n<ul><li>I294_L2_final.csv contains the numerical data to be used for analysis that includes vehicle level trajectory data at every 0.1 second. Vehicle size (small or large), width, length, and whether the vehicle was one of the L2 test vehicles (\"yes\" or \"no\") are provided with instantaneous location, speed, and acceleration data. All distance measurements (width, length, location) were converted from pixels to meters using the following conversion factor: 1 pixel = 0.3-meter conversion.</li>\n<li>I294_L2_Run_X_ref_image_with_lanes.png are the aerial reference images that define the geographic region and associated roadway segments of interest (see bounding boxes on northbound and southbound lanes) for each run X.</li>\n<li>I294_L2_Run_X-geometry-with-ramps.csv contain the coordinates that define the lane centerlines for each Run X. T",
-            "title": "Third Generation Simulation Data (TGSIM) I-294 L2 Trajectories",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -90170,47 +90145,89 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/tpsq-zrwa/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/tpsq-zrwa/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/tpsq-zrwa/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/tpsq-zrwa/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/tpsq-zrwa/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/tpsq-zrwa/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/tpsq-zrwa/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/tpsq-zrwa/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/tpsq-zrwa/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "I-90/I94 in Chicago, IL; I-294 near Hinsdale, IL; I-395 in Washington DC; George Washington University Campus, Washington DC (Foggy Bottom)",
+            "identifier": "https://data.transportation.gov/api/views/tpsq-zrwa",
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
+            "landingPage": "https://data.transportation.gov/d/tpsq-zrwa",
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
+            "title": "Third Generation Simulation Data (TGSIM) I-294 L2 Trajectories"
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
-            "landingPage": "https://data.transportation.gov/d/tpw2-4i7n",
-            "issued": "2006-07-14",
-            "temporal": "2003-01-01/2003-12-31",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "http://ai.fmcsa.dot.gov/ltccs/default.asp%3Fpage=data",
-            "modified": "2024-05-24",
-            "references": [
-                "http://ai.fmcsa.dot.gov/ltccs/data/documents/LTCCS_Manual_Public.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://ai.fmcsa.dot.gov/ltccs/data/documents/LTCCS_Codebook.pdf",
+            "describedByType": "application/pdf",
+            "description": "The Large Truck* Crash Causation Study (LTCCS) is based on a three-year data collection project conducted by the Federal Motor Carrier Safety Administration (FMCSA) and the National Highway Traffic Safety Administration (NHTSA) of the U.S. Department of Transportation (DOT). LTCCS is the first-ever national study to attempt to determine the critical events and associated factors that contribute to serious large truck crashes allowing DOT and others to implement effective countermeasures to reduce the occurrence and severity of these crashes.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://ai.fmcsa.dot.gov/ltccs/Data/TEXT/Public/LTCCS_db_txt_public_02.zip",
+                    "mediaType": "text/csv",
+                    "title": "File 2 (TXT)"
+                }
             ],
+            "identifier": "97.4",
+            "isPartOf": "DOT-97",
+            "issued": "2006-07-14",
             "keyword": [
                 "crash",
                 "federal motor carrier safety administration",
@@ -90219,100 +90236,68 @@
                 "large truck crash causation study",
                 "ltccs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "97.4",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
-            "description": "The Large Truck* Crash Causation Study (LTCCS) is based on a three-year data collection project conducted by the Federal Motor Carrier Safety Administration (FMCSA) and the National Highway Traffic Safety Administration (NHTSA) of the U.S. Department of Transportation (DOT). LTCCS is the first-ever national study to attempt to determine the critical events and associated factors that contribute to serious large truck crashes allowing DOT and others to implement effective countermeasures to reduce the occurrence and severity of these crashes.",
-            "title": "Large Truck Crash Causation Study (LTCCS) - File 2 (TXT)",
-            "isPartOf": "DOT-97",
-            "agencyProgramURL": "http://ai.fmcsa.dot.gov/ltccs/default.asp",
-            "describedByType": "application/pdf",
+            "landingPage": "https://data.transportation.gov/d/tpw2-4i7n",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-24",
+            "phone": "202-366-0324",
             "primaryITInvestmentUII": "021-155552608",
             "programCode": [
                 "021:022"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://ai.fmcsa.dot.gov/ltccs/Data/TEXT/Public/LTCCS_db_txt_public_02.zip",
-                    "mediaType": "text/csv",
-                    "title": "File 2 (TXT)"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "references": [
+                "http://ai.fmcsa.dot.gov/ltccs/data/documents/LTCCS_Manual_Public.pdf"
             ],
             "spatial": "National estimates",
-            "describedBy": "http://ai.fmcsa.dot.gov/ltccs/data/documents/LTCCS_Codebook.pdf",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/ltccs/default.asp%3Fpage=data",
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
+            "title": "Large Truck Crash Causation Study (LTCCS) - File 2 (TXT)"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/tpws-52ei",
-            "issued": "2024-05-02",
             "@type": "dcat:Dataset",
-            "modified": "2024-05-30",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joe McGill",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/tpws-52ei",
+            "issued": "2024-05-02",
+            "landingPage": "https://data.transportation.gov/d/tpws-52ei",
+            "modified": "2024-05-30",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "2022 NCFO Data Files"
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
-            "landingPage": "https://data.transportation.gov/d/tpzy-7wrk",
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
-            "identifier": "99.4",
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
@@ -90321,34 +90306,64 @@
                     "title": "QCMobile API"
                 }
             ],
-            "spatial": "Carrier, Driver",
-            "dataQuality": false,
+            "identifier": "99.4",
+            "isPartOf": "DOT-99",
+            "issued": "2018-12-17",
+            "keyword": [
+                "driver insurance; carrier registration; carrier license"
+            ],
+            "landingPage": "https://data.transportation.gov/d/tpzy-7wrk",
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
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://www.safercar.gov/Safety+Ratings",
+            "agencyProgramURL": "http://www.safercar.gov/Vehicle+Shoppers",
+            "analysisUnit": "Vehicles",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/tqxb-yd4s",
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
+                    "downloadURL": "http://webapi.nhtsa.gov/Default.aspx%3FSafetyRatings/API/5",
+                    "mediaType": "application/json",
+                    "title": "New Car Assessment Program (NCAP) - 5 Star Safety Ratings"
+                }
             ],
+            "identifier": "248.1",
+            "isPartOf": "DOT-248",
+            "issued": "2010-01-05",
             "keyword": [
                 "5",
                 "assessment",
@@ -90362,87 +90377,51 @@
                 "safety",
                 "star"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "248.1",
+            "landingPage": "https://data.transportation.gov/d/tqxb-yd4s",
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
-            "title": "New Car Assessment Program (NCAP) - 5 Star Safety Ratings - New Car Assessment Program (NCAP) - 5 Star Safety Ratings",
-            "isPartOf": "DOT-248",
-            "agencyProgramURL": "http://www.safercar.gov/Vehicle+Shoppers",
-            "programCode": [
-                "021:031"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://webapi.nhtsa.gov/Default.aspx%3FSafetyRatings/API/5",
-                    "mediaType": "application/json",
-                    "title": "New Car Assessment Program (NCAP) - 5 Star Safety Ratings"
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
+            "title": "New Car Assessment Program (NCAP) - 5 Star Safety Ratings - New Car Assessment Program (NCAP) - 5 Star Safety Ratings"
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
-            "landingPage": "https://data.transportation.gov/d/ts96-w777",
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
-            "identifier": "97.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
-            "description": "The Large Truck* Crash Causation Study (LTCCS) is based on a three-year data collection project conducted by the Federal Motor Carrier Safety Administration (FMCSA) and the National Highway Traffic Safety Administration (NHTSA) of the U.S. Department of Transportation (DOT). LTCCS is the first-ever national study to attempt to determine the critical events and associated factors that contribute to serious large truck crashes allowing DOT and others to implement effective countermeasures to reduce the occurrence and severity of these crashes.",
-            "title": "Large Truck Crash Causation Study (LTCCS) - File 2 (Excel)",
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
@@ -90451,36 +90430,72 @@
                     "title": "File 2 (Excel)"
                 }
             ],
-            "spatial": "National estimates",
-            "describedBy": "http://ai.fmcsa.dot.gov/ltccs/data/documents/LTCCS_Codebook.pdf",
-            "dataQuality": true,
+            "identifier": "97.2",
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
+            "landingPage": "https://data.transportation.gov/d/ts96-w777",
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
+            "title": "Large Truck Crash Causation Study (LTCCS) - File 2 (Excel)"
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
-            "landingPage": "https://data.transportation.gov/d/ttq4-28wm",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/02octtvt/tvtoct02.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "October 2002"
+                }
             ],
+            "identifier": "18.143",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -90490,84 +90505,48 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.143",
+            "landingPage": "https://data.transportation.gov/d/ttq4-28wm",
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
-            "title": "Monthly Traffic Volume Trends - October 2002",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/02octtvt/tvtoct02.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "October 2002"
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
+            "title": "Monthly Traffic Volume Trends - October 2002"
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
-            "landingPage": "https://data.transportation.gov/d/tu8k-qqpr",
-            "issued": "1999-04-26",
-            "temporal": "1999/2015",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.nhtsa.gov/Research/Databases+and+Software/NHTSA+Test+Reference+Guides"
-            ],
-            "keyword": [
-                "compliance",
-                "component",
-                "test",
-                "vehicle"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "1842.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "The NHTSA Component Test Database contains engineering data measured during various types of research.",
-            "title": "Component Test Database - Latest Tests",
-            "isPartOf": "DOT-1842",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research",
-            "primaryITInvestmentUII": "021-961265599",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -90576,33 +90555,70 @@
                     "title": "Latest Tests"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "1842.2",
+            "isPartOf": "DOT-1842",
+            "issued": "1999-04-26",
+            "keyword": [
+                "compliance",
+                "component",
+                "test",
+                "vehicle"
+            ],
+            "landingPage": "https://data.transportation.gov/d/tu8k-qqpr",
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
+            "temporal": "1999/2015",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4712",
-            "language": [
-                "en-US"
-            ]
+            "title": "Component Test Database - Latest Tests"
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
-            "landingPage": "https://data.transportation.gov/d/tv6d-4v97",
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
+                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/nits/Noncrash%20injuries/2003-2006/NiTS%202003-2006%20noncrash%20injuries.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2003-2006 Noncrash injuries"
+                }
             ],
+            "identifier": "288.2",
+            "isPartOf": "DOT-288",
+            "issued": "2009-01-27",
             "keyword": [
                 "crash",
                 "death",
@@ -90618,83 +90634,49 @@
                 "vehicle",
                 "victim"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "288.2",
+            "landingPage": "https://data.transportation.gov/d/tv6d-4v97",
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
-            "title": "Not in Traffic Surveillance (NiTS) - 2003-2006 Noncrash injuries",
-            "isPartOf": "DOT-288",
-            "agencyProgramURL": "http://www.nhtsa.gov/Data/State+Data+Programs",
-            "programCode": [
-                "021:032"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/nits/Noncrash%20injuries/2003-2006/NiTS%202003-2006%20noncrash%20injuries.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "2003-2006 Noncrash injuries"
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
+            "title": "Not in Traffic Surveillance (NiTS) - 2003-2006 Noncrash injuries"
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
-            "landingPage": "https://data.transportation.gov/d/tvh4-34xw",
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
-            "identifier": "364.20",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2002",
-            "isPartOf": "DOT-364",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
-            "primaryITInvestmentUII": "021-621341357",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -90703,54 +90685,54 @@
                     "title": "Event Data Records Reports - 2002"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.nhtsa.gov",
-            "theme": [
-                "Transportation"
+            "identifier": "364.20",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Test",
-            "phone": "202-366-4712",
+            "landingPage": "https://data.transportation.gov/d/tvh4-34xw",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
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
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "This dataset contains controlled unclassified information (Information technology systems security information)",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/tw86-qveb",
-            "issued": "2014-11-21",
-            "temporal": "R/2014-11-21/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "cybersecurity",
-                "information technology",
-                "transportation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "1633.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
             "description": "This data set contains information about the security configuration and vulnerability status of DOT information technology assets.  The information identifies individual hardware assets, their security configuration settings, their status with respect to known cyber security vulnerabilities, the software products, version numbers and service packs installed thereon, and the individual users who access those information systems.",
-            "title": "DOT Automated Enterprise Continuous Monitoring Program -",
-            "primaryITInvestmentUII": "021-325711125",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -90758,28 +90740,58 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "theme": [
-                "Transportation"
+            "identifier": "1633.0",
+            "issued": "2014-11-21",
+            "keyword": [
+                "cybersecurity",
+                "information technology",
+                "transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/tw86-qveb",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-7111"
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-14",
+            "phone": "202-366-7111",
+            "primaryITInvestmentUII": "021-325711125",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "rights": "This dataset contains controlled unclassified information (Information technology systems security information)",
+            "temporal": "R/2014-11-21/P1Y",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "DOT Automated Enterprise Continuous Monitoring Program -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/tw8w-mfxe",
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
+            "description": "The Southeast Michigan Operational Data Environment (SEMI-ODE) is a real-time data acquisition and distribution software system that processes vehicle and infrastructure data collected from sources such as the Southeast Michigan testbed Situational Data Clearinghouse (SDC) and the Situational Data Warehouse (SDW), along with other non-connected vehicle sources of data. The ODE offers four core functions to supply tailored and custom-requested data from the SEMI Testbed to subscribing client software applications. The core functions are: 1) Valuation (V), 2) Integration (I), 3) Sanitization (S) (also called de-identification), and 4) Aggregation (A). These four VISA functions are critical to the field test as they enable the subscribing emulated applications to receive data tailored to support their operation. These functions also serve to increase the general usability of the data being generated in the SEMI Test Bed.\r\n\r\nThis legacy dataset was created before data.transportation.gov and is only currently available via the attached file(s). Please contact the dataset owner if there is a need for users to work with this data using the data.transportation.gov analysis features (online viewing, API, graphing, etc.) and the USDOT will consider modifying the dataset to fully integrate in data.transportation.gov.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/download/tw8w-mfxe/application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/tw8w-mfxe",
             "issued": "2016-06-30",
-            "@type": "dcat:Dataset",
-            "temporal": "2016-04-05/2016-04-07",
-            "modified": "2016-06-30",
             "keyword": [
                 "intelligent transportation systems (its)",
                 "its joint program office (jpo)",
@@ -90790,57 +90802,35 @@
                 "southeast michigan operational data environment (semi-ode)",
                 "southeast michigan test bed"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/tw8w-mfxe",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://creativecommons.org/licenses/by-nc-sa/3.0/legalcode",
+            "modified": "2016-06-30",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Department of Transportation"
             },
-            "identifier": "https://data.transportation.gov/api/views/tw8w-mfxe",
-            "description": "The Southeast Michigan Operational Data Environment (SEMI-ODE) is a real-time data acquisition and distribution software system that processes vehicle and infrastructure data collected from sources such as the Southeast Michigan testbed Situational Data Clearinghouse (SDC) and the Situational Data Warehouse (SDW), along with other non-connected vehicle sources of data. The ODE offers four core functions to supply tailored and custom-requested data from the SEMI Testbed to subscribing client software applications. The core functions are: 1) Valuation (V), 2) Integration (I), 3) Sanitization (S) (also called de-identification), and 4) Aggregation (A). These four VISA functions are critical to the field test as they enable the subscribing emulated applications to receive data tailored to support their operation. These functions also serve to increase the general usability of the data being generated in the SEMI Test Bed.\r\n\r\nThis legacy dataset was created before data.transportation.gov and is only currently available via the attached file(s). Please contact the dataset owner if there is a need for users to work with this data using the data.transportation.gov analysis features (online viewing, API, graphing, etc.) and the USDOT will consider modifying the dataset to fully integrate in data.transportation.gov.",
-            "title": "Southeast Michigan Operational Data Environment (SEMI-ODE)",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/download/tw8w-mfxe/application/vnd.openxmlformats-officedocument.wordprocessingml.document",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
-                }
-            ],
             "spatial": "Michigan",
-            "dataQuality": true,
-            "license": "http://creativecommons.org/licenses/by-nc-sa/3.0/legalcode",
-            "accrualPeriodicity": "irregular",
+            "temporal": "2016-04-05/2016-04-07",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Southeast Michigan Operational Data Environment (SEMI-ODE)"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/txg8-88wq",
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
-            "identifier": "https://data.transportation.gov/api/views/txg8-88wq",
             "description": "",
-            "title": "Legacy to New Site Crosswalk",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -90848,68 +90838,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/txg8-88wq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/txg8-88wq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/txg8-88wq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/txg8-88wq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/txg8-88wq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/txg8-88wq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/txg8-88wq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/txg8-88wq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/txg8-88wq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/txg8-88wq",
+            "issued": "2023-08-08",
+            "landingPage": "https://data.transportation.gov/d/txg8-88wq",
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
+            "title": "Legacy to New Site Crosswalk"
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
-            "landingPage": "https://data.transportation.gov/d/tykx-wpab",
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
-            "identifier": "692.34",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - Carbon Monoxide",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "primaryITInvestmentUII": "021-845083703",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -90918,79 +90899,76 @@
                     "title": "Carbon Monoxide"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.34",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/tykx-wpab",
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
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - Carbon Monoxide"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/tzde-v676",
-            "issued": "2021-04-09",
             "@type": "dcat:Dataset",
-            "modified": "2021-04-09",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sean Jahanmir",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/tzde-v676",
+            "issued": "2021-04-09",
+            "landingPage": "https://data.transportation.gov/d/tzde-v676",
+            "modified": "2021-04-09",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Motor Vehicle Fuel Prices"
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
-            "landingPage": "https://data.transportation.gov/d/tzxw-4fe6",
-            "issued": "1981-01-21",
-            "temporal": "1981-01-21/2015",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.nhtsa.gov/Research/Databases+and+Software/NHTSA+Test+Reference+Guides"
-            ],
-            "keyword": [
-                "biomechanics",
-                "crash",
-                "database",
-                "dummy",
-                "occupant",
-                "restraint",
-                "test"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "DOT-1841",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/bio/schema.htm",
             "description": "The NHTSA Biomechanics Test Database is a repository of experimental data used by NHTSA for developing Anthropomophic Test Devices and associated Injury Criteria. The data is disseminated via this website for use by academia, the automotive industry, and the public to improve the safety of automobiles and reduce death and injuries on our nations highway. Because of the nature of the testing, the applicability of the data extends far beyond auto safety, and may be useful for those in the sports medicine, space travel, aircraft, military or any activity where the human body is exposed impact.",
-            "title": "Biomechanics Test Database",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research",
-            "primaryITInvestmentUII": "021-961265599",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -90999,48 +90977,53 @@
                     "title": "Zipped ASCII Export"
                 }
             ],
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/bio/schema.htm",
-            "dataQuality": false,
+            "identifier": "DOT-1841",
+            "issued": "1981-01-21",
+            "keyword": [
+                "biomechanics",
+                "crash",
+                "database",
+                "dummy",
+                "occupant",
+                "restraint",
+                "test"
+            ],
+            "landingPage": "https://data.transportation.gov/d/tzxw-4fe6",
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
+            "temporal": "1981-01-21/2015",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4712",
-            "language": [
-                "en-US"
-            ]
+            "title": "Biomechanics Test Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/u2pk-kyws",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-11-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-15",
-            "keyword": [
-                "aff",
-                "general aviation"
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
-            "identifier": "https://data.transportation.gov/api/views/u2pk-kyws",
             "description": "",
-            "title": "AFF - GA Inventory",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91048,64 +91031,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/u2pk-kyws/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/u2pk-kyws/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/u2pk-kyws/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/u2pk-kyws/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/u2pk-kyws/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/u2pk-kyws/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/u2pk-kyws/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/u2pk-kyws/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/u2pk-kyws/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/u2pk-kyws",
+            "issued": "2024-11-15",
+            "keyword": [
+                "aff",
+                "general aviation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/u2pk-kyws",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-15",
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
+            "title": "AFF - GA Inventory"
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
-            "identifier": "https://data.transportation.gov/api/views/u397-4rr7",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 1988",
-            "title": "Historic HPMS Data (Sample) - 1988",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91113,98 +91093,102 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/u397-4rr7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/u397-4rr7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/u397-4rr7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/u397-4rr7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/u397-4rr7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/u397-4rr7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/u397-4rr7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/u397-4rr7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/u397-4rr7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/u397-4rr7",
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
+            "title": "Historic HPMS Data (Sample) - 1988"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/u3e6-df3v",
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
-            "identifier": "https://data.transportation.gov/api/views/u3e6-df3v",
             "description": "The Bureau of Transportation Statistics releases seasonally adjusted air traffic data based on monthly reports from commercial U.S. air carriers.",
-            "title": "Air Travel - Domestic - Seasonally Adjusted",
+            "identifier": "https://data.transportation.gov/api/views/u3e6-df3v",
+            "issued": "2025-01-16",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/u3e6-df3v",
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
+            "title": "Air Travel - Domestic - Seasonally Adjusted"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://data.transportation.gov/d/u3uh-j5wt",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-02-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-02-01",
-            "keyword": [
-                "pocket guide to transportation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Zereyakob Mekonnen",
                 "hasEmail": "mailto:z.mekonnen.ctr@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/u3uh-j5wt",
             "description": "",
-            "title": "Pocket Guide to Transportation-Transportation Vehicles",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91212,40 +91196,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/u3uh-j5wt/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/u3uh-j5wt/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/u3uh-j5wt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/u3uh-j5wt/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/u3uh-j5wt/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/u3uh-j5wt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/u3uh-j5wt/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/u3uh-j5wt/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/u3uh-j5wt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "https://data.transportation.gov/api/views/u3uh-j5wt",
+            "issued": "2024-02-01",
+            "keyword": [
+                "pocket guide to transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/u3uh-j5wt",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-02-01",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Pocket Guide to Transportation-Transportation Vehicles"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/u3vp-3g5x",
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
+                    "description": "2011 Vermont HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/vermont2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Vermont"
+                }
+            ],
+            "identifier": "678.47",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -91259,55 +91277,41 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.47",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Vermont",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/u3vp-3g5x",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-5035",
             "primaryITInvestmentUII": "021-099281808",
             "programCode": [
-                "021:009"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/vermont2011.zip",
-                    "description": "2011 Vermont HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Vermont"
-                }
+                "021:009"
             ],
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Vermont"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/u3wt-eyhe",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Overview of Household Spending on Transportation by Income Quintile. Household spending on transportation and transportation spending as a percent of after tax income over time.",
+            "identifier": "https://data.transportation.gov/api/views/u3wt-eyhe",
             "issued": "2023-09-12",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
             "keyword": [
                 "income quintile characteristics",
                 "number of vehicles",
@@ -91322,54 +91326,34 @@
                 "vehicle miles traveled",
                 "vehicle trips"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/u3wt-eyhe",
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
-            "identifier": "https://data.transportation.gov/api/views/u3wt-eyhe",
-            "description": "Overview of Household Spending on Transportation by Income Quintile. Household spending on transportation and transportation spending as a percent of after tax income over time.",
-            "title": "Transportation Cost Burden: Overview of Household Spending on Transportation by Income Quintile",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Transportation Cost Burden: Overview of Household Spending on Transportation by Income Quintile"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/u4i8-4m26",
             "bureauCode": [
                 "021:17"
             ],
-            "issued": "2023-12-08",
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
-            "identifier": "https://data.transportation.gov/api/views/u4i8-4m26",
             "description": "Records for all carriers/brokers/freight forwarders with active, inactive, or pending authorities (common or contract).  It includes the DOT number and MC/FF/MX number for the carrier/broker/freight forwarder, along with company census data (e.g., types of authority, address, types of insurance on file, and amounts of insurance on file).  See dataset attachment \"FMCSA Dataset Description and Data Definitions - Select Datasets\" for more information.",
-            "title": "Carrier - All With History",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91377,50 +91361,47 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/u4i8-4m26",
+            "issued": "2023-12-08",
+            "keyword": [
+                "motor carrier",
+                "operating authority",
+                "broker",
+                "insurance"
+            ],
+            "landingPage": "https://data.transportation.gov/d/u4i8-4m26",
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
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://hepgis.fhwa.dot.gov/hepgismaps11/#",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/u4tz-837w",
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
-            "identifier": "692.7",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - National Network Conventional Combination Trucks",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "primaryITInvestmentUII": "021-845083703",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91429,79 +91410,79 @@
                     "title": "National Network Conventional Combination Trucks"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.7",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/u4tz-837w",
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
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - National Network Conventional Combination Trucks"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/u4v9-pch5",
-            "issued": "2020-08-13",
             "@type": "dcat:Dataset",
-            "modified": "2021-04-09",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/u4v9-pch5",
+            "issued": "2020-08-13",
+            "landingPage": "https://data.transportation.gov/d/u4v9-pch5",
+            "modified": "2021-04-09",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
-            "title": "2018-2019 Urban Summaries Data",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "2018-2019 Urban Summaries Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/Ped/",
+            "agencyProgramURL": "https://www.nhtsa.gov/research-data/national-automotive-sampling-system-nass",
+            "analysisUnit": "Motor vehicle vs Pedestrian crash",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/u6ip-pqkc",
-            "issued": "1999-09-17",
-            "temporal": "1994-06-01/1998-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/Ped/"
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
-            "identifier": "DOT-289",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "The Pedestrian Crash Data Study (PCDS) collected detailed data on motor vehicle vs pedestrian crashes.",
-            "title": "The Pedestrian Crash Data Study (PCDS)",
-            "agencyProgramURL": "https://www.nhtsa.gov/research-data/national-automotive-sampling-system-nass",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91510,48 +91491,52 @@
                     "title": "SAS File"
                 }
             ],
-            "spatial": "United States",
-            "dataQuality": true,
+            "identifier": "DOT-289",
+            "issued": "1999-09-17",
+            "keyword": [
+                "crash",
+                "injury",
+                "motor vehicle",
+                "pedestrian",
+                "vehicle"
+            ],
+            "landingPage": "https://data.transportation.gov/d/u6ip-pqkc",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/Ped/",
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
+                "https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/Ped/"
+            ],
+            "spatial": "United States",
+            "temporal": "1994-06-01/1998-12-31",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "analysisUnit": "Motor vehicle vs Pedestrian crash",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4998",
-            "language": [
-                "en-US"
-            ]
+            "title": "The Pedestrian Crash Data Study (PCDS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/u7gh-36sf",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2020-12-07",
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
-            "identifier": "https://data.transportation.gov/api/views/u7gh-36sf",
+            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
             "description": "State DOT will provide VMT. This data is summarized by Paved and Unpaved and by Vehicle Type.",
-            "title": "National Summaries 2018",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91559,83 +91544,112 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/u7gh-36sf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/u7gh-36sf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/u7gh-36sf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/u7gh-36sf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/u7gh-36sf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/u7gh-36sf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/u7gh-36sf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/u7gh-36sf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/u7gh-36sf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "USA",
-            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
+            "identifier": "https://data.transportation.gov/api/views/u7gh-36sf",
+            "issued": "2020-12-07",
+            "landingPage": "https://data.transportation.gov/d/u7gh-36sf",
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
+            "title": "National Summaries 2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/u8i5-iu8e",
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
                 "hasEmail": "mailto:answers@bts.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/u8i5-iu8e",
             "description": "Freight and mail carried by U.S. airlines in all service classes (schedule and nonscheduled) on domestic flights. The Bureau of Transportation Statistics collects air traffic data from U.S. air carriers and international carriers operating within the U.S.",
-            "title": "Air Cargo - Domestic",
+            "identifier": "https://data.transportation.gov/api/views/u8i5-iu8e",
+            "issued": "2025-01-15",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/u8i5-iu8e",
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
+            "title": "Air Cargo - Domestic"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
+            "agencyDataSeriesURL": "https://ai.fmcsa.dot.gov/CrashProfile/CrashProfileMainNew.asp",
+            "agencyProgramURL": "http://ai.fmcsa.dot.gov/CrashProfile/CrashProfileMainNew.asp",
+            "analysisUnit": "Crash, Motor Carrier, State",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/u8pg-fvnj",
-            "issued": "2018-12-17",
-            "temporal": "R/2005-03-01/P3M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://ai.fmcsa.dot.gov/CrashProfile/CrashProfileMainNew.asp"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Crash Statistics are summarized crash statistics for large trucks and buses involved in fatal and non-fatal Crashes that occurred in the United States. These statistics are derived from two sources:  the Fatality Analysis Reporting System (FARS) and the Motor Carrier Management Information System (MCMIS). Crash Statistics contain information that can be used to identify safety problems in specific geographical areas or to compare state statistics to the national crash figures.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://ai.fmcsa.dot.gov/CrashProfile/statecrashprofilemain.asp",
+                    "mediaType": "text/html",
+                    "title": "State Profiles"
+                }
             ],
+            "identifier": "DOT-112",
+            "issued": "2018-12-17",
             "keyword": [
                 "bus",
                 "crash",
@@ -91652,83 +91666,50 @@
                 "motorcoach",
                 "towaway"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "DOT-112",
+            "landingPage": "https://data.transportation.gov/d/u8pg-fvnj",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-24",
+            "phone": "202-366-2161",
+            "programCode": [
+                "021:022"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Motor Carrier Safety Administration"
             },
-            "description": "Crash Statistics are summarized crash statistics for large trucks and buses involved in fatal and non-fatal Crashes that occurred in the United States. These statistics are derived from two sources:  the Fatality Analysis Reporting System (FARS) and the Motor Carrier Management Information System (MCMIS). Crash Statistics contain information that can be used to identify safety problems in specific geographical areas or to compare state statistics to the national crash figures.",
-            "title": "A&I - Crash Statistics",
-            "agencyProgramURL": "http://ai.fmcsa.dot.gov/CrashProfile/CrashProfileMainNew.asp",
-            "programCode": [
-                "021:022"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://ai.fmcsa.dot.gov/CrashProfile/statecrashprofilemain.asp",
-                    "mediaType": "text/html",
-                    "title": "State Profiles"
-                }
+            "references": [
+                "http://ai.fmcsa.dot.gov/CrashProfile/CrashProfileMainNew.asp"
             ],
             "spatial": "National, State, County",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "https://ai.fmcsa.dot.gov/CrashProfile/CrashProfileMainNew.asp",
+            "temporal": "R/2005-03-01/P3M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P3M",
-            "analysisUnit": "Crash, Motor Carrier, State",
-            "categoryDesignation": "Research",
-            "phone": "202-366-2161",
-            "language": [
-                "en-US"
-            ]
+            "title": "A&I - Crash Statistics"
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
-            "landingPage": "https://data.transportation.gov/d/uack-gist",
-            "issued": "1992-12-31",
-            "temporal": "R/1992-12-31/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "National Bridge Inventory Database System.",
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
-            "identifier": "DOT-693",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
             "description": "The NBI System is the collection of bridge inspection information and costs associated with bridge replacements of structurally deficient bridges on and off the NHS. This data is collected under the auspices of the National Bridge Inspection Standards (NBIS) as prescribed by law. The NBI System collects the information that is used to determine eligibility for NHS projects, performance measure reporting, NHS penalty determination, and reporting to Congress.  It supports oversight of the NBIS through various report tools, and provides data reporting that supports agency strategic goals.",
-            "title": "National Bridge Inventory System (NBI)",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
-            "primaryITInvestmentUII": "021-012940226",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91737,50 +91718,53 @@
                     "title": "1992"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
-            "dataQuality": true,
+            "identifier": "DOT-693",
+            "issued": "1992-12-31",
+            "keyword": [
+                "bridge",
+                "condition",
+                "deck",
+                "inspection",
+                "structure"
+            ],
+            "landingPage": "https://data.transportation.gov/d/uack-gist",
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
+            "title": "National Bridge Inventory System (NBI)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ub6a-sqr5",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-10-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-01",
-            "keyword": [
-                "commodity",
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
-            "identifier": "https://data.transportation.gov/api/views/ub6a-sqr5",
             "description": "Source: U.S. Department of Transportation, Bureau of Transportation Statistics, based upon U.S. Department of Commerce, U.S. Census Bureau, Foreign Trade Division, USA Trade Online, \"HS Port-level Data\", available at https://usatrade.census.gov/ as of Sept 2024.",
-            "title": "Value of Containerized Imports by Coast in 2023",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91788,47 +91772,79 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ub6a-sqr5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ub6a-sqr5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ub6a-sqr5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ub6a-sqr5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ub6a-sqr5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ub6a-sqr5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ub6a-sqr5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ub6a-sqr5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ub6a-sqr5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/ub6a-sqr5",
+            "issued": "2024-10-01",
+            "keyword": [
+                "commodity",
+                "ports"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ub6a-sqr5",
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
+            "title": "Value of Containerized Imports by Coast in 2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/PT1S",
+            "agencyProgramURL": "https://resourcecenter.911.gov/code/home.aspx",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/ubde-kzjs",
-            "issued": "2018-12-18",
-            "temporal": "R/2013/PT1S",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": false,
+            "description": "Collect and aggregate information from state level reporting entities that can be used to measure the progress of 9 1-1 authorities across the country in enhancing their existing operations and migrating to more advanced - Internet-Protocol-enabled emergency networks. The data will be maintained in a \"National 9-1-1 Profile Database.\" One of the objectives of the National 9-1-1 Program is to develop, collect, and disseminate information concerning practices, procedures, and technology used in the implementation of E9 1 1 services and to support 9-1-1 Public Safety Answering Points (PSAPs) and related state and local public safety agencies for 9 1 1 deployment and operations. The National 9-1-1 profile database can be used to follow the progress of 9-1-1 authorities in enhancing their existing systems and implementing next-generation networks for more advanced systems.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://resourcecenter.911.gov/code/9-1-1ProfileDatabase.aspx",
+                    "mediaType": "text/html",
+                    "title": "National 9-1-1 Profile Database"
+                }
+            ],
+            "identifier": "416.2",
+            "isPartOf": "DOT-416",
+            "issued": "2018-12-18",
             "keyword": [
                 "911",
                 "9-11",
@@ -91838,82 +91854,45 @@
                 "public safety answering points",
                 "resource center"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "416.2",
+            "landingPage": "https://data.transportation.gov/d/ubde-kzjs",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-01",
+            "phone": "202-366-2705",
+            "programCode": [
+                "021:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Highway Traffic Safety Administration"
             },
-            "description": "Collect and aggregate information from state level reporting entities that can be used to measure the progress of 9 1-1 authorities across the country in enhancing their existing operations and migrating to more advanced - Internet-Protocol-enabled emergency networks. The data will be maintained in a \"National 9-1-1 Profile Database.\" One of the objectives of the National 9-1-1 Program is to develop, collect, and disseminate information concerning practices, procedures, and technology used in the implementation of E9 1 1 services and to support 9-1-1 Public Safety Answering Points (PSAPs) and related state and local public safety agencies for 9 1 1 deployment and operations. The National 9-1-1 profile database can be used to follow the progress of 9-1-1 authorities in enhancing their existing systems and implementing next-generation networks for more advanced systems.",
-            "title": "National 9-1-1 Profile Database - National 9-1-1 Profile Database",
-            "isPartOf": "DOT-416",
-            "agencyProgramURL": "https://resourcecenter.911.gov/code/home.aspx",
-            "programCode": [
-                "021:031"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://resourcecenter.911.gov/code/9-1-1ProfileDatabase.aspx",
-                    "mediaType": "text/html",
-                    "title": "National 9-1-1 Profile Database"
-                }
-            ],
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "temporal": "R/2013/PT1S",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/PT1S",
-            "categoryDesignation": "Research",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-2705"
+            "title": "National 9-1-1 Profile Database - National 9-1-1 Profile Database"
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
-            "landingPage": "https://data.transportation.gov/d/ubt8-8i5i",
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
-            "identifier": "DOT-1840",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/veh/vehdb-export-fields.htm",
             "description": "The NHTSA Vehicle Crash Test Database contains engineering data measured during various types of research, the New Car Assessment Program (NCAP), and compliance crash tests. Information in this database refers to the performance and response of vehicles and other structures in impacts. This database is not intended to support general consumer safety issues. For general consumer information please see the NHTSA's information on buying a safer car.",
-            "title": "Vehicle Crash Test Database",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research",
-            "primaryITInvestmentUII": "021-961265599",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91922,57 +91901,57 @@
                     "title": "Browse the latest tests"
                 }
             ],
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/veh/vehdb-export-fields.htm",
-            "dataQuality": true,
+            "identifier": "DOT-1840",
+            "issued": "1981-12-31",
+            "keyword": [
+                "compliance",
+                "crash",
+                "database",
+                "ncap",
+                "test",
+                "vehicle"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ubt8-8i5i",
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
+            "title": "Vehicle Crash Test Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/PT1S",
+            "agencyProgramURL": "https://resourcecenter.911.gov/code/home.aspx",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/uc84-ygpm",
-            "issued": "2018-12-18",
-            "temporal": "R/2013/PT1S",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "911",
-                "9-11",
-                "9-1-1",
-                "information clearinghouse",
-                "psap",
-                "public safety answering points",
-                "resource center"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "416.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
             "description": "Collect and aggregate information from state level reporting entities that can be used to measure the progress of 9 1-1 authorities across the country in enhancing their existing operations and migrating to more advanced - Internet-Protocol-enabled emergency networks. The data will be maintained in a \"National 9-1-1 Profile Database.\" One of the objectives of the National 9-1-1 Program is to develop, collect, and disseminate information concerning practices, procedures, and technology used in the implementation of E9 1 1 services and to support 9-1-1 Public Safety Answering Points (PSAPs) and related state and local public safety agencies for 9 1 1 deployment and operations. The National 9-1-1 profile database can be used to follow the progress of 9-1-1 authorities in enhancing their existing systems and implementing next-generation networks for more advanced systems.",
-            "title": "National 9-1-1 Profile Database - National 9-1-1 Profile Database",
-            "isPartOf": "DOT-416",
-            "agencyProgramURL": "https://resourcecenter.911.gov/code/home.aspx",
-            "programCode": [
-                "021:031"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -91981,51 +91960,87 @@
                     "title": "National 9-1-1 Profile Database"
                 }
             ],
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "416.1",
+            "isPartOf": "DOT-416",
+            "issued": "2018-12-18",
+            "keyword": [
+                "911",
+                "9-11",
+                "9-1-1",
+                "information clearinghouse",
+                "psap",
+                "public safety answering points",
+                "resource center"
             ],
-            "accrualPeriodicity": "R/PT1S",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/uc84-ygpm",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-2705"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-01",
+            "phone": "202-366-2705",
+            "programCode": [
+                "021:031"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "temporal": "R/2013/PT1S",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "National 9-1-1 Profile Database - National 9-1-1 Profile Database"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ucnj-kcz7",
-            "issued": "2024-08-09",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-09",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DiJoseph, Patricia (OST)",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/ucnj-kcz7",
+            "issued": "2024-08-09",
+            "landingPage": "https://data.transportation.gov/d/ucnj-kcz7",
+            "modified": "2024-08-09",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Cruise Ship Calls and Passenger Counts"
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
-            "landingPage": "https://data.transportation.gov/d/udp8-pk9g",
-            "issued": "2011-10-07",
-            "temporal": "R/2002-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-05",
+            "categoryDesignation": "Research",
             "collectionInstrument": "web-based reporting system",
-            "references": [
-                "http://www.ntdprogram.gov/ntdprogram/pubs/MonthlyRidership/2012/ridership.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John D. Giorgis",
+                "hasEmail": "mailto:john.giorgis@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www.ntdprogram.gov/ntdprogram/Glossary.htm",
+            "description": "Data collected monthly from urbanized area transit systems. The Monthly module includes a limited set of key indicators reported by transit properties. Data is reported on a monthly basis, by mode and type of service, for a calendar year. The four data items included are: Unlinked Passenger Trips, Vehicle Revenue Miles, Vehicle Revenue Hours, and Vehicles Operated in Maximum Service (Peak Vehicles). Monthly data are reported by mode and type of service.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://go.usa.gov/kfQP",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Raw Data Release"
+                }
             ],
+            "identifier": "DOT-19",
+            "issued": "2011-10-07",
             "keyword": [
                 "boardings",
                 "bus",
@@ -92035,82 +92050,49 @@
                 "train",
                 "transit"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John D. Giorgis",
-                "hasEmail": "mailto:john.giorgis@dot.gov"
-            },
-            "identifier": "DOT-19",
+            "landingPage": "https://data.transportation.gov/d/udp8-pk9g",
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
-            "description": "Data collected monthly from urbanized area transit systems. The Monthly module includes a limited set of key indicators reported by transit properties. Data is reported on a monthly basis, by mode and type of service, for a calendar year. The four data items included are: Unlinked Passenger Trips, Vehicle Revenue Miles, Vehicle Revenue Hours, and Vehicles Operated in Maximum Service (Peak Vehicles). Monthly data are reported by mode and type of service.",
-            "title": "NTD Monthly Module Data Set",
-            "agencyProgramURL": "http://www.ntdprogram.gov; http://www.ntdprogram.gov/ntdprogram/data.htm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://go.usa.gov/kfQP",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "Raw Data Release"
-                }
+            "references": [
+                "http://www.ntdprogram.gov/ntdprogram/pubs/MonthlyRidership/2012/ridership.pdf"
             ],
             "spatial": "Urbanized Area",
-            "describedBy": "http://www.ntdprogram.gov/ntdprogram/Glossary.htm",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.ntdprogram.gov/ntdprogram/data.htm",
+            "temporal": "R/2002-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Research",
-            "analysisUnit": "various",
-            "phone": "202-366-5430",
-            "language": [
-                "en-US"
-            ]
+            "title": "NTD Monthly Module Data Set"
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
-            "landingPage": "https://data.transportation.gov/d/udv7-ayxf",
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
-            "identifier": "364.12",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database - Biomechanics Test Database Interactive Access",
-            "isPartOf": "DOT-364",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
-            "primaryITInvestmentUII": "021-621341357",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -92119,53 +92101,52 @@
                     "title": "Biomechanics Test Database Interactive Access"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.12",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/udv7-ayxf",
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
+            "title": "Vehicle Safety Research and Development Database - Biomechanics Test Database Interactive Access"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/udzf-9fvh",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2017-08-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-05",
-            "keyword": [
-                "aviation",
-                "international departures",
-                "international freight",
-                "international passengers",
-                "international seats",
-                "office of aviation analysis"
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
-            "identifier": "https://data.transportation.gov/api/views/udzf-9fvh",
+            "dataQuality": true,
             "description": "The main, combined file that is used for the 4 Views for each type: Departures, Freight, Seats, and Passengers.  This combined dataset will not be published, but the 4 views will be published separately.",
-            "title": "International_Passengers_Freight_ All_Types",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -92173,43 +92154,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/udzf-9fvh/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/udzf-9fvh/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/udzf-9fvh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/udzf-9fvh/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/udzf-9fvh/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/udzf-9fvh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/udzf-9fvh/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/udzf-9fvh/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/udzf-9fvh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/udzf-9fvh",
+            "issued": "2017-08-29",
+            "keyword": [
+                "aviation",
+                "international departures",
+                "international freight",
+                "international passengers",
+                "international seats",
+                "office of aviation analysis"
+            ],
+            "landingPage": "https://data.transportation.gov/d/udzf-9fvh",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2024-11-05",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
             "theme": [
                 "Aviation"
-            ]
+            ],
+            "title": "International_Passengers_Freight_ All_Types"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ueau-ishk",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRA Safety Data Team",
+                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This is the page for Accident Cause (including Highway-Rail Crossings) (3.10).",
+            "identifier": "https://data.transportation.gov/api/views/ueau-ishk",
             "issued": "2024-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "collision",
                 "derailment",
@@ -92217,68 +92222,43 @@
                 "train",
                 "train accident"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRA Safety Data Team",
-                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/ueau-ishk",
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
-            "identifier": "https://data.transportation.gov/api/views/ueau-ishk",
-            "description": "This is the page for Accident Cause (including Highway-Rail Crossings) (3.10).",
-            "title": "Accident Cause (including Highway-Rail Crossings) (3.10)",
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
+            "title": "Accident Cause (including Highway-Rail Crossings) (3.10)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www.rita.dot.gov/freedom_of_information_act/",
+            "agencyProgramURL": "http://www.rita.dot.gov/freedom_of_information_act/",
+            "analysisUnit": "Company",
             "bureauCode": [
                 "021:53"
             ],
-            "landingPage": "https://data.transportation.gov/d/ueb3-8zmf",
-            "issued": "2011-01-18",
-            "temporal": "2007-01-01/2011-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.rita.dot.gov/freedom_of_information_act/"
-            ],
-            "keyword": [
-                "administrative law",
-                "data.gov",
-                "foia",
-                "law",
-                "transportation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "330.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Research and Innovative Technology Administration"
-            },
+            "dataQuality": true,
             "description": "FOIA Electronic Reading Room - Final Opinions/Orders in Adjudicated Cases",
-            "title": "Administrative Law Judge Opinions issued by the Research and Innovative Technology Administration -",
-            "isPartOf": "DOT-330",
-            "agencyProgramURL": "http://www.rita.dot.gov/freedom_of_information_act/",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -92286,31 +92266,67 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "330.2",
+            "isPartOf": "DOT-330",
+            "issued": "2011-01-18",
+            "keyword": [
+                "administrative law",
+                "data.gov",
+                "foia",
+                "law",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ueb3-8zmf",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.rita.dot.gov/freedom_of_information_act/",
+            "modified": "2024-11-14",
+            "phone": "202-366-4308",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Research and Innovative Technology Administration"
+            },
+            "references": [
+                "http://www.rita.dot.gov/freedom_of_information_act/"
+            ],
+            "temporal": "2007-01-01/2011-01-18",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "analysisUnit": "Company",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4308",
-            "language": [
-                "en-US"
-            ]
+            "title": "Administrative Law Judge Opinions issued by the Research and Innovative Technology Administration -"
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
-            "landingPage": "https://data.transportation.gov/d/ufbb-q3u3",
-            "issued": "2014-12-29",
-            "temporal": "2014-12-29/2014-12-29",
-            "@type": "dcat:Dataset",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "A compilation of historic documents and articles on the Interstate System, Federal-Aid Highway Program, FHWA, and transportation.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fhwa.dot.gov/infrastructure/history.cfm",
+                    "mediaType": "text/html",
+                    "title": "Highway History"
+                }
+            ],
+            "identifier": "696.2",
+            "isPartOf": "DOT-696",
+            "issued": "2014-12-29",
             "keyword": [
                 "articles",
                 "documents",
@@ -92318,58 +92334,59 @@
                 "history",
                 "legislation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "696.2",
+            "landingPage": "https://data.transportation.gov/d/ufbb-q3u3",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-4856",
+            "programCode": [
+                "021:011"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "A compilation of historic documents and articles on the Interstate System, Federal-Aid Highway Program, FHWA, and transportation.",
-            "title": "Highway History - Highway History",
-            "isPartOf": "DOT-696",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/infrastructure/history.cfm",
-            "programCode": [
-                "021:011"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/infrastructure/history.cfm",
-                    "mediaType": "text/html",
-                    "title": "Highway History"
-                }
-            ],
             "spatial": "National",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "temporal": "2014-12-29/2014-12-29",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/infrastructure/history.cfm",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-4856"
+            "title": "Highway History - Highway History"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.locationaffordability.info/lai.aspx%3Furl=download.php",
+            "agencyProgramURL": "http://www.locationaffordability.info/",
+            "analysisUnit": "Core Based Statistical Area (CBSA)",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/ufww-akxc",
-            "issued": "2013-11-19",
-            "temporal": "2006-01-01/2010-12-31",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
-            "references": [
-                "http://www.locationaffordability.info/downloads/ModelingCode.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://lai.locationaffordability.info/lai_data_dictionary.pdf",
+            "describedByType": "application/pdf",
+            "description": "The Location Affordability Index is an indicator of housing and transportation costs at the neighborhood level.  It gives the percentage of a given family's income estimated to be spent on housing and transportation costs in a given location for eight different household profiles.  It is calculated using actual and modeled data for Census block groups in all 942 Combined Base Statistical Areas, which cover 94% of the U.S. population.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://lai.locationaffordability.info/download_csv.php%3Fstate=us&geography=place",
+                    "mediaType": "text/csv",
+                    "title": "All Census Places"
+                }
             ],
+            "identifier": "337.1",
+            "isPartOf": "DOT-337",
+            "issued": "2013-11-19",
             "keyword": [
                 "access",
                 "affordability",
@@ -92382,59 +92399,60 @@
                 "transit",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "337.1",
+            "landingPage": "https://data.transportation.gov/d/ufww-akxc",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-08",
+            "phone": "800-245-2691",
+            "programCode": [
+                "021:058"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Secretary of Transportation"
             },
-            "description": "The Location Affordability Index is an indicator of housing and transportation costs at the neighborhood level.  It gives the percentage of a given family's income estimated to be spent on housing and transportation costs in a given location for eight different household profiles.  It is calculated using actual and modeled data for Census block groups in all 942 Combined Base Statistical Areas, which cover 94% of the U.S. population.",
-            "title": "Location Affordability Index - All Census Places",
-            "isPartOf": "DOT-337",
-            "agencyProgramURL": "http://www.locationaffordability.info/",
-            "describedByType": "application/pdf",
-            "programCode": [
-                "021:058"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://lai.locationaffordability.info/download_csv.php%3Fstate=us&geography=place",
-                    "mediaType": "text/csv",
-                    "title": "All Census Places"
-                }
+            "references": [
+                "http://www.locationaffordability.info/downloads/ModelingCode.pdf"
             ],
             "spatial": "Core Based Statistical Area (CBSA)",
-            "describedBy": "http://lai.locationaffordability.info/lai_data_dictionary.pdf",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.locationaffordability.info/lai.aspx%3Furl=download.php",
+            "temporal": "2006-01-01/2010-12-31",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Core Based Statistical Area (CBSA)",
-            "phone": "800-245-2691",
-            "language": [
-                "en-US"
-            ]
+            "title": "Location Affordability Index - All Census Places"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/ufyn-xyri",
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
+                    "description": "2012 Maryland HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/maryland2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Maryland"
+                }
+            ],
+            "identifier": "678.74",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -92448,78 +92466,40 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.74",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Maryland",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/ufyn-xyri",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/maryland2012.zip",
-                    "description": "2012 Maryland HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Maryland"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Maryland"
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
-            "identifier": "https://data.transportation.gov/api/views/ug5e-ztkm",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 1992",
-            "title": "Historic HPMS Data (Sample) - 1992",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -92527,47 +92507,85 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ug5e-ztkm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ug5e-ztkm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ug5e-ztkm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ug5e-ztkm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
```

