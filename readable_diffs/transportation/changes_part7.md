# Change History for transportation.json (Part 7)

### Changes from 31606f9 to dd2190f (Part 6/9)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 District of Columbia",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/kagd-275f",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/district2013.zip",
-                    "description": "2013 District of Columbia HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 District of Columbia"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 District of Columbia"
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
-            "landingPage": "https://data.transportation.gov/d/kagf-7gx5",
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
+            "identifier": "96.1",
+            "isPartOf": "DOT-96",
+            "issued": "2018-12-17",
             "keyword": [
                 "bus",
                 "civil penalties",
@@ -66025,159 +66040,123 @@
                 "motor carrier",
                 "truck"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "96.1",
+            "landingPage": "https://data.transportation.gov/d/kagf-7gx5",
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
-            "title": "Closed Enforcement Cases - Fiscal Year 2010",
-            "isPartOf": "DOT-96",
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
-            "categoryDesignation": "Research",
-            "analysisUnit": "Enforcement Case",
-            "phone": "202-366-4869",
-            "language": [
-                "en-US"
-            ]
+            "title": "Closed Enforcement Cases - Fiscal Year 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/kar5-6dpn",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "The Bureau of Transportation Statistics' (BTS) interactive bikeshare and e-scooter map shows the effects of COVID-19 on bikeshare (docked and dockless) and e-scooter systems in from January to August 2020. Many systems temporarily suspended operations or delayed seasonal opening. Several systems closed due to budgetary issues and no longer serve the area.",
+            "identifier": "https://data.transportation.gov/api/views/kar5-6dpn",
             "issued": "2020-08-06",
-            "@type": "dcat:Dataset",
-            "temporal": "2020",
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
+            "landingPage": "https://data.transportation.gov/d/kar5-6dpn",
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
-            "identifier": "https://data.transportation.gov/api/views/kar5-6dpn",
-            "description": "The Bureau of Transportation Statistics' (BTS) interactive bikeshare and e-scooter map shows the effects of COVID-19 on bikeshare (docked and dockless) and e-scooter systems in from January to August 2020. Many systems temporarily suspended operations or delayed seasonal opening. Several systems closed due to budgetary issues and no longer serve the area.",
-            "title": "Effects of COVID-19 on Bikeshare (Docked and Dockless) and E-scooter Operations",
-            "programCode": [
-                "021:053"
-            ],
             "spatial": "United States",
-            "license": "https://www.usa.gov/government-works",
+            "temporal": "2020",
             "theme": [
                 "Bicycles and Pedestrians"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Effects of COVID-19 on Bikeshare (Docked and Dockless) and E-scooter Operations"
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
+            "dataQuality": true,
+            "description": "Traffic Volume Data (based on unweighted raw continuous traffic count information collected by State Highway Agencies)",
+            "identifier": "https://data.transportation.gov/api/views/katt-tac5",
             "issued": "2021-04-06",
-            "@type": "dcat:Dataset",
+            "keyword": [
+                "traffic",
+                "traffic volume trends"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-23",
-            "keyword": [
-                "traffic",
-                "traffic volume trends"
+            "programCode": [
+                "021:009"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/katt-tac5",
-            "description": "Traffic Volume Data (based on unweighted raw continuous traffic count information collected by State Highway Agencies)",
-            "title": "TMAS Data Program",
-            "programCode": [
-                "021:009"
-            ],
             "spatial": "United States",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TMAS Data Program"
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
-            "landingPage": "https://data.transportation.gov/d/kb23-shrm",
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
-            "identifier": "700.2",
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
@@ -66186,34 +66165,70 @@
                     "title": "Travel Monitoring Analysis System"
                 }
             ],
-            "spatial": "National, State, Urban, Rural",
-            "dataQuality": true,
+            "identifier": "700.2",
+            "isPartOf": "DOT-700",
+            "issued": "2014-12-29",
+            "keyword": [
+                "aadt",
+                "travel",
+                "vmt"
+            ],
+            "landingPage": "https://data.transportation.gov/d/kb23-shrm",
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
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/kb7m-s8ye",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/13jantvt/13jantvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "January 2013"
+                }
             ],
+            "identifier": "18.46",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -66223,93 +66238,89 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.46",
+            "landingPage": "https://data.transportation.gov/d/kb7m-s8ye",
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
-            "title": "Monthly Traffic Volume Trends - January 2013",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/13jantvt/13jantvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "January 2013"
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
+            "title": "Monthly Traffic Volume Trends - January 2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/kbe7-qgqu",
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
-            "identifier": "https://data.transportation.gov/api/views/kbe7-qgqu",
             "description": "Light trucks include trucks with up to 14,000 pounds gross vehicle weight, including minivans and sport utility vehicles. Prior to the 2003 Benchmark Revision, light trucks were up to 10,000 pounds. The U.S. Bureau of Economic Analysis releases auto and truck sales data, which are used in the preparation of estimates of personal consumption expenditures.",
-            "title": "Light Truck Sales Seasonally Adjusted Annual Rate (SAAR)",
+            "identifier": "https://data.transportation.gov/api/views/kbe7-qgqu",
+            "issued": "2025-01-02",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/kbe7-qgqu",
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
+            "title": "Light Truck Sales Seasonally Adjusted Annual Rate (SAAR)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.21949/1503763",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2013-11-30",
-            "@type": "dcat:Dataset",
-            "modified": "2016-12-23",
-            "references": [
-                "https://rosap.ntl.bts.gov/view/dot/3607"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Transportation Library Data Curator",
+                "hasEmail": "mailto:ntldatacurator@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Travel time reliability information includes static data about traffic speeds or trip times that capture historic variations from day to day, and it can help individuals understand the level of variation in traffic. Unlike real-time travel time information, which provides a current snapshot of trip conditions and travel time, reliability information can be used to plan and budget in advance for a trip. Travel time reliability information can improve urban mobility by conveying reliability-related information to system users so that they can make informed decisions about their travel.  Data files in this zipped package include macro-enabled Microsoft Excel spreadsheets. These spreadsheets operate as interactive games. To save them into open formats would destroy this functionality. Therefore the macro-enabled spreadsheets are left as-is. There were opened prior to ingest in this repository using Microsoft Excel 2010. This dataset supports SHRP 2 report S2-L14-RW-1, Effectiveness of different approaches to disseminating traveler information on travel time reliability. Zip contains 628 MB. Files were accessed with Microsoft Excel 2016. Data will be preserved as it is. For the publication see: https://rosap.ntl.bts.gov/view/dot/3607",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Travel time reliability information includes static data about traffic speeds or trip times that capture historic variations from day to day, and it can help individuals understand the level of variation in traffic. Unlike real-time travel time information, which provides a current snapshot of trip conditions and travel time, reliability information can be used to plan and budget in advance for a trip. Travel time reliability information can improve urban mobility by conveying reliability-related information to system users so that they can make informed decisions about their travel.  Data files in this zipped package include macro-enabled Microsoft Excel spreadsheets. These spreadsheets operate as interactive games. To save them into open formats would destroy this functionality. Therefore the macro-enabled spreadsheets are left as-is. There were opened prior to ingest in this repository using Microsoft Excel 2010. This dataset supports SHRP 2 report S2-L14-RW-1, Effectiveness of different approaches to disseminating traveler information on travel time reliability. Zip contains 628 MB. Files were accessed with Microsoft Excel 2016. Data will be preserved as it is. For the publication see: https://rosap.ntl.bts.gov/view/dot/3607",
+                    "downloadURL": "https://doi.org/10.21949/1503763",
+                    "mediaType": "application/zip",
+                    "title": "Effectiveness of Different Approaches to Disseminating Traveler Information on Travel Time Reliability [supporting datasets]"
+                }
             ],
+            "identifier": "https://data.transportation.gov/api/views/kbii-m57p",
+            "issued": "2013-11-30",
             "keyword": [
                 "definitions",
                 "human factors",
@@ -66325,72 +66336,38 @@
                 "travel time",
                 "travel time reliability"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Transportation Library Data Curator",
-                "hasEmail": "mailto:ntldatacurator@dot.gov"
-            },
+            "landingPage": "https://doi.org/10.21949/1503763",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2016-12-23",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/kbii-m57p",
-            "description": "Travel time reliability information includes static data about traffic speeds or trip times that capture historic variations from day to day, and it can help individuals understand the level of variation in traffic. Unlike real-time travel time information, which provides a current snapshot of trip conditions and travel time, reliability information can be used to plan and budget in advance for a trip. Travel time reliability information can improve urban mobility by conveying reliability-related information to system users so that they can make informed decisions about their travel.  Data files in this zipped package include macro-enabled Microsoft Excel spreadsheets. These spreadsheets operate as interactive games. To save them into open formats would destroy this functionality. Therefore the macro-enabled spreadsheets are left as-is. There were opened prior to ingest in this repository using Microsoft Excel 2010. This dataset supports SHRP 2 report S2-L14-RW-1, Effectiveness of different approaches to disseminating traveler information on travel time reliability. Zip contains 628 MB. Files were accessed with Microsoft Excel 2016. Data will be preserved as it is. For the publication see: https://rosap.ntl.bts.gov/view/dot/3607",
-            "title": "Effectiveness of Different Approaches to Disseminating Traveler Information on Travel Time Reliability [supporting datasets]",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://doi.org/10.21949/1503763",
-                    "description": "Travel time reliability information includes static data about traffic speeds or trip times that capture historic variations from day to day, and it can help individuals understand the level of variation in traffic. Unlike real-time travel time information, which provides a current snapshot of trip conditions and travel time, reliability information can be used to plan and budget in advance for a trip. Travel time reliability information can improve urban mobility by conveying reliability-related information to system users so that they can make informed decisions about their travel.  Data files in this zipped package include macro-enabled Microsoft Excel spreadsheets. These spreadsheets operate as interactive games. To save them into open formats would destroy this functionality. Therefore the macro-enabled spreadsheets are left as-is. There were opened prior to ingest in this repository using Microsoft Excel 2010. This dataset supports SHRP 2 report S2-L14-RW-1, Effectiveness of different approaches to disseminating traveler information on travel time reliability. Zip contains 628 MB. Files were accessed with Microsoft Excel 2016. Data will be preserved as it is. For the publication see: https://rosap.ntl.bts.gov/view/dot/3607",
-                    "@type": "dcat:Distribution",
-                    "title": "Effectiveness of Different Approaches to Disseminating Traveler Information on Travel Time Reliability [supporting datasets]"
-                }
+            "references": [
+                "https://rosap.ntl.bts.gov/view/dot/3607"
             ],
             "spatial": "United States",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "language": [
-                "en-US"
-            ]
+            "title": "Effectiveness of Different Approaches to Disseminating Traveler Information on Travel Time Reliability [supporting datasets]"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/kbvr-tyu5",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2022-06-17",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-21",
-            "keyword": [
-                "diesel",
-                "fuel",
-                "fuel tax",
-                "gasoline",
-                "highways",
-                "highway trust fund",
-                "motor fuel",
-                "roadways",
-                "special fuels"
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
-            "identifier": "https://data.transportation.gov/api/views/kbvr-tyu5",
             "description": "Monthly motor fuel sales reported by states from the U.S. Department of Transportation's Federal Highway Administrations' Monthly Motor Fuel Report, available at: https://www.fhwa.dot.gov/policyinformation/motorfuelhwy_trustfund.cfm\r\n\r\nIncludes only gallons taxed by the state and reported by wholesale distributors to State motor fuel tax agencies. It includes highway use, non-highway use, and losses.",
-            "title": "Monthly Motor Fuel Sales Reported by States: Selected Data from FHWA Monthly Motor Fuel Report",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -66398,48 +66375,87 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/kbvr-tyu5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/kbvr-tyu5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/kbvr-tyu5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/kbvr-tyu5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/kbvr-tyu5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/kbvr-tyu5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/kbvr-tyu5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/kbvr-tyu5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/kbvr-tyu5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/kbvr-tyu5",
+            "issued": "2022-06-17",
+            "keyword": [
+                "diesel",
+                "fuel",
+                "fuel tax",
+                "gasoline",
+                "highways",
+                "highway trust fund",
+                "motor fuel",
+                "roadways",
+                "special fuels"
+            ],
+            "landingPage": "https://data.transportation.gov/d/kbvr-tyu5",
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
+            "title": "Monthly Motor Fuel Sales Reported by States: Selected Data from FHWA Monthly Motor Fuel Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "ftp://ftp.nhtsa.dot.gov/FARS",
+            "agencyProgramURL": "http://www-fars.nhtsa.dot.gov/Main/index.aspx",
+            "analysisUnit": "Crash  / Vehicle  / driver /person",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/kcpj-k9k9",
-            "issued": "1980-01-01",
-            "temporal": "R/1975-01-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Statistical",
             "collectionInstrument": "Web application",
-            "references": [
-                "http://www-fars.nhtsa.dot.gov/Main/index.aspx"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www-fars.nhtsa.dot.gov/Main/index.aspx",
+            "description": "The program collects data for analysis of traffic safety crashes to identify problems, and evaluate countermeasures leading to reducing injuries and property damage resulting from motor vehicle crashes. The FARS dataset contains descriptions, in standard format, of each fatal crash reported.  To qualify for inclusion, a crash must involve a motor vehicle traveling a traffic-way customarily open to the public and resulting in the death of a person (occupant of a vehicle or a non-motorist) within 30 days of the crash.  Each crash has more than 100 coded data elements that characterize the crash, the vehicles, and the people involved.  The specific data elements may be changed slightly each year to conform to the changing user needs, vehicle characteristics and highway safety emphasis areas.  The type of information that FARS, a major application, processes is therefore motor vehicle crash data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/FARS",
+                    "mediaType": "text/plain",
+                    "title": "FTP Raw Data"
+                }
             ],
+            "identifier": "25.3",
+            "isPartOf": "DOT-25",
+            "issued": "1980-01-01",
             "keyword": [
                 "crash",
                 "death",
@@ -66450,77 +66466,42 @@
                 "injury",
                 "vehicle"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "25.3",
+            "landingPage": "https://data.transportation.gov/d/kcpj-k9k9",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-2622",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Highway Traffic Safety Administration"
             },
-            "description": "The program collects data for analysis of traffic safety crashes to identify problems, and evaluate countermeasures leading to reducing injuries and property damage resulting from motor vehicle crashes. The FARS dataset contains descriptions, in standard format, of each fatal crash reported.  To qualify for inclusion, a crash must involve a motor vehicle traveling a traffic-way customarily open to the public and resulting in the death of a person (occupant of a vehicle or a non-motorist) within 30 days of the crash.  Each crash has more than 100 coded data elements that characterize the crash, the vehicles, and the people involved.  The specific data elements may be changed slightly each year to conform to the changing user needs, vehicle characteristics and highway safety emphasis areas.  The type of information that FARS, a major application, processes is therefore motor vehicle crash data.",
-            "title": "Fatality Analysis Reporting System ( FARS ) - FTP Raw Data",
-            "isPartOf": "DOT-25",
-            "agencyProgramURL": "http://www-fars.nhtsa.dot.gov/Main/index.aspx",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/FARS",
-                    "mediaType": "text/plain",
-                    "title": "FTP Raw Data"
-                }
+            "references": [
+                "http://www-fars.nhtsa.dot.gov/Main/index.aspx"
             ],
             "spatial": "latitude/longitude",
-            "describedBy": "http://www-fars.nhtsa.dot.gov/Main/index.aspx",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "ftp://ftp.nhtsa.dot.gov/FARS",
+            "temporal": "R/1975-01-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Statistical",
-            "analysisUnit": "Crash  / Vehicle  / driver /person",
-            "phone": "202-366-2622",
-            "language": [
-                "en-US"
-            ]
+            "title": "Fatality Analysis Reporting System ( FARS ) - FTP Raw Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ke6h-ga46",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2024-05-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-30",
-            "keyword": [
-                "ferry",
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
-            "identifier": "https://data.transportation.gov/api/views/ke6h-ga46",
             "description": "A data base of responses to the 2022 National Census of Ferries.\n\nThis file gives information about ferry terminals.",
-            "title": "2022 NCFO Terminals File",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -66528,70 +66509,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ke6h-ga46/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ke6h-ga46/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ke6h-ga46/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ke6h-ga46/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ke6h-ga46/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ke6h-ga46/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ke6h-ga46/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ke6h-ga46/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ke6h-ga46/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/ke6h-ga46",
+            "issued": "2024-05-30",
+            "keyword": [
+                "ferry",
+                "ferry transit",
+                "ncfo",
+                "passenger ferry"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ke6h-ga46",
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
+            "title": "2022 NCFO Terminals File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.bts.gov/browse-statistical-products-and-data/border-crossing-data/border-crossingentry-data",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2022-09-08",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-28",
-            "keyword": [
-                "buses",
-                "canada",
-                "containers",
-                "inbound border crossing entries",
-                "mexico",
-                "passengers",
-                "pedestrians",
-                "personal vehicles",
-                "ports",
-                "trains",
-                "trucks"
-            ],
             "conformsTo": "https://project-open-data.cio.gov/v1.1/schema/",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sean Jahanmir",
                 "hasEmail": "mailto:Sean.Jahanmir@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/keg4-3bc2",
+            "dataQuality": true,
             "description": "The Bureau of Transportation Statistics (BTS) Border Crossing Data provide summary statistics for inbound crossings at the U.S.-Canada and the U.S.-Mexico border at the port level.  Data are available for trucks, trains, containers, buses, personal vehicles, passengers, and pedestrians.  Border crossing data are collected at ports of entry by U.S. Customs and Border Protection (CBP).  The data reflect the number of vehicles, containers, passengers or pedestrians entering the United States.  CBP does not collect comparable data on outbound crossings.  Users seeking data on outbound counts may therefore want to review data from individual bridge operators, border state governments, or the Mexican and Canadian governments.",
-            "title": "Border Crossing Entry Data",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -66599,61 +66575,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/keg4-3bc2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/keg4-3bc2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/keg4-3bc2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/keg4-3bc2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/keg4-3bc2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/keg4-3bc2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/keg4-3bc2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/keg4-3bc2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/keg4-3bc2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/keg4-3bc2",
+            "issued": "2022-09-08",
+            "keyword": [
+                "buses",
+                "canada",
+                "containers",
+                "inbound border crossing entries",
+                "mexico",
+                "passengers",
+                "pedestrians",
+                "personal vehicles",
+                "ports",
+                "trains",
+                "trucks"
+            ],
+            "landingPage": "https://www.bts.gov/browse-statistical-products-and-data/border-crossing-data/border-crossingentry-data",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-28",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "spatial": "United States, Canada, Mexico",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1M",
             "theme": [
                 "Research and Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Border Crossing Entry Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/kett-pmdy",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-10-03",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-03",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:answers@bts.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/kett-pmdy",
-            "description": "Source: U.S. Department of Transportation, Bureau of Transportation Statistics, based upon U.S. Department of Commerce, U.S. Census Bureau, Foreign Trade Division, USA Trade Online, \"HS Port-level Data\", available at https://usatrade.census.gov/ as of Sept 2024.",
-            "title": "Top 10 Containerized Non-Durable Import Commodities by Value and Coast 2023",
-            "programCode": [
-                "021:042"
-            ],
+            "description": "Source: U.S. Department of Transportation, Bureau of Transportation Statistics, based upon U.S. Department of Commerce, U.S. Census Bureau, Foreign Trade Division, USA Trade Online, \"HS Port-level Data\", available at https://usatrade.census.gov/ as of Sept 2024.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -66661,47 +66649,77 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/kett-pmdy/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/kett-pmdy/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/kett-pmdy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/kett-pmdy/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/kett-pmdy/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/kett-pmdy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/kett-pmdy/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/kett-pmdy/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/kett-pmdy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/kett-pmdy",
+            "issued": "2024-10-03",
+            "landingPage": "https://data.transportation.gov/d/kett-pmdy",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-10-03",
+            "programCode": [
+                "021:042"
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
+            "title": "Top 10 Containerized Non-Durable Import Commodities by Value and Coast 2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/kf2f-6g73",
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
+                    "description": "2011 Minnesota HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/minnesota2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Minnesota"
+                }
+            ],
+            "identifier": "678.25",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -66715,76 +66733,39 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.25",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Minnesota",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/kf2f-6g73",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/minnesota2011.zip",
-                    "description": "2011 Minnesota HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Minnesota"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Minnesota"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/kfcv-nyy3",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2021-08-03",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
-            "keyword": [
-                "airport",
-                "airports",
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
-            "identifier": "https://data.transportation.gov/api/views/kfcv-nyy3",
             "description": "The Airports dataset includes all official and operational aerodromes as of July 16, 2020 and is part of the U.S. Department of Transportation (USDOT)/Bureau of Transportation Statistics (BTS) National Transportation Atlas Database (NTAD). The Airports database is a geographic point database of official operational aerodromes in the United States and U.S. Territories. Attribute data is provided on the physical and operational characteristics of the aerodrome, current usage including enplanements and aircraft operations, congestion levels and usage categories. This geospatial data is derived from the FAA's National Airspace System Resource Aeronautical Data Product.",
-            "title": "Airports -- Citizen Connect",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -66792,50 +66773,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/kfcv-nyy3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/kfcv-nyy3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/kfcv-nyy3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/kfcv-nyy3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/kfcv-nyy3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/kfcv-nyy3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/kfcv-nyy3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/kfcv-nyy3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/kfcv-nyy3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/kfcv-nyy3",
+            "issued": "2021-08-03",
+            "keyword": [
+                "airport",
+                "airports",
+                "national transportation atlas database",
+                "ntad"
+            ],
+            "landingPage": "https://data.transportation.gov/d/kfcv-nyy3",
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
+            "title": "Airports -- Citizen Connect"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/kgxm-khq2",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/kgxm-khq2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "Trespasser Fatalities",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -66843,40 +66833,55 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/kgxm-khq2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/kgxm-khq2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/kgxm-khq2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/kgxm-khq2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/kgxm-khq2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/kgxm-khq2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/kgxm-khq2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/kgxm-khq2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/kgxm-khq2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/kgxm-khq2",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/kgxm-khq2",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Trespasser Fatalities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/khzx-vxu4",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRA Safety Data Team",
+                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This is the report for Employee on Duty Fatalities, Injuries, and Illnesses",
+            "identifier": "https://data.transportation.gov/api/views/khzx-vxu4",
             "issued": "2024-08-19",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "casualties",
                 "casualty",
@@ -66894,41 +66899,54 @@
                 "trespassers",
                 "worker on duty"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRA Safety Data Team",
-                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/khzx-vxu4",
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
-            "identifier": "https://data.transportation.gov/api/views/khzx-vxu4",
-            "description": "This is the report for Employee on Duty Fatalities, Injuries, and Illnesses",
-            "title": "Employee on Duty Fatalities, Injuries, and Illnesses (2.04 & 2.05)",
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
+            "title": "Employee on Duty Fatalities, Injuries, and Illnesses (2.04 & 2.05)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/ki7u-xetf",
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
+                    "description": "2012 Hawaii HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/hawaii2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Hawaii"
+                }
+            ],
+            "identifier": "678.65",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -66942,101 +66960,64 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.65",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Hawaii",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/ki7u-xetf",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/hawaii2012.zip",
-                    "description": "2012 Hawaii HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Hawaii"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Hawaii"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/kijm-95mr",
-            "issued": "2025-01-31",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sean Jahanmir",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/kijm-95mr",
+            "issued": "2025-01-31",
+            "landingPage": "https://data.transportation.gov/d/kijm-95mr",
+            "modified": "2025-01-31",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "TransBorder Freight Data"
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
-            "landingPage": "https://data.transportation.gov/d/kj2v-r2fj",
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
-            "identifier": "692.24",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - MPO Boundaries",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "primaryITInvestmentUII": "021-845083703",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67045,35 +67026,66 @@
                     "title": "MPO Boundaries"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.24",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/kj2v-r2fj",
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
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - MPO Boundaries"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Data includes PII.",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.psp.fmcsa.dot.gov/",
+            "agencyProgramURL": "http://www.psp.fmcsa.dot.gov/",
+            "analysisUnit": "Driver",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/kjve-jwtv",
-            "issued": "2010-05-12",
-            "temporal": "R/2010-05-12/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.psp.fmcsa.dot.gov/"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The program helps motor carriers make more informed hiring decisions by providing electronic access to driver crash and inspection history from the FMCSA Motor Carrier Management Information System (MCMIS). PSP records are now available for motor carriers and commercial drivers.  PSP is designed to assist the motor carrier industry in assessing individual operator crash and serious safety violation history as a pre-employment condition. A carrier will pay $10 for each requested driver history. An annual subscription fee of $100 also applies. Carriers with fewer than 100 power units qualify for a discounted annual fee of $25 per year.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.transportation.gov/mission/data-inventory-not-available",
+                    "mediaType": "text/html"
+                }
             ],
+            "identifier": "101.0",
+            "issued": "2010-05-12",
             "keyword": [
                 "cdl",
                 "commercial drivers license",
@@ -67085,58 +67097,62 @@
                 "out of service",
                 "violation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "101.0",
+            "landingPage": "https://data.transportation.gov/d/kjve-jwtv",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-24",
+            "phone": "202-366-2974",
+            "programCode": [
+                "021:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Motor Carrier Safety Administration"
             },
-            "description": "The program helps motor carriers make more informed hiring decisions by providing electronic access to driver crash and inspection history from the FMCSA Motor Carrier Management Information System (MCMIS). PSP records are now available for motor carriers and commercial drivers.  PSP is designed to assist the motor carrier industry in assessing individual operator crash and serious safety violation history as a pre-employment condition. A carrier will pay $10 for each requested driver history. An annual subscription fee of $100 also applies. Carriers with fewer than 100 power units qualify for a discounted annual fee of $25 per year.",
-            "title": "Pre-Employment Screening Program (PSP) -",
-            "agencyProgramURL": "http://www.psp.fmcsa.dot.gov/",
-            "programCode": [
-                "021:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.transportation.gov/mission/data-inventory-not-available",
-                    "mediaType": "text/html"
-                }
+            "references": [
+                "http://www.psp.fmcsa.dot.gov/"
             ],
+            "rights": "Data includes PII.",
             "spatial": "State-level crash and inspection data.",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.psp.fmcsa.dot.gov/",
+            "temporal": "R/2010-05-12/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Driver",
-            "phone": "202-366-2974",
-            "language": [
-                "en-US"
-            ]
+            "title": "Pre-Employment Screening Program (PSP) -"
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
-            "landingPage": "https://data.transportation.gov/d/kmdh-4pn5",
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
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/pubs/MonthlyData/September%202015%20Adjusted%20Database.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "September 2015 Adjusted Data"
+                }
             ],
+            "identifier": "19.4",
+            "isPartOf": "DOT-19",
+            "issued": "2011-10-07",
             "keyword": [
                 "boardings",
                 "bus",
@@ -67146,57 +67162,53 @@
                 "train",
                 "transit"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John D. Giorgis",
-                "hasEmail": "mailto:john.giorgis@dot.gov"
-            },
-            "identifier": "19.4",
+            "landingPage": "https://data.transportation.gov/d/kmdh-4pn5",
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
-            "title": "NTD Monthly Module Data Set - September 2015 Adjusted Data",
-            "isPartOf": "DOT-19",
-            "agencyProgramURL": "http://www.ntdprogram.gov; http://www.ntdprogram.gov/ntdprogram/data.htm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/pubs/MonthlyData/September%202015%20Adjusted%20Database.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "September 2015 Adjusted Data"
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
+            "title": "NTD Monthly Module Data Set - September 2015 Adjusted Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "021:15"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kate Hartman",
+                "hasEmail": "mailto:kate.hartman@dot.gov"
             },
+            "dataQuality": true,
+            "description": "These data files were obtained from Minnesota Department of Transportation (MnDOT) under the Integrated Mobile Observation (IMO) contract. The instrumented vehicles include snowplows (made by Sterling and International) and light-duty pickups (made by Ford).  The snowplows travel pre-determined routes in 12-hour shifts during winter-weather events, carrying out winter-maintenance activities appropriate for the event and MnDOT rules of practice (snow-plowing, applying chemicals, etc.).  The light-duty vehicles travel throughout the state. Data from May 2013 onward is included. The files include VaiX records, DjX records, CanX records, ObdY records, vehicle location and status and store-and-forward messages.",
+            "distribution": [
                 {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/kn5d-ptj9",
-            "bureauCode": [
-                "021:15"
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/download/kn5d-ptj9/application/msword",
+                    "mediaType": "application/msword"
+                }
             ],
+            "identifier": "https://data.transportation.gov/api/views/kn5d-ptj9",
             "issued": "2013-05-15",
-            "@type": "dcat:Dataset",
-            "temporal": "2013-06-26/2015-12-21",
-            "modified": "2013-05-15",
             "keyword": [
                 "arterial",
                 "cellular",
@@ -67212,70 +67224,39 @@
                 "simulation data",
                 "weather"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/kn5d-ptj9",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
+            "modified": "2013-05-15",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Department of Transportation"
             },
-            "identifier": "https://data.transportation.gov/api/views/kn5d-ptj9",
-            "description": "These data files were obtained from Minnesota Department of Transportation (MnDOT) under the Integrated Mobile Observation (IMO) contract. The instrumented vehicles include snowplows (made by Sterling and International) and light-duty pickups (made by Ford).  The snowplows travel pre-determined routes in 12-hour shifts during winter-weather events, carrying out winter-maintenance activities appropriate for the event and MnDOT rules of practice (snow-plowing, applying chemicals, etc.).  The light-duty vehicles travel throughout the state. Data from May 2013 onward is included. The files include VaiX records, DjX records, CanX records, ObdY records, vehicle location and status and store-and-forward messages.",
-            "title": "Minnesota Department of Transportation Mobile Observation",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/download/kn5d-ptj9/application/msword",
-                    "mediaType": "application/msword"
-                }
-            ],
             "spatial": "Minnesota",
-            "dataQuality": true,
-            "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "irregular",
+            "temporal": "2013-06-26/2015-12-21",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Minnesota Department of Transportation Mobile Observation"
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
-            "identifier": "https://data.transportation.gov/api/views/kpa7-pmax",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 2004",
-            "title": "Historic HPMS Data (Universe) - 2004",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67283,50 +67264,83 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/kpa7-pmax/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/kpa7-pmax/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/kpa7-pmax/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/kpa7-pmax/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/kpa7-pmax/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/kpa7-pmax/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/kpa7-pmax/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/kpa7-pmax/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/kpa7-pmax/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/kpa7-pmax",
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
+            "title": "Historic HPMS Data (Universe) - 2004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyProgramURL": "http://www.nhtsa.gov/fuel-economy",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/kpk3-ypkx",
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
+            "identifier": "1862.5",
+            "isPartOf": "DOT-1862",
+            "issued": "2015-12-16",
             "keyword": [
                 "amfa",
                 "civil penalties",
@@ -67343,104 +67357,66 @@
                 "report",
                 "shortfall"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "1862.5",
+            "landingPage": "https://data.transportation.gov/d/kpk3-ypkx",
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
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/kqpm-i9tw",
-            "issued": "2022-12-20",
             "@type": "dcat:Dataset",
-            "modified": "2023-01-18",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joe McGill",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "Maps of Value, Tonnage, Ton-Miles and Average Miles per Shipment by State",
             "identifier": "https://data.transportation.gov/api/views/kqpm-i9tw",
+            "issued": "2022-12-20",
+            "landingPage": "https://data.transportation.gov/d/kqpm-i9tw",
+            "modified": "2023-01-18",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "Maps of Value, Tonnage, Ton-Miles and Average Miles per Shipment by State",
             "title": "Historical CFS Data Maps"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "rights": "https://wxde.fhwa.dot.gov/termsOfUse.jsp",
+            "accrualPeriodicity": "R/PT1S",
+            "agencyProgramURL": "https://ops.fhwa.dot.gov/weather/index.asp",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/kqqy-zb6p",
-            "issued": "2013-01-01",
-            "temporal": "R/2013-01-01/PT1S",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
-            "references": [
-                "https://wxde.fhwa.dot.gov/frequentlyAskedQuestions.jsp"
-            ],
-            "keyword": [
-                "clarus",
-                "connected vehicle",
-                "ess",
-                "road weather",
-                "rwis",
-                "weather",
-                "wxde"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "2068.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "https://wxde.fhwa.dot.gov/auth2/metadata.jsp",
             "description": "The Weather Data Environment (WxDE) collects and shares transportation-related weather data with a particular focus on weather data related to connected vehicle applications. The WxDE collects data in real time from both fixed environmental sensor stations and mobile sources. The WxDE computes value-added enhancements to this data, such as checking the quality of observed data and inferring weather parameters from vehicle data (e.g., inferring precipitation based on windshield wiper activation). The WxDE archives both collected and computed data. The WxDE supports subscriptions for access to real-time data in near real time generated by individual weather-related connected vehicle projects.",
-            "title": "Weather Data Environment - Data Catalog",
-            "isPartOf": "DOT-2068",
-            "agencyProgramURL": "https://ops.fhwa.dot.gov/weather/index.asp",
-            "programCode": [
-                "021:011"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67449,33 +67425,72 @@
                     "title": "Data Catalog"
                 }
             ],
-            "describedBy": "https://wxde.fhwa.dot.gov/auth2/metadata.jsp",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/licenses/by-sa/3.0/",
-            "theme": [
-                "Transportation"
+            "identifier": "2068.1",
+            "isPartOf": "DOT-2068",
+            "issued": "2013-01-01",
+            "keyword": [
+                "clarus",
+                "connected vehicle",
+                "ess",
+                "road weather",
+                "rwis",
+                "weather",
+                "wxde"
             ],
-            "accrualPeriodicity": "R/PT1S",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/kqqy-zb6p",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-0754"
+            "license": "https://creativecommons.org/licenses/by-sa/3.0/",
+            "modified": "2024-05-08",
+            "phone": "202-366-0754",
+            "programCode": [
+                "021:011"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "references": [
+                "https://wxde.fhwa.dot.gov/frequentlyAskedQuestions.jsp"
+            ],
+            "rights": "https://wxde.fhwa.dot.gov/termsOfUse.jsp",
+            "temporal": "R/2013-01-01/PT1S",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Weather Data Environment - Data Catalog"
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
-            "landingPage": "https://data.transportation.gov/d/krsq-rb7x",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/13octtvt/13octtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "October 2013"
+                }
             ],
+            "identifier": "18.55",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -67485,82 +67500,49 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.55",
+            "landingPage": "https://data.transportation.gov/d/krsq-rb7x",
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
-            "title": "Monthly Traffic Volume Trends - October 2013",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/13octtvt/13octtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "October 2013"
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
+            "title": "Monthly Traffic Volume Trends - October 2013"
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
-            "landingPage": "https://data.transportation.gov/d/krzz-gijc",
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
-            "identifier": "DOT-687",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://safety.fhwa.dot.gov/tools/data_tools/memohsip072911/",
             "description": "The HSIP ORT establishes a standardized reporting process that promotes consistency among state reports while maintaining flexibility to meet states reporting needs. It allows States and Divisions to submit required annual HSIP reports through an easy to use web interface, and will be used for regular and special reports for the White House, Congress, FHWA management, OST, GAO and others.",
-            "title": "Highway Safety Improvement Program (HSIP)",
-            "agencyProgramURL": "http://safety.fhwa.dot.gov/hsip/",
-            "primaryITInvestmentUII": "021-133811186",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67569,35 +67551,69 @@
                     "title": "Highway Safety Improvement Program"
                 }
             ],
-            "spatial": "National, State",
-            "describedBy": "http://safety.fhwa.dot.gov/tools/data_tools/memohsip072911/",
-            "dataQuality": true,
+            "identifier": "DOT-687",
+            "issued": "2014-12-29",
+            "keyword": [
+                "highway",
+                "safety"
+            ],
+            "landingPage": "https://data.transportation.gov/d/krzz-gijc",
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
+            "title": "Highway Safety Improvement Program (HSIP)"
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
-            "landingPage": "https://data.transportation.gov/d/ksgb-ksyx",
-            "issued": "2010-10-01",
-            "temporal": "R/1996-12-31/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-05",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "www.transit.dot.gov/ntd"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NTD Program Support",
+                "hasEmail": "mailto:NTDHelp@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www.ntdprogram.gov/ntdprogram/data.htm",
+            "description": "Data reported to the NTD by urbanized area transit systems in their annual reports.   Includes contact information, contractural relationshps, subrecipient informatino, service area, sources of funds, operating expenditures by object class and function, capital expenditures by object class and function, fixed guideway information, revenue vehicle inventory, fuel consumption, employees, and labor hours, and urbanized area allocation information.   Also includes service supplied and consumed by annual total, average weekday, average saturday, and average sunday.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/1998NTDxls.exe",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "1998 Database"
+                }
             ],
+            "identifier": "21.2",
+            "isPartOf": "DOT-21",
+            "issued": "2010-10-01",
             "keyword": [
                 "agency",
                 "allocation",
@@ -67616,58 +67632,60 @@
                 "urbanized",
                 "vehicles"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NTD Program Support",
-                "hasEmail": "mailto:NTDHelp@dot.gov"
-            },
-            "identifier": "21.2",
+            "landingPage": "https://data.transportation.gov/d/ksgb-ksyx",
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
-            "title": "NTD Annual Module Data Set - 1998 Database",
-            "isPartOf": "DOT-21",
-            "agencyProgramURL": "http://www.ntdprogram.gov",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/1998NTDxls.exe",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "1998 Database"
-                }
+            "references": [
+                "www.transit.dot.gov/ntd"
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
+            "title": "NTD Annual Module Data Set - 1998 Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/ksry-e7gg",
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
+                    "description": "2012 Rhode Island HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/rhodeisland2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Rhode Island"
+                }
+            ],
+            "identifier": "678.93",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -67681,60 +67699,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.93",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Rhode Island",
-            "isPartOf": "DOT-678",
-            "primaryITInvestmentUII": "021-099281808",
-            "programCode": [
-                "021:009"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/rhodeisland2012.zip",
-                    "description": "2012 Rhode Island HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Rhode Island"
-                }
+            "landingPage": "https://data.transportation.gov/d/ksry-e7gg",
+            "language": [
+                "en-US"
             ],
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
-            "dataQuality": false,
             "license": "https://project-open-data.cio.gov/unknown-license/",
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Rhode Island"
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
-            "landingPage": "https://data.transportation.gov/d/ktzy-94pf",
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
+            "identifier": "121.1",
+            "isPartOf": "DOT-121",
+            "issued": "2000-01-01",
             "keyword": [
                 "bus",
                 "company safety profile.",
@@ -67749,64 +67764,39 @@
                 "safersys",
                 "safety and fitness electronic records"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "121.1",
+            "landingPage": "https://data.transportation.gov/d/ktzy-94pf",
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
-            "landingPage": "https://data.transportation.gov/d/kuvg-3uwp",
-            "issued": "2023-04-21",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:list-fra-safeteam@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
-            "identifier": "https://data.transportation.gov/api/views/kuvg-3uwp",
             "description": "This dataset is the source dataset and contains raw data values. It will replace the current data download (https://safetydata.fra.dot.gov/OfficeofSafety/publicsite/on_the_fly_download.aspx) when the safetydata.fra.dot.gov site is decommissioned in 2024. To download data that contains data in a user-friendly human-readable format, please reference https://data.transportation.gov/Railroads/Injury-Illness-Summary-Casualty-Data/rash-pd2d.",
-            "title": "Injury/Illness Summary - Casualty Source Data (Form 55A)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -67814,109 +67804,134 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/kuvg-3uwp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/kuvg-3uwp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/kuvg-3uwp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/kuvg-3uwp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/kuvg-3uwp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/kuvg-3uwp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/kuvg-3uwp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/kuvg-3uwp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/kuvg-3uwp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/kuvg-3uwp",
+            "issued": "2023-04-21",
+            "landingPage": "https://data.transportation.gov/d/kuvg-3uwp",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-31",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Injury/Illness Summary - Casualty Source Data (Form 55A)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/kuvi-vigf",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2024-07-05",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-19",
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
-            "identifier": "https://data.transportation.gov/api/views/kuvi-vigf",
             "description": "Employment and revenue.",
-            "title": "Financials",
+            "identifier": "https://data.transportation.gov/api/views/kuvi-vigf",
+            "issued": "2024-07-05",
+            "keyword": [
+                "aff",
+                "aviation facts & figures"
+            ],
+            "landingPage": "https://data.transportation.gov/d/kuvi-vigf",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-19",
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
+            "title": "Financials"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:36"
             ],
-            "landingPage": "https://data.transportation.gov/d/kwy6-xug7",
-            "issued": "2024-10-17",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-17",
-            "keyword": [
-                "operating expenses",
-                "transit"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NTD Program Support",
                 "hasEmail": "mailto:NTDHelp@dot.gov"
             },
+            "description": "A summary of operating expenses applied to provide public transit as reported by transit agencies to the National Transit Database (NTD) in Report Year 2023.\r\n\r\nNTD Data Summaries organize and summarize data from the 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. \r\n\r\nThis summary is based on the 2023 Operating Expenses database file on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
+            "identifier": "https://data.transportation.gov/api/views/kwy6-xug7",
+            "issued": "2024-10-17",
+            "keyword": [
+                "operating expenses",
+                "transit"
+            ],
+            "landingPage": "https://data.transportation.gov/d/kwy6-xug7",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-10-17",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Transit Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/kwy6-xug7",
-            "description": "A summary of operating expenses applied to provide public transit as reported by transit agencies to the National Transit Database (NTD) in Report Year 2023.\r\n\r\nNTD Data Summaries organize and summarize data from the 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. \r\n\r\nThis summary is based on the 2023 Operating Expenses database file on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
-            "title": "2023 NTD Data Summary - Operating Expenses",
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "2023 NTD Data Summary - Operating Expenses"
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
-            "landingPage": "https://data.transportation.gov/d/kxj7-jm27",
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
+            "identifier": "106.1",
+            "isPartOf": "DOT-106",
+            "issued": "2010-12-15",
             "keyword": [
                 "basic",
                 "basics",
@@ -67944,60 +67959,61 @@
                 "unsafe driving",
                 "vehicle maintenance"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "106.1",
+            "landingPage": "https://data.transportation.gov/d/kxj7-jm27",
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
-            "title": "Carrier Safety Measurement System (CSMS, or SMS) - Raw Data - Download Current Data",
-            "isPartOf": "DOT-106",
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
-            "categoryDesignation": "Research",
-            "analysisUnit": "Motor Carrier",
-            "phone": "202-366-5797",
-            "language": [
-                "en-US"
-            ]
+            "title": "Carrier Safety Measurement System (CSMS, or SMS) - Raw Data - Download Current Data"
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
-            "landingPage": "https://data.transportation.gov/d/kxup-jk28",
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
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/rrgxrtab.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Hwy/Rail Table By Railroad"
+                }
             ],
+            "identifier": "214.14",
+            "isPartOf": "DOT-214",
+            "issued": "2010-09-29",
             "keyword": [
                 "accident",
                 "casualty",
@@ -68010,71 +68026,42 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "214.14",
+            "landingPage": "https://data.transportation.gov/d/kxup-jk28",
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
-            "title": "Highway Rail Accidents - Hwy/Rail Table By Railroad",
-            "isPartOf": "DOT-214",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/rrgxrtab.aspx",
-                    "mediaType": "text/csv",
-                    "title": "Hwy/Rail Table By Railroad"
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
+            "title": "Highway Rail Accidents - Hwy/Rail Table By Railroad"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/kxxg-a7c6",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-11-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-15",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:answers@bts.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/kxxg-a7c6",
             "description": "",
-            "title": "AFF - GA Performance",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68082,46 +68069,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/kxxg-a7c6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/kxxg-a7c6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/kxxg-a7c6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/kxxg-a7c6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/kxxg-a7c6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/kxxg-a7c6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/kxxg-a7c6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/kxxg-a7c6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/kxxg-a7c6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/kxxg-a7c6",
+            "issued": "2024-11-13",
+            "landingPage": "https://data.transportation.gov/d/kxxg-a7c6",
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
+            "title": "AFF - GA Performance"
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
-            "landingPage": "https://data.transportation.gov/d/kyun-5gtf",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12octtvt/12octtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "October 2012"
+                }
             ],
+            "identifier": "18.43",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -68131,60 +68146,62 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.43",
+            "landingPage": "https://data.transportation.gov/d/kyun-5gtf",
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
-            "title": "Monthly Traffic Volume Trends - October 2012",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12octtvt/12octtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "October 2012"
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
+            "title": "Monthly Traffic Volume Trends - October 2012"
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
-            "landingPage": "https://data.transportation.gov/d/kyux-4ae5",
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
+                    "downloadURL": "http://lai.locationaffordability.info/download_csv.php%3Fstate=us&geography=county",
+                    "mediaType": "text/csv",
+                    "title": "All Census Counties"
+                }
             ],
+            "identifier": "337.2",
+            "isPartOf": "DOT-337",
+            "issued": "2013-11-19",
             "keyword": [
                 "access",
                 "affordability",
@@ -68197,153 +68214,118 @@
                 "transit",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "337.2",
+            "landingPage": "https://data.transportation.gov/d/kyux-4ae5",
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
-            "title": "Location Affordability Index - All Census Counties",
-            "isPartOf": "DOT-337",
-            "agencyProgramURL": "http://www.locationaffordability.info/",
-            "describedByType": "application/pdf",
-            "programCode": [
-                "021:058"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://lai.locationaffordability.info/download_csv.php%3Fstate=us&geography=county",
-                    "mediaType": "text/csv",
-                    "title": "All Census Counties"
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
+            "title": "Location Affordability Index - All Census Counties"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/kz29-w2ns",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Economic concepts related to highway transportation cost index.",
+            "identifier": "https://data.transportation.gov/api/views/kz29-w2ns",
             "issued": "2020-02-24",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
             "keyword": [
                 "construction cost",
                 "highway cost",
                 "transportation cost",
                 "transportation economics"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/kz29-w2ns",
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
-            "identifier": "https://data.transportation.gov/api/views/kz29-w2ns",
-            "description": "Economic concepts related to highway transportation cost index.",
-            "title": "Transportation Economic Concepts: Value of Transportation - Construction Cost",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Transportation Economic Concepts: Value of Transportation - Construction Cost"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/kzni-a7vm",
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
-            "identifier": "https://data.transportation.gov/api/views/kzni-a7vm",
             "description": "Freight and mail carried by U.S. airlines in all service classes (schedule and nonscheduled) on international flights. A revenue ton-mile is the movement of one ton of revenue cargo carried for one mile. The Bureau of Transportation Statistics air traffic data from U.S. air carriers and international carriers operating within the U.S.",
-            "title": "Air Cargo - International",
+            "identifier": "https://data.transportation.gov/api/views/kzni-a7vm",
+            "issued": "2025-01-15",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/kzni-a7vm",
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
+            "title": "Air Cargo - International"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/kzrh-n8jg",
+            "accrualPeriodicity": "irregular",
+            "agencyProgramURL": "http://www.sustainablecommunities.gov/map.html",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2009-06-30",
-            "temporal": "2009-06-30/2013-12-31",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
-            "references": [
-                "http://www.sustainablecommunities.gov/map.html"
-            ],
-            "keyword": [
-                "grants",
-                "sustainability"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
-            "identifier": "250.0",
+            "dataQuality": true,
             "description": "The Partnership for Sustainable Communities is comprised of the Department of Housing and Urban Development (HUD), the US Department of Transportation (DOT), and the Environmental Protection Agency (EPA)",
-            "title": "Partnership for Sustainable Communities - Grants Map -",
-            "agencyProgramURL": "http://www.sustainablecommunities.gov/map.html",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68351,27 +68333,59 @@
                     "mediaType": "text/csv"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "250.0",
+            "issued": "2009-06-30",
+            "keyword": [
+                "grants",
+                "sustainability"
+            ],
+            "landingPage": "https://data.transportation.gov/d/kzrh-n8jg",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
+            "modified": "2024-05-08",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "references": [
+                "http://www.sustainablecommunities.gov/map.html"
+            ],
+            "temporal": "2009-06-30/2013-12-31",
             "theme": [
                 "Transportation"
             ],
-            "categoryDesignation": "Research",
-            "language": [
-                "en-US"
-            ]
+            "title": "Partnership for Sustainable Communities - Grants Map -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://primis.phmsa.dot.gov/comm/reports/enforce/enforcement.html",
+            "agencyDataSeriesURL": "https://primis.phmsa.dot.gov/comm/reports/enforce/enforcement.html",
             "bureauCode": [
                 "021:50"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Seong Hwang",
+                "hasEmail": "mailto:seong.hwang@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://primis.phmsa.dot.gov/comm/EnforcementProgram.htm",
+            "description": "The Pipeline Safety Enforcement Program is designed to monitor and enforce compliance with pipeline safety regulations and confirm operators are meeting PHMSA expectations for safe, reliable, and environmentally sound operation of their facilities.\n\nOn this website PHMSA offers a variety of reports and records detailing its enforcement activity involving pipeline operators. These reports and records are offered on both nationwide and operator-specific bases and includes the following:\nNationwide Enforcement Activity - A high-level summary of PHMSA's overall enforcement activity.\n\nEnforcement Actions - A summary of the various enforcement actions that have been undertaken by PHMSA.\n\nEnforcement Case Status - The status of various types of enforcement cases by the year they were initiated.\n\nCivil Penalty Case Status - The status of enforcement cases involving civil penalties.\n\nEnforcement Information for Specific Operators - The national-level reports above are also provided on an operator-specific basis.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://primis.phmsa.dot.gov/comm/reports/enforce/enforcement.html",
+                    "mediaType": "text/html",
+                    "title": "PHMSA Enforcement Transparency Portal"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/m28n-9ah6",
             "issued": "2002-01-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2002-01-01/P1M",
-            "modified": "2024-08-01",
             "keyword": [
                 "case documents",
                 "case status",
@@ -68384,76 +68398,39 @@
                 "pipeline",
                 "probable violation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Seong Hwang",
-                "hasEmail": "mailto:seong.hwang@dot.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Pipeline and Hazardous Materials Safety Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/m28n-9ah6",
-            "description": "The Pipeline Safety Enforcement Program is designed to monitor and enforce compliance with pipeline safety regulations and confirm operators are meeting PHMSA expectations for safe, reliable, and environmentally sound operation of their facilities.\n\nOn this website PHMSA offers a variety of reports and records detailing its enforcement activity involving pipeline operators. These reports and records are offered on both nationwide and operator-specific bases and includes the following:\nNationwide Enforcement Activity - A high-level summary of PHMSA's overall enforcement activity.\n\nEnforcement Actions - A summary of the various enforcement actions that have been undertaken by PHMSA.\n\nEnforcement Case Status - The status of various types of enforcement cases by the year they were initiated.\n\nCivil Penalty Case Status - The status of enforcement cases involving civil penalties.\n\nEnforcement Information for Specific Operators - The national-level reports above are also provided on an operator-specific basis.",
-            "title": "Pipeline Enforcement Transparency Portal",
+            "landingPage": "https://primis.phmsa.dot.gov/comm/reports/enforce/enforcement.html",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-08-01",
             "primaryITInvestmentUII": "021-339943484",
             "programCode": [
                 "021:044"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://primis.phmsa.dot.gov/comm/reports/enforce/enforcement.html",
-                    "mediaType": "text/html",
-                    "title": "PHMSA Enforcement Transparency Portal"
-                }
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Pipeline and Hazardous Materials Safety Administration"
+            },
             "spatial": "United States",
-            "describedBy": "https://primis.phmsa.dot.gov/comm/EnforcementProgram.htm",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "agencyDataSeriesURL": "https://primis.phmsa.dot.gov/comm/reports/enforce/enforcement.html",
+            "temporal": "2002-01-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Pipeline Enforcement Transparency Portal"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/m2bh-93w3",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2023-09-25",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-21",
-            "keyword": [
-                "access",
-                "accessibility",
-                "air",
-                "bus",
-                "intercity",
-                "rail",
-                "rural",
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
-            "identifier": "https://data.transportation.gov/api/views/m2bh-93w3",
             "description": "Total and percent of rural population with access to scheduled intercity bus, rail, and air transportation. Rural areas are Census block groups with their centroid (center) outside of all Census urban areas. Summarized to county level. Facilities used available at: https://data.transportation.gov/Research-and-Statistics/Intercity-Air-Bus-and-Rail-Transportation-Faciliti/xnub-2sc4. \n\nInteractive map showing access to intercity transportation in rural areas:\nhttps://datahub.transportation.gov/stories/s/Rural-Access-to-Intercity-Transportation/gr9y-9gjq\n\nMethodology:\nhttps://datahub.transportation.gov/stories/s/dbb4-pr2c",
-            "title": "Access to Intercity Air, Bus, and Rail Transportation in Rural Areas",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68461,65 +68438,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/m2bh-93w3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/m2bh-93w3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/m2bh-93w3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/m2bh-93w3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/m2bh-93w3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/m2bh-93w3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/m2bh-93w3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/m2bh-93w3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/m2bh-93w3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "county",
+            "identifier": "https://data.transportation.gov/api/views/m2bh-93w3",
+            "issued": "2023-09-25",
+            "keyword": [
+                "access",
+                "accessibility",
+                "air",
+                "bus",
+                "intercity",
+                "rail",
+                "rural",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/m2bh-93w3",
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
+            "spatial": "county",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Access to Intercity Air, Bus, and Rail Transportation in Rural Areas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/m2f8-22s6",
             "bureauCode": [
                 "021:27"
             ],
-            "issued": "2023-07-25",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
-            "keyword": [
-                "crossing",
-                "crossing inventory",
-                "form 71",
-                "highway-rail",
-                "inventory"
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
-            "identifier": "https://data.transportation.gov/api/views/m2f8-22s6",
+            "dataQuality": true,
             "description": "This dataset is in a user-friendly human-readable format. It contains the current crossing inventory - one record for each crossing. To download historical data, go here: https://data.transportation.gov/Railroads/Crossing-Inventory-Data-Historical/vhwz-raag. To download the source dataset that contains raw data values, go here: https://data.transportation.gov/dataset/Crossing-Inventory-Source-Data-Form-71-Current/xp92-5xme.",
-            "title": "Crossing Inventory Data (Form 71) - Current",
-            "programCode": [
-                "021:036"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68527,75 +68508,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/m2f8-22s6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/m2f8-22s6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/m2f8-22s6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/m2f8-22s6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/m2f8-22s6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/m2f8-22s6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/m2f8-22s6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/m2f8-22s6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/m2f8-22s6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
-            "theme": [
-                "Railroads"
+            "identifier": "https://data.transportation.gov/api/views/m2f8-22s6",
+            "issued": "2023-07-25",
+            "keyword": [
+                "crossing",
+                "crossing inventory",
+                "form 71",
+                "highway-rail",
+                "inventory"
             ],
+            "landingPage": "https://data.transportation.gov/d/m2f8-22s6",
             "language": [
                 "en-US"
-            ]
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
+            "title": "Crossing Inventory Data (Form 71) - Current"
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
-            "landingPage": "https://data.transportation.gov/d/m2ha-qic9",
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
-            "identifier": "81.2",
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
@@ -68604,31 +68584,64 @@
                     "title": "NHTSA API"
                 }
             ],
-            "spatial": "N/A",
-            "describedBy": "http://www-odi.nhtsa.dot.gov/downloads/folders/Complaints/CMPL.txt",
-            "dataQuality": true,
+            "identifier": "81.2",
+            "isPartOf": "DOT-81",
+            "issued": "2002-12-16",
+            "keyword": [
+                "complaints",
+                "email",
+                "paper",
+                "phone",
+                "safercar.gov"
+            ],
+            "landingPage": "https://data.transportation.gov/d/m2ha-qic9",
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
-            "landingPage": "https://data.transportation.gov/d/m4hg-hmxq",
             "bureauCode": [
                 "021:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kate Hartman",
+                "hasEmail": "mailto:kate.hartman@dot.gov"
+            },
+            "description": "I-4 FRAME project is of strategic importance to FDOT\u2019s emerging technologies and connected vehicle deployments. The project has been thoroughly planned, effectively designed and efficiently procured for realizing the safety, and mobility goals.  The uploaded files contains 20 broad categories based on Connected Vehicle Applications. These are further subdivided folder-wise based on sub-application, with the relevant CSV files within them.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Main dataset has a total of 195 files with approximately 115 MB in size. The data has been submitted as one-time action. Data consists of approximately 200 individual files, with the majority ranging between 100 KB to 1 MB. Half of the files are in tabular CSV format, with the first row consisting of data field headers, and the remaining rows containing data entries, and the other half of the files with the same name are .txt files with the description of the data stored in the .csv files. ",
+                    "downloadURL": "https://its-datahub-files.s3.amazonaws.com/index.html",
+                    "mediaType": "text/html",
+                    "title": "FDOT I-4 FRAME"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/m4hg-hmxq",
             "issued": "2023-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
             "keyword": [
                 "advanced transportation and congestion management technologies deployment (atcmtd)",
                 "connected vehicles",
@@ -68640,47 +68653,52 @@
                 "its joint program office (jpo)",
                 "weather"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/m4hg-hmxq",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-07",
+            "programCode": [
+                "021:042"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/m4hg-hmxq",
-            "description": "I-4 FRAME project is of strategic importance to FDOT\u2019s emerging technologies and connected vehicle deployments. The project has been thoroughly planned, effectively designed and efficiently procured for realizing the safety, and mobility goals.  The uploaded files contains 20 broad categories based on Connected Vehicle Applications. These are further subdivided folder-wise based on sub-application, with the relevant CSV files within them.",
-            "title": "Florida DOT I-4 FRAME (Florida\u2019s Regional Advanced Mobility Elements)",
-            "programCode": [
-                "021:042"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://its-datahub-files.s3.amazonaws.com/index.html",
-                    "description": "Main dataset has a total of 195 files with approximately 115 MB in size. The data has been submitted as one-time action. Data consists of approximately 200 individual files, with the majority ranging between 100 KB to 1 MB. Half of the files are in tabular CSV format, with the first row consisting of data field headers, and the remaining rows containing data entries, and the other half of the files with the same name are .txt files with the description of the data stored in the .csv files. ",
-                    "@type": "dcat:Distribution",
-                    "title": "FDOT I-4 FRAME"
-                }
-            ],
             "spatial": "I-4 from central business district in Tampa to Southwest Orlando.",
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Automobiles"
-            ]
+            ],
+            "title": "Florida DOT I-4 FRAME (Florida\u2019s Regional Advanced Mobility Elements)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/m4it-z7cp",
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
+                    "description": "2011 Washington HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/washington2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Washington"
+                }
+            ],
+            "identifier": "678.49",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -68694,60 +68712,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.49",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Washington",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/m4it-z7cp",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/washington2011.zip",
-                    "description": "2011 Washington HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Washington"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Washington"
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
-            "landingPage": "https://data.transportation.gov/d/m6nn-4xqp",
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
+                    "mediaType": "text/csv",
+                    "title": "New Car Assessment Program (NCAP) - 5 Star Safety Ratings"
+                }
             ],
+            "identifier": "248.3",
+            "isPartOf": "DOT-248",
+            "issued": "2010-01-05",
             "keyword": [
                 "5",
                 "assessment",
@@ -68761,60 +68776,62 @@
                 "safety",
                 "star"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "248.3",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "NCAP rates vehicles to determine crash worthiness and rollover safety. The safety ratings are gathered during controlled crash and rollover tests conducted at NHTSA research facilities. Vehicles with a rating of five stars indicate the highest safety rating, whereas a one star indicates the lowest rating.",
-            "title": "New Car Assessment Program (NCAP) - 5 Star Safety Ratings - New Car Assessment Program (NCAP) - 5 Star Safety Ratings",
-            "isPartOf": "DOT-248",
-            "agencyProgramURL": "http://www.safercar.gov/Vehicle+Shoppers",
+            "landingPage": "https://data.transportation.gov/d/m6nn-4xqp",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-5269",
             "programCode": [
                 "021:031"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://webapi.nhtsa.gov/Default.aspx%3FSafetyRatings/API/5",
-                    "mediaType": "text/csv",
-                    "title": "New Car Assessment Program (NCAP) - 5 Star Safety Ratings"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
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
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/FLAT_RCL.zip",
+            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
+            "analysisUnit": "Vehicles , Tires, Child Safety Seats, Equipment",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/m759-pyxy",
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
+                    "downloadURL": "http://www-odi.nhtsa.dot.gov/owners/SearchSafetyIssues%3FprodType=E",
+                    "mediaType": "text/html",
+                    "title": "Recalls - Equipment"
+                }
             ],
+            "identifier": "83.14",
+            "isPartOf": "DOT-83",
+            "issued": "2002-12-16",
             "keyword": [
                 "air bag",
                 "air bags",
@@ -68841,89 +68858,50 @@
                 "vin",
                 "vin search"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "83.14",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Manufacturers who determine that a product or piece of original equipment either has a safety defect or is not in compliance with Federal safety standards are required to notify the National Highway Traffic Safety Administration (NHTSA) within 5 business days. NHTSA requires that manufacturers file a Defect and Noncompliance report as well as quarterly recall status reports, in compliance with Federal Regulation 49 (the National Traffic and Motor Safety Act) Part 573, which identifies the requirements for safety recalls. This information is stored in the NHTSA database. Use this data to search for recall information related to:-\tSpecific NHTSA campaigns -\tProduct types Access to public searches of NHTSA recall databases for tires, vehicles, car seats and equipment.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - Recalls - Equipment",
-            "isPartOf": "DOT-83",
-            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
-            "describedByType": "text/plain",
+            "landingPage": "https://data.transportation.gov/d/m759-pyxy",
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
-                    "downloadURL": "http://www-odi.nhtsa.dot.gov/owners/SearchSafetyIssues%3FprodType=E",
-                    "mediaType": "text/html",
-                    "title": "Recalls - Equipment"
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
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - Recalls - Equipment"
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
-            "landingPage": "https://data.transportation.gov/d/m79z-hhkd",
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
-            "identifier": "1840.7",
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
@@ -68932,51 +68910,54 @@
                     "title": "Query by vehicle parameters such as make, model, and year"
                 }
             ],
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/veh/vehdb-export-fields.htm",
-            "dataQuality": true,
+            "identifier": "1840.7",
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
+            "landingPage": "https://data.transportation.gov/d/m79z-hhkd",
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
-            "landingPage": "https://data.transportation.gov/d/m8i6-zdsy",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2023-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
-            "keyword": [
-                "form 55",
-                "miles",
-                "operational data",
-                "passenger miles",
-                "safety"
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
-            "identifier": "https://data.transportation.gov/api/views/m8i6-zdsy",
+            "dataQuality": true,
             "description": "This dataset is in a user-friendly human-readable format. To download the source dataset that contains raw data values, go here: https://data.transportation.gov/dataset/Form-55-Source-Table/unww-uhxd.",
-            "title": "Injury/Illness Summary - Operational Data (Form 55)",
-            "programCode": [
-                "021:036"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -68984,111 +68965,146 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/m8i6-zdsy/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/m8i6-zdsy/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/m8i6-zdsy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/m8i6-zdsy/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/m8i6-zdsy/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/m8i6-zdsy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/m8i6-zdsy/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/m8i6-zdsy/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/m8i6-zdsy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/m8i6-zdsy",
+            "issued": "2023-07-19",
+            "keyword": [
+                "form 55",
+                "miles",
+                "operational data",
+                "passenger miles",
+                "safety"
+            ],
+            "landingPage": "https://data.transportation.gov/d/m8i6-zdsy",
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
+            "title": "Injury/Illness Summary - Operational Data (Form 55)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/m8js-a9a4",
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
-            "identifier": "https://data.transportation.gov/api/views/m8js-a9a4",
             "description": "The Great Lakes St. Lawrence Seaway\u2019s navigation season generally begins in late March and closes in late December. Opening and closing dates vary from year to year.",
-            "title": "Great Lakes St. Lawrence Seaway Tonnage",
+            "identifier": "https://data.transportation.gov/api/views/m8js-a9a4",
+            "issued": "2024-12-31",
+            "landingPage": "https://data.transportation.gov/d/m8js-a9a4",
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
+            "title": "Great Lakes St. Lawrence Seaway Tonnage"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/m8rp-gsp3",
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
-            "identifier": "https://data.transportation.gov/api/views/m8rp-gsp3",
             "description": "Personal spending on transportation services includes spending on motor vehicle services, such as maintenance and repair, and public transportation, including rail transportation, intercity buses, taxicabs and ride sharing services, intracity mass transit, air transportation, and water transportation. The Bureau of Economic Analysis estimates personal consumption expenditures, the primary measure of consumer spending on goods and services in the U.S. economy, for each quarter and releases new statistics every month. Quarterly PCE data are seasonally adjusted at annual rates to remove the effects of normal seasonal variation.",
-            "title": "Transportation Services - Seasonally Adjusted",
+            "identifier": "https://data.transportation.gov/api/views/m8rp-gsp3",
+            "issued": "2025-01-02",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/m8rp-gsp3",
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
+            "title": "Transportation Services - Seasonally Adjusted"
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
-            "landingPage": "https://data.transportation.gov/d/m937-689v",
-            "issued": "2010-10-01",
-            "temporal": "R/1996-12-31/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-05",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "https://www.transit.dot.gov/ntd"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NTD Program Support",
+                "hasEmail": "mailto:NTDHelp@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www.ntdprogram.gov/ntdprogram/data.htm",
+            "description": "Data reported to the NTD by urbanized area transit systems in their annual reports.   Includes contact information, contractural relationshps, subrecipient informatino, service area, sources of funds, operating expenditures by object class and function, capital expenditures by object class and function, fixed guideway information, revenue vehicle inventory, fuel consumption, employees, and labor hours, and urbanized area allocation information.   Also includes service supplied and consumed by annual total, average weekday, average saturday, and average sunday.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2008_database/NTD_database_2008.exe",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2008 Database"
+                }
             ],
+            "identifier": "21.12",
+            "isPartOf": "DOT-21",
+            "issued": "2010-10-01",
             "keyword": [
                 "agency",
                 "allocation",
@@ -69107,150 +69123,115 @@
                 "urbanized",
                 "vehicles"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NTD Program Support",
-                "hasEmail": "mailto:NTDHelp@dot.gov"
-            },
-            "identifier": "21.12",
+            "landingPage": "https://data.transportation.gov/d/m937-689v",
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
-            "title": "NTD Annual Module Data Set - 2008 Database",
-            "isPartOf": "DOT-21",
-            "agencyProgramURL": "http://www.ntdprogram.gov",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2008_database/NTD_database_2008.exe",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "2008 Database"
-                }
+            "references": [
+                "https://www.transit.dot.gov/ntd"
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
+            "title": "NTD Annual Module Data Set - 2008 Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/m9eb-yevh",
-            "issued": "2019-12-28",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-16",
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
-            "identifier": "https://data.transportation.gov/api/views/m9eb-yevh",
             "description": "Timely, high-quality national stats from the Bureau of Transportation Statistics",
-            "title": "Monthly Transportation Statistics",
-            "programCode": [
-                "021:053"
+            "identifier": "https://data.transportation.gov/api/views/m9eb-yevh",
+            "issued": "2019-12-28",
+            "keyword": [
+                "monthly transportation statistics"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "landingPage": "https://data.transportation.gov/d/m9eb-yevh",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-06-16",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Monthly Transportation Statistics"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ma52-8ti5",
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
-            "identifier": "https://data.transportation.gov/api/views/ma52-8ti5",
             "description": "The U.S. Census Bureau provides monthly estimates of the total dollar value of construction work done in the United States as part of the Value of Construction Put in Place Survey (VIP). Includes construction related to passenger terminals, mass transit, railroad, maintenance facilities, and freight terminals.",
-            "title": "State and Local Government Construction Spending - Land Transportation",
+            "identifier": "https://data.transportation.gov/api/views/ma52-8ti5",
+            "issued": "2025-01-03",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ma52-8ti5",
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
+            "title": "State and Local Government Construction Spending - Land Transportation"
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
-            "landingPage": "https://data.transportation.gov/d/ma8j-e7nk",
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
-            "identifier": "692.35",
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
@@ -69259,61 +69240,50 @@
                     "title": "Lead"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.35",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ma8j-e7nk",
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
-            "landingPage": "https://data.transportation.gov/d/manf-4hb6",
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
-            "identifier": "https://data.transportation.gov/api/views/manf-4hb6",
             "description": "Test case WFCW-1 Results - FCW Stopped Vehicle Rep 2",
-            "title": "LTE-V2X Wyoming Connected Vehicle Pilot test ID WFCW-1 Rep 2",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69321,44 +69291,92 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/manf-4hb6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/manf-4hb6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/manf-4hb6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/manf-4hb6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/manf-4hb6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/manf-4hb6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/manf-4hb6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/manf-4hb6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/manf-4hb6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Wyoming",
+            "identifier": "https://data.transportation.gov/api/views/manf-4hb6",
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
+            "landingPage": "https://data.transportation.gov/d/manf-4hb6",
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
+            "title": "LTE-V2X Wyoming Connected Vehicle Pilot test ID WFCW-1 Rep 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/mbj2-trkm",
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
+                    "description": "2012 Connecticut HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/connecticut2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Connecticut"
+                }
+            ],
+            "identifier": "678.60",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -69372,101 +69390,65 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.60",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Connecticut",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/mbj2-trkm",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/connecticut2012.zip",
-                    "description": "2012 Connecticut HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Connecticut"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Connecticut"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/mc6b-y96m",
-            "issued": "2024-01-31",
             "@type": "dcat:Dataset",
-            "modified": "2024-07-24",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joe McGill",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "A tool to create estimates for user-defined variables using the VIUS Public use file. Instructions and links to the source material can be found inside the page.",
             "identifier": "https://data.transportation.gov/api/views/mc6b-y96m",
+            "issued": "2024-01-31",
+            "landingPage": "https://data.transportation.gov/d/mc6b-y96m",
+            "modified": "2024-07-24",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "A tool to create estimates for user-defined variables using the VIUS Public use file. Instructions and links to the source material can be found inside the page.",
             "title": "VIUS Tabulation Tool"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.nhtsa.gov/Laws+&+Regulations/Guidance+Documents",
+            "agencyProgramURL": "http://www.nhtsa.gov/Laws+&+Regulations/Guidance+Documents",
+            "analysisUnit": "Regulations",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/mc7k-mvnn",
-            "issued": "2011-01-18",
-            "temporal": "R/2006-01-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.nhtsa.gov/Laws+&+Regulations/Guidance+Documents"
-            ],
-            "keyword": [
-                "data.gov",
-                "law",
-                "significant guidance",
-                "transportation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "DOT-319",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "A list of Significant Guidance documents, which include guidance document disseminated to regulated entities or the general public that may reasonably be anticipated to lead to an annual effect on the economy of $100 million or more or adversely affect in a material way the economy, a sector of the economy, productivity, competition, jobs, the environment, public health or safety, or State, local, or tribal governments or communities; create a serious inconsistency or otherwise interfere with an action taken or planned by another agency; materially alter the budgetary impact of entitlements, grants, user fees, or loan programs or the rights and obligations of recipients thereof; or raise novel legal or policy issues arising out of legal mandates, the President's priorities, or the principles set forth in Executive Order 12866, as further amended.",
-            "title": "Significant Guidance Issued by the National Highway Traffic Safety Administration",
-            "agencyProgramURL": "http://www.nhtsa.gov/Laws+&+Regulations/Guidance+Documents",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69474,58 +69456,58 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "DOT-319",
+            "issued": "2011-01-18",
+            "keyword": [
+                "data.gov",
+                "law",
+                "significant guidance",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/mc7k-mvnn",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.nhtsa.gov/Laws+&+Regulations/Guidance+Documents",
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
+                "http://www.nhtsa.gov/Laws+&+Regulations/Guidance+Documents"
+            ],
+            "temporal": "R/2006-01-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "analysisUnit": "Regulations",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4308",
-            "language": [
-                "en-US"
-            ]
+            "title": "Significant Guidance Issued by the National Highway Traffic Safety Administration"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
+            "agencyDataSeriesURL": "http://www.dot.gov/sites/dot.gov/files/docs/DOT_RnDAssets2015.xlsx",
+            "agencyProgramURL": "http://www.dot.gov/open/research-facilities",
+            "analysisUnit": "Facility",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/mcwr-f47u",
-            "issued": "2015-02-05",
-            "temporal": "R/2015-02-05/P3M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.dot.gov/sites/dot.gov/files/docs/DOT_RnDAssets2015.xlsx"
-            ],
-            "keyword": [
-                "facilities",
-                "research",
-                "technology",
-                "transfer",
-                "transportation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "1672.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
-            "description": "This dataset contains information about designated user-facilities and R&D equipment funded by the U.S. Department of Transportation and accessible to the private sector. These facilities reside throughout the United States and are meant to advance scientific research and accelerated technology commercialization.",
-            "title": "DOT User Facilities and R&D Equipment - List",
-            "agencyProgramURL": "http://www.dot.gov/open/research-facilities",
+            "dataQuality": true,
+            "describedBy": "http://www.dot.gov/sites/dot.gov/files/docs/DOT_RnDAssets2015.xlsx",
             "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "programCode": [
-                "021:053"
-            ],
+            "description": "This dataset contains information about designated user-facilities and R&D equipment funded by the U.S. Department of Transportation and accessible to the private sector. These facilities reside throughout the United States and are meant to advance scientific research and accelerated technology commercialization.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69534,35 +69516,69 @@
                     "title": "List"
                 }
             ],
-            "describedBy": "http://www.dot.gov/sites/dot.gov/files/docs/DOT_RnDAssets2015.xlsx",
-            "dataQuality": true,
+            "identifier": "1672.0",
+            "issued": "2015-02-05",
+            "keyword": [
+                "facilities",
+                "research",
+                "technology",
+                "transfer",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/mcwr-f47u",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.dot.gov/sites/dot.gov/files/docs/DOT_RnDAssets2015.xlsx",
+            "modified": "2024-11-14",
+            "phone": "202-366-0849",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "references": [
+                "http://www.dot.gov/sites/dot.gov/files/docs/DOT_RnDAssets2015.xlsx"
+            ],
+            "temporal": "R/2015-02-05/P3M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P3M",
-            "categoryDesignation": "Administrative",
-            "analysisUnit": "Facility",
-            "phone": "202-366-0849",
-            "language": [
-                "en-US"
-            ]
+            "title": "DOT User Facilities and R&D Equipment - List"
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
-            "landingPage": "https://data.transportation.gov/d/mf5d-ue9a",
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
+                    "downloadURL": "http://www.fra.dot.gov/eLib/Details/L04111",
+                    "mediaType": "text/csv",
+                    "title": "Signalmen Background Survey"
+                }
             ],
+            "identifier": "283.5",
+            "isPartOf": "DOT-283",
+            "issued": "2008-03-01",
             "keyword": [
                 "alertness",
                 "employee",
@@ -69573,61 +69589,59 @@
                 "sleep",
                 "work"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "283.5",
+            "landingPage": "https://data.transportation.gov/d/mf5d-ue9a",
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
-            "title": "Work Schedules and Sleep Patterns of Railroad Employees - Signalmen Background Survey",
-            "isPartOf": "DOT-283",
-            "agencyProgramURL": "http://www.fra.dot.gov/Page/P0068",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fra.dot.gov/eLib/Details/L04111",
-                    "mediaType": "text/csv",
-                    "title": "Signalmen Background Survey"
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
+            "title": "Work Schedules and Sleep Patterns of Railroad Employees - Signalmen Background Survey"
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
-            "landingPage": "https://data.transportation.gov/d/mffm-7krj",
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
+            "identifier": "322.2",
+            "isPartOf": "DOT-322",
+            "issued": "2011-01-18",
             "keyword": [
                 "administrative law judge opinions",
                 "airline citizenship",
@@ -69644,80 +69658,48 @@
                 "motor carriers",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DOT Socrata",
-                "hasEmail": "mailto:Socrata@dot.gov"
-            },
-            "identifier": "322.2",
+            "landingPage": "https://data.transportation.gov/d/mffm-7krj",
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
-            "title": "Administrative Law Judge Opinions issued by the Office of the Secretary of Transportation -",
-            "isPartOf": "DOT-322",
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
+            "title": "Administrative Law Judge Opinions issued by the Office of the Secretary of Transportation -"
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
-            "landingPage": "https://data.transportation.gov/d/mhas-eabg",
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
-            "identifier": "364.11",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database - Vehicle Database Export",
-            "isPartOf": "DOT-364",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
-            "primaryITInvestmentUII": "021-621341357",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69726,52 +69708,51 @@
                     "title": "Vehicle Database Export"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.11",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/mhas-eabg",
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
+            "title": "Vehicle Safety Research and Development Database - Vehicle Database Export"
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
-                "name": "data.transportation.gov"
-            },
-            "identifier": "https://data.transportation.gov/api/views/mhuc-n78n",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 1991",
-            "title": "Historic HPMS Data (Universe) - 1991",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -69779,45 +69760,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/mhuc-n78n/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/mhuc-n78n/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/mhuc-n78n/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/mhuc-n78n/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/mhuc-n78n/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/mhuc-n78n/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/mhuc-n78n/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/mhuc-n78n/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/mhuc-n78n/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/mhuc-n78n",
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
+            "title": "Historic HPMS Data (Universe) - 1991"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.21949/1503750",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Transportation Library Data Curator",
+                "hasEmail": "mailto:ntldatacurator@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This zip file contains 45 files of data to support FHWA-JPO-13-063 Response, Emergency Staging, Communications, Uniform Management, and Evacuation (R.E.S.C.U.M.E.) : Concept of Operations. Zip size is 9.9 MB. The files have been uploaded as-is; no further documentation was supplied by NTL. The attached zip files can be unzipped using any zip compression/decompression software. These zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .txt. files that may be opened with any text editing software; .docx files that may be opened with Microsoft Word; .kml files, Keyhole markup Language files, which are a XML file type and may be opened with any text editor [software requirements]. Files were accessed in 2017.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "This zip file contains 45 files of data to support FHWA-JPO-13-063 Response, Emergency Staging, Communications, Uniform Management, and Evacuation (R.E.S.C.U.M.E.) : Concept of Operations. Zip size is 9.9 MB. The files have been uploaded as-is; no further documentation was supplied by NTL. The attached zip files can be unzipped using any zip compression/decompression software. These zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .txt. files that may be opened with any text editing software; .docx files that may be opened with Microsoft Word; .kml files, Keyhole markup Language files, which are a XML file type and may be opened with any text editor [software requirements]. Files were accessed in 2017.",
+                    "downloadURL": "https://doi.org/10.21949/1503750",
+                    "mediaType": "application/zip",
+                    "title": "Response, Emergency Staging, Communications, Uniform Management, and Evacuation (R.E.S.C.U.M.E.): Concept of Operations [supporting datasets]"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/mi9k-kefq",
             "issued": "2017-10-13",
-            "@type": "dcat:Dataset",
-            "modified": "2017-10-13",
             "keyword": [
                 "data sharing",
                 "disasters and emergency operations",
@@ -69827,70 +69841,71 @@
                 "rescume",
                 "r.e.s.c.u.m.e."
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Transportation Library Data Curator",
-                "hasEmail": "mailto:ntldatacurator@dot.gov"
-            },
+            "landingPage": "https://doi.org/10.21949/1503750",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2017-10-13",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/mi9k-kefq",
-            "description": "This zip file contains 45 files of data to support FHWA-JPO-13-063 Response, Emergency Staging, Communications, Uniform Management, and Evacuation (R.E.S.C.U.M.E.) : Concept of Operations. Zip size is 9.9 MB. The files have been uploaded as-is; no further documentation was supplied by NTL. The attached zip files can be unzipped using any zip compression/decompression software. These zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .txt. files that may be opened with any text editing software; .docx files that may be opened with Microsoft Word; .kml files, Keyhole markup Language files, which are a XML file type and may be opened with any text editor [software requirements]. Files were accessed in 2017.",
-            "title": "Response, Emergency Staging, Communications, Uniform Management, and Evacuation (R.E.S.C.U.M.E.): Concept of Operations [supporting datasets]",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://doi.org/10.21949/1503750",
-                    "description": "This zip file contains 45 files of data to support FHWA-JPO-13-063 Response, Emergency Staging, Communications, Uniform Management, and Evacuation (R.E.S.C.U.M.E.) : Concept of Operations. Zip size is 9.9 MB. The files have been uploaded as-is; no further documentation was supplied by NTL. The attached zip files can be unzipped using any zip compression/decompression software. These zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .txt. files that may be opened with any text editing software; .docx files that may be opened with Microsoft Word; .kml files, Keyhole markup Language files, which are a XML file type and may be opened with any text editor [software requirements]. Files were accessed in 2017.",
-                    "@type": "dcat:Distribution",
-                    "title": "Response, Emergency Staging, Communications, Uniform Management, and Evacuation (R.E.S.C.U.M.E.): Concept of Operations [supporting datasets]"
-                }
-            ],
             "spatial": "United States",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "language": [
-                "en-US"
-            ]
+            "title": "Response, Emergency Staging, Communications, Uniform Management, and Evacuation (R.E.S.C.U.M.E.): Concept of Operations [supporting datasets]"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/mign-rc8p",
-            "issued": "2021-05-19",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sean Jahanmir",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/mign-rc8p",
+            "issued": "2021-05-19",
+            "landingPage": "https://data.transportation.gov/d/mign-rc8p",
+            "modified": "2025-01-27",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Home | BTS Port Performance Freight Statistics Program"
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
-            "landingPage": "https://data.transportation.gov/d/mimc-qa8y",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/10jultvt/10jultvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "July 2010"
+                }
             ],
+            "identifier": "18.20",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -69900,60 +69915,61 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.20",
+            "landingPage": "https://data.transportation.gov/d/mimc-qa8y",
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
-            "title": "Monthly Traffic Volume Trends - July 2010",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/10jultvt/10jultvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "July 2010"
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
+            "title": "Monthly Traffic Volume Trends - July 2010"
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
-            "landingPage": "https://data.transportation.gov/d/miub-cu89",
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
+                    "downloadURL": "http://faf.ornl.gov/fafweb/FUT.aspx",
+                    "mediaType": "text/html",
+                    "title": "All FAF summary datasets"
+                }
             ],
+            "identifier": "286.6",
+            "isPartOf": "DOT-286",
+            "issued": "2013-03-20",
             "keyword": [
                 "commodity",
                 "consumption",
@@ -69978,61 +69994,61 @@
                 "value",
                 "wear"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "286.6",
+            "landingPage": "https://data.transportation.gov/d/miub-cu89",
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
-            "title": "Freight Analysis Framework - All FAF summary datasets",
-            "isPartOf": "DOT-286",
-            "agencyProgramURL": "http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://faf.ornl.gov/fafweb/FUT.aspx",
-                    "mediaType": "text/html",
-                    "title": "All FAF summary datasets"
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
+            "title": "Freight Analysis Framework - All FAF summary datasets"
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
-            "landingPage": "https://data.transportation.gov/d/mivp-8kw9",
-            "issued": "2013-11-19",
-            "temporal": "2006-01-01/2010-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
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
+            "identifier": "DOT-337",
+            "issued": "2013-11-19",
             "keyword": [
                 "access",
                 "affordability",
@@ -70045,84 +70061,49 @@
                 "transit",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "DOT-337",
+            "landingPage": "https://data.transportation.gov/d/mivp-8kw9",
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
-            "title": "Location Affordability Index",
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
+            "title": "Location Affordability Index"
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
-            "landingPage": "https://data.transportation.gov/d/mix3-nnjg",
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
-            "identifier": "DOT-330",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Research and Innovative Technology Administration"
-            },
+            "dataQuality": true,
             "description": "FOIA Electronic Reading Room - Final Opinions/Orders in Adjudicated Cases",
-            "title": "Administrative Law Judge Opinions issued by the Research and Innovative Technology Administration",
-            "agencyProgramURL": "http://www.rita.dot.gov/freedom_of_information_act/",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70130,50 +70111,51 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "DOT-330",
+            "issued": "2011-01-18",
+            "keyword": [
+                "administrative law",
+                "data.gov",
+                "foia",
+                "law",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/mix3-nnjg",
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
+            "title": "Administrative Law Judge Opinions issued by the Research and Innovative Technology Administration"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/mjx8-bw4c",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-09-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-30",
-            "keyword": [
-                "commodity",
-                "port",
-                "ports",
-                "waterways tonnage"
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
-            "identifier": "https://data.transportation.gov/api/views/mjx8-bw4c",
             "description": "Source: U.S. Department of Transportation, Bureau of Transportation Statistics based upon U.S. Department of Commerce, U.S. Census Bureau, Foreign Trade Division, USA Trade Online, \"HS Port-level Data\", available at https://usatrade.census.gov/ as of Sept 2024.",
-            "title": "Value of Containerized Exports by Coast in 2023",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70181,72 +70163,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/mjx8-bw4c/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/mjx8-bw4c/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/mjx8-bw4c/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/mjx8-bw4c/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/mjx8-bw4c/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/mjx8-bw4c/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/mjx8-bw4c/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/mjx8-bw4c/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/mjx8-bw4c/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/mjx8-bw4c",
+            "issued": "2024-09-30",
+            "keyword": [
+                "commodity",
+                "port",
+                "ports",
+                "waterways tonnage"
+            ],
+            "landingPage": "https://data.transportation.gov/d/mjx8-bw4c",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-09-30",
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
+            "title": "Value of Containerized Exports by Coast in 2023"
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
-            "landingPage": "https://data.transportation.gov/d/mkvy-hv4q",
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
-            "identifier": "DOT-1637",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
             "description": "The 2008 National Survey of Drinking and Driving Attitudes and Behaviors was composed of a single questionnaire administered to a sample of randomly selected individuals 16 and older, with ages 16 through 24 over-sampled. The respondents were asked about their drinking behavior, their drinking and driving behavior, use of designated drivers, their hosting events in which drinking occurred, risks they perceive associated with drinking and driving, experience with anti-DWI enforcement activity, and their attitudes concerning major intervention strategies.The survey was administered from September 10, 2008 to December 22, 2008. A total of 6,999 respondents completed the survey, including 5,392 landline interviews and 1,607 cell phone interviews. The total number of completed interviews for each of the four Census regions (Northeast, Midwest, South, and West) was 1,409, 1,654, 2,390, and 1,546, respectively.",
-            "title": "2008 National Survey of Drinking and Driving Attitudes and Behaviors",
-            "agencyProgramURL": "http://www.nhtsa.gov/Driving+Safety/Occupant+Protection/2008+National+Survey+of+Drinking+and+Driving+Attitudes+and+Behaviors",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70255,38 +70236,47 @@
                     "title": "SPSS Database File"
                 }
             ],
-            "spatial": "n/a",
-            "dataQuality": false,
+            "identifier": "DOT-1637",
+            "issued": "2010-08-31",
+            "keyword": [
+                "attitudes",
+                "behaviors",
+                "drinking",
+                "driving"
+            ],
+            "landingPage": "https://data.transportation.gov/d/mkvy-hv4q",
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
+            "title": "2008 National Survey of Drinking and Driving Attitudes and Behaviors"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/mmgn-pg9s",
-            "issued": "2022-01-26",
             "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "US Department of Transportation"
-            },
-            "identifier": "https://data.transportation.gov/api/views/mmgn-pg9s",
             "description": "RAISE Program Persistent Poverty Dataset.",
-            "title": "RAISE Persistent Poverty",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70294,81 +70284,106 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/mmgn-pg9s/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/mmgn-pg9s/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/mmgn-pg9s/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/mmgn-pg9s/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/mmgn-pg9s/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/mmgn-pg9s/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/mmgn-pg9s/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/mmgn-pg9s/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/mmgn-pg9s/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/mmgn-pg9s",
+            "issued": "2022-01-26",
+            "landingPage": "https://data.transportation.gov/d/mmgn-pg9s",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-14",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
             "theme": [
                 "Administrative"
-            ]
+            ],
+            "title": "RAISE Persistent Poverty"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/mmn6-892i",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:answers@dot.gov"
+            },
+            "description": "The movement of a passenger for a distance of one mile. The Federal Railroad Administration collects accident/incident and operational data from railroads. Tourist and commuter railroad are excluded.",
+            "identifier": "https://data.transportation.gov/api/views/mmn6-892i",
             "issued": "2025-01-03",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-03",
             "keyword": [
                 "monthly transportation statistics"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:answers@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/mmn6-892i",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-03",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/mmn6-892i",
-            "description": "The movement of a passenger for a distance of one mile. The Federal Railroad Administration collects accident/incident and operational data from railroads. Tourist and commuter railroad are excluded.",
-            "title": "Intercity Passenger Rail Travel - Passenger-Miles",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "theme": [
                 "Research and Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Intercity Passenger Rail Travel - Passenger-Miles"
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
-            "landingPage": "https://data.transportation.gov/d/mmv8-jgga",
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
+            "identifier": "DOT-679",
+            "issued": "1993-07-01",
             "keyword": [
                 "asphalt concrete",
                 "continuously reinforced concrete pavement",
@@ -70385,84 +70400,48 @@
                 "texture",
                 "traffic loading"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "DOT-679",
+            "landingPage": "https://data.transportation.gov/d/mmv8-jgga",
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
-            "title": "Long-Term Pavement Performance (LTPP)",
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
+            "title": "Long-Term Pavement Performance (LTPP)"
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
-            "landingPage": "https://data.transportation.gov/d/mn78-48fx",
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
-            "identifier": "524.19",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
             "description": "STATE DATA REPORTING SYSTEMS. Annual reports on the Fatality Analysis Reporting System (FARS) which is data regarding fatalities that is collected by a FARS analyst from each State and provided to NHTSA.",
-            "title": "GES Reports - 1994",
-            "isPartOf": "DOT-524",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70471,85 +70450,87 @@
                     "title": "1994"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
-            "dataQuality": true,
+            "identifier": "524.19",
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
+            "landingPage": "https://data.transportation.gov/d/mn78-48fx",
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
+            "title": "GES Reports - 1994"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/mnwf-3med",
             "bureauCode": [
                 "021:27"
             ],
-            "issued": "2024-11-22",
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
-            "identifier": "https://data.transportation.gov/api/views/mnwf-3med",
+            "dataQuality": true,
             "description": "This is the landing page for the Form 6180.55a Injury/Illness Continuation Sheet [Casualty] data.",
-            "title": "Form 55a Data Downloads",
+            "identifier": "https://data.transportation.gov/api/views/mnwf-3med",
+            "issued": "2024-11-22",
+            "landingPage": "https://data.transportation.gov/d/mnwf-3med",
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
+            "title": "Form 55a Data Downloads"
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
-            "identifier": "https://data.transportation.gov/api/views/mp2w-t2nd",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 1990",
-            "title": "Historic HPMS Data (Universe) - 1990",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70557,54 +70538,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/mp2w-t2nd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/mp2w-t2nd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/mp2w-t2nd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/mp2w-t2nd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/mp2w-t2nd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/mp2w-t2nd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/mp2w-t2nd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/mp2w-t2nd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/mp2w-t2nd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/mp2w-t2nd",
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
+            "title": "Historic HPMS Data (Universe) - 1990"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/mqfn-syak",
-            "issued": "2024-10-25",
             "@type": "dcat:Dataset",
-            "modified": "2024-10-25",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "theresa.firestine",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/mqfn-syak",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "The Bikeshare dataset was compiled on August 10, 2021 and was updated October 19, 2022 from the Bureau of Transportation Statistics (BTS) and is part of the U.S. Department of Transportation (USDOT)/Bureau of Transportation Statistics (BTS) National Transportation Atlas Database (NTAD). The IPCD is a nationwide database of passenger transportation terminals, with data on the availability of connections among the various scheduled public transportation modes at each facility. The IPCD data covers the following types of passenger transportation terminals/stops: 1. Scheduled airline service airports. 2. Intercity bus stations (includes stations served by regular scheduled intercity bus service such as Greyhound, Trailways, code sharing buses such as Amtrak Thruway feeder buses, supplemental buses that provide additional frequencies along rail routes, and airport bus services from locations that are outside of the airport metropolitan area). 3. Intercity and transit ferry terminals. 4. Light-rail transit stations. 5. Heavy-rail transit stations. 6. Passenger-rail stations on the national rail network served by intercity rail and/or commuter rail services. 7. Bike-share stations belonging to bike-share systems that are open to the general public, IT-automated, and station based (contain hubs to which users can grab and return a bike). The data elements describe the location of the above types of terminals as well as the availability of intercity, commuter, and transit rail; scheduled air service; intercity and transit bus; intercity and transit ferry services; and bike-share availability. Transit bus service locations are not specifically included in the database. However, the status of transit bus as a connecting mode is included for each bike-share facility in the database.",
-            "title": "Bikeshare",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70612,42 +70602,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/mqfn-syak/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/mqfn-syak/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/mqfn-syak/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/mqfn-syak/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/mqfn-syak/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/mqfn-syak/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/mqfn-syak/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/mqfn-syak/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/mqfn-syak/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "https://data.transportation.gov/api/views/mqfn-syak",
+            "issued": "2024-10-25",
+            "landingPage": "https://data.transportation.gov/d/mqfn-syak",
+            "modified": "2024-10-25",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
+            "title": "Bikeshare"
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
-            "landingPage": "https://data.transportation.gov/d/msbh-h49n",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/04dectvt/04dectvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "December 2004"
+                }
             ],
+            "identifier": "18.117",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -70657,57 +70672,60 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.117",
+            "landingPage": "https://data.transportation.gov/d/msbh-h49n",
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
-            "title": "Monthly Traffic Volume Trends - December 2004",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/04dectvt/04dectvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "December 2004"
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
+            "title": "Monthly Traffic Volume Trends - December 2004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/msk9-xb6p",
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
+                    "description": "2013 Utah HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/utah2013.zip",
+                    "mediaType": "text/html",
+                    "title": "2013 Utah"
+                }
+            ],
+            "identifier": "678.154",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -70721,60 +70739,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.154",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Utah",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/msk9-xb6p",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/utah2013.zip",
-                    "description": "2013 Utah HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Utah"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Utah"
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
-            "landingPage": "https://data.transportation.gov/d/mt26-g4gk",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/08augtvt/08augtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "August 2008"
+                }
             ],
+            "identifier": "18.73",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -70784,84 +70799,42 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.73",
+            "landingPage": "https://data.transportation.gov/d/mt26-g4gk",
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
-            "title": "Monthly Traffic Volume Trends - August 2008",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/08augtvt/08augtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "August 2008"
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
+            "title": "Monthly Traffic Volume Trends - August 2008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://ops.fhwa.dot.gov/freight/sw/index.htm",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2021-03-25",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-01",
-            "keyword": [
-                "citations",
-                "os/ow",
-                "os/ow permits",
-                "oversize/overweight",
-                "truck",
-                "truck size and weight",
-                "vehicle size and weight",
-                "violation",
-                "weigh-in-motion",
-                "weigh stations",
-                "weight",
-                "wim"
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
-            "identifier": "https://data.transportation.gov/api/views/mt5m-skz3",
             "description": "This dataset consists of truck size and weight enforcement data including number of trucks weighed, number of violations, and number of oversize/overweight permits, as reported by the States in their annual certification to FHWA.",
-            "title": "Truck Size and Weight Enforcement Data",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -70869,69 +70842,111 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/mt5m-skz3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/mt5m-skz3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/mt5m-skz3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/mt5m-skz3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/mt5m-skz3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/mt5m-skz3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/mt5m-skz3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/mt5m-skz3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/mt5m-skz3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "USA",
+            "identifier": "https://data.transportation.gov/api/views/mt5m-skz3",
+            "issued": "2021-03-25",
+            "keyword": [
+                "citations",
+                "os/ow",
+                "os/ow permits",
+                "oversize/overweight",
+                "truck",
+                "truck size and weight",
+                "vehicle size and weight",
+                "violation",
+                "weigh-in-motion",
+                "weigh stations",
+                "weight",
+                "wim"
+            ],
+            "landingPage": "https://ops.fhwa.dot.gov/freight/sw/index.htm",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-08-01",
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
+            "title": "Truck Size and Weight Enforcement Data"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/mu69-gcck",
-            "issued": "2021-04-28",
             "@type": "dcat:Dataset",
-            "modified": "2022-11-29",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Chambers",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/mu69-gcck",
+            "issued": "2021-04-28",
+            "landingPage": "https://data.transportation.gov/d/mu69-gcck",
+            "modified": "2022-11-29",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Ro/Ro Vessel Dwell Times"
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
-            "landingPage": "https://data.transportation.gov/d/mudk-t6dx",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/09dectvt/09dectvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "December 2009"
+                }
             ],
+            "identifier": "18.27",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -70941,56 +70956,52 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.27",
+            "landingPage": "https://data.transportation.gov/d/mudk-t6dx",
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
-            "title": "Monthly Traffic Volume Trends - December 2009",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/09dectvt/09dectvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "December 2009"
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
+            "title": "Monthly Traffic Volume Trends - December 2009"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/mupt-aksf",
             "bureauCode": [
                 "021:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kate Hartman",
+                "hasEmail": "mailto:kate.hartman@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "As part of the Federal Highway Administration\u2019s (FHWA) Next Generation Simulation (NGSIM) project, video data were collected on November 8th, 2006 on an arterial segment on Peachtree Street located in Atlanta, Georgia. The data represents 30 minutes total, segmented into two periods (12:45 p.m. to 1:00 p.m. and 4:00 p.m. to 4:15 p.m.). The dataset includes files for both raw and processed video data from each of the eight cameras for the two time periods available for download. Camera numbering is in order of southern-most (1) to northern-most (8). The raw video files give the original vehicle movement data and offer users a view of how the section was observed. The processed video files provide videos of the vehicles along with a superimposition of the vehicle identification numbers. These videos can be used alone or can be used for cross referencing of the textual vehicle trajectory data provided in the NGSIM trajectory data with the corresponding video.\n\nFor related datasets please see the following:\n- NGSIM Vehicle Trajectories and Supporting Data: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Vehicle-Trajector/8ect-6jqj\n- NGSIM I-80 Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-I-80-Vide/2577-gpny\n- NGSIM US-101 Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-US-101-Vi/4qzi-thur\n- NGSIM Lankershim Boulevard Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-Lankershi/uv3e-y54k",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/download/mupt-aksf/application/pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/mupt-aksf",
             "issued": "2016-01-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2006-11-08",
-            "modified": "2016-01-01",
             "keyword": [
                 "arterial",
                 "atlanta",
@@ -71001,49 +71012,56 @@
                 "peachtree st",
                 "video"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/mupt-aksf",
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
-            "identifier": "https://data.transportation.gov/api/views/mupt-aksf",
-            "description": "As part of the Federal Highway Administration\u2019s (FHWA) Next Generation Simulation (NGSIM) project, video data were collected on November 8th, 2006 on an arterial segment on Peachtree Street located in Atlanta, Georgia. The data represents 30 minutes total, segmented into two periods (12:45 p.m. to 1:00 p.m. and 4:00 p.m. to 4:15 p.m.). The dataset includes files for both raw and processed video data from each of the eight cameras for the two time periods available for download. Camera numbering is in order of southern-most (1) to northern-most (8). The raw video files give the original vehicle movement data and offer users a view of how the section was observed. The processed video files provide videos of the vehicles along with a superimposition of the vehicle identification numbers. These videos can be used alone or can be used for cross referencing of the textual vehicle trajectory data provided in the NGSIM trajectory data with the corresponding video.\n\nFor related datasets please see the following:\n- NGSIM Vehicle Trajectories and Supporting Data: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Vehicle-Trajector/8ect-6jqj\n- NGSIM I-80 Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-I-80-Vide/2577-gpny\n- NGSIM US-101 Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-US-101-Vi/4qzi-thur\n- NGSIM Lankershim Boulevard Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-Lankershi/uv3e-y54k",
-            "title": "Next Generation Simulation (NGSIM) Program Peachtree Street Videos",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/download/mupt-aksf/application/pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
             "spatial": "Atlanta, Georgia",
-            "dataQuality": true,
-            "license": "http://creativecommons.org/licenses/by-sa/4.0/legalcode",
+            "temporal": "2006-11-08",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Next Generation Simulation (NGSIM) Program Peachtree Street Videos"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/murd-f5xb",
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
+                    "description": "2011 Hawaii HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/hawaii2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Hawaii"
+                }
+            ],
+            "identifier": "678.13",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -71057,57 +71075,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.13",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Hawaii",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/murd-f5xb",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/hawaii2011.zip",
-                    "description": "2011 Hawaii HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Hawaii"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Hawaii"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/mw7x-gdda",
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
+                    "description": "2011 District of Columbia HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/district2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 District of Columbia"
+                }
+            ],
+            "identifier": "678.10",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -71121,73 +71139,39 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.10",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 District of Columbia",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/mw7x-gdda",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/district2011.zip",
-                    "description": "2011 District of Columbia HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 District of Columbia"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 District of Columbia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://data.transportation.gov/d/mwaz-n68f",
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
-            "identifier": "https://data.transportation.gov/api/views/mwaz-n68f",
             "description": "",
-            "title": "Pocket Guide to Transportation-Transportation Network Length",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71195,40 +71179,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/mwaz-n68f/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/mwaz-n68f/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/mwaz-n68f/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/mwaz-n68f/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/mwaz-n68f/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/mwaz-n68f/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/mwaz-n68f/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/mwaz-n68f/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/mwaz-n68f/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "https://data.transportation.gov/api/views/mwaz-n68f",
+            "issued": "2024-02-01",
+            "keyword": [
+                "pocket guide to transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/mwaz-n68f",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-02-01",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Pocket Guide to Transportation-Transportation Network Length"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/mx8t-gmyk",
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
+                    "description": "2013 Texas HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/texas2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Texas"
+                }
+            ],
+            "identifier": "678.147",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -71242,60 +71260,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.147",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Texas",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/mx8t-gmyk",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/texas2013.zip",
-                    "description": "2013 Texas HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Texas"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Texas"
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
-            "landingPage": "https://data.transportation.gov/d/mxa4-xcd3",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/09augtvt/09augtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "August 2009"
+                }
             ],
+            "identifier": "18.31",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -71305,77 +71320,43 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.31",
+            "landingPage": "https://data.transportation.gov/d/mxa4-xcd3",
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
-            "title": "Monthly Traffic Volume Trends - August 2009",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/09augtvt/09augtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "August 2009"
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
+            "title": "Monthly Traffic Volume Trends - August 2009"
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
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/mxiv-t53i",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 1989",
-            "title": "Historic HPMS Data (Universe) - 1989",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71383,50 +71364,85 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/mxiv-t53i/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/mxiv-t53i/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/mxiv-t53i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/mxiv-t53i/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/mxiv-t53i/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/mxiv-t53i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/mxiv-t53i/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/mxiv-t53i/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/mxiv-t53i/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/mxiv-t53i",
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
+            "title": "Historic HPMS Data (Universe) - 1989"
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
-            "landingPage": "https://data.transportation.gov/d/mxwu-xxfn",
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
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2003NTDxls.exe",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2003 Database"
+                }
             ],
+            "identifier": "21.7",
+            "isPartOf": "DOT-21",
+            "issued": "2010-10-01",
             "keyword": [
                 "agency",
                 "allocation",
@@ -71445,102 +71461,67 @@
                 "urbanized",
                 "vehicles"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John D. Giorgis",
-                "hasEmail": "mailto:john.giorgis@dot.gov"
-            },
-            "identifier": "21.7",
+            "landingPage": "https://data.transportation.gov/d/mxwu-xxfn",
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
-            "title": "NTD Annual Module Data Set - 2003 Database",
-            "isPartOf": "DOT-21",
-            "agencyProgramURL": "http://www.ntdprogram.gov",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2003NTDxls.exe",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "2003 Database"
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
+            "title": "NTD Annual Module Data Set - 2003 Database"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/myhq-rm6q",
-            "issued": "2023-10-20",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sean Jahanmir",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/myhq-rm6q",
+            "issued": "2023-10-20",
+            "landingPage": "https://data.transportation.gov/d/myhq-rm6q",
+            "modified": "2025-01-31",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Data Dashboard"
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
-            "landingPage": "https://data.transportation.gov/d/mymy-fe88",
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
-            "identifier": "692.28",
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
@@ -71549,56 +71530,56 @@
                     "title": "8-Hour Ozone"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.28",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/mymy-fe88",
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
+            "agencyDataSeriesURL": "http://hepgis.fhwa.dot.gov/hepgismaps11/#",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/mz9r-82mk",
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
-            "identifier": "692.11",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - Pedestrian Fatal Crashes 2009-2012",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "primaryITInvestmentUII": "021-845083703",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71607,44 +71588,50 @@
                     "title": "Pedestrian Fatal Crashes 2009-2012"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.11",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/mz9r-82mk",
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
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - Pedestrian Fatal Crashes 2009-2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/mzmm-6xep",
             "bureauCode": [
                 "021:17"
             ],
-            "issued": "2023-04-14",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO Office",
                 "hasEmail": "mailto:FMCSA.CDO@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/mzmm-6xep",
             "description": "*This is a \"daily difference\" dataset.  See dataset attachment \"FMCSA Dataset Description and Data Definitions - Select Datasets\" for more information.*  Records for carrier/broker/freight forwarder active or pending individual insurance policies. The records are linked to the entities by docket numbers included in the dataset. The dataset contains information on the insurance policy, including insurance company name, policy number and type of insurance. Entities can hold multiple insurance policies, so there may be multiple records associated with a particular entity.",
-            "title": "Insur",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71652,25 +71639,53 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/mzmm-6xep",
+            "issued": "2023-04-14",
+            "landingPage": "https://data.transportation.gov/d/mzmm-6xep",
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
+            "title": "Insur"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.nhtsa.gov/content/nhtsa-ftp/251",
+            "agencyProgramURL": "http://www-fars.nhtsa.dot.gov/Main/index.aspx",
+            "analysisUnit": "Crash  / Vehicle  / driver /person",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/mzrg-xkip",
-            "issued": "1980-01-01",
-            "temporal": "R/1975-01-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Statistical",
             "collectionInstrument": "Web application",
-            "references": [
-                "http://www-fars.nhtsa.dot.gov/Main/index.aspx"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www-fars.nhtsa.dot.gov/Main/index.aspx",
+            "description": "The program collects data for analysis of traffic safety crashes to identify problems, and evaluate countermeasures leading to reducing injuries and property damage resulting from motor vehicle crashes. The FARS dataset contains descriptions, in standard format, of each fatal crash reported.  To qualify for inclusion, a crash must involve a motor vehicle traveling a traffic-way customarily open to the public and resulting in the death of a person (occupant of a vehicle or a non-motorist) within 30 days of the crash.  Each crash has more than 100 coded data elements that characterize the crash, the vehicles, and the people involved.  The specific data elements may be changed slightly each year to conform to the changing user needs, vehicle characteristics and highway safety emphasis areas.  The type of information that FARS, a major application, processes is therefore motor vehicle crash data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www-fars.nhtsa.dot.gov/QueryTool/QuerySection/SelectYear.aspx",
+                    "mediaType": "text/html",
+                    "title": "Online Query Tool"
+                }
             ],
+            "identifier": "DOT-25",
+            "issued": "1980-01-01",
             "keyword": [
                 "crash",
                 "death",
@@ -71681,82 +71696,49 @@
                 "injury",
                 "vehicle"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "DOT-25",
+            "landingPage": "https://data.transportation.gov/d/mzrg-xkip",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-2622",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Highway Traffic Safety Administration"
             },
-            "description": "The program collects data for analysis of traffic safety crashes to identify problems, and evaluate countermeasures leading to reducing injuries and property damage resulting from motor vehicle crashes. The FARS dataset contains descriptions, in standard format, of each fatal crash reported.  To qualify for inclusion, a crash must involve a motor vehicle traveling a traffic-way customarily open to the public and resulting in the death of a person (occupant of a vehicle or a non-motorist) within 30 days of the crash.  Each crash has more than 100 coded data elements that characterize the crash, the vehicles, and the people involved.  The specific data elements may be changed slightly each year to conform to the changing user needs, vehicle characteristics and highway safety emphasis areas.  The type of information that FARS, a major application, processes is therefore motor vehicle crash data.",
-            "title": "Fatality Analysis Reporting System ( FARS )",
-            "agencyProgramURL": "http://www-fars.nhtsa.dot.gov/Main/index.aspx",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www-fars.nhtsa.dot.gov/QueryTool/QuerySection/SelectYear.aspx",
-                    "mediaType": "text/html",
-                    "title": "Online Query Tool"
-                }
+            "references": [
+                "http://www-fars.nhtsa.dot.gov/Main/index.aspx"
             ],
             "spatial": "latitude/longitude",
-            "describedBy": "http://www-fars.nhtsa.dot.gov/Main/index.aspx",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "https://www.nhtsa.gov/content/nhtsa-ftp/251",
+            "temporal": "R/1975-01-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Statistical",
-            "analysisUnit": "Crash  / Vehicle  / driver /person",
-            "phone": "202-366-2622",
-            "language": [
-                "en-US"
-            ]
+            "title": "Fatality Analysis Reporting System ( FARS )"
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
-            "landingPage": "https://data.transportation.gov/d/mzz6-86rb",
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
-            "identifier": "364.23",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2005",
-            "isPartOf": "DOT-364",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
-            "primaryITInvestmentUII": "021-621341357",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71765,35 +71747,69 @@
                     "title": "Event Data Records Reports - 2005"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.23",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/mzz6-86rb",
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
+            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2005"
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
-            "landingPage": "https://data.transportation.gov/d/n2bg-y3i6",
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
+                    "description": "This access point provides access to the LTPP InfoPave search features including contextual full-text, sections, data, library, and ancillary data search.",
+                    "downloadURL": "https://infopave.fhwa.dot.gov/%3FGoto=Search",
+                    "mediaType": "application/zip",
+                    "title": "Search"
+                }
             ],
+            "identifier": "679.5",
+            "isPartOf": "DOT-679",
+            "issued": "1993-07-01",
             "keyword": [
                 "asphalt concrete",
                 "continuously reinforced concrete pavement",
@@ -71810,60 +71826,60 @@
                 "texture",
                 "traffic loading"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "679.5",
+            "landingPage": "https://data.transportation.gov/d/n2bg-y3i6",
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
-            "title": "Long-Term Pavement Performance (LTPP) - Search",
-            "isPartOf": "DOT-679",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/research/tfhrc/programs/infrastructure/pavements/ltpp/",
-            "programCode": [
-                "021:009"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://infopave.fhwa.dot.gov/%3FGoto=Search",
-                    "description": "This access point provides access to the LTPP InfoPave search features including contextual full-text, sections, data, library, and ancillary data search.",
-                    "@type": "dcat:Distribution",
-                    "title": "Search"
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
+            "title": "Long-Term Pavement Performance (LTPP) - Search"
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
-            "landingPage": "https://data.transportation.gov/d/n3r3-p7tn",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/bridge/nbi/ascii.cfm%3Fyear=1994",
+                    "mediaType": "application/zip",
+                    "title": "1994"
+                }
             ],
+            "identifier": "693.3",
+            "isPartOf": "DOT-693",
+            "issued": "1992-12-31",
             "keyword": [
                 "bridge",
                 "condition",
@@ -71871,80 +71887,49 @@
                 "inspection",
                 "structure"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "693.3",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "The NBI System is the collection of bridge inspection information and costs associated with bridge replacements of structurally deficient bridges on and off the NHS. This data is collected under the auspices of the National Bridge Inspection Standards (NBIS) as prescribed by law. The NBI System collects the information that is used to determine eligibility for NHS projects, performance measure reporting, NHS penalty determination, and reporting to Congress.  It supports oversight of the NBIS through various report tools, and provides data reporting that supports agency strategic goals.",
-            "title": "National Bridge Inventory System (NBI) - 1994",
-            "isPartOf": "DOT-693",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
+            "landingPage": "https://data.transportation.gov/d/n3r3-p7tn",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-1575",
             "primaryITInvestmentUII": "021-012940226",
             "programCode": [
                 "021:009"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/bridge/nbi/ascii.cfm%3Fyear=1994",
-                    "mediaType": "application/zip",
-                    "title": "1994"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
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
+            "title": "National Bridge Inventory System (NBI) - 1994"
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
-            "landingPage": "https://data.transportation.gov/d/n46a-mfgy",
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
-            "identifier": "99.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": false,
             "description": "Data collected through FMCSA's Licensing and Insurance programs and information collections (BOC-3, OP-1, etc).",
-            "title": "Licensing and Insurance - Licensing and Insurance",
-            "isPartOf": "DOT-99",
-            "agencyProgramURL": "http://li-public.fmcsa.dot.gov/",
-            "primaryITInvestmentUII": "021-000001001",
-            "programCode": [
-                "021:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -71953,49 +71938,47 @@
                     "title": "Licensing and Insurance"
                 }
             ],
-            "spatial": "Carrier, Driver",
-            "dataQuality": false,
+            "identifier": "99.2",
+            "isPartOf": "DOT-99",
+            "issued": "2018-12-17",
+            "keyword": [
+                "driver insurance; carrier registration; carrier license"
+            ],
+            "landingPage": "https://data.transportation.gov/d/n46a-mfgy",
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
+            "title": "Licensing and Insurance - Licensing and Insurance"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/n4xv-8upm",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-09-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-30",
-            "keyword": [
-                "commodity",
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
-            "identifier": "https://data.transportation.gov/api/views/n4xv-8upm",
             "description": "Source: U.S. Department of Transportation, Bureau of Transportation Statistics, based upon U.S. Department of Commerce, U.S. Census Bureau, Foreign Trade Division, USA Trade Online \"HS Port-level Data\", available at https://usatrade.census.gov/ as of Sept 2024.",
-            "title": "Top 10 Containerized Import Commodities by Value and Coast 2023",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72003,54 +71986,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/n4xv-8upm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/n4xv-8upm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/n4xv-8upm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/n4xv-8upm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/n4xv-8upm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/n4xv-8upm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/n4xv-8upm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/n4xv-8upm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/n4xv-8upm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/n4xv-8upm",
+            "issued": "2024-09-30",
+            "keyword": [
+                "commodity",
+                "imports",
+                "ports"
+            ],
+            "landingPage": "https://data.transportation.gov/d/n4xv-8upm",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-09-30",
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
+            "title": "Top 10 Containerized Import Commodities by Value and Coast 2023"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/n6n3-vpjj",
-            "issued": "2024-12-22",
             "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO Office",
                 "hasEmail": "mailto:FMCSA.CDO@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/n6n3-vpjj",
             "description": "The FMCSA Safety Measurement System (SMS) data, consists of summary results of all active Interstate and Intrastate Hazmat Motor\nCarriers of passengers only. File is comma delimited.",
-            "title": "SMS EXTRACT INTER PASS",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72058,43 +72048,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/n6n3-vpjj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/n6n3-vpjj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/n6n3-vpjj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/n6n3-vpjj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/n6n3-vpjj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/n6n3-vpjj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/n6n3-vpjj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/n6n3-vpjj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/n6n3-vpjj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/n6n3-vpjj",
+            "issued": "2024-12-22",
+            "landingPage": "https://data.transportation.gov/d/n6n3-vpjj",
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
+            "title": "SMS EXTRACT INTER PASS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/n729-bvxb",
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
+                    "description": "2012 Nebraska HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/nebraska20913.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Nebraska"
+                }
+            ],
+            "identifier": "678.81",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -72108,60 +72126,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.81",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Nebraska",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/n729-bvxb",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/nebraska20913.zip",
-                    "description": "2012 Nebraska HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Nebraska"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Nebraska"
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
-            "landingPage": "https://data.transportation.gov/d/n7ac-p5xk",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/03jantvt/tvtjan03.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "January 2003"
+                }
             ],
+            "identifier": "18.140",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -72171,125 +72186,125 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.140",
+            "landingPage": "https://data.transportation.gov/d/n7ac-p5xk",
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
-            "title": "Monthly Traffic Volume Trends - January 2003",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/03jantvt/tvtjan03.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "January 2003"
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
+            "title": "Monthly Traffic Volume Trends - January 2003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:36"
             ],
-            "landingPage": "https://data.transportation.gov/d/n7zv-h2cx",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NTD Program Support",
+                "hasEmail": "mailto:NTDHelp@dot.gov"
+            },
+            "description": "A national summary of employees based on data reported by transit agencies to the National Transit Database (NTD) in Report Year 2022.\r\n\r\nNTD Data Summaries organize and summarize data from the 2022 National Transit Database in a manner that is more useful for quick reference and summary analysis. \r\n\r\nThis summary is based on the 2022 Employees file on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
+            "identifier": "https://data.transportation.gov/api/views/n7zv-h2cx",
             "issued": "2023-09-11",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-10",
             "keyword": [
                 "transit employees",
                 "transit salaries",
                 "transit wage rates"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NTD Program Support",
-                "hasEmail": "mailto:NTDHelp@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/n7zv-h2cx",
+            "modified": "2024-09-10",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Transit Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/n7zv-h2cx",
-            "description": "A national summary of employees based on data reported by transit agencies to the National Transit Database (NTD) in Report Year 2022.\r\n\r\nNTD Data Summaries organize and summarize data from the 2022 National Transit Database in a manner that is more useful for quick reference and summary analysis. \r\n\r\nThis summary is based on the 2022 Employees file on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
-            "title": "2022 NTD Annual Data Summary - Employees",
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "2022 NTD Annual Data Summary - Employees"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/n867-bmag",
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
-            "identifier": "https://data.transportation.gov/api/views/n867-bmag",
             "description": "Heavy trucks include trucks with more than 14,000 pounds gross vehicle weight. Prior to the 2003 Benchmark Revision heavy trucks were more than 10,000 pounds. The U.S. Bureau of Economic Analysis releases auto and truck sales data, which are used in the preparation of estimates of personal consumption expenditures.",
-            "title": "Heavy Truck Sales Seasonally Adjusted Annual Rate (SAAR)",
+            "identifier": "https://data.transportation.gov/api/views/n867-bmag",
+            "issued": "2025-01-02",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/n867-bmag",
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
+            "title": "Heavy Truck Sales Seasonally Adjusted Annual Rate (SAAR)"
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
-            "landingPage": "https://data.transportation.gov/d/n8gc-wpg2",
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
+                    "downloadURL": "https://cms.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/docs/closedByEnforcement_FY2012_04-26-2013.xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Fiscal Year 2012"
+                }
             ],
+            "identifier": "96.8",
+            "isPartOf": "DOT-96",
+            "issued": "2018-12-17",
             "keyword": [
                 "bus",
                 "civil penalties",
@@ -72302,131 +72317,131 @@
                 "motor carrier",
                 "truck"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "96.8",
+            "landingPage": "https://data.transportation.gov/d/n8gc-wpg2",
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
-            "title": "Closed Enforcement Cases - Fiscal Year 2012",
-            "isPartOf": "DOT-96",
-            "agencyProgramURL": "http://www.fmcsa.dot.gov/regulations/enforcement/civil-penalties",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://cms.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/docs/closedByEnforcement_FY2012_04-26-2013.xlsx",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "Fiscal Year 2012"
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
+            "title": "Closed Enforcement Cases - Fiscal Year 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/n8yb-nfqs",
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
-            "identifier": "https://data.transportation.gov/api/views/n8yb-nfqs",
             "description": "Passengers transported on Amtrak and Alaska Railroad operations. The Federal Railroad Administration collects accident/incident and operational data from railroads. Tourist and commuter railroad are excluded.",
-            "title": "Intercity Passenger Rail Travel - Passengers",
+            "identifier": "https://data.transportation.gov/api/views/n8yb-nfqs",
+            "issued": "2025-01-03",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/n8yb-nfqs",
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
+            "title": "Intercity Passenger Rail Travel - Passengers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/nad9-43zf",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Economic concepts related to transportation as an economic indicator.",
+            "identifier": "https://data.transportation.gov/api/views/nad9-43zf",
             "issued": "2020-02-24",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
             "keyword": [
                 "economic indicators",
                 "transportation",
                 "transportation services index",
                 "tsi"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/nad9-43zf",
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
-            "identifier": "https://data.transportation.gov/api/views/nad9-43zf",
-            "description": "Economic concepts related to transportation as an economic indicator.",
-            "title": "Transportation Economic Concepts: Transportation as an Economic Indicator",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Transportation Economic Concepts: Transportation as an Economic Indicator"
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
-            "landingPage": "https://data.transportation.gov/d/nakk-yyk5",
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
+                    "downloadURL": "http://www.fra.dot.gov/eLib/Details/L04105",
+                    "mediaType": "text/csv",
+                    "title": "Dispatcher Background Survey"
+                }
             ],
+            "identifier": "DOT-283",
+            "issued": "2008-03-01",
             "keyword": [
                 "alertness",
                 "employee",
@@ -72437,73 +72452,42 @@
                 "sleep",
                 "work"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "DOT-283",
+            "landingPage": "https://data.transportation.gov/d/nakk-yyk5",
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
-            "title": "Work Schedules and Sleep Patterns of Railroad Employees",
-            "agencyProgramURL": "http://www.fra.dot.gov/Page/P0068",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fra.dot.gov/eLib/Details/L04105",
-                    "mediaType": "text/csv",
-                    "title": "Dispatcher Background Survey"
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
+            "title": "Work Schedules and Sleep Patterns of Railroad Employees"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/navd-gpqa",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-12-09",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
-            "keyword": [
-                "aff"
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
-            "identifier": "https://data.transportation.gov/api/views/navd-gpqa",
             "description": "",
-            "title": "AFF - P12a - Fuel Cost by Carrier Group",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72511,68 +72495,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/navd-gpqa/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/navd-gpqa/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/navd-gpqa/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/navd-gpqa/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/navd-gpqa/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/navd-gpqa/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/navd-gpqa/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/navd-gpqa/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/navd-gpqa/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/navd-gpqa",
+            "issued": "2024-12-09",
+            "keyword": [
+                "aff"
+            ],
+            "landingPage": "https://data.transportation.gov/d/navd-gpqa",
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
+            "title": "AFF - P12a - Fuel Cost by Carrier Group"
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
-            "landingPage": "https://data.transportation.gov/d/naz3-8itw",
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
-            "identifier": "692.40",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - Total Pollutants by County",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "primaryITInvestmentUII": "021-845083703",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72581,55 +72562,54 @@
                     "title": "Total Pollutants by County"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.40",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/naz3-8itw",
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
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - Total Pollutants by County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "The data set contains controlled unclassified procurement information, confidential business information, and information protected by statute or regulation.",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/nbds-ggt9",
-            "issued": "2014-12-29",
-            "temporal": "R/2014-12-29/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "document approval",
-                "line of accounting",
-                "purchase order",
-                "receiving",
-                "suppliers"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "739.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
             "description": "Delphi purchasing module contains the following data elements, but is not limited to purchase order document ID, suppliers, receiving, line of accounting, and document approval history.",
-            "title": "Delphi Purchasing Module -",
-            "primaryITInvestmentUII": "021-105731835",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72637,57 +72617,57 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "theme": [
-                "Transportation"
+            "identifier": "739.0",
+            "issued": "2014-12-29",
+            "keyword": [
+                "document approval",
+                "line of accounting",
+                "purchase order",
+                "receiving",
+                "suppliers"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/nbds-ggt9",
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
+            "title": "Delphi Purchasing Module -"
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
-            "landingPage": "https://data.transportation.gov/d/nc3v-xpzg",
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
-            "identifier": "693.8",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
             "description": "The NBI System is the collection of bridge inspection information and costs associated with bridge replacements of structurally deficient bridges on and off the NHS. This data is collected under the auspices of the National Bridge Inspection Standards (NBIS) as prescribed by law. The NBI System collects the information that is used to determine eligibility for NHS projects, performance measure reporting, NHS penalty determination, and reporting to Congress.  It supports oversight of the NBIS through various report tools, and provides data reporting that supports agency strategic goals.",
-            "title": "National Bridge Inventory System (NBI) - 1999",
-            "isPartOf": "DOT-693",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
-            "primaryITInvestmentUII": "021-012940226",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72696,90 +72676,94 @@
                     "title": "1999"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
-            "dataQuality": true,
+            "identifier": "693.8",
+            "isPartOf": "DOT-693",
+            "issued": "1992-12-31",
+            "keyword": [
+                "bridge",
+                "condition",
+                "deck",
+                "inspection",
+                "structure"
+            ],
+            "landingPage": "https://data.transportation.gov/d/nc3v-xpzg",
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
+            "title": "National Bridge Inventory System (NBI) - 1999"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/nc6g-has7",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2024-06-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
-            "keyword": [
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "nhtsa"
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
-            "identifier": "https://data.transportation.gov/api/views/nc6g-has7",
             "description": "The Vulnerable road user In-depth Crash Investigation Study collected detailed pedestrian crash data for 87 crashes involving pedestrians in 2022. Skilled teams identified crashes at four sites across the United States and conducted inspections of scenes and involved vehicles. Pedestrian medical records were reviewed to document injuries. Engineers reviewed crash and injury data to establish pedestrian kinematic trajectories and injury causation scenarios, as well as crash avoidance assessments. Case data are available in a browser-based viewer which includes coded data elements, crash scene diagrams, and images of the crash scene and involved vehicle.",
-            "title": "Vulnerable Road User In-Depth Crash Investigation Study",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://crashviewer.nhtsa.dot.gov/CIREN/SearchIndex?study=CIRENVICIS&SearchType=CIRENVICIS",
-                    "description": "Case data are available in a browser-based viewer which includes coded data elements, crash scene diagrams, and images of the crash scene and involved vehicle. Attached to this dataset is a csv file as a supplemental source for end users \u2013 it will allow for tabular view of key data elements from the crash viewer.",
                     "@type": "dcat:Distribution",
+                    "description": "Case data are available in a browser-based viewer which includes coded data elements, crash scene diagrams, and images of the crash scene and involved vehicle. Attached to this dataset is a csv file as a supplemental source for end users \u2013 it will allow for tabular view of key data elements from the crash viewer.",
+                    "downloadURL": "https://crashviewer.nhtsa.dot.gov/CIREN/SearchIndex?study=CIRENVICIS&SearchType=CIRENVICIS",
+                    "mediaType": "text/html",
                     "title": "Vulnerable road user In-depth Crash Investigation Study Crash Viewer"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/nc6g-has7",
+            "issued": "2024-06-28",
+            "keyword": [
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "nhtsa"
+            ],
+            "landingPage": "https://data.transportation.gov/d/nc6g-has7",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-07",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
             "theme": [
                 "Automobiles"
-            ]
+            ],
+            "title": "Vulnerable Road User In-Depth Crash Investigation Study"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2024-05-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-07",
-            "keyword": [
-                "speed data",
-                "speed trends"
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
-            "identifier": "https://data.transportation.gov/api/views/ncrx-4ncc",
+            "dataQuality": true,
             "description": "This data set is to hold some SBIR Documents to be released.",
-            "title": "SBIR Documents",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72787,74 +72771,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ncrx-4ncc/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ncrx-4ncc/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ncrx-4ncc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ncrx-4ncc/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ncrx-4ncc/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ncrx-4ncc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ncrx-4ncc/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ncrx-4ncc/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ncrx-4ncc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/ncrx-4ncc",
+            "issued": "2024-05-30",
+            "keyword": [
+                "speed data",
+                "speed trends"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-06-07",
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
+            "title": "SBIR Documents"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.nhtsa.gov/Laws+&+Regulations/Guidance+Documents",
+            "agencyProgramURL": "http://www.nhtsa.gov/Laws+&+Regulations/Guidance+Documents",
+            "analysisUnit": "Regulations",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/ndu9-g4hs",
-            "issued": "2011-01-18",
-            "temporal": "R/2006-01-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.nhtsa.gov/Laws+&+Regulations/Guidance+Documents"
-            ],
-            "keyword": [
-                "data.gov",
-                "law",
-                "significant guidance",
-                "transportation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "319.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "A list of Significant Guidance documents, which include guidance document disseminated to regulated entities or the general public that may reasonably be anticipated to lead to an annual effect on the economy of $100 million or more or adversely affect in a material way the economy, a sector of the economy, productivity, competition, jobs, the environment, public health or safety, or State, local, or tribal governments or communities; create a serious inconsistency or otherwise interfere with an action taken or planned by another agency; materially alter the budgetary impact of entitlements, grants, user fees, or loan programs or the rights and obligations of recipients thereof; or raise novel legal or policy issues arising out of legal mandates, the President's priorities, or the principles set forth in Executive Order 12866, as further amended.",
-            "title": "Significant Guidance Issued by the National Highway Traffic Safety Administration -",
-            "isPartOf": "DOT-319",
-            "agencyProgramURL": "http://www.nhtsa.gov/Laws+&+Regulations/Guidance+Documents",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72862,34 +72843,67 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "319.1",
+            "isPartOf": "DOT-319",
+            "issued": "2011-01-18",
+            "keyword": [
+                "data.gov",
+                "law",
+                "significant guidance",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ndu9-g4hs",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.nhtsa.gov/Laws+&+Regulations/Guidance+Documents",
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
+                "http://www.nhtsa.gov/Laws+&+Regulations/Guidance+Documents"
+            ],
+            "temporal": "R/2006-01-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "analysisUnit": "Regulations",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4308",
-            "language": [
-                "en-US"
-            ]
+            "title": "Significant Guidance Issued by the National Highway Traffic Safety Administration -"
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
-            "landingPage": "https://data.transportation.gov/d/ndz8-z44c",
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
+            "identifier": "DOT-116",
+            "issued": "2018-12-17",
             "keyword": [
                 "bus",
                 "federal motor carrier safety administration",
@@ -72907,73 +72921,43 @@
                 "sms",
                 "vehicles"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "DOT-116",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
-            "description": "This Web site is designed to inform passenger carriers and the traveling public about the Federal Motor Carrier Safety Administration's passenger carrier program and regulations.",
-            "title": "A&I - Bus/Passenger Carrier Information",
-            "agencyProgramURL": "http://www.fmcsa.dot.gov/safety-security/pcs/Index.aspx",
-            "primaryITInvestmentUII": "021-000001010",
-            "programCode": [
-                "021:022"
+            "landingPage": "https://data.transportation.gov/d/ndz8-z44c",
+            "language": [
+                "en-US"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fmcsa.dot.gov/safety-security/PCS/Consumers.aspx",
-                    "mediaType": "text/html",
-                    "title": "Data Mining Tool"
-                }
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-24",
+            "phone": "202-366-2161",
+            "primaryITInvestmentUII": "021-000001010",
+            "programCode": [
+                "021:022"
+            ],
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
+            "title": "A&I - Bus/Passenger Carrier Information"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://data.transportation.gov/d/neuq-kfdt",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2021-08-25",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-20",
-            "keyword": [
-                "pocket guide to transportation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:https://transportation.libanswers.com/form.php "
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/neuq-kfdt",
             "description": "",
-            "title": "Pocket Guide to Transportation",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -72981,66 +72965,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/neuq-kfdt/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/neuq-kfdt/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/neuq-kfdt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/neuq-kfdt/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/neuq-kfdt/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/neuq-kfdt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/neuq-kfdt/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/neuq-kfdt/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/neuq-kfdt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "https://data.transportation.gov/api/views/neuq-kfdt",
+            "issued": "2021-08-25",
+            "keyword": [
+                "pocket guide to transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/neuq-kfdt",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2022-09-20",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Pocket Guide to Transportation"
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
-            "landingPage": "https://data.transportation.gov/d/ney2-64e6",
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
-            "identifier": "276.2",
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
@@ -73048,35 +73029,69 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "276.2",
+            "isPartOf": "DOT-276",
+            "issued": "2011-01-18",
+            "keyword": [
+                "data.gov",
+                "law",
+                "significant guidance",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ney2-64e6",
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
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/SafetyProgram/Review.aspx",
+            "agencyProgramURL": "https://www.fmcsa.dot.gov/safety/new-entrant-safety-assurance-program, https://ai.fmcsa.dot.gov/Grants/MCSAP.aspx",
+            "analysisUnit": "Motor Carrier",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/nfap-4mdw",
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
+            "identifier": "95.2",
+            "isPartOf": "DOT-95",
+            "issued": "2018-12-17",
             "keyword": [
                 "bus",
                 "compliance reviews",
@@ -73095,70 +73110,42 @@
                 "safety audits",
                 "safety rating"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "95.2",
+            "landingPage": "https://data.transportation.gov/d/nfap-4mdw",
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
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/nfsh-p62e",
-            "issued": "2024-01-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-10",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "TBD",
                 "hasEmail": "mailto:sean.jahanmir@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/nfsh-p62e",
             "description": "",
-            "title": "Monthly Average Container Vessel Dwell Times at the Top 25 U.S. Container Ports January 2019 to June 2023",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73166,65 +73153,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/nfsh-p62e/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/nfsh-p62e/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/nfsh-p62e/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/nfsh-p62e/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/nfsh-p62e/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/nfsh-p62e/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/nfsh-p62e/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/nfsh-p62e/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/nfsh-p62e/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "https://data.transportation.gov/api/views/nfsh-p62e",
+            "issued": "2024-01-10",
+            "landingPage": "https://data.transportation.gov/d/nfsh-p62e",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-01-10",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Monthly Average Container Vessel Dwell Times at the Top 25 U.S. Container Ports January 2019 to June 2023"
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
-            "landingPage": "https://data.transportation.gov/d/ngf2-c829",
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
-            "identifier": "364.6",
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
@@ -73233,51 +73215,51 @@
                     "title": "Vehicle Test Query by Vehicle Barrier Parameters"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.6",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ngf2-c829",
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
-            "landingPage": "https://data.transportation.gov/d/ngjm-b5rq",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-10-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-01",
-            "keyword": [
-                "commodity",
-                "container",
-                "containers",
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
-            "identifier": "https://data.transportation.gov/api/views/ngjm-b5rq",
             "description": "Source: U.S. Department of Transportation, Bureau of Transportation Statistics, based upon U.S. Department of Commerce, U.S. Census Bureau, Foreign Trade Division, USA Trade Online, \"HS Port-level Data\", available at https://usatrade.census.gov/ as of Sept 2024.",
-            "title": "Containerized Imports' Value and Weight by Port in 2023",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73285,50 +73267,83 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ngjm-b5rq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ngjm-b5rq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ngjm-b5rq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ngjm-b5rq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ngjm-b5rq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ngjm-b5rq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ngjm-b5rq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ngjm-b5rq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ngjm-b5rq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/ngjm-b5rq",
+            "issued": "2024-10-01",
+            "keyword": [
+                "commodity",
+                "container",
+                "containers",
+                "ports"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ngjm-b5rq",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-10-01",
+            "programCode": [
+                "021:042"
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
+            "title": "Containerized Imports' Value and Weight by Port in 2023"
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
-            "landingPage": "https://data.transportation.gov/d/ngki-jsft",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/13jultvt/13jultvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "July 2013"
+                }
             ],
+            "identifier": "18.52",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -73338,82 +73353,49 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.52",
+            "landingPage": "https://data.transportation.gov/d/ngki-jsft",
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
-            "title": "Monthly Traffic Volume Trends - July 2013",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/13jultvt/13jultvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "July 2013"
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
+            "title": "Monthly Traffic Volume Trends - July 2013"
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
-            "landingPage": "https://data.transportation.gov/d/ngpj-zen5",
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
-            "identifier": "364.2",
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
@@ -73422,32 +73404,68 @@
                     "title": "Vehicle Test Query by Vehicle Test Parameters"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.2",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ngpj-zen5",
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
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/nhd6-vqyx",
+            "categoryDesignation": "Administrative",
+            "collectionInstrument": "Transportation",
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
+                    "description": "2012 Vermont HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/vermont2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Vermont"
+                }
+            ],
+            "identifier": "678.99",
+            "isPartOf": "DOT-678",
             "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
-            "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
             "keyword": [
                 "aadt",
                 "condition",
@@ -73461,60 +73479,56 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.99",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Vermont",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/nhd6-vqyx",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/vermont2012.zip",
-                    "description": "2012 Vermont HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Vermont"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Vermont"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.fra.dot.gov/eLib/Find#p1_z5_gD_lEA",
+            "agencyProgramURL": "http://www.fra.dot.gov/eLib/Find#p1_z5_gD_lEA",
             "bureauCode": [
                 "021:27"
             ],
-            "landingPage": "https://data.transportation.gov/d/nhei-divn",
-            "issued": "2010-09-29",
-            "temporal": "R/2003-10-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-09",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.fra.dot.gov/eLib/Find#p1_z5_gD_lEA"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Summary of civil penalties incurred by railroads as a result of FRA action during the previous year.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fra.dot.gov/eLib/Find#p1_z5_gD_lEA",
+                    "mediaType": "text/html",
+                    "title": "Search Reports"
+                }
             ],
+            "identifier": "256.2",
+            "isPartOf": "DOT-256",
+            "issued": "2010-09-29",
             "keyword": [
                 "annual",
                 "audits",
@@ -73525,85 +73539,50 @@
                 "inspection",
                 "railroad safety violations"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "256.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Railroad Administration"
-            },
-            "description": "Summary of civil penalties incurred by railroads as a result of FRA action during the previous year.",
-            "title": "Annual Civil Penalty Report - Search Reports",
-            "isPartOf": "DOT-256",
-            "agencyProgramURL": "http://www.fra.dot.gov/eLib/Find#p1_z5_gD_lEA",
+            "landingPage": "https://data.transportation.gov/d/nhei-divn",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-10-09",
+            "phone": "202-493-6036",
             "primaryITInvestmentUII": "021-863675665",
             "programCode": [
                 "021:036"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fra.dot.gov/eLib/Find#p1_z5_gD_lEA",
-                    "mediaType": "text/html",
-                    "title": "Search Reports"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Railroad Administration"
+            },
+            "references": [
+                "http://www.fra.dot.gov/eLib/Find#p1_z5_gD_lEA"
             ],
             "spatial": "National",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.fra.dot.gov/eLib/Find#p1_z5_gD_lEA",
+            "temporal": "R/2003-10-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "phone": "202-493-6036",
-            "language": [
-                "en-US"
-            ]
+            "title": "Annual Civil Penalty Report - Search Reports"
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
-            "landingPage": "https://data.transportation.gov/d/nhet-w2n3",
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
-            "identifier": "524.12",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
             "description": "STATE DATA REPORTING SYSTEMS. Annual reports on the Fatality Analysis Reporting System (FARS) which is data regarding fatalities that is collected by a FARS analyst from each State and provided to NHTSA.",
-            "title": "GES Reports - 2010",
-            "isPartOf": "DOT-524",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73612,35 +73591,72 @@
                     "title": "2010"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
-            "dataQuality": true,
+            "identifier": "524.12",
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
+            "landingPage": "https://data.transportation.gov/d/nhet-w2n3",
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
+            "title": "GES Reports - 2010"
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
-            "landingPage": "https://data.transportation.gov/d/nhkj-aj8m",
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
+            "identifier": "288.6",
+            "isPartOf": "DOT-288",
+            "issued": "2009-01-27",
             "keyword": [
                 "crash",
                 "death",
@@ -73656,76 +73672,43 @@
                 "vehicle",
                 "victim"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "288.6",
+            "landingPage": "https://data.transportation.gov/d/nhkj-aj8m",
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
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/nhvr-exvq",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2018-10-24",
-            "@type": "dcat:Dataset",
-            "modified": "2018-10-10",
-            "keyword": [
-                "data element",
-                "functional classification",
-                "highway sub-domain"
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
-            "identifier": "https://data.transportation.gov/api/views/nhvr-exvq",
+            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=DED",
             "description": "This is list of data elements and their attributes that are used by data assets at the Federal Highway Administration.",
-            "title": "Highway Data Element Dictionary",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73733,102 +73716,98 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/nhvr-exvq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/nhvr-exvq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/nhvr-exvq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/nhvr-exvq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/nhvr-exvq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/nhvr-exvq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/nhvr-exvq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/nhvr-exvq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/nhvr-exvq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=DED",
+            "identifier": "https://data.transportation.gov/api/views/nhvr-exvq",
+            "issued": "2018-10-24",
+            "keyword": [
+                "data element",
+                "functional classification",
+                "highway sub-domain"
+            ],
+            "landingPage": "https://data.transportation.gov/d/nhvr-exvq",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2018-10-10",
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
+            "title": "Highway Data Element Dictionary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ni8u-e22d",
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
-            "identifier": "https://data.transportation.gov/api/views/ni8u-e22d",
             "description": "A monthly measure of the volume of services performed by the for-hire transportation sector. The index covers the activities of for-hire freight carriers and for-hire passenger carriers.",
-            "title": "Transportation Services Index - Combined",
+            "identifier": "https://data.transportation.gov/api/views/ni8u-e22d",
+            "issued": "2025-01-02",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ni8u-e22d",
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
+            "title": "Transportation Services Index - Combined"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "accrualPeriodicity": "Monthly",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2019-01-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "12-month moving average",
-                "cumulative vmt",
-                "month",
-                "seasonally adjusted vmt",
-                "vehicle miles traveled",
-                "vmt",
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
-            "identifier": "https://data.transportation.gov/api/views/niaw-6xw6",
+            "dataQuality": true,
             "description": "Summary monthly traffic volume trends.",
-            "title": "Monthly Travel Trends - National",
-            "isPartOf": "Traffic Volume Trends",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73836,66 +73815,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/niaw-6xw6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/niaw-6xw6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/niaw-6xw6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/niaw-6xw6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/niaw-6xw6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/niaw-6xw6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/niaw-6xw6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/niaw-6xw6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/niaw-6xw6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/niaw-6xw6",
+            "isPartOf": "Traffic Volume Trends",
+            "issued": "2019-01-08",
+            "keyword": [
+                "12-month moving average",
+                "cumulative vmt",
+                "month",
+                "seasonally adjusted vmt",
+                "vehicle miles traveled",
+                "vmt",
+                "year"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "language": [
+                "English"
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
             "spatial": "National",
             "systemOfRecords": "Travel Monitoring Analysis System (TMAS)",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Monthly",
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Monthly Travel Trends - National"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/nimp-626k",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-09-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
-            "keyword": [
-                "buses",
-                "trains",
-                "transit vehicles",
-                "vehicle counts"
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
-            "identifier": "https://data.transportation.gov/api/views/nimp-626k",
             "description": "This dataset details vehicle types and ages for transit agencies reporting to the National Transit Database in the 2022 and 2023 report years. Vehicle types describe the vehicles employed in direct operation or support of transit service. \n\nNTD Data Tables organize and summarize data from the 2022 and 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. This dataset is based on the 2022 and 2023 Revenue Vehicle Inventory and Service Vehicle Inventory database files.\n\nRural reporters that operate in more than one state report their vehicles in only one of their states.\n\nIn years 2015-2021, you can find this data in the \"Vehicles\" data table on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.\n\nIf you have any other questions about this table, please contact the NTD Help Desk at NTDHelp@dot.gov.",
-            "title": "2022 - 2023 NTD Annual Data - Vehicles (Type Count by Agency)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -73903,76 +73887,96 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/nimp-626k/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/nimp-626k/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/nimp-626k/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/nimp-626k/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/nimp-626k/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/nimp-626k/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/nimp-626k/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/nimp-626k/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/nimp-626k/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/nimp-626k",
+            "issued": "2024-09-06",
+            "keyword": [
+                "buses",
+                "trains",
+                "transit vehicles",
+                "vehicle counts"
+            ],
+            "landingPage": "https://data.transportation.gov/d/nimp-626k",
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
+            "title": "2022 - 2023 NTD Annual Data - Vehicles (Type Count by Agency)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/nixb-9brz",
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
-            "identifier": "https://data.transportation.gov/api/views/nixb-9brz",
             "description": "National Highway Traffic Safety Administration releases data on highway fatalities in the Fatality Analysis Reporting System (FARS). Data for the most recent year are preliminary estimates.",
-            "title": "Highway Fatalities",
+            "identifier": "https://data.transportation.gov/api/views/nixb-9brz",
+            "issued": "2025-01-29",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/nixb-9brz",
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
+            "title": "Highway Fatalities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/nj8g-qpm9",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Theresa Firestine",
+                "hasEmail": "mailto:theresa.firestine@dot.gov"
+            },
+            "description": "Page describes the U.S. Department of Transportation, Bureau of Transportation Statistics' Local Area Transportation Data offerings.",
+            "identifier": "https://data.transportation.gov/api/views/nj8g-qpm9",
             "issued": "2020-12-15",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-09",
             "keyword": [
                 "accessibility",
                 "bikeshare",
@@ -73987,58 +73991,34 @@
                 "transit",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Theresa Firestine",
-                "hasEmail": "mailto:theresa.firestine@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/nj8g-qpm9",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-01-09",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/nj8g-qpm9",
-            "description": "Page describes the U.S. Department of Transportation, Bureau of Transportation Statistics' Local Area Transportation Data offerings.",
-            "title": "Local Area Transportation Data for TRB",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Local Area Transportation Data for TRB"
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
-            "identifier": "https://data.transportation.gov/api/views/nk63-g3hx",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 1989",
-            "title": "Historic HPMS Data (Sample) - 1989",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74046,75 +74026,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/nk63-g3hx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/nk63-g3hx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/nk63-g3hx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/nk63-g3hx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/nk63-g3hx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/nk63-g3hx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/nk63-g3hx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/nk63-g3hx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/nk63-g3hx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/nk63-g3hx",
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
+            "title": "Historic HPMS Data (Sample) - 1989"
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
-            "landingPage": "https://data.transportation.gov/d/nkba-7d82",
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
-            "identifier": "524.4",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
             "description": "STATE DATA REPORTING SYSTEMS. Annual reports on the Fatality Analysis Reporting System (FARS) which is data regarding fatalities that is collected by a FARS analyst from each State and provided to NHTSA.",
-            "title": "GES Reports - 2002",
-            "isPartOf": "DOT-524",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74123,56 +74102,57 @@
                     "title": "2002"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
-            "dataQuality": true,
+            "identifier": "524.4",
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
+            "landingPage": "https://data.transportation.gov/d/nkba-7d82",
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
+            "title": "GES Reports - 2002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Data set contains controlled unclassified information (Information technology systems security information), and potentially security sensitive information (SSI)",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/nkks-jmyk",
-            "issued": "2014-11-21",
-            "temporal": "R/2014-11-21/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "cybersecurity",
-                "incident response",
-                "metrics",
-                "transportation",
-                "vulnerability"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "1630.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
             "description": "This data set contains information about the Department of Transportation's cybersecurity incident response tickets, incident response metrics, incident response time, vulnerability data, and remediation recommendations broken down by OA. The CSMC owns maintains, collects, and operates this data as a service for the entire department.",
-            "title": "DOT JAS -",
-            "primaryITInvestmentUII": "021-325711125",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74180,60 +74160,50 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "theme": [
-                "Transportation"
+            "identifier": "1630.0",
+            "issued": "2014-11-21",
+            "keyword": [
+                "cybersecurity",
+                "incident response",
+                "metrics",
+                "transportation",
+                "vulnerability"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/nkks-jmyk",
             "language": [
                 "en-US"
             ],
-            "phone": "202-306-9933"
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-14",
+            "phone": "202-306-9933",
+            "primaryITInvestmentUII": "021-325711125",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "rights": "Data set contains controlled unclassified information (Information technology systems security information), and potentially security sensitive information (SSI)",
+            "temporal": "R/2014-11-21/P1Y",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "DOT JAS -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.tampacvpilot.com/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2019-03-05",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-19",
-            "references": [
-                "https://www.sae.org/standards/content/j2735_201603/",
-                "https://www.sae.org/standards/content/j2945/1_201603/"
-            ],
-            "keyword": [
-                "arterial",
-                "basic safety message (bsm)",
-                "connected vehicle message",
-                "connected vehicle pilot (cvp)",
-                "field test",
-                "florida",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "roadside equipment (rse)",
-                "tampa",
-                "tampa connected vehicle pilot deployment (tampa cv pilot)",
-                "tampa hillsborough expressway authority (thea)"
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
-            "identifier": "https://data.transportation.gov/api/views/nm7w-nvbm",
+            "dataQuality": true,
             "description": "The Tampa CV Pilot generates data from the interaction between vehicles and between vehicles and infrastructure. This dataset consists of Basic Safety Messages (BSMs) generated by participant and public transportation vehicles onboard units (OBU) and transmitted to road-side units (RSU) located throughout the Tampa CV Pilot Study area. The full set of raw, BSM data from Tampa CV Pilot can be found in the <a href=\"http://usdot-its-cvpilot-publicdata.s3.amazonaws.com/index.html\" target=\"_blank\" >ITS Sandbox</a>. The data fields follow SAE J2735 and J2945/1 standards and adopted units of measure. \n\nThis dataset holds a flattened sample of the BSM data from Tampa CV Pilot. An extra geo column (coreData_position) was added to this dataset to allow for mapping of the geocoded BSM data within Socrata, and a column of random numbers (randomNum) was added to allow for random sampling of data points within Socrata.",
-            "title": "Tampa CV Pilot Basic Safety Message (BSM) Sample",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74241,106 +74211,117 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/nm7w-nvbm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/nm7w-nvbm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/nm7w-nvbm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/nm7w-nvbm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/nm7w-nvbm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/nm7w-nvbm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/nm7w-nvbm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/nm7w-nvbm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/nm7w-nvbm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Tampa, Florida",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/nm7w-nvbm",
+            "issued": "2019-03-05",
+            "keyword": [
+                "arterial",
+                "basic safety message (bsm)",
+                "connected vehicle message",
+                "connected vehicle pilot (cvp)",
+                "field test",
+                "florida",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "roadside equipment (rse)",
+                "tampa",
+                "tampa connected vehicle pilot deployment (tampa cv pilot)",
+                "tampa hillsborough expressway authority (thea)"
+            ],
+            "landingPage": "https://www.tampacvpilot.com/",
+            "language": [
+                "English"
+            ],
             "license": "http://creativecommons.org/licenses/by-sa/4.0/legalcode",
+            "modified": "2021-03-19",
+            "programCode": [
+                "021:013"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "USDOT"
+            },
+            "references": [
+                "https://www.sae.org/standards/content/j2735_201603/",
+                "https://www.sae.org/standards/content/j2945/1_201603/"
+            ],
+            "spatial": "Tampa, Florida",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "Tampa CV Pilot Basic Safety Message (BSM) Sample"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/nmfc-gh7h",
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
-            "identifier": "https://data.transportation.gov/api/views/nmfc-gh7h",
             "description": "The U.S. Census Bureau provides monthly estimates of the total dollar value of construction work done in the United States as part of the Value of Construction Put in Place Survey (VIP). Includes commercial parking lots and garages.",
-            "title": "State and Local Government Construction Spending - Parking Facilities",
+            "identifier": "https://data.transportation.gov/api/views/nmfc-gh7h",
+            "issued": "2025-01-03",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/nmfc-gh7h",
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
+            "title": "State and Local Government Construction Spending - Parking Facilities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Access restricted under the Privacy Act of 1974; SORN issued by OPM; see reference on DOT Privacy Act page www.dot.gov/privacy under Government-wide System of Records",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/nn2p-6uvm",
-            "issued": "2014-11-21",
-            "temporal": "R/2014-11-21/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-11-14",
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
-            "identifier": "1634.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
             "description": "This data set contains payroll and personnel data for current and past DOT employees.  This data is produced by the current HR and payroll provider (Department of Interior's IBC) with historical data also maintained in the dataset produced by DOT's CUPS, CPMIS and IPPS systems.  The data contains PII (Employee Name, SSN, Date of Birth, Home Address, Financial information, etc.), Civil Rights (Disability, Gender, Race) and other sensitive data (Background Investigations and Security Clearance).",
-            "title": "Personnel and Payroll Data (FPPS and associated systems FPPS Datamart, WebPrinting System) and eOPF - Workforce Statistics Archive",
-            "isPartOf": "DOT-1634",
-            "primaryITInvestmentUII": "021-999991221",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74349,32 +74330,66 @@
                     "title": "Workforce Statistics Archive"
                 }
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "theme": [
-                "Transportation"
+            "identifier": "1634.1",
+            "isPartOf": "DOT-1634",
+            "issued": "2014-11-21",
+            "keyword": [
+                "hr",
+                "payroll",
+                "personnel"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Administrative",
+            "landingPage": "https://data.transportation.gov/d/nn2p-6uvm",
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
+            "title": "Personnel and Payroll Data (FPPS and associated systems FPPS Datamart, WebPrinting System) and eOPF - Workforce Statistics Archive"
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
-            "landingPage": "https://data.transportation.gov/d/nn44-abcq",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12novtvt/12novtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "November 2012"
+                }
             ],
+            "identifier": "18.44",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -74384,90 +74399,88 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.44",
+            "landingPage": "https://data.transportation.gov/d/nn44-abcq",
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
-            "title": "Monthly Traffic Volume Trends - November 2012",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12novtvt/12novtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "November 2012"
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
+            "title": "Monthly Traffic Volume Trends - November 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/nnp9-e3f3",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2020-05-28",
-            "@type": "dcat:Dataset",
-            "modified": "2020-07-06",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Janine McFadden",
                 "hasEmail": "mailto:janine.mcfadden@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/nnp9-e3f3",
+            "describedBy": "2017-01-01/2017-12-31",
             "description": "Data tables and descriptions",
-            "title": "National Census of Ferry Operators (NCFO) 2018: National Ferry Database",
+            "identifier": "https://data.transportation.gov/api/views/nnp9-e3f3",
+            "issued": "2020-05-28",
+            "landingPage": "https://data.transportation.gov/d/nnp9-e3f3",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2020-07-06",
             "programCode": [
                 "021:042"
             ],
-            "describedBy": "2017-01-01/2017-12-31",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Ferry Transit"
-            ]
+            ],
+            "title": "National Census of Ferry Operators (NCFO) 2018: National Ferry Database"
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
-            "landingPage": "https://data.transportation.gov/d/nnty-zyft",
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
+            "identifier": "DOT-335",
+            "issued": "2007-10-01",
             "keyword": [
                 "amtrak stations",
                 "grade crossing",
@@ -74483,55 +74496,60 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "DOT-335",
+            "landingPage": "https://data.transportation.gov/d/nnty-zyft",
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
-            "title": "Federal Railroad Administration GIS Web Mapping Application",
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
-                "Transportation"
-            ],
-            "accrualPeriodicity": "R/P3M",
-            "analysisUnit": "National Railroad Network",
-            "categoryDesignation": "Geospatial",
-            "phone": "202-493-1343",
-            "language": [
-                "en-US"
-            ]
+                "Transportation"
+            ],
+            "title": "Federal Railroad Administration GIS Web Mapping Application"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/nqcu-3734",
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
+                    "description": "2013 North Carolina HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/northcarolina2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 North Carolina"
+                }
+            ],
+            "identifier": "678.137",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -74545,121 +74563,83 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.137",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 North Carolina",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/nqcu-3734",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/northcarolina2013.zip",
-                    "description": "2013 North Carolina HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 North Carolina"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 North Carolina"
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
+                "fn": "Debbie Phillips",
+                "hasEmail": "mailto:deborah.phillips@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Interactive dashboard and data assets that provide interested parties with access to the source data for the agency\u2019s longstanding Monthly Motor Fuel Report publication",
+            "identifier": "https://data.transportation.gov/api/views/nrec-wf7k",
             "issued": "2023-05-24",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-18",
             "keyword": [
                 "distribution",
                 "gasoline",
                 "volume"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Debbie Phillips",
-                "hasEmail": "mailto:deborah.phillips@dot.gov"
-            },
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-07-18",
+            "programCode": [
+                "021:009"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/nrec-wf7k",
-            "description": "Interactive dashboard and data assets that provide interested parties with access to the source data for the agency\u2019s longstanding Monthly Motor Fuel Report publication",
-            "title": "Monthly Motor Fuel Report",
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
+            "title": "Monthly Motor Fuel Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "DART processes reports on potential FOIA data, but only for internal and limited federal audiences.",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://ai.fmcsa.dot.gov/DART/",
+            "agencyProgramURL": "https://ai.fmcsa.dot.gov/DART/",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/nsfz-pmeu",
-            "issued": "2005-12-18",
-            "temporal": "R/2005-12-18/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "https://ai.fmcsa.dot.gov/DART/"
-            ],
-            "keyword": [
-                "carrier data",
-                "data quality",
-                "driver data",
-                "registration"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO",
                 "hasEmail": "mailto:fmcsa.cdo@dot.gov"
             },
-            "identifier": "105.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": true,
             "description": "The DART team is responsible for fulfilling ad hoc data requests that come in to the Analysis Division, FMCSA.  The DART system tracks these requests, stores any coding and results, and performs internal reporting about requests received.",
-            "title": "Data Analysis Reports Team (DART) -",
-            "agencyProgramURL": "https://ai.fmcsa.dot.gov/DART/",
-            "programCode": [
-                "021:019"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74667,59 +74647,53 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "Driver",
-            "dataQuality": true,
+            "identifier": "105.0",
+            "issued": "2005-12-18",
+            "keyword": [
+                "carrier data",
+                "data quality",
+                "driver data",
+                "registration"
+            ],
+            "landingPage": "https://data.transportation.gov/d/nsfz-pmeu",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "https://ai.fmcsa.dot.gov/DART/",
+            "modified": "2024-05-24",
+            "phone": "202-366-2161",
+            "programCode": [
+                "021:019"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "references": [
+                "https://ai.fmcsa.dot.gov/DART/"
+            ],
+            "rights": "DART processes reports on potential FOIA data, but only for internal and limited federal audiences.",
+            "spatial": "Driver",
+            "temporal": "R/2005-12-18/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "phone": "202-366-2161",
-            "language": [
-                "en-US"
-            ]
+            "title": "Data Analysis Reports Team (DART) -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ntts-pk3f",
+            "accrualPeriodicity": "R/PT0.1S",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2016-01-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2016-08-01/2016-08-01",
-            "modified": "2016-01-01",
-            "keyword": [
-                "basic safety message (bsm)",
-                "connected vehicle message",
-                "freeway",
-                "incident data",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "seattle",
-                "simulated data",
-                "trajectory conversion algorithm (tca)",
-                "vissim",
-                "washington",
-                "weather"
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
-            "identifier": "https://data.transportation.gov/api/views/ntts-pk3f",
+            "dataQuality": true,
             "description": "Data provided consists of Basic Safety Messages (BSM) generated by the Trajectory Converter Analysis (TCA) tool with input from VISSIM calibrated simulations of the I-405 corridor in Seattle, Washington. The Seattle I-405 data environment includes data for a variety of network operational conditions, market penetrations of connected vehicles and communication strategies along the I-405 travel corridor.\r\n\r\nThis legacy dataset was created before data.transportation.gov and is only currently available via the attached file(s). Please contact the dataset owner if there is a need for users to work with this data using the data.transportation.gov analysis features (online viewing, API, graphing, etc.) and the USDOT will consider modifying the dataset to fully integrate in data.transportation.gov.",
-            "title": "Seattle I-405 Simulated Basic Safety Message",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74866,49 +74840,54 @@
                     "title": "Many Incidents BSM RSE Interchange 75% 500ms "
                 }
             ],
-            "spatial": "Seattle, Washington",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/ntts-pk3f",
+            "issued": "2016-01-01",
+            "keyword": [
+                "basic safety message (bsm)",
+                "connected vehicle message",
+                "freeway",
+                "incident data",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "seattle",
+                "simulated data",
+                "trajectory conversion algorithm (tca)",
+                "vissim",
+                "washington",
+                "weather"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ntts-pk3f",
+            "language": [
+                "en-US"
+            ],
             "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "R/PT0.1S",
+            "modified": "2016-01-01",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
+            "spatial": "Seattle, Washington",
+            "temporal": "2016-08-01/2016-08-01",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Seattle I-405 Simulated Basic Safety Message"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.bts.gov/tpfs",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2019-07-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-21",
-            "keyword": [
-                "federal",
-                "state and local",
-                "transportation expenditure",
-                "transportation finance",
-                "transportation revenue",
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
-            "identifier": "https://data.transportation.gov/api/views/nu8j-7gmn",
             "description": "Government Transportation Financial Statistics is no longer being updated by the Bureau of Transportation Statistics as of June 2024! \r\n\r\nIt is being replaced by our new product, Transportation Public Financial Statistics (TPFS) which provides more granularity by expanding the categories of revenues and expenditures. The new dataset can be found: \r\nhttps://data.bts.gov/Research-and-Statistics/Transportation-Public-Financial-Statistics-TPFS-/6aiz-ybqx/about_data\r\n\r\nFurther information about the TPFS can be found at: https://www.bts.gov/tpfs\r\n\r\nThe government plays an important role in the U.S. transportation system, as a provider of transportation infrastructure and as an administrator and regulator of the system. The government spends a large amount of funds on building, rehabilitating, maintaining, operating, and administering the infrastructure system. Government revenue generated from several sources including user fees, taxes from transportation and non-transportation-related activities, borrowing, and grants from federal, state, and local governments primarily supports these activities.\r\n\r\nGovernment Transportation Financial Statistics (GTFS) provides a set of maps, charts, and tables with information on transportation-related revenue and expenditures for all levels of government, including federal, state, and local, and for all modes of transportation.\r\n\r\nRelated tables can be found in National Transportation Statistics, Section 3.D - Government Finance (https://www.bts.gov/topics/national-transportation-statistics).\r\n\r\nFor further information, data definitions, and methodology, see https://www.bts.gov/gtfs",
-            "title": "Government Transportation Financial Statistics (GTFS) Data",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74916,52 +74895,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/nu8j-7gmn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/nu8j-7gmn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/nu8j-7gmn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/nu8j-7gmn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/nu8j-7gmn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/nu8j-7gmn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/nu8j-7gmn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/nu8j-7gmn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/nu8j-7gmn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "National",
+            "identifier": "https://data.transportation.gov/api/views/nu8j-7gmn",
+            "issued": "2019-07-02",
+            "keyword": [
+                "federal",
+                "state and local",
+                "transportation expenditure",
+                "transportation finance",
+                "transportation revenue",
+                "transportation spending"
+            ],
+            "landingPage": "https://www.bts.gov/tpfs",
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
+            "spatial": "National",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Government Transportation Financial Statistics (GTFS) Data"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/nw2s-ygjq",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/nw2s-ygjq",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "Grade Crossings",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -74969,63 +74959,57 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/nw2s-ygjq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/nw2s-ygjq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/nw2s-ygjq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/nw2s-ygjq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/nw2s-ygjq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/nw2s-ygjq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/nw2s-ygjq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/nw2s-ygjq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/nw2s-ygjq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/nw2s-ygjq",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/nw2s-ygjq",
+            "modified": "2025-01-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Grade Crossings"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/highwaytrustfund/",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/nwrm-fk68",
-            "issued": "2014-12-29",
-            "temporal": "R/2014-12-29/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative - Financial",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "balance",
-                "highway trust fund",
-                "outlays",
-                "receipts"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "DOT-685",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": false,
             "description": "Status of the Highway Trust Fund - The actual receipts, outlays and balances, posted each month shortly after month-end as the information becomes available.",
-            "title": "Status of the Highway Trust Fund",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75034,34 +75018,66 @@
                     "title": "Status of the Highway Trust Fund"
                 }
             ],
-            "spatial": "National",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "DOT-685",
+            "issued": "2014-12-29",
+            "keyword": [
+                "balance",
+                "highway trust fund",
+                "outlays",
+                "receipts"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/highwaytrustfund/",
-            "categoryDesignation": "Administrative - Financial",
+            "landingPage": "https://data.transportation.gov/d/nwrm-fk68",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-1442"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-1442",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "spatial": "National",
+            "temporal": "R/2014-12-29/P1M",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Status of the Highway Trust Fund"
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
-            "landingPage": "https://data.transportation.gov/d/nx3z-j3de",
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
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/statsSas.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Accident/Incident Overview"
+                }
             ],
+            "identifier": "199.2",
+            "isPartOf": "DOT-199",
+            "issued": "2010-09-29",
             "keyword": [
                 "acts of god",
                 "collisions",
@@ -75072,95 +75088,94 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "199.2",
+            "landingPage": "https://data.transportation.gov/d/nx3z-j3de",
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
-            "title": "Rail Equipment Accidents - Accident/Incident Overview",
-            "isPartOf": "DOT-199",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:036"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/statsSas.aspx",
-                    "mediaType": "text/csv",
-                    "title": "Accident/Incident Overview"
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
+            "title": "Rail Equipment Accidents - Accident/Incident Overview"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ny5d-7xny",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Contribution of industries to the economy and their use of transportation services to produce goods and services, including number of person employed in transportation occupations.",
+            "identifier": "https://data.transportation.gov/api/views/ny5d-7xny",
             "issued": "2020-07-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
             "keyword": [
                 "production",
                 "transportation",
                 "transportation satellite accounts"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/ny5d-7xny",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-18",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/ny5d-7xny",
-            "description": "Contribution of industries to the economy and their use of transportation services to produce goods and services, including number of person employed in transportation occupations.",
-            "title": "Transportation Economic Trends: Contribution of Transportation - Industry Snapshots",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Transportation Economic Trends: Contribution of Transportation - Industry Snapshots"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
+            "agencyDataSeriesURL": "https://rosap.ntl.bts.gov/",
+            "agencyProgramURL": "https://ntl.bts.gov/",
+            "analysisUnit": "N/A",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://rosap.ntl.bts.gov/",
-            "issued": "2012-01-01",
-            "temporal": "1920-01-01/2019-05-09",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-10",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://ntlsearch.bts.gov/repository/index.do"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Mary Moulton",
+                "hasEmail": "mailto:Mary.Moulton@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The National Transportation Library (NTL) provides national and international access to transportation information, coordinates information creation and dissemination, and provides reference services for Department of Transportation (DOT) employees and public stakeholders. Established in 1998 by the Transportation Equity Act for the 21st Century (TEA-21; P.L. 105-178), NTL\u2019s authorized role was expanded in 2012\u2019s Moving Ahead for Progress in the 21st Century (MAP-21; P.L. 112- 141). NTL\u2019s primary product and service is the Repository and Open Science Access Portal (ROSA P) (https://rosap.ntl.bts.gov). \n\nNTL\u2019s collections in ROSA P are full-text digital publications, datasets, and other resources. Legacy print materials that have been digitized are collected if they have historic, technical, or national significance. The repository is also designated as the full-text repository for USDOT-funded research under the USDOT Public Access Plan. Collections in ROSA P are available without restriction to transportation researchers, statistical organizations, the media, and the general public.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The National Transportation Library (NTL) provides national and international access to transportation information, coordinates information creation and dissemination, and provides reference services for Department of Transportation (DOT) employees and public stakeholders. Established in 1998 by the Transportation Equity Act for the 21st Century (TEA-21; P.L. 105-178), NTL\u2019s authorized role was expanded in 2012\u2019s Moving Ahead for Progress in the 21st Century (MAP-21; P.L. 112- 141). NTL\u2019s primary product and service is the Repository and Open Science Access Portal (ROSA P) (https://rosap.ntl.bts.gov). \n\nNTL\u2019s collections in ROSA P are full-text digital publications, datasets, and other resources. Legacy print materials that have been digitized are collected if they have historic, technical, or national significance. The repository is also designated as the full-text repository for USDOT-funded research under the USDOT Public Access Plan. Collections in ROSA P are available without restriction to transportation researchers, statistical organizations, the media, and the general public.",
+                    "downloadURL": "https://rosap.ntl.bts.gov/",
+                    "mediaType": "text/html",
+                    "title": "National Transportation Library Repository & Open Science Access Portal"
+                }
             ],
+            "identifier": "DOT-432",
+            "issued": "2012-01-01",
             "keyword": [
                 "accidents",
                 "air quality",
@@ -75194,72 +75209,43 @@
                 "tunnels",
                 "vessels"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Mary Moulton",
-                "hasEmail": "mailto:Mary.Moulton@dot.gov"
-            },
-            "identifier": "DOT-432",
+            "landingPage": "https://rosap.ntl.bts.gov/",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2019-05-10",
+            "phone": "202-366-0303",
+            "primaryITInvestmentUII": "021-658036941",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Research and Innovative Technology Administration"
             },
-            "description": "The National Transportation Library (NTL) provides national and international access to transportation information, coordinates information creation and dissemination, and provides reference services for Department of Transportation (DOT) employees and public stakeholders. Established in 1998 by the Transportation Equity Act for the 21st Century (TEA-21; P.L. 105-178), NTL\u2019s authorized role was expanded in 2012\u2019s Moving Ahead for Progress in the 21st Century (MAP-21; P.L. 112- 141). NTL\u2019s primary product and service is the Repository and Open Science Access Portal (ROSA P) (https://rosap.ntl.bts.gov). \n\nNTL\u2019s collections in ROSA P are full-text digital publications, datasets, and other resources. Legacy print materials that have been digitized are collected if they have historic, technical, or national significance. The repository is also designated as the full-text repository for USDOT-funded research under the USDOT Public Access Plan. Collections in ROSA P are available without restriction to transportation researchers, statistical organizations, the media, and the general public.",
-            "title": "National Transportation Library (NTL) Repository & Open Science Access Platform (ROSA P)",
-            "agencyProgramURL": "https://ntl.bts.gov/",
-            "primaryITInvestmentUII": "021-658036941",
-            "programCode": [
-                "021:053"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://rosap.ntl.bts.gov/",
-                    "description": "The National Transportation Library (NTL) provides national and international access to transportation information, coordinates information creation and dissemination, and provides reference services for Department of Transportation (DOT) employees and public stakeholders. Established in 1998 by the Transportation Equity Act for the 21st Century (TEA-21; P.L. 105-178), NTL\u2019s authorized role was expanded in 2012\u2019s Moving Ahead for Progress in the 21st Century (MAP-21; P.L. 112- 141). NTL\u2019s primary product and service is the Repository and Open Science Access Portal (ROSA P) (https://rosap.ntl.bts.gov). \n\nNTL\u2019s collections in ROSA P are full-text digital publications, datasets, and other resources. Legacy print materials that have been digitized are collected if they have historic, technical, or national significance. The repository is also designated as the full-text repository for USDOT-funded research under the USDOT Public Access Plan. Collections in ROSA P are available without restriction to transportation researchers, statistical organizations, the media, and the general public.",
-                    "@type": "dcat:Distribution",
-                    "title": "National Transportation Library Repository & Open Science Access Portal"
-                }
+            "references": [
+                "http://ntlsearch.bts.gov/repository/index.do"
             ],
             "spatial": "N/A",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "agencyDataSeriesURL": "https://rosap.ntl.bts.gov/",
+            "temporal": "1920-01-01/2019-05-09",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1W",
-            "categoryDesignation": "Research",
-            "analysisUnit": "N/A",
-            "phone": "202-366-0303",
-            "language": [
-                "en-US"
-            ]
+            "title": "National Transportation Library (NTL) Repository & Open Science Access Platform (ROSA P)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/nzpz-e5xn",
             "bureauCode": [
                 "021:17"
             ],
-            "issued": "2023-12-08",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
-            "keyword": [
-                "motor carrier",
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
-            "identifier": "https://data.transportation.gov/api/views/nzpz-e5xn",
             "description": "This dataset contains information on a carrier\u2019s/broker\u2019s/freight forwarder\u2019s previous insurance policy(ies). This dataset contains the DOT number and docket number of the entity. Additionally, it contains the cancellation method (cancelled, replaced, name change, transferred), the type of policy, the policy number, and the effective and cancellation dates of the policy.  All insurance information is related to the insurance policy either being cancelled, being replaced, or prior to a name change.  It is not the subsequent (if applicable) policy.  See dataset attachment \"FMCSA Dataset Description and Data Definitions - Select Datasets\" for more information.",
-            "title": "InsHist - All With History",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75267,28 +75253,57 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/nzpz-e5xn",
+            "issued": "2023-12-08",
+            "keyword": [
+                "motor carrier",
+                "insurance"
+            ],
+            "landingPage": "https://data.transportation.gov/d/nzpz-e5xn",
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
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/p27r-wftd",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/02augtvt/tvtaug02.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "August 2002"
+                }
             ],
+            "identifier": "18.145",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -75298,57 +75313,60 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.145",
+            "landingPage": "https://data.transportation.gov/d/p27r-wftd",
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
-            "title": "Monthly Traffic Volume Trends - August 2002",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/02augtvt/tvtaug02.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "August 2002"
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
+            "title": "Monthly Traffic Volume Trends - August 2002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/p28k-z7re",
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
+                    "description": "2013 Virginia HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/virginia2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Virginia"
+                }
+            ],
+            "identifier": "678.149",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -75362,60 +75380,56 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.149",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Virginia",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/p28k-z7re",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/virginia2013.zip",
-                    "description": "2013 Virginia HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Virginia"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Virginia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyProgramURL": "http://www.nhtsa.gov/fuel-economy",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/p2d3-7dwj",
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
+            "identifier": "1862.1",
+            "isPartOf": "DOT-1862",
+            "issued": "2015-12-16",
             "keyword": [
                 "amfa",
                 "civil penalties",
@@ -75432,62 +75446,38 @@
                 "report",
                 "shortfall"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "1862.1",
+            "landingPage": "https://data.transportation.gov/d/p2d3-7dwj",
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
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/p2i3-kbv9",
-            "issued": "2023-02-04",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/p2i3-kbv9",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "BNSF",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75495,49 +75485,49 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/p2i3-kbv9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/p2i3-kbv9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/p2i3-kbv9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/p2i3-kbv9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/p2i3-kbv9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/p2i3-kbv9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/p2i3-kbv9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/p2i3-kbv9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/p2i3-kbv9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/p2i3-kbv9",
+            "issued": "2023-02-04",
+            "landingPage": "https://data.transportation.gov/d/p2i3-kbv9",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "BNSF"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/p2mt-9ige",
-            "issued": "2025-01-10",
             "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO Office",
                 "hasEmail": "mailto:FMCSA.CDO@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/p2mt-9ige",
             "description": "The FMCSA New Entrant Safety Assurance Program out of service (OOS) data, consists of all entities that have received an OOS order from FMCSA. File is comma delimited.",
-            "title": "OUT OF SERVICE ORDERS",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75545,46 +75535,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/p2mt-9ige/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/p2mt-9ige/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/p2mt-9ige/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/p2mt-9ige/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/p2mt-9ige/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/p2mt-9ige/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/p2mt-9ige/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/p2mt-9ige/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/p2mt-9ige/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/p2mt-9ige",
+            "issued": "2025-01-10",
+            "landingPage": "https://data.transportation.gov/d/p2mt-9ige",
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
+            "title": "OUT OF SERVICE ORDERS"
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
-            "landingPage": "https://data.transportation.gov/d/p2zh-rg3i",
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
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/statsSas.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Accident/Incident Overview"
+                }
             ],
+            "identifier": "214.2",
+            "isPartOf": "DOT-214",
+            "issued": "2010-09-29",
             "keyword": [
                 "accident",
                 "casualty",
@@ -75597,80 +75613,79 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "214.2",
+            "landingPage": "https://data.transportation.gov/d/p2zh-rg3i",
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
-            "title": "Highway Rail Accidents - Accident/Incident Overview",
-            "isPartOf": "DOT-214",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/statsSas.aspx",
-                    "mediaType": "text/csv",
-                    "title": "Accident/Incident Overview"
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
+            "title": "Highway Rail Accidents - Accident/Incident Overview"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/p3bt-a5up",
-            "issued": "2024-10-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-10-04",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DiJoseph, Patricia (OST)",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/p3bt-a5up",
+            "issued": "2024-10-03",
+            "landingPage": "https://data.transportation.gov/d/p3bt-a5up",
+            "modified": "2024-10-04",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Containerized Imports at US Ports"
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
-            "landingPage": "https://data.transportation.gov/d/p3c6-j4dy",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/09maytvt/09maytvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "May 2009"
+                }
             ],
+            "identifier": "18.34",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -75680,84 +75695,49 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.34",
+            "landingPage": "https://data.transportation.gov/d/p3c6-j4dy",
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
-            "title": "Monthly Traffic Volume Trends - May 2009",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/09maytvt/09maytvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "May 2009"
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
+            "title": "Monthly Traffic Volume Trends - May 2009"
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
-            "landingPage": "https://data.transportation.gov/d/p3jd-zfum",
-            "issued": "1999-09-17",
-            "temporal": "1994-06-01/1998-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
-            "collectionInstrument": "Transportation",
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
+            "categoryDesignation": "Research",
+            "collectionInstrument": "Transportation",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "289.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "The Pedestrian Crash Data Study (PCDS) collected detailed data on motor vehicle vs pedestrian crashes.",
-            "title": "The Pedestrian Crash Data Study (PCDS) - SAS File",
-            "isPartOf": "DOT-289",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75766,59 +75746,59 @@
                     "title": "SAS File"
                 }
             ],
-            "spatial": "United States",
-            "dataQuality": true,
+            "identifier": "289.1",
+            "isPartOf": "DOT-289",
+            "issued": "1999-09-17",
+            "keyword": [
+                "crash",
+                "injury",
+                "motor vehicle",
+                "pedestrian",
+                "vehicle"
+            ],
+            "landingPage": "https://data.transportation.gov/d/p3jd-zfum",
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
+            "title": "The Pedestrian Crash Data Study (PCDS) - SAS File"
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
-            "landingPage": "https://data.transportation.gov/d/p483-abjt",
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
-            "identifier": "80.1",
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
@@ -75827,58 +75807,59 @@
                     "title": "NHTSA API"
                 }
             ],
-            "spatial": "Zip, State, Geo co-ordinates",
-            "dataQuality": false,
+            "identifier": "80.1",
+            "isPartOf": "DOT-80",
+            "issued": "2010-01-05",
+            "keyword": [
+                "child seat",
+                "inspection",
+                "safety",
+                "station",
+                "stations"
+            ],
+            "landingPage": "https://data.transportation.gov/d/p483-abjt",
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
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www.fmcsa.dot.gov/rules-regulations/administration/fmcsr/fmcsrguide.aspx%3Fsection_type=G",
+            "agencyProgramURL": "http://www.fmcsa.dot.gov/rules-regulations/administration/fmcsr/fmcsrguide.aspx%3Fsection_type=G",
+            "analysisUnit": "Regulations",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/p4kt-vnkq",
-            "issued": "2011-01-18",
-            "temporal": "2007-01-01/2011-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-31",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.fmcsa.dot.gov/rules-regulations/administration/fmcsr/fmcsrguide.aspx%3Fsection_type=G"
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
-            "identifier": "305.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": true,
             "description": "A list of Significant Guidance documents, which include guidance document disseminated to regulated entities or the general public that may reasonably be anticipated to lead to an annual effect on the economy of $100 million or more or adversely affect in a material way the economy, a sector of the economy, productivity, competition, jobs, the environment, public health or safety, or State, local, or tribal governments or communities; create a serious inconsistency or otherwise interfere with an action taken or planned by another agency; materially alter the budgetary impact of entitlements, grants, user fees, or loan programs or the rights and obligations of recipients thereof; or raise novel legal or policy issues arising out of legal mandates, the President's priorities, or the principles set forth in Executive Order 12866, as further amended.",
-            "title": "Significant Guidance Issued by the Federal Motor Carrier Safety Administration -",
-            "isPartOf": "DOT-305",
-            "agencyProgramURL": "http://www.fmcsa.dot.gov/rules-regulations/administration/fmcsr/fmcsrguide.aspx%3Fsection_type=G",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -75886,31 +75867,68 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "305.2",
+            "isPartOf": "DOT-305",
+            "issued": "2011-01-18",
+            "keyword": [
+                "data.gov",
+                "law",
+                "significant guidance",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/p4kt-vnkq",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fmcsa.dot.gov/rules-regulations/administration/fmcsr/fmcsrguide.aspx%3Fsection_type=G",
+            "modified": "2024-05-31",
+            "phone": "202-493-0215",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "references": [
+                "http://www.fmcsa.dot.gov/rules-regulations/administration/fmcsr/fmcsrguide.aspx%3Fsection_type=G"
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
-            "landingPage": "https://data.transportation.gov/d/p5n7-79rg",
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
+                    "description": "2011 Pennsylvania HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/pennsylvania2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Pennsylvania"
+                }
+            ],
+            "identifier": "678.40",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -75924,78 +75942,40 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.40",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Pennsylvania",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/p5n7-79rg",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/pennsylvania2011.zip",
-                    "description": "2011 Pennsylvania HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Pennsylvania"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Pennsylvania"
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
-            "identifier": "https://data.transportation.gov/api/views/p5ru-9mg9",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 2000",
-            "title": "Historic HPMS Data (Sample) - 2000",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76003,98 +75983,101 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/p5ru-9mg9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/p5ru-9mg9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/p5ru-9mg9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/p5ru-9mg9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/p5ru-9mg9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/p5ru-9mg9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/p5ru-9mg9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/p5ru-9mg9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/p5ru-9mg9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/p5ru-9mg9",
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
+            "title": "Historic HPMS Data (Sample) - 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/p6ng-bqkx",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2020-04-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-30",
-            "keyword": [
-                "government revenue",
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
-            "identifier": "https://data.transportation.gov/api/views/p6ng-bqkx",
             "description": "Government transportation revenue",
-            "title": "Transportation Economic Trends: Government Transportation Revenue",
+            "identifier": "https://data.transportation.gov/api/views/p6ng-bqkx",
+            "issued": "2020-04-23",
+            "keyword": [
+                "government revenue",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/p6ng-bqkx",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-12-30",
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
+            "title": "Transportation Economic Trends: Government Transportation Revenue"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/p7t5-fmvf",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-09-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-30",
-            "keyword": [
-                "commodity",
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
-            "identifier": "https://data.transportation.gov/api/views/p7t5-fmvf",
             "description": "Source: U.S. Department of Transportation, Bureau of Transportation Statistics, based upon U.S. Department of Commerce, U.S. Census Bureau, Foreign Trade Division, USA Trade Online \"HS Port-level Data\", available at https://usatrade.census.gov/ as of Sept 2024.\nShipping weight is in kg.",
-            "title": "Top 10 Containerized Import Commodities by Shipping Weight and Coast 2023",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76102,68 +76085,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/p7t5-fmvf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/p7t5-fmvf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/p7t5-fmvf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/p7t5-fmvf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/p7t5-fmvf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/p7t5-fmvf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/p7t5-fmvf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/p7t5-fmvf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/p7t5-fmvf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/p7t5-fmvf",
+            "issued": "2024-09-30",
+            "keyword": [
+                "commodity",
+                "imports",
+                "ports"
+            ],
+            "landingPage": "https://data.transportation.gov/d/p7t5-fmvf",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-09-30",
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
+            "title": "Top 10 Containerized Import Commodities by Shipping Weight and Coast 2023"
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
-            "identifier": "https://data.transportation.gov/api/views/p7t6-tka4",
             "description": "Historic Highway Performance Monitoring System sample data for the year 1996",
-            "title": "Historic HPMS Data (Sample) - 1996",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76171,73 +76150,75 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/p7t6-tka4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/p7t6-tka4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/p7t6-tka4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/p7t6-tka4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/p7t6-tka4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/p7t6-tka4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/p7t6-tka4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/p7t6-tka4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/p7t6-tka4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/p7t6-tka4",
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
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Historic HPMS Data (Sample) - 1996"
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
-            "landingPage": "https://data.transportation.gov/d/p8ie-hvfd",
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
-            "identifier": "698.2",
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
@@ -76246,36 +76227,71 @@
                     "title": "Monthly Motor Fuel Reports"
                 }
             ],
-            "spatial": "National, State",
-            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hss/guide/ch2.cfm",
-            "dataQuality": true,
+            "identifier": "698.2",
+            "isPartOf": "DOT-698",
+            "issued": "1998-01-01",
+            "keyword": [
+                "diesel",
+                "fuel tax",
+                "gallons",
+                "gasoline",
+                "motor fuel"
+            ],
+            "landingPage": "https://data.transportation.gov/d/p8ie-hvfd",
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
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/",
+            "agencyProgramURL": "http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/",
+            "analysisUnit": "Region",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/p8n7-xzhk",
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
+                    "downloadURL": "http://faf.ornl.gov/fafweb/FUT.aspx",
+                    "mediaType": "text/html",
+                    "title": "All FAF summary datasets"
+                }
             ],
+            "identifier": "286.7",
+            "isPartOf": "DOT-286",
+            "issued": "2013-03-20",
             "keyword": [
                 "commodity",
                 "consumption",
@@ -76300,86 +76316,51 @@
                 "value",
                 "wear"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "286.7",
+            "landingPage": "https://data.transportation.gov/d/p8n7-xzhk",
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
-            "title": "Freight Analysis Framework - All FAF summary datasets",
-            "isPartOf": "DOT-286",
-            "agencyProgramURL": "http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://faf.ornl.gov/fafweb/FUT.aspx",
-                    "mediaType": "text/html",
-                    "title": "All FAF summary datasets"
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
+            "title": "Freight Analysis Framework - All FAF summary datasets"
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
-            "landingPage": "https://data.transportation.gov/d/p8qw-xvej",
-            "issued": "2010-09-29",
-            "temporal": "R/1975-01-31/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-09",
+            "categoryDesignation": "Research",
             "collectionInstrument": "https://safetydata.fra.dot.gov/Gcis/UserManagement/Login.aspx",
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
-            "identifier": "DOT-224",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Railroad Administration"
-            },
-            "description": "The entire National Highway-Rail Crossing Inventory is available in three separate downloadble files. There is a file of all current Public-at-Grade crossings. There is a file of all current Private and grade-separated crossings. There is also a file which contains about 10 years of archival records for all types of crossings.",
-            "title": "Highway-Rail Crossings Inventory Data",
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
@@ -76388,36 +76369,70 @@
                     "title": "Crossing Inventory - Public Site"
                 }
             ],
-            "spatial": "Latitude/Longitude",
-            "describedBy": "http://safetydata.fra.dot.gov/OfficeofSafety/Documents/GCIS%20Electronic%20Submissions%20Instructions.pdf",
-            "dataQuality": true,
+            "identifier": "DOT-224",
+            "issued": "2010-09-29",
+            "keyword": [
+                "acts of god",
+                "collisions",
+                "derailments",
+                "explosions",
+                "fires",
+                "rail"
+            ],
+            "landingPage": "https://data.transportation.gov/d/p8qw-xvej",
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
+            "title": "Highway-Rail Crossings Inventory Data"
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
-            "landingPage": "https://data.transportation.gov/d/p9n7-6bei",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/07maytvt/07maytvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "May 2007"
+                }
             ],
+            "identifier": "18.88",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -76427,75 +76442,43 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.88",
+            "landingPage": "https://data.transportation.gov/d/p9n7-6bei",
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
-            "title": "Monthly Traffic Volume Trends - May 2007",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/07maytvt/07maytvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "May 2007"
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
+            "title": "Monthly Traffic Volume Trends - May 2007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/pa3c-z6h4",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-10-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-02",
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
-            "identifier": "https://data.transportation.gov/api/views/pa3c-z6h4",
             "description": "Source: U.S. Department of Transportation, Bureau of Transportation Statistics, based upon U.S. Department of Commerce, U.S. Census Bureau, Foreign Trade Division, USA Trade Online, \"HS Port-level Data\", available at https://usatrade.census.gov/ as of Sept 2024.",
-            "title": "Top 10 Containerized Export Non-Durable Commodities in Short Tons by Coast, 2023",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76503,132 +76486,128 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/pa3c-z6h4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/pa3c-z6h4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/pa3c-z6h4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/pa3c-z6h4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/pa3c-z6h4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/pa3c-z6h4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/pa3c-z6h4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/pa3c-z6h4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/pa3c-z6h4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/pa3c-z6h4",
+            "issued": "2024-10-02",
+            "keyword": [
+                "containerized",
+                "exports",
+                "ports"
+            ],
+            "landingPage": "https://data.transportation.gov/d/pa3c-z6h4",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-10-02",
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
+            "title": "Top 10 Containerized Export Non-Durable Commodities in Short Tons by Coast, 2023"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/pamu-knra",
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
             "identifier": "https://data.transportation.gov/api/views/pamu-knra",
+            "issued": "2021-01-21",
+            "landingPage": "https://data.transportation.gov/d/pamu-knra",
+            "modified": "2021-01-21",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "NTS"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/pbag-pyes",
-            "issued": "2021-04-26",
             "@type": "dcat:Dataset",
-            "modified": "2024-02-07",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Chambers",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "PPFSP 24",
             "identifier": "https://data.transportation.gov/api/views/pbag-pyes",
+            "issued": "2021-04-26",
+            "landingPage": "https://data.transportation.gov/d/pbag-pyes",
+            "modified": "2024-02-07",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "PPFSP 24",
             "title": "Container Vessel Dwell Times"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/pbt9-k67k",
-            "issued": "2023-10-18",
             "@type": "dcat:Dataset",
-            "modified": "2024-12-02",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sean Jahanmir",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/pbt9-k67k",
+            "issued": "2023-10-18",
+            "landingPage": "https://data.transportation.gov/d/pbt9-k67k",
+            "modified": "2024-12-02",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Data Visualizations"
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
-            "landingPage": "https://data.transportation.gov/d/pbwd-g6js",
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
-            "identifier": "524.22",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
             "description": "STATE DATA REPORTING SYSTEMS. Annual reports on the Fatality Analysis Reporting System (FARS) which is data regarding fatalities that is collected by a FARS analyst from each State and provided to NHTSA.",
-            "title": "GES Reports - 1991",
-            "isPartOf": "DOT-524",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76637,35 +76616,71 @@
                     "title": "1991"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
-            "dataQuality": true,
+            "identifier": "524.22",
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
+            "landingPage": "https://data.transportation.gov/d/pbwd-g6js",
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
+            "title": "GES Reports - 1991"
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
-            "landingPage": "https://data.transportation.gov/d/pdby-qvwy",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/08maytvt/08maytvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "May 2008"
+                }
             ],
+            "identifier": "18.76",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -76675,60 +76690,60 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.76",
+            "landingPage": "https://data.transportation.gov/d/pdby-qvwy",
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
-            "title": "Monthly Traffic Volume Trends - May 2008",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/08maytvt/08maytvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "May 2008"
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
+            "title": "Monthly Traffic Volume Trends - May 2008"
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
-            "landingPage": "https://data.transportation.gov/d/peci-d8pn",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/02aprtvt/tvtapr02.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "April 2002"
+                }
             ],
+            "identifier": "18.149",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -76738,82 +76753,49 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.149",
+            "landingPage": "https://data.transportation.gov/d/peci-d8pn",
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
-            "title": "Monthly Traffic Volume Trends - April 2002",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/02aprtvt/tvtapr02.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "April 2002"
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
+            "title": "Monthly Traffic Volume Trends - April 2002"
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
-            "landingPage": "https://data.transportation.gov/d/pf9x-tiut",
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
-            "identifier": "364.25",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2007",
-            "isPartOf": "DOT-364",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
-            "primaryITInvestmentUII": "021-621341357",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76822,89 +76804,89 @@
                     "title": "Event Data Records Reports - 2007"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.25",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/pf9x-tiut",
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
+            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/pgc3-e7j9",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2019-12-07",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
-            "keyword": [
-                "contribution of transportation",
-                "final demand"
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
-            "identifier": "https://data.transportation.gov/api/views/pgc3-e7j9",
             "description": "Final Demand Attributed to Transportation",
-            "title": "Transportation Economic Trends: Contribution of Transportation - Final Demand",
+            "identifier": "https://data.transportation.gov/api/views/pgc3-e7j9",
+            "issued": "2019-12-07",
+            "keyword": [
+                "contribution of transportation",
+                "final demand"
+            ],
+            "landingPage": "https://data.transportation.gov/d/pgc3-e7j9",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-27",
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
+            "title": "Transportation Economic Trends: Contribution of Transportation - Final Demand"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "The data system is not publicly available because it is related solely to internal agency management and may contain sensitive data.",
+            "accrualPeriodicity": "R/PT1S",
+            "agencyDataSeriesURL": "http://fhwadms.fhwa.dot.gov/sites/FHWACA",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/phec-e6gt",
-            "issued": "2009-12-01",
-            "temporal": "R/2009-12-01/PT1S",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative;Operations;Project",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
-            "keyword": [
-                "document management",
-                "fhwa",
-                "nara",
-                "workflow management"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "697.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "The Document Management System will provide FHWA the capability to integrate document creation, storage, and transfer with critical business process applications. The electronic DMS is comprised of 2 components: (1) a SharePoint solution delivered as a temporary solution for 3 field offices that were using GroupWise, that was intended to provide a temporary solution while FHWA explored other enterprise Document and Records Management solutions that better served the needs of the entire mode. This is operational, and It will be decommissioned upon implementation of the enterprise solution. (2) the Enterprise Document and Records Management solution. We have completed the initial requirements phase.%3F",
-            "title": "FHWA Document Management System (DMS) -",
-            "primaryITInvestmentUII": "021-268349528",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76912,33 +76894,68 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "697.0",
+            "issued": "2009-12-01",
+            "keyword": [
+                "document management",
+                "fhwa",
+                "nara",
+                "workflow management"
             ],
-            "accrualPeriodicity": "R/PT1S",
-            "agencyDataSeriesURL": "http://fhwadms.fhwa.dot.gov/sites/FHWACA",
-            "categoryDesignation": "Administrative;Operations;Project",
+            "landingPage": "https://data.transportation.gov/d/phec-e6gt",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-9029"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "202-366-9029",
+            "primaryITInvestmentUII": "021-268349528",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "rights": "The data system is not publicly available because it is related solely to internal agency management and may contain sensitive data.",
+            "temporal": "R/2009-12-01/PT1S",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "FHWA Document Management System (DMS) -"
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
-            "landingPage": "https://data.transportation.gov/d/pin3-udpr",
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
+            "identifier": "83.7",
+            "isPartOf": "DOT-83",
+            "issued": "2002-12-16",
             "keyword": [
                 "air bag",
                 "air bags",
@@ -76965,81 +76982,43 @@
                 "vin",
                 "vin search"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "83.7",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Manufacturers who determine that a product or piece of original equipment either has a safety defect or is not in compliance with Federal safety standards are required to notify the National Highway Traffic Safety Administration (NHTSA) within 5 business days. NHTSA requires that manufacturers file a Defect and Noncompliance report as well as quarterly recall status reports, in compliance with Federal Regulation 49 (the National Traffic and Motor Safety Act) Part 573, which identifies the requirements for safety recalls. This information is stored in the NHTSA database. Use this data to search for recall information related to:-\tSpecific NHTSA campaigns -\tProduct types Access to public searches of NHTSA recall databases for tires, vehicles, car seats and equipment.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - Recalls Lookup by VIN",
-            "isPartOf": "DOT-83",
-            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
-            "describedByType": "text/plain",
+            "landingPage": "https://data.transportation.gov/d/pin3-udpr",
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
-            "phone": "202-366-0154",
-            "language": [
-                "en-US"
-            ]
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - Recalls Lookup by VIN"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/pivg-szje",
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
-            "identifier": "https://data.transportation.gov/api/views/pivg-szje",
             "description": "*This is a \"daily difference\" dataset.  See dataset attachment \"FMCSA Dataset Description and Data Definitions - Select Datasets\" for more information.*  Information on carrier/broker/freight forwarder authorities that have been revoked by FMCSA. The dataset includes the DOT number and docket number of the entity, the type of authority revoked, and the reason.",
-            "title": "Revocation",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77047,22 +77026,61 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/pivg-szje",
+            "issued": "2023-04-14",
+            "keyword": [
+                "active",
+                "for-hire motor carriers",
+                "operating authority",
+                "registration status",
+                "revoked",
+                "suspended"
+            ],
+            "landingPage": "https://data.transportation.gov/d/pivg-szje",
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
+            "title": "Revocation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/pjiw-sxdj",
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
+                    "description": "2011 New Mexico HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/newmexico2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 New Mexico"
+                }
+            ],
+            "identifier": "678.33",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -77076,83 +77094,43 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.33",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 New Mexico",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/pjiw-sxdj",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/newmexico2011.zip",
-                    "description": "2011 New Mexico HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 New Mexico"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 New Mexico"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Access is restricted to FMCSA field and headquartered employees.",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/pjpv-6sxz",
-            "issued": "2011-12-05",
-            "temporal": "R/2011-12-05/PT1S",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-31",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Electronic",
-            "keyword": [
-                "application enhancement",
-                "application governance",
-                "application modification and application defect resolution",
-                "modification requests",
-                "mrs",
-                "production fix",
-                "sdlc."
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO",
                 "hasEmail": "mailto:fmcsa.cdo@dot.gov"
             },
-            "identifier": "1639.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": false,
             "description": "IT Configuration Management: eReqs is a multi-phase, web-based enterprise system that allows federal and state users to submit requests for application enhancement, application modification and application defect resolution.",
-            "title": "eREQS -",
-            "primaryITInvestmentUII": "021-000001018",
-            "programCode": [
-                "021:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77160,32 +77138,69 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "1639.0",
+            "issued": "2011-12-05",
+            "keyword": [
+                "application enhancement",
+                "application governance",
+                "application modification and application defect resolution",
+                "modification requests",
+                "mrs",
+                "production fix",
+                "sdlc."
             ],
-            "accrualPeriodicity": "R/PT1S",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/pjpv-6sxz",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-0440"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-31",
+            "phone": "202-366-0440",
+            "primaryITInvestmentUII": "021-000001018",
+            "programCode": [
+                "021:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "rights": "Access is restricted to FMCSA field and headquartered employees.",
+            "temporal": "R/2011-12-05/PT1S",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "eREQS -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/NTS/",
+            "agencyProgramURL": "https://www.nhtsa.gov/crash-data-systems/non-traffic-surveillance",
+            "analysisUnit": "vehicle crash",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/pjrk-m2dz",
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
+            "description": "The Not-in-Traffic Surveillance (NTS) system is a virtual data collection system designed to provide counts and details regarding fatalities and injuries that occur in non-traffic crashes and in non-crash incidents. NiTS non-traffic crash data is obtained through NHTSA's National Automotive Sampling System, General Estimates System (NASS GES) and the Fatality Analysis Reporting System (FARS). NiTS non-crash injury data is based upon emergency department records from a special study conducted by the Consumer Product Safety Commission's National Electronic Injury Surveillance System (NEISS) All Injury Program. NiTS non-crash fatality data is derived from death certificate information from the Centers for Disease Control's National Vital Statistics System.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.nhtsa.gov/content/nhtsa-ftp/179891",
+                    "mediaType": "application/vndams-excel",
+                    "title": "NTS Data"
+                }
             ],
+            "identifier": "DOT-288",
+            "issued": "2009-01-27",
             "keyword": [
                 "crash",
                 "death",
@@ -77201,91 +77216,87 @@
                 "vehicle",
                 "victim"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "DOT-288",
+            "landingPage": "https://data.transportation.gov/d/pjrk-m2dz",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-2714",
+            "programCode": [
+                "021:032"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Highway Traffic Safety Administration"
             },
-            "description": "The Not-in-Traffic Surveillance (NTS) system is a virtual data collection system designed to provide counts and details regarding fatalities and injuries that occur in non-traffic crashes and in non-crash incidents. NiTS non-traffic crash data is obtained through NHTSA's National Automotive Sampling System, General Estimates System (NASS GES) and the Fatality Analysis Reporting System (FARS). NiTS non-crash injury data is based upon emergency department records from a special study conducted by the Consumer Product Safety Commission's National Electronic Injury Surveillance System (NEISS) All Injury Program. NiTS non-crash fatality data is derived from death certificate information from the Centers for Disease Control's National Vital Statistics System.",
-            "title": "Not in Traffic Surveillance (NTS)",
-            "agencyProgramURL": "https://www.nhtsa.gov/crash-data-systems/non-traffic-surveillance",
-            "programCode": [
-                "021:032"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.nhtsa.gov/content/nhtsa-ftp/179891",
-                    "mediaType": "application/vndams-excel",
-                    "title": "NTS Data"
-                }
+            "references": [
+                "http://www-nrd.nhtsa.dot.gov/Cats/listpublications.aspx%3FId=233&ShowBy=Category"
             ],
             "spatial": "United States of America",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/Cats/listpublications.aspx%3FId=233&ShowBy=Category",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/NTS/",
+            "temporal": "2008-01-01/2010-12-31",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "analysisUnit": "vehicle crash",
-            "phone": "202-366-2714",
-            "language": [
-                "en-US"
-            ]
+            "title": "Not in Traffic Surveillance (NTS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/pk4v-772c",
             "bureauCode": [
                 "021:27"
             ],
-            "issued": "2024-08-14",
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
-            "identifier": "https://data.transportation.gov/api/views/pk4v-772c",
+            "dataQuality": true,
             "description": "This is the data download page for FRA Form 6180.54 Rail Equipment Accident/Incident data.",
-            "title": "Form 54 Data Downloads",
+            "identifier": "https://data.transportation.gov/api/views/pk4v-772c",
+            "issued": "2024-08-14",
+            "landingPage": "https://data.transportation.gov/d/pk4v-772c",
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
+            "title": "Form 54 Data Downloads"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "021:00"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Transportation Library Data Curator",
+                "hasEmail": "mailto:ntldatacurator@dot.gov"
             },
+            "dataQuality": true,
+            "description": "This project focused specifically on design treatments that can be used to improve travel time reliability. The objectives of this research were to (1) identify the full range of possible roadway design features used by transportation agencies to improve travel time reliability and reduce delays from key causes of nonrecurrent congestion, (2) assess their costs and operational and safety effectiveness, and (3) provide recommendations for their use and eventual incorporation into appropriate design guides. This research generated two companion products that allow transportation agencies and professionals to apply these research findings effectively in daily practice. These products are the Design Guide for Addressing Nonrecurrent Congestion, which is a catalogue of the design elements and their associated use information, and the Analysis Tool for Design Treatments to Address Nonrecurring Congestion, which is a tool to execute the various analysis procedures and models to measure the effectiveness of a design element on travel time reliability.  This zip file contains comma separated value (.csv) files of data to support SHRP 2 Report S2-L07-RR-1, Identification and Evaluation of the Cost-Effectiveness of Highway Design Features to Reduce Nonrecurrent Congestion, https://rosap.ntl.bts.gov/view/dot/4040  The compressed zip file is 12 MB. These files can be unzipped using any zip compression/decompression software. The .csv files can be read with any basic text editor.",
+            "distribution": [
                 {
-            "accessLevel": "public",
-            "landingPage": "https://doi.org/10.21949/1503769",
-            "bureauCode": [
-                "021:00"
+                    "@type": "dcat:Distribution",
+                    "description": "This project focused specifically on design treatments that can be used to improve travel time reliability. The objectives of this research were to (1) identify the full range of possible roadway design features used by transportation agencies to improve travel time reliability and reduce delays from key causes of nonrecurrent congestion, (2) assess their costs and operational and safety effectiveness, and (3) provide recommendations for their use and eventual incorporation into appropriate design guides. This research generated two companion products that allow transportation agencies and professionals to apply these research findings effectively in daily practice. These products are the Design Guide for Addressing Nonrecurrent Congestion, which is a catalogue of the design elements and their associated use information, and the Analysis Tool for Design Treatments to Address Nonrecurring Congestion, which is a tool to execute the various analysis procedures and models to measure the effectiveness of a design element on travel time reliability.  This zip file contains comma separated value (.csv) files of data to support SHRP 2 Report S2-L07-RR-1, Identification and Evaluation of the Cost-Effectiveness of Highway Design Features to Reduce Nonrecurrent Congestion, https://rosap.ntl.bts.gov/view/dot/4040  The compressed zip file is 12 MB. These files can be unzipped using any zip compression/decompression software. The .csv files can be read with any basic text editor.",
+                    "downloadURL": "https://doi.org/10.21949/1503769",
+                    "mediaType": "application/zip",
+                    "title": "Identification and Evaluation of the Cost-Effectiveness of Highway Design Features to Reduce Nonrecurrent Congestion [supporting datasets]"
+                }
             ],
+            "identifier": "https://data.transportation.gov/api/views/pkq2-c4au",
             "issued": "2014-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2016-12-20",
-            "references": [
-                "https://rosap.ntl.bts.gov/view/dot/4040"
-            ],
             "keyword": [
                 "benefit cost analysis",
                 "cost effectiveness",
@@ -77303,69 +77314,38 @@
                 "travel time",
                 "travel time reliability"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Transportation Library Data Curator",
-                "hasEmail": "mailto:ntldatacurator@dot.gov"
-            },
+            "landingPage": "https://doi.org/10.21949/1503769",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2016-12-20",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/pkq2-c4au",
-            "description": "This project focused specifically on design treatments that can be used to improve travel time reliability. The objectives of this research were to (1) identify the full range of possible roadway design features used by transportation agencies to improve travel time reliability and reduce delays from key causes of nonrecurrent congestion, (2) assess their costs and operational and safety effectiveness, and (3) provide recommendations for their use and eventual incorporation into appropriate design guides. This research generated two companion products that allow transportation agencies and professionals to apply these research findings effectively in daily practice. These products are the Design Guide for Addressing Nonrecurrent Congestion, which is a catalogue of the design elements and their associated use information, and the Analysis Tool for Design Treatments to Address Nonrecurring Congestion, which is a tool to execute the various analysis procedures and models to measure the effectiveness of a design element on travel time reliability.  This zip file contains comma separated value (.csv) files of data to support SHRP 2 Report S2-L07-RR-1, Identification and Evaluation of the Cost-Effectiveness of Highway Design Features to Reduce Nonrecurrent Congestion, https://rosap.ntl.bts.gov/view/dot/4040  The compressed zip file is 12 MB. These files can be unzipped using any zip compression/decompression software. The .csv files can be read with any basic text editor.",
-            "title": "Identification and Evaluation of the Cost-Effectiveness of Highway Design Features to Reduce Nonrecurrent Congestion [supporting datasets]",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://doi.org/10.21949/1503769",
-                    "description": "This project focused specifically on design treatments that can be used to improve travel time reliability. The objectives of this research were to (1) identify the full range of possible roadway design features used by transportation agencies to improve travel time reliability and reduce delays from key causes of nonrecurrent congestion, (2) assess their costs and operational and safety effectiveness, and (3) provide recommendations for their use and eventual incorporation into appropriate design guides. This research generated two companion products that allow transportation agencies and professionals to apply these research findings effectively in daily practice. These products are the Design Guide for Addressing Nonrecurrent Congestion, which is a catalogue of the design elements and their associated use information, and the Analysis Tool for Design Treatments to Address Nonrecurring Congestion, which is a tool to execute the various analysis procedures and models to measure the effectiveness of a design element on travel time reliability.  This zip file contains comma separated value (.csv) files of data to support SHRP 2 Report S2-L07-RR-1, Identification and Evaluation of the Cost-Effectiveness of Highway Design Features to Reduce Nonrecurrent Congestion, https://rosap.ntl.bts.gov/view/dot/4040  The compressed zip file is 12 MB. These files can be unzipped using any zip compression/decompression software. The .csv files can be read with any basic text editor.",
-                    "@type": "dcat:Distribution",
-                    "title": "Identification and Evaluation of the Cost-Effectiveness of Highway Design Features to Reduce Nonrecurrent Congestion [supporting datasets]"
-                }
+            "references": [
+                "https://rosap.ntl.bts.gov/view/dot/4040"
             ],
             "spatial": "United States",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "language": [
-                "en-US"
-            ]
+            "title": "Identification and Evaluation of the Cost-Effectiveness of Highway Design Features to Reduce Nonrecurrent Congestion [supporting datasets]"
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
-            "identifier": "https://data.transportation.gov/api/views/pm76-ggui",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 2003",
-            "title": "Historic HPMS Data (Sample) - 2003",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77373,50 +77353,85 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/pm76-ggui/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/pm76-ggui/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/pm76-ggui/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/pm76-ggui/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/pm76-ggui/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/pm76-ggui/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/pm76-ggui/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/pm76-ggui/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/pm76-ggui/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/pm76-ggui",
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
+            "title": "Historic HPMS Data (Sample) - 2003"
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
-            "landingPage": "https://data.transportation.gov/d/pmy4-2cci",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/13novtvt/13novtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "November 2013"
+                }
             ],
+            "identifier": "18.56",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -77426,84 +77441,48 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.56",
+            "landingPage": "https://data.transportation.gov/d/pmy4-2cci",
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
-            "title": "Monthly Traffic Volume Trends - November 2013",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/13novtvt/13novtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "November 2013"
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
+            "title": "Monthly Traffic Volume Trends - November 2013"
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
-            "landingPage": "https://data.transportation.gov/d/pna7-5aen",
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
-            "identifier": "1842.1",
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
@@ -77512,57 +77491,55 @@
                     "title": "Latest Tests"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "1842.1",
+            "isPartOf": "DOT-1842",
+            "issued": "1999-04-26",
+            "keyword": [
+                "compliance",
+                "component",
+                "test",
+                "vehicle"
+            ],
+            "landingPage": "https://data.transportation.gov/d/pna7-5aen",
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
             "accessLevel": "non-public",
-            "rights": "The data set contains controlled unclassified procurement information, confidential business information, and information protected by statute or regulation.",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/pnp8-24gn",
-            "issued": "2014-12-29",
-            "temporal": "R/2014-12-29/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "bill presentment",
-                "cash receipts",
-                "collection",
-                "customer",
-                "geographical hierarchical structures",
-                "line of accounting",
-                "payments",
-                "sales tax"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "598.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
             "description": "Delphi accounts receivable module contains the following data elements, but are not limited to customer information, cash receipts, line of accounting details, bill presentment architecture, collection information, payments interface, sales tax information, and geographical hierarchical structures.",
-            "title": "Delphi Accounts Receivable Module -",
-            "primaryITInvestmentUII": "021-105731835",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77570,29 +77547,70 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "theme": [
-                "Transportation"
+            "identifier": "598.0",
+            "issued": "2014-12-29",
+            "keyword": [
+                "bill presentment",
+                "cash receipts",
+                "collection",
+                "customer",
+                "geographical hierarchical structures",
+                "line of accounting",
+                "payments",
+                "sales tax"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/pnp8-24gn",
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
+            "title": "Delphi Accounts Receivable Module -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/pp4z-sh8j",
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
+                    "description": "2012 Wyoming HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/wyoming2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Wyoming"
+                }
+            ],
+            "identifier": "678.104",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -77606,73 +77624,39 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.104",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Wyoming",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/pp4z-sh8j",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/wyoming2012.zip",
-                    "description": "2012 Wyoming HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Wyoming"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Wyoming"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ppe3-tvgj",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2020-06-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-25",
-            "keyword": [
-                "noise"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Justyna Goworowska",
                 "hasEmail": "mailto:j.goworowska.ctr@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/ppe3-tvgj",
             "description": "This table shows the number and percent of people in the United States potentially exposed to different levels of noise from road sources.",
-            "title": "Population potentially exposed to road noise, 2016 and 2018",
-            "programCode": [
-                "021:052"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77680,66 +77664,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ppe3-tvgj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ppe3-tvgj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ppe3-tvgj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ppe3-tvgj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ppe3-tvgj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ppe3-tvgj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ppe3-tvgj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ppe3-tvgj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ppe3-tvgj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/ppe3-tvgj",
+            "issued": "2020-06-22",
+            "keyword": [
+                "noise"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ppe3-tvgj",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2020-06-25",
+            "programCode": [
+                "021:052"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "Population potentially exposed to road noise, 2016 and 2018"
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
-            "landingPage": "https://data.transportation.gov/d/pq82-pyxa",
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
-            "identifier": "DOT-10",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
+            "describedBy": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Transaction+Data+and+Reports",
             "description": "The Car Allowance Rebate System (CARS), otherwise known as Cash for Clunkers, was a program intended to provide economic incentives to United States residents to purchase a new and more fuel efficient vehicle when trading in a less full efficient vehicle. The program was promoted as providing stimulus to the economy by boosting auto sales, while putting safer, cleaner and more fuel efficient vehicles on the road.",
-            "title": "Car Allowance Rebate System (CARS) - Transactions",
-            "agencyProgramURL": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Officially+Ended",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77748,57 +77732,54 @@
                     "title": "Final Paid Transaction Database mdb file (via ftp)"
                 }
             ],
-            "spatial": "N/A",
-            "describedBy": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Transaction+Data+and+Reports",
-            "dataQuality": false,
+            "identifier": "DOT-10",
+            "issued": "2018-12-17",
+            "keyword": [
+                "cars",
+                "transactions"
+            ],
+            "landingPage": "https://data.transportation.gov/d/pq82-pyxa",
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
+            "title": "Car Allowance Rebate System (CARS) - Transactions"
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
-            "landingPage": "https://data.transportation.gov/d/pqqp-3qd3",
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
-            "identifier": "692.12",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - Pedestrian Fatal Crashes 2009-2012",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "primaryITInvestmentUII": "021-845083703",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77807,52 +77788,56 @@
                     "title": "Pedestrian Fatal Crashes 2009-2012"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.12",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/pqqp-3qd3",
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
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - Pedestrian Fatal Crashes 2009-2012"
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
-            "landingPage": "https://data.transportation.gov/d/pr3m-hsey",
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
-            "identifier": "99.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": false,
             "description": "Data collected through FMCSA's Licensing and Insurance programs and information collections (BOC-3, OP-1, etc).",
-            "title": "Licensing and Insurance - Licensing and Insurance",
-            "isPartOf": "DOT-99",
-            "agencyProgramURL": "http://li-public.fmcsa.dot.gov/",
-            "primaryITInvestmentUII": "021-000001001",
-            "programCode": [
-                "021:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -77861,31 +77846,45 @@
                     "title": "Licensing and Insurance"
                 }
             ],
-            "spatial": "Carrier, Driver",
-            "dataQuality": false,
+            "identifier": "99.1",
+            "isPartOf": "DOT-99",
+            "issued": "2018-12-17",
+            "keyword": [
+                "driver insurance; carrier registration; carrier license"
+            ],
+            "landingPage": "https://data.transportation.gov/d/pr3m-hsey",
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
+            "title": "Licensing and Insurance - Licensing and Insurance"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/prsc-k6eu",
-            "issued": "2021-04-07",
             "@type": "dcat:Dataset",
-            "modified": "2022-11-29",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Chambers",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "PPFSP '23",
+            "identifier": "https://data.transportation.gov/api/views/prsc-k6eu",
+            "issued": "2021-04-07",
             "keyword": [
                 "bureau",
                 "container",
@@ -77903,28 +77902,44 @@
                 "transportation",
                 "vessel"
             ],
-            "identifier": "https://data.transportation.gov/api/views/prsc-k6eu",
+            "landingPage": "https://data.transportation.gov/d/prsc-k6eu",
+            "modified": "2022-11-29",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "PPFSP '23",
             "title": "Air Draft & Channel Depths"
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
-            "landingPage": "https://data.transportation.gov/d/prsu-6i2a",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/07juntvt/07juntvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "June 2007"
+                }
             ],
+            "identifier": "18.87",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -77934,60 +77949,59 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.87",
+            "landingPage": "https://data.transportation.gov/d/prsu-6i2a",
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
-            "title": "Monthly Traffic Volume Trends - June 2007",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/07juntvt/07juntvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "June 2007"
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
+            "title": "Monthly Traffic Volume Trends - June 2007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/SafetyProgram/Review.aspx",
+            "agencyProgramURL": "http://www.fmcsa.dot.gov/safety-security/grants/New-Entrant/index.aspx, http://www.fmcsa.dot.gov/safety-security/grants/MCSAP-Basic-Incentive/index.aspx",
+            "analysisUnit": "Motor Carrier",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/psah-4yqx",
-            "issued": "2018-12-17",
-            "temporal": "2009-01-01/2013-12-31",
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
+            "description": "Contains data on compliance reviews and new entrant safety audits performed by FMCSA and State grantees.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://ai.fmcsa.dot.gov/SafetyProgram/Review.aspx",
+                    "mediaType": "text/html",
+                    "title": "Data Mining Tool"
+                }
             ],
+            "identifier": "DOT-95",
+            "issued": "2018-12-17",
             "keyword": [
                 "bus",
                 "compliance reviews",
@@ -78006,85 +78020,51 @@
                 "safety audits",
                 "safety rating"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "DOT-95",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
-            "description": "Contains data on compliance reviews and new entrant safety audits performed by FMCSA and State grantees.",
-            "title": "Motor Carrier Compliance Reviews and Safety Audits",
-            "agencyProgramURL": "http://www.fmcsa.dot.gov/safety-security/grants/New-Entrant/index.aspx, http://www.fmcsa.dot.gov/safety-security/grants/MCSAP-Basic-Incentive/index.aspx",
+            "landingPage": "https://data.transportation.gov/d/psah-4yqx",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-24",
+            "phone": "202-493-0215",
             "primaryITInvestmentUII": "021-000001005",
             "programCode": [
                 "021:020"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://ai.fmcsa.dot.gov/SafetyProgram/Review.aspx",
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
+            "title": "Motor Carrier Compliance Reviews and Safety Audits"
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
-            "landingPage": "https://data.transportation.gov/d/psn9-d3mi",
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
-            "identifier": "693.22",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
             "description": "The NBI System is the collection of bridge inspection information and costs associated with bridge replacements of structurally deficient bridges on and off the NHS. This data is collected under the auspices of the National Bridge Inspection Standards (NBIS) as prescribed by law. The NBI System collects the information that is used to determine eligibility for NHS projects, performance measure reporting, NHS penalty determination, and reporting to Congress.  It supports oversight of the NBIS through various report tools, and provides data reporting that supports agency strategic goals.",
-            "title": "National Bridge Inventory System (NBI) - 2013",
-            "isPartOf": "DOT-693",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
-            "primaryITInvestmentUII": "021-012940226",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78093,34 +78073,65 @@
                     "title": "2013"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
-            "dataQuality": true,
+            "identifier": "693.22",
+            "isPartOf": "DOT-693",
+            "issued": "1992-12-31",
+            "keyword": [
+                "bridge",
+                "condition",
+                "deck",
+                "inspection",
+                "structure"
+            ],
+            "landingPage": "https://data.transportation.gov/d/psn9-d3mi",
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
+            "title": "National Bridge Inventory System (NBI) - 2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.21949/1503761",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2012-11-30",
-            "@type": "dcat:Dataset",
-            "modified": "2017-06-21",
-            "references": [
-                "https://rosap.ntl.bts.gov/view/dot/3605"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Transportation Library Data Curator",
+                "hasEmail": "mailto:ntldatacurator@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The objective of this project was to develop technical relationships between reliability improvement strategies and reliability performance metrics. This project defined reliability, explained the importance of travel time distributions for measuring reliability, and recommended specific reliability performance measures. The research reexamined the contribution of the various causes of nonrecurring congestion on urban freeway sections, however, some attention was also given to rural highways and urban arterials). Numerous actions that can potentially reduce nonrecurring congestion were identified with an indication of their relative importance. Models for predicting nonrecurring congestion were developed using three methods, all based on empirical procedures: The first involved before and after studies; the second was termed a 'data poor' approach and resulted in a parsimonious and easy-to-apply set of models; the third was entitled a 'data rich model' and used cross-section inputs including data on selected factors known to directly affect nonrecurring congestion. An important conclusion of the study is that actions to improve operations, reduce demand, and increase capacity all can improve travel time reliability.  The 3 attached zip files contains comma separated value (.csv) files of data to support SHRP 2 report S2-L03-RR-1, Analytical procedures for determining the impacts of reliability mitigation strategies.Zip size is 1.83 MB. Files were accessed in Microsoft Excel 2016. Data will be preserved as is. To view publication see: https://rosap.ntl.bts.gov/view/dot/3605",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The objective of this project was to develop technical relationships between reliability improvement strategies and reliability performance metrics. This project defined reliability, explained the importance of travel time distributions for measuring reliability, and recommended specific reliability performance measures. The research reexamined the contribution of the various causes of nonrecurring congestion on urban freeway sections, however, some attention was also given to rural highways and urban arterials). Numerous actions that can potentially reduce nonrecurring congestion were identified with an indication of their relative importance. Models for predicting nonrecurring congestion were developed using three methods, all based on empirical procedures: The first involved before and after studies; the second was termed a 'data poor' approach and resulted in a parsimonious and easy-to-apply set of models; the third was entitled a 'data rich model' and used cross-section inputs including data on selected factors known to directly affect nonrecurring congestion. An important conclusion of the study is that actions to improve operations, reduce demand, and increase capacity all can improve travel time reliability.  The 3 attached zip files contains comma separated value (.csv) files of data to support SHRP 2 report S2-L03-RR-1, Analytical procedures for determining the impacts of reliability mitigation strategies.Zip size is 1.83 MB. Files were accessed in Microsoft Excel 2016. Data will be preserved as is. To view publication see: https://rosap.ntl.bts.gov/view/dot/3605",
+                    "downloadURL": "https://doi.org/10.21949/1503761",
+                    "mediaType": "application/zip",
+                    "title": "Analytical Procedures for Determining the Impacts of Reliability Mitigation Strategies [supporting datasets]"
+                }
             ],
+            "identifier": "https://data.transportation.gov/api/views/psu5-muct",
+            "issued": "2012-11-30",
             "keyword": [
                 "before and after studies",
                 "highways",
@@ -78137,51 +78148,56 @@
                 "travel time variability",
                 "uncertainty"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Transportation Library Data Curator",
-                "hasEmail": "mailto:ntldatacurator@dot.gov"
-            },
+            "landingPage": "https://doi.org/10.21949/1503761",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2017-06-21",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/psu5-muct",
-            "description": "The objective of this project was to develop technical relationships between reliability improvement strategies and reliability performance metrics. This project defined reliability, explained the importance of travel time distributions for measuring reliability, and recommended specific reliability performance measures. The research reexamined the contribution of the various causes of nonrecurring congestion on urban freeway sections, however, some attention was also given to rural highways and urban arterials). Numerous actions that can potentially reduce nonrecurring congestion were identified with an indication of their relative importance. Models for predicting nonrecurring congestion were developed using three methods, all based on empirical procedures: The first involved before and after studies; the second was termed a 'data poor' approach and resulted in a parsimonious and easy-to-apply set of models; the third was entitled a 'data rich model' and used cross-section inputs including data on selected factors known to directly affect nonrecurring congestion. An important conclusion of the study is that actions to improve operations, reduce demand, and increase capacity all can improve travel time reliability.  The 3 attached zip files contains comma separated value (.csv) files of data to support SHRP 2 report S2-L03-RR-1, Analytical procedures for determining the impacts of reliability mitigation strategies.Zip size is 1.83 MB. Files were accessed in Microsoft Excel 2016. Data will be preserved as is. To view publication see: https://rosap.ntl.bts.gov/view/dot/3605",
-            "title": "Analytical Procedures for Determining the Impacts of Reliability Mitigation Strategies [supporting datasets]",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://doi.org/10.21949/1503761",
-                    "description": "The objective of this project was to develop technical relationships between reliability improvement strategies and reliability performance metrics. This project defined reliability, explained the importance of travel time distributions for measuring reliability, and recommended specific reliability performance measures. The research reexamined the contribution of the various causes of nonrecurring congestion on urban freeway sections, however, some attention was also given to rural highways and urban arterials). Numerous actions that can potentially reduce nonrecurring congestion were identified with an indication of their relative importance. Models for predicting nonrecurring congestion were developed using three methods, all based on empirical procedures: The first involved before and after studies; the second was termed a 'data poor' approach and resulted in a parsimonious and easy-to-apply set of models; the third was entitled a 'data rich model' and used cross-section inputs including data on selected factors known to directly affect nonrecurring congestion. An important conclusion of the study is that actions to improve operations, reduce demand, and increase capacity all can improve travel time reliability.  The 3 attached zip files contains comma separated value (.csv) files of data to support SHRP 2 report S2-L03-RR-1, Analytical procedures for determining the impacts of reliability mitigation strategies.Zip size is 1.83 MB. Files were accessed in Microsoft Excel 2016. Data will be preserved as is. To view publication see: https://rosap.ntl.bts.gov/view/dot/3605",
-                    "@type": "dcat:Distribution",
-                    "title": "Analytical Procedures for Determining the Impacts of Reliability Mitigation Strategies [supporting datasets]"
-                }
+            "references": [
+                "https://rosap.ntl.bts.gov/view/dot/3605"
             ],
             "spatial": "United States",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "language": [
-                "en-US"
-            ]
+            "title": "Analytical Procedures for Determining the Impacts of Reliability Mitigation Strategies [supporting datasets]"
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
-            "landingPage": "https://data.transportation.gov/d/pswk-ekgs",
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
+                    "downloadURL": "http://go.usa.gov/kfQG",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Adjusted Data Release"
+                }
             ],
+            "identifier": "19.2",
+            "isPartOf": "DOT-19",
+            "issued": "2011-10-07",
             "keyword": [
                 "boardings",
                 "bus",
@@ -78191,74 +78207,43 @@
                 "train",
                 "transit"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John D. Giorgis",
-                "hasEmail": "mailto:john.giorgis@dot.gov"
-            },
-            "identifier": "19.2",
+            "landingPage": "https://data.transportation.gov/d/pswk-ekgs",
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
-            "title": "NTD Monthly Module Data Set - Adjusted Data Release",
-            "isPartOf": "DOT-19",
-            "agencyProgramURL": "http://www.ntdprogram.gov; http://www.ntdprogram.gov/ntdprogram/data.htm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://go.usa.gov/kfQG",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "Adjusted Data Release"
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
+            "title": "NTD Monthly Module Data Set - Adjusted Data Release"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ptrd-vf53",
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
-            "identifier": "https://data.transportation.gov/api/views/ptrd-vf53",
+            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
             "description": "State DOT will provide VMT. This data is summarized by Paved and Unpaved and by Vehicle Type.",
-            "title": "National Summaries 2019",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78266,48 +78251,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ptrd-vf53/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ptrd-vf53/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ptrd-vf53/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ptrd-vf53/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ptrd-vf53/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ptrd-vf53/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ptrd-vf53/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ptrd-vf53/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ptrd-vf53/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "USA",
-            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
+            "identifier": "https://data.transportation.gov/api/views/ptrd-vf53",
+            "issued": "2020-12-07",
+            "landingPage": "https://data.transportation.gov/d/ptrd-vf53",
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
+            "title": "National Summaries 2019"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/on_the_fly_download.aspx",
+            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
+            "analysisUnit": "57 Filing",
+            "bureauCode": [
+                "021:27"
+            ],
+            "categoryDesignation": "Research",
+            "collectionInstrument": "Transportation",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/DownloadFStructure.aspx",
+            "description": "This file contains reported cases of impacts between on-track equipment and any user of a public or private highway-rail intersection. National files from 1975 through the current year are available for download. In addition, individual files by State are available for the years 1991 through the current year.",
+            "distribution": [
                 {
-            "accessLevel": "public",
-            "bureauCode": [
-                "021:27"
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/on_the_fly_download.aspx",
+                    "mediaType": "text/plain",
+                    "title": "Highway-Rail Crossing Accident"
+                }
             ],
-            "landingPage": "https://data.transportation.gov/d/ptvy-p3tk",
+            "identifier": "DOT-214",
             "issued": "2010-09-29",
-            "temporal": "R/1975-01-31/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-09",
-            "collectionInstrument": "Transportation",
-            "references": [
-                "https://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Newregulation.aspx%3Fdoc=FRAGuideforPreparingAccIncReportspubMay2011.pdf"
-            ],
             "keyword": [
                 "accident",
                 "casualty",
@@ -78320,85 +78335,49 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "DOT-214",
+            "landingPage": "https://data.transportation.gov/d/ptvy-p3tk",
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
-            "title": "Highway Rail Accidents",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/on_the_fly_download.aspx",
-                    "mediaType": "text/plain",
-                    "title": "Highway-Rail Crossing Accident"
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
+            "title": "Highway Rail Accidents"
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
-            "landingPage": "https://data.transportation.gov/d/pvaj-2nvh",
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
-            "identifier": "524.5",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
             "description": "STATE DATA REPORTING SYSTEMS. Annual reports on the Fatality Analysis Reporting System (FARS) which is data regarding fatalities that is collected by a FARS analyst from each State and provided to NHTSA.",
-            "title": "GES Reports - 2003",
-            "isPartOf": "DOT-524",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78407,61 +78386,62 @@
                     "title": "2003"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
-            "dataQuality": true,
+            "identifier": "524.5",
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
+            "landingPage": "https://data.transportation.gov/d/pvaj-2nvh",
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
+            "title": "GES Reports - 2003"
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
-            "landingPage": "https://data.transportation.gov/d/pve6-prnz",
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
-            "identifier": "81.7",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Complaint information entered into NHTSA-ODI's vehicle owner's complaint database is used with other data sources to identify safety issues that warrant investigation and to determine if a safety-related defect trend exists. Complaint information is also analyzed to monitor existing recalls for proper scope and adequacy.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Complaints - Complaints Search",
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
@@ -78470,60 +78450,60 @@
                     "title": "Complaints Search"
                 }
             ],
-            "spatial": "N/A",
-            "describedBy": "http://www-odi.nhtsa.dot.gov/downloads/folders/Complaints/CMPL.txt",
-            "dataQuality": true,
+            "identifier": "81.7",
+            "isPartOf": "DOT-81",
+            "issued": "2002-12-16",
+            "keyword": [
+                "complaints",
+                "email",
+                "paper",
+                "phone",
+                "safercar.gov"
+            ],
+            "landingPage": "https://data.transportation.gov/d/pve6-prnz",
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
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Complaints - Complaints Search"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "https://portal.phmsa.dot.gov/ocfrTool/interpretations",
+            "agencyProgramURL": "https://portal.phmsa.dot.gov/ocfrTool/interpretations",
+            "analysisUnit": "Regulated Entity",
             "bureauCode": [
                 "021:50"
             ],
-            "landingPage": "https://data.transportation.gov/d/pwdf-sj2q",
-            "issued": "2011-01-18",
-            "temporal": "1995-01-01/2011-01-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-29",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "https://portal.phmsa.dot.gov/ocfrTool/interpretations"
-            ],
-            "keyword": [
-                "data.gov",
-                "hazardous materials",
-                "interpretation",
-                "law",
-                "safety",
-                "transportation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Eamonn Patrick",
                 "hasEmail": "mailto:eamonn.patrick@dot.gov"
             },
-            "identifier": "DOT-327",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Pipeline and Hazardous Materials Safety Administration"
-            },
+            "dataQuality": true,
             "description": "The Pipeline and Hazardous Materials Safety Administration, Office of Hazardous Materials Safety (OHMS) provides written clarifications of the Hazardous Materials Regulations (HMR; 49 CFR Parts 100-185) in the form of interpretation letters.  These letters reflect the agency's current application of the HMR to the specific facts presented by the person requesting the clarification.  Interpretations are one form of Guidance provided by OHMS.",
-            "title": "Hazardous Materials Safety Interpretations",
-            "agencyProgramURL": "https://portal.phmsa.dot.gov/ocfrTool/interpretations",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78531,31 +78511,69 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "DOT-327",
+            "issued": "2011-01-18",
+            "keyword": [
+                "data.gov",
+                "hazardous materials",
+                "interpretation",
+                "law",
+                "safety",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/pwdf-sj2q",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "https://portal.phmsa.dot.gov/ocfrTool/interpretations",
+            "modified": "2024-07-29",
+            "phone": "202-366-4308",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Pipeline and Hazardous Materials Safety Administration"
+            },
+            "references": [
+                "https://portal.phmsa.dot.gov/ocfrTool/interpretations"
+            ],
+            "temporal": "1995-01-01/2011-01-18",
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
+            "title": "Hazardous Materials Safety Interpretations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/pwgx-xzva",
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
+                    "description": "2012 Washington HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/washington2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Washington"
+                }
+            ],
+            "identifier": "678.101",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -78569,92 +78587,92 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.101",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Washington",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/pwgx-xzva",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/washington2012.zip",
-                    "description": "2012 Washington HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Washington"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Washington"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/pxc9-6ify",
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
-            "identifier": "https://data.transportation.gov/api/views/pxc9-6ify",
             "description": "Air carriers include scheduled and non-scheduled commercial passenger flights as well as cargo flights under FAR Part 121. The National Transportation Safety Board releases aviation fatality data in the Aviation Accident Database.",
-            "title": "Air Carrier Fatalities",
+            "identifier": "https://data.transportation.gov/api/views/pxc9-6ify",
+            "issued": "2025-01-03",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/pxc9-6ify",
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
+            "title": "Air Carrier Fatalities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/pxgs-mzu7",
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
+                    "description": "2013 Oklahoma HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/oklahoma2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Oklahoma"
+                }
+            ],
+            "identifier": "678.140",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -78668,78 +78686,40 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.140",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Oklahoma",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/pxgs-mzu7",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/oklahoma2013.zip",
-                    "description": "2013 Oklahoma HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Oklahoma"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Oklahoma"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/pxnz-pyjp",
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
-            "identifier": "https://data.transportation.gov/api/views/pxnz-pyjp",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 2002",
-            "title": "Historic HPMS Data (Sample) - 2002",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78747,119 +78727,154 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/pxnz-pyjp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/pxnz-pyjp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/pxnz-pyjp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/pxnz-pyjp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/pxnz-pyjp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/pxnz-pyjp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/pxnz-pyjp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/pxnz-pyjp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/pxnz-pyjp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/pxnz-pyjp",
+            "issued": "2022-07-08",
+            "keyword": [
+                "highway",
+                "highway performance monitoring",
+                "highway performance monitoring system",
+                "highways",
+                "hpms",
+                "sample"
+            ],
+            "landingPage": "https://data.transportation.gov/d/pxnz-pyjp",
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
+            "title": "Historic HPMS Data (Sample) - 2002"
         },
         {
-            "accessLevel": "public",
-            "bureauCode": [
-                "021:36"
-            ],
-            "landingPage": "https://data.transportation.gov/d/py8m-wb7u",
-            "issued": "2023-09-11",
             "@type": "dcat:Dataset",
-            "modified": "2024-09-11",
-            "keyword": [
-                "operating expenses",
-                "transit"
+            "accessLevel": "public",
+            "bureauCode": [
+                "021:36"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NTD Program Support",
                 "hasEmail": "mailto:NTDHelp@dot.gov"
             },
+            "description": "A summary of operating expenses applied to provide public transit as reported by transit agencies to the National Transit Database (NTD) in Report Year 2022.\r\n\r\nNTD Data Summaries organize and summarize data from the 2022 National Transit Database in a manner that is more useful for quick reference and summary analysis. \r\n\r\nThis summary is based on the 2022 Operating Expenses database file on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
+            "identifier": "https://data.transportation.gov/api/views/py8m-wb7u",
+            "issued": "2023-09-11",
+            "keyword": [
+                "operating expenses",
+                "transit"
+            ],
+            "landingPage": "https://data.transportation.gov/d/py8m-wb7u",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-09-11",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Department of Transportation"
             },
-            "identifier": "https://data.transportation.gov/api/views/py8m-wb7u",
-            "description": "A summary of operating expenses applied to provide public transit as reported by transit agencies to the National Transit Database (NTD) in Report Year 2022.\r\n\r\nNTD Data Summaries organize and summarize data from the 2022 National Transit Database in a manner that is more useful for quick reference and summary analysis. \r\n\r\nThis summary is based on the 2022 Operating Expenses database file on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
-            "title": "2022 NTD Data Summary - Operating Expenses",
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "2022 NTD Data Summary - Operating Expenses"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://datahub.transportation.gov/stories/s/pya5-6a78",
             "bureauCode": [
                 "021:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Weekly analytical reports to provide snapshots of near real-time information on traffic volume and gasoline product supplied.  Please direct all questions and comments to PolicyInfoFeedback@dot.gov.",
+            "identifier": "https://data.transportation.gov/api/views/pya5-6a78",
             "issued": "2020-09-22",
-            "@type": "dcat:Dataset",
-            "modified": "2022-06-01",
             "keyword": [
                 "fhwa",
                 "gasoline",
                 "travel",
                 "weekly"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
+            "landingPage": "https://datahub.transportation.gov/stories/s/pya5-6a78",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2022-06-01",
+            "programCode": [
+                "021:009"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/pya5-6a78",
-            "description": "Weekly analytical reports to provide snapshots of near real-time information on traffic volume and gasoline product supplied.  Please direct all questions and comments to PolicyInfoFeedback@dot.gov.",
-            "title": "Special Weekly Reports - Gasoline Product Supplied & Traffic Volume",
-            "programCode": [
-                "021:009"
-            ],
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Special Weekly Reports - Gasoline Product Supplied & Traffic Volume"
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
-            "landingPage": "https://data.transportation.gov/d/pyan-9tgk",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/08jultvt/08jultvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "July 2008"
+                }
             ],
+            "identifier": "18.74",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -78869,72 +78884,43 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.74",
+            "landingPage": "https://data.transportation.gov/d/pyan-9tgk",
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
-            "title": "Monthly Traffic Volume Trends - July 2008",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/08jultvt/08jultvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "July 2008"
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
+            "title": "Monthly Traffic Volume Trends - July 2008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/pydt-j7kj",
             "bureauCode": [
                 "021:04"
             ],
-            "rights": "Business-sensitive data has been removed from this dataset",
-            "issued": "2020-05-05",
-            "@type": "dcat:Dataset",
-            "temporal": "2017-01-01/2017-12-31",
-            "modified": "2020-07-07",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Janine McFadden",
                 "hasEmail": "mailto:janine.mcfadden@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statisitics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/pydt-j7kj",
+            "dataQuality": true,
             "description": "Reported 2017 calendar year ferry vessels as surveyed in the 2018 NCFO",
-            "title": "National Census of Ferry Operators (NCFO) 2018: Vessel data",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -78942,103 +78928,91 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/pydt-j7kj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/pydt-j7kj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/pydt-j7kj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/pydt-j7kj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/pydt-j7kj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/pydt-j7kj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/pydt-j7kj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/pydt-j7kj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/pydt-j7kj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S., U.S. Territories, and applicable Canadian providences",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/pydt-j7kj",
+            "issued": "2020-05-05",
+            "landingPage": "https://data.transportation.gov/d/pydt-j7kj",
             "license": "Other",
+            "modified": "2020-07-07",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statisitics"
+            },
+            "rights": "Business-sensitive data has been removed from this dataset",
+            "spatial": "U.S., U.S. Territories, and applicable Canadian providences",
+            "temporal": "2017-01-01/2017-12-31",
             "theme": [
                 "Ferry Transit"
-            ]
+            ],
+            "title": "National Census of Ferry Operators (NCFO) 2018: Vessel data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/pzph-cciz",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2020-05-28",
-            "temporal": "2017-01-01/2017-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-26",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Janine McFadden",
                 "hasEmail": "mailto:janine.mcfadden@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/pzph-cciz",
             "description": "Facts and figures on ferry terminals and segments",
-            "title": "National Census of Ferry Operators (NCFO) 2018: Ferry Terminals and Segments",
+            "identifier": "https://data.transportation.gov/api/views/pzph-cciz",
+            "issued": "2020-05-28",
+            "landingPage": "https://data.transportation.gov/d/pzph-cciz",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2021-07-26",
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
+            "title": "National Census of Ferry Operators (NCFO) 2018: Ferry Terminals and Segments"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/q3ms-nja6",
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
-                "probe data control message (pdcm)",
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
-            "identifier": "https://data.transportation.gov/api/views/q3ms-nja6",
+            "dataQuality": true,
             "description": "Contains all PDCMs generated during the AMCD field testing program. The PDCM is a control message sent from the server to OBUs to customize a request for Probe Vehicle Data (PVD) from the receiving OBU. All PDCMs are generated by the VCC Cloud server and transmitted to OBU clients through either a DSRC or cellular communications channel.",
-            "title": "Advanced Messaging Concept Development: Probe Data Control Message",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79046,71 +79020,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/q3ms-nja6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/q3ms-nja6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/q3ms-nja6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/q3ms-nja6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/q3ms-nja6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/q3ms-nja6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/q3ms-nja6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/q3ms-nja6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/q3ms-nja6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Tyson\u2019s Corner, Fairfax County, Virginia",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/q3ms-nja6",
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
+                "probe data control message (pdcm)",
+                "virginia tech transportation institute (vtti)"
+            ],
+            "landingPage": "https://data.transportation.gov/d/q3ms-nja6",
             "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "irregular",
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
+            "title": "Advanced Messaging Concept Development: Probe Data Control Message"
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
-            "landingPage": "https://data.transportation.gov/d/q4jk-fgxd",
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
-            "identifier": "692.8",
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
@@ -79119,49 +79100,50 @@
                     "title": "National Network Conventional Combination Trucks"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.8",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/q4jk-fgxd",
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
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://maps.dot.gov/fhwa/iit/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2024-03-27",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-23",
-            "keyword": [
-                "air",
-                "cost",
-                "hwy"
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
-            "identifier": "https://data.transportation.gov/api/views/q4t7-b6y5",
             "description": "This file contains the road segments from FHWA's HPMS dataset with estimates of the cost of air pollution from the traffic on that segment. The cost of air pollution is estimated using a combination of traffic volumes and speeds from FHWA's HPMS, the emission rate of PM2.5 from EPA's MOVES, the dispersion rate and pollutant concentration from EPA's AERMOD, the per unit health costs from a series of studies cited in EPA's COBRA, and the population affected from the US Census ACS 2019. The resulting cost per road segment is transformed into cost per 1/10 mile length of roadway and binned into 7 different categories to reduce the file size. For more information on this data please visit: https://maps.dot.gov/fhwa/iit/",
-            "title": "Inequity Identification Tool (IIT) Air Cost",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -79169,65 +79151,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
```

