# Change History for transportation.json (Part 5)

### Changes from 31606f9 to dd2190f (Part 4/9)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
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
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/crc3-3tgf",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/08septvt/08septvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "September 2008"
+                }
             ],
+            "identifier": "18.72",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -39506,60 +39521,60 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.72",
+            "landingPage": "https://data.transportation.gov/d/crc3-3tgf",
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
-            "title": "Monthly Traffic Volume Trends - September 2008",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/08septvt/08septvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "September 2008"
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
+            "title": "Monthly Traffic Volume Trends - September 2008"
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
-            "landingPage": "https://data.transportation.gov/d/crdk-re95",
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
+                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/GES/GES05",
+                    "mediaType": "text/plain",
+                    "title": "2005"
+                }
             ],
+            "identifier": "524.7",
+            "isPartOf": "DOT-524",
+            "issued": "1988-12-31",
             "keyword": [
                 "crashworthiness",
                 "estimation",
@@ -39568,70 +39583,42 @@
                 "nass",
                 "system"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "524.7",
+            "landingPage": "https://data.transportation.gov/d/crdk-re95",
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
-            "title": "GES Reports - 2005",
-            "isPartOf": "DOT-524",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:032"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/GES/GES05",
-                    "mediaType": "text/plain",
-                    "title": "2005"
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
+            "title": "GES Reports - 2005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/crem-w557",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2020-09-21",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Transportation Analysis",
                 "hasEmail": "mailto:ramond.robinson@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/crem-w557",
             "description": "Monthly Transportation Statistics is a compilation of national statistics on transportation. The Bureau of Transportation Statistics brings together the latest data from across the Federal government and transportation industry. Monthly Transportation Statistics contains over 50 time series from nearly two dozen data sources.",
-            "title": "Monthly Transportation Statistics",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39639,71 +39626,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/crem-w557/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/crem-w557/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/crem-w557/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/crem-w557/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/crem-w557/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/crem-w557/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/crem-w557/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/crem-w557/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/crem-w557/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/crem-w557",
+            "issued": "2020-09-21",
+            "landingPage": "https://data.transportation.gov/d/crem-w557",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-31",
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
+            "title": "Monthly Transportation Statistics"
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
-            "landingPage": "https://data.transportation.gov/d/csi5-t9mg",
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
-            "identifier": "693.16",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
             "description": "The NBI System is the collection of bridge inspection information and costs associated with bridge replacements of structurally deficient bridges on and off the NHS. This data is collected under the auspices of the National Bridge Inspection Standards (NBIS) as prescribed by law. The NBI System collects the information that is used to determine eligibility for NHS projects, performance measure reporting, NHS penalty determination, and reporting to Congress.  It supports oversight of the NBIS through various report tools, and provides data reporting that supports agency strategic goals.",
-            "title": "National Bridge Inventory System (NBI) - 2007",
-            "isPartOf": "DOT-693",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
-            "primaryITInvestmentUII": "021-012940226",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39712,59 +39692,59 @@
                     "title": "2007"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
-            "dataQuality": true,
+            "identifier": "693.16",
+            "isPartOf": "DOT-693",
+            "issued": "1992-12-31",
+            "keyword": [
+                "bridge",
+                "condition",
+                "deck",
+                "inspection",
+                "structure"
+            ],
+            "landingPage": "https://data.transportation.gov/d/csi5-t9mg",
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
+            "title": "National Bridge Inventory System (NBI) - 2007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyProgramURL": "http://www.transportation.gov/digitalstrategy",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/ct28-q6ev",
-            "issued": "2015-09-30",
-            "temporal": "2015-09-30/2015-09-30",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-11-14",
-            "references": [
-                "http://www.transportation.gov/digitalstrategy"
-            ],
-            "keyword": [
-                "chief information officer",
-                "fitara",
-                "information technology",
-                "leadership"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "1855.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.transportation.gov/digitalstrategy",
             "description": "A listing of individuals who, besides the Chief Information Officer, have bureau-specific duties or responsibilities as a chief information officer.",
-            "title": "DOT Bureau IT Leadership Directory - Download",
-            "primaryITInvestmentUII": "021-748752384",
-            "agencyProgramURL": "http://www.transportation.gov/digitalstrategy",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39773,30 +39753,68 @@
                     "title": "Download"
                 }
             ],
-            "describedBy": "http://www.transportation.gov/digitalstrategy",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "1855.0",
+            "issued": "2015-09-30",
+            "keyword": [
+                "chief information officer",
+                "fitara",
+                "information technology",
+                "leadership"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Administrative",
+            "landingPage": "https://data.transportation.gov/d/ct28-q6ev",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-9201"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-11-14",
+            "phone": "202-366-9201",
+            "primaryITInvestmentUII": "021-748752384",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "references": [
+                "http://www.transportation.gov/digitalstrategy"
+            ],
+            "temporal": "2015-09-30/2015-09-30",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "DOT Bureau IT Leadership Directory - Download"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/ctbx-3psd",
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
+                    "description": "2011 Illinois HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/illinois2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Illinois"
+                }
+            ],
+            "identifier": "678.15",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -39810,76 +39828,40 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.15",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Illinois",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/ctbx-3psd",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/illinois2011.zip",
-                    "description": "2011 Illinois HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Illinois"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Illinois"
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
-            "identifier": "https://data.transportation.gov/api/views/cu4q-nx8c",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 1986",
-            "title": "Historic HPMS Data (Universe) - 1986",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39887,83 +39869,84 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/cu4q-nx8c/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/cu4q-nx8c/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/cu4q-nx8c/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/cu4q-nx8c/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/cu4q-nx8c/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/cu4q-nx8c/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/cu4q-nx8c/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/cu4q-nx8c/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/cu4q-nx8c/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/cu4q-nx8c",
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
+            "title": "Historic HPMS Data (Universe) - 1986"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/cu77-wjet",
-            "issued": "2021-07-21",
             "@type": "dcat:Dataset",
-            "modified": "2021-07-30",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Todd Solomon",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/cu77-wjet",
+            "issued": "2021-07-21",
+            "landingPage": "https://data.transportation.gov/d/cu77-wjet",
+            "modified": "2021-07-30",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "U.S. Olympic Team Travel to 2021 Tokyo Games"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/cvai-skrf",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2023-02-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-06",
-            "keyword": [
-                "bikeshare",
-                "transportation"
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
-            "identifier": "https://data.transportation.gov/api/views/cvai-skrf",
             "description": "Data from 2019 through 2023. For years after 2023, see: https://data.bts.gov/Research-and-Statistics/Docked-Bikeshare-Ridership/6cfa-ipzd\n\nHistoric data updated on 07/14/2023. Q4 of 2023 and data for all years on systems allowing parking outside of a docking station updated on 06/04/2024.\n\nBikeshare ridership by system, year, and month for bikeshare systems with docking stations.  Data available by month starting in January 2019. Months are rearranged to include the same number of days of the week across years (see below). Data designed to show the impacts of COVID-19 on bikeshare ridership as featured at https://maps.dot.gov/BTS/dockedbikeshare-COVID/\n\nRidership data not available for all docked bikeshare systems. Only docked bikeshare systems with ridership data shown. Some systems included in the data permit users to leave a bicycle outside of a docking station; these trips are indicated by the trip type. Trips defined as rides from point A to B. If user makes trip from B to A on same day, counted as a second trip. Trips labeled as round trips in Metro Bike Share and Indego trip files counted as 2 trips. Trips with no trip time are not counted. For trips starting and ending at a docking station or on systems where only docked trips are permitted, trips with no start station identifier and/or end station id are not counted in totals. Trips shorter than 1 minute or greater than 2 hours excluded. Days aligned to include the same days of weeks in 2019 and 2020. Days included in each month are as follows: \n\nDays included in each month can be found in the attachment (https://data.bts.gov/api/views/6cfa-ipzd/files/36fde1b8-57c3-4d31-b9dc-bbc896ba346e?download=true&filename=days_included_in_docked_bikeshare_monthly_summaries.xlsx)\n\nTrips beginning on 12/31/2019 but ending on 01/01/2020 not included in totals.\n\nData visualizations available at: https://data.bts.gov/stories/s/Summary-of-Docked-Bikeshare-Trips-by-System-and-Ot/7fgy-2zkf/",
-            "title": "Docked Bikeshare Ridership by System, Year, and Month",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39971,42 +39954,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/cvai-skrf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/cvai-skrf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/cvai-skrf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/cvai-skrf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/cvai-skrf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/cvai-skrf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/cvai-skrf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/cvai-skrf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/cvai-skrf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/cvai-skrf",
+            "issued": "2023-02-08",
+            "keyword": [
+                "bikeshare",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/cvai-skrf",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-09-06",
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
+            "title": "Docked Bikeshare Ridership by System, Year, and Month"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/cvki-zubk",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "The Infrastructure Investment and Jobs Act (IIJA) also known as the Bipartisan Infrastructure Law (BIL) contains thousands of line items of transportation infrastructure funds. This report helps detail those line items.",
+            "identifier": "https://data.transportation.gov/api/views/cvki-zubk",
             "issued": "2022-03-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
             "keyword": [
                 "bil",
                 "bipartisan infrastructure law",
@@ -40014,63 +40018,40 @@
                 "iija",
                 "infrastructure investment and jobs act"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/cvki-zubk",
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
-            "identifier": "https://data.transportation.gov/api/views/cvki-zubk",
-            "description": "The Infrastructure Investment and Jobs Act (IIJA) also known as the Bipartisan Infrastructure Law (BIL) contains thousands of line items of transportation infrastructure funds. This report helps detail those line items.",
-            "title": "Infrastructure Investment and Jobs Act (BIL) Transportation Authorizations",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Infrastructure Investment and Jobs Act (BIL) Transportation Authorizations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://mcmis.volpe.dot.gov/mcs150t/pkg_ct_public.prc_ct_public_search",
+            "agencyProgramURL": "http://mcmis.volpe.dot.gov/mcs150t/pkg_ct_public.prc_ct_public_search",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/cvr3-j8yp",
-            "issued": "2010-01-26",
-            "temporal": "R/1974-06-01/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
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
-            "identifier": "DOT-125",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": true,
             "description": "Searchable list of cargo tank manufacturers and repair facilities.",
-            "title": "SAFER - Cargo Tank Facility",
-            "agencyProgramURL": "http://mcmis.volpe.dot.gov/mcs150t/pkg_ct_public.prc_ct_public_search",
-            "programCode": [
-                "021:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40079,34 +40060,69 @@
                     "title": "SAFER - Cargo Tank Facility"
                 }
             ],
-            "spatial": "State, National",
-            "dataQuality": true,
+            "identifier": "DOT-125",
+            "issued": "2010-01-26",
+            "keyword": [
+                "cargo tank",
+                "safer",
+                "tank registration.",
+                "usdot number"
+            ],
+            "landingPage": "https://data.transportation.gov/d/cvr3-j8yp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://mcmis.volpe.dot.gov/mcs150t/pkg_ct_public.prc_ct_public_search",
+            "modified": "2024-05-24",
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
+            "title": "SAFER - Cargo Tank Facility"
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
-            "landingPage": "https://data.transportation.gov/d/cvx2-prbv",
-            "issued": "1992-12-31",
-            "temporal": "R/1992-12-31/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "National Bridge Inventory Database System.",
-            "modified": "2024-05-08",
-            "references": [
-                "http://www.fhwa.dot.gov/bridge/mtguide.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
+            "description": "The NBI System is the collection of bridge inspection information and costs associated with bridge replacements of structurally deficient bridges on and off the NHS. This data is collected under the auspices of the National Bridge Inspection Standards (NBIS) as prescribed by law. The NBI System collects the information that is used to determine eligibility for NHS projects, performance measure reporting, NHS penalty determination, and reporting to Congress.  It supports oversight of the NBIS through various report tools, and provides data reporting that supports agency strategic goals.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fhwa.dot.gov/bridge/nbi/ascii.cfm%3Fyear=2008",
+                    "mediaType": "application/zip",
+                    "title": "2008"
+                }
             ],
+            "identifier": "693.17",
+            "isPartOf": "DOT-693",
+            "issued": "1992-12-31",
             "keyword": [
                 "bridge",
                 "condition",
@@ -40114,83 +40130,49 @@
                 "inspection",
                 "structure"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "693.17",
+            "landingPage": "https://data.transportation.gov/d/cvx2-prbv",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-1575",
+            "primaryITInvestmentUII": "021-012940226",
+            "programCode": [
+                "021:009"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "description": "The NBI System is the collection of bridge inspection information and costs associated with bridge replacements of structurally deficient bridges on and off the NHS. This data is collected under the auspices of the National Bridge Inspection Standards (NBIS) as prescribed by law. The NBI System collects the information that is used to determine eligibility for NHS projects, performance measure reporting, NHS penalty determination, and reporting to Congress.  It supports oversight of the NBIS through various report tools, and provides data reporting that supports agency strategic goals.",
-            "title": "National Bridge Inventory System (NBI) - 2008",
-            "isPartOf": "DOT-693",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
-            "primaryITInvestmentUII": "021-012940226",
-            "programCode": [
-                "021:009"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/bridge/nbi/ascii.cfm%3Fyear=2008",
-                    "mediaType": "application/zip",
-                    "title": "2008"
-                }
+            "references": [
+                "http://www.fhwa.dot.gov/bridge/mtguide.pdf"
             ],
             "spatial": "Point",
-            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/bridge/nbi/ascii.cfm",
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
+            "title": "National Bridge Inventory System (NBI) - 2008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.safercar.gov/Vehicle+Shoppers/Air+Bags/Deactivation+FAQ",
+            "agencyProgramURL": "http://www.safercar.gov/Air+Bags",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/cw7t-jxrv",
-            "issued": "2008-12-31",
-            "temporal": "R/2014/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "595",
-                "air bag",
-                "deactivation",
-                "disability",
-                "modifiers",
-                "waiver"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "1671.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
             "description": "Contain information that identifies, and provides contact information for, businesses modifying vehicles to enable persons with disabilities to operate the vehicle, or ride as a passenger.",
-            "title": "Vehicle Modifications for Persons with Disabilities - Modifier List",
-            "agencyProgramURL": "http://www.safercar.gov/Air+Bags",
-            "programCode": [
-                "021:031"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40199,30 +40181,66 @@
                     "title": "Modifier List"
                 }
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "theme": [
-                "Transportation"
+            "identifier": "1671.0",
+            "issued": "2008-12-31",
+            "keyword": [
+                "595",
+                "air bag",
+                "deactivation",
+                "disability",
+                "modifiers",
+                "waiver"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "agencyDataSeriesURL": "http://www.safercar.gov/Vehicle+Shoppers/Air+Bags/Deactivation+FAQ",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/cw7t-jxrv",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-5302"
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-5302",
+            "programCode": [
+                "021:031"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "temporal": "R/2014/P1Y",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Vehicle Modifications for Persons with Disabilities - Modifier List"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/cwy8-sk2w",
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
+                    "description": "2012 Indiana HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/indiana2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Indiana"
+                }
+            ],
+            "identifier": "678.68",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -40236,94 +40254,91 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.68",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Indiana",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/cwy8-sk2w",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/indiana2012.zip",
-                    "description": "2012 Indiana HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Indiana"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Indiana"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/cxir-yiqt",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Employment in transportation and related occupations",
+            "identifier": "https://data.transportation.gov/api/views/cxir-yiqt",
             "issued": "2020-03-09",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-29",
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
+            "landingPage": "https://data.transportation.gov/d/cxir-yiqt",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-29",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/cxir-yiqt",
-            "description": "Employment in transportation and related occupations",
-            "title": "Transportation Economic Trends: Transportation Employment - Occupation",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Transportation Economic Trends: Transportation Employment - Occupation"
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
-            "landingPage": "https://data.transportation.gov/d/cxj6-gknf",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/09juntvt/09juntvt.xls",
+                    "mediaType": "text/csv",
+                    "title": "June 2009"
+                }
             ],
+            "identifier": "18.33",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -40333,85 +40348,50 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.33",
+            "landingPage": "https://data.transportation.gov/d/cxj6-gknf",
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
-            "title": "Monthly Traffic Volume Trends - June 2009",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/09juntvt/09juntvt.xls",
-                    "mediaType": "text/csv",
-                    "title": "June 2009"
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
+            "title": "Monthly Traffic Volume Trends - June 2009"
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
-            "landingPage": "https://data.transportation.gov/d/cxja-pv4e",
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
-            "identifier": "693.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
             "description": "The NBI System is the collection of bridge inspection information and costs associated with bridge replacements of structurally deficient bridges on and off the NHS. This data is collected under the auspices of the National Bridge Inspection Standards (NBIS) as prescribed by law. The NBI System collects the information that is used to determine eligibility for NHS projects, performance measure reporting, NHS penalty determination, and reporting to Congress.  It supports oversight of the NBIS through various report tools, and provides data reporting that supports agency strategic goals.",
-            "title": "National Bridge Inventory System (NBI) - 1993",
-            "isPartOf": "DOT-693",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
-            "primaryITInvestmentUII": "021-012940226",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40420,61 +40400,53 @@
                     "title": "1993"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
-            "dataQuality": true,
+            "identifier": "693.2",
+            "isPartOf": "DOT-693",
+            "issued": "1992-12-31",
+            "keyword": [
+                "bridge",
+                "condition",
+                "deck",
+                "inspection",
+                "structure"
+            ],
+            "landingPage": "https://data.transportation.gov/d/cxja-pv4e",
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
+            "title": "National Bridge Inventory System (NBI) - 1993"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/czer-epuy",
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
-            "identifier": "https://data.transportation.gov/api/views/czer-epuy",
             "description": "Part of Wyoming Department of Transportation Connected Vehicle Pilot Phase 4. Verify that OBUs use different LTE-V2X Configuration Profiles based on the vehicle's speed.\nHost and remote vehicles travelling below 120 kmph\nHost and remote vehicles travelling above 120 kmph",
-            "title": "LTE-V2X Wyoming Connected Vehicle Pilot test ID WV2IMCT-1 Vehicle 2 70 mph",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40482,42 +40454,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/czer-epuy/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/czer-epuy/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/czer-epuy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/czer-epuy/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/czer-epuy/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/czer-epuy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/czer-epuy/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/czer-epuy/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/czer-epuy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Wyoming",
+            "identifier": "https://data.transportation.gov/api/views/czer-epuy",
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
+            "landingPage": "https://data.transportation.gov/d/czer-epuy",
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
+            "title": "LTE-V2X Wyoming Connected Vehicle Pilot test ID WV2IMCT-1 Vehicle 2 70 mph"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:36"
             ],
-            "landingPage": "https://data.transportation.gov/d/czjt-pnci",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NTD Program Support",
+                "hasEmail": "mailto:NTDHelp@dot.gov"
+            },
+            "description": "A national summary of funding sources based on data reported by transit agencies to the National Transit Database (NTD) in Report Year 2023.\r\n\r\nNTD Data Summaries organize and summarize data from the 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis.\r\n\r\nThis summary is based on the 2023 Revenue Sources file on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
+            "identifier": "https://data.transportation.gov/api/views/czjt-pnci",
             "issued": "2024-10-17",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-17",
             "keyword": [
                 "fares",
                 "federal funding",
@@ -40525,37 +40529,48 @@
                 "public transit",
                 "transit"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NTD Program Support",
-                "hasEmail": "mailto:NTDHelp@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/czjt-pnci",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-10-17",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Transit Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/czjt-pnci",
-            "description": "A national summary of funding sources based on data reported by transit agencies to the National Transit Database (NTD) in Report Year 2023.\r\n\r\nNTD Data Summaries organize and summarize data from the 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis.\r\n\r\nThis summary is based on the 2023 Revenue Sources file on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
-            "title": "2023 NTD Annual Data Summary - Funding Sources",
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "2023 NTD Annual Data Summary - Funding Sources"
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
-            "landingPage": "https://data.transportation.gov/d/d274-c5r3",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/06maytvt/06maytvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "May 2006"
+                }
             ],
+            "identifier": "18.100",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -40565,60 +40580,60 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.100",
+            "landingPage": "https://data.transportation.gov/d/d274-c5r3",
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
-            "title": "Monthly Traffic Volume Trends - May 2006",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/06maytvt/06maytvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "May 2006"
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
+            "title": "Monthly Traffic Volume Trends - May 2006"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www-nrd.nhtsa.dot.gov/CMSWeb/listpublications.aspx%3FId=19&ShowBy=Category",
+            "agencyProgramURL": "http://www.nhtsa.gov/Research/Human+Factors/Seatbelt+and+Child+Seat+Use",
+            "bureauCode": [
+                "021:18"
+            ],
+            "categoryDesignation": "Research",
+            "collectionInstrument": "Transportation",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
+            "dataQuality": true,
+            "describedBy": "ftp://ftp.nhtsa.dot.gov/Child_Seat_Usage_Surveys/LATCH_Use_and_Misuse_Study_2006/contents.pdf",
+            "describedByType": "application/pdf",
+            "description": "Provide information on the impact of LATCH on child seat use. It will show if consumers are using LATCH to install child safety seats, if they are easy to install and if they are installed correctly.",
+            "distribution": [
                 {
-            "accessLevel": "public",
-            "bureauCode": [
-                "021:18"
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/Child_Seat_Usage_Surveys/LATCH_Use_and_Misuse_Study_2006/tbloccupant.sas7bdat",
+                    "mediaType": "text/plain",
+                    "title": "SAS Occupant Data"
+                }
             ],
-            "landingPage": "https://data.transportation.gov/d/d2ht-5adb",
+            "identifier": "DOT-539",
             "issued": "2006-12-31",
-            "temporal": "2005-04-01/2005-08-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
-            "collectionInstrument": "Transportation",
-            "references": [
-                "http://www-nrd.nhtsa.dot.gov/Pubs/811852.pdf"
-            ],
             "keyword": [
                 "child restraint systems",
                 "css",
@@ -40629,80 +40644,46 @@
                 "research methodology",
                 "use and misuse"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "DOT-539",
+            "landingPage": "https://data.transportation.gov/d/d2ht-5adb",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-4696",
+            "programCode": [
+                "021:032"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Highway Traffic Safety Administration"
             },
-            "description": "Provide information on the impact of LATCH on child seat use. It will show if consumers are using LATCH to install child safety seats, if they are easy to install and if they are installed correctly.",
-            "title": "Child Restraint Use Survey:  LATCH Use and Misuse",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Human+Factors/Seatbelt+and+Child+Seat+Use",
-            "describedByType": "application/pdf",
-            "programCode": [
-                "021:032"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/Child_Seat_Usage_Surveys/LATCH_Use_and_Misuse_Study_2006/tbloccupant.sas7bdat",
-                    "mediaType": "text/plain",
-                    "title": "SAS Occupant Data"
-                }
+            "references": [
+                "http://www-nrd.nhtsa.dot.gov/Pubs/811852.pdf"
             ],
-            "describedBy": "ftp://ftp.nhtsa.dot.gov/Child_Seat_Usage_Surveys/LATCH_Use_and_Misuse_Study_2006/contents.pdf",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www-nrd.nhtsa.dot.gov/CMSWeb/listpublications.aspx%3FId=19&ShowBy=Category",
+            "temporal": "2005-04-01/2005-08-31",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4696",
-            "language": [
-                "en-US"
-            ]
+            "title": "Child Restraint Use Survey:  LATCH Use and Misuse"
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
-            "landingPage": "https://data.transportation.gov/d/d2nm-dif4",
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
-            "identifier": "696.5",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "A compilation of historic documents and articles on the Interstate System, Federal-Aid Highway Program, FHWA, and transportation.",
-            "title": "Highway History - Federal-Aid Legislation",
-            "isPartOf": "DOT-696",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/infrastructure/history.cfm",
-            "programCode": [
-                "021:011"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40711,51 +40692,49 @@
                     "title": "Federal-Aid Legislation"
                 }
             ],
-            "spatial": "National",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "696.5",
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
+            "landingPage": "https://data.transportation.gov/d/d2nm-dif4",
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
+            "title": "Highway History - Federal-Aid Legislation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/d2st-9nd6",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2022-04-01",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "ferry",
-                "ferry operators",
-                "ferry transit",
-                "passenger ferry",
-                "transportation",
-                "water transportation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Clara Reschovsky",
                 "hasEmail": "mailto:clara.reschovsky@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/d2st-9nd6",
             "description": "This is the Vessels file for the 2020 National Census of Ferry Operators. It is one of five data sets that make up the 2020 NCFO",
-            "title": "2020 NCFO Vessels File",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40763,73 +40742,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/d2st-9nd6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/d2st-9nd6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/d2st-9nd6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/d2st-9nd6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/d2st-9nd6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/d2st-9nd6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/d2st-9nd6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/d2st-9nd6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/d2st-9nd6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States. 50 States, Washington DC and Territories",
+            "identifier": "https://data.transportation.gov/api/views/d2st-9nd6",
+            "issued": "2022-04-01",
+            "keyword": [
+                "ferry",
+                "ferry operators",
+                "ferry transit",
+                "passenger ferry",
+                "transportation",
+                "water transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/d2st-9nd6",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2022-04-28",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "spatial": "United States. 50 States, Washington DC and Territories",
             "theme": [
                 "Maritime and Waterways"
-            ]
+            ],
+            "title": "2020 NCFO Vessels File"
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
-            "landingPage": "https://data.transportation.gov/d/d35b-tz62",
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
-            "identifier": "1840.4",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/veh/vehdb-export-fields.htm",
             "description": "The NHTSA Vehicle Crash Test Database contains engineering data measured during various types of research, the New Car Assessment Program (NCAP), and compliance crash tests. Information in this database refers to the performance and response of vehicles and other structures in impacts. This database is not intended to support general consumer safety issues. For general consumer information please see the NHTSA's information on buying a safer car.",
-            "title": "Vehicle Crash Test Database - Interactive Access",
-            "isPartOf": "DOT-1840",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research",
-            "primaryITInvestmentUII": "021-961265599",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40838,54 +40816,54 @@
                     "title": "Interactive Access"
                 }
             ],
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/veh/vehdb-export-fields.htm",
-            "dataQuality": true,
+            "identifier": "1840.4",
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
+            "landingPage": "https://data.transportation.gov/d/d35b-tz62",
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
+            "title": "Vehicle Crash Test Database - Interactive Access"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/d38r-yvh5",
             "bureauCode": [
                 "021:04"
             ],
-            "rights": "Business-sensitive data has been removed from this dataset",
-            "issued": "2020-05-05",
-            "@type": "dcat:Dataset",
-            "temporal": "2017-01-01/2017-12-31",
-            "modified": "2020-07-07",
-            "keyword": [
-                "ferry transit",
-                "ncfo",
-                "operator segment",
-                "passenger transit",
-                "route segment",
-                "transit"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Janine McFadden",
                 "hasEmail": "mailto:janine.mcfadden@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/d38r-yvh5",
+            "dataQuality": true,
             "description": "Reported calendar year 2017 segments as surveyed in the 2018 NCFO. \n\nSome segments are reported by more than one ferry operator.",
-            "title": "National Census of Ferry Operators (NCFO) 2018: Operator Segment Data",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40893,67 +40871,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/d38r-yvh5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/d38r-yvh5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/d38r-yvh5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/d38r-yvh5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/d38r-yvh5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/d38r-yvh5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/d38r-yvh5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/d38r-yvh5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/d38r-yvh5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S., U.S. Territories, and applicable Canadian providences",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/d38r-yvh5",
+            "issued": "2020-05-05",
+            "keyword": [
+                "ferry transit",
+                "ncfo",
+                "operator segment",
+                "passenger transit",
+                "route segment",
+                "transit"
+            ],
+            "landingPage": "https://data.transportation.gov/d/d38r-yvh5",
             "license": "Other",
+            "modified": "2020-07-07",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "rights": "Business-sensitive data has been removed from this dataset",
+            "spatial": "U.S., U.S. Territories, and applicable Canadian providences",
+            "temporal": "2017-01-01/2017-12-31",
             "theme": [
                 "Ferry Transit"
-            ]
+            ],
+            "title": "National Census of Ferry Operators (NCFO) 2018: Operator Segment Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Access restricted under the Privacy Act of 1974; see System of Records Notice for more information.",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/d38v-rmke",
-            "issued": "2014-12-29",
-            "temporal": "R/2014-12-29/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "civil rights",
-                "disability",
-                "reasonable accommodation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "558.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
             "description": "Data related to the request for reasonable accommodations.",
-            "title": "Reasonable Accommodation Request Data -",
-            "primaryITInvestmentUII": "021-613720405",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40961,27 +40943,49 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "theme": [
-                "Transportation"
+            "identifier": "558.0",
+            "issued": "2014-12-29",
+            "keyword": [
+                "civil rights",
+                "disability",
+                "reasonable accommodation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/d38v-rmke",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-8741"
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-14",
+            "phone": "202-366-8741",
+            "primaryITInvestmentUII": "021-613720405",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "rights": "Access restricted under the Privacy Act of 1974; see System of Records Notice for more information.",
+            "temporal": "R/2014-12-29/P1Y",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Reasonable Accommodation Request Data -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/d3er-58uw",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Transportation Analysis",
+                "hasEmail": "mailto:long.nguyen@dot.gov"
+            },
+            "description": "Freight Facts and Figures - The Nation Served by Freight",
+            "identifier": "https://data.transportation.gov/api/views/d3er-58uw",
             "issued": "2019-07-16",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-17",
             "keyword": [
                 "bts",
                 "bureau of transportation statistics",
@@ -40991,34 +40995,34 @@
                 "freight facts & figures",
                 "freight transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Transportation Analysis",
-                "hasEmail": "mailto:long.nguyen@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/d3er-58uw",
+            "modified": "2024-06-17",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statisitics"
             },
-            "identifier": "https://data.transportation.gov/api/views/d3er-58uw",
-            "description": "Freight Facts and Figures - The Nation Served by Freight",
-            "title": "The Nation Served by Freight",
-            "programCode": [
-                "021:053"
-            ],
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "The Nation Served by Freight"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:36"
             ],
-            "landingPage": "https://data.transportation.gov/d/d3w6-v5j8",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NTD Program Support",
+                "hasEmail": "mailto:NTDHelp@dot.gov"
+            },
+            "description": "A national summary of funding sources based on data reported by transit agencies to the National Transit Database (NTD) in Report Year 2022.\r\n\r\nNTD Data Summaries organize and summarize data from the 2022 National Transit Database in a manner that is more useful for quick reference and summary analysis.\r\n\r\nThis summary is based on the 2022 Revenue Sources file on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
+            "identifier": "https://data.transportation.gov/api/views/d3w6-v5j8",
             "issued": "2023-09-09",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-10",
             "keyword": [
                 "fares",
                 "federal funding",
@@ -41026,60 +41030,38 @@
                 "public transit",
                 "transit"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NTD Program Support",
-                "hasEmail": "mailto:NTDHelp@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/d3w6-v5j8",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-09-10",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Transit Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/d3w6-v5j8",
-            "description": "A national summary of funding sources based on data reported by transit agencies to the National Transit Database (NTD) in Report Year 2022.\r\n\r\nNTD Data Summaries organize and summarize data from the 2022 National Transit Database in a manner that is more useful for quick reference and summary analysis.\r\n\r\nThis summary is based on the 2022 Revenue Sources file on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
-            "title": "2022 NTD Annual Data Summary - Funding Sources",
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "2022 NTD Annual Data Summary - Funding Sources"
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
-            "landingPage": "https://data.transportation.gov/d/d45u-4dpp",
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
-            "identifier": "DOT-671",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Railroad Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.fra.dot.gov/eLib/Find",
             "description": "Collection of documents",
-            "title": "eLibrary",
-            "agencyProgramURL": "http://www.fra.dot.gov/eLib/Find",
-            "primaryITInvestmentUII": "021-255678806",
-            "programCode": [
-                "021:036"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41088,60 +41070,57 @@
                     "title": "Search Tool"
                 }
             ],
-            "describedBy": "http://www.fra.dot.gov/eLib/Find",
-            "dataQuality": true,
+            "identifier": "DOT-671",
+            "issued": "2014-11-21",
+            "keyword": [
+                "fra elibrary",
+                "fra e-library",
+                "fra library",
+                "library fra"
+            ],
+            "landingPage": "https://data.transportation.gov/d/d45u-4dpp",
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
+            "title": "eLibrary"
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
-            "landingPage": "https://data.transportation.gov/d/d47m-rf6y",
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
-            "identifier": "524.16",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "STATE DATA REPORTING SYSTEMS. Annual reports on the Fatality Analysis Reporting System (FARS) which is data regarding fatalities that is collected by a FARS analyst from each State and provided to NHTSA.",
-            "title": "GES Reports - 1997",
-            "isPartOf": "DOT-524",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:032"
-            ],
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
+            "description": "STATE DATA REPORTING SYSTEMS. Annual reports on the Fatality Analysis Reporting System (FARS) which is data regarding fatalities that is collected by a FARS analyst from each State and provided to NHTSA.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41150,30 +41129,55 @@
                     "title": "1997"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
-            "dataQuality": true,
+            "identifier": "524.16",
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
+            "landingPage": "https://data.transportation.gov/d/d47m-rf6y",
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
+            "title": "GES Reports - 1997"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/d5am-u7vx",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Simon Randrianarivelo",
+                "hasEmail": "mailto:s.randrianarivelo@dot.gov"
+            },
+            "description": "Page describes the U.S. Department of Transportation, Bureau of Transportation Statistics' Transportation Economic Data offerings.",
+            "identifier": "https://data.transportation.gov/api/views/d5am-u7vx",
             "issued": "2020-12-15",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-09",
             "keyword": [
                 "cost",
                 "economics",
@@ -41193,35 +41197,44 @@
                 "transportation productivity",
                 "transportation revenue"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Simon Randrianarivelo",
-                "hasEmail": "mailto:s.randrianarivelo@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/d5am-u7vx",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-01-09",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/d5am-u7vx",
-            "description": "Page describes the U.S. Department of Transportation, Bureau of Transportation Statistics' Transportation Economic Data offerings.",
-            "title": "Transportation Economic Trends (TET) for TRB",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Transportation Economic Trends (TET) for TRB"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.21949/1501460",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Transportation Library",
+                "hasEmail": "mailto:ntldatacurator@dot.gov"
+            },
+            "description": "The report covers transportation-related financial activities of the federal, \nstate and local governments, as well as government enterprises \n(e.g., public transit agencies, toll highways, parking lots, air terminals, \netc) that finance most of their outlays by providing services to the public. \nThe report focuses on the role of the government as transportation \ninfrastructure system provider and its financial activities pertaining to \nthis function. The financial activities of the government as user of the \ntransportation system are not included except when these activities are \ndirectly relevant to its role as provider of the transportation \ninfrastructure. The following broad categories of data are provided in this \nreport: Federal revenues and expenditures by mode and program for \nFY 1985-2000. Federal grants to state and local governments by mode for \nFY 1985-2000. Federal budget authority and obligations by mode and program \nfor FY 1985-2000. State government revenues and expenditures by mode for \nthe fifty states for FY 1985- 1999.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://doi.org/10.21949/1501460",
+                    "mediaType": "application/zip",
+                    "title": "Government Transportation Financial Statistics (GTFS) 2001 [supporting datasets]"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/d5bg-kazz",
             "issued": "2002-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2022-02-15",
             "keyword": [
                 "airlines",
                 "earnings",
@@ -41245,74 +41258,38 @@
                 "trend (statistics)",
                 "water transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Transportation Library",
-                "hasEmail": "mailto:ntldatacurator@dot.gov"
-            },
+            "landingPage": "https://doi.org/10.21949/1501460",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-02-15",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/d5bg-kazz",
-            "description": "The report covers transportation-related financial activities of the federal, \nstate and local governments, as well as government enterprises \n(e.g., public transit agencies, toll highways, parking lots, air terminals, \netc) that finance most of their outlays by providing services to the public. \nThe report focuses on the role of the government as transportation \ninfrastructure system provider and its financial activities pertaining to \nthis function. The financial activities of the government as user of the \ntransportation system are not included except when these activities are \ndirectly relevant to its role as provider of the transportation \ninfrastructure. The following broad categories of data are provided in this \nreport: Federal revenues and expenditures by mode and program for \nFY 1985-2000. Federal grants to state and local governments by mode for \nFY 1985-2000. Federal budget authority and obligations by mode and program \nfor FY 1985-2000. State government revenues and expenditures by mode for \nthe fifty states for FY 1985- 1999.",
-            "title": "Government Transportation Financial Statistics (GTFS) 2001 [supporting datasets]",
-            "programCode": [
-                "021:053"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://doi.org/10.21949/1501460",
-                    "mediaType": "application/zip",
-                    "title": "Government Transportation Financial Statistics (GTFS) 2001 [supporting datasets]"
-                }
-            ],
             "spatial": "United States",
-            "accrualPeriodicity": "R/PT1S",
             "theme": [
                 "Research and Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Government Transportation Financial Statistics (GTFS) 2001 [supporting datasets]"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/d6nc-s8v6",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2017-10-31",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
-            "keyword": [
-                "airfares",
-                "aviation",
-                "aviation policy",
-                "city pair",
-                "consumer airfare report",
-                "fare levels",
-                "fare premium",
-                "fares",
-                "office of aviation analysis",
-                "table 7"
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
-            "identifier": "https://data.transportation.gov/api/views/d6nc-s8v6",
+            "dataQuality": true,
             "description": "Provides fare premiums for airports in the top 1,000 city pairs, and demonstrates the impact of low-fare service and hub domination on fare levels.  \r\nAll records are aggregated as directionless city pair markets.  Air traffic in each direction is combined.  https://www.transportation.gov/policy/aviation-policy/competition-data-analysis/research-reports",
-            "title": "Consumer Airfare Report: Table 7 - Fare Premiums for Select Cities with More Than 20 Passengers per Day",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41320,45 +41297,86 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/d6nc-s8v6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/d6nc-s8v6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/d6nc-s8v6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/d6nc-s8v6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/d6nc-s8v6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/d6nc-s8v6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/d6nc-s8v6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/d6nc-s8v6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/d6nc-s8v6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/d6nc-s8v6",
+            "issued": "2017-10-31",
+            "keyword": [
+                "airfares",
+                "aviation",
+                "aviation policy",
+                "city pair",
+                "consumer airfare report",
+                "fare levels",
+                "fare premium",
+                "fares",
+                "office of aviation analysis",
+                "table 7"
+            ],
+            "landingPage": "https://data.transportation.gov/d/d6nc-s8v6",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2025-01-27",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
             "theme": [
                 "Aviation"
-            ]
+            ],
+            "title": "Consumer Airfare Report: Table 7 - Fare Premiums for Select Cities with More Than 20 Passengers per Day"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/d7ha-dyix",
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
+                    "description": "2013 Illinois HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/illinois2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Illinois"
+                }
+            ],
+            "identifier": "678.117",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -41372,84 +41390,45 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.117",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Illinois",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/d7ha-dyix",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/illinois2013.zip",
-                    "description": "2013 Illinois HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Illinois"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Illinois"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://nationalregistry.fmcsa.dot.gov/NRPublicUI/home.seam",
+            "agencyProgramURL": "https://nationalregistry.fmcsa.dot.gov/NRPublicUI/home.seam",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/d8hn-gwuw",
-            "issued": "2015-01-21",
-            "temporal": "R/2015-01-21/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "https://nationalregistry.fmcsa.dot.gov/NRPublicUI/home.seam"
-            ],
-            "keyword": [
-                "driver and carrier.",
-                "driver drug test",
-                "driver medical examiner",
-                "driver testing",
-                "medical examiners"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO",
                 "hasEmail": "mailto:fmcsa.cdo@dot.gov"
             },
-            "identifier": "1643.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": true,
             "description": "All commercial drivers whose current medical certificate expires on or after May 21, 2014, at expiration of that certificate must be examined by a medical professional listed on the National Registry of Certified Medical Examiners. Only medical examiners that have completed training and successfully passed a test on FMCSA's physical qualification standards will be listed on the National Registry.",
-            "title": "The National Registry of Certified Medical Examiners - The National Registry of Certified Medical Examiners",
-            "agencyProgramURL": "https://nationalregistry.fmcsa.dot.gov/NRPublicUI/home.seam",
-            "primaryITInvestmentUII": "021-748398219",
-            "programCode": [
-                "021:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41458,51 +41437,77 @@
                     "title": "The National Registry of Certified Medical Examiners"
                 }
             ],
-            "spatial": "National, State.",
-            "dataQuality": true,
+            "identifier": "1643.0",
+            "issued": "2015-01-21",
+            "keyword": [
+                "driver and carrier.",
+                "driver drug test",
+                "driver medical examiner",
+                "driver testing",
+                "medical examiners"
+            ],
+            "landingPage": "https://data.transportation.gov/d/d8hn-gwuw",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "https://nationalregistry.fmcsa.dot.gov/NRPublicUI/home.seam",
+            "modified": "2024-05-24",
+            "phone": "202-366-2829",
+            "primaryITInvestmentUII": "021-748398219",
+            "programCode": [
+                "021:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "references": [
+                "https://nationalregistry.fmcsa.dot.gov/NRPublicUI/home.seam"
+            ],
+            "spatial": "National, State.",
+            "temporal": "R/2015-01-21/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "phone": "202-366-2829",
-            "language": [
-                "en-US"
-            ]
+            "title": "The National Registry of Certified Medical Examiners - The National Registry of Certified Medical Examiners"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/dahn-mb3y",
-            "issued": "2020-08-13",
             "@type": "dcat:Dataset",
-            "modified": "2021-04-21",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/dahn-mb3y",
+            "issued": "2020-08-13",
+            "landingPage": "https://data.transportation.gov/d/dahn-mb3y",
+            "modified": "2021-04-21",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
-            "title": "2018-2019 County Summary Data",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "2018-2019 County Summary Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/dakf-i7zd",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "FRA\u2019s Office of Safety public data portal includes railroad safety information, reports and data tables on topics such as railroad accidents, incidents, casualties, and highway-rail grade crossing inventory.",
+            "identifier": "https://data.transportation.gov/api/views/dakf-i7zd",
             "issued": "2023-08-08",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "accidents",
                 "casualties",
@@ -41515,96 +41520,72 @@
                 "railroad",
                 "safety data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/dakf-i7zd",
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
-            "identifier": "https://data.transportation.gov/api/views/dakf-i7zd",
-            "description": "FRA\u2019s Office of Safety public data portal includes railroad safety information, reports and data tables on topics such as railroad accidents, incidents, casualties, and highway-rail grade crossing inventory.",
-            "title": "FRA Safety Data Landing Page",
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
+            "title": "FRA Safety Data Landing Page"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/dbb4-pr2c",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Methodology for page with interactive map and graph showing access to intercity transportation in rural areas",
+            "identifier": "https://data.transportation.gov/api/views/dbb4-pr2c",
             "issued": "2019-12-17",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-21",
             "keyword": [
                 "accessibility",
                 "intercity transportation",
                 "rural",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/dbb4-pr2c",
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
-            "identifier": "https://data.transportation.gov/api/views/dbb4-pr2c",
-            "description": "Methodology for page with interactive map and graph showing access to intercity transportation in rural areas",
-            "title": "Rural Accessibility Methodology",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Rural Accessibility Methodology"
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
-            "identifier": "https://data.transportation.gov/api/views/dbr2-hxmv",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 1988",
-            "title": "Historic HPMS Data (Universe) - 1988",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41612,65 +41593,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/dbr2-hxmv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dbr2-hxmv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dbr2-hxmv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/dbr2-hxmv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dbr2-hxmv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dbr2-hxmv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/dbr2-hxmv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dbr2-hxmv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dbr2-hxmv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/dbr2-hxmv",
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
+            "title": "Historic HPMS Data (Universe) - 1988"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/dc74-f8qd",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2021-12-16",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-25",
-            "keyword": [
-                "public transit",
-                "transit",
-                "transit ridership"
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
-            "identifier": "https://data.transportation.gov/api/views/dc74-f8qd",
             "description": "Includes New York City MTA Subway, San Francisco BART Rail, Washington Metropolitan Area Transit Authority Bus and Rail",
-            "title": "Daily Transit Ridership",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41678,62 +41661,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/dc74-f8qd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dc74-f8qd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dc74-f8qd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/dc74-f8qd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dc74-f8qd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dc74-f8qd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/dc74-f8qd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dc74-f8qd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dc74-f8qd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/dc74-f8qd",
+            "issued": "2021-12-16",
+            "keyword": [
+                "public transit",
+                "transit",
+                "transit ridership"
+            ],
+            "landingPage": "https://data.transportation.gov/d/dc74-f8qd",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1W",
+            "modified": "2022-10-25",
+            "phone": "2023660573",
+            "programCode": [
+                "021:042"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Transit"
             ],
-            "phone": "2023660573",
-            "language": [
-                "en-US"
-            ]
+            "title": "Daily Transit Ridership"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/dd43-h6wv",
-            "bureauCode": [
-                "021:36"
-            ],
-            "issued": "2024-10-02",
             "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
-            "keyword": [
-                "funding",
-                "state funding"
+            "accessLevel": "public",
+            "bureauCode": [
+                "021:36"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NTD Program Support",
                 "hasEmail": "mailto:NTDHelp@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Transit Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/dd43-h6wv",
             "description": "This dataset details state funding sources for each applicable agency reporting to the National Transit Database in the 2022 and 2023 report years. Examples include General and Transportation funds.\n\nNTD Data Tables organize and summarize data from the 2022 and 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. This dataset is based on the 2022 and 2023 Revenue Sources database files.\n\nIn report year 2022, Extraordinary and Special Item Funds were reported under General Funds. In report year 2023, this was separated into its own category. \n\nIn years 2015-2021, you can find this data in the \"Funding Sources\" data table on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.\n\nIf you have any other questions about this table, please contact the NTD Help Desk at NTDHelp@dot.gov.",
-            "title": "2022 - 2023 NTD Annual Data - Funding Sources (State)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41741,119 +41727,115 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/dd43-h6wv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dd43-h6wv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dd43-h6wv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/dd43-h6wv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dd43-h6wv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dd43-h6wv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/dd43-h6wv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dd43-h6wv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dd43-h6wv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/dd43-h6wv",
+            "issued": "2024-10-02",
+            "keyword": [
+                "funding",
+                "state funding"
+            ],
+            "landingPage": "https://data.transportation.gov/d/dd43-h6wv",
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
+            "title": "2022 - 2023 NTD Annual Data - Funding Sources (State)"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ddp4-w9sp",
-            "issued": "2021-05-10",
             "@type": "dcat:Dataset",
-            "modified": "2024-03-13",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sean Jahanmir",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/ddp4-w9sp",
+            "issued": "2021-05-10",
+            "landingPage": "https://data.transportation.gov/d/ddp4-w9sp",
+            "modified": "2024-03-13",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Infrastructure"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/dds7-ww3c",
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
-            "identifier": "https://data.transportation.gov/api/views/dds7-ww3c",
             "description": "The Bureau of Transportation Statistics releases seasonally adjusted air traffic data based on monthly reports from commercial U.S. air carriers.",
-            "title": "Air Travel - International - Seasonally Adjusted",
+            "identifier": "https://data.transportation.gov/api/views/dds7-ww3c",
+            "issued": "2025-01-16",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/dds7-ww3c",
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
+            "title": "Air Travel - International - Seasonally Adjusted"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://data.transportation.gov/d/ddsj-fhuf",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2014-09-16",
-            "temporal": "R/2014-09-16/PT1S",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Energy and Utilities",
-            "modified": "2024-11-14",
-            "keyword": [
-                "consumption",
-                "electrical",
-                "power",
-                "use"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
-            "identifier": "383.0",
+            "dataQuality": false,
             "description": "This data set contains electric power usage for the DOT Headquarters building.",
-            "title": "Electrical Metering Data -",
-            "primaryITInvestmentUII": "021-291792267",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41861,55 +41843,53 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
+            "identifier": "383.0",
+            "issued": "2014-09-16",
+            "keyword": [
+                "consumption",
+                "electrical",
+                "power",
+                "use"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ddsj-fhuf",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2024-11-14",
+            "phone": "202-366-0046",
+            "primaryITInvestmentUII": "021-291792267",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "temporal": "R/2014-09-16/PT1S",
             "theme": [
                 "Energy and Utilities"
             ],
-            "categoryDesignation": "Administrative",
-            "phone": "202-366-0046",
-            "language": [
-                "en-US"
-            ]
+            "title": "Electrical Metering Data -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www.nhtsa.gov/staticfiles/nti/other/2008survey/drinkdrive_2008.sas7bdat",
+            "agencyProgramURL": "http://www.nhtsa.gov/Driving+Safety/Occupant+Protection/2008+National+Survey+of+Drinking+and+Driving+Attitudes+and+Behaviors",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/ddwk-wmh2",
-            "issued": "2010-08-31",
-            "temporal": "2008-09-10/2008-12-22",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.nhtsa.gov/staticfiles/nti/other/2008survey/formats.sas7bcat"
-            ],
-            "keyword": [
-                "attitudes",
-                "behaviors",
-                "drinking",
-                "driving"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "1637.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
             "description": "The 2008 National Survey of Drinking and Driving Attitudes and Behaviors was composed of a single questionnaire administered to a sample of randomly selected individuals 16 and older, with ages 16 through 24 over-sampled. The respondents were asked about their drinking behavior, their drinking and driving behavior, use of designated drivers, their hosting events in which drinking occurred, risks they perceive associated with drinking and driving, experience with anti-DWI enforcement activity, and their attitudes concerning major intervention strategies.The survey was administered from September 10, 2008 to December 22, 2008. A total of 6,999 respondents completed the survey, including 5,392 landline interviews and 1,607 cell phone interviews. The total number of completed interviews for each of the four Census regions (Northeast, Midwest, South, and West) was 1,409, 1,654, 2,390, and 1,546, respectively.",
-            "title": "2008 National Survey of Drinking and Driving Attitudes and Behaviors - SAS Data",
-            "isPartOf": "DOT-1637",
-            "agencyProgramURL": "http://www.nhtsa.gov/Driving+Safety/Occupant+Protection/2008+National+Survey+of+Drinking+and+Driving+Attitudes+and+Behaviors",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41918,31 +41898,69 @@
                     "title": "SAS Data"
                 }
             ],
-            "spatial": "n/a",
-            "dataQuality": false,
+            "identifier": "1637.2",
+            "isPartOf": "DOT-1637",
+            "issued": "2010-08-31",
+            "keyword": [
+                "attitudes",
+                "behaviors",
+                "drinking",
+                "driving"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ddwk-wmh2",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.nhtsa.gov/staticfiles/nti/other/2008survey/drinkdrive_2008.sas7bdat",
+            "modified": "2024-05-01",
+            "phone": "202-366-6401",
+            "programCode": [
+                "021:035"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "http://www.nhtsa.gov/staticfiles/nti/other/2008survey/formats.sas7bcat"
+            ],
+            "spatial": "n/a",
+            "temporal": "2008-09-10/2008-12-22",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "phone": "202-366-6401",
-            "language": [
-                "en-US"
-            ]
+            "title": "2008 National Survey of Drinking and Driving Attitudes and Behaviors - SAS Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/de8a-c3q9",
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
+                    "description": "2011 Wyoming HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/wyoming2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Wyoming"
+                }
+            ],
+            "identifier": "678.52",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -41956,55 +41974,51 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.52",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Wyoming",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/de8a-c3q9",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/wyoming2011.zip",
-                    "description": "2011 Wyoming HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Wyoming"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Wyoming"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.21949/1503757",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Transportation Library Data Curator",
+                "hasEmail": "mailto:ntldatacurator@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This zip file contains POSTDATA.ATT (.ATT); Print to File (.PRN); Portable Document Format (.PDF); and document (.DOCX) files of data to support FHWA-JPO-16-385, Analysis, modeling, and simulation (AMS) testbed development and evaluation to support dynamic mobility applications (DMA) and active transportation and demand management (ATDM) programs \u2014 evaluation report for ATDM program. Zip size is 168 MB. Files were accessed in 2017. Data will be preserved as is.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "This zip file contains POSTDATA.ATT (.ATT); Print to File (.PRN); Portable Document Format (.PDF); and document (.DOCX) files of data to support FHWA-JPO-16-385, Analysis, modeling, and simulation (AMS) testbed development and evaluation to support dynamic mobility applications (DMA) and active transportation and demand management (ATDM) programs \u2014 evaluation report for ATDM program. Zip size is 168 MB. Files were accessed in 2017. Data will be preserved as is.",
+                    "downloadURL": "https://doi.org/10.21949/1503757",
+                    "mediaType": "application/zip",
+                    "title": "Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs \u2014 Evaluation Report for ATDM Program [supporting datasets - Pasadena]"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/df88-xjvr",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2017-07-18",
             "keyword": [
                 "active transportation and demand management",
                 "ams pasadena",
@@ -42020,51 +42034,52 @@
                 "traffic flow",
                 "travel demand"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Transportation Library Data Curator",
-                "hasEmail": "mailto:ntldatacurator@dot.gov"
-            },
+            "landingPage": "https://doi.org/10.21949/1503757",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2017-07-18",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/df88-xjvr",
-            "description": "This zip file contains POSTDATA.ATT (.ATT); Print to File (.PRN); Portable Document Format (.PDF); and document (.DOCX) files of data to support FHWA-JPO-16-385, Analysis, modeling, and simulation (AMS) testbed development and evaluation to support dynamic mobility applications (DMA) and active transportation and demand management (ATDM) programs \u2014 evaluation report for ATDM program. Zip size is 168 MB. Files were accessed in 2017. Data will be preserved as is.",
-            "title": "Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs - Evaluation Report for ATDM Program [supporting datasets: Pasadena]",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://doi.org/10.21949/1503757",
-                    "description": "This zip file contains POSTDATA.ATT (.ATT); Print to File (.PRN); Portable Document Format (.PDF); and document (.DOCX) files of data to support FHWA-JPO-16-385, Analysis, modeling, and simulation (AMS) testbed development and evaluation to support dynamic mobility applications (DMA) and active transportation and demand management (ATDM) programs \u2014 evaluation report for ATDM program. Zip size is 168 MB. Files were accessed in 2017. Data will be preserved as is.",
-                    "@type": "dcat:Distribution",
-                    "title": "Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs \u2014 Evaluation Report for ATDM Program [supporting datasets - Pasadena]"
-                }
-            ],
             "spatial": "United States, California, Pasadena",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "language": [
-                "en-US"
-            ]
+            "title": "Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs - Evaluation Report for ATDM Program [supporting datasets: Pasadena]"
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
-            "landingPage": "https://data.transportation.gov/d/dfcg-vgjt",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/06septvt/06septvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "September 2006"
+                }
             ],
+            "identifier": "18.96",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -42074,55 +42089,45 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.96",
+            "landingPage": "https://data.transportation.gov/d/dfcg-vgjt",
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
-            "title": "Monthly Traffic Volume Trends - September 2006",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/06septvt/06septvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "September 2006"
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
+            "title": "Monthly Traffic Volume Trends - September 2006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/dgnq-c8xp",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRA Safety Data Team",
+                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This is the report for Fatality, Injury, and Illness Detail Listing (4.12).",
+            "identifier": "https://data.transportation.gov/api/views/dgnq-c8xp",
             "issued": "2024-08-19",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "casualties",
                 "casualty",
@@ -42140,68 +42145,43 @@
                 "trespassers",
                 "worker on duty"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRA Safety Data Team",
-                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/dgnq-c8xp",
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
-            "identifier": "https://data.transportation.gov/api/views/dgnq-c8xp",
-            "description": "This is the report for Fatality, Injury, and Illness Detail Listing (4.12).",
-            "title": "Fatality, Injury, and Illness Detail Listing (4.12)",
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
+            "title": "Fatality, Injury, and Illness Detail Listing (4.12)"
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
-            "landingPage": "https://data.transportation.gov/d/dh4m-3qpu",
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
-            "identifier": "373.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": true,
             "description": "Each Freedom of Information Act office uses a case log to track FOIA requests. The logs typically include the dates on which requests were received and closed, control numbers, requester names and descriptions of the requested records.",
-            "title": "Freedom of Information Act Logs for the Office of the Secretary of Transportation - 2008",
-            "isPartOf": "DOT-373",
-            "agencyProgramURL": "http://www.dot.gov/foia",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42210,53 +42190,53 @@
                     "title": "2008"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "373.2",
+            "isPartOf": "DOT-373",
+            "issued": "2007-12-31",
+            "keyword": [
+                "foia",
+                "freedom of information act",
+                "log",
+                "request"
+            ],
+            "landingPage": "https://data.transportation.gov/d/dh4m-3qpu",
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
+            "title": "Freedom of Information Act Logs for the Office of the Secretary of Transportation - 2008"
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
-            "identifier": "https://data.transportation.gov/api/views/dh5b-3r85",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 2008",
-            "title": "Historic HPMS Data (Sample) - 2008",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42264,128 +42244,128 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/dh5b-3r85/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dh5b-3r85/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dh5b-3r85/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/dh5b-3r85/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dh5b-3r85/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dh5b-3r85/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/dh5b-3r85/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dh5b-3r85/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dh5b-3r85/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/dh5b-3r85",
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
+            "title": "Historic HPMS Data (Sample) - 2008"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/di29-9hvz",
-            "issued": "2022-08-09",
             "@type": "dcat:Dataset",
-            "modified": "2023-01-19",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ong, Lisa CTR (OST)",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/di29-9hvz",
+            "issued": "2022-08-09",
+            "landingPage": "https://data.transportation.gov/d/di29-9hvz",
+            "modified": "2023-01-19",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Commodity Flow Survey 1997-2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/digq-7e2f",
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
-            "identifier": "https://data.transportation.gov/api/views/digq-7e2f",
             "description": "General aviation fatalities include private aviation operations and excludes Federal Aviation Regulation (FAR) Part 121 (Air Carriers), 129 (Foreign), 135 (On-Demand), and Non-U.S./Commercial operations. The National Transportation Safety Board releases aviation fatality data in the Aviation Accident Database.",
-            "title": "General Aviation Fatalities",
+            "identifier": "https://data.transportation.gov/api/views/digq-7e2f",
+            "issued": "2025-01-03",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/digq-7e2f",
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
+            "title": "General Aviation Fatalities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://portal.phmsa.dot.gov/PDMPublicReport/?url=https://portal.phmsa.dot.gov/analytics/saw.dll?Portalpages&PortalPath=%2Fshared%2FPublic%20Website%20Pages%2F_portal%2FYearly%20Incident%20Summary%20Reports ",
+            "agencyProgramURL": "http://www.phmsa.dot.gov/hazmat/library/data-stats/incidents",
+            "analysisUnit": "Incident",
             "bureauCode": [
                 "021:50"
             ],
-            "landingPage": "https://data.transportation.gov/d/dirx-hdpw",
-            "issued": "2003-01-01",
-            "temporal": "R/2003-01-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-29",
+            "categoryDesignation": "Research",
             "collectionInstrument": "DOT F 5800.1",
-            "references": [
-                "http://www.phmsa.dot.gov/hazmat/library/data-stats/incidents"
-            ],
-            "keyword": [
-                "hazardous",
-                "hazardous material",
-                "hazmat",
-                "incident",
-                "material",
-                "report"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Serita McKoy",
                 "hasEmail": "mailto:hmrequests@dot.gov"
             },
-            "identifier": "DOT-269",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Pipeline and Hazardous Materials Safety Administration"
-            },
+            "dataQuality": true,
             "description": "Series of Incident data and summary statistics reports produced which provide statistical information on incidents by type, year, geographical location, and others. The data provided is that from the Hazardous Materials Incident Report Form 5800.1",
-            "title": "Hazmat Yearly Incident Summary Reports",
-            "agencyProgramURL": "http://www.phmsa.dot.gov/hazmat/library/data-stats/incidents",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42394,78 +42374,85 @@
                     "title": "Data Mining Tool"
                 }
             ],
-            "spatial": "Street address",
-            "dataQuality": true,
+            "identifier": "DOT-269",
+            "issued": "2003-01-01",
+            "keyword": [
+                "hazardous",
+                "hazardous material",
+                "hazmat",
+                "incident",
+                "material",
+                "report"
+            ],
+            "landingPage": "https://data.transportation.gov/d/dirx-hdpw",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "https://portal.phmsa.dot.gov/PDMPublicReport/?url=https://portal.phmsa.dot.gov/analytics/saw.dll?Portalpages&PortalPath=%2Fshared%2FPublic%20Website%20Pages%2F_portal%2FYearly%20Incident%20Summary%20Reports ",
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
+                "http://www.phmsa.dot.gov/hazmat/library/data-stats/incidents"
+            ],
+            "spatial": "Street address",
+            "temporal": "R/2003-01-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "analysisUnit": "Incident",
-            "categoryDesignation": "Research",
-            "phone": "202-366-3373",
-            "language": [
-                "en-US"
-            ]
+            "title": "Hazmat Yearly Incident Summary Reports"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/dk5i-ipsm",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2019-12-07",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-05",
-            "keyword": [
-                "production",
-                "transportation services"
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
-            "identifier": "https://data.transportation.gov/api/views/dk5i-ipsm",
             "description": "Use of transportation services by industry",
-            "title": "Transportation Economic Trends: Contribution of Transportation - Use by Industry",
+            "identifier": "https://data.transportation.gov/api/views/dk5i-ipsm",
+            "issued": "2019-12-07",
+            "keyword": [
+                "production",
+                "transportation services"
+            ],
+            "landingPage": "https://data.transportation.gov/d/dk5i-ipsm",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-12-05",
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
+            "title": "Transportation Economic Trends: Contribution of Transportation - Use by Industry"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/dkbd-kjgw",
-            "issued": "2020-06-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-07-15",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Justyna Goworowska",
                 "hasEmail": "mailto:j.goworowska.ctr@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/dkbd-kjgw",
             "description": "This table shows the number and percent of people in the contiguous United States (excludes Alaska and Hawaii) potentially exposed to different levels of noise from passenger rail sources.",
-            "title": "Population potentially exposed to passenger rail noise, 2018",
-            "programCode": [
-                "021:052"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42473,69 +42460,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/dkbd-kjgw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dkbd-kjgw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dkbd-kjgw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/dkbd-kjgw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dkbd-kjgw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dkbd-kjgw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/dkbd-kjgw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dkbd-kjgw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dkbd-kjgw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "https://data.transportation.gov/api/views/dkbd-kjgw",
+            "issued": "2020-06-22",
+            "landingPage": "https://data.transportation.gov/d/dkbd-kjgw",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2020-07-15",
+            "programCode": [
+                "021:052"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Population potentially exposed to passenger rail noise, 2018"
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
-            "landingPage": "https://data.transportation.gov/d/dkc3-e57i",
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
-            "identifier": "557.5",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
+            "describedBy": "https://www.civilrights.dot.gov/node/3828",
             "description": "Data related to the management of EEO complaint processing.  Due to the presence of PII, the raw data is not available for public consumption.  However, aggregated data is available in the DOT's NoFEAR Act report and Form 462 Report.  Both are located on the DOT Office of Civil Rights' public website.",
-            "title": "EEO Complaint Processing Data - FMCSA No FEAR Data",
-            "isPartOf": "DOT-557",
-            "agencyProgramURL": "http://www.civilrights.dot.gov",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42544,32 +42523,71 @@
                     "title": "FMCSA No FEAR Data"
                 }
             ],
-            "describedBy": "https://www.civilrights.dot.gov/node/3828",
-            "dataQuality": false,
+            "identifier": "557.5",
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
+            "landingPage": "https://data.transportation.gov/d/dkc3-e57i",
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
+            "title": "EEO Complaint Processing Data - FMCSA No FEAR Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/dku8-74s7",
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
+                    "description": "2011 Montana HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/montana2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Montana"
+                }
+            ],
+            "identifier": "678.28",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -42583,73 +42601,39 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.28",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Montana",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/dku8-74s7",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/montana2011.zip",
-                    "description": "2011 Montana HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Montana"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Montana"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/dkxx-zjd6",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
-            "keyword": [
-                "general administration",
-                "transit expenses",
-                "transit function",
-                "vehicle operations"
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
-            "identifier": "https://data.transportation.gov/api/views/dkxx-zjd6",
             "description": "This dataset details operating expenses for each applicable agency, mode, and type of service (TOS), split by expense type reporting to the National Transit Database in the 2022 and 2023 report years. Expense types include Vehicle Operations, General Administration, and more.\n\nOnly Full Reporters report expenses by function and type. Expenses from other reporter types are included under Reduced Reporter Expenses.\n\nNTD Data Tables organize and summarize data from the 2022 and 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. This dataset is based on the 2022 and 2023 Operating Expenses database files.\n\nIn years 2015-2021, you can find this data in the \"Operating Expenses\" data table on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.\n\nIf you have any other questions about this table, please contact the NTD Help Desk at NTDHelp@dot.gov.",
-            "title": "2022 - 2023 NTD Annual Data - Operating Expenses (by Function)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42657,68 +42641,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/dkxx-zjd6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dkxx-zjd6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dkxx-zjd6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/dkxx-zjd6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dkxx-zjd6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dkxx-zjd6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/dkxx-zjd6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dkxx-zjd6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dkxx-zjd6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/dkxx-zjd6",
+            "issued": "2024-09-10",
+            "keyword": [
+                "general administration",
+                "transit expenses",
+                "transit function",
+                "vehicle operations"
+            ],
+            "landingPage": "https://data.transportation.gov/d/dkxx-zjd6",
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
+            "title": "2022 - 2023 NTD Annual Data - Operating Expenses (by Function)"
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
-            "landingPage": "https://data.transportation.gov/d/dm7t-vyrp",
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
-            "identifier": "692.33",
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
@@ -42727,51 +42708,51 @@
                     "title": "Carbon Monoxide"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.33",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/dm7t-vyrp",
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
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2022-06-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "motor vehicle",
-                "motor vehicle registrations",
-                "registrations",
-                "states",
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
-            "identifier": "https://data.transportation.gov/api/views/dmdt-3iju",
+            "dataQuality": true,
             "description": "The motor vehicle registration dashboard shows the number and type of vehicle (automobile, truck, motorcycle, and bus) registered over time in each state.",
-            "title": "Motor Vehicle Registrations Dashboard data",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42779,67 +42760,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/dmdt-3iju/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dmdt-3iju/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dmdt-3iju/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/dmdt-3iju/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dmdt-3iju/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dmdt-3iju/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/dmdt-3iju/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dmdt-3iju/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dmdt-3iju/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/dmdt-3iju",
+            "issued": "2022-06-02",
+            "keyword": [
+                "motor vehicle",
+                "motor vehicle registrations",
+                "registrations",
+                "states",
+                "travel"
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
+            "title": "Motor Vehicle Registrations Dashboard data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/dmn2-bn4i",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2019-08-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-09",
-            "keyword": [
-                "amtrak",
-                "opportunity zone",
-                "rail",
-                "railroad",
-                "station"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Railroad Safety",
                 "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
-            "identifier": "https://data.transportation.gov/api/views/dmn2-bn4i",
+            "dataQuality": true,
             "description": "This dataset shows Amtrak stations in opportunity zones",
-            "title": "Amtrak Real Estate Assets in Opportunity Zones - Stations",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -42847,46 +42829,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/dmn2-bn4i/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dmn2-bn4i/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dmn2-bn4i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/dmn2-bn4i/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dmn2-bn4i/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dmn2-bn4i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/dmn2-bn4i/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dmn2-bn4i/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dmn2-bn4i/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/dmn2-bn4i",
+            "issued": "2019-08-02",
+            "keyword": [
+                "amtrak",
+                "opportunity zone",
+                "rail",
+                "railroad",
+                "station"
+            ],
+            "landingPage": "https://data.transportation.gov/d/dmn2-bn4i",
+            "language": [
+                "en-US"
+            ],
             "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-10-09",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
             "theme": [
                 "Railroads"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Amtrak Real Estate Assets in Opportunity Zones - Stations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/dmnz-cpt3",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This report contains a ranking of highway grade crossing incidents by (1) total incidents, (2) total fatal incidents and (3) total injury incidents, along with data for total fatalities and total injuries.",
+            "identifier": "https://data.transportation.gov/api/views/dmnz-cpt3",
             "issued": "2023-08-04",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "fatal incidents",
                 "fatalities",
@@ -42898,43 +42903,53 @@
                 "injury incidents",
                 "total incidents"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/dmnz-cpt3",
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
-            "identifier": "https://data.transportation.gov/api/views/dmnz-cpt3",
-            "description": "This report contains a ranking of highway grade crossing incidents by (1) total incidents, (2) total fatal incidents and (3) total injury incidents, along with data for total fatalities and total injuries.",
-            "title": "Frequency of Highway-Rail Grade Crossing Incidents (5.08)",
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
+            "title": "Frequency of Highway-Rail Grade Crossing Incidents (5.08)"
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
-            "landingPage": "https://data.transportation.gov/d/dnur-tu3r",
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
+            "identifier": "123.2",
+            "isPartOf": "DOT-123",
+            "issued": "2000-01-01",
             "keyword": [
                 "bus",
                 "company safety profile",
@@ -42951,55 +42966,45 @@
                 "safersys",
                 "safety and fitness electronic records"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "123.2",
+            "landingPage": "https://data.transportation.gov/d/dnur-tu3r",
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
-            "title": "SAFER - Company Safety Profile - Company Safety Profile (CSP)",
-            "isPartOf": "DOT-123",
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
-            "categoryDesignation": "Research",
-            "analysisUnit": "Motor Carrier",
-            "phone": "202-493-0215",
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFER - Company Safety Profile - Company Safety Profile (CSP)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/dnz7-ag8y",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Report Filter Definitions and Guidance\r\nPlease note that all filter options are present in the dataset. For example, if you are looking at a dataset and a state is missing, it means there is no data for the year selected in that state - it does not use a list of all US states. \r\nAlso note that if the data table disappears, there is no data available for the filter selections made.",
+            "identifier": "https://data.transportation.gov/api/views/dnz7-ag8y",
             "issued": "2023-08-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-03",
             "keyword": [
                 "define",
                 "definitions",
@@ -43007,74 +43012,84 @@
                 "glossary",
                 "guidance"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/dnz7-ag8y",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-03",
+            "programCode": [
+                "021:036"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Railroad Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/dnz7-ag8y",
-            "description": "Report Filter Definitions and Guidance\r\nPlease note that all filter options are present in the dataset. For example, if you are looking at a dataset and a state is missing, it means there is no data for the year selected in that state - it does not use a list of all US states. \r\nAlso note that if the data table disappears, there is no data available for the filter selections made.",
-            "title": "Glossary of Report Filters",
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
+            "title": "Glossary of Report Filters"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:36"
             ],
-            "landingPage": "https://data.transportation.gov/d/dpf9-883g",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NTD Program Support",
+                "hasEmail": "mailto:NTDHelp@dot.gov"
+            },
+            "description": "A national summary of Federal Funding Allocation data reported by transit agencies to the National Transit Database (NTD) in Report Year 2023.\r\n\r\nNTD Data Summaries organize and summarize data from the 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. \r\n\r\nThis summary is based on the 2023 Federal Funding Allocation database file on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
+            "identifier": "https://data.transportation.gov/api/views/dpf9-883g",
             "issued": "2024-10-17",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-17",
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
+            "landingPage": "https://data.transportation.gov/d/dpf9-883g",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-10-17",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Transit Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/dpf9-883g",
-            "description": "A national summary of Federal Funding Allocation data reported by transit agencies to the National Transit Database (NTD) in Report Year 2023.\r\n\r\nNTD Data Summaries organize and summarize data from the 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. \r\n\r\nThis summary is based on the 2023 Federal Funding Allocation database file on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
-            "title": "2023 NTD Data Summary - Federal Funding Allocation",
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "2023 NTD Data Summary - Federal Funding Allocation"
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
-            "landingPage": "https://data.transportation.gov/d/dqb3-ktks",
-            "issued": "2002-01-01",
-            "temporal": "R/2002-01-31/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-05",
+            "categoryDesignation": "Research",
             "collectionInstrument": "http://www.ntdprogram.gov/ntdprogram/safety.htm",
-            "references": [
-                "http://www.ntdprogram.gov/ntdprogram/safety.htm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John D. Giorgis",
+                "hasEmail": "mailto:john.giorgis@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Summary (\"count\") data submitted to the Safety & Security Module of the NTD.   Reflects counts of incidents, fatalities, injuries, fires, collisions, etc.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/pubs/MonthlyData/S&STimeSeries-September2015-160104.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Safety & Security Time Series Data"
+                }
             ],
+            "identifier": "22.5",
+            "isPartOf": "DOT-22",
+            "issued": "2002-01-01",
             "keyword": [
                 "bicyclist",
                 "collision",
@@ -43093,57 +43108,60 @@
                 "transit",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John D. Giorgis",
-                "hasEmail": "mailto:john.giorgis@dot.gov"
-            },
-            "identifier": "22.5",
+            "landingPage": "https://data.transportation.gov/d/dqb3-ktks",
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
-            "title": "NTD Safety & Security Summary Data Set - Safety & Security Time Series Data",
-            "isPartOf": "DOT-22",
-            "agencyProgramURL": "http://www.ntdprogram.gov/",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/pubs/MonthlyData/S&STimeSeries-September2015-160104.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "Safety & Security Time Series Data"
-                }
+            "references": [
+                "http://www.ntdprogram.gov/ntdprogram/safety.htm"
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
+            "title": "NTD Safety & Security Summary Data Set - Safety & Security Time Series Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/dqvg-6cx9",
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
+                    "description": "2012 Delaware HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/delaware2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Delaware"
+                }
+            ],
+            "identifier": "678.61",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -43157,60 +43175,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.61",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Delaware",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/dqvg-6cx9",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/delaware2012.zip",
-                    "description": "2012 Delaware HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Delaware"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Delaware"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://safer.fmcsa.dot.gov/",
+            "agencyProgramURL": "http://safer.fmcsa.dot.gov/",
+            "analysisUnit": "Motor Carriers",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/dr8u-v9z2",
-            "issued": "2000-01-01",
-            "temporal": "R/1974-06-01/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://safer.fmcsa.dot.gov/"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The FMCSA Safety and Fitness Electronic Records (SAFER) System offers company safety data and related services to industry and the public over the Internet. Users can search FMCSA databases, register for a USDOT number, pay fines online, order company safety profiles, challenge FMCSA data using the DataQs system, access the Hazardous Material Route registry, obtain National Crash and Out of Service rates for Hazmat Permit Registration, get printable registration forms and find information about other FMCSA Information Systems.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://safer.fmcsa.dot.gov/",
+                    "mediaType": "text/html",
+                    "title": "SAFER Front Page"
+                }
             ],
+            "identifier": "121.2",
+            "isPartOf": "DOT-121",
+            "issued": "2000-01-01",
             "keyword": [
                 "bus",
                 "company safety profile.",
@@ -43225,64 +43240,39 @@
                 "safersys",
                 "safety and fitness electronic records"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "121.2",
+            "landingPage": "https://data.transportation.gov/d/dr8u-v9z2",
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
-            "description": "The FMCSA Safety and Fitness Electronic Records (SAFER) System offers company safety data and related services to industry and the public over the Internet. Users can search FMCSA databases, register for a USDOT number, pay fines online, order company safety profiles, challenge FMCSA data using the DataQs system, access the Hazardous Material Route registry, obtain National Crash and Out of Service rates for Hazmat Permit Registration, get printable registration forms and find information about other FMCSA Information Systems.",
-            "title": "Safety and Fitness Electronic Records (SAFER) - SAFER Front Page",
-            "isPartOf": "DOT-121",
-            "agencyProgramURL": "http://safer.fmcsa.dot.gov/",
-            "programCode": [
-                "021:026"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safer.fmcsa.dot.gov/",
-                    "mediaType": "text/html",
-                    "title": "SAFER Front Page"
-                }
+            "references": [
+                "http://safer.fmcsa.dot.gov/"
             ],
             "spatial": "National, State, Business Addresses",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://safer.fmcsa.dot.gov/",
+            "temporal": "R/1974-06-01/P1D",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Motor Carriers",
-            "phone": "202-493-0215",
-            "language": [
-                "en-US"
-            ]
+            "title": "Safety and Fitness Electronic Records (SAFER) - SAFER Front Page"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/dri9-7c4y",
-            "issued": "2024-12-22",
             "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA MCMIS",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/dri9-7c4y",
             "description": "The FMCSA Safety Measurement System (SMS) data, consists of active Intrastate Non-Hazmat Motor Carriers of passengers only. File is\ncomma delimited. One carrier per row.",
-            "title": "SMS EXTRACT INTRA PASS",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43290,72 +43280,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/dri9-7c4y/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dri9-7c4y/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dri9-7c4y/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/dri9-7c4y/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dri9-7c4y/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dri9-7c4y/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/dri9-7c4y/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dri9-7c4y/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dri9-7c4y/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/dri9-7c4y",
+            "issued": "2024-12-22",
+            "landingPage": "https://data.transportation.gov/d/dri9-7c4y",
             "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2025-02-01",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
             "theme": [
                 "Trucking and Motorcoaches"
-            ]
+            ],
+            "title": "SMS EXTRACT INTRA PASS"
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
-            "landingPage": "https://data.transportation.gov/d/drpd-mddr",
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
-            "identifier": "303.1",
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
@@ -43363,60 +43341,60 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "303.1",
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
+            "landingPage": "https://data.transportation.gov/d/drpd-mddr",
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
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www.nhtsa.gov/Research/Databases+and+Software/NHTSA+Test+Reference+Guides",
+            "agencyProgramURL": "http://www.nhtsa.gov/Research",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/dryv-xvf9",
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
-            "identifier": "1840.10",
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
@@ -43425,34 +43403,62 @@
                     "title": "Query by barrier parameters"
                 }
             ],
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/veh/vehdb-export-fields.htm",
-            "dataQuality": true,
+            "identifier": "1840.10",
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
+            "landingPage": "https://data.transportation.gov/d/dryv-xvf9",
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
-            "landingPage": "https://data.transportation.gov/d/dsgr-arn8",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2020-12-30",
-            "@type": "dcat:Dataset",
-            "temporal": "2018-09-24/2020-06-22",
-            "modified": "2020-12-30",
-            "references": [
-                "https://rosap.ntl.bts.gov/view/dot/50751",
-                "https://rosap.ntl.bts.gov/view/dot/54774"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kate Hartman",
+                "hasEmail": "mailto:kate.hartman@dot.gov"
+            },
+            "description": "This dataset contains raw Signal Phasing and Timing (SPaT), MAP, and Basic Safety Messages (BSM) data from the \"Feasibility Study and Assessment of Communications Approaches for Real-Time Traffic Signal Applications\" project in the hexadecimal string and pcap formats. The project characterizes and assesses the feasibility of SPaT messages for infrastructure-based safety applications by comparing messages received through cellular networks with those received through Dedicated Short Range Communication (DSRC).\n\nThis dataset contains the raw research data collected for the project. The project's final report and supporting dataset can be found at the National Transportation Library and is linked in the references section of this dataset.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/download/dsgr-arn8/application/pdf",
+                    "mediaType": "application/pdf"
+                }
             ],
+            "identifier": "https://data.transportation.gov/api/views/dsgr-arn8",
+            "issued": "2020-12-30",
             "keyword": [
                 "basic safety message (bsm)",
                 "cellular",
@@ -43465,81 +43471,92 @@
                 "virginia connected corridor (vcc)",
                 "virginia department of transportation (vdot)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/dsgr-arn8",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-30",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Department of Transportation"
             },
-            "identifier": "https://data.transportation.gov/api/views/dsgr-arn8",
-            "description": "This dataset contains raw Signal Phasing and Timing (SPaT), MAP, and Basic Safety Messages (BSM) data from the \"Feasibility Study and Assessment of Communications Approaches for Real-Time Traffic Signal Applications\" project in the hexadecimal string and pcap formats. The project characterizes and assesses the feasibility of SPaT messages for infrastructure-based safety applications by comparing messages received through cellular networks with those received through Dedicated Short Range Communication (DSRC).\n\nThis dataset contains the raw research data collected for the project. The project's final report and supporting dataset can be found at the National Transportation Library and is linked in the references section of this dataset.",
-            "title": "Feasibility Study and Assessment of Communications Approaches for Real-Time Traffic Signal Applications Study Data",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/download/dsgr-arn8/application/pdf",
-                    "mediaType": "application/pdf"
-                }
+            "references": [
+                "https://rosap.ntl.bts.gov/view/dot/50751",
+                "https://rosap.ntl.bts.gov/view/dot/54774"
             ],
             "spatial": "Route 7 and Springhill Rd, Gallows Rd at Yorktowne and Route 50 corridor in Northern Virginia region",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2018-09-24/2020-06-22",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "Feasibility Study and Assessment of Communications Approaches for Real-Time Traffic Signal Applications Study Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/dsuf-xcni",
             "bureauCode": [
                 "021:27"
             ],
-            "issued": "2024-12-18",
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
-            "identifier": "https://data.transportation.gov/api/views/dsuf-xcni",
+            "dataQuality": true,
             "description": "This is the Rail Safety Overview Report (1.12), which contains summary level train accidents, highway-rail incidents, casualty and operational data.",
-            "title": "Rail Safety Overview Report (1.12)",
+            "identifier": "https://data.transportation.gov/api/views/dsuf-xcni",
+            "issued": "2024-12-18",
+            "landingPage": "https://data.transportation.gov/d/dsuf-xcni",
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
+            "title": "Rail Safety Overview Report (1.12)"
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
-            "landingPage": "https://data.transportation.gov/d/dsv2-cvt5",
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
+            "identifier": "83.8",
+            "isPartOf": "DOT-83",
+            "issued": "2002-12-16",
             "keyword": [
                 "air bag",
                 "air bags",
@@ -43566,58 +43583,46 @@
                 "vin",
                 "vin search"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "83.8",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Manufacturers who determine that a product or piece of original equipment either has a safety defect or is not in compliance with Federal safety standards are required to notify the National Highway Traffic Safety Administration (NHTSA) within 5 business days. NHTSA requires that manufacturers file a Defect and Noncompliance report as well as quarterly recall status reports, in compliance with Federal Regulation 49 (the National Traffic and Motor Safety Act) Part 573, which identifies the requirements for safety recalls. This information is stored in the NHTSA database. Use this data to search for recall information related to:-\tSpecific NHTSA campaigns -\tProduct types Access to public searches of NHTSA recall databases for tires, vehicles, car seats and equipment.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - Recalls - Safety Issues for Vehicles, Child Restraints, Tires, and Equipment.",
-            "isPartOf": "DOT-83",
-            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
-            "describedByType": "text/plain",
+            "landingPage": "https://data.transportation.gov/d/dsv2-cvt5",
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
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/dtcu-5apw",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRA Safety Data Team",
+                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This is the page for Train Accident (not at Highway-Rail Crossings) Summary (2.03).",
+            "identifier": "https://data.transportation.gov/api/views/dtcu-5apw",
             "issued": "2024-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "collision",
                 "derailment",
@@ -43625,38 +43630,51 @@
                 "train",
                 "train accident"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRA Safety Data Team",
-                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/dtcu-5apw",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-27",
+            "programCode": [
+                "FRA Safety and Operations"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Railroad Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/dtcu-5apw",
-            "description": "This is the page for Train Accident (not at Highway-Rail Crossings) Summary (2.03).",
-            "title": "Train Accident (not at Highway-Rail Crossings) Summary (2.03)",
-            "programCode": [
-                "FRA Safety and Operations"
-            ],
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Train Accident (not at Highway-Rail Crossings) Summary (2.03)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/dtv4-kbqh",
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
+                    "description": "2012 Maine HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/maine2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Maine"
+                }
+            ],
+            "identifier": "678.73",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -43670,86 +43688,41 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.73",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Maine",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/dtv4-kbqh",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/maine2012.zip",
-                    "description": "2012 Maine HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Maine"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Maine"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/dusd-cr84",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2018-12-13",
-            "temporal": "2018-05-21/2018-09-19",
-            "@type": "dcat:Dataset",
-            "modified": "2018-12-13",
-            "keyword": [
-                "automated lane change and merge",
-                "closed track testing",
-                "cooperative automated driving system (cads)",
-                "cooperative automated research mobility applications (carma) platform",
-                "dedicated short range communication (dsrc)",
-                "integrated highway prototype",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "sae level 1",
-                "speed harmonization",
-                "vehicle platooning",
-                "vehicle to infrastructure (v2i)",
-                "vehicle to vehicle (v2v)"
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
-            "identifier": "https://data.transportation.gov/api/views/dusd-cr84",
+            "dataQuality": true,
             "description": "Data represent the performance of prototype cooperative automated driving system applications for improving traffic mobility. The applications include the integrated highway prototype that consists of vehicle platooning, speed harmonization, and automated lane change and merge.",
-            "title": "Cooperative Automated Research Mobility Applications (CARMA) 2",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43757,51 +43730,93 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/dusd-cr84/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dusd-cr84/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dusd-cr84/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/dusd-cr84/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dusd-cr84/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dusd-cr84/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/dusd-cr84/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dusd-cr84/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dusd-cr84/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/dusd-cr84",
+            "issued": "2018-12-13",
+            "keyword": [
+                "automated lane change and merge",
+                "closed track testing",
+                "cooperative automated driving system (cads)",
+                "cooperative automated research mobility applications (carma) platform",
+                "dedicated short range communication (dsrc)",
+                "integrated highway prototype",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "sae level 1",
+                "speed harmonization",
+                "vehicle platooning",
+                "vehicle to infrastructure (v2i)",
+                "vehicle to vehicle (v2v)"
+            ],
+            "landingPage": "https://data.transportation.gov/d/dusd-cr84",
+            "language": [
+                "english"
+            ],
             "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "irregular",
+            "modified": "2018-12-13",
+            "programCode": [
+                "021:013"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "USDOT"
+            },
+            "temporal": "2018-05-21/2018-09-19",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "english"
-            ]
+            "title": "Cooperative Automated Research Mobility Applications (CARMA) 2"
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
-            "landingPage": "https://data.transportation.gov/d/duxv-wci3",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/04octtvt/04octtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "October 2004"
+                }
             ],
+            "identifier": "18.119",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -43811,83 +43826,51 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.119",
+            "landingPage": "https://data.transportation.gov/d/duxv-wci3",
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
-            "title": "Monthly Traffic Volume Trends - October 2004",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/04octtvt/04octtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "October 2004"
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
+            "title": "Monthly Traffic Volume Trends - October 2004"
         },
         {
-            "accessLevel": "public",
-            "bureauCode": [
-                "021:04"
-            ],
-            "landingPage": "https://data.transportation.gov/d/dvgi-kux7",
-            "issued": "2013-02-01",
-            "temporal": "R/2012-01-01/P1Y",
-            "@type": "dcat:Dataset",
-            "collectionInstrument": "Transportation",
-            "modified": "2024-11-14",
-            "references": [
-                "http://www.justice.gov/oip/docs/doj-handbook-for-agency-annual-freedom-of-information-act-reports.pdf"
-            ],
-            "keyword": [
-                "backlog",
-                "freedom of information act",
-                "requests"
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.dot.gov/individuals/foia/dot-annual-foia-reports-congress",
+            "agencyProgramURL": "http://www.dot.gov/foia",
+            "analysisUnit": "FOIA Request",
+            "bureauCode": [
+                "021:04"
             ],
+            "categoryDesignation": "Research",
+            "collectionInstrument": "Transportation",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "372.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
-            "description": "The FOIA requires each federal agency to submit an Annual Report to the Attorney General each year. These reports contain detailed statistics on the numbers of requests received and processed by each agency, the time taken to respond, and the outcome of each request, as well as many other vital statistics regarding the administration of the FOIA at federal departments and agencies.",
-            "title": "Freedom of Information Act Annual Report - 2013 Report",
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
@@ -43896,55 +43879,54 @@
                     "title": "2013 Report"
                 }
             ],
-            "spatial": "not applicable",
-            "describedBy": "http://www.justice.gov/oip/docs/doj-handbook-for-agency-annual-freedom-of-information-act-reports.pdf",
-            "dataQuality": true,
+            "identifier": "372.2",
+            "isPartOf": "DOT-372",
+            "issued": "2013-02-01",
+            "keyword": [
+                "backlog",
+                "freedom of information act",
+                "requests"
+            ],
+            "landingPage": "https://data.transportation.gov/d/dvgi-kux7",
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
+            "title": "Freedom of Information Act Annual Report - 2013 Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "This system houses software requirements. The information contained is documented at the system level and may contain IT Security Sensitive information.",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/dwpu-mwp9",
-            "issued": "2014-12-15",
-            "temporal": "R/2014-12-15/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-31",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "change request",
-                "configuration management",
-                "scr"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO",
                 "hasEmail": "mailto:fmcsa.cdo@dot.gov"
             },
-            "identifier": "1640.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": false,
             "description": "Borland StarTeam (now owned by Micro Focus) is the FMCSA Change Management tool for IT systems.",
-            "title": "Borland StarTeam -",
-            "primaryITInvestmentUII": "021-000001018",
-            "programCode": [
-                "021:022"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -43952,64 +43934,100 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "1640.0",
+            "issued": "2014-12-15",
+            "keyword": [
+                "change request",
+                "configuration management",
+                "scr"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/dwpu-mwp9",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-6830"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-31",
+            "phone": "202-366-6830",
+            "primaryITInvestmentUII": "021-000001018",
+            "programCode": [
+                "021:022"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "rights": "This system houses software requirements. The information contained is documented at the system level and may contain IT Security Sensitive information.",
+            "temporal": "R/2014-12-15/P1Y",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Borland StarTeam -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/dwrv-9qyx",
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
-            "identifier": "https://data.transportation.gov/api/views/dwrv-9qyx",
             "description": "Fixed route bus includes commuter bus, motor bus, bus rapid transit, and trolleybus. The Federal Highway Administration estimates monthly transit ridership, released as part of the National Transit Database. Ridership estimates have been adjusted to account for changes in data collection over time. Starting in January 2012, data for Small System Waiver agencies that do not have a mode are reported under motor bus. Data reported under hybrid rail are reported under their classifications prior to January 2012.",
-            "title": "Transit Ridership - Fixed Route Bus",
+            "identifier": "https://data.transportation.gov/api/views/dwrv-9qyx",
+            "issued": "2025-01-15",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/dwrv-9qyx",
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
+            "title": "Transit Ridership - Fixed Route Bus"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/dwsf-u9iq",
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
+                    "description": "2012 West Virginia HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/westvirginia2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 West Virginia"
+                }
+            ],
+            "identifier": "678.102",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -44023,85 +44041,46 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.102",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 West Virginia",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/dwsf-u9iq",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/westvirginia2012.zip",
-                    "description": "2012 West Virginia HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 West Virginia"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 West Virginia"
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
-            "landingPage": "https://data.transportation.gov/d/dwwy-43gt",
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
-            "identifier": "524.8",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
             "description": "STATE DATA REPORTING SYSTEMS. Annual reports on the Fatality Analysis Reporting System (FARS) which is data regarding fatalities that is collected by a FARS analyst from each State and provided to NHTSA.",
-            "title": "GES Reports - 2006",
-            "isPartOf": "DOT-524",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44110,61 +44089,61 @@
                     "title": "2006"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
-            "dataQuality": true,
+            "identifier": "524.8",
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
+            "landingPage": "https://data.transportation.gov/d/dwwy-43gt",
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
+            "title": "GES Reports - 2006"
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
-            "landingPage": "https://data.transportation.gov/d/dx3v-id89",
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
-            "identifier": "557.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
+            "describedBy": "https://www.civilrights.dot.gov/node/3828",
             "description": "Data related to the management of EEO complaint processing.  Due to the presence of PII, the raw data is not available for public consumption.  However, aggregated data is available in the DOT's NoFEAR Act report and Form 462 Report.  Both are located on the DOT Office of Civil Rights' public website.",
-            "title": "EEO Complaint Processing Data - DOT-wide No FEAR Data",
-            "isPartOf": "DOT-557",
-            "agencyProgramURL": "http://www.civilrights.dot.gov",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44173,35 +44152,70 @@
                     "title": "DOT-wide No FEAR Data"
                 }
             ],
-            "describedBy": "https://www.civilrights.dot.gov/node/3828",
-            "dataQuality": false,
+            "identifier": "557.2",
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
+            "landingPage": "https://data.transportation.gov/d/dx3v-id89",
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
+            "title": "EEO Complaint Processing Data - DOT-wide No FEAR Data"
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
-            "landingPage": "https://data.transportation.gov/d/dxqq-yjrs",
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
+                    "downloadURL": "https://cms.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/docs/closedByEnforcement_FY2010_04-26-2013.xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Fiscal Year 2010"
+                }
             ],
+            "identifier": "DOT-96",
+            "issued": "2018-12-17",
             "keyword": [
                 "bus",
                 "civil penalties",
@@ -44214,59 +44228,61 @@
                 "motor carrier",
                 "truck"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "DOT-96",
+            "landingPage": "https://data.transportation.gov/d/dxqq-yjrs",
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
-            "title": "Closed Enforcement Cases",
-            "agencyProgramURL": "http://www.fmcsa.dot.gov/regulations/enforcement/civil-penalties",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://cms.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/docs/closedByEnforcement_FY2010_04-26-2013.xlsx",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "Fiscal Year 2010"
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
-            "analysisUnit": "Enforcement Case",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4869",
-            "language": [
-                "en-US"
-            ]
+            "title": "Closed Enforcement Cases"
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
-            "landingPage": "https://data.transportation.gov/d/dyvj-fjut",
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
+            "identifier": "287.1",
+            "isPartOf": "DOT-287",
+            "issued": "1992-01-01",
             "keyword": [
                 "air",
                 "area",
@@ -44287,59 +44303,61 @@
                 "quality",
                 "voc"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "287.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "All 50 states and the District of Columbia submit annual reports of their CMAQ project obligations in March of   every year. The FHWA uses these yearly submissions to maintain an active database of CMAQ investments, trends within the program, and other anecdotal information focusing on the program's performance. This   database of CMAQ Project information has always been reserved for internal use by authorized FHWA personnel for Congressional reporting and made available to state DOTs and MPOs on a limited basis.",
-            "title": "Congestion Mitigation and Air Quality (CMAQ) - Public Access System",
-            "isPartOf": "DOT-287",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/environment/air_quality/cmaq/",
+            "landingPage": "https://data.transportation.gov/d/dyvj-fjut",
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
+            "title": "Congestion Mitigation and Air Quality (CMAQ) - Public Access System"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Project",
-            "phone": "202-366-2076",
-            "language": [
-                "en-US"
-            ]
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
+                    "description": "2012 Iowa HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/iowa2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Iowa"
+                }
             ],
-            "landingPage": "https://data.transportation.gov/d/dz2t-d58r",
+            "identifier": "678.69",
+            "isPartOf": "DOT-678",
             "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
-            "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
             "keyword": [
                 "aadt",
                 "condition",
@@ -44353,57 +44371,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.69",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Iowa",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/dz2t-d58r",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/iowa2012.zip",
-                    "description": "2012 Iowa HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Iowa"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Iowa"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/dz3j-zsfr",
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
+                    "description": "2011 West Virginia HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/westvirginia2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 West Virginia"
+                }
+            ],
+            "identifier": "678.50",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -44417,77 +44435,40 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.50",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 West Virginia",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/dz3j-zsfr",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/westvirginia2011.zip",
-                    "description": "2011 West Virginia HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 West Virginia"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 West Virginia"
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
-            "identifier": "https://data.transportation.gov/api/views/dzuk-qpr3",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 1998",
-            "title": "Historic HPMS Data (Universe) - 1998",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44495,50 +44476,84 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/dzuk-qpr3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dzuk-qpr3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dzuk-qpr3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/dzuk-qpr3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dzuk-qpr3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dzuk-qpr3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/dzuk-qpr3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/dzuk-qpr3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/dzuk-qpr3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/dzuk-qpr3",
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
+            "title": "Historic HPMS Data (Universe) - 1998"
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
-            "landingPage": "https://data.transportation.gov/d/dzwy-vzbf",
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
+            "identifier": "122.2",
+            "isPartOf": "DOT-122",
+            "issued": "2000-01-01",
             "keyword": [
                 "bus",
                 "company safety profile",
@@ -44559,81 +44574,46 @@
                 "safety and fitness electronic records",
                 "safety rating"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "122.2",
+            "landingPage": "https://data.transportation.gov/d/dzwy-vzbf",
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
             "accessLevel": "non-public",
-            "rights": "The data set contains pre-decisional information.",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/e38n-zcuk",
-            "issued": "2014-10-24",
-            "temporal": "R/2013-01-01/P3M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "budget",
-                "operational plan",
-                "opplan",
-                "wcf",
-                "working capital fund"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "587.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
             "description": "This data set contains formulations for the DOT Working Capital Fund (WCF) budget, generated on a fiscal year basis. It also includes in-year revisions to the WCF budget (operational plans).",
-            "title": "Working Capital Fund Budget Data -",
-            "primaryITInvestmentUII": "021-172781355",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44641,53 +44621,54 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "theme": [
-                "Transportation"
+            "identifier": "587.0",
+            "issued": "2014-10-24",
+            "keyword": [
+                "budget",
+                "operational plan",
+                "opplan",
+                "wcf",
+                "working capital fund"
             ],
-            "accrualPeriodicity": "R/P3M",
-            "categoryDesignation": "Administrative",
+            "landingPage": "https://data.transportation.gov/d/e38n-zcuk",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-4331"
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-14",
+            "phone": "202-366-4331",
+            "primaryITInvestmentUII": "021-172781355",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "rights": "The data set contains pre-decisional information.",
+            "temporal": "R/2013-01-01/P3M",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Working Capital Fund Budget Data -"
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
-            "landingPage": "https://data.transportation.gov/d/e3es-bm8i",
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
-            "identifier": "696.6",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "A compilation of historic documents and articles on the Interstate System, Federal-Aid Highway Program, FHWA, and transportation.",
-            "title": "Highway History - Federal-Aid Legislation",
-            "isPartOf": "DOT-696",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/infrastructure/history.cfm",
-            "programCode": [
-                "021:011"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44696,37 +44677,46 @@
                     "title": "Federal-Aid Legislation"
                 }
             ],
-            "spatial": "National",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "696.6",
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
+            "landingPage": "https://data.transportation.gov/d/e3es-bm8i",
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
+            "title": "Highway History - Federal-Aid Legislation"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/e3ix-8sgi",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/e3ix-8sgi",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "SMT 2 - GENESEE & WYOMING",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44734,45 +44724,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/e3ix-8sgi/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/e3ix-8sgi/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/e3ix-8sgi/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/e3ix-8sgi/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/e3ix-8sgi/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/e3ix-8sgi/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/e3ix-8sgi/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/e3ix-8sgi/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/e3ix-8sgi/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/e3ix-8sgi",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/e3ix-8sgi",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "SMT 2 - GENESEE & WYOMING"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyProgramURL": "http://www.nhtsa.gov/fuel-economy",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/e3ty-vt2x",
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
+                    "description": "Credits are an earned or purchased allowance used to determine compliance within the CAFE program. Also available in PDF and XLS.",
+                    "downloadURL": "http://www.nhtsa.gov/CAFE_PIC/CAFE_PIC_Credit_LIVE.html",
+                    "mediaType": "text/html",
+                    "title": "Credit Status Report"
+                }
             ],
+            "identifier": "1862.6",
+            "isPartOf": "DOT-1862",
+            "issued": "2015-12-16",
             "keyword": [
                 "amfa",
                 "civil penalties",
@@ -44789,134 +44803,101 @@
                 "report",
                 "shortfall"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "1862.6",
+            "landingPage": "https://data.transportation.gov/d/e3ty-vt2x",
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
-            "title": "CAFE (Corporate Average Fuel Economy) - Credit Status Report",
-            "isPartOf": "DOT-1862",
-            "agencyProgramURL": "http://www.nhtsa.gov/fuel-economy",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.nhtsa.gov/CAFE_PIC/CAFE_PIC_Credit_LIVE.html",
-                    "description": "Credits are an earned or purchased allowance used to determine compliance within the CAFE program. Also available in PDF and XLS.",
-                    "@type": "dcat:Distribution",
-                    "title": "Credit Status Report"
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
+            "title": "CAFE (Corporate Average Fuel Economy) - Credit Status Report"
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
-            "landingPage": "https://data.transportation.gov/d/e54a-dum3",
-            "issued": "1998-12-24",
-            "temporal": "R/1998-12-14/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.nhtsa.gov/Research/Databases+and+Software/NHTSA+Test+Reference+Guides"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www-nrd.nhtsa.dot.gov/database/VSR/com/QueryTest.aspx",
+                    "mediaType": "text/html",
+                    "title": "Component Test Database Interactive Access"
+                }
             ],
+            "identifier": "364.16",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
             "keyword": [
                 "nhtsa crash test database",
                 "nhtsa vehicle crash test database"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "364.16",
+            "landingPage": "https://data.transportation.gov/d/e54a-dum3",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-01",
+            "phone": "202-366-4712",
+            "primaryITInvestmentUII": "021-621341357",
+            "programCode": [
+                "021:035"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Highway Traffic Safety Administration"
             },
-            "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database - Component Test Database Interactive Access",
-            "isPartOf": "DOT-364",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
-            "primaryITInvestmentUII": "021-621341357",
-            "programCode": [
-                "021:035"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www-nrd.nhtsa.dot.gov/database/VSR/com/QueryTest.aspx",
-                    "mediaType": "text/html",
-                    "title": "Component Test Database Interactive Access"
-                }
+            "references": [
+                "http://www.nhtsa.gov/Research/Databases+and+Software/NHTSA+Test+Reference+Guides"
             ],
             "spatial": "N/A",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.nhtsa.gov",
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
+            "title": "Vehicle Safety Research and Development Database - Component Test Database Interactive Access"
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
-            "identifier": "https://data.transportation.gov/api/views/e56t-hfa9",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 1987",
-            "title": "Historic HPMS Data (Universe) - 1987",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44924,74 +44905,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/e56t-hfa9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/e56t-hfa9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/e56t-hfa9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/e56t-hfa9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/e56t-hfa9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/e56t-hfa9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/e56t-hfa9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/e56t-hfa9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/e56t-hfa9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/e56t-hfa9",
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
+            "title": "Historic HPMS Data (Universe) - 1987"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/e5bn-vf7s",
+            "accrualPeriodicity": "R/PT20S",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2016-02-17",
-            "@type": "dcat:Dataset",
-            "temporal": "2015-01-12/2015-01-16",
-            "modified": "2016-02-17",
-            "keyword": [
-                "field test",
-                "freeway",
-                "i-5",
-                "intelligent network flow optimization (inflo)",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "prototype infrastructure traffic sensor (tss) system data aggregator",
-                "seattle",
-                "sensor data",
-                "washington",
-                "washington state department of transportation (wsdot)"
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
-            "identifier": "https://data.transportation.gov/api/views/e5bn-vf7s",
+            "dataQuality": true,
             "description": "Data is from the small-scale demonstration of the Intelligent Network Flow Optimization (INFLO) Prototype System and applications in Seattle, Washington. Connected vehicle systems were deployed in 21 vehicles in a scripted driving scenario circuiting this I-5 corridor northbound and southbound during morning rush hour. This data set contains real-time volume, speed and loop occupancy data that were collected from WSDOT\u2019s simulated roadway sensors every 20 seconds and aggregated according to user defined procedures and threshold by the Infrastructure Traffic Sensor System (TSS) Data Aggregator software.",
-            "title": "Intelligent Network Flow Optimization Prototype Infrastructure Traffic Sensor System Data Aggregator",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -44999,75 +44974,75 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/e5bn-vf7s/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/e5bn-vf7s/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/e5bn-vf7s/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/e5bn-vf7s/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/e5bn-vf7s/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/e5bn-vf7s/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/e5bn-vf7s/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/e5bn-vf7s/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/e5bn-vf7s/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Seattle, Washington",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/e5bn-vf7s",
+            "issued": "2016-02-17",
+            "keyword": [
+                "field test",
+                "freeway",
+                "i-5",
+                "intelligent network flow optimization (inflo)",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "prototype infrastructure traffic sensor (tss) system data aggregator",
+                "seattle",
+                "sensor data",
+                "washington",
+                "washington state department of transportation (wsdot)"
+            ],
+            "landingPage": "https://data.transportation.gov/d/e5bn-vf7s",
+            "language": [
+                "en-US"
+            ],
             "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "R/PT20S",
+            "modified": "2016-02-17",
+            "programCode": [
+                "021:013"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
+            "spatial": "Seattle, Washington",
+            "temporal": "2015-01-12/2015-01-16",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Intelligent Network Flow Optimization Prototype Infrastructure Traffic Sensor System Data Aggregator"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/e5cn-ri8q",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-05-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-21",
-            "keyword": [
-                "diesel",
-                "fuel",
-                "fuel tax",
-                "gashol",
-                "gasoline",
-                "highways",
-                "highway trust fund",
-                "liquefied petroleum",
-                "motor fuel",
-                "roadways",
-                "state"
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
-            "identifier": "https://data.transportation.gov/api/views/e5cn-ri8q",
             "description": "Tax rates on motor fuel by type and state from the U.S. Department of Transportation's Federal Highway Administrations' Monthly Motor Fuel Report, available at: https://www.fhwa.dot.gov/policyinformation/motorfuelhwy_trustfund.cfm\n\nAll States levy volume taxes on gasoline and diesel fuel. Traditionally, State fuel tax rates could only be changed with legislation, but as of 2021, 10 States have variable rate motor fuel taxes. These taxes are adjusted at specified intervals annually, semi-annually, or quarterly. Adjustments to variable tax rates are announced by State tax agencies shortly before the effective date of the change. \n\nThe fuel tax rate is collected annually and therefore the semi-annual and quarterly adjustments are not captured in the data.",
-            "title": "Tax Rates by Motor Fuel and State",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45075,48 +45050,88 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/e5cn-ri8q/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/e5cn-ri8q/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/e5cn-ri8q/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/e5cn-ri8q/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/e5cn-ri8q/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/e5cn-ri8q/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/e5cn-ri8q/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/e5cn-ri8q/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/e5cn-ri8q/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/e5cn-ri8q",
+            "issued": "2024-05-13",
+            "keyword": [
+                "diesel",
+                "fuel",
+                "fuel tax",
+                "gashol",
+                "gasoline",
+                "highways",
+                "highway trust fund",
+                "liquefied petroleum",
+                "motor fuel",
+                "roadways",
+                "state"
+            ],
+            "landingPage": "https://data.transportation.gov/d/e5cn-ri8q",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
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
+            "title": "Tax Rates by Motor Fuel and State"
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
-            "landingPage": "https://data.transportation.gov/d/e5qb-p9gu",
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
+                    "mediaType": "application/xml",
+                    "title": "New Car Assessment Program (NCAP) - 5 Star Safety Ratings"
+                }
             ],
+            "identifier": "248.2",
+            "isPartOf": "DOT-248",
+            "issued": "2010-01-05",
             "keyword": [
                 "5",
                 "assessment",
@@ -45130,60 +45145,61 @@
                 "safety",
                 "star"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "248.2",
+            "landingPage": "https://data.transportation.gov/d/e5qb-p9gu",
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
-                    "mediaType": "application/xml",
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
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/on_the_fly_download.aspx",
+            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
+            "analysisUnit": "Form 54 Filing",
             "bureauCode": [
                 "021:27"
             ],
-            "landingPage": "https://data.transportation.gov/d/e5vm-43rk",
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
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/incrpt.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Accident Detail Report"
+                }
             ],
+            "identifier": "199.17",
+            "isPartOf": "DOT-199",
+            "issued": "2010-09-29",
             "keyword": [
                 "acts of god",
                 "collisions",
@@ -45194,83 +45210,49 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "199.17",
+            "landingPage": "https://data.transportation.gov/d/e5vm-43rk",
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
-            "title": "Rail Equipment Accidents - Accident Detail Report",
-            "isPartOf": "DOT-199",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:036"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/incrpt.aspx",
-                    "mediaType": "text/csv",
-                    "title": "Accident Detail Report"
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
+            "title": "Rail Equipment Accidents - Accident Detail Report"
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
-            "landingPage": "https://data.transportation.gov/d/e5xm-fdw6",
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
-            "identifier": "364.18",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database - Component Test Database Export",
-            "isPartOf": "DOT-364",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
-            "primaryITInvestmentUII": "021-621341357",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45279,32 +45261,68 @@
                     "title": "Component Test Database Export"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.18",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/e5xm-fdw6",
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
+            "title": "Vehicle Safety Research and Development Database - Component Test Database Export"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/e799-n54r",
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
+                    "description": "2011 Rhode Island HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/rhodeisland2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Rhode Island"
+                }
+            ],
+            "identifier": "678.41",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -45318,55 +45336,42 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.41",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Rhode Island",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/e799-n54r",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/rhodeisland2011.zip",
-                    "description": "2011 Rhode Island HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Rhode Island"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Rhode Island"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/e7jy-zh35",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRA Safety Data Team",
+                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This is the page for Accident Track Type by Railroad.",
+            "identifier": "https://data.transportation.gov/api/views/e7jy-zh35",
             "issued": "2024-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "collision",
                 "derailment",
@@ -45374,40 +45379,47 @@
                 "train",
                 "train accident"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRA Safety Data Team",
-                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/e7jy-zh35",
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
                 "name": "US Department of Transportation"
             },
-            "identifier": "https://data.transportation.gov/api/views/e7jy-zh35",
-            "description": "This is the page for Accident Track Type by Railroad.",
-            "title": "Accident Track Type by Railroad",
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
+            "title": "Accident Track Type by Railroad"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/e8av-qz9y",
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
+            "description": "The Trajectory Conversion Algorithm Version 2.3 (TCA) is designed to test different strategies for producing, transmitting, and storing Connected Vehicle information. The TCA uses vehicle trajectory data, roadside equipment (RSE) location information, cellular region information and strategy information to emulate the messages connected vehicles would produce. This data set contains common data sets generated by the TCA using the BSM and PDM at 100% market penetration for two simulated traffic networks, an arterial network (Van Ness Avenue in San Francisco, CA) and a freeway network (the interchange of I-270 and I-44 in St. Louis, MO).\r\n\r\nThis legacy dataset was created before data.transportation.gov and is only currently available via the attached file(s). Please contact the dataset owner if there is a need for users to work with this data using the data.transportation.gov analysis features (online viewing, API, graphing, etc.) and the USDOT will consider modifying the dataset to fully integrate in data.transportation.gov.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/download/e8av-qz9y/application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/e8av-qz9y",
             "issued": "2016-01-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2016-03-28/2016-03-28",
-            "modified": "2016-01-01",
             "keyword": [
                 "arterial",
                 "basic safety message (bsm)",
@@ -45427,57 +45439,35 @@
                 "trajectory conversion algorithm (tca)",
                 "vissim"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/e8av-qz9y",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
+            "modified": "2016-01-01",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Department of Transportation"
             },
-            "identifier": "https://data.transportation.gov/api/views/e8av-qz9y",
-            "description": "The Trajectory Conversion Algorithm Version 2.3 (TCA) is designed to test different strategies for producing, transmitting, and storing Connected Vehicle information. The TCA uses vehicle trajectory data, roadside equipment (RSE) location information, cellular region information and strategy information to emulate the messages connected vehicles would produce. This data set contains common data sets generated by the TCA using the BSM and PDM at 100% market penetration for two simulated traffic networks, an arterial network (Van Ness Avenue in San Francisco, CA) and a freeway network (the interchange of I-270 and I-44 in St. Louis, MO).\r\n\r\nThis legacy dataset was created before data.transportation.gov and is only currently available via the attached file(s). Please contact the dataset owner if there is a need for users to work with this data using the data.transportation.gov analysis features (online viewing, API, graphing, etc.) and the USDOT will consider modifying the dataset to fully integrate in data.transportation.gov.",
-            "title": "Basic Safety Message Data Emulator",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/download/e8av-qz9y/application/vnd.openxmlformats-officedocument.wordprocessingml.document",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
-                }
-            ],
             "spatial": "Van Ness, California; St. Louis, Missouri",
-            "dataQuality": true,
-            "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "irregular",
+            "temporal": "2016-03-28/2016-03-28",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Basic Safety Message Data Emulator"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/e8e5-ygyu",
-            "issued": "2023-02-04",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/e8e5-ygyu",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "KCS",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45485,45 +45475,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/e8e5-ygyu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/e8e5-ygyu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/e8e5-ygyu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/e8e5-ygyu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/e8e5-ygyu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/e8e5-ygyu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/e8e5-ygyu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/e8e5-ygyu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/e8e5-ygyu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/e8e5-ygyu",
+            "issued": "2023-02-04",
+            "landingPage": "https://data.transportation.gov/d/e8e5-ygyu",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "KCS"
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
-            "landingPage": "https://data.transportation.gov/d/e8hh-fkbb",
-            "issued": "2002-01-01",
-            "temporal": "R/2002-01-31/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-05",
+            "categoryDesignation": "Research",
             "collectionInstrument": "http://www.ntdprogram.gov/ntdprogram/safety.htm",
-            "references": [
-                "http://www.ntdprogram.gov/ntdprogram/safety.htm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John D. Giorgis",
+                "hasEmail": "mailto:john.giorgis@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Summary (\"count\") data submitted to the Safety & Security Module of the NTD.   Reflects counts of incidents, fatalities, injuries, fires, collisions, etc.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/pubs/MonthlyData/S&STimeSeriesDecember2011-04032012.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Major Only Time Series"
+                }
             ],
+            "identifier": "22.2",
+            "isPartOf": "DOT-22",
+            "issued": "2002-01-01",
             "keyword": [
                 "bicyclist",
                 "collision",
@@ -45542,60 +45557,61 @@
                 "transit",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John D. Giorgis",
-                "hasEmail": "mailto:john.giorgis@dot.gov"
-            },
-            "identifier": "22.2",
+            "landingPage": "https://data.transportation.gov/d/e8hh-fkbb",
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
-            "title": "NTD Safety & Security Summary Data Set - Major Only Time Series",
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
-                    "title": "Major Only Time Series"
-                }
+            "references": [
+                "http://www.ntdprogram.gov/ntdprogram/safety.htm"
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
+            "title": "NTD Safety & Security Summary Data Set - Major Only Time Series"
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
-            "landingPage": "https://data.transportation.gov/d/e8in-8yra",
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
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2011_database/NTD_database_2011.exe",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2011 Database"
+                }
             ],
+            "identifier": "21.15",
+            "isPartOf": "DOT-21",
+            "issued": "2010-10-01",
             "keyword": [
                 "agency",
                 "allocation",
@@ -45614,58 +45630,60 @@
                 "urbanized",
                 "vehicles"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John D. Giorgis",
-                "hasEmail": "mailto:john.giorgis@dot.gov"
-            },
-            "identifier": "21.15",
+            "landingPage": "https://data.transportation.gov/d/e8in-8yra",
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
-            "title": "NTD Annual Module Data Set - 2011 Database",
-            "isPartOf": "DOT-21",
-            "agencyProgramURL": "http://www.ntdprogram.gov",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2011_database/NTD_database_2011.exe",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "2011 Database"
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
+            "title": "NTD Annual Module Data Set - 2011 Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/e99u-gpib",
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
+                    "description": "2012 Kansas HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/kansas2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Kansas"
+                }
+            ],
+            "identifier": "678.70",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -45679,81 +45697,46 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.70",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Kansas",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/e99u-gpib",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/kansas2012.zip",
-                    "description": "2012 Kansas HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Kansas"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Kansas"
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
-            "landingPage": "https://data.transportation.gov/d/ea2d-gfjm",
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
-            "identifier": "10.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
+            "describedBy": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Transaction+Data+and+Reports",
             "description": "The Car Allowance Rebate System (CARS), otherwise known as Cash for Clunkers, was a program intended to provide economic incentives to United States residents to purchase a new and more fuel efficient vehicle when trading in a less full efficient vehicle. The program was promoted as providing stimulus to the economy by boosting auto sales, while putting safer, cleaner and more fuel efficient vehicles on the road.",
-            "title": "Car Allowance Rebate System (CARS) - Transactions - Final Paid Transaction Database mdb file (via ftp)",
-            "isPartOf": "DOT-10",
-            "agencyProgramURL": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Officially+Ended",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45762,35 +45745,67 @@
                     "title": "Final Paid Transaction Database mdb file (via ftp)"
                 }
             ],
-            "spatial": "N/A",
-            "describedBy": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Transaction+Data+and+Reports",
-            "dataQuality": false,
+            "identifier": "10.1",
+            "isPartOf": "DOT-10",
+            "issued": "2018-12-17",
+            "keyword": [
+                "cars",
+                "transactions"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ea2d-gfjm",
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
+            "title": "Car Allowance Rebate System (CARS) - Transactions - Final Paid Transaction Database mdb file (via ftp)"
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
-            "landingPage": "https://data.transportation.gov/d/ea7s-bvme",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/09martvt/09martvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "March 2009"
+                }
             ],
+            "identifier": "18.66",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -45800,58 +45815,54 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.66",
+            "landingPage": "https://data.transportation.gov/d/ea7s-bvme",
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
-            "title": "Monthly Traffic Volume Trends - March 2009",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/09martvt/09martvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "March 2009"
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
+            "title": "Monthly Traffic Volume Trends - March 2009"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.21949/1503753",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2017-04-01",
-            "@type": "dcat:Dataset",
-            "modified": "2017-03-16",
-            "references": [
-                "https://rosap.ntl.bts.gov/view/dot/34269"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Transportation Library Data Curator",
+                "hasEmail": "mailto:ntldatacurator@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The datasets in this zip file are in support of Intelligent Transportation Systems Joint Program Office (ITS JPO) report FHWA-JPO-16-385, \\\"Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs \u2014 Evaluation Report for ATDM Program,\\\" https://rosap.ntl.bts.gov/view/dot/32520 and FHWA-JPO-16-388, \\\"Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs \u2014 Evaluation Summary for the Chicago Testbed,\\\" https://rosap.ntl.bts.gov/view/dot/34269   \\n\\nThe files in this zip file are specifically related to the Chicago Testbed.\\n\\nThe compressed zip files total 1.6 GB in size. The files have been uploaded as-is; no further documentation was supplied by NTL. All located .docx files were converted to .pdf document files which are an open, archival format. These pdfs were then added to the zip file alongside the original .docx files.\\n\\nThese files can be unzipped using any zip compression/decompression software.  \\n\\nThis zip file contains files in the following formats: \\n.pdf document files which can be read using any pdf reader;\\n.cvs text files which can be read using any text editor;\\n.txt text files which can be read using any text editor;\\n.docx document files which can be read in Microsoft Word and some other word processing programs;\\n. xlsx spreadsheet files which can be read in Microsoft Excel and some other spreadsheet programs;\\n.dat data files which may be text or multimedia;\\nas well as GIS or mapping files in the fowlling formats: .mxd, .dbf, .prj, .sbn, .shp., .shp.xml; which may be opened in ArcGIS or other GIS software.\\n[software requirements]\\n\\nThese files were last accessed in 2017.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The datasets in this zip file are in support of Intelligent Transportation Systems Joint Program Office (ITS JPO) report FHWA-JPO-16-385, \"Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs \u2014 Evaluation Report for ATDM Program, \" https://rosap.ntl.bts.gov/view/dot/32520 and FHWA-JPO-16-388, \"Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs \u2014 Evaluation Summary for the Chicago Testbed, \" https://rosap.ntl.bts.gov/view/dot/34269 The files in this zip file are specifically related to the Chicago Testbed. The compressed zip files total 1.6 GB in size. The files have been uploaded as-is; no further documentation was supplied by NTL. All located .docx files were converted to .pdf document files which are an open, archival format. These pdfs were then added to the zip file alongside the original .docx files. These files can be unzipped using any zip compression/decompression software.  This zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .cvs text files which can be read using any text editor; .txt text files which can be read using any text editor; .docx document files which can be read in Microsoft Word and some other word processing programs; .xlsx spreadsheet files which can be read in Microsoft Excel and some other spreadsheet programs; .dat data files which may be text or multimedia; as well as GIS or mapping files in the following formats: .mxd, .dbf, .prj, .sbn, .shp., .shp .xml; which may be opened in ArcGIS or other GIS software.\\n[software requirements] These files were last accessed in 2017.",
+                    "downloadURL": "https://doi.org/10.21949/1503753",
+                    "mediaType": "application/zip",
+                    "title": "Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs \u2014 Summary Report for the Chicago Testbed [supporting datasets]"
+                }
             ],
+            "identifier": "https://data.transportation.gov/api/views/ebq2-dfgt",
+            "issued": "2017-04-01",
             "keyword": [
                 "active transportation and demand management (atdm)",
                 "ams chicago",
@@ -45867,48 +45878,55 @@
                 "traffic flow",
                 "travel demand"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Transportation Library Data Curator",
-                "hasEmail": "mailto:ntldatacurator@dot.gov"
-            },
+            "landingPage": "https://doi.org/10.21949/1503753",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2017-03-16",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/ebq2-dfgt",
-            "description": "The datasets in this zip file are in support of Intelligent Transportation Systems Joint Program Office (ITS JPO) report FHWA-JPO-16-385, \\\"Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs \u2014 Evaluation Report for ATDM Program,\\\" https://rosap.ntl.bts.gov/view/dot/32520 and FHWA-JPO-16-388, \\\"Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs \u2014 Evaluation Summary for the Chicago Testbed,\\\" https://rosap.ntl.bts.gov/view/dot/34269   \\n\\nThe files in this zip file are specifically related to the Chicago Testbed.\\n\\nThe compressed zip files total 1.6 GB in size. The files have been uploaded as-is; no further documentation was supplied by NTL. All located .docx files were converted to .pdf document files which are an open, archival format. These pdfs were then added to the zip file alongside the original .docx files.\\n\\nThese files can be unzipped using any zip compression/decompression software.  \\n\\nThis zip file contains files in the following formats: \\n.pdf document files which can be read using any pdf reader;\\n.cvs text files which can be read using any text editor;\\n.txt text files which can be read using any text editor;\\n.docx document files which can be read in Microsoft Word and some other word processing programs;\\n. xlsx spreadsheet files which can be read in Microsoft Excel and some other spreadsheet programs;\\n.dat data files which may be text or multimedia;\\nas well as GIS or mapping files in the fowlling formats: .mxd, .dbf, .prj, .sbn, .shp., .shp.xml; which may be opened in ArcGIS or other GIS software.\\n[software requirements]\\n\\nThese files were last accessed in 2017.",
-            "title": "Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs \u2014 Summary Report for the Chicago Testbed [supporting datasets]",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://doi.org/10.21949/1503753",
-                    "description": "The datasets in this zip file are in support of Intelligent Transportation Systems Joint Program Office (ITS JPO) report FHWA-JPO-16-385, \"Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs \u2014 Evaluation Report for ATDM Program, \" https://rosap.ntl.bts.gov/view/dot/32520 and FHWA-JPO-16-388, \"Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs \u2014 Evaluation Summary for the Chicago Testbed, \" https://rosap.ntl.bts.gov/view/dot/34269 The files in this zip file are specifically related to the Chicago Testbed. The compressed zip files total 1.6 GB in size. The files have been uploaded as-is; no further documentation was supplied by NTL. All located .docx files were converted to .pdf document files which are an open, archival format. These pdfs were then added to the zip file alongside the original .docx files. These files can be unzipped using any zip compression/decompression software.  This zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .cvs text files which can be read using any text editor; .txt text files which can be read using any text editor; .docx document files which can be read in Microsoft Word and some other word processing programs; .xlsx spreadsheet files which can be read in Microsoft Excel and some other spreadsheet programs; .dat data files which may be text or multimedia; as well as GIS or mapping files in the following formats: .mxd, .dbf, .prj, .sbn, .shp., .shp .xml; which may be opened in ArcGIS or other GIS software.\\n[software requirements] These files were last accessed in 2017.",
-                    "@type": "dcat:Distribution",
-                    "title": "Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs \u2014 Summary Report for the Chicago Testbed [supporting datasets]"
-                }
+            "references": [
+                "https://rosap.ntl.bts.gov/view/dot/34269"
             ],
             "spatial": "United States, Illinois, Chicago",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "language": [
-                "en-US"
-            ]
+            "title": "Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs \u2014 Summary Report for the Chicago Testbed [supporting datasets]"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/ecg9-wrvc",
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
+                    "description": "2012 Oregon HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/oregon2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Oregon"
+                }
+            ],
+            "identifier": "678.91",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -45922,70 +45940,39 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.91",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Oregon",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/ecg9-wrvc",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/oregon2012.zip",
-                    "description": "2012 Oregon HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Oregon"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Oregon"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/ecnj-b3e2",
-            "issued": "2020-07-16",
-            "@type": "dcat:Dataset",
-            "modified": "2020-07-16",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Justyna Goworowska",
                 "hasEmail": "mailto:j.goworowska.ctr@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/ecnj-b3e2",
             "description": "This table shows the number and percent of people in the United States potentially exposed to different levels of noise from combined aviation and road sources.",
-            "title": "Population potentially exposed to combined aviation and road noise, 2016 and 2018",
-            "programCode": [
-                "021:052"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -45993,43 +45980,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ecnj-b3e2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ecnj-b3e2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ecnj-b3e2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ecnj-b3e2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ecnj-b3e2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ecnj-b3e2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ecnj-b3e2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ecnj-b3e2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ecnj-b3e2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "https://data.transportation.gov/api/views/ecnj-b3e2",
+            "issued": "2020-07-16",
+            "landingPage": "https://data.transportation.gov/d/ecnj-b3e2",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2020-07-16",
+            "programCode": [
+                "021:052"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Population potentially exposed to combined aviation and road noise, 2016 and 2018"
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
-            "landingPage": "https://data.transportation.gov/d/ecnv-epwq",
-            "issued": "2010-07-15",
-            "temporal": "R/2009-10-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://ai.fmcsa.dot.gov/HazmatStat/Default.aspx"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The reports listed below are designed to provide information focused on hazardous materials and carriers and the hazardous materials safety permit program. All reports provide options to choose fiscal or calendar year, and carrier domicile including United States, Canada, and Mexico.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://ai.fmcsa.dot.gov/HazmatStat/Default.aspx",
+                    "mediaType": "text/html",
+                    "title": "Hazardous Materials Safety Data"
+                }
             ],
+            "identifier": "DOT-120",
+            "issued": "2010-07-15",
             "keyword": [
                 "bulk",
                 "compliance review",
@@ -46046,80 +46060,46 @@
                 "shipper",
                 "violation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "DOT-120",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
-            "description": "The reports listed below are designed to provide information focused on hazardous materials and carriers and the hazardous materials safety permit program. All reports provide options to choose fiscal or calendar year, and carrier domicile including United States, Canada, and Mexico.",
-            "title": "A&I - Hazardous Materials Carrier",
-            "agencyProgramURL": "http://ai.fmcsa.dot.gov/HazmatStat/Default.aspx",
+            "landingPage": "https://data.transportation.gov/d/ecnv-epwq",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-24",
+            "phone": "202-366-2161",
             "primaryITInvestmentUII": "021-534052663",
             "programCode": [
                 "021:022"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://ai.fmcsa.dot.gov/HazmatStat/Default.aspx",
-                    "mediaType": "text/html",
-                    "title": "Hazardous Materials Safety Data"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "references": [
+                "http://ai.fmcsa.dot.gov/HazmatStat/Default.aspx"
             ],
             "spatial": "National, State",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/HazmatStat/Default.aspx",
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
+            "title": "A&I - Hazardous Materials Carrier"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Access restricted under the Privacy Act of 1974; SORN issued by OPM; see reference on DOT Privacy Act page www.dot.gov/privacy under Government-wide System of Records",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/ecxw-iueb",
-            "issued": "2014-11-21",
-            "temporal": "R/2014-11-21/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
-            "keyword": [
-                "hire",
-                "hr",
-                "human resources",
-                "personnel",
-                "recruit"
-            ],
+            "categoryDesignation": "Administrative",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "1635.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": true,
             "description": "This data set contains personnel data for DOT new hires and recruits.  This data is maintained by the current HR and payroll provider (Department of Interior's IBC) and USAJobs.  The data contains PII (Employee Name, SSN, Date of Birth, Home Address, etc.), Civil Rights (Disability, Gender, Race) and other sensitive data (Background Investigations and Security Clearance).",
-            "title": "Personnel Hiring Data (WTTS/EODS) and Recruitment Data (USAJobs)",
-            "primaryITInvestmentUII": "021-999996341",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46127,30 +46107,68 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "1635.0",
+            "issued": "2014-11-21",
+            "keyword": [
+                "hire",
+                "hr",
+                "human resources",
+                "personnel",
+                "recruit"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ecxw-iueb",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-14",
+            "phone": "202-366-5140",
+            "primaryITInvestmentUII": "021-999996341",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "rights": "Access restricted under the Privacy Act of 1974; SORN issued by OPM; see reference on DOT Privacy Act page www.dot.gov/privacy under Government-wide System of Records",
             "systemOfRecords": "https://www.govinfo.gov/content/pkg/FR-2008-11-07/pdf/E8-26595.pdf",
+            "temporal": "R/2014-11-21/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Administrative",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-5140"
+            "title": "Personnel Hiring Data (WTTS/EODS) and Recruitment Data (USAJobs)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/ed3b-886g",
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
+                    "description": "2013 New Jersey HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/newjersey2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 New Jersey"
+                }
+            ],
+            "identifier": "678.134",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -46164,60 +46182,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.134",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 New Jersey",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/ed3b-886g",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/newjersey2013.zip",
-                    "description": "2013 New Jersey HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 New Jersey"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 New Jersey"
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
-            "landingPage": "https://data.transportation.gov/d/edde-s6b6",
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
+            "identifier": "94.2",
+            "isPartOf": "DOT-94",
+            "issued": "2011-09-14",
             "keyword": [
                 "bus",
                 "federal motor carrier safety administration",
@@ -46229,61 +46244,59 @@
                 "roadside inspections",
                 "truck"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "94.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
-            "description": "Contains data on roadside inspections of large trucks and buses, including violations discovered. The majority of this information comes from state police jurisdictions to FMCSA, although some Federally-conducted inspections are also included.",
-            "title": "Motor Carrier Inspections - Data Mining Tool",
-            "isPartOf": "DOT-94",
-            "agencyProgramURL": "http://www.fmcsa.dot.gov/safety-security/grants/MCSAP-Basic-Incentive/index.aspx",
+            "landingPage": "https://data.transportation.gov/d/edde-s6b6",
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
+            "accrualPeriodicity": "R/PT1S",
+            "agencyDataSeriesURL": "https://mobile.fmcsa.dot.gov/developer/apidoc.page%3Fcid=48598",
+            "agencyProgramURL": "https://mobile.fmcsa.dot.gov/developer/apidoc.page%3Fcid=48598",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/edyh-n3ic",
-            "issued": "2012-02-18",
-            "temporal": "R/2014/PT1S",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "https://mobile.fmcsa.dot.gov/developer/apidoc.page%3Fcid=48598"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The SaferBus API is a RESTful service API provided by FMCSA for the purpose of making available, the safety performance data of U.S. Department of Transportation (U.S. DOT) registered bus companies. The primary goal is to encourage the development of products, tools or services that can help consumers more easily check the safety record of bus companies to avoid those that have been placed out of service or those that do not have the proper operating authority.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://mobile.fmcsa.dot.gov/developer/apidoc.page%3Fcid=172675",
+                    "mediaType": "application/atom+xml",
+                    "title": "Documentation"
+                }
             ],
+            "identifier": "1668.0",
+            "issued": "2012-02-18",
             "keyword": [
                 "basics",
                 "bus safety",
@@ -46297,63 +46310,40 @@
                 "safety performance",
                 "van safety"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "1668.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
-            "description": "The SaferBus API is a RESTful service API provided by FMCSA for the purpose of making available, the safety performance data of U.S. Department of Transportation (U.S. DOT) registered bus companies. The primary goal is to encourage the development of products, tools or services that can help consumers more easily check the safety record of bus companies to avoid those that have been placed out of service or those that do not have the proper operating authority.",
-            "title": "SaferBus API - Documentation",
-            "agencyProgramURL": "https://mobile.fmcsa.dot.gov/developer/apidoc.page%3Fcid=48598",
+            "landingPage": "https://data.transportation.gov/d/edyh-n3ic",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-24",
+            "phone": "202-366-9409",
             "primaryITInvestmentUII": "021-048312011",
             "programCode": [
                 "021:022"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://mobile.fmcsa.dot.gov/developer/apidoc.page%3Fcid=172675",
-                    "mediaType": "application/atom+xml",
-                    "title": "Documentation"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "references": [
+                "https://mobile.fmcsa.dot.gov/developer/apidoc.page%3Fcid=48598"
             ],
             "spatial": "National, State, Regional",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "https://mobile.fmcsa.dot.gov/developer/apidoc.page%3Fcid=48598",
+            "temporal": "R/2014/PT1S",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/PT1S",
-            "categoryDesignation": "Research",
-            "phone": "202-366-9409",
-            "language": [
-                "en-US"
-            ]
+            "title": "SaferBus API - Documentation"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/eek5-pv8d",
-            "issued": "2023-08-10",
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
-            "identifier": "https://data.transportation.gov/api/views/eek5-pv8d",
             "description": "State, County and City FIPS (Federal Information Processing Standards) codes are a set of numeric designations given to state, cities and counties by the U.S. federal government. All geographic data submitted to the FRA must have a FIPS code.",
-            "title": "State, County and City FIPS Reference Table",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46361,46 +46351,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/eek5-pv8d/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/eek5-pv8d/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/eek5-pv8d/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/eek5-pv8d/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/eek5-pv8d/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/eek5-pv8d/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/eek5-pv8d/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/eek5-pv8d/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/eek5-pv8d/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/eek5-pv8d",
+            "issued": "2023-08-10",
+            "landingPage": "https://data.transportation.gov/d/eek5-pv8d",
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
+            "title": "State, County and City FIPS Reference Table"
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
-            "landingPage": "https://data.transportation.gov/d/eemt-wbfs",
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
+                    "downloadURL": "http://faf.ornl.gov/fafweb/",
+                    "mediaType": "text/html",
+                    "title": "FAF3 Origin-Destination zip data"
+                }
             ],
+            "identifier": "286.5",
+            "isPartOf": "DOT-286",
+            "issued": "2013-03-20",
             "keyword": [
                 "commodity",
                 "consumption",
@@ -46425,105 +46441,63 @@
                 "value",
                 "wear"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "286.5",
+            "landingPage": "https://data.transportation.gov/d/eemt-wbfs",
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
-            "title": "Freight Analysis Framework - FAF3 Origin-Destination zip data",
-            "isPartOf": "DOT-286",
-            "agencyProgramURL": "http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://faf.ornl.gov/fafweb/",
-                    "mediaType": "text/html",
-                    "title": "FAF3 Origin-Destination zip data"
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
+            "title": "Freight Analysis Framework - FAF3 Origin-Destination zip data"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/eevn-mgvi",
-            "issued": "2024-05-10",
             "@type": "dcat:Dataset",
-            "modified": "2024-05-30",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joe McGill",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/eevn-mgvi",
+            "issued": "2024-05-10",
+            "landingPage": "https://data.transportation.gov/d/eevn-mgvi",
+            "modified": "2024-05-30",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "2022 NCFO Terminals and Segments"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/eezi-v4pm",
+            "accrualPeriodicity": "R/PT1S",
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
-                "basic safety message (bsm)",
-                "blacksburg",
-                "connected vehicle message",
-                "dedicated short range communication (dsrc)",
-                "field test",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "northern virginia",
-                "on-board unit (obu)",
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
-            "identifier": "https://data.transportation.gov/api/views/eezi-v4pm",
+            "dataQuality": true,
             "description": "Contains all Basic Safety Messages (BSMs) collected during the Advanced Messaging Concept Development (AMCD) field testing program. For this project, all of the Part I BSM message fields were populated. Additional data fields were also added to the row to identify sender, time of communication, mode of communication, etc., allowing the consumer of this data set to accurately track messages through the system. All BSMs are generated by OBUs and ultimately received by the VCC Cloud server.",
-            "title": "Advanced Messaging Concept Development Basic Safety Message",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46531,49 +46505,90 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/eezi-v4pm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/eezi-v4pm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/eezi-v4pm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/eezi-v4pm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/eezi-v4pm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/eezi-v4pm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/eezi-v4pm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/eezi-v4pm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/eezi-v4pm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Tyson\u2019s Corner, Fairfax County, Virginia",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/eezi-v4pm",
+            "issued": "2016-09-01",
+            "keyword": [
+                "advanced messaging concept development (amcd)",
+                "arterial",
+                "basic safety message (bsm)",
+                "blacksburg",
+                "connected vehicle message",
+                "dedicated short range communication (dsrc)",
+                "field test",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "northern virginia",
+                "on-board unit (obu)",
+                "virginia tech transportation institute (vtti)"
+            ],
+            "landingPage": "https://data.transportation.gov/d/eezi-v4pm",
             "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "R/PT1S",
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
             "theme": [
                 "Automobiles"
-            ]
+            ],
+            "title": "Advanced Messaging Concept Development Basic Safety Message"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "https://www.nhtsa.gov/content/nhtsa-ftp/2926",
+            "analysisUnit": "automobile crash",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/efry-jap6",
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
+            "identifier": "376.2",
+            "isPartOf": "DOT-376",
+            "issued": "2008-12-05",
             "keyword": [
                 "avoidance",
                 "causation",
@@ -46586,75 +46601,43 @@
                 "pre-crash",
                 "vehicle"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "376.2",
+            "landingPage": "https://data.transportation.gov/d/efry-jap6",
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
-            "agencyDataSeriesURL": "https://www.nhtsa.gov/content/nhtsa-ftp/2926",
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
-            "issued": "2022-07-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "highway",
-                "highway performance monitoring",
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
-            "identifier": "https://data.transportation.gov/api/views/efu4-vidc",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 1980",
-            "title": "Historic HPMS Data (Universe) - 1980",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46662,46 +46645,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/efu4-vidc/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/efu4-vidc/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/efu4-vidc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/efu4-vidc/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/efu4-vidc/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/efu4-vidc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/efu4-vidc/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/efu4-vidc/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/efu4-vidc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/efu4-vidc",
+            "issued": "2022-07-06",
+            "keyword": [
+                "highway",
+                "highway performance monitoring",
+                "hpms"
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
+            "title": "Historic HPMS Data (Universe) - 1980"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "description": "Historic Highway Performance Monitoring (HPMS) Data by year",
+            "identifier": "https://data.transportation.gov/api/views/egfy-6ipf",
             "issued": "2022-07-08",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-26",
             "keyword": [
                 "highway",
                 "highway performance monitoring",
@@ -46711,40 +46715,51 @@
                 "sample",
                 "universe"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
+            "modified": "2022-09-26",
+            "programCode": [
+                "021:009"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/egfy-6ipf",
-            "description": "Historic Highway Performance Monitoring (HPMS) Data by year",
-            "title": "Historic Highway Performance Monitoring (HPMS) Data",
-            "programCode": [
-                "021:009"
-            ],
             "spatial": "United States",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "Historic Highway Performance Monitoring (HPMS) Data"
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
-            "landingPage": "https://data.transportation.gov/d/egud-z46w",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/09jultvt/09jultvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "July 2009"
+                }
             ],
+            "identifier": "18.32",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -46754,184 +46769,151 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.32",
+            "landingPage": "https://data.transportation.gov/d/egud-z46w",
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
-            "title": "Monthly Traffic Volume Trends - July 2009",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/09jultvt/09jultvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "July 2009"
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
+            "title": "Monthly Traffic Volume Trends - July 2009"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ehhj-nune",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Janine McFadden",
+                "hasEmail": "mailto:janine.mcfadden@dot.gov"
+            },
+            "description": "A landing page for the National Census of Ferry Operators, a biennial survey of passenger ferry operations in the United States",
+            "identifier": "https://data.transportation.gov/api/views/ehhj-nune",
             "issued": "2020-04-15",
-            "temporal": "2017-01-01/2017-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-08-26",
             "keyword": [
                 "census",
                 "ferry",
                 "operators",
                 "transit"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Janine McFadden",
-                "hasEmail": "mailto:janine.mcfadden@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/ehhj-nune",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2020-08-26",
+            "programCode": [
+                "021:042"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/ehhj-nune",
-            "description": "A landing page for the National Census of Ferry Operators, a biennial survey of passenger ferry operations in the United States",
-            "title": "National Census of Ferry Operators (NCFO) 2018: Landing Page",
-            "programCode": [
-                "021:042"
-            ],
-            "license": "https://www.usa.gov/government-works",
+            "temporal": "2017-01-01/2017-12-31",
             "theme": [
                 "Ferry Transit"
-            ]
+            ],
+            "title": "National Census of Ferry Operators (NCFO) 2018: Landing Page"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ejmp-u4kv",
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
-            "identifier": "https://data.transportation.gov/api/views/ejmp-u4kv",
             "description": "Rail intermodal traffic is comprised of shipping containers and truck trailers moved on rail cars, which transport a large range of goods. The Association of American Railroads releases data on carloads and intermodal units originated by U.S. railroads on a weekly and monthly basis.",
-            "title": "Freight Rail Traffic - Intermodal Units",
+            "identifier": "https://data.transportation.gov/api/views/ejmp-u4kv",
+            "issued": "2025-01-21",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ejmp-u4kv",
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
+            "title": "Freight Rail Traffic - Intermodal Units"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ejv6-cpdh",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This report contains a listing of each highway-rail crossing in the United States. Each row displays the crossing ID, or USDOT Crossing Inventory Number, along with the state, railroad, whether the crossing is open or closed, milepost, county name, city name, street, last update, highest level of warning device present at the crossing, crossing position, crossing type, crossing purpose, THR (Train Horn Rule) Request Number, average daily vehicle count, total number of tracks, and trains per day.",
+            "identifier": "https://data.transportation.gov/api/views/ejv6-cpdh",
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
+            "landingPage": "https://data.transportation.gov/d/ejv6-cpdh",
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
-            "identifier": "https://data.transportation.gov/api/views/ejv6-cpdh",
-            "description": "This report contains a listing of each highway-rail crossing in the United States. Each row displays the crossing ID, or USDOT Crossing Inventory Number, along with the state, railroad, whether the crossing is open or closed, milepost, county name, city name, street, last update, highest level of warning device present at the crossing, crossing position, crossing type, crossing purpose, THR (Train Horn Rule) Request Number, average daily vehicle count, total number of tracks, and trains per day.",
-            "title": "Crossing Inventory Listing (8.01/8.08)",
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
+            "title": "Crossing Inventory Listing (8.01/8.08)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ekg5-frzt",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
-            "keyword": [
-                "average fares per trip",
-                "cost per hour",
-                "fare recovery ratio",
-                "transit kpis",
-                "transit metrics",
-                "trips per mile"
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
-            "identifier": "https://data.transportation.gov/api/views/ekg5-frzt",
             "description": "This dataset details service and cost efficiency metrics for agencies reporting to the National Transit Database in the 2022 and 2023 report years.\n\nOnly Full Reporters report data on Passenger Miles. The columns containing ratios have been calculated as the average across all reporting modes, not as the ratio of summed data. Thus, each transit agency received equal weight, regardless of that agency's total ridership.\n\nNTD Data Tables organize and summarize data from the 2022 and 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. This dataset is based on the 2022 and 2023 Federal Funding Allocation, Operating Expenses, and Service database files.\n\nIn years 2015-2021, you can find this data in the \"Metrics\" data table on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.\n\nIn versions of the NTD data tables from before 2014, you can find data on metrics in the files called \"Fare per Passenger and Recovery Ratio\" and \"Service Supplied and Consumed Ratios.\"\n\nIf you have any other questions about this table, please contact the NTD Help Desk at NTDHelp@dot.gov.",
-            "title": "2022 - 2023 NTD Annual Data - Metrics",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -46939,93 +46921,92 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ekg5-frzt/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ekg5-frzt/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ekg5-frzt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ekg5-frzt/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ekg5-frzt/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ekg5-frzt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ekg5-frzt/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ekg5-frzt/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ekg5-frzt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/ekg5-frzt",
+            "issued": "2024-09-10",
+            "keyword": [
+                "average fares per trip",
+                "cost per hour",
+                "fare recovery ratio",
+                "transit kpis",
+                "transit metrics",
+                "trips per mile"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ekg5-frzt",
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
+            "title": "2022 - 2023 NTD Annual Data - Metrics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/em4z-nqt3",
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
-            "identifier": "https://data.transportation.gov/api/views/em4z-nqt3",
             "description": "The Bureau of Transportation Statistics releases non-seasonally adjusted air traffic data based on monthly reports from commercial U.S. air carriers.",
-            "title": "Air Travel - Domestic",
+            "identifier": "https://data.transportation.gov/api/views/em4z-nqt3",
+            "issued": "2025-01-16",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/em4z-nqt3",
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
-            ]
+            ],
+            "title": "Air Travel - Domestic"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/em9t-xx9j",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2024-10-02",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
-            "keyword": [
-                "aff",
-                "air carriers",
-                "aviation facts & figures",
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
-            "identifier": "https://data.transportation.gov/api/views/em9t-xx9j",
             "description": "Average annual employment by air carrier.",
-            "title": "AFF - P1a Employees Summary",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47033,73 +47014,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/em9t-xx9j/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/em9t-xx9j/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/em9t-xx9j/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/em9t-xx9j/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/em9t-xx9j/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/em9t-xx9j/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/em9t-xx9j/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/em9t-xx9j/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/em9t-xx9j/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/em9t-xx9j",
+            "issued": "2024-10-02",
+            "keyword": [
+                "aff",
+                "air carriers",
+                "aviation facts & figures",
+                "transportation employment"
+            ],
+            "landingPage": "https://data.transportation.gov/d/em9t-xx9j",
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
+            "title": "AFF - P1a Employees Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/emdt-zjhy",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2024-05-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-01",
-            "references": [
-                "https://github.com/FHWA-Ofc-Transportation-Policy-Studies/FHWA-Mobility-Trends"
-            ],
-            "keyword": [
-                "charging stations",
-                "emerging trends",
-                "fhwa",
-                "forecasting",
-                "ghg",
-                "modeling",
-                "tms",
-                "transit mode share",
-                "transportation demand",
-                "travel behavior",
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
-            "identifier": "https://data.transportation.gov/api/views/emdt-zjhy",
             "description": "The mobility trends team forecasts each of the transportation trend indicators through 2050 to create performance metric forecasts. These forecasts, using varying scenarios of the trend indicators, allows our team to estimate the future of transportation demand. The analysis of emerging trends and policy alternatives is a core function of the Office of Transportation Policy Studies. The goal of this research project is to enhance FHWA\u2019s empirical understanding of the impact of trends on travel behavior and transportation demand, and ultimately system performance and the user experience. At the core of this research project is the identification and analysis of trends to support a variety of modeling, forecasting, and \u2018what if\u2019 projections to support policy and decision making.",
-            "title": "Mobility Trends County Level Indicator Forecasts",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47107,68 +47077,114 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/emdt-zjhy/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/emdt-zjhy/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/emdt-zjhy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/emdt-zjhy/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/emdt-zjhy/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/emdt-zjhy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/emdt-zjhy/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/emdt-zjhy/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/emdt-zjhy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/emdt-zjhy",
+            "issued": "2024-05-31",
+            "keyword": [
+                "charging stations",
+                "emerging trends",
+                "fhwa",
+                "forecasting",
+                "ghg",
+                "modeling",
+                "tms",
+                "transit mode share",
+                "transportation demand",
+                "travel behavior",
+                "vmt",
+                "what if"
+            ],
+            "landingPage": "https://data.transportation.gov/d/emdt-zjhy",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-01-01",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "references": [
+                "https://github.com/FHWA-Ofc-Transportation-Policy-Studies/FHWA-Mobility-Trends"
+            ],
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "Mobility Trends County Level Indicator Forecasts"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/en3y-72zv",
-            "issued": "2020-08-14",
             "@type": "dcat:Dataset",
-            "modified": "2021-04-20",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/en3y-72zv",
+            "issued": "2020-08-14",
+            "landingPage": "https://data.transportation.gov/d/en3y-72zv",
+            "modified": "2021-04-20",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
-            "title": "2018-2019 All Road Network Of Linear Data (ARNOLD)",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "2018-2019 All Road Network Of Linear Data (ARNOLD)"
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
-            "landingPage": "https://data.transportation.gov/d/encb-vt68",
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
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/inctmap.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Accident Map with Table"
+                }
             ],
+            "identifier": "199.14",
+            "isPartOf": "DOT-199",
+            "issued": "2010-09-29",
             "keyword": [
                 "acts of god",
                 "collisions",
@@ -47179,82 +47195,49 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "199.14",
+            "landingPage": "https://data.transportation.gov/d/encb-vt68",
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
-            "title": "Rail Equipment Accidents - Accident Map with Table",
-            "isPartOf": "DOT-199",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:036"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/inctmap.aspx",
-                    "mediaType": "text/csv",
-                    "title": "Accident Map with Table"
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
+            "title": "Rail Equipment Accidents - Accident Map with Table"
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
-            "landingPage": "https://data.transportation.gov/d/epjk-ax3b",
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
-            "identifier": "10.3",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
+            "describedBy": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Transaction+Data+and+Reports",
             "description": "The Car Allowance Rebate System (CARS), otherwise known as Cash for Clunkers, was a program intended to provide economic incentives to United States residents to purchase a new and more fuel efficient vehicle when trading in a less full efficient vehicle. The program was promoted as providing stimulus to the economy by boosting auto sales, while putting safer, cleaner and more fuel efficient vehicles on the road.",
-            "title": "Car Allowance Rebate System (CARS) - Transactions - Cancelled Transaction Database text file",
-            "isPartOf": "DOT-10",
-            "agencyProgramURL": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Officially+Ended",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47263,52 +47246,50 @@
                     "title": "Cancelled Transaction Database text file"
                 }
             ],
-            "spatial": "N/A",
-            "describedBy": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Transaction+Data+and+Reports",
-            "dataQuality": false,
+            "identifier": "10.3",
+            "isPartOf": "DOT-10",
+            "issued": "2018-12-17",
+            "keyword": [
+                "cars",
+                "transactions"
+            ],
+            "landingPage": "https://data.transportation.gov/d/epjk-ax3b",
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
+            "title": "Car Allowance Rebate System (CARS) - Transactions - Cancelled Transaction Database text file"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2024-02-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-20",
-            "references": [
-                "FHWA"
-            ],
-            "keyword": [
-                "national bicycle network",
-                "nbn"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "US Department of Transportation"
-            },
-            "identifier": "https://data.transportation.gov/api/views/epq5-enxz",
+            "dataQuality": true,
             "description": "The National Bicycle Network is a geospatial dataset for nationwide bicycle routes. It is based on data and information released by public agencies such as state transportation departments, local Metropolitan Planning Organizations, local Councils of Government, city, and county public works and transportation departments. The FHWA Office of Highway Policy Information (HPPI) integrates all releases into one nationwide bicycle network, construction, and operating of such facilities as a safe, efficient, and equitable travel mode.",
-            "title": "National Bicycle Network",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47316,45 +47297,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/epq5-enxz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/epq5-enxz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/epq5-enxz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/epq5-enxz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/epq5-enxz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/epq5-enxz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/epq5-enxz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/epq5-enxz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/epq5-enxz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/epq5-enxz",
+            "issued": "2024-02-02",
+            "keyword": [
+                "national bicycle network",
+                "nbn"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-08-20",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
+            "references": [
+                "FHWA"
+            ],
             "spatial": "Nationwide",
-            "dataQuality": true,
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "National Bicycle Network"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/eqb9-f3e5",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This report contains US-level key statistics, including data on highway-rail grade crossing incidents, fatalities, and injuries; public and private grade crossings; and trespasser incidents, fatalities and injuries.",
+            "identifier": "https://data.transportation.gov/api/views/eqb9-f3e5",
             "issued": "2023-08-04",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "crossing counts",
                 "grade crossing",
@@ -47364,43 +47369,55 @@
                 "summary",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/eqb9-f3e5",
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
-            "identifier": "https://data.transportation.gov/api/views/eqb9-f3e5",
-            "description": "This report contains US-level key statistics, including data on highway-rail grade crossing incidents, fatalities, and injuries; public and private grade crossings; and trespasser incidents, fatalities and injuries.",
-            "title": "Highway-Rail Incidents, Inventory and Trespasser High-Level Summary (1.11)",
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
+            "title": "Highway-Rail Incidents, Inventory and Trespasser High-Level Summary (1.11)"
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
-            "landingPage": "https://data.transportation.gov/d/er8h-eeja",
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
+            "identifier": "266.3",
+            "isPartOf": "DOT-266",
+            "issued": "2009-09-01",
             "keyword": [
                 "crash",
                 "data",
@@ -47412,84 +47429,49 @@
                 "safety",
                 "vehicle"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "266.3",
+            "landingPage": "https://data.transportation.gov/d/er8h-eeja",
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
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://www.nhtsa.gov",
+            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
+            "analysisUnit": "Test",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/ercz-9u3e",
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
-            "identifier": "364.8",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database - Vehicle Browse Tests",
-            "isPartOf": "DOT-364",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
-            "primaryITInvestmentUII": "021-621341357",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47498,57 +47480,57 @@
                     "title": "Vehicle Browse Tests"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.8",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ercz-9u3e",
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
+            "title": "Vehicle Safety Research and Development Database - Vehicle Browse Tests"
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
-            "landingPage": "https://data.transportation.gov/d/ertf-m57u",
-            "issued": "1998-12-24",
-            "temporal": "R/1998-12-14/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
-            "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.nhtsa.gov/Research/Databases+and+Software/NHTSA+Test+Reference+Guides"
-            ],
-            "keyword": [
-                "nhtsa crash test database",
-                "nhtsa vehicle crash test database"
-            ],
+            "categoryDesignation": "Research",
+            "collectionInstrument": "Transportation",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "364.17",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database - Component Test Database Interactive Access",
-            "isPartOf": "DOT-364",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
-            "primaryITInvestmentUII": "021-621341357",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47557,35 +47539,68 @@
                     "title": "Component Test Database Interactive Access"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.17",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ertf-m57u",
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
+            "title": "Vehicle Safety Research and Development Database - Component Test Database Interactive Access"
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
-            "landingPage": "https://data.transportation.gov/d/eryt-2388",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/04septvt/04septvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "September 2004"
+                }
             ],
+            "identifier": "18.120",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -47595,60 +47610,60 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.120",
+            "landingPage": "https://data.transportation.gov/d/eryt-2388",
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
-            "title": "Monthly Traffic Volume Trends - September 2004",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/04septvt/04septvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "September 2004"
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
+            "title": "Monthly Traffic Volume Trends - September 2004"
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
-            "landingPage": "https://data.transportation.gov/d/es8d-dwmg",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/07septvt/07septvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "September 2007"
+                }
             ],
+            "identifier": "18.84",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -47658,60 +47673,62 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.84",
+            "landingPage": "https://data.transportation.gov/d/es8d-dwmg",
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
-            "title": "Monthly Traffic Volume Trends - September 2007",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/07septvt/07septvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "September 2007"
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
+            "title": "Monthly Traffic Volume Trends - September 2007"
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
-            "landingPage": "https://data.transportation.gov/d/ess2-7zfz",
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
+                    "downloadURL": "http://www-odi.nhtsa.dot.gov/owners/SearchSafetyIssues%3FprodType=T",
+                    "mediaType": "text/html",
+                    "title": "Recalls - Tires"
+                }
             ],
+            "identifier": "83.11",
+            "isPartOf": "DOT-83",
+            "issued": "2002-12-16",
             "keyword": [
                 "air bag",
                 "air bags",
@@ -47738,87 +47755,50 @@
                 "vin",
                 "vin search"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "83.11",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Manufacturers who determine that a product or piece of original equipment either has a safety defect or is not in compliance with Federal safety standards are required to notify the National Highway Traffic Safety Administration (NHTSA) within 5 business days. NHTSA requires that manufacturers file a Defect and Noncompliance report as well as quarterly recall status reports, in compliance with Federal Regulation 49 (the National Traffic and Motor Safety Act) Part 573, which identifies the requirements for safety recalls. This information is stored in the NHTSA database. Use this data to search for recall information related to:-\tSpecific NHTSA campaigns -\tProduct types Access to public searches of NHTSA recall databases for tires, vehicles, car seats and equipment.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - Recalls - Tires",
-            "isPartOf": "DOT-83",
-            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
-            "describedByType": "text/plain",
+            "landingPage": "https://data.transportation.gov/d/ess2-7zfz",
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
-                    "downloadURL": "http://www-odi.nhtsa.dot.gov/owners/SearchSafetyIssues%3FprodType=T",
-                    "mediaType": "text/html",
-                    "title": "Recalls - Tires"
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
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - Recalls - Tires"
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
-            "landingPage": "https://data.transportation.gov/d/esv7-a6mk",
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
-            "identifier": "DOT-320",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "NHTSA's Chief Counsel interprets the statutes that the agency administers and the regulations that it promulgates. The Chief Counsel's interpretations, issued in the form of letters responding to questions from the motor vehicle industry and the public, represent the definitive view of the agency on the questions addressed and may be relied upon by the regulated industry and members of the public. These interpretations have always been available to the public in the agency's technical reference library in Washington. The World Wide Web enables us to make them available through the Internet.",
-            "title": "Federal Motor Vehicle Safety Standards Interpretations",
-            "agencyProgramURL": "http://isearch.nhtsa.gov/",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47826,55 +47806,56 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "DOT-320",
+            "issued": "2011-01-18",
+            "keyword": [
+                "data.gov",
+                "interpretation",
+                "law",
+                "motor vehicle",
+                "safety",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/esv7-a6mk",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://isearch.nhtsa.gov/",
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
+            "title": "Federal Motor Vehicle Safety Standards Interpretations"
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
-            "landingPage": "https://data.transportation.gov/d/etsc-pmhi",
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
-            "identifier": "696.9",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "A compilation of historic documents and articles on the Interstate System, Federal-Aid Highway Program, FHWA, and transportation.",
-            "title": "Highway History - General Highway History",
-            "isPartOf": "DOT-696",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/infrastructure/history.cfm",
-            "programCode": [
-                "021:011"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47883,33 +47864,67 @@
                     "title": "General Highway History"
                 }
             ],
-            "spatial": "National",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "696.9",
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
+            "landingPage": "https://data.transportation.gov/d/etsc-pmhi",
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
+            "title": "Highway History - General Highway History"
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
-            "landingPage": "https://data.transportation.gov/d/euji-34vt",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/11martvt/11martvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "March 2011"
+                }
             ],
+            "identifier": "18.12",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -47919,76 +47934,45 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.12",
+            "landingPage": "https://data.transportation.gov/d/euji-34vt",
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
-            "title": "Monthly Traffic Volume Trends - March 2011",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/11martvt/11martvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "March 2011"
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
+            "title": "Monthly Traffic Volume Trends - March 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/bridge/inspection/tunnel/inventory.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2022-06-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "tunnel inventory",
-                "tunnels"
-            ],
             "conformsTo": "https://www.fhwa.dot.gov/bridge/inspection/tunnel/snti/hif15006.pdf",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/euv9-yzr3",
-            "description": "The NTI is an aggregation of structure inventory and appraisal data of tunnels located on public roads submitted by States, Federal agencies and Tribal governments in accordance with the National Tunnel Inspection Standards (NTIS) which requires each State prepare and maintain an inventory of all tunnels. The NTI data is used as a data source to assist in the oversight of the National Tunnel Inspection Program and to respond to inquiries from different entities on the Nation\u2019s tunnels.",
-            "title": "National Tunnel Inventory (NTI)",
+            "describedBy": "https://www.fhwa.dot.gov/bridge/inspection/tunnel/snti/hif15006.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "021:009"
-            ],
+            "description": "The NTI is an aggregation of structure inventory and appraisal data of tunnels located on public roads submitted by States, Federal agencies and Tribal governments in accordance with the National Tunnel Inspection Standards (NTIS) which requires each State prepare and maintain an inventory of all tunnels. The NTI data is used as a data source to assist in the oversight of the National Tunnel Inspection Program and to respond to inquiries from different entities on the Nation\u2019s tunnels.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -47997,47 +47981,78 @@
                     "title": "Main Page for National Tunnel Inventory"
                 }
             ],
-            "spatial": "United States",
-            "describedBy": "https://www.fhwa.dot.gov/bridge/inspection/tunnel/snti/hif15006.pdf",
+            "identifier": "https://data.transportation.gov/api/views/euv9-yzr3",
+            "issued": "2022-06-23",
+            "keyword": [
+                "tunnel inventory",
+                "tunnels"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/bridge/inspection/tunnel/inventory.cfm",
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
                 "National Geospatial Data Asset Transportation"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "National Tunnel Inventory (NTI)"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/evey-tqdd",
-            "issued": "2021-12-08",
             "@type": "dcat:Dataset",
-            "modified": "2023-03-02",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/evey-tqdd",
+            "issued": "2021-12-08",
+            "landingPage": "https://data.transportation.gov/d/evey-tqdd",
+            "modified": "2023-03-02",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
-            "title": "Geocoding Test Story",
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Geocoding Test Story"
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
+            "description": "The Intelligent Transportation Systems Joint Program Office (ITS JPO) of the U.S. Department of Transportation (U.S. DOT) has developed this ITS Benefits Database. Major objectives are; (1) document findings from the evaluation of ITS deployments pertaining to the effect of ITS on transportation systems performance, (2) provide transportation professionals with convenient access to the benefits of ITS deployment so that they can make informed planning and investment decisions.\n\nFindings from ITS evaluations are presented in a concise summary format. Each benefit entry includes items such as a title in the form of a short statement of the evaluation finding, context narrative, and identifying information such as date, location, and source, as well as the evaluation details that describe how the identified ITS benefit was determined.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Link to Intelligent Transportation Systems (ITS) Benefits Database's Web User Interface.",
+                    "downloadURL": "https://www.itskrs.its.dot.gov/benefits",
+                    "mediaType": "text/html",
+                    "title": "Intelligent Transportation Systems (ITS) Benefits"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/ex7f-b9wq",
             "issued": "2019-05-02",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-02",
             "keyword": [
                 "arterial management",
                 "automated vehicles",
@@ -48055,72 +48070,37 @@
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
-            "identifier": "https://data.transportation.gov/api/views/ex7f-b9wq",
-            "description": "The Intelligent Transportation Systems Joint Program Office (ITS JPO) of the U.S. Department of Transportation (U.S. DOT) has developed this ITS Benefits Database. Major objectives are; (1) document findings from the evaluation of ITS deployments pertaining to the effect of ITS on transportation systems performance, (2) provide transportation professionals with convenient access to the benefits of ITS deployment so that they can make informed planning and investment decisions.\n\nFindings from ITS evaluations are presented in a concise summary format. Each benefit entry includes items such as a title in the form of a short statement of the evaluation finding, context narrative, and identifying information such as date, location, and source, as well as the evaluation details that describe how the identified ITS benefit was determined.",
-            "title": "Intelligent Transportation Systems (ITS) Benefits",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.itskrs.its.dot.gov/benefits",
-                    "description": "Link to Intelligent Transportation Systems (ITS) Benefits Database's Web User Interface.",
-                    "@type": "dcat:Distribution",
-                    "title": "Intelligent Transportation Systems (ITS) Benefits"
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
+            "title": "Intelligent Transportation Systems (ITS) Benefits"
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
-            "identifier": "https://data.transportation.gov/api/views/exgp-m9a9",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 2009",
-            "title": "Historic HPMS Data (Sample) - 2009",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48128,85 +48108,120 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/exgp-m9a9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/exgp-m9a9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/exgp-m9a9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/exgp-m9a9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/exgp-m9a9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/exgp-m9a9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/exgp-m9a9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/exgp-m9a9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/exgp-m9a9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/exgp-m9a9",
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
+            "title": "Historic HPMS Data (Sample) - 2009"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ey6f-ijqz",
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
-            "identifier": "https://data.transportation.gov/api/views/ey6f-ijqz",
             "description": "Employed persons include people aged 16 years and older in the civilian noninstitutional population who did any work at all as paid employees; worked in their own business, profession, or on their own farm, or worked 15 hours or more as unpaid workers in an enterprise operated by a member of the family; and all those who were not working but who had jobs or businesses from which they were temporarily absent. The Bureau of Labor Statistics produces industry estimates of nonfarm payroll employment as part of the Current Population Survey.",
-            "title": "Transportation Employment - Pipeline Transportation",
+            "identifier": "https://data.transportation.gov/api/views/ey6f-ijqz",
+            "issued": "2025-01-02",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ey6f-ijqz",
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
+            "title": "Transportation Employment - Pipeline Transportation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
+            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/mapping/ssdq/",
+            "agencyProgramURL": "http://ai.fmcsa.dot.gov/DataQuality/dataquality.asp%3F",
+            "analysisUnit": "State data quality performance",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/eyt8-92qc",
-            "issued": "2004-03-15",
-            "temporal": "R/2007-01-01/P3M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://ai.fmcsa.dot.gov/DataQuality/DataQuality.asp%3Fredirect=methodology.asp"
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
+            "identifier": "113.1",
+            "isPartOf": "DOT-113",
+            "issued": "2004-03-15",
             "keyword": [
                 "accuracy",
                 "completeness",
@@ -48223,83 +48238,49 @@
                 "state safety data quality map",
                 "timelines"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "113.1",
+            "landingPage": "https://data.transportation.gov/d/eyt8-92qc",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-24",
+            "phone": "202-366-5387",
+            "programCode": [
+                "021:022"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Motor Carrier Safety Administration"
             },
-            "description": "Data Quality identifies FMCSA resources for evaluating, monitoring, and improving the quality of data submitted by States to the Motor Carrier Management Information System (MCMIS).",
-            "title": "A&I - Data Quality - State Safety Data Quality Map",
-            "isPartOf": "DOT-113",
-            "agencyProgramURL": "http://ai.fmcsa.dot.gov/DataQuality/dataquality.asp%3F",
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
+                "http://ai.fmcsa.dot.gov/DataQuality/DataQuality.asp%3Fredirect=methodology.asp"
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
-            "categoryDesignation": "Research",
-            "analysisUnit": "State data quality performance",
-            "phone": "202-366-5387",
-            "language": [
-                "en-US"
-            ]
+            "title": "A&I - Data Quality - State Safety Data Quality Map"
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
-            "landingPage": "https://data.transportation.gov/d/eywr-tzvd",
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
-            "identifier": "DOT-373",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": true,
             "description": "Each Freedom of Information Act office uses a case log to track FOIA requests. The logs typically include the dates on which requests were received and closed, control numbers, requester names and descriptions of the requested records.",
-            "title": "Freedom of Information Act Logs for the Office of the Secretary of Transportation",
-            "agencyProgramURL": "http://www.dot.gov/foia",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48308,59 +48289,58 @@
                     "title": "2007"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "DOT-373",
+            "issued": "2007-12-31",
+            "keyword": [
+                "foia",
+                "freedom of information act",
+                "log",
+                "request"
+            ],
+            "landingPage": "https://data.transportation.gov/d/eywr-tzvd",
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
+            "title": "Freedom of Information Act Logs for the Office of the Secretary of Transportation"
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
-            "landingPage": "https://data.transportation.gov/d/ezbe-vf5q",
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
-            "identifier": "302.2",
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
@@ -48368,34 +48348,68 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "302.2",
+            "isPartOf": "DOT-302",
+            "issued": "2011-01-18",
+            "keyword": [
+                "data.gov",
+                "law",
+                "significant guidance",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ezbe-vf5q",
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
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/economicrecovery/",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/economicrecovery/",
+            "analysisUnit": "Regulations",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/ezjk-jjx7",
-            "issued": "2011-01-18",
-            "temporal": "2009-01-01/2011-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.fhwa.dot.gov/economicrecovery/"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Specific Federal Highway Administration Policy and Guidance Statements relating to the American Recovery and Reinvestment Act of 2009",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fhwa.dot.gov/economicrecovery/",
+                    "mediaType": "text/html"
+                }
             ],
+            "identifier": "304.2",
+            "isPartOf": "DOT-304",
+            "issued": "2011-01-18",
             "keyword": [
                 "data.gov",
                 "highway",
@@ -48406,120 +48420,84 @@
                 "stimulus",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "304.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "Specific Federal Highway Administration Policy and Guidance Statements relating to the American Recovery and Reinvestment Act of 2009",
-            "title": "Federal Highway Administration American Recovery and Reinvestment Act of 2009 Policy and Guidance -",
-            "isPartOf": "DOT-304",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/economicrecovery/",
+            "landingPage": "https://data.transportation.gov/d/ezjk-jjx7",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-4308",
             "primaryITInvestmentUII": "021-803057200",
             "programCode": [
                 "021:000"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/economicrecovery/",
-                    "mediaType": "text/html"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "references": [
+                "http://www.fhwa.dot.gov/economicrecovery/"
             ],
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/economicrecovery/",
+            "temporal": "2009-01-01/2011-01-18",
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
+            "title": "Federal Highway Administration American Recovery and Reinvestment Act of 2009 Policy and Guidance -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ezry-n9vi",
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
-            "identifier": "https://data.transportation.gov/api/views/ezry-n9vi",
             "description": "Autos include all passenger cars, including station wagons. The U.S. Bureau of Economic Analysis releases auto and truck sales data, which are used in the preparation of estimates of personal consumption expenditures.",
-            "title": "Auto Sales Seasonally Adjusted Annual Rate (SAAR)",
+            "identifier": "https://data.transportation.gov/api/views/ezry-n9vi",
+            "issued": "2025-01-02",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ezry-n9vi",
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
+            "title": "Auto Sales Seasonally Adjusted Annual Rate (SAAR)"
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
-            "landingPage": "https://data.transportation.gov/d/f4sa-r8m7",
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
-            "identifier": "18.127",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - February 2004",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48528,51 +48506,90 @@
                     "title": "February 2004"
                 }
             ],
+            "identifier": "18.127",
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
+            "landingPage": "https://data.transportation.gov/d/f4sa-r8m7",
+            "language": [
+                "en-US"
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
+            "title": "Monthly Traffic Volume Trends - February 2004"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/f4xs-qfzx",
-            "issued": "2024-04-05",
             "@type": "dcat:Dataset",
-            "modified": "2024-04-05",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sean Jahanmir",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/f4xs-qfzx",
+            "issued": "2024-04-05",
+            "landingPage": "https://data.transportation.gov/d/f4xs-qfzx",
+            "modified": "2024-04-05",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Chapter 4. Economic Characteristics of Passenger Travel"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/f59h-qd39",
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
+            "identifier": "678.1",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -48586,78 +48603,40 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 NHS",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/f59h-qd39",
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 NHS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2022-06-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "fatalities",
-                "fatality",
-                "highway mileage",
-                "mileage",
-                "roadway & bridges",
-                "travel",
-                "vehicle miles traveled"
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
-            "identifier": "https://data.transportation.gov/api/views/f6w3-9e37",
+            "dataQuality": true,
             "description": "The Summary Statistics dashboard includes rural and urban measures for roadway mileage, lane miles, vehicle miles traveled, fatalities, and fatality rate.",
-            "title": "Select Summary Statistics Dashboard data",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48665,84 +48644,120 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/f6w3-9e37/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/f6w3-9e37/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/f6w3-9e37/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/f6w3-9e37/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/f6w3-9e37/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/f6w3-9e37/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/f6w3-9e37/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/f6w3-9e37/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/f6w3-9e37/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/f6w3-9e37",
+            "issued": "2022-06-02",
+            "keyword": [
+                "fatalities",
+                "fatality",
+                "highway mileage",
+                "mileage",
+                "roadway & bridges",
+                "travel",
+                "vehicle miles traveled"
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
+            "title": "Select Summary Statistics Dashboard data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/f74i-v6w2",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "List of subtopics within Government Transportation Revenues and Expenditures topic in Transportation Economic Trends.",
+            "identifier": "https://data.transportation.gov/api/views/f74i-v6w2",
             "issued": "2020-05-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-23",
             "keyword": [
                 "government transportation expenditures",
                 "government transportation revenue",
                 "transportation finance"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/f74i-v6w2",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-09-23",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/f74i-v6w2",
-            "description": "List of subtopics within Government Transportation Revenues and Expenditures topic in Transportation Economic Trends.",
-            "title": "Transportation Economic Trends: Government Transportation Revenue and Expenditure - Table of Contents",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Transportation Economic Trends: Government Transportation Revenue and Expenditure - Table of Contents"
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
-            "landingPage": "https://data.transportation.gov/d/f7ai-zrgk",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/06dectvt/06dectvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "December 2006"
+                }
             ],
+            "identifier": "18.93",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -48752,60 +48767,61 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.93",
+            "landingPage": "https://data.transportation.gov/d/f7ai-zrgk",
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
-            "title": "Monthly Traffic Volume Trends - December 2006",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/06dectvt/06dectvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "December 2006"
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
+            "title": "Monthly Traffic Volume Trends - December 2006"
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
-            "landingPage": "https://data.transportation.gov/d/f7gq-ydnp",
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
+                    "description": "This access point provides access to the LTPP InfoPave analysis features including LTPP research matrix and interactive data analysis plan.",
+                    "downloadURL": "https://infopave.fhwa.dot.gov/%3FGoto=Analysis",
+                    "mediaType": "application/atom+xml",
+                    "title": "Analysis"
+                }
             ],
+            "identifier": "679.7",
+            "isPartOf": "DOT-679",
+            "issued": "1993-07-01",
             "keyword": [
                 "asphalt concrete",
                 "continuously reinforced concrete pavement",
@@ -48822,55 +48838,43 @@
                 "texture",
                 "traffic loading"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "679.7",
+            "landingPage": "https://data.transportation.gov/d/f7gq-ydnp",
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
-            "title": "Long-Term Pavement Performance (LTPP) - Analysis",
-            "isPartOf": "DOT-679",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/research/tfhrc/programs/infrastructure/pavements/ltpp/",
-            "programCode": [
-                "021:009"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/atom+xml",
-                    "downloadURL": "https://infopave.fhwa.dot.gov/%3FGoto=Analysis",
-                    "description": "This access point provides access to the LTPP InfoPave analysis features including LTPP research matrix and interactive data analysis plan.",
-                    "@type": "dcat:Distribution",
-                    "title": "Analysis"
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
+            "title": "Long-Term Pavement Performance (LTPP) - Analysis"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/f7sr-d4s8",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Transportation Analysis",
+                "hasEmail": "mailto:long.nguyen@dot.gov"
+            },
+            "description": "Freight Facts and Figures - Freight Transportation Energy Use and Environmental Impacts",
+            "identifier": "https://data.transportation.gov/api/views/f7sr-d4s8",
             "issued": "2019-09-24",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-23",
             "keyword": [
                 "bts",
                 "bureau of transportation statistics",
@@ -48882,61 +48886,39 @@
                 "freight facts & figures",
                 "freight transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Transportation Analysis",
-                "hasEmail": "mailto:long.nguyen@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/f7sr-d4s8",
+            "modified": "2024-07-23",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statisitics"
             },
-            "identifier": "https://data.transportation.gov/api/views/f7sr-d4s8",
-            "description": "Freight Facts and Figures - Freight Transportation Energy Use and Environmental Impacts",
-            "title": "Freight Transportation Energy Use & Environmental Impacts",
-            "programCode": [
-                "021:053"
-            ],
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Freight Transportation Energy Use & Environmental Impacts"
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
-            "landingPage": "https://data.transportation.gov/d/f7v6-sxk5",
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
-            "identifier": "364.3",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database - Vehicle Test Query by Vehicle Table Parameters",
-            "isPartOf": "DOT-364",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
-            "primaryITInvestmentUII": "021-621341357",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -48945,35 +48927,68 @@
                     "title": "Vehicle Test Query by Vehicle Table Parameters"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.3",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/f7v6-sxk5",
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
+            "title": "Vehicle Safety Research and Development Database - Vehicle Test Query by Vehicle Table Parameters"
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
-            "landingPage": "https://data.transportation.gov/d/f8aq-ba7k",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/04jultvt/04Jultvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "July 2004"
+                }
             ],
+            "identifier": "18.122",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -48983,120 +48998,109 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.122",
+            "landingPage": "https://data.transportation.gov/d/f8aq-ba7k",
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
-            "title": "Monthly Traffic Volume Trends - July 2004",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/04jultvt/04Jultvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "July 2004"
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
+            "title": "Monthly Traffic Volume Trends - July 2004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/f8um-w6eh",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRA Safety Data Team",
+                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This is a report for trespasser and suicide data, not at highway-rail crossings.",
+            "identifier": "https://data.transportation.gov/api/views/f8um-w6eh",
             "issued": "2024-09-26",
-            "@type": "dcat:Dataset",
+            "keyword": [
+                "suicide",
+                "trespasser"
+            ],
+            "landingPage": "https://data.transportation.gov/d/f8um-w6eh",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2025-01-27",
-            "keyword": [
-                "suicide",
-                "trespasser"
+            "programCode": [
+                "FRA Safety and Operations"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRA Safety Data Team",
-                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
-            },
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Railroad Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/f8um-w6eh",
-            "description": "This is a report for trespasser and suicide data, not at highway-rail crossings.",
-            "title": "Trespassers (not at Highway-Rail Crossings), including Suicides (2.07)",
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
+            "title": "Trespassers (not at Highway-Rail Crossings), including Suicides (2.07)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/f9e6-x6x6",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "MARAD-Datahub",
+                "hasEmail": "mailto:data.marad@dot.gov"
+            },
+            "description": "A listing of oceangoing, self-propelled, privately-owned U.S.-flag vessels of 1,000 gross tons and above that carry cargo from port to port for commercial and government  customers",
+            "identifier": "https://data.transportation.gov/api/views/f9e6-x6x6",
             "issued": "2022-05-02",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-09",
             "keyword": [
                 "jones act",
                 "maritime",
                 "merchant fleet"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "MARAD-Datahub",
-                "hasEmail": "mailto:data.marad@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/f9e6-x6x6",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2022-05-09",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/f9e6-x6x6",
-            "description": "A listing of oceangoing, self-propelled, privately-owned U.S.-flag vessels of 1,000 gross tons and above that carry cargo from port to port for commercial and government  customers",
-            "title": "US Flag Fleet List - January 2022 - Report Summary",
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Maritime and Waterways"
-            ]
+            ],
+            "title": "US Flag Fleet List - January 2022 - Report Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/f9jm-cqwe",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "A look at the consumer price index and producer price index for transportation as a measure of transportation inflation.",
+            "identifier": "https://data.transportation.gov/api/views/f9jm-cqwe",
             "issued": "2022-08-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
             "keyword": [
                 "consumer price index",
                 "cpi",
@@ -49104,59 +49108,35 @@
                 "inflation and transportation",
                 "transportation inflation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/f9jm-cqwe",
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
-            "identifier": "https://data.transportation.gov/api/views/f9jm-cqwe",
-            "description": "A look at the consumer price index and producer price index for transportation as a measure of transportation inflation.",
-            "title": "Transportation and Inflation",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Transportation and Inflation"
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
-            "identifier": "https://data.transportation.gov/api/views/f9t2-7xn2",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 1995",
-            "title": "Historic HPMS Data (Sample) - 1995",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49164,47 +49144,85 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/f9t2-7xn2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/f9t2-7xn2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/f9t2-7xn2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/f9t2-7xn2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/f9t2-7xn2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/f9t2-7xn2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/f9t2-7xn2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/f9t2-7xn2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/f9t2-7xn2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/f9t2-7xn2",
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
+            "title": "Historic HPMS Data (Sample) - 1995"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/fa3i-u3ht",
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
+                    "description": "2013 Wisconsin HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/wisconsin2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Wisconsin"
+                }
+            ],
+            "identifier": "678.152",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -49218,58 +49236,51 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.152",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Wisconsin",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/fa3i-u3ht",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/wisconsin2013.zip",
-                    "description": "2013 Wisconsin HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Wisconsin"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Wisconsin"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.21949/1503752",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2017-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2017-01-05",
-            "references": [
-                "https://rosap.ntl.bts.gov/view/dot/31810"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Transportation Library Data Curator",
+                "hasEmail": "mailto:ntldatacurator@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This zip file contains files of data to support FHWA-JPO-16-370, Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs - San Mateo Testbed Analysis Plan : Final Report. Zip size is 1.5 GB. The files have been uploaded as-is; no further documentation was supplied by NTL. All located .docx files were copied to .pdf document files which are an archival format. These .pdfs were then added to the zip file alongside the original .docx files. The attached zip files can be unzipped using any zip compression/decompression software. These zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .docx document files which may be opened with Microsoft Word or some other open source document editors; .xlsx spreadsheet files which may be opened with Microsoft Excel or some other open source spreadsheet editors; .syn files are a proprietary file format for signal timing plans which are provided in the Synchro Model given as \u201cEl Camino Real Synchro.syn\u201d and can be opened using Trafficware Synchro, which  may require users to purchase a license or software (for more information go to http://www.trafficware.com/); .csv data files, an open format, which may be opened with any text editor or in many spreadsheet applications; .db generic database files, often associated with thumbnail images in the Windows operating environment; .rbc files, which are scripts written in Rembo-C, which can be opened in a text editor, but require a server with Rembo installed to run the scripts; .vap audio files which will require special audio editing software to manipulate; .dll dynamically linked files for Windows program operations; .layx, a file type on which we could not locate reliable information; and .inpx files, a file type on which we could not locate reliable information [software requirements]. These files were last accessed in 2017.  Files were accessed in 2017. Data will be preserved as is.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "This zip file contains files of data to support FHWA-JPO-16-370, Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs - San Mateo Testbed Analysis Plan : Final Report. Zip size is 1.5 GB. The files have been uploaded as-is; no further documentation was supplied by NTL. All located .docx files were copied to .pdf document files which are an archival format. These .pdfs were then added to the zip file alongside the original .docx files. The attached zip files can be unzipped using any zip compression/decompression software. These zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .docx document files which may be opened with Microsoft Word or some other open source document editors; .xlsx spreadsheet files which may be opened with Microsoft Excel or some other open source spreadsheet editors; .syn files are a proprietary file format for signal timing plans which are provided in the Synchro Model given as \u201cEl Camino Real Synchro.syn\u201d and can be opened using Trafficware Synchro, which  may require users to purchase a license or software (for more information go to http://www.trafficware.com/); .csv data files, an open format, which may be opened with any text editor or in many spreadsheet applications; .db generic database files, often associated with thumbnail images in the Windows operating environment; .rbc files, which are scripts written in Rembo-C, which can be opened in a text editor, but require a server with Rembo installed to run the scripts; .vap audio files which will require special audio editing software to manipulate; .dll dynamically linked files for Windows program operations; .layx, a file type on which we could not locate reliable information; and .inpx files, a file type on which we could not locate reliable information [software requirements]. These files were last accessed in 2017.  Files were accessed in 2017. Data will be preserved as is",
+                    "downloadURL": "https://doi.org/10.21949/1503752",
+                    "mediaType": "application/zip",
+                    "title": "Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs: San Mateo Testbed Analysis Plan [supporting datasets]"
+                }
             ],
+            "identifier": "https://data.transportation.gov/api/views/faae-ej8x",
+            "issued": "2017-06-26",
             "keyword": [
                 "active transportation and demand management",
                 "ams san mateo",
@@ -49285,51 +49296,55 @@
                 "traffic flow",
                 "travel demand"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Transportation Library Data Curator",
-                "hasEmail": "mailto:ntldatacurator@dot.gov"
-            },
+            "landingPage": "https://doi.org/10.21949/1503752",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2017-01-05",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/faae-ej8x",
-            "description": "This zip file contains files of data to support FHWA-JPO-16-370, Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs - San Mateo Testbed Analysis Plan : Final Report. Zip size is 1.5 GB. The files have been uploaded as-is; no further documentation was supplied by NTL. All located .docx files were copied to .pdf document files which are an archival format. These .pdfs were then added to the zip file alongside the original .docx files. The attached zip files can be unzipped using any zip compression/decompression software. These zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .docx document files which may be opened with Microsoft Word or some other open source document editors; .xlsx spreadsheet files which may be opened with Microsoft Excel or some other open source spreadsheet editors; .syn files are a proprietary file format for signal timing plans which are provided in the Synchro Model given as \u201cEl Camino Real Synchro.syn\u201d and can be opened using Trafficware Synchro, which  may require users to purchase a license or software (for more information go to http://www.trafficware.com/); .csv data files, an open format, which may be opened with any text editor or in many spreadsheet applications; .db generic database files, often associated with thumbnail images in the Windows operating environment; .rbc files, which are scripts written in Rembo-C, which can be opened in a text editor, but require a server with Rembo installed to run the scripts; .vap audio files which will require special audio editing software to manipulate; .dll dynamically linked files for Windows program operations; .layx, a file type on which we could not locate reliable information; and .inpx files, a file type on which we could not locate reliable information [software requirements]. These files were last accessed in 2017.  Files were accessed in 2017. Data will be preserved as is.",
-            "title": "Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs: San Mateo Testbed Analysis Plan [supporting datasets]",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://doi.org/10.21949/1503752",
-                    "description": "This zip file contains files of data to support FHWA-JPO-16-370, Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs - San Mateo Testbed Analysis Plan : Final Report. Zip size is 1.5 GB. The files have been uploaded as-is; no further documentation was supplied by NTL. All located .docx files were copied to .pdf document files which are an archival format. These .pdfs were then added to the zip file alongside the original .docx files. The attached zip files can be unzipped using any zip compression/decompression software. These zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .docx document files which may be opened with Microsoft Word or some other open source document editors; .xlsx spreadsheet files which may be opened with Microsoft Excel or some other open source spreadsheet editors; .syn files are a proprietary file format for signal timing plans which are provided in the Synchro Model given as \u201cEl Camino Real Synchro.syn\u201d and can be opened using Trafficware Synchro, which  may require users to purchase a license or software (for more information go to http://www.trafficware.com/); .csv data files, an open format, which may be opened with any text editor or in many spreadsheet applications; .db generic database files, often associated with thumbnail images in the Windows operating environment; .rbc files, which are scripts written in Rembo-C, which can be opened in a text editor, but require a server with Rembo installed to run the scripts; .vap audio files which will require special audio editing software to manipulate; .dll dynamically linked files for Windows program operations; .layx, a file type on which we could not locate reliable information; and .inpx files, a file type on which we could not locate reliable information [software requirements]. These files were last accessed in 2017.  Files were accessed in 2017. Data will be preserved as is",
-                    "@type": "dcat:Distribution",
-                    "title": "Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs: San Mateo Testbed Analysis Plan [supporting datasets]"
-                }
+            "references": [
+                "https://rosap.ntl.bts.gov/view/dot/31810"
             ],
             "spatial": "United States, California, San Mateo",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "language": [
-                "en-US"
-            ]
+            "title": "Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs: San Mateo Testbed Analysis Plan [supporting datasets]"
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
-            "landingPage": "https://data.transportation.gov/d/fadx-f3um",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/08juntvt/08juntvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "June 2008"
+                }
             ],
+            "identifier": "18.75",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -49339,78 +49354,42 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.75",
+            "landingPage": "https://data.transportation.gov/d/fadx-f3um",
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
-            "title": "Monthly Traffic Volume Trends - June 2008",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/08juntvt/08juntvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "June 2008"
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
+            "title": "Monthly Traffic Volume Trends - June 2008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/fb8g-ngam",
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
-            "identifier": "https://data.transportation.gov/api/views/fb8g-ngam",
             "description": "*This is a \"daily difference\" dataset.  See dataset attachment \"FMCSA Dataset Description and Data Definitions - Select Datasets\" for more information.*  Records for each BOC3 agent hired by a carrier/broker/freight forwarder. Each entity must hire a BOC3 agent to represent them in legal matters to obtain operating authority. In some cases, entities may act as their own BOC3 agent. The records in the dataset contain the BOC3 agent\u2019s name and address. The dataset also contains the DOT number and docket number of the represented entity.",
-            "title": "BOC3",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49418,50 +49397,51 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/fb8g-ngam",
+            "issued": "2023-04-14",
+            "keyword": [
+                "active",
+                "for-hire motor carriers",
+                "operating authority",
+                "registration status",
+                "revoked",
+                "suspended"
+            ],
+            "landingPage": "https://data.transportation.gov/d/fb8g-ngam",
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
+            "title": "BOC3"
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
-            "landingPage": "https://data.transportation.gov/d/fbc7-nw4p",
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
-            "identifier": "693.4",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
             "description": "The NBI System is the collection of bridge inspection information and costs associated with bridge replacements of structurally deficient bridges on and off the NHS. This data is collected under the auspices of the National Bridge Inspection Standards (NBIS) as prescribed by law. The NBI System collects the information that is used to determine eligibility for NHS projects, performance measure reporting, NHS penalty determination, and reporting to Congress.  It supports oversight of the NBIS through various report tools, and provides data reporting that supports agency strategic goals.",
-            "title": "National Bridge Inventory System (NBI) - 1995",
-            "isPartOf": "DOT-693",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
-            "primaryITInvestmentUII": "021-012940226",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49470,81 +49450,79 @@
                     "title": "1995"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
-            "dataQuality": true,
+            "identifier": "693.4",
+            "isPartOf": "DOT-693",
+            "issued": "1992-12-31",
+            "keyword": [
+                "bridge",
+                "condition",
+                "deck",
+                "inspection",
+                "structure"
+            ],
+            "landingPage": "https://data.transportation.gov/d/fbc7-nw4p",
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
+            "title": "National Bridge Inventory System (NBI) - 1995"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/fbi4-tays",
-            "issued": "2022-04-13",
             "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joe McGill",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "A summary of boarding counts broken down by state and operators.",
             "identifier": "https://data.transportation.gov/api/views/fbi4-tays",
+            "issued": "2022-04-13",
+            "landingPage": "https://data.transportation.gov/d/fbi4-tays",
+            "modified": "2022-04-28",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "A summary of boarding counts broken down by state and operators.",
             "title": "Passenger and Vehicle Boarding Counts"
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
-            "landingPage": "https://data.transportation.gov/d/fbre-hj92",
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
-            "identifier": "18.148",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - May 2002",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49553,35 +49531,72 @@
                     "title": "May 2002"
                 }
             ],
+            "identifier": "18.148",
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
+            "landingPage": "https://data.transportation.gov/d/fbre-hj92",
+            "language": [
+                "en-US"
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
+            "title": "Monthly Traffic Volume Trends - May 2002"
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
-            "landingPage": "https://data.transportation.gov/d/fbt5-4nnr",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/13septvt/13septvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "September 2013"
+                }
             ],
+            "identifier": "18.54",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -49591,64 +49606,39 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.54",
+            "landingPage": "https://data.transportation.gov/d/fbt5-4nnr",
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
-            "title": "Monthly Traffic Volume Trends - September 2013",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/13septvt/13septvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "September 2013"
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
+            "title": "Monthly Traffic Volume Trends - September 2013"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/fccg-bjqh",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-06",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/fccg-bjqh",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "Rail Crossings",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49656,128 +49646,123 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/fccg-bjqh/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/fccg-bjqh/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/fccg-bjqh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/fccg-bjqh/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/fccg-bjqh/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/fccg-bjqh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/fccg-bjqh/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/fccg-bjqh/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/fccg-bjqh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/fccg-bjqh",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/fccg-bjqh",
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
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/fd9d-t7sq",
-            "issued": "2024-12-12",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-12",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:answers@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/fd9d-t7sq",
             "description": "Aircraft seating capacity and average fleet age.",
-            "title": "Fleet Mix",
+            "identifier": "https://data.transportation.gov/api/views/fd9d-t7sq",
+            "issued": "2024-12-12",
+            "landingPage": "https://data.transportation.gov/d/fd9d-t7sq",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-12-12",
             "programCode": [
                 "021:042"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Aviation"
-            ]
+            ],
+            "title": "Fleet Mix"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/fdsx-2s48",
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
-            "identifier": "https://data.transportation.gov/api/views/fdsx-2s48",
             "description": "The Bureau of Transportation Statistics calculates this index based on the American Trucking Association\u2019s monthly Truck Tonnage Index.",
-            "title": "Truck Tonnage Index - Seasonally Adjusted",
+            "identifier": "https://data.transportation.gov/api/views/fdsx-2s48",
+            "issued": "2025-01-21",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/fdsx-2s48",
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
+            "title": "Truck Tonnage Index - Seasonally Adjusted"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www-nrd.nhtsa.dot.gov/Pubs/812069.pdf",
+            "agencyProgramURL": "http://www-nrd.nhtsa.dot.gov/Pubs/812069.pdf",
+            "analysisUnit": "fatalities",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/ffdk-8yjp",
-            "issued": "2015-01-31",
-            "temporal": "2014/2015",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www-nrd.nhtsa.dot.gov/Pubs/812069.pdf"
-            ],
-            "keyword": [
-                "fars; statistical analysis; evaluation; benefits; effec-tiveness; fatality reduction; injury reduction; crashwor-thiness; crash avoidance"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "DOT-1836",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
             "description": "SAS programs and auxiliary files used in report no. DOT HS 812 069, Lives Saved by Vehicle Safety Technologies & Associated FMVSS, 1960 to 2012 Passenger Cars & LTV's",
-            "title": "Lives Saved by Vehicle Safety Technologies and Associated Federal Motor Vehicle Safety Standards",
-            "agencyProgramURL": "http://www-nrd.nhtsa.dot.gov/Pubs/812069.pdf",
-            "programCode": [
-                "021:031"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49786,77 +49771,72 @@
                     "title": "SAS Programs"
                 }
             ],
-            "dataQuality": false,
+            "identifier": "DOT-1836",
+            "issued": "2015-01-31",
+            "keyword": [
+                "fars; statistical analysis; evaluation; benefits; effec-tiveness; fatality reduction; injury reduction; crashwor-thiness; crash avoidance"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ffdk-8yjp",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www-nrd.nhtsa.dot.gov/Pubs/812069.pdf",
+            "modified": "2024-05-01",
+            "phone": "202-366-4696",
+            "programCode": [
+                "021:031"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "http://www-nrd.nhtsa.dot.gov/Pubs/812069.pdf"
+            ],
+            "temporal": "2014/2015",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "analysisUnit": "fatalities",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4696",
-            "language": [
-                "en-US"
-            ]
+            "title": "Lives Saved by Vehicle Safety Technologies and Associated Federal Motor Vehicle Safety Standards"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/fgaw-84ep",
-            "issued": "2022-04-22",
             "@type": "dcat:Dataset",
-            "modified": "2024-05-21",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joe McGill",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "Facts and Figures for the operators of ferry services",
             "identifier": "https://data.transportation.gov/api/views/fgaw-84ep",
+            "issued": "2022-04-22",
+            "landingPage": "https://data.transportation.gov/d/fgaw-84ep",
+            "modified": "2024-05-21",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "Facts and Figures for the operators of ferry services",
             "title": "Ferry Operators"
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
-            "landingPage": "https://data.transportation.gov/d/fgpw-9g4h",
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
-            "identifier": "80.6",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
             "description": "The Child Safety Seat Inspection Station Locations are used to make it easier for all citizens to get their Child Safety Seats properly installed. Car crashes are the largest cause of fatalities and serious injuries for children between ages 2 and 15.  Also, surveys indicate that a high percentage of Child Safety Seats are not installed properly.  Information updates for each station are reported to NHTSA and enterred by NHTSA staff.  NHTSA staff will also attempt to validate the station locations using a comercial Geographic database so this data will, in most cases, be able to be used for driving directions.",
-            "title": "NHTSA Child Safety Seat Inspection Station Locator - NCSSISL - Child Car Seat Inspection Station Locator",
-            "isPartOf": "DOT-80",
-            "agencyProgramURL": "http://www.nhtsa.gov/cps/cpsfitting/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -49865,35 +49845,70 @@
                     "title": "Child Car Seat Inspection Station Locator"
                 }
             ],
-            "spatial": "Zip, State, Geo co-ordinates",
-            "dataQuality": false,
+            "identifier": "80.6",
+            "isPartOf": "DOT-80",
+            "issued": "2010-01-05",
+            "keyword": [
+                "child seat",
+                "inspection",
+                "safety",
+                "station",
+                "stations"
+            ],
+            "landingPage": "https://data.transportation.gov/d/fgpw-9g4h",
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
+            "title": "NHTSA Child Safety Seat Inspection Station Locator - NCSSISL - Child Car Seat Inspection Station Locator"
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
-            "landingPage": "https://data.transportation.gov/d/fh82-r9y7",
-            "issued": "2002-01-01",
-            "temporal": "R/2002-01-31/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-05",
+            "categoryDesignation": "Research",
             "collectionInstrument": "http://www.ntdprogram.gov/ntdprogram/safety.htm",
-            "references": [
-                "http://www.ntdprogram.gov/ntdprogram/safety.htm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John D. Giorgis",
+                "hasEmail": "mailto:john.giorgis@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Summary (\"count\") data submitted to the Safety & Security Module of the NTD.   Reflects counts of incidents, fatalities, injuries, fires, collisions, etc.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/pubs/MonthlyData/S&STimeSeries-July2015-11012015.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Safety & Security Time Series Data"
+                }
             ],
+            "identifier": "22.3",
+            "isPartOf": "DOT-22",
+            "issued": "2002-01-01",
             "keyword": [
                 "bicyclist",
                 "collision",
@@ -49912,117 +49927,84 @@
                 "transit",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John D. Giorgis",
-                "hasEmail": "mailto:john.giorgis@dot.gov"
-            },
-            "identifier": "22.3",
+            "landingPage": "https://data.transportation.gov/d/fh82-r9y7",
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
-            "title": "NTD Safety & Security Summary Data Set - Safety & Security Time Series Data",
-            "isPartOf": "DOT-22",
-            "agencyProgramURL": "http://www.ntdprogram.gov/",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/pubs/MonthlyData/S&STimeSeries-July2015-11012015.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "Safety & Security Time Series Data"
-                }
+            "references": [
+                "http://www.ntdprogram.gov/ntdprogram/safety.htm"
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
+            "title": "NTD Safety & Security Summary Data Set - Safety & Security Time Series Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/fhkw-h7xy",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "This site lists the Transportation Economic Trends (TET) topics, charts and tables, and the schedule of updates.",
+            "identifier": "https://data.transportation.gov/api/views/fhkw-h7xy",
             "issued": "2021-08-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-21",
             "keyword": [
                 "economics",
                 "transportation",
                 "trends"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/fhkw-h7xy",
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
-            "identifier": "https://data.transportation.gov/api/views/fhkw-h7xy",
-            "description": "This site lists the Transportation Economic Trends (TET) topics, charts and tables, and the schedule of updates.",
-            "title": "Transportation Economic Trends Schedule",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Transportation Economic Trends Schedule"
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
-            "landingPage": "https://data.transportation.gov/d/fhz7-hztw",
-            "issued": "2011-01-18",
-            "temporal": "2005-01-01/2011-01-18",
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
                 "fn": "HMIC",
                 "hasEmail": "mailto:PHMSA_Guidance@dot.gov"
             },
-            "identifier": "DOT-326",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Pipeline and Hazardous Materials Safety Administration"
-            },
+            "dataQuality": true,
             "description": "A list of Significant Guidance documents, which include guidance document disseminated to regulated entities or the general public that may reasonably be anticipated to lead to an annual effect on the economy of $100 million or more or adversely affect in a material way the economy, a sector of the economy, productivity, competition, jobs, the environment, public health or safety, or State, local, or tribal governments or communities; create a serious inconsistency or otherwise interfere with an action taken or planned by another agency; materially alter the budgetary impact of entitlements, grants, user fees, or loan programs or the rights and obligations of recipients thereof; or raise novel legal or policy issues arising out of legal mandates, the President's priorities, or the principles set forth in Executive Order 12866, as further amended.",
-            "title": "Significant Guidance on Hazardous Materials Safety Issued by the Pipeline and Hazardous Materials Safety Administration",
-            "agencyProgramURL": "https://www.phmsa.dot.gov/guidance",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50030,34 +50012,66 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "DOT-326",
+            "issued": "2011-01-18",
+            "keyword": [
+                "data.gov",
+                "law",
+                "significant guidance",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/fhz7-hztw",
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
+            "temporal": "2005-01-01/2011-01-18",
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
+            "title": "Significant Guidance on Hazardous Materials Safety Issued by the Pipeline and Hazardous Materials Safety Administration"
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
-            "landingPage": "https://data.transportation.gov/d/fi8b-nngd",
-            "issued": "2011-01-18",
-            "temporal": "2007-01-01/2011-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.rita.dot.gov/freedom_of_information_act/"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DOT Socrata",
+                "hasEmail": "mailto:Socrata@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "FOIA Electronic Reading Room - Final Opinions/Orders in Adjudicated Cases",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.rita.dot.gov/freedom_of_information_act/",
+                    "mediaType": "text/html"
+                }
             ],
+            "identifier": "330.1",
+            "isPartOf": "DOT-330",
+            "issued": "2011-01-18",
             "keyword": [
                 "administrative law",
                 "data.gov",
@@ -50065,83 +50079,41 @@
                 "law",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DOT Socrata",
-                "hasEmail": "mailto:Socrata@dot.gov"
-            },
-            "identifier": "330.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Research and Innovative Technology Administration"
-            },
-            "description": "FOIA Electronic Reading Room - Final Opinions/Orders in Adjudicated Cases",
-            "title": "Administrative Law Judge Opinions issued by the Research and Innovative Technology Administration -",
-            "isPartOf": "DOT-330",
-            "agencyProgramURL": "http://www.rita.dot.gov/freedom_of_information_act/",
+            "landingPage": "https://data.transportation.gov/d/fi8b-nngd",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-14",
+            "phone": "202-366-4308",
             "programCode": [
                 "021:000"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.rita.dot.gov/freedom_of_information_act/",
-                    "mediaType": "text/html"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Research and Innovative Technology Administration"
+            },
+            "references": [
+                "http://www.rita.dot.gov/freedom_of_information_act/"
             ],
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.rita.dot.gov/freedom_of_information_act/",
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
-            "landingPage": "https://data.transportation.gov/d/fib6-v7nq",
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
-            "identifier": "https://data.transportation.gov/api/views/fib6-v7nq",
             "description": "Part of Wyoming Department of Transportation Connected Vehicle Pilot Phase 4. Verify that OBUs use different LTE-V2X Configuration Profiles based on the vehicle's speed.\nHost and remote vehicles travelling below 120 kmph\nHost and remote vehicles travelling above 120 kmph",
-            "title": "LTE-V2X Wyoming Connected Vehicle Pilot test ID WV2IMCT-1 Vehicle 1 70 mph",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50149,47 +50121,89 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/fib6-v7nq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/fib6-v7nq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/fib6-v7nq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/fib6-v7nq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/fib6-v7nq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/fib6-v7nq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/fib6-v7nq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/fib6-v7nq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/fib6-v7nq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Wyoming",
+            "identifier": "https://data.transportation.gov/api/views/fib6-v7nq",
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
+            "landingPage": "https://data.transportation.gov/d/fib6-v7nq",
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
+            "title": "LTE-V2X Wyoming Connected Vehicle Pilot test ID WV2IMCT-1 Vehicle 1 70 mph"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
+            "agencyDataSeriesURL": "http://fragis.frasafety.net/GISFRASafety",
+            "agencyProgramURL": "http://fragis.fra.dot.gov/GISFRASafety/",
+            "analysisUnit": "National Railroad Network",
             "bureauCode": [
                 "021:27"
             ],
-            "landingPage": "https://data.transportation.gov/d/fiti-etxs",
-            "issued": "2007-10-01",
-            "temporal": "R/2007-01-31/P3M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-09",
+            "categoryDesignation": "Geospatial",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://fragis.fra.dot.gov/GISFRASafety/"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The GIS Web Mapping Application is design to have the look and feel as Google Earth. The primary functionality is to provide the user information about FRA's rail lines, rail crossings, freight stations, and mileposting.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://fragis.fra.dot.gov/GISFRASafety/",
+                    "mediaType": "text/html"
+                }
             ],
+            "identifier": "335.2",
+            "isPartOf": "DOT-335",
+            "issued": "2007-10-01",
             "keyword": [
                 "amtrak stations",
                 "grade crossing",
@@ -50205,80 +50219,47 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "335.2",
+            "landingPage": "https://data.transportation.gov/d/fiti-etxs",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-10-09",
+            "phone": "202-493-1343",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Railroad Administration"
             },
-            "description": "The GIS Web Mapping Application is design to have the look and feel as Google Earth. The primary functionality is to provide the user information about FRA's rail lines, rail crossings, freight stations, and mileposting.",
-            "title": "Federal Railroad Administration GIS Web Mapping Application -",
-            "isPartOf": "DOT-335",
-            "agencyProgramURL": "http://fragis.fra.dot.gov/GISFRASafety/",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://fragis.fra.dot.gov/GISFRASafety/",
-                    "mediaType": "text/html"
-                }
+            "references": [
+                "http://fragis.fra.dot.gov/GISFRASafety/"
             ],
             "spatial": "longitude/latitude pair",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://fragis.frasafety.net/GISFRASafety",
+            "temporal": "R/2007-01-31/P3M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P3M",
-            "categoryDesignation": "Geospatial",
-            "analysisUnit": "National Railroad Network",
-            "phone": "202-493-1343",
-            "language": [
-                "en-US"
-            ]
+            "title": "Federal Railroad Administration GIS Web Mapping Application -"
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
-            "landingPage": "https://data.transportation.gov/d/fj64-spq6",
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
-            "identifier": "696.8",
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
@@ -50287,71 +50268,106 @@
                     "title": "History of FHWA"
                 }
             ],
-            "spatial": "National",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "696.8",
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
+            "landingPage": "https://data.transportation.gov/d/fj64-spq6",
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
+            "title": "Highway History - History of FHWA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/fjds-yiin",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This report allows users to generate a Form 6180.71 Crossing Inventory PDF form, Form 6180.57 Highway-Rail Grade Crossing Accident/Incident PDF form and/or map a USDOT Crossing Inventory Number/ID in the FRA Crossing Locator application.",
+            "identifier": "https://data.transportation.gov/api/views/fjds-yiin",
             "issued": "2023-10-25",
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
+            "landingPage": "https://data.transportation.gov/d/fjds-yiin",
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
-            "identifier": "https://data.transportation.gov/api/views/fjds-yiin",
-            "description": "This report allows users to generate a Form 6180.71 Crossing Inventory PDF form, Form 6180.57 Highway-Rail Grade Crossing Accident/Incident PDF form and/or map a USDOT Crossing Inventory Number/ID in the FRA Crossing Locator application.",
-            "title": "Crossing PDF Reports and Crossing Locator Map (5.02)",
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
+            "title": "Crossing PDF Reports and Crossing Locator Map (5.02)"
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
-            "landingPage": "https://data.transportation.gov/d/fju2-6h5s",
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
+                    "description": "This access point provides access to the LTPP Reference Library.  Ability to search the reference library is provided through Google Search Appliance.  Also, access to LTPP IMS Users Guide is provided.",
+                    "downloadURL": "https://infopave.fhwa.dot.gov/%3FGoto=Library",
+                    "mediaType": "text/html",
+                    "title": "Library"
+                }
             ],
+            "identifier": "679.4",
+            "isPartOf": "DOT-679",
+            "issued": "1993-07-01",
             "keyword": [
                 "asphalt concrete",
                 "continuously reinforced concrete pavement",
@@ -50368,119 +50384,81 @@
                 "texture",
                 "traffic loading"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "679.4",
+            "landingPage": "https://data.transportation.gov/d/fju2-6h5s",
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
-            "title": "Long-Term Pavement Performance (LTPP) - Library",
-            "isPartOf": "DOT-679",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/research/tfhrc/programs/infrastructure/pavements/ltpp/",
-            "programCode": [
-                "021:009"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://infopave.fhwa.dot.gov/%3FGoto=Library",
-                    "description": "This access point provides access to the LTPP Reference Library.  Ability to search the reference library is provided through Google Search Appliance.  Also, access to LTPP IMS Users Guide is provided.",
-                    "@type": "dcat:Distribution",
-                    "title": "Library"
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
+            "title": "Long-Term Pavement Performance (LTPP) - Library"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/fjyj-2qqx",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2024-09-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-11",
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
-            "identifier": "https://data.transportation.gov/api/views/fjyj-2qqx",
             "description": "Domestic & international departures by year and by carrier.",
-            "title": "Flights",
+            "identifier": "https://data.transportation.gov/api/views/fjyj-2qqx",
+            "issued": "2024-09-18",
+            "keyword": [
+                "aff",
+                "aviation facts & figures"
+            ],
+            "landingPage": "https://data.transportation.gov/d/fjyj-2qqx",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-10-11",
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
+            "title": "Flights"
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
-            "landingPage": "https://data.transportation.gov/d/fkqb-beg4",
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
-            "identifier": "1840.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/veh/vehdb-export-fields.htm",
             "description": "The NHTSA Vehicle Crash Test Database contains engineering data measured during various types of research, the New Car Assessment Program (NCAP), and compliance crash tests. Information in this database refers to the performance and response of vehicles and other structures in impacts. This database is not intended to support general consumer safety issues. For general consumer information please see the NHTSA's information on buying a safer car.",
-            "title": "Vehicle Crash Test Database - Browse the latest tests",
-            "isPartOf": "DOT-1840",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research",
-            "primaryITInvestmentUII": "021-961265599",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50489,60 +50467,60 @@
                     "title": "Browse the latest tests"
                 }
             ],
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/veh/vehdb-export-fields.htm",
-            "dataQuality": true,
+            "identifier": "1840.2",
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
+            "landingPage": "https://data.transportation.gov/d/fkqb-beg4",
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
+            "title": "Vehicle Crash Test Database - Browse the latest tests"
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
-            "landingPage": "https://data.transportation.gov/d/fkwe-2c3r",
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
-            "identifier": "1840.8",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/veh/vehdb-export-fields.htm",
             "description": "The NHTSA Vehicle Crash Test Database contains engineering data measured during various types of research, the New Car Assessment Program (NCAP), and compliance crash tests. Information in this database refers to the performance and response of vehicles and other structures in impacts. This database is not intended to support general consumer safety issues. For general consumer information please see the NHTSA's information on buying a safer car.",
-            "title": "Vehicle Crash Test Database - Query by vehicle parameters such as make, model, and year",
-            "isPartOf": "DOT-1840",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research",
-            "primaryITInvestmentUII": "021-961265599",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50551,34 +50529,73 @@
                     "title": "Query by vehicle parameters such as make, model, and year"
                 }
             ],
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/veh/vehdb-export-fields.htm",
-            "dataQuality": true,
+            "identifier": "1840.8",
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
+            "landingPage": "https://data.transportation.gov/d/fkwe-2c3r",
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
+            "title": "Vehicle Crash Test Database - Query by vehicle parameters such as make, model, and year"
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
-            "landingPage": "https://data.transportation.gov/d/fmyn-qyh5",
+            "categoryDesignation": "Research",
+            "collectionInstrument": "N/A",
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
+                    "downloadURL": "http://www-odi.nhtsa.dot.gov/downloads/folders/TSBS/FLAT_TSBS.zip",
+                    "mediaType": "application/zip",
+                    "title": "Manufacturer Communications Flat File"
+                }
+            ],
+            "identifier": "83.17",
+            "isPartOf": "DOT-83",
             "issued": "2002-12-16",
-            "temporal": "R/1949-01-01/P1D",
-            "@type": "dcat:Dataset",
-            "collectionInstrument": "N/A",
-            "modified": "2024-05-01",
-            "references": [
-                "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/RCL.txt"
-            ],
             "keyword": [
                 "air bag",
                 "air bags",
@@ -50605,63 +50622,61 @@
                 "vin",
                 "vin search"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "83.17",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Manufacturers who determine that a product or piece of original equipment either has a safety defect or is not in compliance with Federal safety standards are required to notify the National Highway Traffic Safety Administration (NHTSA) within 5 business days. NHTSA requires that manufacturers file a Defect and Noncompliance report as well as quarterly recall status reports, in compliance with Federal Regulation 49 (the National Traffic and Motor Safety Act) Part 573, which identifies the requirements for safety recalls. This information is stored in the NHTSA database. Use this data to search for recall information related to:-\tSpecific NHTSA campaigns -\tProduct types Access to public searches of NHTSA recall databases for tires, vehicles, car seats and equipment.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - Manufacturer Communications Flat File",
-            "isPartOf": "DOT-83",
-            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
-            "describedByType": "text/plain",
+            "landingPage": "https://data.transportation.gov/d/fmyn-qyh5",
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
-                    "downloadURL": "http://www-odi.nhtsa.dot.gov/downloads/folders/TSBS/FLAT_TSBS.zip",
-                    "mediaType": "application/zip",
-                    "title": "Manufacturer Communications Flat File"
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
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - Manufacturer Communications Flat File"
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
-            "landingPage": "https://data.transportation.gov/d/fnch-gyrn",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/08novtvt/08novtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "November 2008"
+                }
             ],
+            "identifier": "18.70",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -50671,60 +50686,61 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.70",
+            "landingPage": "https://data.transportation.gov/d/fnch-gyrn",
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
-            "title": "Monthly Traffic Volume Trends - November 2008",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/08novtvt/08novtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "November 2008"
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
+            "title": "Monthly Traffic Volume Trends - November 2008"
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
-            "landingPage": "https://data.transportation.gov/d/fnhq-3dex",
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
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/gxrabbr.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Hwy/Rail Incidents By State/Railroad"
+                }
             ],
+            "identifier": "214.9",
+            "isPartOf": "DOT-214",
+            "issued": "2010-09-29",
             "keyword": [
                 "accident",
                 "casualty",
@@ -50737,87 +50753,44 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "214.9",
+            "landingPage": "https://data.transportation.gov/d/fnhq-3dex",
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
-            "title": "Highway Rail Accidents - Hwy/Rail Incidents By State/Railroad",
-            "isPartOf": "DOT-214",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/gxrabbr.aspx",
-                    "mediaType": "text/csv",
-                    "title": "Hwy/Rail Incidents By State/Railroad"
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
+            "title": "Highway Rail Accidents - Hwy/Rail Incidents By State/Railroad"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/fnkc-y5dk",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2016-02-17",
-            "@type": "dcat:Dataset",
-            "temporal": "2015-01-12/2015-01-16",
-            "modified": "2016-02-17",
-            "keyword": [
-                "application message",
-                "arterial",
-                "dedicated short range communication (dsrc)",
-                "field test",
-                "freeway",
-                "i-5",
-                "intelligent network flow optimization (inflo)",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "seattle",
-                "traffic management entity-based queue warning (q-warn)",
-                "washington",
-                "washington state department of transportation (wsdot)"
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
-            "identifier": "https://data.transportation.gov/api/views/fnkc-y5dk",
+            "dataQuality": true,
             "description": "Data is from the small-scale demonstration of the Intelligent Network Flow Optimization (INFLO) Prototype System and applications in Seattle, Washington. Connected vehicle systems were deployed in 21 vehicles in a scripted driving scenario circuiting this I-5 corridor northbound and southbound during morning rush hour. This data set contains queue warning messages that were recommended by the INFLO Q-WARN algorithm and sent by the traffic management center to vehicles to warn drivers upstream of the queue. The objective of queue warning is to provide a vehicle operator sufficient warning of impending queue backup in order to brake safely, change lanes, or modify route such that secondary collisions can be minimized or even eliminated.",
-            "title": "Intelligent Network Flow Optimization Prototype Traffic Management Entity-Based Queue Warning",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50825,50 +50798,88 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/fnkc-y5dk/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/fnkc-y5dk/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/fnkc-y5dk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/fnkc-y5dk/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/fnkc-y5dk/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/fnkc-y5dk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/fnkc-y5dk/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/fnkc-y5dk/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/fnkc-y5dk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Seattle, Washington",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/fnkc-y5dk",
+            "issued": "2016-02-17",
+            "keyword": [
+                "application message",
+                "arterial",
+                "dedicated short range communication (dsrc)",
+                "field test",
+                "freeway",
+                "i-5",
+                "intelligent network flow optimization (inflo)",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "seattle",
+                "traffic management entity-based queue warning (q-warn)",
+                "washington",
+                "washington state department of transportation (wsdot)"
+            ],
+            "landingPage": "https://data.transportation.gov/d/fnkc-y5dk",
+            "language": [
+                "en-US"
+            ],
             "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "irregular",
+            "modified": "2016-02-17",
+            "programCode": [
+                "021:013"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
+            "spatial": "Seattle, Washington",
+            "temporal": "2015-01-12/2015-01-16",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Intelligent Network Flow Optimization Prototype Traffic Management Entity-Based Queue Warning"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.21949/1503756",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2015-01-27",
-            "@type": "dcat:Dataset",
-            "modified": "2016-02-23",
-            "references": [
-                "https://rosap.ntl.bts.gov/view/dot/3553"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Transportation Library Data Curator",
+                "hasEmail": "mailto:ntldatacurator@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The datasets in this zip file are in support of Intelligent Transportation Systems Joint Program Office (ITS JPO) report FHWA-JPO-14-134, \"Dynamic Mobility Applications Policy Analysis: Policy and Institutional Issues for Integrated Dynamic Transit Operations (IDTO)\": https://rosap.ntl.bts.gov/view/dot/3553 The compressed zip file totals 0.6 GB in size. The zip file have been uploaded as-is; no further documentation was supplied by NTL, excepted as noted: All located .docx files were converted to .pdf document files which are an archival format. These pdfs were then added to the zip file alongside the original .docx files. The zip file can be unzipped using any zip compression/decompression software. This zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .cvs text files which can be read using any text editor; .docx document files which can be read in Microsoft Word and some other word processing programs; . xlsx spreadsheet files which can be read in Microsoft Excel and some other spreadsheet programs [software requirements]. These files were last accessed in 2017. To view the related publication see: https://rosap.ntl.bts.gov/view/dot/3553 Other related publications can also be found in the ITSJPO collection in ROSA P: https://rosap.ntl.bts.gov/cbrowse?pid=dot%3A239&parentId=dot%3A239",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The datasets in this zip file are in support of Intelligent Transportation Systems Joint Program Office (ITS JPO) report FHWA-JPO-14-134, \"Dynamic Mobility Applications Policy Analysis: Policy and Institutional Issues for Integrated Dynamic Transit Operations (IDTO)\": https://rosap.ntl.bts.gov/view/dot/3553 The compressed zip file totals 0.6 GB in size. The zip file have been uploaded as-is; no further documentation was supplied by NTL, excepted as noted: All located .docx files were converted to .pdf document files which are an archival format. These pdfs were then added to the zip file alongside the original .docx files. The zip file can be unzipped using any zip compression/decompression software. This zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .cvs text files which can be read using any text editor; .docx document files which can be read in Microsoft Word and some other word processing programs; . xlsx spreadsheet files which can be read in Microsoft Excel and some other spreadsheet programs [software requirements]. These files were last accessed in 2017. To view the related publication see: https://rosap.ntl.bts.gov/view/dot/3553 Other related publications can also be found in the ITSJPO collection in ROSA P: https://rosap.ntl.bts.gov/cbrowse?pid=dot%3A239&parentId=dot%3A239",
+                    "downloadURL": "https://doi.org/10.21949/1503756",
+                    "mediaType": "application/zip",
+                    "title": "Dynamic Mobility Applications Policy Analysis: Policy and Institutional Issues for Integrated Dynamic Transit Operations (IDTO) [supporting datasets]"
+                }
             ],
+            "identifier": "https://data.transportation.gov/api/views/fnqc-9yjf",
+            "issued": "2015-01-27",
             "keyword": [
                 "data collection",
                 "integrated dynamic transit operations (idto)",
@@ -50877,63 +50888,37 @@
                 "ridesharing",
                 "trip purpose"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Transportation Library Data Curator",
-                "hasEmail": "mailto:ntldatacurator@dot.gov"
-            },
+            "landingPage": "https://doi.org/10.21949/1503756",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2016-02-23",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/fnqc-9yjf",
-            "description": "The datasets in this zip file are in support of Intelligent Transportation Systems Joint Program Office (ITS JPO) report FHWA-JPO-14-134, \"Dynamic Mobility Applications Policy Analysis: Policy and Institutional Issues for Integrated Dynamic Transit Operations (IDTO)\": https://rosap.ntl.bts.gov/view/dot/3553 The compressed zip file totals 0.6 GB in size. The zip file have been uploaded as-is; no further documentation was supplied by NTL, excepted as noted: All located .docx files were converted to .pdf document files which are an archival format. These pdfs were then added to the zip file alongside the original .docx files. The zip file can be unzipped using any zip compression/decompression software. This zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .cvs text files which can be read using any text editor; .docx document files which can be read in Microsoft Word and some other word processing programs; . xlsx spreadsheet files which can be read in Microsoft Excel and some other spreadsheet programs [software requirements]. These files were last accessed in 2017. To view the related publication see: https://rosap.ntl.bts.gov/view/dot/3553 Other related publications can also be found in the ITSJPO collection in ROSA P: https://rosap.ntl.bts.gov/cbrowse?pid=dot%3A239&parentId=dot%3A239",
-            "title": "Dynamic Mobility Applications Policy Analysis: Policy and Institutional Issues for Integrated Dynamic Transit Operations (IDTO) [supporting datasets]",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://doi.org/10.21949/1503756",
-                    "description": "The datasets in this zip file are in support of Intelligent Transportation Systems Joint Program Office (ITS JPO) report FHWA-JPO-14-134, \"Dynamic Mobility Applications Policy Analysis: Policy and Institutional Issues for Integrated Dynamic Transit Operations (IDTO)\": https://rosap.ntl.bts.gov/view/dot/3553 The compressed zip file totals 0.6 GB in size. The zip file have been uploaded as-is; no further documentation was supplied by NTL, excepted as noted: All located .docx files were converted to .pdf document files which are an archival format. These pdfs were then added to the zip file alongside the original .docx files. The zip file can be unzipped using any zip compression/decompression software. This zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .cvs text files which can be read using any text editor; .docx document files which can be read in Microsoft Word and some other word processing programs; . xlsx spreadsheet files which can be read in Microsoft Excel and some other spreadsheet programs [software requirements]. These files were last accessed in 2017. To view the related publication see: https://rosap.ntl.bts.gov/view/dot/3553 Other related publications can also be found in the ITSJPO collection in ROSA P: https://rosap.ntl.bts.gov/cbrowse?pid=dot%3A239&parentId=dot%3A239",
-                    "@type": "dcat:Distribution",
-                    "title": "Dynamic Mobility Applications Policy Analysis: Policy and Institutional Issues for Integrated Dynamic Transit Operations (IDTO) [supporting datasets]"
-                }
+            "references": [
+                "https://rosap.ntl.bts.gov/view/dot/3553"
             ],
             "spatial": "United States",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "language": [
-                "en-US"
-            ]
+            "title": "Dynamic Mobility Applications Policy Analysis: Policy and Institutional Issues for Integrated Dynamic Transit Operations (IDTO) [supporting datasets]"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/fphd-jyyj",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
-            "keyword": [
-                "capital expenses",
-                "expenditure",
-                "transit expansion"
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
-            "identifier": "https://data.transportation.gov/api/views/fphd-jyyj",
             "description": "This dataset details capital expenses by capital use type (existing or expansion) for each applicable agency, mode, and type of service (TOS) reporting to the National Transit Database in the 2022 and 2023 report years.\n\nNTD Data Tables organize and summarize data from the 2022 and 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. This dataset is based on the 2022 and 2023 Capital Use database files.\n\nIn years 2015-2021, you can find this data in the \"Capital Expenses\" data table on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.\n\nIf you have any other questions about this table, please contact the NTD Help Desk at NTDHelp@dot.gov.",
-            "title": "2022 - 2023 NTD Annual Data - Capital Expenses (by Capital Use)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -50941,64 +50926,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/fphd-jyyj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/fphd-jyyj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/fphd-jyyj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/fphd-jyyj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/fphd-jyyj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/fphd-jyyj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/fphd-jyyj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/fphd-jyyj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/fphd-jyyj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/fphd-jyyj",
+            "issued": "2024-09-10",
+            "keyword": [
+                "capital expenses",
+                "expenditure",
+                "transit expansion"
+            ],
+            "landingPage": "https://data.transportation.gov/d/fphd-jyyj",
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
+            "title": "2022 - 2023 NTD Annual Data - Capital Expenses (by Capital Use)"
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
-            "identifier": "https://data.transportation.gov/api/views/fq83-y3yp",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 2007",
-            "title": "Historic HPMS Data (Sample) - 2007",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51006,104 +50986,139 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/fq83-y3yp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/fq83-y3yp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/fq83-y3yp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/fq83-y3yp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/fq83-y3yp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/fq83-y3yp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/fq83-y3yp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/fq83-y3yp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/fq83-y3yp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/fq83-y3yp",
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
+            "title": "Historic HPMS Data (Sample) - 2007"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/fr95-2sc8",
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
             "identifier": "https://data.transportation.gov/api/views/fr95-2sc8",
+            "issued": "2021-01-21",
+            "landingPage": "https://data.transportation.gov/d/fr95-2sc8",
+            "modified": "2021-01-21",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Monthly Transportation Statistics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/fr96-cce8",
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
-            "identifier": "https://data.transportation.gov/api/views/fr96-cce8",
             "description": "Unemployed persons are people aged 16 years or older who had no employment, are available for work, except for temporary illness, and make no specific efforts to find employment in the past four weeks. The Bureau of Labor Statistics produces industry estimates of nonfarm payroll employment as part of the Current Population Survey. Employment data are seasonally adjusted to remove the effects of normal seasonal variation.",
-            "title": "Unemployed - Seasonally Adjusted",
+            "identifier": "https://data.transportation.gov/api/views/fr96-cce8",
+            "issued": "2025-01-02",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/fr96-cce8",
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
+            "title": "Unemployed - Seasonally Adjusted"
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
-            "landingPage": "https://data.transportation.gov/d/fr9q-sicm",
-            "issued": "2010-07-15",
-            "temporal": "R/2009-10-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://ai.fmcsa.dot.gov/HazmatStat/Default.aspx"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The reports listed below are designed to provide information focused on hazardous materials and carriers and the hazardous materials safety permit program. All reports provide options to choose fiscal or calendar year, and carrier domicile including United States, Canada, and Mexico.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://ai.fmcsa.dot.gov/HazmatStat/Default.aspx",
+                    "mediaType": "text/html",
+                    "title": "Hazardous Materials Safety Data"
+                }
             ],
+            "identifier": "120.1",
+            "isPartOf": "DOT-120",
+            "issued": "2010-07-15",
             "keyword": [
                 "bulk",
                 "compliance review",
@@ -51120,79 +51135,43 @@
                 "shipper",
                 "violation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "120.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
-            "description": "The reports listed below are designed to provide information focused on hazardous materials and carriers and the hazardous materials safety permit program. All reports provide options to choose fiscal or calendar year, and carrier domicile including United States, Canada, and Mexico.",
-            "title": "A&I - Hazardous Materials Carrier - Hazardous Materials Safety Data",
-            "isPartOf": "DOT-120",
-            "agencyProgramURL": "http://ai.fmcsa.dot.gov/HazmatStat/Default.aspx",
+            "landingPage": "https://data.transportation.gov/d/fr9q-sicm",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-24",
+            "phone": "202-366-2161",
             "primaryITInvestmentUII": "021-534052663",
             "programCode": [
                 "021:022"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://ai.fmcsa.dot.gov/HazmatStat/Default.aspx",
-                    "mediaType": "text/html",
-                    "title": "Hazardous Materials Safety Data"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "references": [
+                "http://ai.fmcsa.dot.gov/HazmatStat/Default.aspx"
             ],
             "spatial": "National, State",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/HazmatStat/Default.aspx",
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
-            "landingPage": "https://data.transportation.gov/d/frme-pssc",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-07-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-21",
-            "keyword": [
-                "local",
-                "person miles traveled",
-                "person trips",
-                "travel",
-                "vehicle miles traveled",
-                "vehicle trips"
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
-            "identifier": "https://data.transportation.gov/api/views/frme-pssc",
             "description": "Estimates of average weekday household person trips, vehicle trips, person miles traveled, and vehicle miles traveled (per day), for all Census tracts in the United States for 2009.\r\n\r\nFor latest data (2017), see https://data.bts.gov/Research-and-Statistics/Local-Area-Transportation-Characteristics-by-House/va72-z8hz\r\n\r\nFor methodology, see attachments",
-            "title": "Local Area Transportation Characteristics by Household 2009",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51200,83 +51179,119 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/frme-pssc/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/frme-pssc/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/frme-pssc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/frme-pssc/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/frme-pssc/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/frme-pssc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/frme-pssc/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/frme-pssc/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/frme-pssc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/frme-pssc",
+            "issued": "2024-07-01",
+            "keyword": [
+                "local",
+                "person miles traveled",
+                "person trips",
+                "travel",
+                "vehicle miles traveled",
+                "vehicle trips"
+            ],
+            "landingPage": "https://data.transportation.gov/d/frme-pssc",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-08-21",
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
+            "title": "Local Area Transportation Characteristics by Household 2009"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.bts.gov/stories/s/fseh-ipec",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "List of Bureau of Transportation Statistics bikeshare (docked and dockless) and e-scooter data and visualizations.",
+            "identifier": "https://data.transportation.gov/api/views/fseh-ipec",
             "issued": "2021-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-30",
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
+            "landingPage": "https://data.bts.gov/stories/s/fseh-ipec",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-09-30",
+            "phone": "202-366-DATA(3282)",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/fseh-ipec",
-            "description": "List of Bureau of Transportation Statistics bikeshare (docked and dockless) and e-scooter data and visualizations.",
-            "title": "Bikeshare and E-scooter Table of Contents",
-            "programCode": [
-                "021:053"
-            ],
             "spatial": "United States",
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Bicycles and Pedestrians"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Bikeshare and E-scooter Table of Contents"
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
-            "landingPage": "https://data.transportation.gov/d/ft73-x4fr",
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
+            "identifier": "124.1",
+            "isPartOf": "DOT-124",
+            "issued": "2000-01-01",
             "keyword": [
                 "90 day failure to pay.",
                 "bus",
@@ -51295,57 +51310,60 @@
                 "safety and fitness electronic records",
                 "unsatifactory = unfit"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "124.1",
+            "landingPage": "https://data.transportation.gov/d/ft73-x4fr",
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
-            "title": "SAFER - Out of Service Orders - FMCSA Out of Service Orders",
-            "isPartOf": "DOT-124",
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
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Out of Service Motor Carriers",
-            "phone": "202-493-0215",
-            "language": [
-                "en-US"
-            ]
+            "title": "SAFER - Out of Service Orders - FMCSA Out of Service Orders"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/ftc3-uc4y",
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
+                    "description": "2011 Florida HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/florida2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Florida"
+                }
+            ],
+            "identifier": "678.11",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -51359,60 +51377,58 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.11",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Florida",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/ftc3-uc4y",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/florida2011.zip",
-                    "description": "2011 Florida HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Florida"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Florida"
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
-            "landingPage": "https://data.transportation.gov/d/ftjg-drvn",
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
+            "identifier": "286.1",
+            "isPartOf": "DOT-286",
+            "issued": "2013-03-20",
             "keyword": [
                 "commodity",
                 "consumption",
@@ -51437,79 +51453,43 @@
                 "value",
                 "wear"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "286.1",
+            "landingPage": "https://data.transportation.gov/d/ftjg-drvn",
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
-            "title": "Freight Analysis Framework - Regional Data base for 2007 with forecasts through 2040",
-            "isPartOf": "DOT-286",
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
+            "title": "Freight Analysis Framework - Regional Data base for 2007 with forecasts through 2040"
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
-            "identifier": "https://data.transportation.gov/api/views/fued-gbsq",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 1980",
-            "title": "Historic HPMS Data (Sample) - 1981",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51517,67 +51497,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/fued-gbsq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/fued-gbsq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/fued-gbsq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/fued-gbsq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/fued-gbsq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/fued-gbsq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/fued-gbsq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/fued-gbsq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/fued-gbsq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/fued-gbsq",
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
+            "title": "Historic HPMS Data (Sample) - 1981"
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
-            "landingPage": "https://data.transportation.gov/d/fux9-ij6p",
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
-            "identifier": "DOT-102",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": true,
             "description": "Collects information from the State of Indiana's UCR Payment System.",
-            "title": "Unified Carrier Registration (UCR)",
-            "agencyProgramURL": "http://safer.fmcsa.dot.gov/",
-            "programCode": [
-                "021:026"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51586,35 +51573,63 @@
                     "title": "Online Form"
                 }
             ],
-            "spatial": "State",
-            "dataQuality": true,
+            "identifier": "DOT-102",
+            "issued": "1974-06-01",
+            "keyword": [
+                "carrier",
+                "registration"
+            ],
+            "landingPage": "https://data.transportation.gov/d/fux9-ij6p",
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
+            "title": "Unified Carrier Registration (UCR)"
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
-            "landingPage": "https://data.transportation.gov/d/fv6u-yibx",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/02novtvt/02novtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "November 2002"
+                }
             ],
+            "identifier": "18.142",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -51624,82 +51639,82 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.142",
+            "landingPage": "https://data.transportation.gov/d/fv6u-yibx",
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
-            "title": "Monthly Traffic Volume Trends - November 2002",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/02novtvt/02novtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "November 2002"
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
+            "title": "Monthly Traffic Volume Trends - November 2002"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/fv8r-q32z",
-            "issued": "2020-06-02",
             "@type": "dcat:Dataset",
-            "modified": "2023-06-13",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA Data Team",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/fv8r-q32z",
+            "issued": "2020-06-02",
+            "landingPage": "https://data.transportation.gov/d/fv8r-q32z",
+            "modified": "2023-06-13",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
-            "title": "Socrata User Guide",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "Socrata User Guide"
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
-            "landingPage": "https://data.transportation.gov/d/fvxd-yxbe",
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
+            "identifier": "1837.1",
+            "isPartOf": "DOT-1837",
+            "issued": "2014-06-30",
             "keyword": [
                 "benefit",
                 "effectiveness",
@@ -51708,108 +51723,79 @@
                 "fuel system integrity",
                 "post-crash fires"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "1837.1",
+            "landingPage": "https://data.transportation.gov/d/fvxd-yxbe",
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
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/fwcs-jprj",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Bikeshare and e-scooters are types of micromobility, a category of modes of transportation that includes very light, low-occupancy vehicles such as electric scooters (e-scooters), electric skateboards, shared bicycles, and electric pedal assisted bicycles (e-bikes). Explore trends in micromobility in the U.S. since 2015 using the interactive map, which features docked bikeshare, dockless bikeshare, and e-scooter systems.",
+            "identifier": "https://data.transportation.gov/api/views/fwcs-jprj",
             "issued": "2019-09-19",
-            "@type": "dcat:Dataset",
-            "temporal": "2015 to present",
-            "modified": "2024-11-29",
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
+            "landingPage": "https://data.transportation.gov/d/fwcs-jprj",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-29",
+            "phone": "202-366-DATA(3282)",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/fwcs-jprj",
-            "description": "Bikeshare and e-scooters are types of micromobility, a category of modes of transportation that includes very light, low-occupancy vehicles such as electric scooters (e-scooters), electric skateboards, shared bicycles, and electric pedal assisted bicycles (e-bikes). Explore trends in micromobility in the U.S. since 2015 using the interactive map, which features docked bikeshare, dockless bikeshare, and e-scooter systems.",
-            "title": "Bikeshare and e-scooters in the U.S.",
-            "programCode": [
-                "021:053"
-            ],
             "spatial": "United States",
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2015 to present",
             "theme": [
                 "Bicycles and Pedestrians"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Bikeshare and e-scooters in the U.S."
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/fx4q-ay7w",
             "bureauCode": [
                 "021:17"
             ],
-            "issued": "2024-04-24",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
-            "keyword": [
-                "inspection",
-                "violation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO Office",
                 "hasEmail": "mailto:FMCSA.CDO@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
-            "identifier": "https://data.transportation.gov/api/views/fx4q-ay7w",
             "description": "Federal and State field enforcement staff performs Inspections on Interstate and Intrastate Motor Carriers and Hazardous Materials carriers. Violations of the Federal Motor Carrier Safety Regulations (FMCSRs) severe enough may result in a vehicle and/or driver being placed \"out-of-service.\" The data collected from inspection activity is collected and stored in the FMCSA Motor Carrier Management Information System (MCMIS) Inspection Data Files.\n\nDue to privacy restrictions, driver information is not included in any inspection files released to the public.",
-            "title": "Vehicle Inspection File",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51817,82 +51803,79 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/fx4q-ay7w/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/fx4q-ay7w/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/fx4q-ay7w/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/fx4q-ay7w/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/fx4q-ay7w/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/fx4q-ay7w/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/fx4q-ay7w/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/fx4q-ay7w/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/fx4q-ay7w/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/fx4q-ay7w",
+            "issued": "2024-04-24",
+            "keyword": [
+                "inspection",
+                "violation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/fx4q-ay7w",
             "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2025-02-01",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Trucking and Motorcoaches"
-            ]
+            ],
+            "title": "Vehicle Inspection File"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/fypj-prj5",
-            "issued": "2020-08-14",
             "@type": "dcat:Dataset",
-            "modified": "2021-04-21",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/fypj-prj5",
+            "issued": "2020-08-14",
+            "landingPage": "https://data.transportation.gov/d/fypj-prj5",
+            "modified": "2021-04-21",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
-            "title": "2018-2019 State Rural Local Summary Data",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "2018-2019 State Rural Local Summary Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/fzbb-f6kc",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
-            "keyword": [
-                "lane miles",
-                "rail",
-                "roadway",
-                "track miles",
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
-            "identifier": "https://data.transportation.gov/api/views/fzbb-f6kc",
             "description": "This dataset details track and roadway mileage/characteristics for each agency, mode, and type of service, as reported to the National Transit Database in Report Years 2022 and 2023. These data include the types of track/roadway elements employed in transit operation, as well as the length and/or count of certain elements.\n\nNTD Data Tables organize and summarize data from the 2022 National Transit Database in a manner that is more useful for quick reference and summary analysis. This dataset is based on the 2022 and 2023 Transit Way Mileage database files.\n\nIn years 2015-2021, you can find this data in the \"Track and Roadway\" data table on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.\n\nIn versions of the data tables from before 2015, you can find corresponding data in the file called \"Transit Way Mileage - Rail Modes\" and \"Transit Way Mileage - Non-Rail Modes.\"\n\nIf you have any other questions about this table, please contact the NTD Help Desk at NTDHelp@dot.gov.",
-            "title": "2022 - 2023 NTD Annual Data - Track & Roadway (by Mode)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -51900,46 +51883,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/fzbb-f6kc/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/fzbb-f6kc/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/fzbb-f6kc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/fzbb-f6kc/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/fzbb-f6kc/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/fzbb-f6kc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/fzbb-f6kc/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/fzbb-f6kc/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/fzbb-f6kc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/fzbb-f6kc",
+            "issued": "2024-09-10",
+            "keyword": [
+                "lane miles",
+                "rail",
+                "roadway",
+                "track miles",
+                "transit"
+            ],
+            "landingPage": "https://data.transportation.gov/d/fzbb-f6kc",
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
+            "title": "2022 - 2023 NTD Annual Data - Track & Roadway (by Mode)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://www.fmcsa.dot.gov/safety-security/PCS/Consumers.aspx",
+            "agencyProgramURL": "http://www.fmcsa.dot.gov/safety-security/pcs/Index.aspx",
+            "analysisUnit": "Passenger Company",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/g2u7-b7jh",
-            "issued": "2018-12-17",
-            "temporal": "R/1974-06-01/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.fmcsa.dot.gov/safety-security/PCS/Consumers.aspx"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This Web site is designed to inform passenger carriers and the traveling public about the Federal Motor Carrier Safety Administration's passenger carrier program and regulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fmcsa.dot.gov/safety-security/PCS/Consumers.aspx",
+                    "mediaType": "text/html",
+                    "title": "Data Mining Tool"
+                }
             ],
+            "identifier": "116.1",
+            "isPartOf": "DOT-116",
+            "issued": "2018-12-17",
             "keyword": [
                 "bus",
                 "federal motor carrier safety administration",
@@ -51957,58 +51972,61 @@
                 "sms",
                 "vehicles"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "116.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
-            "description": "This Web site is designed to inform passenger carriers and the traveling public about the Federal Motor Carrier Safety Administration's passenger carrier program and regulations.",
-            "title": "A&I - Bus/Passenger Carrier Information - Data Mining Tool",
-            "isPartOf": "DOT-116",
-            "agencyProgramURL": "http://www.fmcsa.dot.gov/safety-security/pcs/Index.aspx",
+            "landingPage": "https://data.transportation.gov/d/g2u7-b7jh",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-24",
+            "phone": "202-366-2161",
             "primaryITInvestmentUII": "021-000001010",
             "programCode": [
                 "021:022"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fmcsa.dot.gov/safety-security/PCS/Consumers.aspx",
-                    "mediaType": "text/html",
-                    "title": "Data Mining Tool"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "references": [
+                "http://www.fmcsa.dot.gov/safety-security/PCS/Consumers.aspx"
             ],
             "spatial": "State",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fmcsa.dot.gov/safety-security/PCS/Consumers.aspx",
+            "temporal": "R/1974-06-01/P1D",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Passenger Company",
-            "phone": "202-366-2161",
-            "language": [
-                "en-US"
-            ]
+            "title": "A&I - Bus/Passenger Carrier Information - Data Mining Tool"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/g32u-3b4g",
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
+                    "description": "2011 Nevada HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/nevada2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Nevada"
+                }
+            ],
+            "identifier": "678.30",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -52022,73 +52040,39 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.30",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Nevada",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/g32u-3b4g",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/nevada2011.zip",
-                    "description": "2011 Nevada HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Nevada"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Nevada"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/g3h6-334u",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2020-06-27",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
-            "keyword": [
-                "bikeshare"
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
-            "identifier": "https://data.transportation.gov/api/views/g3h6-334u",
             "description": "Historic data updated on 07/14/2023. Q4 of 2023 and data for all years on systems allowing parking outside of a docking station updated on 06/04/2024.\n\nBikeshare ridership by system, year, month, and day for bikeshare systems with docking stations. Data available by month starting in January 2019. Months are rearranged to include the same number of days of the week across years (see below). Data designed to show the impacts of COVID-19 on bikeshare ridership as featured at https://maps.dot.gov/BTS/dockedbikeshare-COVID/\n\nRidership data not available for all docked bikeshare systems. Only docked bikeshare systems with ridership data shown. Some systems included in the data permit users to leave a bicycle outside of a docking station; these trips are not counted. Trips defined as rides from point A to B. If user makes trip from B to A on same day, counted as a second trip. Trips labeled as round trips in Metro Bike Share and Indego trip files counted as 2 trips. Trips with no trip time are not counted. Trips with no start station identifier and/or end station id are not counted in totals. Trips shorter than 1 minute or greater than 2 hours excluded. Days aligned to include the same days of weeks in 2019 and 2020. Days included in each month are as follows:\n\nAssigned month can be found in the attachments (https://data.bts.gov/api/views/6cfa-ipzd/files/36fde1b8-57c3-4d31-b9dc-bbc896ba346e?download=true&filename=days_included_in_docked_bikeshare_monthly_summaries.xlsx) \n\nTrips beginning on 12/31/2019 but ending on 01/01/2020 not included in totals.\n\nInteractive map application featuring data: https://maps.dot.gov/BTS/dockedbikeshare-COVID/",
-            "title": "Docked Bikeshare Ridership by System, Year, Month, and Day",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52096,72 +52080,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/g3h6-334u/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/g3h6-334u/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/g3h6-334u/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/g3h6-334u/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/g3h6-334u/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/g3h6-334u/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/g3h6-334u/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/g3h6-334u/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/g3h6-334u/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/g3h6-334u",
+            "issued": "2020-06-27",
+            "keyword": [
+                "bikeshare"
+            ],
+            "landingPage": "https://data.transportation.gov/d/g3h6-334u",
             "license": "https://www.usa.gov/government-works",
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
+            "title": "Docked Bikeshare Ridership by System, Year, Month, and Day"
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
-            "landingPage": "https://data.transportation.gov/d/g3zm-kb9k",
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
-            "identifier": "320.1",
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
@@ -52169,48 +52148,54 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "320.1",
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
+            "landingPage": "https://data.transportation.gov/d/g3zm-kb9k",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://isearch.nhtsa.gov/",
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
-            "landingPage": "https://data.transportation.gov/d/g43q-hx7i",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2017-04-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "grants",
-                "tiger"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "USDOT"
-            },
-            "identifier": "https://data.transportation.gov/api/views/g43q-hx7i",
+            "dataQuality": true,
             "description": "This data set comprises all TIGER grants rounds up to 2016",
-            "title": "All TIGER Grants 2016",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52218,45 +52203,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/g43q-hx7i/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/g43q-hx7i/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/g43q-hx7i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/g43q-hx7i/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/g43q-hx7i/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/g43q-hx7i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/g43q-hx7i/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/g43q-hx7i/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/g43q-hx7i/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/g43q-hx7i",
+            "issued": "2017-04-28",
+            "keyword": [
+                "grants",
+                "tiger"
+            ],
+            "landingPage": "https://data.transportation.gov/d/g43q-hx7i",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-05-08",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "USDOT"
+            },
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "All TIGER Grants 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/g46y-ughw",
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
+                    "description": "2013 Florida HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/florida2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Florida"
+                }
+            ],
+            "identifier": "678.113",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -52270,60 +52288,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.113",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Florida",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/g46y-ughw",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/florida2013.zip",
-                    "description": "2013 Florida HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Florida"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Florida"
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
-            "landingPage": "https://data.transportation.gov/d/g4ba-q4qi",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/11octtvt/11octtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "October 2011"
+                }
             ],
+            "identifier": "18.5",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -52333,77 +52348,43 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.5",
+            "landingPage": "https://data.transportation.gov/d/g4ba-q4qi",
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
-            "title": "Monthly Traffic Volume Trends - October 2011",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/11octtvt/11octtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "October 2011"
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
+            "title": "Monthly Traffic Volume Trends - October 2011"
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
-            "identifier": "https://data.transportation.gov/api/views/g5nf-5mpb",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 1993",
-            "title": "Historic HPMS Data (Universe) - 1993",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52411,47 +52392,84 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/g5nf-5mpb/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/g5nf-5mpb/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/g5nf-5mpb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/g5nf-5mpb/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/g5nf-5mpb/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/g5nf-5mpb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/g5nf-5mpb/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/g5nf-5mpb/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/g5nf-5mpb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/g5nf-5mpb",
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
+            "title": "Historic HPMS Data (Universe) - 1993"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/g6s7-wjzu",
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
+                    "description": "2012 Utah HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/utah2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Utah"
+                }
+            ],
+            "identifier": "678.98",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -52465,55 +52483,42 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.98",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Utah",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/g6s7-wjzu",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/utah2012.zip",
-                    "description": "2012 Utah HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Utah"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Utah"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/g7gy-chk8",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRA Safety Data Team",
+                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This is the report page for Highway-Rail Grade Crossing Incidents Within Quiet Zones Summary Report.",
+            "identifier": "https://data.transportation.gov/api/views/g7gy-chk8",
             "issued": "2024-09-11",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "crossing inventory",
                 "grade crossing incident",
@@ -52521,68 +52526,43 @@
                 "quiet zone",
                 "train horn"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRA Safety Data Team",
-                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/g7gy-chk8",
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
-            "identifier": "https://data.transportation.gov/api/views/g7gy-chk8",
-            "description": "This is the report page for Highway-Rail Grade Crossing Incidents Within Quiet Zones Summary Report.",
-            "title": "Highway-Rail Grade Crossing Incidents Within Quiet Zones Summary Report",
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
+            "title": "Highway-Rail Grade Crossing Incidents Within Quiet Zones Summary Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.nhtsa.gov/content/nhtsa-ftp/256",
+            "agencyProgramURL": "https://www.nhtsa.gov/national-automotive-sampling-system-nass/nass-general-estimates-system",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/g7u3-etwr",
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
-            "identifier": "DOT-524",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
             "description": "STATE DATA REPORTING SYSTEMS. Annual reports on the Fatality Analysis Reporting System (FARS) which is data regarding fatalities that is collected by a FARS analyst from each State and provided to NHTSA.",
-            "title": "GES Reports",
-            "agencyProgramURL": "https://www.nhtsa.gov/national-automotive-sampling-system-nass/nass-general-estimates-system",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52591,100 +52571,98 @@
                     "title": "SAS Data"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
-            "dataQuality": true,
+            "identifier": "DOT-524",
+            "issued": "1988-12-31",
+            "keyword": [
+                "crashworthiness",
+                "estimation",
+                "fars",
+                "general",
+                "nass",
+                "system"
+            ],
+            "landingPage": "https://data.transportation.gov/d/g7u3-etwr",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "https://www.nhtsa.gov/content/nhtsa-ftp/256",
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
+            "title": "GES Reports"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/g8cu-2jtu",
             "bureauCode": [
                 "021:27"
             ],
-            "issued": "2024-09-26",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
-            "keyword": [
-                "suicide",
-                "trespasser"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Data Team",
                 "hasEmail": "mailto:list-fra-safeteam@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Railroad Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/g8cu-2jtu",
+            "dataQuality": true,
             "description": "This is the report for all trespassers, including suicides.",
-            "title": "Total Trespasser (not at Highway-Rail Crossing at Highway-Rail Crossing), Including Suicides (4.13)",
+            "identifier": "https://data.transportation.gov/api/views/g8cu-2jtu",
+            "issued": "2024-09-26",
+            "keyword": [
+                "suicide",
+                "trespasser"
+            ],
+            "landingPage": "https://data.transportation.gov/d/g8cu-2jtu",
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
+            "title": "Total Trespasser (not at Highway-Rail Crossing at Highway-Rail Crossing), Including Suicides (4.13)"
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
-            "landingPage": "https://data.transportation.gov/d/g8qn-pywp",
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
-            "identifier": "84.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "The National Highway Traffic Safety Administration (NHTSA) has the right to investigate reports of defective products. Information about defective products can come from manufacturers, consumers or law enforcement agencies. NHTSA stores defect investigation information in a database. It uses this information to generate monthly defect reports. It also makes this information available to consumers through the NHTSA web site. You can search for defect investigation information for the following product categories: -\tVehicles -\tEquipment -\tChild Restraints -\tTires",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Investigations - Investigations Flat File",
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
@@ -52693,35 +52671,72 @@
                     "title": "Investigations Flat File"
                 }
             ],
-            "describedBy": "http://www-odi.nhtsa.dot.gov/downloads/folders/Investigations/INV.txt",
-            "dataQuality": true,
+            "identifier": "84.1",
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
+            "landingPage": "https://data.transportation.gov/d/g8qn-pywp",
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
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Investigations - Investigations Flat File"
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
-            "landingPage": "https://data.transportation.gov/d/g93w-3xqt",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12juntvt/12juntvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "June 2012"
+                }
             ],
+            "identifier": "18.39",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
```

