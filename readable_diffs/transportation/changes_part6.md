# Change History for transportation.json (Part 6)

### Changes from 31606f9 to dd2190f (Part 5/9)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
                 "aadt",
                 "'fhwa",
@@ -52731,83 +52746,58 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.39",
+            "landingPage": "https://data.transportation.gov/d/g93w-3xqt",
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
-            "title": "Monthly Traffic Volume Trends - June 2012",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12juntvt/12juntvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "June 2012"
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
+            "title": "Monthly Traffic Volume Trends - June 2012"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ga2d-np8k",
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
             "identifier": "https://data.transportation.gov/api/views/ga2d-np8k",
+            "issued": "2024-05-10",
+            "landingPage": "https://data.transportation.gov/d/ga2d-np8k",
+            "modified": "2024-05-30",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "2022 NCFO Passenger and Vehicle Boarding Counts"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/gag3-mgv7",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/gag3-mgv7",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "Freight Stations",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52815,70 +52805,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/gag3-mgv7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gag3-mgv7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gag3-mgv7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/gag3-mgv7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gag3-mgv7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gag3-mgv7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/gag3-mgv7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gag3-mgv7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gag3-mgv7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/gag3-mgv7",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/gag3-mgv7",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Freight Stations"
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
-            "landingPage": "https://data.transportation.gov/d/gb52-4vsi",
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
-            "identifier": "DOT-303",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "Specific Federal Highway Administration Policy Statements",
-            "title": "Federal Highway Administration Policy Statements",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/foia/errpolicy.htm",
-            "primaryITInvestmentUII": "021-803057200",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52886,51 +52865,54 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "DOT-303",
+            "issued": "2011-01-18",
+            "keyword": [
+                "data.gov",
+                "highway",
+                "interpretation",
+                "law",
+                "policy",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/gb52-4vsi",
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
-            "analysisUnit": "Regulations",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4308",
-            "language": [
-                "en-US"
-            ]
+            "title": "Federal Highway Administration Policy Statements"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/gbe2-48iq",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2022-11-08",
-            "@type": "dcat:Dataset",
-            "temporal": "2017-2021",
-            "modified": "2022-12-20",
-            "keyword": [
-                "freight",
-                "freight facts & figures",
-                "rail",
-                "safety"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joseph McGill",
                 "hasEmail": "mailto:joseph.mcgill@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/gbe2-48iq",
+            "dataQuality": true,
             "description": "These are the count data for each type of Class III flammable liquid by each type of tank car, for each year. The data is based on information provided to the USDOT/Bureau of Transportation Statistics for the annual report: Fleet Compostion of Rail Tank Cars carrying Flammable Liquids.\n\nPreferred Citation:\nU.S. Department of Transportation, Bureau of Transportation Statistics, Fleet Composition of Rail Tank Cars Carrying Flammable Liquids: 2022 Report (Washington, DC: 2022). https://doi.org/10.21949/1527850",
-            "title": "Tank Car Data 2017-2021",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52938,52 +52920,85 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/gbe2-48iq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gbe2-48iq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gbe2-48iq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/gbe2-48iq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gbe2-48iq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gbe2-48iq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/gbe2-48iq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gbe2-48iq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gbe2-48iq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "This data set covers rail tank cars operating in the United States.",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/gbe2-48iq",
+            "issued": "2022-11-08",
+            "keyword": [
+                "freight",
+                "freight facts & figures",
+                "rail",
+                "safety"
+            ],
+            "landingPage": "https://data.transportation.gov/d/gbe2-48iq",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-12-20",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "spatial": "This data set covers rail tank cars operating in the United States.",
+            "temporal": "2017-2021",
             "theme": [
                 "Railroads"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Tank Car Data 2017-2021"
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
-            "landingPage": "https://data.transportation.gov/d/gbfj-925u",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/03maytvt/tvtmay03.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "May 2003"
+                }
             ],
+            "identifier": "18.136",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -52993,84 +53008,49 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.136",
+            "landingPage": "https://data.transportation.gov/d/gbfj-925u",
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
-            "title": "Monthly Traffic Volume Trends - May 2003",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/03maytvt/tvtmay03.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "May 2003"
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
+            "title": "Monthly Traffic Volume Trends - May 2003"
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
-            "landingPage": "https://data.transportation.gov/d/gbxz-3anw",
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
-            "identifier": "373.6",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": true,
             "description": "Each Freedom of Information Act office uses a case log to track FOIA requests. The logs typically include the dates on which requests were received and closed, control numbers, requester names and descriptions of the requested records.",
-            "title": "Freedom of Information Act Logs for the Office of the Secretary of Transportation - 2012",
-            "isPartOf": "DOT-373",
-            "agencyProgramURL": "http://www.dot.gov/foia",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -53079,35 +53059,70 @@
                     "title": "2012"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "373.6",
+            "isPartOf": "DOT-373",
+            "issued": "2007-12-31",
+            "keyword": [
+                "foia",
+                "freedom of information act",
+                "log",
+                "request"
+            ],
+            "landingPage": "https://data.transportation.gov/d/gbxz-3anw",
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
+            "title": "Freedom of Information Act Logs for the Office of the Secretary of Transportation - 2012"
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
-            "landingPage": "https://data.transportation.gov/d/gcsb-ti5h",
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
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/pubs/MonthlyData/S&STimeSeries-September2015-MajorOnly-160104.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Safety & Security Major-Only Time Series Data"
+                }
             ],
+            "identifier": "22.6",
+            "isPartOf": "DOT-22",
+            "issued": "2002-01-01",
             "keyword": [
                 "bicyclist",
                 "collision",
@@ -53126,55 +53141,44 @@
                 "transit",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John D. Giorgis",
-                "hasEmail": "mailto:john.giorgis@dot.gov"
-            },
-            "identifier": "22.6",
+            "landingPage": "https://data.transportation.gov/d/gcsb-ti5h",
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
-            "title": "NTD Safety & Security Summary Data Set - Safety & Security Major-Only Time Series Data",
-            "isPartOf": "DOT-22",
-            "agencyProgramURL": "http://www.ntdprogram.gov/",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/pubs/MonthlyData/S&STimeSeries-September2015-MajorOnly-160104.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "Safety & Security Major-Only Time Series Data"
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
+            "title": "NTD Safety & Security Summary Data Set - Safety & Security Major-Only Time Series Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:36"
             ],
-            "landingPage": "https://data.transportation.gov/d/gd62-jzra",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NTD Program Support",
+                "hasEmail": "mailto:NTDHelp@dot.gov"
+            },
+            "description": "A national summary of facilities and stations based on data reported by transit agencies to the National Transit Database (NTD) in Report Year 2023.\r\n\r\nNTD Data Summaries organize and summarize data from the 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis.\r\n\r\nThis summary is based on the 2023 Facility Inventory, Transit Facilities, and Transit Stations files on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
+            "identifier": "https://data.transportation.gov/api/views/gd62-jzra",
             "issued": "2024-10-17",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-17",
             "keyword": [
                 "maintenance facilities",
                 "passenger terminals",
@@ -53182,59 +53186,37 @@
                 "stations",
                 "transit"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NTD Program Support",
-                "hasEmail": "mailto:NTDHelp@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/gd62-jzra",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-10-17",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Transit Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/gd62-jzra",
-            "description": "A national summary of facilities and stations based on data reported by transit agencies to the National Transit Database (NTD) in Report Year 2023.\r\n\r\nNTD Data Summaries organize and summarize data from the 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis.\r\n\r\nThis summary is based on the 2023 Facility Inventory, Transit Facilities, and Transit Stations files on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
-            "title": "2023 NTD Annual Data Summary - Facilities and Stations",
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "2023 NTD Annual Data Summary - Facilities and Stations"
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
-            "landingPage": "https://data.transportation.gov/d/gfmg-umzq",
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
-            "identifier": "364.19",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2001",
-            "isPartOf": "DOT-364",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
-            "primaryITInvestmentUII": "021-621341357",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -53243,35 +53225,68 @@
                     "title": "Event Data Records Reports - 2001"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.nhtsa.gov",
-            "theme": [
-                "Transportation"
+            "identifier": "364.19",
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
+            "landingPage": "https://data.transportation.gov/d/gfmg-umzq",
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
+            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2001"
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
-            "landingPage": "https://data.transportation.gov/d/gft8-5xx4",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/11jultvt/11jultvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "July 2011"
+                }
             ],
+            "identifier": "18.8",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -53281,78 +53296,42 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.8",
+            "landingPage": "https://data.transportation.gov/d/gft8-5xx4",
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
-            "title": "Monthly Traffic Volume Trends - July 2011",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/11jultvt/11jultvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "July 2011"
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
+            "title": "Monthly Traffic Volume Trends - July 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ggca-ddee",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2022-04-26",
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
-            "identifier": "https://data.transportation.gov/api/views/ggca-ddee",
             "description": "This is the Operator Segment file for the 2020 National Census of Ferry Operators. It is one of five data sets that make up the 2020 NCFO",
-            "title": "2020 NCFO Operator Segment File",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -53360,72 +53339,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ggca-ddee/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ggca-ddee/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ggca-ddee/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ggca-ddee/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ggca-ddee/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ggca-ddee/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ggca-ddee/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ggca-ddee/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ggca-ddee/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/ggca-ddee",
+            "issued": "2022-04-26",
+            "keyword": [
+                "ferry",
+                "ferry operators",
+                "ferry transit",
+                "passenger ferry",
+                "transportation",
+                "water transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ggca-ddee",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2022-04-28",
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
+            "title": "2020 NCFO Operator Segment File"
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
-            "landingPage": "https://data.transportation.gov/d/ggig-xnj8",
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
-            "identifier": "1840.6",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/veh/vehdb-export-fields.htm",
             "description": "The NHTSA Vehicle Crash Test Database contains engineering data measured during various types of research, the New Car Assessment Program (NCAP), and compliance crash tests. Information in this database refers to the performance and response of vehicles and other structures in impacts. This database is not intended to support general consumer safety issues. For general consumer information please see the NHTSA's information on buying a safer car.",
-            "title": "Vehicle Crash Test Database - Query by Test Parameters",
-            "isPartOf": "DOT-1840",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research",
-            "primaryITInvestmentUII": "021-961265599",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -53434,31 +53412,71 @@
                     "title": "Query by Test Parameters"
                 }
             ],
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/veh/vehdb-export-fields.htm",
-            "dataQuality": true,
+            "identifier": "1840.6",
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
+            "landingPage": "https://data.transportation.gov/d/ggig-xnj8",
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
+            "title": "Vehicle Crash Test Database - Query by Test Parameters"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/ggpn-exi9",
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
+                    "description": "2013 Maine HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/maine2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Maine"
+                }
+            ],
+            "identifier": "678.123",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -53472,60 +53490,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.123",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Maine",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/ggpn-exi9",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/maine2013.zip",
-                    "description": "2013 Maine HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Maine"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Maine"
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
-            "landingPage": "https://data.transportation.gov/d/ghfk-rfay",
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
+            "identifier": "DOT-2",
+            "issued": "2008-02-01",
             "keyword": [
                 "child",
                 "css",
@@ -53535,60 +53550,61 @@
                 "safety",
                 "seat"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "DOT-2",
+            "landingPage": "https://data.transportation.gov/d/ghfk-rfay",
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
-            "title": "Child Safety Seat Ease of Use Rating",
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
+            "title": "Child Safety Seat Ease of Use Rating"
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
-            "landingPage": "https://data.transportation.gov/d/ghnm-qngp",
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
+                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/nits/Noncrash%20fatalities/2005-2007/2005-2007%20Noncrash%20Fatalities.xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2005-2007 Noncrash Fatalities"
+                }
             ],
+            "identifier": "288.12",
+            "isPartOf": "DOT-288",
+            "issued": "2009-01-27",
             "keyword": [
                 "crash",
                 "death",
@@ -53604,83 +53620,51 @@
                 "vehicle",
                 "victim"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "288.12",
+            "landingPage": "https://data.transportation.gov/d/ghnm-qngp",
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
-            "title": "Not in Traffic Surveillance (NiTS) - 2005-2007 Noncrash Fatalities",
-            "isPartOf": "DOT-288",
-            "agencyProgramURL": "http://www.nhtsa.gov/Data/State+Data+Programs",
-            "programCode": [
-                "021:032"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/nits/Noncrash%20fatalities/2005-2007/2005-2007%20Noncrash%20Fatalities.xlsx",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "2005-2007 Noncrash Fatalities"
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
+            "title": "Not in Traffic Surveillance (NiTS) - 2005-2007 Noncrash Fatalities"
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
-            "landingPage": "https://data.transportation.gov/d/gi6c-njta",
-            "issued": "2013-02-01",
-            "temporal": "R/2012-01-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
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
-            "identifier": "DOT-372",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
-            "description": "The FOIA requires each federal agency to submit an Annual Report to the Attorney General each year. These reports contain detailed statistics on the numbers of requests received and processed by each agency, the time taken to respond, and the outcome of each request, as well as many other vital statistics regarding the administration of the FOIA at federal departments and agencies.",
-            "title": "Freedom of Information Act Annual Report",
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
@@ -53689,50 +53673,50 @@
                     "title": "2012 Report"
                 }
             ],
-            "spatial": "not applicable",
-            "describedBy": "http://www.justice.gov/oip/docs/doj-handbook-for-agency-annual-freedom-of-information-act-reports.pdf",
-            "dataQuality": true,
+            "identifier": "DOT-372",
+            "issued": "2013-02-01",
+            "keyword": [
+                "backlog",
+                "freedom of information act",
+                "requests"
+            ],
+            "landingPage": "https://data.transportation.gov/d/gi6c-njta",
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
+            "title": "Freedom of Information Act Annual Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/gjfe-peac",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2021-06-30",
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
-            "identifier": "https://data.transportation.gov/api/views/gjfe-peac",
+            "dataQuality": true,
             "description": "2015 Traffic Volume Data - FHWA's TMAS Data Program (based on unweighted raw continuous traffic count information collected by state highway agencies)",
-            "title": "TMAS 2015",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -53740,66 +53724,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/gjfe-peac/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gjfe-peac/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gjfe-peac/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/gjfe-peac/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gjfe-peac/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gjfe-peac/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/gjfe-peac/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gjfe-peac/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gjfe-peac/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/gjfe-peac",
+            "issued": "2021-06-30",
+            "keyword": [
+                "traffic",
+                "traffic volume trends"
+            ],
+            "landingPage": "https://data.transportation.gov/d/gjfe-peac",
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
+            "title": "TMAS 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/gjp5-nh2u",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2024-10-17",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
-            "keyword": [
-                "air carriers",
-                "airfare",
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
-            "identifier": "https://data.transportation.gov/api/views/gjp5-nh2u",
             "description": "Average domestic market air fare by carrier.",
-            "title": "AFF - Average Air Fare by Carrier",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -53807,43 +53789,79 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/gjp5-nh2u/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gjp5-nh2u/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gjp5-nh2u/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/gjp5-nh2u/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gjp5-nh2u/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gjp5-nh2u/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/gjp5-nh2u/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gjp5-nh2u/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gjp5-nh2u/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/gjp5-nh2u",
+            "issued": "2024-10-17",
+            "keyword": [
+                "air carriers",
+                "airfare",
+                "aviation facts & figures"
+            ],
+            "landingPage": "https://data.transportation.gov/d/gjp5-nh2u",
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
+            "title": "AFF - Average Air Fare by Carrier"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/gjyq-hk8t",
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
+                    "description": "2012 Tennessee HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/tennessee2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Tennessee"
+                }
+            ],
+            "identifier": "678.96",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -53857,82 +53875,45 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.96",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Tennessee",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/gjyq-hk8t",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/tennessee2012.zip",
-                    "description": "2012 Tennessee HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Tennessee"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Tennessee"
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
-            "landingPage": "https://data.transportation.gov/d/gktv-x5cr",
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
-            "identifier": "692.18",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - 2010 Fatal Crashes",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "primaryITInvestmentUII": "021-845083703",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -53941,59 +53922,58 @@
                     "title": "2010 Fatal Crashes"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.18",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/gktv-x5cr",
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
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - 2010 Fatal Crashes"
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
-            "landingPage": "https://data.transportation.gov/d/gkz9-nr9w",
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
-            "identifier": "693.10",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
             "description": "The NBI System is the collection of bridge inspection information and costs associated with bridge replacements of structurally deficient bridges on and off the NHS. This data is collected under the auspices of the National Bridge Inspection Standards (NBIS) as prescribed by law. The NBI System collects the information that is used to determine eligibility for NHS projects, performance measure reporting, NHS penalty determination, and reporting to Congress.  It supports oversight of the NBIS through various report tools, and provides data reporting that supports agency strategic goals.",
-            "title": "National Bridge Inventory System (NBI) - 2001",
-            "isPartOf": "DOT-693",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
-            "primaryITInvestmentUII": "021-012940226",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -54002,52 +53982,53 @@
                     "title": "2001"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
-            "dataQuality": true,
+            "identifier": "693.10",
+            "isPartOf": "DOT-693",
+            "issued": "1992-12-31",
+            "keyword": [
+                "bridge",
+                "condition",
+                "deck",
+                "inspection",
+                "structure"
+            ],
+            "landingPage": "https://data.transportation.gov/d/gkz9-nr9w",
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
+            "title": "National Bridge Inventory System (NBI) - 2001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/gm5m-aghp",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-26",
-            "keyword": [
-                "maintenance facilities",
-                "passenger facilities",
-                "public transit",
-                "transit administrative facilities",
-                "transit facilities",
-                "transit parking facilities",
-                "transit stations"
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
-            "identifier": "https://data.transportation.gov/api/views/gm5m-aghp",
             "description": "The Facility Inventory dataset details all facilities supporting public transit service as reported to the National Transit Database (NTD) by each public transit agency in the 2023 report year.\n\nThis file is also published at https://www.transit.dot.gov/ntd/ntd-data, under the Product Type of \"Annual Database (Excel).\" Equivalent datasets from 2018 through 2022 can also be found using that link.\nIf you have any other questions about this table, please contact the NTD Help Desk at NTDHelp@dot.gov.",
-            "title": "2023 NTD Annual Data - Facility Inventory",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -54055,41 +54036,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/gm5m-aghp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gm5m-aghp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gm5m-aghp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/gm5m-aghp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gm5m-aghp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gm5m-aghp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/gm5m-aghp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gm5m-aghp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gm5m-aghp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/gm5m-aghp",
+            "issued": "2024-09-10",
+            "keyword": [
+                "maintenance facilities",
+                "passenger facilities",
+                "public transit",
+                "transit administrative facilities",
+                "transit facilities",
+                "transit parking facilities",
+                "transit stations"
+            ],
+            "landingPage": "https://data.transportation.gov/d/gm5m-aghp",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-26",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Transit Administration"
+            },
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "2023 NTD Annual Data - Facility Inventory"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/gm7w-zhdc",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Theresa Firestine",
+                "hasEmail": "mailto:theresa.firestine@dot.gov"
+            },
+            "description": "Page describes the U.S. Department of Transportation, Bureau of Transportation Statistics' Transportation Satellite Accounts (TSA), which measure the contribution of for-hire and in-house transportation to the economy.",
+            "identifier": "https://data.transportation.gov/api/views/gm7w-zhdc",
             "issued": "2020-12-15",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-07",
             "keyword": [
                 "economics",
                 "for-hire transportation",
@@ -54102,40 +54106,52 @@
                 "tsa",
                 "value added"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Theresa Firestine",
-                "hasEmail": "mailto:theresa.firestine@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/gm7w-zhdc",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-01-07",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/gm7w-zhdc",
-            "description": "Page describes the U.S. Department of Transportation, Bureau of Transportation Statistics' Transportation Satellite Accounts (TSA), which measure the contribution of for-hire and in-house transportation to the economy.",
-            "title": "Transportation Satellite Accounts for TRB",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Transportation Satellite Accounts for TRB"
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
-            "landingPage": "https://data.transportation.gov/d/gmqv-khu7",
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
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/on_the_fly_download.aspx",
+                    "mediaType": "text/plain",
+                    "title": "Highway-Rail Crossing Accident"
+                }
             ],
+            "identifier": "214.1",
+            "isPartOf": "DOT-214",
+            "issued": "2010-09-29",
             "keyword": [
                 "accident",
                 "casualty",
@@ -54148,111 +54164,77 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "214.1",
+            "landingPage": "https://data.transportation.gov/d/gmqv-khu7",
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
-            "title": "Highway Rail Accidents - Highway-Rail Crossing Accident",
-            "isPartOf": "DOT-214",
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
+            "title": "Highway Rail Accidents - Highway-Rail Crossing Accident"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/gmwv-css9",
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
-            "identifier": "https://data.transportation.gov/api/views/gmwv-css9",
             "description": "The Bureau of Transportation Statistics releases seasonally adjusted air traffic data based on monthly reports from commercial U.S. air carriers.",
-            "title": "Air Travel - Total - Seasonally Adjusted",
+            "identifier": "https://data.transportation.gov/api/views/gmwv-css9",
+            "issued": "2025-01-16",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/gmwv-css9",
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
+            "title": "Air Travel - Total - Seasonally Adjusted"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/gmxu-awv7",
             "bureauCode": [
                 "021:17"
             ],
-            "issued": "2023-12-08",
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
-            "identifier": "https://data.transportation.gov/api/views/gmxu-awv7",
             "description": "Records for each BOC3 agent hired by a carrier/broker/freight forwarder. Each entity must hire a BOC3 agent to represent them in legal matters to obtain operating authority. In some cases, entities may act as their own BOC3 agent. The records in the dataset contain the BOC3 agent\u2019s name and address. The dataset also contains the DOT number and docket number of the represented entity.  See dataset attachment \"FMCSA Dataset Description and Data Definitions - Select Datasets\" for more information.",
-            "title": "BOC3 - All With History",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -54260,46 +54242,43 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/gmxu-awv7",
+            "issued": "2023-12-08",
+            "keyword": [
+                "boc3",
+                "motor carrier",
+                "process agent"
+            ],
+            "landingPage": "https://data.transportation.gov/d/gmxu-awv7",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
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
+            "title": "BOC3 - All With History"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/gn77-pp24",
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
-            "identifier": "https://data.transportation.gov/api/views/gn77-pp24",
-            "description": "This is the Segments file for the 2020 National Census of Ferry Operators. It is one of five data sets that make up the 2020 NCFO",
-            "title": "2020 NCFO Segments File",
-            "programCode": [
-                "021:053"
-            ],
+            "description": "This is the Segments file for the 2020 National Census of Ferry Operators. It is one of five data sets that make up the 2020 NCFO",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -54307,46 +54286,82 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/gn77-pp24/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gn77-pp24/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gn77-pp24/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/gn77-pp24/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gn77-pp24/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gn77-pp24/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/gn77-pp24/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gn77-pp24/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gn77-pp24/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/gn77-pp24",
+            "issued": "2022-04-01",
+            "keyword": [
+                "ferry",
+                "ferry operators",
+                "ferry transit",
+                "passenger ferry",
+                "transportation",
+                "water transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/gn77-pp24",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2022-04-28",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Maritime and Waterways"
-            ]
+            ],
+            "title": "2020 NCFO Segments File"
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
-            "landingPage": "https://data.transportation.gov/d/gnfc-hzrg",
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
+                    "mediaType": "application/jsv",
+                    "title": "New Car Assessment Program (NCAP) - 5 Star Safety Ratings"
+                }
             ],
+            "identifier": "248.4",
+            "isPartOf": "DOT-248",
+            "issued": "2010-01-05",
             "keyword": [
                 "5",
                 "assessment",
@@ -54360,84 +54375,49 @@
                 "safety",
                 "star"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "248.4",
+            "landingPage": "https://data.transportation.gov/d/gnfc-hzrg",
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
-                    "mediaType": "application/jsv",
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
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://www.nhtsa.gov/cps/cpsfitting/index.cfm",
+            "agencyProgramURL": "http://www.nhtsa.gov/cps/cpsfitting/index.cfm",
+            "analysisUnit": "N/A",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/gngh-v4cw",
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
-            "identifier": "80.5",
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
@@ -54446,33 +54426,66 @@
                     "title": "Child Car Seat Inspection Station Locator"
                 }
             ],
-            "spatial": "Zip, State, Geo co-ordinates",
-            "dataQuality": false,
+            "identifier": "80.5",
+            "isPartOf": "DOT-80",
+            "issued": "2010-01-05",
+            "keyword": [
+                "child seat",
+                "inspection",
+                "safety",
+                "station",
+                "stations"
+            ],
+            "landingPage": "https://data.transportation.gov/d/gngh-v4cw",
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
             "accessLevel": "non-public",
-            "rights": "Data set contains controlled unclassified information (Draft rules and polices). Some public reports are available.",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/gnz8-5zuh",
-            "issued": "2018-12-18",
-            "temporal": "R/2013-01-01/P1Y",
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
+            "description": "RMS is a DOT-wide system developed for the Office of the General Counsel (OGC) to track the status of rulemakings, document required concurrences, serve as a repository for documents under development, and generate management and compliance reports from the data within the system.  The system allows senior leaders throughout DOT to identify not only the status of rulemakings, but areas where steps can be taken to streamline rulemaking operations at DOT.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.dot.gov/regulations/effects-report-archive",
+                    "mediaType": "text/html",
+                    "title": "Public Effects Reports"
+                }
+            ],
+            "identifier": "DOT-458",
+            "issued": "2018-12-18",
             "keyword": [
                 "economically significant",
                 "effects",
@@ -54495,75 +54508,46 @@
                 "tribalism",
                 "unfunded mandate"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DOT Socrata",
-                "hasEmail": "mailto:Socrata@dot.gov"
-            },
-            "identifier": "DOT-458",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
-            "description": "RMS is a DOT-wide system developed for the Office of the General Counsel (OGC) to track the status of rulemakings, document required concurrences, serve as a repository for documents under development, and generate management and compliance reports from the data within the system.  The system allows senior leaders throughout DOT to identify not only the status of rulemakings, but areas where steps can be taken to streamline rulemaking operations at DOT.",
-            "title": "Rulemaking Management System (RMS)",
+            "landingPage": "https://data.transportation.gov/d/gnz8-5zuh",
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
+            "title": "Rulemaking Management System (RMS)"
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
-            "landingPage": "https://data.transportation.gov/d/gpyv-jjdk",
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
-            "identifier": "DOT-713",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": false,
             "description": "Open Source Application Development Portal (OSADP). The system provides a place for programmers to share software code and solutions.",
-            "title": "Open Source Application  Development Portal",
-            "agencyProgramURL": "http://www.its.dot.gov/dma/",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -54572,81 +54556,70 @@
                     "title": "Website"
                 }
             ],
-            "dataQuality": false,
+            "identifier": "DOT-713",
+            "issued": "2014-09-15",
+            "keyword": [
+                "code",
+                "open source",
+                "research"
+            ],
+            "landingPage": "https://data.transportation.gov/d/gpyv-jjdk",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
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
-            "agencyDataSeriesURL": "http://www.itsforge.net",
-            "categoryDesignation": "Research",
-            "phone": "202-366-6993",
-            "language": [
-                "en-US"
-            ]
+            "title": "Open Source Application  Development Portal"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/gqat-kmi3",
-            "issued": "2022-03-10",
             "@type": "dcat:Dataset",
-            "modified": "2022-09-20",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/gqat-kmi3",
+            "issued": "2022-03-10",
+            "landingPage": "https://data.transportation.gov/d/gqat-kmi3",
+            "modified": "2022-09-20",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
-            "title": "Industry and Workers",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "Industry and Workers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/gr7j-n2cj",
+            "accrualPeriodicity": "R/PT0.1S",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2015-11-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2014-10-21/2015-03-04",
-            "modified": "2015-11-01",
-            "keyword": [
-                "anthem",
-                "arizona",
-                "connected equipment",
-                "field test",
-                "freight",
-                "freight signal priority (fsp)",
-                "intelligent transportation systems (its)",
-                "i-sig",
-                "its joint program office (jpo)",
-                "multi-modal intelligent traffic signal system (mmitss)",
-                "roadside equipment (rse)",
-                "signal phase and timing (spat)",
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
-            "identifier": "https://data.transportation.gov/api/views/gr7j-n2cj",
+            "dataQuality": true,
             "description": "Data were collected during the Multi-Modal Intelligent Transportation Signal Systems (MMITSS) study. MMITSS is a next-generation traffic signal system that seeks to provide a comprehensive traffic information framework to service all modes of transportation.The Signal Plans for Roadside Equipment (RSE) data contains the basics of a Signal Phase and Timing (SPAT) message. This data includes SPAT message and the timestamp of the SPAT message. The data also provides the signal phase and timing information for one or more movements at an intersection.",
-            "title": "Multi-Modal Intelligent Traffic Signal Systems Signal Plans for Roadside Equipment",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -54654,109 +54627,117 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/gr7j-n2cj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gr7j-n2cj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gr7j-n2cj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/gr7j-n2cj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gr7j-n2cj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gr7j-n2cj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/gr7j-n2cj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gr7j-n2cj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gr7j-n2cj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Anthem, Arizona",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/gr7j-n2cj",
+            "issued": "2015-11-01",
+            "keyword": [
+                "anthem",
+                "arizona",
+                "connected equipment",
+                "field test",
+                "freight",
+                "freight signal priority (fsp)",
+                "intelligent transportation systems (its)",
+                "i-sig",
+                "its joint program office (jpo)",
+                "multi-modal intelligent traffic signal system (mmitss)",
+                "roadside equipment (rse)",
+                "signal phase and timing (spat)",
+                "transit signal priority (tsp)"
+            ],
+            "landingPage": "https://data.transportation.gov/d/gr7j-n2cj",
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
+            "temporal": "2014-10-21/2015-03-04",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Multi-Modal Intelligent Traffic Signal Systems Signal Plans for Roadside Equipment"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/gr9y-9gjq",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Access to intercity transportation in rural areas. Interactive map and graphs with data available for different time periods.",
+            "identifier": "https://data.transportation.gov/api/views/gr9y-9gjq",
             "issued": "2019-12-16",
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
+            "landingPage": "https://data.transportation.gov/d/gr9y-9gjq",
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
-            "identifier": "https://data.transportation.gov/api/views/gr9y-9gjq",
-            "description": "Access to intercity transportation in rural areas. Interactive map and graphs with data available for different time periods.",
-            "title": "Rural Access to Intercity Transportation",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Rural Access to Intercity Transportation"
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
-            "landingPage": "https://data.transportation.gov/d/greq-yjg6",
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
-            "identifier": "696.10",
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
@@ -54765,33 +54746,67 @@
                     "title": "General Highway History"
                 }
             ],
-            "spatial": "National",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "696.10",
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
+            "landingPage": "https://data.transportation.gov/d/greq-yjg6",
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
-            "landingPage": "https://data.transportation.gov/d/gs9i-3f25",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/04martvt/04martvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "March 2004"
+                }
             ],
+            "identifier": "18.126",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -54801,60 +54816,59 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.126",
+            "landingPage": "https://data.transportation.gov/d/gs9i-3f25",
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
-            "title": "Monthly Traffic Volume Trends - March 2004",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/04martvt/04martvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "March 2004"
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
+            "title": "Monthly Traffic Volume Trends - March 2004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "https://www.phmsa.dot.gov/approvals-and-permits/hazmat/approvals-search",
+            "agencyProgramURL": "http://www.phmsa.dot.gov/hazmat/regs/sp-a/approvals",
+            "analysisUnit": "Approval",
             "bureauCode": [
                 "021:50"
             ],
-            "landingPage": "https://data.transportation.gov/d/gsii-b55p",
-            "issued": "2012-01-18",
-            "temporal": "R/1980-01-01/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-29",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "https://www.phmsa.dot.gov/approvals-and-permits/hazmat/approvals-search"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Donald Burger",
+                "hasEmail": "mailto:donald.burger@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Pipeline and Hazardous Materials Safety Administration has the primary responsibility for the issuance of DOT Special Permits and Approvals to the Hazardous Materials Regulations (HMR). A Special Permit or Approval is a document which authorizes a person to perform a function that is not currently authorized under the authority of the HMR. Also, in many instances, the Regulations require approvals and/or registrations prior to transportation in commerce.  Approvals Data Search tool allows a user to search for Approvals.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://hazmatonline.phmsa.dot.gov/ApprovalsSearch/",
+                    "mediaType": "text/html",
+                    "title": "Data Mining Tool"
+                }
             ],
+            "identifier": "DOT-30",
+            "issued": "2012-01-18",
             "keyword": [
                 "approvals",
                 "competent authority",
@@ -54865,59 +54879,60 @@
                 "packaging labs",
                 "special permits"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Donald Burger",
-                "hasEmail": "mailto:donald.burger@dot.gov"
-            },
-            "identifier": "DOT-30",
+            "landingPage": "https://data.transportation.gov/d/gsii-b55p",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-07-29",
+            "phone": "202-493-0550",
+            "programCode": [
+                "021:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Pipeline and Hazardous Materials Safety Administration"
             },
-            "description": "The Pipeline and Hazardous Materials Safety Administration has the primary responsibility for the issuance of DOT Special Permits and Approvals to the Hazardous Materials Regulations (HMR). A Special Permit or Approval is a document which authorizes a person to perform a function that is not currently authorized under the authority of the HMR. Also, in many instances, the Regulations require approvals and/or registrations prior to transportation in commerce.  Approvals Data Search tool allows a user to search for Approvals.",
-            "title": "Hazmat Approvals",
-            "agencyProgramURL": "http://www.phmsa.dot.gov/hazmat/regs/sp-a/approvals",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://hazmatonline.phmsa.dot.gov/ApprovalsSearch/",
-                    "mediaType": "text/html",
-                    "title": "Data Mining Tool"
-                }
+            "references": [
+                "https://www.phmsa.dot.gov/approvals-and-permits/hazmat/approvals-search"
             ],
             "spatial": "Address",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "https://www.phmsa.dot.gov/approvals-and-permits/hazmat/approvals-search",
+            "temporal": "R/1980-01-01/P1D",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "analysisUnit": "Approval",
-            "categoryDesignation": "Research",
-            "phone": "202-493-0550",
-            "language": [
-                "en-US"
-            ]
+            "title": "Hazmat Approvals"
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
-            "landingPage": "https://data.transportation.gov/d/gsqt-64vp",
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
+            "identifier": "116.2",
+            "isPartOf": "DOT-116",
+            "issued": "2018-12-17",
             "keyword": [
                 "bus",
                 "federal motor carrier safety administration",
@@ -54935,98 +54950,73 @@
                 "sms",
                 "vehicles"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "116.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
-            "description": "This Web site is designed to inform passenger carriers and the traveling public about the Federal Motor Carrier Safety Administration's passenger carrier program and regulations.",
-            "title": "A&I - Bus/Passenger Carrier Information - Data Mining Tool",
-            "isPartOf": "DOT-116",
-            "agencyProgramURL": "http://www.fmcsa.dot.gov/safety-security/pcs/Index.aspx",
+            "landingPage": "https://data.transportation.gov/d/gsqt-64vp",
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
-            "landingPage": "https://data.transportation.gov/d/gsyp-spgc",
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
-            "identifier": "https://data.transportation.gov/api/views/gsyp-spgc",
             "description": "Average air fares by quarter, airport and air carrier.",
-            "title": "Air Fares",
+            "identifier": "https://data.transportation.gov/api/views/gsyp-spgc",
+            "issued": "2024-07-05",
+            "keyword": [
+                "aff",
+                "aviation facts & figures"
+            ],
+            "landingPage": "https://data.transportation.gov/d/gsyp-spgc",
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
+            "title": "Air Fares"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/gtin-v2za",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/gtin-v2za",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "FRA Regions",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55034,45 +55024,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/gtin-v2za/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gtin-v2za/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gtin-v2za/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/gtin-v2za/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gtin-v2za/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gtin-v2za/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/gtin-v2za/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gtin-v2za/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gtin-v2za/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/gtin-v2za",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/gtin-v2za",
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
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/gts8-2nar",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12martvt/12martvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "March 2012"
+                }
             ],
+            "identifier": "18.36",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -55082,88 +55097,43 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.36",
+            "landingPage": "https://data.transportation.gov/d/gts8-2nar",
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
-            "title": "Monthly Traffic Volume Trends - March 2012",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12martvt/12martvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "March 2012"
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
+            "title": "Monthly Traffic Volume Trends - March 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.its.dot.gov/pilots/pilots_nycdot.htm",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2022-09-30",
-            "temporal": "2021-01/P12M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
-            "keyword": [
-                "aftermarket safety device (asd)",
-                "arterial",
-                "basic safety message (bsm)",
-                "connected vehicle message",
-                "connected vehicle pilot (cvp)",
-                "field test",
-                "independent evaluation",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "new york city department of transportation (nycdot)",
-                "roadside equipment (rse)",
-                "signal phase and timing (spat)",
-                "traveler information message (tim)",
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
-                "name": "US Department of Transportation"
-            },
-            "identifier": "https://data.transportation.gov/api/views/gu5j-r7xj",
+            "dataQuality": true,
             "description": "This is the EVENT data captured from the New York City CV Pilot project that was processed by the independent evaluators at Volpe. Additional data collected and data dictionary are in the attachments.\n\n\nEach EVENT record documents the details of one application warning that occurred on an Aftermarket Safety Device (ASD) in an equipped host vehicle and includes CV messages from a defined recording time both before and after the warning was generated by the host ASD. Messages in the recording time window include the Basic Safety Messages (BSM) of the host vehicle that received the warning, as well as other BSMs received from the warning target equipped vehicle (for V2V applications) or other nearby equipped vehicles. Depending on the application warning type, MAP messages, Signal Phase and Timing (SPaT) messages, and Traveler Information Messages (TIM) that were heard by the host vehicle may also be included in the event record.",
-            "title": "NYC CV Pilot IE Processed Data",
-            "programCode": [
-                "021:010"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55171,106 +55141,112 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/gu5j-r7xj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gu5j-r7xj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gu5j-r7xj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/gu5j-r7xj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gu5j-r7xj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gu5j-r7xj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/gu5j-r7xj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gu5j-r7xj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gu5j-r7xj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/gu5j-r7xj",
+            "issued": "2022-09-30",
+            "keyword": [
+                "aftermarket safety device (asd)",
+                "arterial",
+                "basic safety message (bsm)",
+                "connected vehicle message",
+                "connected vehicle pilot (cvp)",
+                "field test",
+                "independent evaluation",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "new york city department of transportation (nycdot)",
+                "roadside equipment (rse)",
+                "signal phase and timing (spat)",
+                "traveler information message (tim)",
+                "vehicle to infrastructure (v2i)",
+                "vehicle to vehicle (v2v)"
+            ],
+            "landingPage": "https://www.its.dot.gov/pilots/pilots_nycdot.htm",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-07",
+            "programCode": [
+                "021:010"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
             "spatial": "New York City",
-            "dataQuality": true,
+            "temporal": "2021-01/P12M",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NYC CV Pilot IE Processed Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/gutz-h9fp",
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
                 "fn": "Bureau of Transporation Statistics",
                 "hasEmail": "mailto:answers@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/gutz-h9fp",
             "description": "A monthly measure of the volume of services performed by the for-hire transportation sector. The index covers the activities of for-hire trucking, freight railroad services, inland waterway traffic, pipeline movements, and air freight.",
-            "title": "Transportation Services Index - Freight",
+            "identifier": "https://data.transportation.gov/api/views/gutz-h9fp",
+            "issued": "2025-01-03",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/gutz-h9fp",
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
+            "title": "Transportation Services Index - Freight"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/guuc-d2rv",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2022-07-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "analysis",
-                "commute patterns",
-                "geo-economic",
-                "geotype",
-                "geo-typology",
-                "land use",
-                "microtype",
-                "street network",
-                "transportation"
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
-            "identifier": "https://data.transportation.gov/api/views/guuc-d2rv",
             "description": "This dataset includes the inputs and results for developing a transportation geo-typology that categorizes every location in the United States in terms of their main drivers of transportation demand and supply. It provides the raw inputs to the census tract level microtypes and county or CBSA level geotypes as well as the final typology labels at both the tract (microtype) and county/CBSA (geotype) levels. Inputs include information on the street network, economic characteristics, topography, commute patterns, and land use. The methodology is published in \"Popovich, N., Spurlock, C. A., Needell, Z., Jin, L., Wenzel, T., Sheppard, C., & Asudegi, M. (2021). A methodology to develop a geospatial transportation typology. Journal of transport geography, 93, 103061\".",
-            "title": "Geo-spatial Transportation Typology",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55278,47 +55254,88 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/guuc-d2rv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/guuc-d2rv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/guuc-d2rv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/guuc-d2rv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/guuc-d2rv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/guuc-d2rv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/guuc-d2rv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/guuc-d2rv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/guuc-d2rv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States of America, Census Tracts",
+            "identifier": "https://data.transportation.gov/api/views/guuc-d2rv",
+            "issued": "2022-07-29",
+            "keyword": [
+                "analysis",
+                "commute patterns",
+                "geo-economic",
+                "geotype",
+                "geo-typology",
+                "land use",
+                "microtype",
+                "street network",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/guuc-d2rv",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-05-08",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "spatial": "United States of America, Census Tracts",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "Geo-spatial Transportation Typology"
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
-            "landingPage": "https://data.transportation.gov/d/gw97-6he9",
-            "issued": "2010-09-29",
-            "temporal": "R/1975-01-31/P1M",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "https://safetydata.fra.dot.gov/Gcis/UserManagement/Login.aspx",
-            "modified": "2024-10-09",
-            "references": [
-                "http://safetydata.fra.dot.gov/OfficeofSafety/Documents/GCIS%20Electronic%20Submissions%20Instructions.pdfhttps://safetydata.fra.dot.gov/MasterWebService/PublicApi/Develop/QuickStartGuide"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://safetydata.fra.dot.gov/OfficeofSafety/Documents/GCIS%20Electronic%20Submissions%20Instructions.pdf",
+            "describedByType": "application/pdf",
+            "description": "The entire National Highway-Rail Crossing Inventory is available in three separate downloadble files. There is a file of all current Public-at-Grade crossings. There is a file of all current Private and grade-separated crossings. There is also a file which contains about 10 years of archival records for all types of crossings.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://safetydata.fra.dot.gov/MasterWebService/publicapi",
+                    "mediaType": "application/atom+xml",
+                    "title": "GCIS Public API"
+                }
             ],
+            "identifier": "224.3",
+            "isPartOf": "DOT-224",
+            "issued": "2010-09-29",
             "keyword": [
                 "acts of god",
                 "collisions",
@@ -55327,57 +55344,54 @@
                 "fires",
                 "rail"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "224.3",
+            "landingPage": "https://data.transportation.gov/d/gw97-6he9",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-10-09",
+            "phone": "202-493-6285",
+            "programCode": [
+                "021:036"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Railroad Administration"
             },
-            "description": "The entire National Highway-Rail Crossing Inventory is available in three separate downloadble files. There is a file of all current Public-at-Grade crossings. There is a file of all current Private and grade-separated crossings. There is also a file which contains about 10 years of archival records for all types of crossings.",
-            "title": "Highway-Rail Crossings Inventory Data - GCIS Public API",
-            "isPartOf": "DOT-224",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "describedByType": "application/pdf",
-            "programCode": [
-                "021:036"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://safetydata.fra.dot.gov/MasterWebService/publicapi",
-                    "mediaType": "application/atom+xml",
-                    "title": "GCIS Public API"
-                }
+            "references": [
+                "http://safetydata.fra.dot.gov/OfficeofSafety/Documents/GCIS%20Electronic%20Submissions%20Instructions.pdfhttps://safetydata.fra.dot.gov/MasterWebService/PublicApi/Develop/QuickStartGuide"
             ],
             "spatial": "Latitude/Longitude",
-            "describedBy": "http://safetydata.fra.dot.gov/OfficeofSafety/Documents/GCIS%20Electronic%20Submissions%20Instructions.pdf",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "https://safetydata.fra.dot.gov/MasterWebService/publicapi",
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
+            "title": "Highway-Rail Crossings Inventory Data - GCIS Public API"
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
+            "description": "This dataset contains the estimates of the vehicle miles traveled (VMT) for interstate highways and how the total travel measured by VMT compares with travel that occurred in the same week of the previous year.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Weekly Traffic Volume Report estimates the vehicle miles traveled (VMT) for interstate highways and how the total travel measured by VMT compares with travel that occurred in the same week of the previous year. The VMT is further split into passenger vehicle and truck components. The information gives new insights into the effect on traffic by storm activity, economic fluctuations, and other variables that could not be evaluated using the monthly report.",
+                    "downloadURL": "https://www.fhwa.dot.gov/policyinformation/weeklyreports/",
+                    "mediaType": "application/pdf",
+                    "title": "Weekly Travel Reporting"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/gwk8-akhc",
             "issued": "2020-09-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
             "keyword": [
                 "fhwa",
                 "traffic volume trends",
@@ -55387,131 +55401,104 @@
                 "vmt",
                 "weekly"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/gwk8-akhc",
-            "description": "This dataset contains the estimates of the vehicle miles traveled (VMT) for interstate highways and how the total travel measured by VMT compares with travel that occurred in the same week of the previous year.",
-            "title": "Weekly Traffic Volume (Old)",
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-05-08",
             "primaryITInvestmentUII": "021-938741189",
             "programCode": [
                 "021:009"
             ],
-            "distribution": [
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.fhwa.dot.gov/policyinformation/weeklyreports/",
-                    "description": "Weekly Traffic Volume Report estimates the vehicle miles traveled (VMT) for interstate highways and how the total travel measured by VMT compares with travel that occurred in the same week of the previous year. The VMT is further split into passenger vehicle and truck components. The information gives new insights into the effect on traffic by storm activity, economic fluctuations, and other variables that could not be evaluated using the monthly report.",
-                    "@type": "dcat:Distribution",
-                    "title": "Weekly Travel Reporting"
-                }
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
             "systemOfRecords": "https://www.govinfo.gov/content/pkg/FR-2006-05-03/pdf/E6-6510.pdf",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Weekly Traffic Volume (Old)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/gwx6-wfa3",
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
                 "fn": "Sean Jahanmir",
                 "hasEmail": "mailto:sean.jahanmir@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/gwx6-wfa3",
             "description": "Number of personal vehicle passengers, train passengers, bus passengers, and pedestrians entering the United States from Mexico. The Bureau of Transportation of Statistics releases incoming border crossing statistics using data collected at ports of entry by U.S. Customs and Border Protection.",
-            "title": "U.S.-Mexico Incoming Person Crossings",
+            "identifier": "https://data.transportation.gov/api/views/gwx6-wfa3",
+            "issued": "2025-01-29",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/gwx6-wfa3",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://opendatacommons.org/licenses/pddl/1.0/",
+            "modified": "2025-01-29",
             "programCode": [
                 "021:053"
             ],
-            "license": "http://opendatacommons.org/licenses/pddl/1.0/",
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
+            "title": "U.S.-Mexico Incoming Person Crossings"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/gxhw-fwdh",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Cost of fuel for transportation by month and type of fuel.",
+            "identifier": "https://data.transportation.gov/api/views/gxhw-fwdh",
             "issued": "2023-06-21",
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
+            "landingPage": "https://data.transportation.gov/d/gxhw-fwdh",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-18",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/gxhw-fwdh",
-            "description": "Cost of fuel for transportation by month and type of fuel.",
-            "title": "Monthly Motor Fuel Prices",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Monthly Motor Fuel Prices"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/gyti-3rm8",
-            "issued": "2020-06-10",
             "@type": "dcat:Dataset",
-            "modified": "2020-06-10",
-            "keyword": [
-                "transportation and economy"
-            ],
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "BTS Open Data",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
-            "identifier": "https://data.transportation.gov/api/views/gyti-3rm8",
             "description": "Trips by Distance data with additional county transportation statistics",
-            "title": "Trips by Distance with County Data",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55519,74 +55506,105 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/gyti-3rm8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gyti-3rm8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gyti-3rm8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/gyti-3rm8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gyti-3rm8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gyti-3rm8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/gyti-3rm8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/gyti-3rm8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/gyti-3rm8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/gyti-3rm8",
+            "issued": "2020-06-10",
+            "keyword": [
+                "transportation and economy"
+            ],
+            "landingPage": "https://data.transportation.gov/d/gyti-3rm8",
+            "modified": "2020-06-10",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Trips by Distance with County Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/gyuh-ipsr",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2020-03-02",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-28",
-            "keyword": [
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
-            "identifier": "https://data.transportation.gov/api/views/gyuh-ipsr",
             "description": "National spending by category",
-            "title": "Transportation Economic Trends: Transportation Spending - National",
+            "identifier": "https://data.transportation.gov/api/views/gyuh-ipsr",
+            "issued": "2020-03-02",
+            "keyword": [
+                "transportation spending"
+            ],
+            "landingPage": "https://data.transportation.gov/d/gyuh-ipsr",
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
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Transportation Economic Trends: Transportation Spending - National"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/h29m-r5jr",
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
+                    "description": "2011 Missouri HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/missouri2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Missouri"
+                }
+            ],
+            "identifier": "678.27",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -55600,74 +55618,39 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.27",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Missouri",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/h29m-r5jr",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/missouri2011.zip",
-                    "description": "2011 Missouri HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Missouri"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Missouri"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/h2kz-rw8a",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-10-09",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
-            "keyword": [
-                "bicycle",
-                "expenditures"
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
-            "identifier": "https://data.transportation.gov/api/views/h2kz-rw8a",
             "description": "Data from the U.S. Department of Commerce, Bureau of Economic Analysis, National Income Product Accounts on real personal consumption expenditures on bicycles and accessories and data from the U.S. Department of Commerce, Census Bureau, USA Trade Online on U.S. imports of non-motorized bicycles and other cycles, including delivery tricycles. Data by month.",
-            "title": "National Expenditures on Bicycles and Accessories and U.S. Imports of Non-motorized Bicycles",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55675,46 +55658,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/h2kz-rw8a/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/h2kz-rw8a/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/h2kz-rw8a/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/h2kz-rw8a/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/h2kz-rw8a/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/h2kz-rw8a/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/h2kz-rw8a/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/h2kz-rw8a/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/h2kz-rw8a/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/h2kz-rw8a",
+            "issued": "2024-10-09",
+            "keyword": [
+                "bicycle",
+                "expenditures"
+            ],
+            "landingPage": "https://data.transportation.gov/d/h2kz-rw8a",
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
                 "Research and Statistics"
-            ]
+            ],
+            "title": "National Expenditures on Bicycles and Accessories and U.S. Imports of Non-motorized Bicycles"
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
-            "landingPage": "https://data.transportation.gov/d/h2ub-xxjb",
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
+            "identifier": "106.2",
+            "isPartOf": "DOT-106",
+            "issued": "2010-12-15",
             "keyword": [
                 "basic",
                 "basics",
@@ -55742,87 +55757,45 @@
                 "unsafe driving",
                 "vehicle maintenance"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "106.2",
+            "landingPage": "https://data.transportation.gov/d/h2ub-xxjb",
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
-            "landingPage": "https://data.transportation.gov/d/h4kh-i7b7",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2020-05-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-05",
-            "references": [
-                "http://txdot-its-c2c.txdot.gov/WZDx/2.0",
-                "https://collaboration.fhwa.dot.gov/wzmp/updateddocuments/FHWA-HOP-20-020_Data_Dictionary_DRAFT_Report.pdf"
-            ],
-            "keyword": [
-                "highways",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "lane closure (dcmthcd)",
-                "southwest research institute (swri)",
-                "texas",
-                "texas department of transportation (txdot)",
-                "texas dot work zone data (txwzd)",
-                "work zone data exchange (wzdx)",
-                "work zones"
-            ],
             "conformsTo": "https://www.transportation.gov/av/data/wzdx",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kate Hartman",
                 "hasEmail": "mailto:kate.hartman@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "US Department of Transportation"
-            },
-            "identifier": "https://data.transportation.gov/api/views/h4kh-i7b7",
+            "dataQuality": true,
             "description": "This dataset provides lane closure occurrences within the Texas Department of Transportation (TxDOT) highway system in a tabular format.\n\nA continuously updating archive of the TxDOT WZDx feed data can be found at <a href=\"http://usdot-its-workzone-raw-publicdata.s3.amazonaws.com/index.html\" target=\"_blank\" rel=\"noopener\">ITS WorkZone Raw Data Sandbox</a> and the <a href=\"http://usdot-its-workzone-publicdata.s3.amazonaws.com/index.html\" target=\"_blank\" rel=\"noopener\">ITS WorkZone Semi-Processed Data Sandbox</a>.  The <a href=\"http://txdot-its-c2c.txdot.gov/WZDx/2.0\" target=\"_blank\" rel=\"noopener\">live feed</a> is currently compliant with the <a href=\"https://github.com/usdot-jpo-ode/jpo-wzdx/tree/v2.0\" target=\"_blank\" rel=\"noopener\">Work Zone Data Exchange (WZDx) Specification version 2.0</a>.",
-            "title": "Texas DOT (TxDOT) Work Zone Data Schema Version 2.0",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55830,62 +55803,76 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/h4kh-i7b7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/h4kh-i7b7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/h4kh-i7b7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/h4kh-i7b7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/h4kh-i7b7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/h4kh-i7b7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/h4kh-i7b7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/h4kh-i7b7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/h4kh-i7b7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Texas",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/h4kh-i7b7",
+            "issued": "2020-05-26",
+            "keyword": [
+                "highways",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "lane closure (dcmthcd)",
+                "southwest research institute (swri)",
+                "texas",
+                "texas department of transportation (txdot)",
+                "texas dot work zone data (txwzd)",
+                "work zone data exchange (wzdx)",
+                "work zones"
+            ],
+            "landingPage": "https://data.transportation.gov/d/h4kh-i7b7",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2020-06-05",
+            "programCode": [
+                "021:013"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
+            "references": [
+                "http://txdot-its-c2c.txdot.gov/WZDx/2.0",
+                "https://collaboration.fhwa.dot.gov/wzmp/updateddocuments/FHWA-HOP-20-020_Data_Dictionary_DRAFT_Report.pdf"
+            ],
+            "spatial": "Texas",
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Texas DOT (TxDOT) Work Zone Data Schema Version 2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://data.transportation.gov/d/h52u-5adn",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2021-08-31",
-            "@type": "dcat:Dataset",
-            "modified": "2021-08-31",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alpha Wingfield",
                 "hasEmail": "mailto:alpha.wingfield@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/h52u-5adn",
             "description": "This document offers guidance on the correct usage of the USDOT mark, seal, and signatures.",
-            "title": "USDOT Graphic Standards PDF",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55893,48 +55880,41 @@
                     "mediaType": "application/pdf"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/h52u-5adn",
+            "issued": "2021-08-31",
+            "landingPage": "https://data.transportation.gov/d/h52u-5adn",
             "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2021-08-31",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Administrative"
-            ]
+            ],
+            "title": "USDOT Graphic Standards PDF"
         },
         {
-            "accessLevel": "public",
-            "bureauCode": [
-                "021:18"
-            ],
-            "landingPage": "https://data.transportation.gov/d/h54p-g34m",
-            "issued": "1999-04-26",
-            "temporal": "1999/2015",
             "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
-            "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.nhtsa.gov/Research/Databases+and+Software/NHTSA+Test+Reference+Guides"
-            ],
-            "keyword": [
-                "compliance",
-                "component",
-                "test",
-                "vehicle"
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www.nhtsa.gov/Research/Databases+and+Software/NHTSA+Test+Reference+Guides",
+            "agencyProgramURL": "http://www.nhtsa.gov/Research",
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
-            "identifier": "DOT-1842",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "The NHTSA Component Test Database contains engineering data measured during various types of research.",
-            "title": "Component Test Database",
-            "primaryITInvestmentUII": "021-961265599",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55943,33 +55923,68 @@
                     "title": "Latest Tests"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "DOT-1842",
+            "issued": "1999-04-26",
+            "keyword": [
+                "compliance",
+                "component",
+                "test",
+                "vehicle"
+            ],
+            "landingPage": "https://data.transportation.gov/d/h54p-g34m",
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
+            "title": "Component Test Database"
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
-            "landingPage": "https://data.transportation.gov/d/h5j5-hgi3",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/09febtvt/09febtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "February 2009"
+                }
             ],
+            "identifier": "18.67",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -55979,76 +55994,42 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.67",
+            "landingPage": "https://data.transportation.gov/d/h5j5-hgi3",
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
-            "title": "Monthly Traffic Volume Trends - February 2009",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/09febtvt/09febtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "February 2009"
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
+            "title": "Monthly Traffic Volume Trends - February 2009"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/h77j-murt",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2024-10-17",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-14",
-            "keyword": [
-                "aff",
-                "air carriers",
-                "airfare",
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
-            "identifier": "https://data.transportation.gov/api/views/h77j-murt",
             "description": "Average domestic air fare by quarter.",
-            "title": "AFF - Average Air Fare by Quarter",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56056,60 +56037,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/h77j-murt/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/h77j-murt/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/h77j-murt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/h77j-murt/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/h77j-murt/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/h77j-murt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/h77j-murt/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/h77j-murt/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/h77j-murt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/h77j-murt",
+            "issued": "2024-10-17",
+            "keyword": [
+                "aff",
+                "air carriers",
+                "airfare",
+                "aviation facts & figures"
+            ],
+            "landingPage": "https://data.transportation.gov/d/h77j-murt",
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
+            "title": "AFF - Average Air Fare by Quarter"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/h7pv-kjj5",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2021-12-08",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-24",
-            "keyword": [
-                "covid-19",
-                "freight"
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
-            "identifier": "https://data.transportation.gov/api/views/h7pv-kjj5",
+            "dataQuality": true,
             "description": "Three freight indicators tracking weekly compared to a pre-COVID-19 baseline",
-            "title": "Freight Indicators (weekly)",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56117,68 +56102,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/h7pv-kjj5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/h7pv-kjj5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/h7pv-kjj5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/h7pv-kjj5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/h7pv-kjj5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/h7pv-kjj5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/h7pv-kjj5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/h7pv-kjj5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/h7pv-kjj5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/h7pv-kjj5",
+            "issued": "2021-12-08",
+            "keyword": [
+                "covid-19",
+                "freight"
+            ],
+            "landingPage": "https://data.transportation.gov/d/h7pv-kjj5",
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
+            "title": "Freight Indicators (weekly)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/h9qc-expu",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-12-27",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-30",
-            "keyword": [
-                "demand response",
-                "fares",
-                "geographic",
-                "geospatial",
-                "passenger",
-                "public transit",
-                "requirements"
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
-            "identifier": "https://data.transportation.gov/api/views/h9qc-expu",
             "description": "This dataset details passenger eligibility and requirements for Demand Response (DR) modes for each applicable agency and type of service (TOS) reported to the National Transit Database for Report Year 2023.\n\nNTD Data Tables organize and summarize data from the 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. \n\nThis data is a part of new reporting requirements as of 2023. Other datasets describing aspects of Demand Response Geographical Area Coverage can be found at the following links:\nCounties and Places: https://data.transportation.gov/Public-Transit/Demand-Response-Geographic-Area-Coverage-Counties-/3kum-6vpd/about_data\nService Schedules: https://data.transportation.gov/dataset/Demand-Response-Geographic-Area-Coverage-Service-S/4p55-emkp/about_data\n\nIf you have any other questions about this table, please contact the NTD Help Desk at NTDHelp@dot.gov.",
-            "title": "2023 NTD Annual Data - Demand Response Geographic Area Coverage (Passenger Eligibility and Fares)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56186,72 +56167,81 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/h9qc-expu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/h9qc-expu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/h9qc-expu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/h9qc-expu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/h9qc-expu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/h9qc-expu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/h9qc-expu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/h9qc-expu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/h9qc-expu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/h9qc-expu",
+            "issued": "2024-12-27",
+            "keyword": [
+                "demand response",
+                "fares",
+                "geographic",
+                "geospatial",
+                "passenger",
+                "public transit",
+                "requirements"
+            ],
+            "landingPage": "https://data.transportation.gov/d/h9qc-expu",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-30",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Transit Administration"
+            },
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "2023 NTD Annual Data - Demand Response Geographic Area Coverage (Passenger Eligibility and Fares)"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/haqz-eg6b",
-            "issued": "2021-10-13",
             "@type": "dcat:Dataset",
-            "modified": "2023-08-17",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/haqz-eg6b",
+            "issued": "2021-10-13",
+            "landingPage": "https://data.transportation.gov/d/haqz-eg6b",
+            "modified": "2023-08-17",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
-            "title": "SMT Page",
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "SMT Page"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/hbgj-g3yp",
-            "issued": "2023-02-04",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/hbgj-g3yp",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "NS",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56259,75 +56249,54 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hbgj-g3yp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hbgj-g3yp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hbgj-g3yp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/hbgj-g3yp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hbgj-g3yp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hbgj-g3yp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hbgj-g3yp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hbgj-g3yp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hbgj-g3yp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/hbgj-g3yp",
+            "issued": "2023-02-04",
+            "landingPage": "https://data.transportation.gov/d/hbgj-g3yp",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "NS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/hcgc-h7hr",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2017-09-20",
-            "@type": "dcat:Dataset",
-            "temporal": "2017-07-14/2017-07-14",
-            "modified": "2017-09-20",
-            "keyword": [
-                "ams san diego testbed",
-                "analysis modeling and simulation (ams) testbed development",
-                "california",
-                "cluster analysis",
-                "freeway",
-                "i-15",
-                "incident data",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "san diego",
-                "simulation data",
-                "speed contour",
-                "speed-flow-density data",
-                "sr-1163",
-                "sr-78",
-                "transport simulation systems (tss)",
-                "travel time"
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
-            "identifier": "https://data.transportation.gov/api/views/hcgc-h7hr",
+            "dataQuality": true,
             "description": "The data in this repository were collected from the San Diego, California testbed, namely, I-15 from the interchange with SR-78 in the north to the interchange with SR-163 in the south, along the mainline and at the entrance ramps.  This file contains information on the field observation and simulation results for speed profile from the Dallas, Texas testbed. The time reported for the speed profiles are between 2:00PM to 8:00PM in increments of 10 minutes.",
-            "title": "AMS San Diego Testbed - Calibration Data",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56335,49 +56304,95 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hcgc-h7hr/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hcgc-h7hr/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hcgc-h7hr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/hcgc-h7hr/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hcgc-h7hr/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hcgc-h7hr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hcgc-h7hr/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hcgc-h7hr/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hcgc-h7hr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "I-15, San Diego, California",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/hcgc-h7hr",
+            "issued": "2017-09-20",
+            "keyword": [
+                "ams san diego testbed",
+                "analysis modeling and simulation (ams) testbed development",
+                "california",
+                "cluster analysis",
+                "freeway",
+                "i-15",
+                "incident data",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "san diego",
+                "simulation data",
+                "speed contour",
+                "speed-flow-density data",
+                "sr-1163",
+                "sr-78",
+                "transport simulation systems (tss)",
+                "travel time"
+            ],
+            "landingPage": "https://data.transportation.gov/d/hcgc-h7hr",
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
+            "spatial": "I-15, San Diego, California",
+            "temporal": "2017-07-14/2017-07-14",
             "theme": [
                 "Transportation"
-            ]
+            ],
+            "title": "AMS San Diego Testbed - Calibration Data"
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
-            "landingPage": "https://data.transportation.gov/d/hcwt-es4b",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/historicvmt.xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Summary 1970 - 1991"
+                }
             ],
+            "identifier": "18.154",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -56387,60 +56402,61 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.154",
+            "landingPage": "https://data.transportation.gov/d/hcwt-es4b",
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
-            "title": "Monthly Traffic Volume Trends - Summary 1970 - 1991",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/historicvmt.xlsx",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "Summary 1970 - 1991"
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
+            "title": "Monthly Traffic Volume Trends - Summary 1970 - 1991"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/downloads/folders/TSBS/FLAT_TSBS.zip",
+            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
+            "analysisUnit": "Vehicles , Tires, Child Safety Seats, Equipment",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/hczg-qbhf",
-            "issued": "2002-12-16",
-            "temporal": "R/1962-01-01/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www-odi.nhtsa.dot.gov/help/tsb.html"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "http://www-odi.nhtsa.dot.gov/downloads/folders/TSBS/TSBS.txt",
+            "describedByType": "text/plain",
+            "description": "The Technical Service Bulletins data contains summaries of the Manufacturers' Technical Service Bulletins by single year, make and model. An optional item of Vehicle Component may be also available. (The data does not contain all the service bulletins generated by a manufacturer. Bulletins for safety recalls in general are not included, and also bulletins which may not pertain to a defect may not be included.)",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www-odi.nhtsa.dot.gov/downloads/folders/TSBS/FLAT_TSBS.zip",
+                    "mediaType": "text/csv",
+                    "title": "Downloadable file"
+                }
             ],
+            "identifier": "82.0",
+            "issued": "2002-12-16",
             "keyword": [
                 "bulletin",
                 "defect",
@@ -56450,87 +56466,51 @@
                 "summaries",
                 "technical",
                 "vehicle"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "82.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "The Technical Service Bulletins data contains summaries of the Manufacturers' Technical Service Bulletins by single year, make and model. An optional item of Vehicle Component may be also available. (The data does not contain all the service bulletins generated by a manufacturer. Bulletins for safety recalls in general are not included, and also bulletins which may not pertain to a defect may not be included.)",
-            "title": "NHTSA's Office of Defects Investigation (ODI) -  Technical Service Bulletins System (TSBS) - Downloadable file",
-            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
-            "describedByType": "text/plain",
+            ],
+            "landingPage": "https://data.transportation.gov/d/hczg-qbhf",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-2315",
             "primaryITInvestmentUII": "021-777552743",
             "programCode": [
                 "021:000"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www-odi.nhtsa.dot.gov/downloads/folders/TSBS/FLAT_TSBS.zip",
-                    "mediaType": "text/csv",
-                    "title": "Downloadable file"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "http://www-odi.nhtsa.dot.gov/help/tsb.html"
             ],
-            "describedBy": "http://www-odi.nhtsa.dot.gov/downloads/folders/TSBS/TSBS.txt",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/downloads/folders/TSBS/FLAT_TSBS.zip",
+            "temporal": "R/1962-01-01/P1D",
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
+            "title": "NHTSA's Office of Defects Investigation (ODI) -  Technical Service Bulletins System (TSBS) - Downloadable file"
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
-            "landingPage": "https://data.transportation.gov/d/hdbk-762t",
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
-            "identifier": "693.19",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
             "description": "The NBI System is the collection of bridge inspection information and costs associated with bridge replacements of structurally deficient bridges on and off the NHS. This data is collected under the auspices of the National Bridge Inspection Standards (NBIS) as prescribed by law. The NBI System collects the information that is used to determine eligibility for NHS projects, performance measure reporting, NHS penalty determination, and reporting to Congress.  It supports oversight of the NBIS through various report tools, and provides data reporting that supports agency strategic goals.",
-            "title": "National Bridge Inventory System (NBI) - 2010",
-            "isPartOf": "DOT-693",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
-            "primaryITInvestmentUII": "021-012940226",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56539,53 +56519,54 @@
                     "title": "2010"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
-            "dataQuality": true,
+            "identifier": "693.19",
+            "isPartOf": "DOT-693",
+            "issued": "1992-12-31",
+            "keyword": [
+                "bridge",
+                "condition",
+                "deck",
+                "inspection",
+                "structure"
+            ],
+            "landingPage": "https://data.transportation.gov/d/hdbk-762t",
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
+            "title": "National Bridge Inventory System (NBI) - 2010"
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
-                "name": "data.transportation.gov"
-            },
-            "identifier": "https://data.transportation.gov/api/views/hddu-nghv",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 2000",
-            "title": "Historic HPMS Data (Universe) - 2000",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56593,72 +56574,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hddu-nghv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hddu-nghv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hddu-nghv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/hddu-nghv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hddu-nghv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hddu-nghv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hddu-nghv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hddu-nghv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hddu-nghv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/hddu-nghv",
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
+            "title": "Historic HPMS Data (Universe) - 2000"
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
-            "landingPage": "https://data.transportation.gov/d/heuv-inga",
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
-            "identifier": "692.38",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - Sulfur Dioxide",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "primaryITInvestmentUII": "021-845083703",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56667,43 +56648,47 @@
                     "title": "Sulfur Dioxide"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.38",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/heuv-inga",
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
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - Sulfur Dioxide"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/hf8z-xt9r",
-            "issued": "2022-05-09",
             "@type": "dcat:Dataset",
-            "modified": "2024-05-31",
-            "keyword": [
-                "jones act",
-                "maritime",
-                "merchant fleet"
-            ],
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "MARAD-Datahub",
                 "hasEmail": "mailto:data.marad@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
-            "identifier": "https://data.transportation.gov/api/views/hf8z-xt9r",
             "description": "dataset of oceangoing, self-propelled, privately-owned U.S.-flag vessels of 1,000 gross tons and above that carry cargo from port to port for commercial and government  customers.",
-            "title": "US Flag Fleet List - January 2022 - dataset",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56711,50 +56696,55 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hf8z-xt9r/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hf8z-xt9r/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hf8z-xt9r/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/hf8z-xt9r/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hf8z-xt9r/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hf8z-xt9r/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hf8z-xt9r/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hf8z-xt9r/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hf8z-xt9r/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/hf8z-xt9r",
+            "issued": "2022-05-09",
+            "keyword": [
+                "jones act",
+                "maritime",
+                "merchant fleet"
+            ],
+            "landingPage": "https://data.transportation.gov/d/hf8z-xt9r",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-05-31",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Maritime and Waterways"
-            ]
+            ],
+            "title": "US Flag Fleet List - January 2022 - dataset"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/hg4d-8cim",
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
-            "identifier": "https://data.transportation.gov/api/views/hg4d-8cim",
             "description": "The FMCSA Safety Measurement System (SMS) data, consists of summary results of all active Interstate and Intrastate Hazmat Motor\nFile Description: Carriers of property and/or passengers. File is comma delimited. One carrier per row.",
-            "title": "SMS EXTRACT INTER",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56762,71 +56752,53 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hg4d-8cim/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hg4d-8cim/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hg4d-8cim/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/hg4d-8cim/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hg4d-8cim/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hg4d-8cim/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hg4d-8cim/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hg4d-8cim/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hg4d-8cim/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/hg4d-8cim",
+            "issued": "2024-12-22",
+            "landingPage": "https://data.transportation.gov/d/hg4d-8cim",
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
+            "title": "SMS EXTRACT INTER"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/hgck-kgan",
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
-            "identifier": "https://data.transportation.gov/api/views/hgck-kgan",
             "description": "Part of the Wyoming Department of Transportation Connected Vehicle Pilot Phase 4. Verify that OBUs use different LTE-V2X Configuration Profiles based on the vehicle's speed.\nHost and remote vehicles travelling below 120 kmph\nHost and remote vehicles travelling above 120 kmph",
-            "title": "LTE-V2X Wyoming Connected Vehicle Pilot test ID WV2IMCT-1 BSM count",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -56834,42 +56806,85 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hgck-kgan/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hgck-kgan/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hgck-kgan/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/hgck-kgan/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hgck-kgan/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hgck-kgan/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hgck-kgan/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hgck-kgan/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hgck-kgan/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Wyoming",
+            "identifier": "https://data.transportation.gov/api/views/hgck-kgan",
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
+            "landingPage": "https://data.transportation.gov/d/hgck-kgan",
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
+            "title": "LTE-V2X Wyoming Connected Vehicle Pilot test ID WV2IMCT-1 BSM count"
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
+            "description": "The Intelligent Transportation Systems Joint Program Office (ITS JPO) of the U.S. Department of Transportation (U.S. DOT) established the ITS Costs Database as a national resource for transportation professionals to go to in order to obtain cost estimates for ITS deployments. The purpose of the ITS Costs Database is to support informed decision-making by transportation leaders.\n\nThe ITS Costs Database contains estimates of ITS costs that can be used for developing project cost estimates during the planning process or preliminary design phase, and for policy studies and cost-benefit analyses. Both non-recurring (capital) and recurring (operating and maintenance) costs are provided where possible.\n\nTwo types of cost data are available: unit costs and system cost summaries. System cost summaries are the costs of an ITS project or portion of an ITS project such as the cost of expanding a statewide road weather information system or the detailed costs for a signal interconnect project. Each entry describes the background of the project, the ITS technologies deployed, and presents the costs and what the costs covered. A breakout of components and costs is provided for most summaries depending on the information available. Both capital costs and annual O&M costs are presented whenever possible. Unit costs are the costs associated with an individual ITS element, such as a video camera for traffic surveillance or a dynamic message sign. A range of costs (e.g., $500 - $1,000) is presented for the capital cost and annual operations and maintenance (O&M) cost of each element as well as an estimate of the length in years of its usable life. Unit costs are available in two formats: unadjusted and adjusted. Unadjusted costs are presented as the original value along with the dollar year.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Link to Intelligent Transportation Systems (ITS) Costs Database's Web User Interface.",
+                    "downloadURL": "https://www.itskrs.its.dot.gov/costs",
+                    "mediaType": "text/html",
+                    "title": "Intelligent Transportation Systems (ITS) Costs"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/hgmr-wk87",
             "issued": "2019-05-02",
-            "@type": "dcat:Dataset",
-            "modified": "2019-05-02",
             "keyword": [
                 "arterial management",
                 "automated vehicles",
@@ -56886,54 +56901,53 @@
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
-            "identifier": "https://data.transportation.gov/api/views/hgmr-wk87",
-            "description": "The Intelligent Transportation Systems Joint Program Office (ITS JPO) of the U.S. Department of Transportation (U.S. DOT) established the ITS Costs Database as a national resource for transportation professionals to go to in order to obtain cost estimates for ITS deployments. The purpose of the ITS Costs Database is to support informed decision-making by transportation leaders.\n\nThe ITS Costs Database contains estimates of ITS costs that can be used for developing project cost estimates during the planning process or preliminary design phase, and for policy studies and cost-benefit analyses. Both non-recurring (capital) and recurring (operating and maintenance) costs are provided where possible.\n\nTwo types of cost data are available: unit costs and system cost summaries. System cost summaries are the costs of an ITS project or portion of an ITS project such as the cost of expanding a statewide road weather information system or the detailed costs for a signal interconnect project. Each entry describes the background of the project, the ITS technologies deployed, and presents the costs and what the costs covered. A breakout of components and costs is provided for most summaries depending on the information available. Both capital costs and annual O&M costs are presented whenever possible. Unit costs are the costs associated with an individual ITS element, such as a video camera for traffic surveillance or a dynamic message sign. A range of costs (e.g., $500 - $1,000) is presented for the capital cost and annual operations and maintenance (O&M) cost of each element as well as an estimate of the length in years of its usable life. Unit costs are available in two formats: unadjusted and adjusted. Unadjusted costs are presented as the original value along with the dollar year.",
-            "title": "Intelligent Transportation Systems (ITS) Costs",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.itskrs.its.dot.gov/costs",
-                    "description": "Link to Intelligent Transportation Systems (ITS) Costs Database's Web User Interface.",
-                    "@type": "dcat:Distribution",
-                    "title": "Intelligent Transportation Systems (ITS) Costs"
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
+            "title": "Intelligent Transportation Systems (ITS) Costs"
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
-            "landingPage": "https://data.transportation.gov/d/hhr3-a3nk",
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
+            "identifier": "321.2",
+            "isPartOf": "DOT-321",
+            "issued": "2011-01-18",
             "keyword": [
                 "control",
                 "data.gov",
@@ -56944,69 +56958,42 @@
                 "traffic",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "321.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "NHTSA's issues statements of policy on traffic injury control",
-            "title": "Traffic Injury Control Statements of Policy -",
-            "isPartOf": "DOT-321",
-            "agencyProgramURL": "http://www.nhtsa.gov/About+NHTSA/NHTSA+Electronic+Reading+Room+(ERR)",
+            "landingPage": "https://data.transportation.gov/d/hhr3-a3nk",
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
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/hinw-eisy",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-12-11",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-12",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Trans;portation Statistics",
                 "hasEmail": "mailto:answers@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/hinw-eisy",
             "description": "",
-            "title": "AFF - Aircraft Fleet Age by Carrier",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57014,111 +57001,136 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hinw-eisy/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hinw-eisy/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hinw-eisy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/hinw-eisy/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hinw-eisy/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hinw-eisy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hinw-eisy/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hinw-eisy/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hinw-eisy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/hinw-eisy",
+            "issued": "2024-12-11",
+            "landingPage": "https://data.transportation.gov/d/hinw-eisy",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-12-12",
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
+            "title": "AFF - Aircraft Fleet Age by Carrier"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/hjpc-j5px",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2020-04-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-30",
-            "keyword": [
-                "government",
-                "transportation expenditures"
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
-            "identifier": "https://data.transportation.gov/api/views/hjpc-j5px",
             "description": "Government transportation expenditures",
-            "title": "Transportation Economic Trends: Government Transportation Expenditures",
+            "identifier": "https://data.transportation.gov/api/views/hjpc-j5px",
+            "issued": "2020-04-23",
+            "keyword": [
+                "government",
+                "transportation expenditures"
+            ],
+            "landingPage": "https://data.transportation.gov/d/hjpc-j5px",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-12-30",
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
+            "title": "Transportation Economic Trends: Government Transportation Expenditures"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/hjza-d5g7",
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
                 "hasEmail": "mailto:answers@bts.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/hjza-d5g7",
             "description": "Number of personal vehicle passengers, train passengers, bus passengers, and pedestrians entering the United States from Canada. The Bureau of Transportation of Statistics releases incoming border crossing statistics using data collected at ports of entry by U.S. Customs and Border Protection.",
-            "title": "U.S.-Canada Incoming Person Crossings",
+            "identifier": "https://data.transportation.gov/api/views/hjza-d5g7",
+            "issued": "2025-01-29",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/hjza-d5g7",
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
+            "title": "U.S.-Canada Incoming Person Crossings"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/hk7z-wi42",
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
+            "description": "The data elements contained in this data environment were collected during the Prototype Operational Data Environment (P-ODE) formal data collection period. The Prototype Operational Data Environment (P-ODE) is a system that receives data from multiple sources in real-time, is capable of performing validation, integration, and sanitization checks, transforms the data into a consistent format, and makes the data available to applications as well as stores the data in ITS JPO data system. This data environment contains speed, volume, occupancy, travel time, and incident data collected along I-66 in Northern Virginia between May 2016 and August 2016. The ASN.1 data set contains data records in their original binary form, while Detector and Incident data sets each contain records that have been converted to text format.\r\n\r\nThis legacy dataset was created before data.transportation.gov and is only currently available via the attached file(s). Please contact the dataset owner if there is a need for users to work with this data using the data.transportation.gov analysis features (online viewing, API, graphing, etc.) and the USDOT will consider modifying the dataset to fully integrate in data.transportation.gov.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/download/hk7z-wi42/application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/hk7z-wi42",
             "issued": "2016-10-25",
-            "@type": "dcat:Dataset",
-            "temporal": "2016-05-20/2016-08-24",
-            "modified": "2016-10-25",
             "keyword": [
                 "basic safety message (bsm)",
                 "detector",
@@ -57135,71 +57147,39 @@
                 "travel time",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/hk7z-wi42",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://creativecommons.org/licenses/by-nc-sa/3.0/legalcode",
+            "modified": "2016-10-25",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Department of Transportation"
             },
-            "identifier": "https://data.transportation.gov/api/views/hk7z-wi42",
-            "description": "The data elements contained in this data environment were collected during the Prototype Operational Data Environment (P-ODE) formal data collection period. The Prototype Operational Data Environment (P-ODE) is a system that receives data from multiple sources in real-time, is capable of performing validation, integration, and sanitization checks, transforms the data into a consistent format, and makes the data available to applications as well as stores the data in ITS JPO data system. This data environment contains speed, volume, occupancy, travel time, and incident data collected along I-66 in Northern Virginia between May 2016 and August 2016. The ASN.1 data set contains data records in their original binary form, while Detector and Incident data sets each contain records that have been converted to text format.\r\n\r\nThis legacy dataset was created before data.transportation.gov and is only currently available via the attached file(s). Please contact the dataset owner if there is a need for users to work with this data using the data.transportation.gov analysis features (online viewing, API, graphing, etc.) and the USDOT will consider modifying the dataset to fully integrate in data.transportation.gov.",
-            "title": "Prototype Operational Data Environment (P-ODE)",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/download/hk7z-wi42/application/vnd.openxmlformats-officedocument.wordprocessingml.document",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
-                }
-            ],
             "spatial": "Virginia",
-            "dataQuality": true,
-            "license": "http://creativecommons.org/licenses/by-nc-sa/3.0/legalcode",
-            "accrualPeriodicity": "irregular",
+            "temporal": "2016-05-20/2016-08-24",
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Prototype Operational Data Environment (P-ODE)"
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
-            "identifier": "https://data.transportation.gov/api/views/hkeh-xc4t",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 1991",
-            "title": "Historic HPMS Data (Sample) - 1991",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57207,50 +57187,85 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hkeh-xc4t/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hkeh-xc4t/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hkeh-xc4t/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/hkeh-xc4t/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hkeh-xc4t/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hkeh-xc4t/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hkeh-xc4t/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hkeh-xc4t/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hkeh-xc4t/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/hkeh-xc4t",
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
+            "title": "Historic HPMS Data (Sample) - 1991"
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
-            "landingPage": "https://data.transportation.gov/d/hkn8-d8d5",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/07dectvt/07dectvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "December 2007"
+                }
             ],
+            "identifier": "18.81",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -57260,76 +57275,79 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.81",
+            "landingPage": "https://data.transportation.gov/d/hkn8-d8d5",
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
-            "title": "Monthly Traffic Volume Trends - December 2007",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/07dectvt/07dectvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "December 2007"
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
+            "title": "Monthly Traffic Volume Trends - December 2007"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/hkub-bec2",
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
             "identifier": "https://data.transportation.gov/api/views/hkub-bec2",
+            "issued": "2024-05-10",
+            "landingPage": "https://data.transportation.gov/d/hkub-bec2",
+            "modified": "2024-05-30",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "2022 NCFO Ferry Vessels"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/hkvb-pbvd",
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
+                    "description": "2011 Indiana HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/indiana2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Indiana"
+                }
+            ],
+            "identifier": "678.16",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -57343,57 +57361,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.16",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Indiana",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/hkvb-pbvd",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/indiana2011.zip",
-                    "description": "2011 Indiana HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Indiana"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Indiana"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/hmey-w2v4",
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
+                    "description": "2011 Maine HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/maine2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Maine"
+                }
+            ],
+            "identifier": "678.21",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -57407,77 +57425,71 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.21",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Maine",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/hmey-w2v4",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/maine2011.zip",
-                    "description": "2011 Maine HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Maine"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Maine"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/hmpr-7h83",
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
             "identifier": "https://data.transportation.gov/api/views/hmpr-7h83",
+            "issued": "2020-12-08",
+            "landingPage": "https://data.transportation.gov/d/hmpr-7h83",
+            "modified": "2022-01-10",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Tank Car for TRB"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "The data set contains controlled unclassified procurement information, confidential business information, and information protected by statute or regulation.",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/hn23-gvjs",
-            "issued": "2014-12-29",
-            "temporal": "R/2014-12-29/P1Y",
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
+            "description": "Delphi projects module contains the following data elements, but is not limited to raw costs, burdened costs, agreement types, allocation of resources; and stores actual, budget and encumbrance balance per project, task, period, budget version and resource.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.transportation.gov/mission/data-inventory-not-available",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "738.0",
+            "issued": "2014-12-29",
             "keyword": [
                 "agreement types",
                 "budget balance",
@@ -57491,65 +57503,40 @@
                 "resource allocation ; actual balance",
                 "task"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DOT Socrata",
-                "hasEmail": "mailto:Socrata@dot.gov"
-            },
-            "identifier": "738.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
-            "description": "Delphi projects module contains the following data elements, but is not limited to raw costs, burdened costs, agreement types, allocation of resources; and stores actual, budget and encumbrance balance per project, task, period, budget version and resource.",
-            "title": "Delphi Projects Module -",
+            "landingPage": "https://data.transportation.gov/d/hn23-gvjs",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-14",
+            "phone": "202-366-9646",
             "primaryITInvestmentUII": "021-105731835",
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
+            "rights": "The data set contains controlled unclassified procurement information, confidential business information, and information protected by statute or regulation.",
+            "temporal": "R/2014-12-29/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-9646"
+            "title": "Delphi Projects Module -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/hpjf-p2n3",
-            "issued": "2024-04-05",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-05",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "https://www.bts.gov/topics/airlines-airports-and-aviation",
                 "hasEmail": "mailto:Robert.Nazareth@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/hpjf-p2n3",
             "description": "enplaned passengers",
-            "title": "Top 20 U.S. Gateways for Nonstop International Air Travel",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57557,70 +57544,87 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hpjf-p2n3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hpjf-p2n3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hpjf-p2n3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/hpjf-p2n3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hpjf-p2n3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hpjf-p2n3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hpjf-p2n3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hpjf-p2n3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hpjf-p2n3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works"
+            "identifier": "https://data.transportation.gov/api/views/hpjf-p2n3",
+            "issued": "2024-04-05",
+            "landingPage": "https://data.transportation.gov/d/hpjf-p2n3",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-04-05",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Top 20 U.S. Gateways for Nonstop International Air Travel"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:36"
             ],
-            "landingPage": "https://data.transportation.gov/d/hptj-vnn2",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NTD Program Support",
+                "hasEmail": "mailto:NTDHelp@dot.gov"
+            },
+            "description": "A national summary of capital expenses based on data reported by transit agencies to the National Transit Database (NTD) in Report Year 2022.\r\n\r\nNTD Data Summaries organize and summarize data from the 2022 National Transit Database in a manner that is more useful for quick reference and summary analysis.\r\n\r\nThis summary is based on the 2022 Capital Use file on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
+            "identifier": "https://data.transportation.gov/api/views/hptj-vnn2",
             "issued": "2023-09-09",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-10",
             "keyword": [
                 "capital expenses",
                 "expenditures",
                 "public transit",
                 "transit"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NTD Program Support",
-                "hasEmail": "mailto:NTDHelp@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/hptj-vnn2",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-09-10",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Transit Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/hptj-vnn2",
-            "description": "A national summary of capital expenses based on data reported by transit agencies to the National Transit Database (NTD) in Report Year 2022.\r\n\r\nNTD Data Summaries organize and summarize data from the 2022 National Transit Database in a manner that is more useful for quick reference and summary analysis.\r\n\r\nThis summary is based on the 2022 Capital Use file on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
-            "title": "2022 NTD Annual Data Summary - Capital Expenses",
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "2022 NTD Annual Data Summary - Capital Expenses"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/hr8h-ufhq",
             "bureauCode": [
                 "021:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kate Hartman",
+                "hasEmail": "mailto:kate.hartman@dot.gov"
+            },
+            "description": "ITS JPO's Connected Vehicle Pilot Deployment Program integrates connected vehicle research concepts into practical and effective elements to enhance existing operational capabilities. Data were collected throughout each pilot to facilitate independent evaluations of the use of connected vehicle technology on real roadways.\n\nTo encourage additional study and reuse of these data, ITS DataHub has partnered with each pilot site to make sanitized and anonymized tabular and non-tabular data from these projects available to the public. This article gives you a brief overview of what each pilot focused on and what types of CV Pilot data and tools are available on ITS DataHub.",
+            "identifier": "https://data.transportation.gov/api/views/hr8h-ufhq",
             "issued": "2020-05-27",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-27",
             "keyword": [
                 "arterial",
                 "automobiles",
@@ -57651,47 +57655,33 @@
                 "wyoming cv pilot",
                 "wyoming department of transportation (wydot)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/hr8h-ufhq",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/",
+            "modified": "2020-05-27",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Department of Transportation"
             },
-            "identifier": "https://data.transportation.gov/api/views/hr8h-ufhq",
-            "description": "ITS JPO's Connected Vehicle Pilot Deployment Program integrates connected vehicle research concepts into practical and effective elements to enhance existing operational capabilities. Data were collected throughout each pilot to facilitate independent evaluations of the use of connected vehicle technology on real roadways.\n\nTo encourage additional study and reuse of these data, ITS DataHub has partnered with each pilot site to make sanitized and anonymized tabular and non-tabular data from these projects available to the public. This article gives you a brief overview of what each pilot focused on and what types of CV Pilot data and tools are available on ITS DataHub.",
-            "title": "Connected Vehicle Pilot (CVP) Open Data",
-            "programCode": [
-                "021:013"
-            ],
-            "license": "http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Connected Vehicle Pilot (CVP) Open Data"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/hrkg-myni",
-            "issued": "2023-02-04",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/hrkg-myni",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "UP",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57699,90 +57689,87 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hrkg-myni/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hrkg-myni/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hrkg-myni/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/hrkg-myni/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hrkg-myni/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hrkg-myni/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hrkg-myni/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hrkg-myni/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hrkg-myni/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/hrkg-myni",
+            "issued": "2023-02-04",
+            "landingPage": "https://data.transportation.gov/d/hrkg-myni",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "UP"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/hsik-vfxx",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This section is intended to provide detailed information about some of the terms found on the FRA Safety Data site. Many of these definitions, and more detailed explanations, can be found in FRA Guide for Preparing Accident/Incident Reports.",
+            "identifier": "https://data.transportation.gov/api/views/hsik-vfxx",
             "issued": "2023-08-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-22",
             "keyword": [
                 "data",
                 "definitions",
                 "explanations",
                 "terms"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/hsik-vfxx",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-10-22",
+            "programCode": [
+                "021:036"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Railroad Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/hsik-vfxx",
-            "description": "This section is intended to provide detailed information about some of the terms found on the FRA Safety Data site. Many of these definitions, and more detailed explanations, can be found in FRA Guide for Preparing Accident/Incident Reports.",
-            "title": "Data Definitions",
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
+            "title": "Data Definitions"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/hswt-qvr8",
-            "issued": "2024-07-05",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-23",
-            "keyword": [
-                "security"
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
-            "identifier": "https://data.transportation.gov/api/views/hswt-qvr8",
             "description": "Data collected on the SS-30 form. \n\nTransit agencies report to the NTD security personnel in terms of Full-Time Equivalents (FTE) according to the staffing levels at the beginning of the year. One FTE typically works 40 hours per week. An agency may use any  reasonable method to allocate personnel across modes, such as allocating based on modal ridership or on modal annual trips. In certain instances, agencies may base personnel numbers on the prior year\u2019s total hours worked.",
-            "title": "Transit Agency Security Personnel",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57790,56 +57777,56 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hswt-qvr8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hswt-qvr8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hswt-qvr8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/hswt-qvr8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hswt-qvr8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hswt-qvr8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hswt-qvr8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hswt-qvr8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hswt-qvr8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/hswt-qvr8",
+            "issued": "2024-07-05",
+            "keyword": [
+                "security"
+            ],
+            "landingPage": "https://data.transportation.gov/d/hswt-qvr8",
             "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2025-01-23",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "Transit Agency Security Personnel"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/ht7p-2x5y",
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
-            "identifier": "https://data.transportation.gov/api/views/ht7p-2x5y",
             "description": "",
-            "title": "Number of Terminals Handling Containerships with On-Dock Rail at the Top 25 Container Ports: 2023",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57847,40 +57834,52 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ht7p-2x5y/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ht7p-2x5y/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ht7p-2x5y/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ht7p-2x5y/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ht7p-2x5y/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ht7p-2x5y/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ht7p-2x5y/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ht7p-2x5y/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ht7p-2x5y/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "https://data.transportation.gov/api/views/ht7p-2x5y",
+            "issued": "2024-01-10",
+            "landingPage": "https://data.transportation.gov/d/ht7p-2x5y",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-01-10",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Number of Terminals Handling Containerships with On-Dock Rail at the Top 25 Container Ports: 2023"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ht8q-b5eg",
-            "issued": "2021-04-28",
             "@type": "dcat:Dataset",
-            "modified": "2024-12-09",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Chambers",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "PPFSP 23",
+            "identifier": "https://data.transportation.gov/api/views/ht8q-b5eg",
+            "issued": "2021-04-28",
             "keyword": [
                 "bureau",
                 "container",
@@ -57898,24 +57897,37 @@
                 "transportation",
                 "vessel"
             ],
-            "identifier": "https://data.transportation.gov/api/views/ht8q-b5eg",
+            "landingPage": "https://data.transportation.gov/d/ht8q-b5eg",
+            "modified": "2024-12-09",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "PPFSP 23",
             "title": "A Port's Role"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/htmy-j8sh",
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
+            "description": "The files in this data environment were produced using the Vehicle Awareness Device (VAD) installed on one test vehicle over a two month period. The VAD installed in the test car is identical to the VADs installed in over 2800 vehicles participating in the Safety Pilot Model Demonstration conducted from August 2012 through August 2013 by the National Highway Traffic Safety Administration (NHTSA) in Ann Arbor, Michigan.\r\n\r\nThis legacy dataset was created before data.transportation.gov and is only currently available via the attached file(s). Please contact the dataset owner if there is a need for users to work with this data using the data.transportation.gov analysis features (online viewing, API, graphing, etc.) and the USDOT will consider modifying the dataset to fully integrate in data.transportation.gov.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/download/htmy-j8sh/application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/htmy-j8sh",
             "issued": "2013-01-31",
-            "@type": "dcat:Dataset",
-            "temporal": "2012-10-18/2012-12-19",
-            "modified": "2013-01-31",
             "keyword": [
                 "ann arbor",
                 "basic safety message (bsm)",
@@ -57932,79 +57944,47 @@
                 "vehicle awareness device (vad)",
                 "virginia"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/htmy-j8sh",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://creativecommons.org/licenses/by-nc-sa/3.0/legalcode",
+            "modified": "2013-01-31",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Department of Transportation"
             },
-            "identifier": "https://data.transportation.gov/api/views/htmy-j8sh",
-            "description": "The files in this data environment were produced using the Vehicle Awareness Device (VAD) installed on one test vehicle over a two month period. The VAD installed in the test car is identical to the VADs installed in over 2800 vehicles participating in the Safety Pilot Model Demonstration conducted from August 2012 through August 2013 by the National Highway Traffic Safety Administration (NHTSA) in Ann Arbor, Michigan.\r\n\r\nThis legacy dataset was created before data.transportation.gov and is only currently available via the attached file(s). Please contact the dataset owner if there is a need for users to work with this data using the data.transportation.gov analysis features (online viewing, API, graphing, etc.) and the USDOT will consider modifying the dataset to fully integrate in data.transportation.gov.",
-            "title": "Vehicle Awareness Device Data from Leesburg, Virginia",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/download/htmy-j8sh/application/vnd.openxmlformats-officedocument.wordprocessingml.document",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
-                }
-            ],
             "spatial": "Leesburg Virginia, Northern Virginia, Washington D.C. area, Ann Arbor Michigan, Interstate 70",
-            "dataQuality": true,
-            "license": "http://creativecommons.org/licenses/by-nc-sa/3.0/legalcode",
-            "accrualPeriodicity": "irregular",
+            "temporal": "2012-10-18/2012-12-19",
             "theme": [
                 "Research and Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Vehicle Awareness Device Data from Leesburg, Virginia"
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
-            "landingPage": "https://data.transportation.gov/d/htum-kus7",
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
-            "identifier": "81.3",
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
@@ -58013,75 +57993,84 @@
                     "title": "NHTSA API"
                 }
             ],
-            "spatial": "N/A",
-            "describedBy": "http://www-odi.nhtsa.dot.gov/downloads/folders/Complaints/CMPL.txt",
-            "dataQuality": true,
+            "identifier": "81.3",
+            "isPartOf": "DOT-81",
+            "issued": "2002-12-16",
+            "keyword": [
+                "complaints",
+                "email",
+                "paper",
+                "phone",
+                "safercar.gov"
+            ],
+            "landingPage": "https://data.transportation.gov/d/htum-kus7",
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
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/hv4w-5ua8",
-            "issued": "2022-01-12",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-12",
-            "keyword": [
-                "port performance"
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
-            "identifier": "https://data.transportation.gov/api/views/hv4w-5ua8",
             "description": "",
-            "title": "U.S.-International Trade Transported by Water (in U.S. dollars)",
+            "identifier": "https://data.transportation.gov/api/views/hv4w-5ua8",
+            "issued": "2022-01-12",
+            "keyword": [
+                "port performance"
+            ],
+            "landingPage": "https://data.transportation.gov/d/hv4w-5ua8",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2022-01-12",
             "programCode": [
                 "021:053"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "U.S.-International Trade Transported by Water (in U.S. dollars)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/hvq3-38u5",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2022-06-06",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-24",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Todd Solomon",
                 "hasEmail": "mailto:todd.solomon@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/hvq3-38u5",
+            "dataQuality": true,
             "description": "The number of Persons Screened by TSA, US Domestic Flight Departures, and US International Flight Departures by day from January 1, 2019 forward. Bonus columns for filtering include Week Number and Year.",
-            "title": "Commercial Aviation Departures and TSA Screenings (simplified)",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58089,73 +58078,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hvq3-38u5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hvq3-38u5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hvq3-38u5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/hvq3-38u5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hvq3-38u5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hvq3-38u5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hvq3-38u5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hvq3-38u5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hvq3-38u5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/hvq3-38u5",
+            "issued": "2022-06-06",
+            "landingPage": "https://data.transportation.gov/d/hvq3-38u5",
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
+            "spatial": "United States",
             "theme": [
                 "Aviation"
             ],
-            "phone": "2023660573",
-            "language": [
-                "en-US"
-            ]
+            "title": "Commercial Aviation Departures and TSA Screenings (simplified)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/statistics.cfm",
+            "accrualPeriodicity": "Annual",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2019-01-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-10",
-            "keyword": [
-                "automobiles",
-                "buses",
-                "motorcycles",
-                "motor vehicles",
-                "registrations",
-                "state",
-                "trucks"
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
-            "identifier": "https://data.transportation.gov/api/views/hwtm-7xmz",
+            "dataQuality": true,
             "description": "Annual motor vehicle registrations by vehicle type and state, from Highway Statistics table MV-1.",
-            "title": "Motor Vehicle Registrations, by vehicle type and state",
-            "isPartOf": "Highway Statistics",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58163,51 +58142,86 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hwtm-7xmz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hwtm-7xmz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hwtm-7xmz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/hwtm-7xmz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hwtm-7xmz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hwtm-7xmz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/hwtm-7xmz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/hwtm-7xmz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/hwtm-7xmz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/hwtm-7xmz",
+            "isPartOf": "Highway Statistics",
+            "issued": "2019-01-02",
+            "keyword": [
+                "automobiles",
+                "buses",
+                "motorcycles",
+                "motor vehicles",
+                "registrations",
+                "state",
+                "trucks"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/statistics.cfm",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annual",
+            "modified": "2024-12-10",
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
+            "title": "Motor Vehicle Registrations, by vehicle type and state"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
+            "agencyProgramURL": "http://www,transportation.gov/digitalstrategy/",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/hy26-vvg2",
-            "issued": "2015-11-30",
-            "temporal": "R/2011-10-01/P3M",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative - Financial",
             "collectionInstrument": "Federal Government Finances and Employment",
-            "modified": "2024-11-14",
-            "references": [
-                "https://management.cio.gov/schemaexamples/costSavingsAvoidanceSchema.json"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DOT Socrata",
+                "hasEmail": "mailto:Socrata@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://management.cio.gov/schemaexamples/costSavingsAvoidanceSchema.json",
+            "describedByType": "application/json",
+            "description": "IT Reform Cost Savings/Avoidance for the Department of Transportation provides information about cost savings and/or avoidances realized from IT reforms. Cost savings represent reductions in actual expenditures below the projected level of costs to achieve a specific objective. Cost avoidance represents an action taken in the immediate time frame that will decrease costs in the future",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.transportation.gov/digitalstrategy/costsavings.json",
+                    "mediaType": "application/json",
+                    "title": "JSON"
+                }
             ],
+            "identifier": "1861.0",
+            "issued": "2015-11-30",
             "keyword": [
                 "avoidance",
                 "cost",
@@ -58215,61 +58229,62 @@
                 "oversight",
                 "reform",
                 "savings",
-                "technology"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DOT Socrata",
-                "hasEmail": "mailto:Socrata@dot.gov"
-            },
-            "identifier": "1861.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
-            "description": "IT Reform Cost Savings/Avoidance for the Department of Transportation provides information about cost savings and/or avoidances realized from IT reforms. Cost savings represent reductions in actual expenditures below the projected level of costs to achieve a specific objective. Cost avoidance represents an action taken in the immediate time frame that will decrease costs in the future",
-            "title": "DOT IT Cost Savings and Avoidance - JSON",
-            "agencyProgramURL": "http://www,transportation.gov/digitalstrategy/",
-            "describedByType": "application/json",
+                "technology"
+            ],
+            "landingPage": "https://data.transportation.gov/d/hy26-vvg2",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-14",
+            "phone": "202-366-9201",
             "primaryITInvestmentUII": "021-748752384",
             "programCode": [
                 "021:058"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.transportation.gov/digitalstrategy/costsavings.json",
-                    "mediaType": "application/json",
-                    "title": "JSON"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "references": [
+                "https://management.cio.gov/schemaexamples/costSavingsAvoidanceSchema.json"
             ],
-            "describedBy": "https://management.cio.gov/schemaexamples/costSavingsAvoidanceSchema.json",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "temporal": "R/2011-10-01/P3M",
             "theme": [
                 "Federal Government Finances and Employment"
             ],
-            "accrualPeriodicity": "R/P3M",
-            "categoryDesignation": "Administrative - Financial",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-9201"
+            "title": "DOT IT Cost Savings and Avoidance - JSON"
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
-            "landingPage": "https://data.transportation.gov/d/hy9d-cdy5",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/07aprtvt/07aprtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "April 2007"
+                }
             ],
+            "identifier": "18.89",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -58279,104 +58294,68 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.89",
+            "landingPage": "https://data.transportation.gov/d/hy9d-cdy5",
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
-            "title": "Monthly Traffic Volume Trends - April 2007",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/07aprtvt/07aprtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "April 2007"
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
+            "title": "Monthly Traffic Volume Trends - April 2007"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/hymt-hxbk",
-            "issued": "2022-01-09",
             "@type": "dcat:Dataset",
-            "modified": "2023-01-06",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Todd Solomon",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/hymt-hxbk",
+            "issued": "2022-01-09",
+            "landingPage": "https://data.transportation.gov/d/hymt-hxbk",
+            "modified": "2023-01-06",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "National Transit Map for TRB"
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
-            "landingPage": "https://data.transportation.gov/d/i23j-t8it",
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
-            "identifier": "524.17",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
             "description": "STATE DATA REPORTING SYSTEMS. Annual reports on the Fatality Analysis Reporting System (FARS) which is data regarding fatalities that is collected by a FARS analyst from each State and provided to NHTSA.",
-            "title": "GES Reports - 1996",
-            "isPartOf": "DOT-524",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58385,39 +58364,50 @@
                     "title": "1996"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
-            "dataQuality": true,
+            "identifier": "524.17",
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
+            "landingPage": "https://data.transportation.gov/d/i23j-t8it",
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
+            "title": "GES Reports - 1996"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/i3yt-fwrx",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/i3yt-fwrx",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "BNSF Trackage Rights",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58425,45 +58415,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/i3yt-fwrx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/i3yt-fwrx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/i3yt-fwrx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/i3yt-fwrx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/i3yt-fwrx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/i3yt-fwrx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/i3yt-fwrx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/i3yt-fwrx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/i3yt-fwrx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/i3yt-fwrx",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/i3yt-fwrx",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "BNSF Trackage Rights"
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
-            "landingPage": "https://data.transportation.gov/d/i4d3-bx93",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/06octtvt/06octtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "October 2006"
+                }
             ],
+            "identifier": "18.95",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -58473,133 +58488,133 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.95",
+            "landingPage": "https://data.transportation.gov/d/i4d3-bx93",
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
-            "title": "Monthly Traffic Volume Trends - October 2006",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/06octtvt/06octtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "October 2006"
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
+            "title": "Monthly Traffic Volume Trends - October 2006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/i547-g469",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Economic concepts related to transportation investment",
+            "identifier": "https://data.transportation.gov/api/views/i547-g469",
             "issued": "2020-02-24",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
             "keyword": [
                 "transportation assets",
                 "transportation economics",
                 "transportation investment"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/i547-g469",
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
-            "identifier": "https://data.transportation.gov/api/views/i547-g469",
-            "description": "Economic concepts related to transportation investment",
-            "title": "Transportation Economic Concepts: Value of Transportation - Investment",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Transportation Economic Concepts: Value of Transportation - Investment"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/i5dw-jvsi",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRA Safety Data Team",
+                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This is the landing page for Form 6180.57 Highway-Rail Grade Crossing Accident/Incident data.",
+            "identifier": "https://data.transportation.gov/api/views/i5dw-jvsi",
             "issued": "2024-11-22",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "form 57",
                 "grade crossing incident",
                 "highway-rail incident"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRA Safety Data Team",
-                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/i5dw-jvsi",
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
-            "identifier": "https://data.transportation.gov/api/views/i5dw-jvsi",
-            "description": "This is the landing page for Form 6180.57 Highway-Rail Grade Crossing Accident/Incident data.",
-            "title": "Form 57 Data Downloads",
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
+            "title": "Form 57 Data Downloads"
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
-            "landingPage": "https://data.transportation.gov/d/i5sp-tsge",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/14martvt/14martvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "March 2014"
+                }
             ],
+            "identifier": "18.60",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -58609,82 +58624,47 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.60",
+            "landingPage": "https://data.transportation.gov/d/i5sp-tsge",
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
-            "title": "Monthly Traffic Volume Trends - March 2014",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/14martvt/14martvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "March 2014"
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
+            "title": "Monthly Traffic Volume Trends - March 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/i5x2-a58r",
+            "accrualPeriodicity": "R/PT1S",
+            "agencyProgramURL": "https://resourcecenter.911.gov/code/home.aspx",
             "bureauCode": [
                 "021:18"
             ],
-            "issued": "2018-12-18",
-            "temporal": "R/2013/PT1S",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-01",
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
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "identifier": "DOT-416",
+            "dataQuality": false,
             "description": "Collect and aggregate information from state level reporting entities that can be used to measure the progress of 9 1-1 authorities across the country in enhancing their existing operations and migrating to more advanced - Internet-Protocol-enabled emergency networks. The data will be maintained in a \"National 9-1-1 Profile Database.\" One of the objectives of the National 9-1-1 Program is to develop, collect, and disseminate information concerning practices, procedures, and technology used in the implementation of E9 1 1 services and to support 9-1-1 Public Safety Answering Points (PSAPs) and related state and local public safety agencies for 9 1 1 deployment and operations. The National 9-1-1 profile database can be used to follow the progress of 9-1-1 authorities in enhancing their existing systems and implementing next-generation networks for more advanced systems.",
-            "title": "National 9-1-1 Profile Database",
-            "agencyProgramURL": "https://resourcecenter.911.gov/code/home.aspx",
-            "programCode": [
-                "021:031"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58693,28 +58673,81 @@
                     "title": "National 9-1-1 Profile Database"
                 }
             ],
-            "dataQuality": false,
+            "identifier": "DOT-416",
+            "issued": "2018-12-18",
+            "keyword": [
+                "911",
+                "9-11",
+                "9-1-1",
+                "information clearinghouse",
+                "psap",
+                "public safety answering points",
+                "resource center"
+            ],
+            "landingPage": "https://data.transportation.gov/d/i5x2-a58r",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "accrualPeriodicity": "R/PT1S",
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
             "theme": [
                 "Transportation"
             ],
-            "categoryDesignation": "Research",
-            "phone": "202-366-2705",
-            "language": [
-                "en-US"
-            ]
+            "title": "National 9-1-1 Profile Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/i5z4-qh9m",
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
+            "description": "During the 2014 ITS World Congress a demonstration of the connected vehicle infrastructure in the City of Detroit was conducted.  The test site included approximately 14 intersections around Detroit\u2019s COBO convention center and involved 9 equipped vehicles. The Vehicle Situation Data (VSD) data set includes a series of data files that recorded vehicle situational data that were generated by an equipped vehicle. During the ITS World Congress, VSDs were encoded with one of two schemas. The dataset contains decoded data using both 2.0 and 2.1 ASN.1 schemas.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/api/views/i5z4-qh9m/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.transportation.gov/api/views/i5z4-qh9m/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.transportation.gov/api/views/i5z4-qh9m/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.transportation.gov/api/views/i5z4-qh9m/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.transportation.gov/api/views/i5z4-qh9m/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.transportation.gov/api/views/i5z4-qh9m/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.transportation.gov/api/views/i5z4-qh9m/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/i5z4-qh9m",
             "issued": "2015-01-31",
-            "@type": "dcat:Dataset",
-            "temporal": "2014-09-08/2014-09-10",
-            "modified": "2015-01-31",
             "keyword": [
                 "2014 its world congress (itswc) connected vehicle (cv) test bed demonstration",
                 "application message",
@@ -58731,66 +58764,37 @@
                 "signal phase and timing (spat)",
                 "vehicle situation data (vsd)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "USDOT"
-            },
-            "identifier": "https://data.transportation.gov/api/views/i5z4-qh9m",
-            "description": "During the 2014 ITS World Congress a demonstration of the connected vehicle infrastructure in the City of Detroit was conducted.  The test site included approximately 14 intersections around Detroit\u2019s COBO convention center and involved 9 equipped vehicles. The Vehicle Situation Data (VSD) data set includes a series of data files that recorded vehicle situational data that were generated by an equipped vehicle. During the ITS World Congress, VSDs were encoded with one of two schemas. The dataset contains decoded data using both 2.0 and 2.1 ASN.1 schemas.",
-            "title": "2014 ITS World Congress Connected Vehicle Test Bed Demonstration Vehicle Situation Data",
+            "landingPage": "https://data.transportation.gov/d/i5z4-qh9m",
+            "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
+            "modified": "2015-01-31",
             "programCode": [
                 "021:013"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/api/views/i5z4-qh9m/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/i5z4-qh9m/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.transportation.gov/api/views/i5z4-qh9m/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/i5z4-qh9m/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.transportation.gov/api/views/i5z4-qh9m/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "USDOT"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/i5z4-qh9m/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.transportation.gov/api/views/i5z4-qh9m/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
             "spatial": "Detroit, Michigan",
-            "dataQuality": true,
-            "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "irregular",
+            "temporal": "2014-09-08/2014-09-10",
             "theme": [
                 "Automobiles"
-            ]
+            ],
+            "title": "2014 ITS World Congress Connected Vehicle Test Bed Demonstration Vehicle Situation Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/i5zb-xe34",
             "bureauCode": [
                 "021:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kate Hartman",
+                "hasEmail": "mailto:kate.hartman@dot.gov"
+            },
+            "description": "ITS DataHub has partnered with the Federal Highway Administration's (FHWA's) Next Generation SIMulation (NGSIM) program to make available detailed vehicle trajectory data and supporting data files along with the raw and processed video files from the NGSIM data collection efforts. Researchers for the NGSIM program collected the specified data on southbound US 101 and Lankershim Boulevard in Los Angeles, CA, eastbound I-80 in Emeryville, CA and Peachtree Street in Atlanta, GA.\r\n\r\nThis article provides a brief overview of the NGSIM program data collection as well as what types of data are available on ITS DataHub. Some examples of possible uses for the data and information on how to cite the various NGSIM datasets are also included.",
+            "identifier": "https://data.transportation.gov/api/views/i5zb-xe34",
             "issued": "2022-04-21",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
             "keyword": [
                 "arterial",
                 "behavioral algorithm",
@@ -58813,38 +58817,38 @@
                 "us 101",
                 "video"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/i5zb-xe34",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
+            "modified": "2022-04-28",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Department of Transportation"
             },
-            "identifier": "https://data.transportation.gov/api/views/i5zb-xe34",
-            "description": "ITS DataHub has partnered with the Federal Highway Administration's (FHWA's) Next Generation SIMulation (NGSIM) program to make available detailed vehicle trajectory data and supporting data files along with the raw and processed video files from the NGSIM data collection efforts. Researchers for the NGSIM program collected the specified data on southbound US 101 and Lankershim Boulevard in Los Angeles, CA, eastbound I-80 in Emeryville, CA and Peachtree Street in Atlanta, GA.\r\n\r\nThis article provides a brief overview of the NGSIM program data collection as well as what types of data are available on ITS DataHub. Some examples of possible uses for the data and information on how to cite the various NGSIM datasets are also included.",
-            "title": "Next Generation Simulation (NGSIM) Open Data",
-            "programCode": [
-                "021:013"
-            ],
-            "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Next Generation Simulation (NGSIM) Open Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/i6n5-pght",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "A look at the producer price index for transportation and its components as a measure of inflation faced by consumers.",
+            "identifier": "https://data.transportation.gov/api/views/i6n5-pght",
             "issued": "2024-04-04",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
             "keyword": [
                 "consumer price index",
                 "cpi",
@@ -58852,60 +58856,74 @@
                 "inflation and transportation",
                 "transportation inflation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/i6n5-pght",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-18",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/i6n5-pght",
-            "description": "A look at the producer price index for transportation and its components as a measure of inflation faced by consumers.",
-            "title": "Transportation and Inflation - PPI",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Transportation and Inflation - PPI"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/i75f-g5dh",
-            "issued": "2023-12-22",
             "@type": "dcat:Dataset",
-            "modified": "2024-04-15",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
+            "description": "NHTSA Vehicle Recalls Completion Rates",
             "identifier": "https://data.transportation.gov/api/views/i75f-g5dh",
+            "issued": "2023-12-22",
+            "landingPage": "https://data.transportation.gov/d/i75f-g5dh",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-04-15",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "NHTSA Vehicle Recalls Completion Rates",
-            "title": "NHTSA Vehicle Recalls Completion Rates",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "theme": [
                 "Automobiles"
-            ]
+            ],
+            "title": "NHTSA Vehicle Recalls Completion Rates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/i77x-pzye",
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
+                    "description": "2012 Louisiana HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/louisiana2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Louisiana"
+                }
+            ],
+            "identifier": "678.72",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -58919,60 +58937,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.72",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Louisiana",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/i77x-pzye",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/louisiana2012.zip",
-                    "description": "2012 Louisiana HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Louisiana"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Louisiana"
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
-            "landingPage": "https://data.transportation.gov/d/i987-tnag",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/05jultvt/05jultvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "July 2005"
+                }
             ],
+            "identifier": "18.110",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -58982,60 +58997,60 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.110",
+            "landingPage": "https://data.transportation.gov/d/i987-tnag",
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
-            "title": "Monthly Traffic Volume Trends - July 2005",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/05jultvt/05jultvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "July 2005"
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
+            "title": "Monthly Traffic Volume Trends - July 2005"
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
-            "landingPage": "https://data.transportation.gov/d/i9bg-q58y",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/08dectvt/08dectvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "December 2008"
+                }
             ],
+            "identifier": "18.69",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -59045,60 +59060,61 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.69",
+            "landingPage": "https://data.transportation.gov/d/i9bg-q58y",
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
-            "title": "Monthly Traffic Volume Trends - December 2008",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/08dectvt/08dectvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "December 2008"
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
+            "title": "Monthly Traffic Volume Trends - December 2008"
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
-            "landingPage": "https://data.transportation.gov/d/i9h5-e3pm",
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
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/tenyr1a.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Ten Year Accident/Incident Overview by Railroad"
+                }
             ],
+            "identifier": "199.6",
+            "isPartOf": "DOT-199",
+            "issued": "2010-09-29",
             "keyword": [
                 "acts of god",
                 "collisions",
@@ -59109,57 +59125,44 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "199.6",
+            "landingPage": "https://data.transportation.gov/d/i9h5-e3pm",
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
-            "title": "Rail Equipment Accidents - Ten Year Accident/Incident Overview by Railroad",
-            "isPartOf": "DOT-199",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:036"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/tenyr1a.aspx",
-                    "mediaType": "text/csv",
-                    "title": "Ten Year Accident/Incident Overview by Railroad"
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
+            "title": "Rail Equipment Accidents - Ten Year Accident/Incident Overview by Railroad"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/iaad-fgzc",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Janine McFadden",
+                "hasEmail": "mailto:janine.mcfadden@dot.gov"
+            },
+            "description": "Interactive web map to view, query, and download ferry terminal and segment data",
+            "identifier": "https://data.transportation.gov/api/views/iaad-fgzc",
             "issued": "2020-04-15",
-            "temporal": "2017-01-01/2017-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-18",
             "keyword": [
                 "census",
                 "ferry",
@@ -59171,50 +59174,34 @@
                 "transit",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Janine McFadden",
-                "hasEmail": "mailto:janine.mcfadden@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/iaad-fgzc",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2020-11-18",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/iaad-fgzc",
-            "description": "Interactive web map to view, query, and download ferry terminal and segment data",
-            "title": "National Census of Ferry Operators (NCFO) 2018: Map",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "temporal": "2017-01-01/2017-12-31",
             "theme": [
                 "Ferry Transit"
-            ]
+            ],
+            "title": "National Census of Ferry Operators (NCFO) 2018: Map"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/iahn-a7j4",
-            "issued": "2024-01-12",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-12",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "TBD",
                 "hasEmail": "mailto:sean.jahanmir@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/iahn-a7j4",
             "description": "",
-            "title": "20-Foot Equivalent Units (TEU) Handled by Select U.S. Container Ports January 2020 to August 2023",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59222,43 +59209,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/iahn-a7j4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/iahn-a7j4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/iahn-a7j4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/iahn-a7j4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/iahn-a7j4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/iahn-a7j4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/iahn-a7j4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/iahn-a7j4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/iahn-a7j4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "https://data.transportation.gov/api/views/iahn-a7j4",
+            "issued": "2024-01-12",
+            "landingPage": "https://data.transportation.gov/d/iahn-a7j4",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-01-12",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "20-Foot Equivalent Units (TEU) Handled by Select U.S. Container Ports January 2020 to August 2023"
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
-            "landingPage": "https://data.transportation.gov/d/iavd-apfw",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/05juntvt/05juntvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "June 2005"
+                }
             ],
+            "identifier": "18.111",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -59268,85 +59283,50 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.111",
+            "landingPage": "https://data.transportation.gov/d/iavd-apfw",
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
-            "title": "Monthly Traffic Volume Trends - June 2005",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/05juntvt/05juntvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "June 2005"
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
+            "title": "Monthly Traffic Volume Trends - June 2005"
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
-            "landingPage": "https://data.transportation.gov/d/iaz4-xbwa",
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
-            "identifier": "693.7",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
             "description": "The NBI System is the collection of bridge inspection information and costs associated with bridge replacements of structurally deficient bridges on and off the NHS. This data is collected under the auspices of the National Bridge Inspection Standards (NBIS) as prescribed by law. The NBI System collects the information that is used to determine eligibility for NHS projects, performance measure reporting, NHS penalty determination, and reporting to Congress.  It supports oversight of the NBIS through various report tools, and provides data reporting that supports agency strategic goals.",
-            "title": "National Bridge Inventory System (NBI) - 1998",
-            "isPartOf": "DOT-693",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
-            "primaryITInvestmentUII": "021-012940226",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59355,33 +59335,71 @@
                     "title": "1998"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
-            "dataQuality": true,
+            "identifier": "693.7",
+            "isPartOf": "DOT-693",
+            "issued": "1992-12-31",
+            "keyword": [
+                "bridge",
+                "condition",
+                "deck",
+                "inspection",
+                "structure"
+            ],
+            "landingPage": "https://data.transportation.gov/d/iaz4-xbwa",
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
+            "title": "National Bridge Inventory System (NBI) - 1998"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/iber-xk5u",
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
+                    "description": "2012 Ohio HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/ohio2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Ohio"
+                }
+            ],
+            "identifier": "678.89",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -59395,64 +59413,36 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.89",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Ohio",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/iber-xk5u",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/ohio2012.zip",
-                    "description": "2012 Ohio HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Ohio"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Ohio"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ibhd-47st",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/ibhd-47st",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "Amtrak",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59460,45 +59450,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ibhd-47st/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ibhd-47st/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ibhd-47st/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ibhd-47st/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ibhd-47st/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ibhd-47st/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ibhd-47st/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ibhd-47st/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ibhd-47st/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/ibhd-47st",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/ibhd-47st",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Amtrak"
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
-            "landingPage": "https://data.transportation.gov/d/ibw4-njph",
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
+                    "downloadURL": "https://cms.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/docs/closedByEnforcement_FY2006_04-26-2013.xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Fiscal Year 2006"
+                }
             ],
+            "identifier": "96.5",
+            "isPartOf": "DOT-96",
+            "issued": "2018-12-17",
             "keyword": [
                 "bus",
                 "civil penalties",
@@ -59511,60 +59526,60 @@
                 "motor carrier",
                 "truck"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "96.5",
+            "landingPage": "https://data.transportation.gov/d/ibw4-njph",
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
-            "title": "Closed Enforcement Cases - Fiscal Year 2006",
-            "isPartOf": "DOT-96",
-            "agencyProgramURL": "http://www.fmcsa.dot.gov/regulations/enforcement/civil-penalties",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://cms.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/docs/closedByEnforcement_FY2006_04-26-2013.xlsx",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "Fiscal Year 2006"
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
+            "title": "Closed Enforcement Cases - Fiscal Year 2006"
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
-            "landingPage": "https://data.transportation.gov/d/ic5n-t47m",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/06febtvt/06febtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "February 2006"
+                }
             ],
+            "identifier": "18.103",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -59574,64 +59589,39 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.103",
+            "landingPage": "https://data.transportation.gov/d/ic5n-t47m",
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
-            "title": "Monthly Traffic Volume Trends - February 2006",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/06febtvt/06febtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "February 2006"
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
+            "title": "Monthly Traffic Volume Trends - February 2006"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/icqf-xf4w",
-            "issued": "2023-04-03",
             "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
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
-            "identifier": "https://data.transportation.gov/api/views/icqf-xf4w",
             "description": "This dataset is the source dataset and contains raw data values. It will replace the current data download (https://safetydata.fra.dot.gov/OfficeofSafety/publicsite/on_the_fly_download.aspx) when the safetydata.fra.dot.gov site is decommissioned in 2024. To download data that contains data in a user-friendly human-readable format, please reference https://data.transportation.gov/Railroads/Highway-Rail-Grade-Crossing-Accident-Data/7wn6-i5b9.",
-            "title": "Highway-Rail Grade Crossing Accident/Incident Source Data (Form 57)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59639,46 +59629,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/icqf-xf4w/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/icqf-xf4w/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/icqf-xf4w/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/icqf-xf4w/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/icqf-xf4w/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/icqf-xf4w/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/icqf-xf4w/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/icqf-xf4w/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/icqf-xf4w/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/icqf-xf4w",
+            "issued": "2023-04-03",
+            "landingPage": "https://data.transportation.gov/d/icqf-xf4w",
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
+            "title": "Highway-Rail Grade Crossing Accident/Incident Source Data (Form 57)"
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
-            "landingPage": "https://data.transportation.gov/d/iczc-v3zy",
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
+                    "description": "This access point provides access to the LTPP InfoPave data mapping features including sections by location, data by location, and geospatial analysis.",
+                    "downloadURL": "https://infopave.fhwa.dot.gov/%3FGoto=Map",
+                    "mediaType": "application/zip",
+                    "title": "Map"
+                }
             ],
+            "identifier": "679.6",
+            "isPartOf": "DOT-679",
+            "issued": "1993-07-01",
             "keyword": [
                 "asphalt concrete",
                 "continuously reinforced concrete pavement",
@@ -59695,119 +59711,79 @@
                 "texture",
                 "traffic loading"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "679.6",
+            "landingPage": "https://data.transportation.gov/d/iczc-v3zy",
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
-            "title": "Long-Term Pavement Performance (LTPP) - Map",
-            "isPartOf": "DOT-679",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/research/tfhrc/programs/infrastructure/pavements/ltpp/",
-            "programCode": [
-                "021:009"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://infopave.fhwa.dot.gov/%3FGoto=Map",
-                    "description": "This access point provides access to the LTPP InfoPave data mapping features including sections by location, data by location, and geospatial analysis.",
-                    "@type": "dcat:Distribution",
-                    "title": "Map"
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
+            "title": "Long-Term Pavement Performance (LTPP) - Map"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ida7-k95k",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2020-03-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-29",
-            "keyword": [
-                "household spending",
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
-            "identifier": "https://data.transportation.gov/api/views/ida7-k95k",
             "description": "Average household spending",
-            "title": "Transportation Economic Trends: Transportation Spending - Average Household",
+            "identifier": "https://data.transportation.gov/api/views/ida7-k95k",
+            "issued": "2020-03-02",
+            "keyword": [
+                "household spending",
+                "transportation spending"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ida7-k95k",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-29",
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
+            "title": "Transportation Economic Trends: Transportation Spending - Average Household"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "The data set contains controlled unclassified procurement information, confidential business information, and information protected by statute or regulation.",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/idc6-qz39",
-            "issued": "2014-12-29",
-            "temporal": "R/2014-12-29/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "actual balance",
-                "budget balance",
-                "chart of accounts",
-                "encumbrance balance",
-                "event time stamps",
-                "journal entry",
-                "ledger relationships",
-                "united states standard general ledger",
-                "ussgl"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "736.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
-            "description": "Delphi general ledger contains the following data elements, but is not limited to the United States Standard General Ledger (USSGL) chart of accounts, stores actual, budget, and encumbrance balances for detail and summary accounts, event time stamps, stores journal entry source names and descriptions, and stores the relationships between ledgers.",
-            "title": "Delphi General Ledger -",
-            "primaryITInvestmentUII": "021-105731835",
-            "programCode": [
-                "021:058"
-            ],
+            "dataQuality": false,
+            "description": "Delphi general ledger contains the following data elements, but is not limited to the United States Standard General Ledger (USSGL) chart of accounts, stores actual, budget, and encumbrance balances for detail and summary accounts, event time stamps, stores journal entry source names and descriptions, and stores the relationships between ledgers.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59815,53 +59791,58 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "theme": [
-                "Transportation"
+            "identifier": "736.0",
+            "issued": "2014-12-29",
+            "keyword": [
+                "actual balance",
+                "budget balance",
+                "chart of accounts",
+                "encumbrance balance",
+                "event time stamps",
+                "journal entry",
+                "ledger relationships",
+                "united states standard general ledger",
+                "ussgl"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/idc6-qz39",
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
+            "title": "Delphi General Ledger -"
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
-            "landingPage": "https://data.transportation.gov/d/iea8-6j8u",
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
-            "identifier": "696.4",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "A compilation of historic documents and articles on the Interstate System, Federal-Aid Highway Program, FHWA, and transportation.",
-            "title": "Highway History - The Interstate System",
-            "isPartOf": "DOT-696",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/infrastructure/history.cfm",
-            "programCode": [
-                "021:011"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59870,30 +59851,67 @@
                     "title": "The Interstate System"
                 }
             ],
-            "spatial": "National",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "696.4",
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
+            "landingPage": "https://data.transportation.gov/d/iea8-6j8u",
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
+            "title": "Highway History - The Interstate System"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/ied2-3xq9",
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
+                    "description": "2012 Florida HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/florida2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Florida"
+                }
+            ],
+            "identifier": "678.63",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -59907,60 +59925,58 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.63",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Florida",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/ied2-3xq9",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/florida2012.zip",
-                    "description": "2012 Florida HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Florida"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Florida"
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
-            "landingPage": "https://data.transportation.gov/d/ieuq-74gr",
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
+            "identifier": "283.1",
+            "isPartOf": "DOT-283",
+            "issued": "2008-03-01",
             "keyword": [
                 "alertness",
                 "employee",
@@ -59971,61 +59987,60 @@
                 "sleep",
                 "work"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "283.1",
+            "landingPage": "https://data.transportation.gov/d/ieuq-74gr",
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
-            "title": "Work Schedules and Sleep Patterns of Railroad Employees - Dispatcher Background Survey",
-            "isPartOf": "DOT-283",
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
+            "title": "Work Schedules and Sleep Patterns of Railroad Employees - Dispatcher Background Survey"
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
-            "landingPage": "https://data.transportation.gov/d/igqg-mu6m",
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
+            "identifier": "112.1",
+            "isPartOf": "DOT-112",
+            "issued": "2018-12-17",
             "keyword": [
                 "bus",
                 "crash",
@@ -60042,57 +60057,60 @@
                 "motorcoach",
                 "towaway"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "112.1",
+            "landingPage": "https://data.transportation.gov/d/igqg-mu6m",
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
-            "title": "A&I - Crash Statistics - State Profiles",
-            "isPartOf": "DOT-112",
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
-            "categoryDesignation": "Research",
-            "analysisUnit": "Crash, Motor Carrier, State",
-            "phone": "202-366-2161",
-            "language": [
-                "en-US"
-            ]
+            "title": "A&I - Crash Statistics - State Profiles"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/ih33-5y7a",
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
+                    "description": "2012 Montana HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/montana2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Montana"
+                }
+            ],
+            "identifier": "678.80",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -60106,64 +60124,36 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.80",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Montana",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/ih33-5y7a",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/montana2012.zip",
-                    "description": "2012 Montana HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Montana"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Montana"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ih7m-y8tr",
-            "issued": "2023-04-06",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/ih7m-y8tr",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "Main Line Rail",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60171,58 +60161,53 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ih7m-y8tr/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ih7m-y8tr/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ih7m-y8tr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ih7m-y8tr/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ih7m-y8tr/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ih7m-y8tr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ih7m-y8tr/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ih7m-y8tr/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ih7m-y8tr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/ih7m-y8tr",
+            "issued": "2023-04-06",
+            "landingPage": "https://data.transportation.gov/d/ih7m-y8tr",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Main Line Rail"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ihrz-ddnk",
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
-            "identifier": "https://data.transportation.gov/api/views/ihrz-ddnk",
+            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMSS",
             "description": "State DOTs provide the location limits of highway sections to be used to represent statewide aggregations based on a statistically valid Sample Panel.\nThe Mid-America contains data for the following States: Illinois, Indiana, Iowa, Kansas, Michigan, Minnesota, Missouri, Nebraska, North Dakota, Oklahoma, South Dakota, Texas, and Wisconsin.",
-            "title": "Roadway Sections Mid-America 2019",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60230,73 +60215,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ihrz-ddnk/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ihrz-ddnk/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ihrz-ddnk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ihrz-ddnk/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ihrz-ddnk/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ihrz-ddnk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ihrz-ddnk/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ihrz-ddnk/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ihrz-ddnk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "USA",
-            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMSS",
+            "identifier": "https://data.transportation.gov/api/views/ihrz-ddnk",
+            "issued": "2020-12-28",
+            "landingPage": "https://data.transportation.gov/d/ihrz-ddnk",
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
+            "title": "Roadway Sections Mid-America 2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/iie8-uenj",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2023-08-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
-            "keyword": [
-                "advanced driver assistance system (adas)",
-                "automated vehicles",
-                "connected vehicles",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "naturalistic driving study",
-                "ohio",
-                "sae level 2",
-                "single-vehicle",
-                "vehicle interaction"
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
-            "identifier": "https://data.transportation.gov/api/views/iie8-uenj",
+            "dataQuality": true,
             "description": "The datasets contain the subject ADAS-equipped vehicle\u2019s trajectory collected in naturalistic traffic conditions in central Ohio. The instrumented subject vehicle was either a discreet or readily-identifiable ADAS-equipped vehicle with SAE L2 capabilities. The dataset also contains trajectories for adjacent vehicles in traffic (observed by the subject vehicle\u2019s onboard sensors).",
-            "title": "Advanced Driver Assistance System (ADAS)-Equipped Single-Vehicle Data for Central Ohio",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60304,60 +60280,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/iie8-uenj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/iie8-uenj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/iie8-uenj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/iie8-uenj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/iie8-uenj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/iie8-uenj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/iie8-uenj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/iie8-uenj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/iie8-uenj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/iie8-uenj",
+            "issued": "2023-08-23",
+            "keyword": [
+                "advanced driver assistance system (adas)",
+                "automated vehicles",
+                "connected vehicles",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "naturalistic driving study",
+                "ohio",
+                "sae level 2",
+                "single-vehicle",
+                "vehicle interaction"
+            ],
+            "landingPage": "https://data.transportation.gov/d/iie8-uenj",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-07",
+            "programCode": [
+                "021:042"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
             "spatial": "Central Ohio",
-            "dataQuality": true,
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Advanced Driver Assistance System (ADAS)-Equipped Single-Vehicle Data for Central Ohio"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/iiy2-kmkn",
-            "issued": "2024-01-12",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-12",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "TBD",
                 "hasEmail": "mailto:sean.jahanmir@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/iiy2-kmkn",
             "description": "",
-            "title": "Weekly Number of Container Ships Awaiting to Dock at All U.S. Ports: July 2021 to September 2023",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60365,63 +60352,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/iiy2-kmkn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/iiy2-kmkn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/iiy2-kmkn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/iiy2-kmkn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/iiy2-kmkn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/iiy2-kmkn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/iiy2-kmkn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/iiy2-kmkn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/iiy2-kmkn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "https://data.transportation.gov/api/views/iiy2-kmkn",
+            "issued": "2024-01-12",
+            "landingPage": "https://data.transportation.gov/d/iiy2-kmkn",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-01-12",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Weekly Number of Container Ships Awaiting to Dock at All U.S. Ports: July 2021 to September 2023"
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
-            "landingPage": "https://data.transportation.gov/d/ij39-zfnm",
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
-            "identifier": "1836.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
             "description": "SAS programs and auxiliary files used in report no. DOT HS 812 069, Lives Saved by Vehicle Safety Technologies & Associated FMVSS, 1960 to 2012 Passenger Cars & LTV's",
-            "title": "Lives Saved by Vehicle Safety Technologies and Associated Federal Motor Vehicle Safety Standards - 1960-2002 version",
-            "isPartOf": "DOT-1836",
-            "agencyProgramURL": "http://www-nrd.nhtsa.dot.gov/Pubs/812069.pdf",
-            "programCode": [
-                "021:031"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60430,62 +60414,49 @@
                     "title": "1960-2002 version"
                 }
             ],
-            "dataQuality": false,
+            "identifier": "1836.2",
+            "isPartOf": "DOT-1836",
+            "issued": "2015-01-31",
+            "keyword": [
+                "fars; statistical analysis; evaluation; benefits; effec-tiveness; fatality reduction; injury reduction; crashwor-thiness; crash avoidance"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ij39-zfnm",
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
+            "title": "Lives Saved by Vehicle Safety Technologies and Associated Federal Motor Vehicle Safety Standards - 1960-2002 version"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ij7i-psm5",
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
-                "connected vehicles",
-                "dedicated short range communication (dsrc)",
-                "field test",
-                "freeway",
-                "i-5",
-                "intelligent network flow optimization (inflo)",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "seattle",
-                "spd-warn",
-                "speed harmonization",
-                "traffic management entity-based speed harmonization",
-                "washington"
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
-            "identifier": "https://data.transportation.gov/api/views/ij7i-psm5",
+            "dataQuality": true,
             "description": "Data is from the small-scale demonstration of the Intelligent Network Flow Optimization (INFLO) Prototype System and applications in Seattle, Washington. Connected vehicle systems were deployed in 21 vehicles in a scripted driving scenario circuiting this I-5 corridor northbound and southbound during morning rush hour. This data set contains speed harmonization messages that were recommended by the INFLO SPD-HARM algorithm and sent by the traffic management center to the connected vehicles, which provided drivers with the suggested speed while driving on the segment of I-5 that was included in the test.  The objective of speed harmonization is to dynamically adjust and coordinate maximum appropriate vehicle speeds in response to downstream congestion, incidents, and weather or road conditions in order to maximize traffic throughput and reduce crashes.",
-            "title": "Intelligent Network Flow Optimization Prototype Traffic Management Entity-Based Speed Harmonization",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60493,52 +60464,95 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ij7i-psm5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ij7i-psm5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ij7i-psm5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ij7i-psm5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ij7i-psm5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ij7i-psm5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ij7i-psm5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ij7i-psm5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ij7i-psm5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Seattle, Washington",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/ij7i-psm5",
+            "issued": "2016-02-17",
+            "keyword": [
+                "application message",
+                "arterial",
+                "connected vehicles",
+                "dedicated short range communication (dsrc)",
+                "field test",
+                "freeway",
+                "i-5",
+                "intelligent network flow optimization (inflo)",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "seattle",
+                "spd-warn",
+                "speed harmonization",
+                "traffic management entity-based speed harmonization",
+                "washington"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ij7i-psm5",
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
+            "title": "Intelligent Network Flow Optimization Prototype Traffic Management Entity-Based Speed Harmonization"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyProgramURL": "http://www.nhtsa.gov/fuel-economy",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/ij9r-2xbq",
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
+            "identifier": "1862.4",
+            "isPartOf": "DOT-1862",
+            "issued": "2015-12-16",
             "keyword": [
                 "amfa",
                 "civil penalties",
@@ -60555,121 +60569,77 @@
                 "report",
                 "shortfall"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "1862.4",
+            "landingPage": "https://data.transportation.gov/d/ij9r-2xbq",
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
-            "landingPage": "https://data.transportation.gov/d/im7w-eu7z",
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
-            "identifier": "https://data.transportation.gov/api/views/im7w-eu7z",
             "description": "The U.S. Census Bureau provides monthly estimates of the total dollar value of construction work done in the United States as part of the Value of Construction Put in Place Survey (VIP). Includes construction related to docks/marinas and dry dock/marine terminals.",
-            "title": "State and Local Government Construction Spending - Water Transportation",
+            "identifier": "https://data.transportation.gov/api/views/im7w-eu7z",
+            "issued": "2025-01-03",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/im7w-eu7z",
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
+            "title": "State and Local Government Construction Spending - Water Transportation"
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
-                "connected vehicle message",
-                "connected vehicle pilot (cvp)",
-                "field test",
-                "florida",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "roadside equipment (rse)",
-                "tampa",
-                "tampa connected vehicle pilot deployment (tampa cv pilot)",
-                "tampa hillsborough expressway authority (thea)",
-                "traveler information message (tim)"
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
-            "identifier": "https://data.transportation.gov/api/views/in46-gmir",
+            "dataQuality": true,
             "description": "The Tampa CV Pilot generates data from the interaction between vehicles and between vehicles and infrastructure. This dataset consists of Traveler Information Messages (TIMs) transmitted by road-side units (RSU) located throughout the Tampa CV Pilot Study area.  The full set of raw, TIM data from Tampa CV Pilot can be found in the <a href=\"http://usdot-its-cvpilot-publicdata.s3.amazonaws.com/index.html\" target=\"_blank\">ITS Sandbox</a>. The data fields follow a SAE J2735 TIM message structure to convey important traffic information to onboard units (OBU) of equipped vehicles. Refer to SAE J2735 Section 5.16 Message: MSG_TravelerInformation Message (TIM).\n\nThis dataset holds a flattened sample of the TIM data from Tampa CV Pilot. Three additional fields were added to this Socrata dataset during ETL: a geo column (travelerdataframe_msgId_position) to allow for mapping of the geocoded TIM data within Socrata, a random number column (randomNum) to allow for random sampling of data points within Socrata, and a time of day generated column (metadata_generatedAt_timeOfDay) to allow for filtering of data by generated time.",
-            "title": "Tampa CV Pilot Traveler Information Message (TIM) Sample",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60677,51 +60647,97 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/in46-gmir/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/in46-gmir/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/in46-gmir/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/in46-gmir/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/in46-gmir/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/in46-gmir/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/in46-gmir/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/in46-gmir/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/in46-gmir/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Tampa, Florida",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/in46-gmir",
+            "issued": "2019-03-05",
+            "keyword": [
+                "arterial",
+                "connected vehicle message",
+                "connected vehicle pilot (cvp)",
+                "field test",
+                "florida",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "roadside equipment (rse)",
+                "tampa",
+                "tampa connected vehicle pilot deployment (tampa cv pilot)",
+                "tampa hillsborough expressway authority (thea)",
+                "traveler information message (tim)"
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
+            "title": "Tampa CV Pilot Traveler Information Message (TIM) Sample"
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
-            "landingPage": "https://data.transportation.gov/d/inky-5ecv",
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
+                    "downloadURL": "http://www.fra.dot.gov/eLib/Details/L04116",
+                    "mediaType": "text/csv",
+                    "title": "Train and Engine Service (Passenger) Data"
+                }
             ],
+            "identifier": "283.8",
+            "isPartOf": "DOT-283",
+            "issued": "2008-03-01",
             "keyword": [
                 "alertness",
                 "employee",
@@ -60732,58 +60748,60 @@
                 "sleep",
                 "work"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "283.8",
+            "landingPage": "https://data.transportation.gov/d/inky-5ecv",
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
-            "title": "Work Schedules and Sleep Patterns of Railroad Employees - Train and Engine Service (Passenger) Data",
-            "isPartOf": "DOT-283",
-            "agencyProgramURL": "http://www.fra.dot.gov/Page/P0068",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fra.dot.gov/eLib/Details/L04116",
-                    "mediaType": "text/csv",
-                    "title": "Train and Engine Service (Passenger) Data"
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
+            "title": "Work Schedules and Sleep Patterns of Railroad Employees - Train and Engine Service (Passenger) Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/inv3-kitf",
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
+                    "description": "2012 Kentucky HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/kentucky2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Kentucky"
+                }
+            ],
+            "identifier": "678.71",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -60797,60 +60815,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.71",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Kentucky",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/inv3-kitf",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/kentucky2012.zip",
-                    "description": "2012 Kentucky HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Kentucky"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Kentucky"
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
-            "landingPage": "https://data.transportation.gov/d/ip38-pdks",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/tvtarchive.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Summary 1992 - 2002"
+                }
             ],
+            "identifier": "18.153",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -60860,60 +60875,60 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.153",
+            "landingPage": "https://data.transportation.gov/d/ip38-pdks",
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
-            "title": "Monthly Traffic Volume Trends - Summary 1992 - 2002",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/tvtarchive.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "Summary 1992 - 2002"
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
+            "title": "Monthly Traffic Volume Trends - Summary 1992 - 2002"
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
-            "landingPage": "https://data.transportation.gov/d/iptx-cjpq",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/14jultvt/14jultvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "July 2014"
+                }
             ],
+            "identifier": "18.64",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -60923,82 +60938,49 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.64",
+            "landingPage": "https://data.transportation.gov/d/iptx-cjpq",
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
-            "title": "Monthly Traffic Volume Trends - July 2014",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/14jultvt/14jultvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "July 2014"
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
+            "title": "Monthly Traffic Volume Trends - July 2014"
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
-            "landingPage": "https://data.transportation.gov/d/iq2u-ir8u",
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
-            "identifier": "364.27",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2009",
-            "isPartOf": "DOT-364",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
-            "primaryITInvestmentUII": "021-621341357",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61007,54 +60989,87 @@
                     "title": "Event Data Records Reports - 2009"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.27",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/iq2u-ir8u",
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
+            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2009"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/iqfi-cuyv",
-            "issued": "2021-04-07",
             "@type": "dcat:Dataset",
-            "modified": "2024-09-18",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DiJoseph, Patricia (OST)",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/iqfi-cuyv",
+            "issued": "2021-04-07",
+            "landingPage": "https://data.transportation.gov/d/iqfi-cuyv",
+            "modified": "2024-09-18",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Tonnage"
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
-            "landingPage": "https://data.transportation.gov/d/iqsx-qyif",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/10aprtvt/10aprtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "April 2010"
+                }
             ],
+            "identifier": "18.23",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -61064,60 +61079,61 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.23",
+            "landingPage": "https://data.transportation.gov/d/iqsx-qyif",
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
-            "title": "Monthly Traffic Volume Trends - April 2010",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/10aprtvt/10aprtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "April 2010"
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
+            "title": "Monthly Traffic Volume Trends - April 2010"
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
-            "landingPage": "https://data.transportation.gov/d/iqwe-vnd4",
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
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2004NTDxls.exe",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2004 Database"
+                }
             ],
+            "identifier": "21.8",
+            "isPartOf": "DOT-21",
+            "issued": "2010-10-01",
             "keyword": [
                 "agency",
                 "allocation",
@@ -61136,74 +61152,42 @@
                 "urbanized",
                 "vehicles"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NTD Program Support",
-                "hasEmail": "mailto:NTDHelp@dot.gov"
-            },
-            "identifier": "21.8",
+            "landingPage": "https://data.transportation.gov/d/iqwe-vnd4",
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
-            "title": "NTD Annual Module Data Set - 2004 Database",
-            "isPartOf": "DOT-21",
-            "agencyProgramURL": "http://www.ntdprogram.gov",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2004NTDxls.exe",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "2004 Database"
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
+            "title": "NTD Annual Module Data Set - 2004 Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/iqwy-f8z4",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2020-06-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-22",
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
-            "identifier": "https://data.transportation.gov/api/views/iqwy-f8z4",
             "description": "This table shows the number and percent of people in the United States potentially exposed to different levels of noise from aviation sources.",
-            "title": "Population potentially exposed to aviation noise, 2016 and 2018",
-            "programCode": [
-                "021:052"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61211,46 +61195,77 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/iqwy-f8z4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/iqwy-f8z4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/iqwy-f8z4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/iqwy-f8z4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/iqwy-f8z4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/iqwy-f8z4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/iqwy-f8z4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/iqwy-f8z4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/iqwy-f8z4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/iqwy-f8z4",
+            "issued": "2020-06-22",
+            "keyword": [
+                "noise"
+            ],
+            "landingPage": "https://data.transportation.gov/d/iqwy-f8z4",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2020-06-22",
+            "programCode": [
+                "021:052"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Aviation"
-            ]
+            ],
+            "title": "Population potentially exposed to aviation noise, 2016 and 2018"
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
-            "landingPage": "https://data.transportation.gov/d/is2s-d7zk",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/09novtvt/09novtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "November 2009"
+                }
             ],
+            "identifier": "18.28",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -61260,77 +61275,43 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.28",
+            "landingPage": "https://data.transportation.gov/d/is2s-d7zk",
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
-            "title": "Monthly Traffic Volume Trends - November 2009",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/09novtvt/09novtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "November 2009"
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
+            "title": "Monthly Traffic Volume Trends - November 2009"
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
-                "name": "data.transportation.gov"
-            },
-            "identifier": "https://data.transportation.gov/api/views/ismp-dmnm",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 2003",
-            "title": "Historic HPMS Data (Universe) - 2003",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61338,54 +61319,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ismp-dmnm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ismp-dmnm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ismp-dmnm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ismp-dmnm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ismp-dmnm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ismp-dmnm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ismp-dmnm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ismp-dmnm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ismp-dmnm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/ismp-dmnm",
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
+            "title": "Historic HPMS Data (Universe) - 2003"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/isy5-3gj3",
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
-            "identifier": "https://data.transportation.gov/api/views/isy5-3gj3",
             "description": "The FMCSA Safety Measurement System (SMS) data, consists of active Intrastate Non-Hazmat Motor Carriers of property and/or\npassengers. File is comma delimited. One carrier per row.",
-            "title": "SMS EXTRACT INTRA",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61393,77 +61383,105 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/isy5-3gj3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/isy5-3gj3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/isy5-3gj3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/isy5-3gj3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/isy5-3gj3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/isy5-3gj3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/isy5-3gj3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/isy5-3gj3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/isy5-3gj3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/isy5-3gj3",
+            "issued": "2024-12-22",
+            "landingPage": "https://data.transportation.gov/d/isy5-3gj3",
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
+            "title": "SMS EXTRACT INTRA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/itj6-vfiw",
             "bureauCode": [
                 "021:04"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Passengers, seats and load factor by year and carrier.",
+            "identifier": "https://data.transportation.gov/api/views/itj6-vfiw",
             "issued": "2024-07-05",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-13",
             "keyword": [
                 "aff",
                 "aviation facts & figures",
                 "passengers"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/itj6-vfiw",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-13",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/itj6-vfiw",
-            "description": "Passengers, seats and load factor by year and carrier.",
-            "title": "Passengers",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Aviation"
-            ]
+            ],
+            "title": "Passengers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/itrp-yp89",
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
+                    "description": "2012 Massachusetts HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/massachusetts2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Massachusetts"
+                }
+            ],
+            "identifier": "678.75",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -61477,82 +61495,46 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.75",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Massachusetts",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/itrp-yp89",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/massachusetts2012.zip",
-                    "description": "2012 Massachusetts HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Massachusetts"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Massachusetts"
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
-            "landingPage": "https://data.transportation.gov/d/iv92-qqyn",
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
-            "identifier": "364.14",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database - Biomechanics Test Database Export",
-            "isPartOf": "DOT-364",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
-            "primaryITInvestmentUII": "021-621341357",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61561,42 +61543,47 @@
                     "title": "Biomechanics Test Database Export"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.14",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/iv92-qqyn",
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
+            "title": "Vehicle Safety Research and Development Database - Biomechanics Test Database Export"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ivp4-5mkt",
-            "issued": "2020-06-10",
             "@type": "dcat:Dataset",
-            "modified": "2020-06-10",
-            "keyword": [
-                "transportation and economy"
-            ],
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "BTS Open Data",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
-            "identifier": "https://data.transportation.gov/api/views/ivp4-5mkt",
             "description": "Trips by Distance data with additional county transportation statistics",
-            "title": "Trips by Distance with County Data",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61604,64 +61591,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ivp4-5mkt/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ivp4-5mkt/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ivp4-5mkt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ivp4-5mkt/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ivp4-5mkt/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ivp4-5mkt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ivp4-5mkt/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ivp4-5mkt/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ivp4-5mkt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/ivp4-5mkt",
+            "issued": "2020-06-10",
+            "keyword": [
+                "transportation and economy"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ivp4-5mkt",
+            "modified": "2020-06-10",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Trips by Distance with County Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "This is a system to track change and configuration management and help-desk activity. It is used only by FMCSA IT staff and contractors.",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/iw3z-gfkv",
-            "issued": "2015-01-21",
-            "temporal": "R/2015-01-21/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-31",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "change management.",
-                "configuration management",
-                "help desk"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO",
                 "hasEmail": "mailto:fmcsa.cdo@dot.gov"
             },
-            "identifier": "1638.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": false,
             "description": "IT Configuration Management: This helpdesk software is a COTS product. FMCSA utilizes the client server option.",
-            "title": "HEAT (Frontrange Solutions) -",
-            "primaryITInvestmentUII": "021-000001018",
-            "programCode": [
-                "021:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61669,29 +61651,65 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "1638.0",
+            "issued": "2015-01-21",
+            "keyword": [
+                "change management.",
+                "configuration management",
+                "help desk"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/iw3z-gfkv",
             "language": [
                 "en-US"
             ],
-            "phone": "202-385-2701"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-31",
+            "phone": "202-385-2701",
+            "primaryITInvestmentUII": "021-000001018",
+            "programCode": [
+                "021:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "rights": "This is a system to track change and configuration management and help-desk activity. It is used only by FMCSA IT staff and contractors.",
+            "temporal": "R/2015-01-21/P1Y",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "HEAT (Frontrange Solutions) -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/iwkj-qxt4",
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
+                    "description": "2013 Minnesota HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/minnesota2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Minnesota"
+                }
+            ],
+            "identifier": "678.127",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -61705,60 +61723,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.127",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Minnesota",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/iwkj-qxt4",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/minnesota2013.zip",
-                    "description": "2013 Minnesota HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Minnesota"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Minnesota"
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
-            "landingPage": "https://data.transportation.gov/d/iwrx-6vb8",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/14febtvt/14febtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "February 2014"
+                }
             ],
+            "identifier": "18.59",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -61768,56 +61783,53 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.59",
+            "landingPage": "https://data.transportation.gov/d/iwrx-6vb8",
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
-            "title": "Monthly Traffic Volume Trends - February 2014",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/14febtvt/14febtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "February 2014"
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
+            "title": "Monthly Traffic Volume Trends - February 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ixg2-6cni",
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
+            "description": "This set of data files is one of the four test data sets acquired by the USDOT Data Capture and Management program.  It contains the following data for the six months from May 1 2011 to October 31 2011:\n-Raw and cleaned data for traffic detectors deployed by Washington Department of Transportation (WSDOT) along I-5 in Seattle. Data includes 20-second raw reports.\n-Incident response records from the WSDOT's Washington Incident Tracking System (WITS).\n-A record of all messages and travel times posted on WSDOT's Active Traffic -Management signs and conventional variable message signs on I-5.\n-Loop detector volume and occupancy data from arterials parallel to I-5, estimated travel times on arterials derived from Automatic License Plate Reader (ALPR) data, and arterial signal timing plans.\n-Scheduled and actual bus arrival times from King County Metro buses and Sound Transit buses.\n-Incidents on I-5 during the six month period\n-Seattle weather data for the six month period\n-A dataset of GPS breadcrumb data from commercial trucks described in the documentation is not available to the public because of data ownership and privacy issues.\n\nThis legacy dataset was created before data.transportation.gov and is only currently available via the attached file(s). Please contact the dataset owner if there is a need for users to work with this data using the data.transportation.gov analysis features (online viewing, API, graphing, etc.) and the USDOT will consider modifying the dataset to fully integrate in data.transportation.gov.\n\nNote: All extras are attached in Seattle Freeway Travel Times https://data.transportation.gov/Automobiles/Seattle-Freeway-Travel-Times/9v5g-t8u8",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/download/ixg2-6cni/application/msword",
+                    "mediaType": "application/msword"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/ixg2-6cni",
             "issued": "2012-05-31",
-            "@type": "dcat:Dataset",
-            "temporal": "2011-05-01/2011-10-31",
-            "modified": "2012-05-31",
             "keyword": [
                 "arterial",
                 "freeway",
@@ -61838,53 +61850,56 @@
                 "washington state department of transportation (wsdot)",
                 "weather"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/ixg2-6cni",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
+            "modified": "2012-05-31",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Department of Transportation"
             },
-            "identifier": "https://data.transportation.gov/api/views/ixg2-6cni",
-            "description": "This set of data files is one of the four test data sets acquired by the USDOT Data Capture and Management program.  It contains the following data for the six months from May 1 2011 to October 31 2011:\n-Raw and cleaned data for traffic detectors deployed by Washington Department of Transportation (WSDOT) along I-5 in Seattle. Data includes 20-second raw reports.\n-Incident response records from the WSDOT's Washington Incident Tracking System (WITS).\n-A record of all messages and travel times posted on WSDOT's Active Traffic -Management signs and conventional variable message signs on I-5.\n-Loop detector volume and occupancy data from arterials parallel to I-5, estimated travel times on arterials derived from Automatic License Plate Reader (ALPR) data, and arterial signal timing plans.\n-Scheduled and actual bus arrival times from King County Metro buses and Sound Transit buses.\n-Incidents on I-5 during the six month period\n-Seattle weather data for the six month period\n-A dataset of GPS breadcrumb data from commercial trucks described in the documentation is not available to the public because of data ownership and privacy issues.\n\nThis legacy dataset was created before data.transportation.gov and is only currently available via the attached file(s). Please contact the dataset owner if there is a need for users to work with this data using the data.transportation.gov analysis features (online viewing, API, graphing, etc.) and the USDOT will consider modifying the dataset to fully integrate in data.transportation.gov.\n\nNote: All extras are attached in Seattle Freeway Travel Times https://data.transportation.gov/Automobiles/Seattle-Freeway-Travel-Times/9v5g-t8u8",
-            "title": "Seattle 20 Second Freeway",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/download/ixg2-6cni/application/msword",
-                    "mediaType": "application/msword"
-                }
-            ],
             "spatial": "Seattle, Washington",
-            "dataQuality": true,
-            "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "irregular",
+            "temporal": "2011-05-01/2011-10-31",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Seattle 20 Second Freeway"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
+            "agencyDataSeriesURL": "https://ai.fmcsa.dot.gov/CrashProfile/CrashProfileMainNew.asp",
+            "agencyProgramURL": "http://ai.fmcsa.dot.gov/CrashProfile/CrashProfileMainNew.asp",
+            "analysisUnit": "Crash, Motor Carrier, State",
+            "bureauCode": [
+                "021:17"
+            ],
+            "categoryDesignation": "Research",
+            "collectionInstrument": "Transportation",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
             },
+            "dataQuality": true,
+            "description": "Crash Statistics are summarized crash statistics for large trucks and buses involved in fatal and non-fatal Crashes that occurred in the United States. These statistics are derived from two sources:  the Fatality Analysis Reporting System (FARS) and the Motor Carrier Management Information System (MCMIS). Crash Statistics contain information that can be used to identify safety problems in specific geographical areas or to compare state statistics to the national crash figures.",
+            "distribution": [
                 {
-            "accessLevel": "public",
-            "bureauCode": [
-                "021:17"
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://ai.fmcsa.dot.gov/CrashProfile/statecrashprofilemain.asp",
+                    "mediaType": "text/html",
+                    "title": "State Profiles"
+                }
             ],
-            "landingPage": "https://data.transportation.gov/d/ixh8-iip9",
+            "identifier": "112.2",
+            "isPartOf": "DOT-112",
             "issued": "2018-12-17",
-            "temporal": "R/2005-03-01/P3M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
-            "collectionInstrument": "Transportation",
-            "references": [
-                "http://ai.fmcsa.dot.gov/CrashProfile/CrashProfileMainNew.asp"
-            ],
             "keyword": [
                 "bus",
                 "crash",
@@ -61901,77 +61916,42 @@
                 "motorcoach",
                 "towaway"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "112.2",
+            "landingPage": "https://data.transportation.gov/d/ixh8-iip9",
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
-            "title": "A&I - Crash Statistics - State Profiles",
-            "isPartOf": "DOT-112",
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
-            "categoryDesignation": "Research",
-            "analysisUnit": "Crash, Motor Carrier, State",
-            "phone": "202-366-2161",
-            "language": [
-                "en-US"
-            ]
+            "title": "A&I - Crash Statistics - State Profiles"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/iyde-f8k7",
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
-            "identifier": "https://data.transportation.gov/api/views/iyde-f8k7",
             "description": "A data base of responses to the 2022 National Census of Ferries.\n\nThis file gives information about ferry segments.",
-            "title": "2022 NCFO Segments File",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -61979,61 +61959,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/iyde-f8k7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/iyde-f8k7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/iyde-f8k7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/iyde-f8k7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/iyde-f8k7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/iyde-f8k7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/iyde-f8k7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/iyde-f8k7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/iyde-f8k7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/iyde-f8k7",
+            "issued": "2024-05-01",
+            "keyword": [
+                "ferry",
+                "ferry operators",
+                "ferry transit",
+                "ncfo",
+                "passenger ferry"
+            ],
+            "landingPage": "https://data.transportation.gov/d/iyde-f8k7",
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
+            "title": "2022 NCFO Segments File"
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
-            "modified": "2023-10-18",
-            "keyword": [
-                "congress",
-                "congressional district",
-                "district"
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
-            "identifier": "https://data.transportation.gov/api/views/iynb-tzyd",
+            "dataQuality": true,
             "description": "Spatial data representing the United States congressional districts from the 118th congress (2023-2024). These shapes are represented on the app currently hosted at bts.gov/congressionaldistricts.",
-            "title": "Citizen Connect - Congressional District geography (live)",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62041,65 +62024,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/iynb-tzyd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/iynb-tzyd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/iynb-tzyd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/iynb-tzyd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/iynb-tzyd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/iynb-tzyd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/iynb-tzyd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/iynb-tzyd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/iynb-tzyd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/iynb-tzyd",
+            "issued": "2023-10-11",
+            "keyword": [
+                "congress",
+                "congressional district",
+                "district"
+            ],
+            "landingPage": "https://www.bts.dot.gov/congressionaldistricts",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2023-10-18",
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
                 "Congressional districts"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Citizen Connect - Congressional District geography (live)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://data.transportation.gov/d/iyz9-3pd9",
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
-            "identifier": "https://data.transportation.gov/api/views/iyz9-3pd9",
             "description": "",
-            "title": "Pocket Guide to Transportation-Transportation Facilities",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62107,40 +62091,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/iyz9-3pd9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/iyz9-3pd9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/iyz9-3pd9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/iyz9-3pd9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/iyz9-3pd9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/iyz9-3pd9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/iyz9-3pd9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/iyz9-3pd9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/iyz9-3pd9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "https://data.transportation.gov/api/views/iyz9-3pd9",
+            "issued": "2024-02-01",
+            "keyword": [
+                "pocket guide to transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/iyz9-3pd9",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-02-01",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Pocket Guide to Transportation-Transportation Facilities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/izi8-sht2",
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
+                    "description": "2011 Colorado HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/colorado2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Colorado"
+                }
+            ],
+            "identifier": "678.7",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -62154,60 +62172,59 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.7",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Colorado",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/izi8-sht2",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/colorado2011.zip",
-                    "description": "2011 Colorado HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Colorado"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Colorado"
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
-            "landingPage": "https://data.transportation.gov/d/izrd-p2z4",
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
+            "identifier": "83.1",
+            "isPartOf": "DOT-83",
+            "issued": "2002-12-16",
             "keyword": [
                 "air bag",
                 "air bags",
@@ -62234,63 +62251,60 @@
                 "vin",
                 "vin search"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "83.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Manufacturers who determine that a product or piece of original equipment either has a safety defect or is not in compliance with Federal safety standards are required to notify the National Highway Traffic Safety Administration (NHTSA) within 5 business days. NHTSA requires that manufacturers file a Defect and Noncompliance report as well as quarterly recall status reports, in compliance with Federal Regulation 49 (the National Traffic and Motor Safety Act) Part 573, which identifies the requirements for safety recalls. This information is stored in the NHTSA database. Use this data to search for recall information related to:-\tSpecific NHTSA campaigns -\tProduct types Access to public searches of NHTSA recall databases for tires, vehicles, car seats and equipment.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - Recalls Flat File",
-            "isPartOf": "DOT-83",
-            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
-            "describedByType": "text/plain",
+            "landingPage": "https://data.transportation.gov/d/izrd-p2z4",
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
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - Recalls Flat File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyProgramURL": "http://www.nhtsa.gov/fuel-economy",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/j2ph-iiza",
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
+                    "description": "This report provides three data elements for each fleet that includes vehicles that qualify as dual fuel under AMFA. Also available in PDF and XLS.",
+                    "downloadURL": "http://www.nhtsa.gov/CAFE_PIC/CAFE_PIC_AMFA_LIVE.html",
+                    "mediaType": "text/html",
+                    "title": "Flex Fuel/AMFA"
+                }
             ],
+            "identifier": "1862.9",
+            "isPartOf": "DOT-1862",
+            "issued": "2015-12-16",
             "keyword": [
                 "amfa",
                 "civil penalties",
@@ -62307,53 +62321,43 @@
                 "report",
                 "shortfall"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "1862.9",
+            "landingPage": "https://data.transportation.gov/d/j2ph-iiza",
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
-            "landingPage": "https://data.transportation.gov/d/j32x-7fku",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Visualizations of unadjusted and seasonally adjusted transportation data.",
+            "identifier": "https://data.transportation.gov/api/views/j32x-7fku",
             "issued": "2021-09-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-21",
             "keyword": [
                 "air traffic",
                 "available seat miles",
@@ -62371,40 +62375,51 @@
                 "vehicle miles traveled",
                 "water"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/j32x-7fku",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-08-21",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/j32x-7fku",
-            "description": "Visualizations of unadjusted and seasonally adjusted transportation data.",
-            "title": "Transportation as an Economic Indicator: Seasonally-adjusted transportation data",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Transportation as an Economic Indicator: Seasonally-adjusted transportation data"
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
-            "landingPage": "https://data.transportation.gov/d/j46e-dn89",
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
+            "identifier": "408.1",
+            "isPartOf": "DOT-408",
+            "issued": "2008-08-31",
             "keyword": [
                 "air bag",
                 "child safety",
@@ -62415,56 +62430,40 @@
                 "protection",
                 "seat belt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "408.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Survey data the agency uses to track changes in public attitude, knowledge, and behavior related to occupant protection. The MVOSS also collects information related to Emergency Medical Services and crash experience. The survey is composed of two questionnaires, with one focusing on seat belt use and the other focusing on child occupant protection.",
-            "title": "Motor Vehicle Occupant Safety Survey 2007 (MVOSS) - Seat Belt Issues (v1)  (SPSS)",
-            "isPartOf": "DOT-408",
-            "agencyProgramURL": "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/National+Telephone+Surveys",
+            "landingPage": "https://data.transportation.gov/d/j46e-dn89",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-6401",
             "programCode": [
                 "021:032"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.nhtsa.gov/DOT/NHTSA/Traffic%20Injury%20Control/Articles/2007MVOSS/2007MVOSS_SPSS_Version__A.sav",
-                    "mediaType": "text/plain",
-                    "title": "Seat Belt Issues (v1)  (SPSS)"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
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
+            "title": "Motor Vehicle Occupant Safety Survey 2007 (MVOSS) - Seat Belt Issues (v1)  (SPSS)"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/j4yu-qgj6",
-            "issued": "2021-03-18",
             "@type": "dcat:Dataset",
-            "modified": "2024-02-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Chambers",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "PPFSP 23",
+            "identifier": "https://data.transportation.gov/api/views/j4yu-qgj6",
+            "issued": "2021-03-18",
             "keyword": [
                 "bureau",
                 "container",
@@ -62482,53 +62481,34 @@
                 "transportation",
                 "vessel"
             ],
-            "identifier": "https://data.transportation.gov/api/views/j4yu-qgj6",
+            "landingPage": "https://data.transportation.gov/d/j4yu-qgj6",
+            "modified": "2024-02-08",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "PPFSP 23",
             "title": "Rail & Road Connections"
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
-            "landingPage": "https://data.transportation.gov/d/j4zb-icm3",
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
-            "identifier": "693.14",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
             "description": "The NBI System is the collection of bridge inspection information and costs associated with bridge replacements of structurally deficient bridges on and off the NHS. This data is collected under the auspices of the National Bridge Inspection Standards (NBIS) as prescribed by law. The NBI System collects the information that is used to determine eligibility for NHS projects, performance measure reporting, NHS penalty determination, and reporting to Congress.  It supports oversight of the NBIS through various report tools, and provides data reporting that supports agency strategic goals.",
-            "title": "National Bridge Inventory System (NBI) - 2005",
-            "isPartOf": "DOT-693",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
-            "primaryITInvestmentUII": "021-012940226",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62537,48 +62517,53 @@
                     "title": "2005"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
-            "dataQuality": true,
+            "identifier": "693.14",
+            "isPartOf": "DOT-693",
+            "issued": "1992-12-31",
+            "keyword": [
+                "bridge",
+                "condition",
+                "deck",
+                "inspection",
+                "structure"
+            ],
+            "landingPage": "https://data.transportation.gov/d/j4zb-icm3",
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
+            "title": "National Bridge Inventory System (NBI) - 2005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/j5uj-anzx",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
-            "keyword": [
-                "transit fuel expense",
-                "transit operating expense",
-                "transit salary"
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
-            "identifier": "https://data.transportation.gov/api/views/j5uj-anzx",
             "description": "This dataset details operating expenses for each applicable agency, mode, and type of service (TOS), split by expense type or \"Object Class\" reporting to the National Transit Database in the 2022 and 2023 report years.. Object classes include salaries and wages, fuel, and others.\n\nOnly Full Reporters report expenses by function and type. Expenses from other reporter types are included under Reduced Reporter Expenses.\n\nNTD Data Tables organize and summarize data from the 2022 and 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. This dataset is based on the 2022 and 2023 Operating Expenses database files.\n\nIn years 2015-2021, you can find this data in the \"Operating Expenses\" data table on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.\n\nIf you have any other questions about this table, please contact the NTD Help Desk at NTDHelp@dot.gov.",
-            "title": "2022 - 2023 NTD Annual Data - Operating Expenses (by Type)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62586,60 +62571,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/j5uj-anzx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/j5uj-anzx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/j5uj-anzx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/j5uj-anzx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/j5uj-anzx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/j5uj-anzx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/j5uj-anzx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/j5uj-anzx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/j5uj-anzx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/j5uj-anzx",
+            "issued": "2024-09-10",
+            "keyword": [
+                "transit fuel expense",
+                "transit operating expense",
+                "transit salary"
+            ],
+            "landingPage": "https://data.transportation.gov/d/j5uj-anzx",
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
+            "title": "2022 - 2023 NTD Annual Data - Operating Expenses (by Type)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/j6uy-twhg",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2021-03-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-06",
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
-            "identifier": "https://data.transportation.gov/api/views/j6uy-twhg",
             "description": "Data from 2019 through 2023. For years after 2023, see: https://data.bts.gov/Research-and-Statistics/Docked-Bikeshare-Ridership/6cfa-ipzd\n\nHistoric data updated on 07/14/2023. Q4 of 2023 and data for all years on systems allowing parking outside of a docking station updated on 06/04/2024.\n\nBikeshare ridership by system, year, month, and hour the trip ended at for bikeshare systems with docking stations. Data available by month starting in January 2019. Months are rearranged to include the same number of days of the week across years (see below). Data designed to show the impacts of COVID-19 on bikeshare ridership as featured at https://maps.dot.gov/BTS/dockedbikeshare-COVID/\n\nRidership data not available for all docked bikeshare systems. Only docked bikeshare systems with ridership data shown. Some systems included in the data permit users to leave a bicycle outside of a docking station; these trips are indicated by the trip type. Trips defined as rides from point A to B. If user makes trip from B to A on same day, counted as a second trip. Trips labeled as round trips in Metro Bike Share and Indego trip files counted as 2 trips. Trips with no trip time are not counted. For trips starting and ending at a docking station or on systems where only docked trips are permitted, trips with no start station identifier and/or end station id are not counted in totals. Trips shorter than 1 minute or greater than 2 hours excluded. Days aligned to include the same days of weeks in 2019 and 2020. Days included in each month are as follows:\n\nDays included in each month can be found in the attachment (https://data.bts.gov/api/views/6cfa-ipzd/files/36fde1b8-57c3-4d31-b9dc-bbc896ba346e?download=true&filename=days_included_in_docked_bikeshare_monthly_summaries.xlsx). Data are through 2023. For hourly data by calendar year and for hourly data in years after 2023, see https://data.bts.gov/Research-and-Statistics/Docked-Bikeshare-Ridership/6cfa-ipzd \n\nTrips beginning on 12/31/2019 but ending on 01/01/2020 not included in totals.\n\nInteractive map application featuring data: https://maps.dot.gov/BTS/dockedbikeshare-COVID/",
-            "title": "Docked Bikeshare Ridership By System, Year, Month, and Hour",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -62647,47 +62630,79 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/j6uy-twhg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/j6uy-twhg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/j6uy-twhg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/j6uy-twhg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/j6uy-twhg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/j6uy-twhg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/j6uy-twhg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/j6uy-twhg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/j6uy-twhg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/j6uy-twhg",
+            "issued": "2021-03-18",
+            "keyword": [
+                "bikeshare",
+                "docked bikeshare"
+            ],
+            "landingPage": "https://data.transportation.gov/d/j6uy-twhg",
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
                 "Bicycles and Pedestrians"
             ],
-            "phone": "202-366-DATA(3282) "
+            "title": "Docked Bikeshare Ridership By System, Year, Month, and Hour"
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
-            "landingPage": "https://data.transportation.gov/d/j7ny-up73",
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
+                    "downloadURL": "http://www.nhtsa.gov/staticfiles/nti/MVOSS/MVOSS2007_SAS_Combined_Data.sas7bdat",
+                    "mediaType": "text/plain",
+                    "title": "Combined Questionnaire (v1&2) (SAS)"
+                }
             ],
+            "identifier": "408.6",
+            "isPartOf": "DOT-408",
+            "issued": "2008-08-31",
             "keyword": [
                 "air bag",
                 "child safety",
@@ -62698,81 +62713,47 @@
                 "protection",
                 "seat belt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "408.6",
+            "landingPage": "https://data.transportation.gov/d/j7ny-up73",
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
-            "title": "Motor Vehicle Occupant Safety Survey 2007 (MVOSS) - Combined Questionnaire (v1&2) (SAS)",
-            "isPartOf": "DOT-408",
-            "agencyProgramURL": "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/National+Telephone+Surveys",
-            "programCode": [
-                "021:032"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.nhtsa.gov/staticfiles/nti/MVOSS/MVOSS2007_SAS_Combined_Data.sas7bdat",
-                    "mediaType": "text/plain",
-                    "title": "Combined Questionnaire (v1&2) (SAS)"
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
+            "title": "Motor Vehicle Occupant Safety Survey 2007 (MVOSS) - Combined Questionnaire (v1&2) (SAS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "https://hepgis.fhwa.dot.gov/fhwagis/DownloadForm.html",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://hepgis.fhwa.dot.gov/fhwagis/",
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
-            "identifier": "692.23",
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
@@ -62781,34 +62762,68 @@
                     "title": "MPO Boundaries"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.23",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://hepgis.fhwa.dot.gov/fhwagis/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "https://hepgis.fhwa.dot.gov/fhwagis/DownloadForm.html",
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
             "accessLevel": "public",
+            "accrualPeriodicity": "R/PT1S",
+            "agencyDataSeriesURL": "http://www.nhtsa.gov/Vehicle+Safety",
+            "agencyProgramURL": "http://vpic.nhtsa.dot.gov/",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/j7xy-dt4s",
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
+                    "description": "Decodes a Vehicle Identification Number (VIN) and other basic specifications for regulated vehicle types",
+                    "downloadURL": "http://vpic.nhtsa.dot.gov/decoder/",
+                    "mediaType": "text/html",
+                    "title": "VIN Decoder"
+                }
             ],
+            "identifier": "65.3",
+            "isPartOf": "DOT-65",
+            "issued": "2015-10-05",
             "keyword": [
                 "49",
                 "551",
@@ -62845,61 +62860,61 @@
                 "vin",
                 "vpic"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "65.3",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "The NHTSA Product Information Catalog and Vehicle Listing (vPIC) is a consolidated platform that presents data collected within the manufacturer reported data from CFR 49 Parts 551 - 574 for use in a variety of modern tools. NHTSA's vPIC platform is intended to serve as a centralized source for basic Vehicle Identification Number (VIN) decoding, Manufacturer Information Database (MID), Manufacturer Equipment Plant Identification and associated data. vPIC is intended to support the Open Data and Transparency initiatives of the agency by allowing the data to be freely used by the public without the burden of manual retrieval from a library of electronic documents (PDFs). While these documents will still be available online for viewing within the Manufacturer Information Database (MID) module of vPIC one can view and use the actual data through the VIN Decoder and Application Programming Interface (API) modules.",
-            "title": "NHTSA Product Information Catalog and Vehicle Listing (vPIC) - VIN Decoder",
-            "isPartOf": "DOT-65",
-            "agencyProgramURL": "http://vpic.nhtsa.dot.gov/",
+            "landingPage": "https://data.transportation.gov/d/j7xy-dt4s",
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
-                    "downloadURL": "http://vpic.nhtsa.dot.gov/decoder/",
-                    "description": "Decodes a Vehicle Identification Number (VIN) and other basic specifications for regulated vehicle types",
-                    "@type": "dcat:Distribution",
-                    "title": "VIN Decoder"
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
+            "title": "NHTSA Product Information Catalog and Vehicle Listing (vPIC) - VIN Decoder"
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
-            "landingPage": "https://data.transportation.gov/d/j8kd-qyeh",
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
+                    "mediaType": "application/xml",
+                    "title": "Vehicle API XML"
+                }
             ],
+            "identifier": "65.6",
+            "isPartOf": "DOT-65",
+            "issued": "2015-10-05",
             "keyword": [
                 "49",
                 "551",
@@ -62936,61 +62951,62 @@
                 "vin",
                 "vpic"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "65.6",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "The NHTSA Product Information Catalog and Vehicle Listing (vPIC) is a consolidated platform that presents data collected within the manufacturer reported data from CFR 49 Parts 551 - 574 for use in a variety of modern tools. NHTSA's vPIC platform is intended to serve as a centralized source for basic Vehicle Identification Number (VIN) decoding, Manufacturer Information Database (MID), Manufacturer Equipment Plant Identification and associated data. vPIC is intended to support the Open Data and Transparency initiatives of the agency by allowing the data to be freely used by the public without the burden of manual retrieval from a library of electronic documents (PDFs). While these documents will still be available online for viewing within the Manufacturer Information Database (MID) module of vPIC one can view and use the actual data through the VIN Decoder and Application Programming Interface (API) modules.",
-            "title": "NHTSA Product Information Catalog and Vehicle Listing (vPIC) - Vehicle API XML",
-            "isPartOf": "DOT-65",
-            "agencyProgramURL": "http://vpic.nhtsa.dot.gov/",
+            "landingPage": "https://data.transportation.gov/d/j8kd-qyeh",
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
-                    "mediaType": "application/xml",
-                    "downloadURL": "http://vpic.nhtsa.dot.gov/api/",
-                    "description": "APIs for use by developers, programmers or researchers interested in obtaining raw Vehicle or Manufacturer data from vPIC.",
-                    "@type": "dcat:Distribution",
-                    "title": "Vehicle API XML"
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
+            "title": "NHTSA Product Information Catalog and Vehicle Listing (vPIC) - Vehicle API XML"
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
-            "landingPage": "https://data.transportation.gov/d/j95e-kf9i",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/bridge/nbi/ascii.cfm%3Fyear=2011",
+                    "mediaType": "application/zip",
+                    "title": "2011"
+                }
             ],
+            "identifier": "693.20",
+            "isPartOf": "DOT-693",
+            "issued": "1992-12-31",
             "keyword": [
                 "bridge",
                 "condition",
@@ -62998,74 +63014,43 @@
                 "inspection",
                 "structure"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "693.20",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "The NBI System is the collection of bridge inspection information and costs associated with bridge replacements of structurally deficient bridges on and off the NHS. This data is collected under the auspices of the National Bridge Inspection Standards (NBIS) as prescribed by law. The NBI System collects the information that is used to determine eligibility for NHS projects, performance measure reporting, NHS penalty determination, and reporting to Congress.  It supports oversight of the NBIS through various report tools, and provides data reporting that supports agency strategic goals.",
-            "title": "National Bridge Inventory System (NBI) - 2011",
-            "isPartOf": "DOT-693",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
+            "landingPage": "https://data.transportation.gov/d/j95e-kf9i",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/bridge/nbi/ascii.cfm%3Fyear=2011",
-                    "mediaType": "application/zip",
-                    "title": "2011"
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
+            "title": "National Bridge Inventory System (NBI) - 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/j9q7-53ae",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
-            "keyword": [
-                "railway age",
-                "track",
-                "transit track age"
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
-            "identifier": "https://data.transportation.gov/api/views/j9q7-53ae",
             "description": "This dataset details the ages of guideway elements for each applicable agency reporting to the National Transit Database in the 2022 and 2023 report years. Guideway elements include elements, structures, or facilities dedicated specifically to transit use, such as track, subway structures, tunnels, bridges, and propulsion power systems. \n\nNTD Data Tables organize and summarize data from the 2022 and 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. This dataset is based on the 2022 and 2023 Transit Way Mileage database files.\n\nIn years 2015-2021, you can find this data in the \"Track and Roadway\" data table on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.\n\nIn versions of the data tables from before 2015, you can find data on vehicles in the file called \"Transit Way Mileage - Rail Modes.\"\n\nIf you have any other questions about this table, please contact the NTD Help Desk at NTDHelp@dot.gov.",
-            "title": "2022 - 2023 NTD Annual Data - Track & Roadway (Guideway Age Distribution)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63073,65 +63058,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/j9q7-53ae/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/j9q7-53ae/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/j9q7-53ae/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/j9q7-53ae/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/j9q7-53ae/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/j9q7-53ae/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/j9q7-53ae/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/j9q7-53ae/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/j9q7-53ae/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/j9q7-53ae",
+            "issued": "2024-09-10",
+            "keyword": [
+                "railway age",
+                "track",
+                "transit track age"
+            ],
+            "landingPage": "https://data.transportation.gov/d/j9q7-53ae",
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
+            "title": "2022 - 2023 NTD Annual Data - Track & Roadway (Guideway Age Distribution)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Access restricted under the Privacy Act of 1974; see System of Records Notice at http://www.gpo.gov/fdsys/pkg/FR-2000-04-11/pdf/00-8505.pdf#page=79",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/jahc-7qw5",
-            "issued": "2014-09-24",
-            "temporal": "R/2014-09-24/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "congressional",
-                "correspondence",
-                "process"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "455.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
             "description": "This data set contains information on external and internal correspondence addressed to the Secretary, Deputy Secretary, or Chief of Staff. Data include information about the sender, the referring party (if applicable), assigned offices, reviewing offices and clearances.",
-            "title": "Controlled Correspondence Tracking -",
-            "primaryITInvestmentUII": "021-280966704",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63139,63 +63121,49 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "theme": [
-                "Transportation"
+            "identifier": "455.0",
+            "issued": "2014-09-24",
+            "keyword": [
+                "congressional",
+                "correspondence",
+                "process"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/jahc-7qw5",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-4309"
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-14",
+            "phone": "202-366-4309",
+            "primaryITInvestmentUII": "021-280966704",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "rights": "Access restricted under the Privacy Act of 1974; see System of Records Notice at http://www.gpo.gov/fdsys/pkg/FR-2000-04-11/pdf/00-8505.pdf#page=79",
+            "temporal": "R/2014-09-24/P1Y",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Controlled Correspondence Tracking -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/jc5e-psbx",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2015-05-07",
-            "@type": "dcat:Dataset",
-            "temporal": "2014-09-05/2014-09-11",
-            "modified": "2015-05-07",
-            "keyword": [
-                "arterial",
-                "basic safety message (bsm)",
-                "belle isle park",
-                "connected vehicles",
-                "environment sensor stations",
-                "fhwa road weather management program",
-                "integrated mobile observation (imo)",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "its world congress",
-                "michigan",
-                "michigan department of transportation (mdot)",
-                "motorist advisories and warnings",
-                "road weather demonstration",
-                "sensor data",
-                "simulated road weather",
-                "vehicle data translator",
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
-            "identifier": "https://data.transportation.gov/api/views/jc5e-psbx",
+            "dataQuality": true,
             "description": "The Belle Isle data was collected between May 1st, 2014 and September 16th, 2014 on the Belle Isle Park in Michigan. However, within the data file provided as part of this data environment, only data during the World Congress demonstration period from September 5, 2014 to September 11, 2014 is included.  Several vehicles equipped with multiple sensors drove around the island collecting 572,030 readings of multiple variables. The uploaded data file lists all those observations and the pertaining details about the sensor equipment, the sensor platform and the status of quality checking performed for each observation.",
-            "title": "Road Weather Demonstration Data",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63203,66 +63171,79 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/jc5e-psbx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/jc5e-psbx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/jc5e-psbx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/jc5e-psbx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/jc5e-psbx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/jc5e-psbx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/jc5e-psbx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/jc5e-psbx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/jc5e-psbx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Belle Isle, Detroit, Michigan,",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/jc5e-psbx",
+            "issued": "2015-05-07",
+            "keyword": [
+                "arterial",
+                "basic safety message (bsm)",
+                "belle isle park",
+                "connected vehicles",
+                "environment sensor stations",
+                "fhwa road weather management program",
+                "integrated mobile observation (imo)",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "its world congress",
+                "michigan",
+                "michigan department of transportation (mdot)",
+                "motorist advisories and warnings",
+                "road weather demonstration",
+                "sensor data",
+                "simulated road weather",
+                "vehicle data translator",
+                "weather"
+            ],
+            "landingPage": "https://data.transportation.gov/d/jc5e-psbx",
             "license": "http://creativecommons.org/licenses/by-nc-sa/3.0/legalcode",
-            "accrualPeriodicity": "irregular",
+            "modified": "2015-05-07",
+            "programCode": [
+                "021:013"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
+            "spatial": "Belle Isle, Detroit, Michigan,",
+            "temporal": "2014-09-05/2014-09-11",
             "theme": [
                 "Automobiles"
-            ]
+            ],
+            "title": "Road Weather Demonstration Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/jc5k-rzm8",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2020-05-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "references": [
-                "https://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/hpms_field_manual_dec2016.pdf"
-            ],
-            "keyword": [
-                "arnold",
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
-            "identifier": "https://data.transportation.gov/api/views/jc5k-rzm8",
+            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
             "description": "The Federal Highway Administration (FHWA) has been receiving Highway inventory, usage, condition and performance data from State Departments of Transportation (DOT) since 1978 to support the program mission of the FHWA. Specifically, HPMS consists of detailed road segment data (63 Attributes) for higher order systems. Sample attributes for collector systems and summary data for the local roads.\nNew requirements for HPMS took effect in 2014 that required each State DOTs to expand their Linear Referencing Systems (LRS), a statewide geospatial representation of their road system that includes all public roads. This requirement was put in place to support highway safety.\nStates DOTs submit HPMS data annually to the FHWA following a prescribed format outlined in the Highway Performance Monitoring System Field Manual.",
-            "title": "Highway Performance Monitoring System (HPMS)",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63270,51 +63251,86 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/jc5k-rzm8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/jc5k-rzm8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/jc5k-rzm8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/jc5k-rzm8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/jc5k-rzm8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/jc5k-rzm8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/jc5k-rzm8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/jc5k-rzm8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/jc5k-rzm8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "USA",
-            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
+            "identifier": "https://data.transportation.gov/api/views/jc5k-rzm8",
+            "issued": "2020-05-08",
+            "keyword": [
+                "arnold",
+                "hpms"
+            ],
+            "landingPage": "https://data.transportation.gov/d/jc5k-rzm8",
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
+            "title": "Highway Performance Monitoring System (HPMS)"
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
-            "landingPage": "https://data.transportation.gov/d/jc6n-r957",
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
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/gxrrpt.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Hwy/Rail Detail Report"
+                }
             ],
+            "identifier": "214.11",
+            "isPartOf": "DOT-214",
+            "issued": "2010-09-29",
             "keyword": [
                 "accident",
                 "casualty",
@@ -63327,87 +63343,49 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "214.11",
+            "landingPage": "https://data.transportation.gov/d/jc6n-r957",
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
-            "title": "Highway Rail Accidents - Hwy/Rail Detail Report",
-            "isPartOf": "DOT-214",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/gxrrpt.aspx",
-                    "mediaType": "text/csv",
-                    "title": "Hwy/Rail Detail Report"
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
+            "title": "Highway Rail Accidents - Hwy/Rail Detail Report"
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
-            "landingPage": "https://data.transportation.gov/d/jcvt-hn8h",
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
-            "identifier": "1840.3",
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
@@ -63416,56 +63394,57 @@
                     "title": "Interactive Access"
                 }
             ],
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/veh/vehdb-export-fields.htm",
-            "dataQuality": true,
+            "identifier": "1840.3",
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
+            "landingPage": "https://data.transportation.gov/d/jcvt-hn8h",
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
             "accessLevel": "non-public",
-            "landingPage": "https://data.transportation.gov/d/jd5s-gacm",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:17"
             ],
-            "rights": "Records in this system include carrier-related documentation, employee records (PII), and FMCSA policy documentation.",
-            "issued": "2018-12-17",
-            "@type": "dcat:Dataset",
-            "temporal": "R/2013/P1Y",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-24",
-            "keyword": [
-                "driver education",
-                "enforcement",
-                "regulations",
-                "safety audits.",
-                "safety information",
-                "safety trends"
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
-            "identifier": "367.0",
+            "dataQuality": false,
             "description": "EDMS is the FMCSA official document repository. The system contains metadata about carriers and drivers, and is referenced by the FOIA team.",
-            "title": "Electronic Document Management System (EDMS) -",
-            "primaryITInvestmentUII": "021-311675356",
-            "programCode": [
-                "021:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63473,58 +63452,56 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
+            "identifier": "367.0",
+            "issued": "2018-12-17",
+            "keyword": [
+                "driver education",
+                "enforcement",
+                "regulations",
+                "safety audits.",
+                "safety information",
+                "safety trends"
+            ],
+            "landingPage": "https://data.transportation.gov/d/jd5s-gacm",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-05-24",
+            "primaryITInvestmentUII": "021-311675356",
+            "programCode": [
+                "021:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "rights": "Records in this system include carrier-related documentation, employee records (PII), and FMCSA policy documentation.",
+            "temporal": "R/2013/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "categoryDesignation": "Research",
-            "language": [
-                "en-US"
-            ]
+            "title": "Electronic Document Management System (EDMS) -"
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
-            "landingPage": "https://data.transportation.gov/d/jex2-a3d9",
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
-            "identifier": "1841.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/bio/schema.htm",
             "description": "The NHTSA Biomechanics Test Database is a repository of experimental data used by NHTSA for developing Anthropomophic Test Devices and associated Injury Criteria. The data is disseminated via this website for use by academia, the automotive industry, and the public to improve the safety of automobiles and reduce death and injuries on our nations highway. Because of the nature of the testing, the applicability of the data extends far beyond auto safety, and may be useful for those in the sports medicine, space travel, aircraft, military or any activity where the human body is exposed impact.",
-            "title": "Biomechanics Test Database - Latest Tests",
-            "isPartOf": "DOT-1841",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research",
-            "primaryITInvestmentUII": "021-961265599",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63533,51 +63510,60 @@
                     "title": "Latest Tests"
                 }
             ],
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/bio/schema.htm",
-            "dataQuality": false,
+            "identifier": "1841.2",
+            "isPartOf": "DOT-1841",
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
+            "landingPage": "https://data.transportation.gov/d/jex2-a3d9",
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
+            "title": "Biomechanics Test Database - Latest Tests"
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
-            "landingPage": "https://data.transportation.gov/d/jeyh-5nsj",
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
-            "identifier": "DOT-99",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": false,
             "description": "Data collected through FMCSA's Licensing and Insurance programs and information collections (BOC-3, OP-1, etc).",
-            "title": "Licensing and Insurance",
-            "primaryITInvestmentUII": "021-000001001",
-            "agencyProgramURL": "http://li-public.fmcsa.dot.gov/",
-            "programCode": [
-                "021:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63586,29 +63572,47 @@
                     "title": "Licensing and Insurance"
                 }
             ],
-            "spatial": "Carrier, Driver",
-            "dataQuality": false,
+            "identifier": "DOT-99",
+            "issued": "2018-12-17",
+            "keyword": [
+                "driver insurance; carrier registration; carrier license"
+            ],
+            "landingPage": "https://data.transportation.gov/d/jeyh-5nsj",
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
+            "title": "Licensing and Insurance"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/jfcp-usjh",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRA Safety Data Team",
+                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
+            },
+            "description": "This is the report page for Highway-Rail Grade Crossing Incidents Within Quiet Zones Detail Listing.",
+            "identifier": "https://data.transportation.gov/api/views/jfcp-usjh",
             "issued": "2024-09-11",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "crossing inventory",
                 "grade crossing incident",
@@ -63616,40 +63620,51 @@
                 "quiet zone",
                 "train horn"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRA Safety Data Team",
-                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/jfcp-usjh",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-27",
+            "programCode": [
+                "FRA Safety and Operations"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Railroad Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/jfcp-usjh",
-            "description": "This is the report page for Highway-Rail Grade Crossing Incidents Within Quiet Zones Detail Listing.",
-            "title": "Highway-Rail Grade Crossing Incidents Within Quiet Zones Detail Listing",
-            "programCode": [
-                "FRA Safety and Operations"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Highway-Rail Grade Crossing Incidents Within Quiet Zones Detail Listing"
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
-            "landingPage": "https://data.transportation.gov/d/jfma-6fjd",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/10martvt/10martvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "March 2010"
+                }
             ],
+            "identifier": "18.24",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -63659,57 +63674,60 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.24",
+            "landingPage": "https://data.transportation.gov/d/jfma-6fjd",
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
-            "title": "Monthly Traffic Volume Trends - March 2010",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/10martvt/10martvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "March 2010"
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
+            "title": "Monthly Traffic Volume Trends - March 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/jh56-mhgx",
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
+                    "description": "2013 Alabama HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/alabama2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Alabama"
+                }
+            ],
+            "identifier": "678.105",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -63723,87 +63741,45 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.105",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Alabama",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/jh56-mhgx",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/alabama2013.zip",
-                    "description": "2013 Alabama HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Alabama"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Alabama"
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
-            "landingPage": "https://data.transportation.gov/d/jhdh-ixke",
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
-            "identifier": "2068.2",
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
@@ -63812,59 +63788,63 @@
                     "title": "Data Catalog"
                 }
             ],
-            "describedBy": "https://wxde.fhwa.dot.gov/auth2/metadata.jsp",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/licenses/by-sa/3.0/",
-            "theme": [
-                "Transportation"
+            "identifier": "2068.2",
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
+            "landingPage": "https://data.transportation.gov/d/jhdh-ixke",
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
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
+            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/owners/SearchSafetyIssues",
+            "analysisUnit": "Vehicles , Tires, Child Safety Seats, Equipment",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/jhit-z9cc",
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
-            "identifier": "81.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Complaint information entered into NHTSA-ODI's vehicle owner's complaint database is used with other data sources to identify safety issues that warrant investigation and to determine if a safety-related defect trend exists. Complaint information is also analyzed to monitor existing recalls for proper scope and adequacy.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Complaints - Complaints Flat File",
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
@@ -63873,31 +63853,55 @@
                     "title": "Complaints Flat File"
                 }
             ],
-            "spatial": "N/A",
-            "describedBy": "http://www-odi.nhtsa.dot.gov/downloads/folders/Complaints/CMPL.txt",
-            "dataQuality": true,
+            "identifier": "81.1",
+            "isPartOf": "DOT-81",
+            "issued": "2002-12-16",
+            "keyword": [
+                "complaints",
+                "email",
+                "paper",
+                "phone",
+                "safercar.gov"
+            ],
+            "landingPage": "https://data.transportation.gov/d/jhit-z9cc",
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
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Complaints - Complaints Flat File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/jixs-h7uw",
             "bureauCode": [
                 "021:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kate Hartman",
+                "hasEmail": "mailto:kate.hartman@dot.gov"
+            },
+            "description": "ITS DataHub has partnered with the work zone data community, Federal Highway Administration's (FHWA) Work Zone Data Initiative (WZDI), and the broader Work Zone Data Working Group to create the following suite of proof-of-concept tools for work zone feeds compliant with the Work Zone Data Exchange (WZDx) specification. This data story describes those tools, focusing on the WZDx Feed Registry and the WZDx Data Archive.",
+            "identifier": "https://data.transportation.gov/api/views/jixs-h7uw",
             "issued": "2019-12-20",
-            "@type": "dcat:Dataset",
-            "modified": "2019-12-20",
             "keyword": [
                 "arterial",
                 "automobiles",
@@ -63919,40 +63923,52 @@
                 "trucking & motorcoaches",
                 "work zone data exchange (wzdx)"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/jixs-h7uw",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2019-12-20",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Department of Transportation"
             },
-            "identifier": "https://data.transportation.gov/api/views/jixs-h7uw",
-            "description": "ITS DataHub has partnered with the work zone data community, Federal Highway Administration's (FHWA) Work Zone Data Initiative (WZDI), and the broader Work Zone Data Working Group to create the following suite of proof-of-concept tools for work zone feeds compliant with the Work Zone Data Exchange (WZDx) specification. This data story describes those tools, focusing on the WZDx Feed Registry and the WZDx Data Archive.",
-            "title": "Work Zone Data Initiative Partnership",
-            "programCode": [
-                "021:013"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "Work Zone Data Initiative Partnership"
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
-            "landingPage": "https://data.transportation.gov/d/jjep-yru2",
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
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/gxrtmap.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Hwy/Rail Map with Table"
+                }
             ],
+            "identifier": "214.12",
+            "isPartOf": "DOT-214",
+            "issued": "2010-09-29",
             "keyword": [
                 "accident",
                 "casualty",
@@ -63965,86 +63981,49 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "214.12",
+            "landingPage": "https://data.transportation.gov/d/jjep-yru2",
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
-            "title": "Highway Rail Accidents - Hwy/Rail Map with Table",
-            "isPartOf": "DOT-214",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/gxrtmap.aspx",
-                    "mediaType": "text/csv",
-                    "title": "Hwy/Rail Map with Table"
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
+            "title": "Highway Rail Accidents - Hwy/Rail Map with Table"
         },
         {
-            "accessLevel": "public",
-            "bureauCode": [
-                "021:18"
-            ],
-            "landingPage": "https://data.transportation.gov/d/jkjp-8xef",
-            "issued": "1988-12-31",
-            "temporal": "R/1988-01-01/P1Y",
             "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
-            "collectionInstrument": "Transportation",
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
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "ftp://ftp.nhtsa.dot.gov/GES/",
+            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
+            "bureauCode": [
+                "021:18"
             ],
+            "categoryDesignation": "Administrative",
+            "collectionInstrument": "Transportation",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "524.3",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
             "description": "STATE DATA REPORTING SYSTEMS. Annual reports on the Fatality Analysis Reporting System (FARS) which is data regarding fatalities that is collected by a FARS analyst from each State and provided to NHTSA.",
-            "title": "GES Reports - 1999",
-            "isPartOf": "DOT-524",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64053,58 +64032,59 @@
                     "title": "1999"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
-            "dataQuality": true,
+            "identifier": "524.3",
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
+            "landingPage": "https://data.transportation.gov/d/jkjp-8xef",
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
+            "title": "GES Reports - 1999"
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
-            "landingPage": "https://data.transportation.gov/d/jm3h-j7xj",
-            "issued": "2014-12-29",
-            "temporal": "R/2014-12-29/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
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
-            "identifier": "DOT-700",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "Internal FHWA data program that assists in the collection and analysis of data on traffic volumes, vehicle classification, truck weights for traffic statistics, analysis; it is used for development of policies and regulations.  The monthly data are published in the Traffic Volume Trends (TVT) report.",
-            "title": "Travel Monitoring Analysis System (TMAS)",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/travelmonitoring.cfm",
-            "primaryITInvestmentUII": "021-938741189",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64113,47 +64093,51 @@
                     "title": "Travel Monitoring Analysis System"
                 }
             ],
-            "spatial": "National, State, Urban, Rural",
-            "dataQuality": true,
+            "identifier": "DOT-700",
+            "issued": "2014-12-29",
+            "keyword": [
+                "aadt",
+                "travel",
+                "vmt"
+            ],
+            "landingPage": "https://data.transportation.gov/d/jm3h-j7xj",
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
+            "title": "Travel Monitoring Analysis System (TMAS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://data.transportation.gov/d/jn4u-gqv9",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-01-26",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-21",
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
-            "identifier": "https://data.transportation.gov/api/views/jn4u-gqv9",
             "description": "",
-            "title": "Pocket Guide to Transportation-Vehicle Miles Traveled",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64161,65 +64145,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/jn4u-gqv9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/jn4u-gqv9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/jn4u-gqv9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/jn4u-gqv9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/jn4u-gqv9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/jn4u-gqv9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/jn4u-gqv9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/jn4u-gqv9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/jn4u-gqv9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "https://data.transportation.gov/api/views/jn4u-gqv9",
+            "issued": "2024-01-26",
+            "keyword": [
+                "pocket guide to transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/jn4u-gqv9",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-21",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Pocket Guide to Transportation-Vehicle Miles Traveled"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "The data system is not publicly available because it is related solely to internal agency management and may contain sensitive data.",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "https://fhwaapps.fhwa.dot.gov/upacsp",
+            "agencyProgramURL": "https://fhwaapps.fhwa.dot.gov",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/jpqs-jeau",
-            "issued": "2014-12-29",
-            "temporal": "2014-12-29/2014-12-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "access control",
-                "authentication",
-                "authorization",
-                "fhwa",
-                "icam",
-                "upacs"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "727.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "https://fhwaapps.fhwa.dot.gov/upacsp",
             "description": "UPACS stands for the User Profile and Access Control System. UPACS is the security control system that manages user authentication and associated access rights for individuals needing entry into one of FHWA's Information Systems.",
-            "title": "User Profile & Access Control System (UPACS) -",
-            "agencyProgramURL": "https://fhwaapps.fhwa.dot.gov",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64227,35 +64209,68 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "National, State",
-            "describedBy": "https://fhwaapps.fhwa.dot.gov/upacsp",
-            "dataQuality": true,
+            "identifier": "727.0",
+            "issued": "2014-12-29",
+            "keyword": [
+                "access control",
+                "authentication",
+                "authorization",
+                "fhwa",
+                "icam",
+                "upacs"
+            ],
+            "landingPage": "https://data.transportation.gov/d/jpqs-jeau",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "https://fhwaapps.fhwa.dot.gov/upacsp",
+            "modified": "2024-05-08",
+            "phone": "202-366-1746",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "rights": "The data system is not publicly available because it is related solely to internal agency management and may contain sensitive data.",
+            "spatial": "National, State",
+            "temporal": "2014-12-29/2014-12-29",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Administrative",
-            "phone": "202-366-1746",
-            "language": [
-                "en-US"
-            ]
+            "title": "User Profile & Access Control System (UPACS) -"
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
-            "landingPage": "https://data.transportation.gov/d/jqs7-jaq3",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/05jantvt/05jantvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "January 2005"
+                }
             ],
+            "identifier": "18.116",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -64265,79 +64280,80 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.116",
+            "landingPage": "https://data.transportation.gov/d/jqs7-jaq3",
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
-            "title": "Monthly Traffic Volume Trends - January 2005",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/05jantvt/05jantvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "January 2005"
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
+            "title": "Monthly Traffic Volume Trends - January 2005"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/jqyi-ax4d",
-            "issued": "2021-06-14",
             "@type": "dcat:Dataset",
-            "modified": "2022-01-14",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Chambers",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/jqyi-ax4d",
+            "issued": "2021-06-14",
+            "landingPage": "https://data.transportation.gov/d/jqyi-ax4d",
+            "modified": "2022-01-14",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Table of Contents"
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
-            "landingPage": "https://data.transportation.gov/d/jrab-i2nr",
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
+            "identifier": "25.2",
+            "isPartOf": "DOT-25",
+            "issued": "1980-01-01",
             "keyword": [
                 "crash",
                 "death",
@@ -64348,56 +64364,44 @@
                 "injury",
                 "vehicle"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "25.2",
+            "landingPage": "https://data.transportation.gov/d/jrab-i2nr",
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
-            "title": "Fatality Analysis Reporting System ( FARS ) - Online Query Tool",
-            "isPartOf": "DOT-25",
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
+            "title": "Fatality Analysis Reporting System ( FARS ) - Online Query Tool"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/jrb8-y6mq",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "A look at the consumer price index for transportation and its components as a measure of inflation faced by consumers.",
+            "identifier": "https://data.transportation.gov/api/views/jrb8-y6mq",
             "issued": "2024-04-04",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
             "keyword": [
                 "consumer price index",
                 "cpi",
@@ -64405,40 +64409,50 @@
                 "inflation and transportation",
                 "transportation inflation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/jrb8-y6mq",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-18",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/jrb8-y6mq",
-            "description": "A look at the consumer price index for transportation and its components as a measure of inflation faced by consumers.",
-            "title": "Transportation and Inflation - CPI",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Transportation and Inflation - CPI"
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
-            "landingPage": "https://data.transportation.gov/d/jrw6-ye84",
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
+            "identifier": "DOT-248",
+            "issued": "2010-01-05",
             "keyword": [
                 "5",
                 "assessment",
@@ -64452,75 +64466,79 @@
                 "safety",
                 "star"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "DOT-248",
+            "landingPage": "https://data.transportation.gov/d/jrw6-ye84",
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
-            "title": "New Car Assessment Program (NCAP) - 5 Star Safety Ratings",
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
-            "analysisUnit": "Vehicles",
-            "categoryDesignation": "Research",
-            "phone": "202-366-5269",
-            "language": [
-                "en-US"
-            ]
+            "title": "New Car Assessment Program (NCAP) - 5 Star Safety Ratings"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/jswi-2e7b",
-            "issued": "2023-10-17",
             "@type": "dcat:Dataset",
-            "modified": "2023-10-20",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sean Jahanmir",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/jswi-2e7b",
+            "issued": "2023-10-17",
+            "landingPage": "https://data.transportation.gov/d/jswi-2e7b",
+            "modified": "2023-10-20",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Border Crossing/Entry Data"
         },
         {
-            "accessLevel": "public",
-            "bureauCode": [
-                "021:15"
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
+            },
+            "dataQuality": false,
+            "describedBy": "http://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
+            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "2012 Arkansas HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/arkansas2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Arkansas"
+                }
             ],
-            "landingPage": "https://data.transportation.gov/d/jswk-bp9m",
+            "identifier": "678.57",
+            "isPartOf": "DOT-678",
             "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
-            "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
             "keyword": [
                 "aadt",
                 "condition",
@@ -64534,64 +64552,36 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.57",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Arkansas",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/jswk-bp9m",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/arkansas2012.zip",
-                    "description": "2012 Arkansas HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Arkansas"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Arkansas"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/jthd-hrj3",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/jthd-hrj3",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "SMT 2 (RR MILES)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64599,40 +64589,54 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/jthd-hrj3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/jthd-hrj3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/jthd-hrj3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/jthd-hrj3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/jthd-hrj3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/jthd-hrj3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/jthd-hrj3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/jthd-hrj3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/jthd-hrj3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/jthd-hrj3",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/jthd-hrj3",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "SMT 2 (RR MILES)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/jti8-bkwp",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Transportation Public Finance Statistics (TPFS) provides information on transportation-related revenue and expenditures for all levels of government, including federal, state, and local, and for all modes of transportation.",
+            "identifier": "https://data.transportation.gov/api/views/jti8-bkwp",
             "issued": "2024-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-31",
             "keyword": [
                 "expenditure",
                 "federal",
@@ -64643,53 +64647,33 @@
                 "state",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/jti8-bkwp",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-12-31",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/jti8-bkwp",
-            "description": "Transportation Public Finance Statistics (TPFS) provides information on transportation-related revenue and expenditures for all levels of government, including federal, state, and local, and for all modes of transportation.",
-            "title": "Transportation Public Finance Tables",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Transportation Public Finance Tables"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/jtvy-isaj",
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
-            "identifier": "https://data.transportation.gov/api/views/jtvy-isaj",
             "description": "",
-            "title": "AFF - P12a - Average Fuel Cost by Carrier Group",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64697,79 +64681,110 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/jtvy-isaj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/jtvy-isaj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/jtvy-isaj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/jtvy-isaj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/jtvy-isaj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/jtvy-isaj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/jtvy-isaj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/jtvy-isaj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/jtvy-isaj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/jtvy-isaj",
+            "issued": "2024-12-09",
+            "keyword": [
+                "aff"
+            ],
+            "landingPage": "https://data.transportation.gov/d/jtvy-isaj",
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
+            "title": "AFF - P12a - Average Fuel Cost by Carrier Group"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/jufd-yprb",
             "bureauCode": [
                 "021:27"
             ],
-            "issued": "2024-10-24",
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
-            "identifier": "https://data.transportation.gov/api/views/jufd-yprb",
+            "dataQuality": true,
             "description": "This is the landing page for operational data reported to the FRA on Form 6180.55 Injury/Illness Summary.",
-            "title": "Operational Data Reports - Landing Page",
+            "identifier": "https://data.transportation.gov/api/views/jufd-yprb",
+            "issued": "2024-10-24",
+            "landingPage": "https://data.transportation.gov/d/jufd-yprb",
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
+            "title": "Operational Data Reports - Landing Page"
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
-            "landingPage": "https://data.transportation.gov/d/juzf-xepk",
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
+                    "downloadURL": "http://www.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/docs/closedByEnforcement_FY2013_04-26-2013.xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Fiscal Year 2013"
+                }
             ],
+            "identifier": "96.9",
+            "isPartOf": "DOT-96",
+            "issued": "2018-12-17",
             "keyword": [
                 "bus",
                 "civil penalties",
@@ -64782,83 +64797,50 @@
                 "motor carrier",
                 "truck"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "96.9",
+            "landingPage": "https://data.transportation.gov/d/juzf-xepk",
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
-            "title": "Closed Enforcement Cases - Fiscal Year 2013",
-            "isPartOf": "DOT-96",
-            "agencyProgramURL": "http://www.fmcsa.dot.gov/regulations/enforcement/civil-penalties",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/docs/closedByEnforcement_FY2013_04-26-2013.xlsx",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "Fiscal Year 2013"
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
+            "title": "Closed Enforcement Cases - Fiscal Year 2013"
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
-            "landingPage": "https://data.transportation.gov/d/jvqa-gwse",
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
-            "identifier": "664.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Railroad Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "https://gradedec.fra.dot.gov/",
             "description": "General Purpose Data and Statistics.  GradeDEC.Net is a web-based tool for the investment analysis of highway-rail grade crossing improvements.  It provides state departments of transportation, local governments, metropolitan planning agencies, inspectors, and railroad companies with the online ability to conduct benefit-cost analysis of highway-rail grade crossing infrastructure investments. GradeDEC.Net allows users to divert highway traffic to and from closed or separated grade crossings to adjacent crossings, and calculate a full set of benefits including changes in accident risk associated with changes in traditional grade crossing technology. Users can also evaluate supplemental safety measures listed in the Notice of Proposed Rulemaking covering the use of locomotive horns at highway-rail grade crossing. Users are also able to save an analysis on-site for later revision and update and submit reports directly to the FRA.",
-            "title": "GradeDec.Net - Online Tool",
-            "isPartOf": "DOT-664",
-            "agencyProgramURL": "https://gradedec.fra.dot.gov/",
-            "primaryITInvestmentUII": "021-092395457",
-            "programCode": [
-                "021:036"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64867,36 +64849,69 @@
                     "title": "Online Tool"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "https://gradedec.fra.dot.gov/",
-            "dataQuality": true,
+            "identifier": "664.1",
+            "isPartOf": "DOT-664",
+            "issued": "2014-11-21",
+            "keyword": [
+                "fra system for highway-rail grade crossing",
+                "gade crossing invetment analysis"
+            ],
+            "landingPage": "https://data.transportation.gov/d/jvqa-gwse",
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
+            "title": "GradeDec.Net - Online Tool"
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
-            "landingPage": "https://data.transportation.gov/d/jvta-nc8m",
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
+                    "downloadURL": "http://www.fmcsa.dot.gov/about/infosys/softwarefoia/ProVu_3.2.0.12_Full_Install.exe",
+                    "mediaType": "application/xml",
+                    "title": "CSP XML Viewer"
+                }
             ],
+            "identifier": "123.3",
+            "isPartOf": "DOT-123",
+            "issued": "2000-01-01",
             "keyword": [
                 "bus",
                 "company safety profile",
@@ -64913,82 +64928,49 @@
                 "safersys",
                 "safety and fitness electronic records"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "123.3",
+            "landingPage": "https://data.transportation.gov/d/jvta-nc8m",
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
-            "title": "SAFER - Company Safety Profile - CSP XML Viewer",
-            "isPartOf": "DOT-123",
-            "agencyProgramURL": "http://safer.fmcsa.dot.gov/CSP_Order.asp",
-            "programCode": [
-                "021:026"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fmcsa.dot.gov/about/infosys/softwarefoia/ProVu_3.2.0.12_Full_Install.exe",
-                    "mediaType": "application/xml",
-                    "title": "CSP XML Viewer"
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
+            "title": "SAFER - Company Safety Profile - CSP XML Viewer"
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
-            "landingPage": "https://data.transportation.gov/d/jxne-p3z4",
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
-            "identifier": "364.26",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2008",
-            "isPartOf": "DOT-364",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
-            "primaryITInvestmentUII": "021-621341357",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -64997,33 +64979,62 @@
                     "title": "Event Data Records Reports - 2008"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.26",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/jxne-p3z4",
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
+            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.21949/1503762",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2017-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2016-12-23",
-            "references": [
-                "https://rosap.ntl.bts.gov/view/dot/3612"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Transportation Library Data Curator",
+                "hasEmail": "mailto:ntldatacurator@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "As our highway infrastructure continues to age, there is the imperative need to renew the entire network while keeping it operational. Moreover, many highway corridors and regional networks are becoming ever more congested. As a result there is an increasing need to (1) examine various construction alternatives within those corridors and networks to determine the potential disruption and/or benefit that alternative renewal activities may have over time, and (2) examine the effect of constructing multiple corridors concurrently or in sequence. Without an evaluation of the various construction alternatives during the program and project development process, negative impacts on the traveling public and the local communities may increase dramatically. The research on Project R11 focused on answering the following related questions: \u2022 How should highway reconstruction projects be set in space and time to minimize disruption to the traveling public, businesses, and adjacent communities? \u2022 What is the traffic impact on the regional network when multiple corridors are being considered for renewal? \u2022 Are there strategies that may minimize impacts on the corridor and/or regional network?  This zip file contains comma separated value (.csv) files of data to support SHRP 2 report S2-R11-RW-1, Strategic approaches at the corridor and network level to minimize disruption from the renewal process. Zip size is 0.46 MB. Files were accessed in Microsoft Excel 2016. Data will be preserved as is. To view the publication see: https://rosap.ntl.bts.gov/view/dot/3612",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "As our highway infrastructure continues to age, there is the imperative need to renew the entire network while keeping it operational. Moreover, many highway corridors and regional networks are becoming ever more congested. As a result there is an increasing need to (1) examine various construction alternatives within those corridors and networks to determine the potential disruption and/or benefit that alternative renewal activities may have over time, and (2) examine the effect of constructing multiple corridors concurrently or in sequence. Without an evaluation of the various construction alternatives during the program and project development process, negative impacts on the traveling public and the local communities may increase dramatically. The research on Project R11 focused on answering the following related questions: \u2022 How should highway reconstruction projects be set in space and time to minimize disruption to the traveling public, businesses, and adjacent communities? \u2022 What is the traffic impact on the regional network when multiple corridors are being considered for renewal? \u2022 Are there strategies that may minimize impacts on the corridor and/or regional network?  This zip file contains comma separated value (.csv) files of data to support SHRP 2 report S2-R11-RW-1, Strategic approaches at the corridor and network level to minimize disruption from the renewal process. Zip size is 0.46 MB. Files were accessed in Microsoft Excel 2016. Data will be preserved as is. To view the publication see: https://rosap.ntl.bts.gov/view/dot/3612",
+                    "downloadURL": "https://doi.org/10.21949/1503762",
+                    "mediaType": "application/zip",
+                    "title": "Strategic Approaches at the Corridor and Network Level to Minimize Disruption from the Renewal Process [supporting datasets]"
+                }
             ],
+            "identifier": "https://data.transportation.gov/api/views/jyc5-9vwx",
+            "issued": "2017-01-01",
             "keyword": [
                 "decision support systems",
                 "highway corridors",
@@ -65039,71 +65050,75 @@
                 "transportation improvement projects",
                 "urban renewal",
                 "work zone traffic control"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Transportation Library Data Curator",
-                "hasEmail": "mailto:ntldatacurator@dot.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/jyc5-9vwx",
-            "description": "As our highway infrastructure continues to age, there is the imperative need to renew the entire network while keeping it operational. Moreover, many highway corridors and regional networks are becoming ever more congested. As a result there is an increasing need to (1) examine various construction alternatives within those corridors and networks to determine the potential disruption and/or benefit that alternative renewal activities may have over time, and (2) examine the effect of constructing multiple corridors concurrently or in sequence. Without an evaluation of the various construction alternatives during the program and project development process, negative impacts on the traveling public and the local communities may increase dramatically. The research on Project R11 focused on answering the following related questions: \u2022 How should highway reconstruction projects be set in space and time to minimize disruption to the traveling public, businesses, and adjacent communities? \u2022 What is the traffic impact on the regional network when multiple corridors are being considered for renewal? \u2022 Are there strategies that may minimize impacts on the corridor and/or regional network?  This zip file contains comma separated value (.csv) files of data to support SHRP 2 report S2-R11-RW-1, Strategic approaches at the corridor and network level to minimize disruption from the renewal process. Zip size is 0.46 MB. Files were accessed in Microsoft Excel 2016. Data will be preserved as is. To view the publication see: https://rosap.ntl.bts.gov/view/dot/3612",
-            "title": "Strategic Approaches at the Corridor and Network Level to Minimize Disruption from the Renewal Process [supporting datasets]",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://doi.org/10.21949/1503762",
-                    "description": "As our highway infrastructure continues to age, there is the imperative need to renew the entire network while keeping it operational. Moreover, many highway corridors and regional networks are becoming ever more congested. As a result there is an increasing need to (1) examine various construction alternatives within those corridors and networks to determine the potential disruption and/or benefit that alternative renewal activities may have over time, and (2) examine the effect of constructing multiple corridors concurrently or in sequence. Without an evaluation of the various construction alternatives during the program and project development process, negative impacts on the traveling public and the local communities may increase dramatically. The research on Project R11 focused on answering the following related questions: \u2022 How should highway reconstruction projects be set in space and time to minimize disruption to the traveling public, businesses, and adjacent communities? \u2022 What is the traffic impact on the regional network when multiple corridors are being considered for renewal? \u2022 Are there strategies that may minimize impacts on the corridor and/or regional network?  This zip file contains comma separated value (.csv) files of data to support SHRP 2 report S2-R11-RW-1, Strategic approaches at the corridor and network level to minimize disruption from the renewal process. Zip size is 0.46 MB. Files were accessed in Microsoft Excel 2016. Data will be preserved as is. To view the publication see: https://rosap.ntl.bts.gov/view/dot/3612",
-                    "@type": "dcat:Distribution",
-                    "title": "Strategic Approaches at the Corridor and Network Level to Minimize Disruption from the Renewal Process [supporting datasets]"
-                }
-            ],
-            "spatial": "United States",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
+            ],
+            "landingPage": "https://doi.org/10.21949/1503762",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2016-12-23",
+            "programCode": [
+                "021:013"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "references": [
+                "https://rosap.ntl.bts.gov/view/dot/3612"
+            ],
+            "spatial": "United States",
+            "title": "Strategic Approaches at the Corridor and Network Level to Minimize Disruption from the Renewal Process [supporting datasets]"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/jyrm-py8x",
-            "issued": "2021-05-10",
             "@type": "dcat:Dataset",
-            "modified": "2024-10-02",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sean Jahanmir",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/jyrm-py8x",
+            "issued": "2021-05-10",
+            "landingPage": "https://data.transportation.gov/d/jyrm-py8x",
+            "modified": "2024-10-02",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Moving People"
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
-            "landingPage": "https://data.transportation.gov/d/jzka-dpba",
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
+                    "description": "Decodes a Vehicle Identification Number (VIN) and other basic specifications for regulated vehicle types",
+                    "downloadURL": "http://vpic.nhtsa.dot.gov/decoder/",
+                    "mediaType": "text/html",
+                    "title": "VIN Decoder"
+                }
             ],
+            "identifier": "65.4",
+            "isPartOf": "DOT-65",
+            "issued": "2015-10-05",
             "keyword": [
                 "49",
                 "551",
@@ -65140,81 +65155,49 @@
                 "vin",
                 "vpic"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "65.4",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "The NHTSA Product Information Catalog and Vehicle Listing (vPIC) is a consolidated platform that presents data collected within the manufacturer reported data from CFR 49 Parts 551 - 574 for use in a variety of modern tools. NHTSA's vPIC platform is intended to serve as a centralized source for basic Vehicle Identification Number (VIN) decoding, Manufacturer Information Database (MID), Manufacturer Equipment Plant Identification and associated data. vPIC is intended to support the Open Data and Transparency initiatives of the agency by allowing the data to be freely used by the public without the burden of manual retrieval from a library of electronic documents (PDFs). While these documents will still be available online for viewing within the Manufacturer Information Database (MID) module of vPIC one can view and use the actual data through the VIN Decoder and Application Programming Interface (API) modules.",
-            "title": "NHTSA Product Information Catalog and Vehicle Listing (vPIC) - VIN Decoder",
-            "isPartOf": "DOT-65",
-            "agencyProgramURL": "http://vpic.nhtsa.dot.gov/",
+            "landingPage": "https://data.transportation.gov/d/jzka-dpba",
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
-                    "downloadURL": "http://vpic.nhtsa.dot.gov/decoder/",
-                    "description": "Decodes a Vehicle Identification Number (VIN) and other basic specifications for regulated vehicle types",
-                    "@type": "dcat:Distribution",
-                    "title": "VIN Decoder"
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
+            "title": "NHTSA Product Information Catalog and Vehicle Listing (vPIC) - VIN Decoder"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "The data system is not publicly available because it is related solely to internal agency management and may contain sensitive data.",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/tpp/ddetfp.htm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/tpp/ddetfp.htm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/k28r-xkgi",
-            "issued": "2014-12-29",
-            "temporal": "2014-12-29/2014-12-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative - Training & Education",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "dwight david eisenhower",
-                "fellowship",
-                "transportation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "699.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "DDETFP is a web-based application used to measure the performance of the DDETFP program, enhance reporting, and evaluate the programs' effectiveness in meeting goals and objectives in advancing transportation education, research, and workforce development. The system has been converted from a Microsoft Access application at the request of the agency due to PII.",
-            "title": "Dwight David Eisenhower Transportation Fellowship Program System -",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/tpp/ddetfp.htm",
-            "primaryITInvestmentUII": "021-670869498",
-            "programCode": [
-                "021:011"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -65222,44 +65205,48 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "International",
-            "dataQuality": true,
+            "identifier": "699.0",
+            "issued": "2014-12-29",
+            "keyword": [
+                "dwight david eisenhower",
+                "fellowship",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/k28r-xkgi",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/tpp/ddetfp.htm",
+            "modified": "2024-05-08",
+            "phone": "404-562-3917",
+            "primaryITInvestmentUII": "021-670869498",
+            "programCode": [
+                "021:011"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "rights": "The data system is not publicly available because it is related solely to internal agency management and may contain sensitive data.",
+            "spatial": "International",
+            "temporal": "2014-12-29/2014-12-29",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Administrative - Training & Education",
-            "phone": "404-562-3917",
-            "language": [
-                "en-US"
-            ]
+            "title": "Dwight David Eisenhower Transportation Fellowship Program System -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/k3id-nynu",
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
-            "identifier": "https://data.transportation.gov/api/views/k3id-nynu",
             "description": "This table shows the number and percent of people in the contiguous United States (excludes Alaska and Hawaii) potentially exposed to different levels of noise from combined aviation, road and passenger rail sources.",
-            "title": "Population potentially exposed to combined aviation, road and rail noise, 2016 and 2018",
-            "programCode": [
-                "021:052"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -65267,40 +65254,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/k3id-nynu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/k3id-nynu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/k3id-nynu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/k3id-nynu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/k3id-nynu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/k3id-nynu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/k3id-nynu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/k3id-nynu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/k3id-nynu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "https://data.transportation.gov/api/views/k3id-nynu",
+            "issued": "2020-07-16",
+            "landingPage": "https://data.transportation.gov/d/k3id-nynu",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2020-07-16",
+            "programCode": [
+                "021:052"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Population potentially exposed to combined aviation, road and rail noise, 2016 and 2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/k3jk-mcm7",
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
+                    "description": "2013 Maryland HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/maryland2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Maryland"
+                }
+            ],
+            "identifier": "678.124",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -65314,81 +65332,43 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.124",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Maryland",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/k3jk-mcm7",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/maryland2013.zip",
-                    "description": "2013 Maryland HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Maryland"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Maryland"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "This dataset can be made available to the public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/k3mt-4ggh",
-            "issued": "2014-11-21",
-            "temporal": "R/2014-11-21/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "cybersecurity",
-                "information technology",
-                "specialized",
-                "training",
-                "transportation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "1631.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
             "description": "This data set contains information about the Department of Transportation Office of the Chief Information Officer Black Hat Cybersecurity Specialized Education Training Program. This information contains the individual participating Federal employees, contactor support, and an overview of the training session and objectives.",
-            "title": "DOT Black Hat Cybersecurity Specialized Education Training Program -",
-            "primaryITInvestmentUII": "021-325711125",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -65396,70 +65376,105 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "theme": [
-                "Transportation"
+            "identifier": "1631.0",
+            "issued": "2014-11-21",
+            "keyword": [
+                "cybersecurity",
+                "information technology",
+                "specialized",
+                "training",
+                "transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/k3mt-4ggh",
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
+            "rights": "This dataset can be made available to the public",
+            "temporal": "R/2014-11-21/P1Y",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "DOT Black Hat Cybersecurity Specialized Education Training Program -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/k4x2-7tix",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This report contains summary level data for all open highway-rail crossings, broken out by crossing type (public, private, and not specified). There are four views of data: by (1) state, (2) county, (3) city, and (4) railroad.",
+            "identifier": "https://data.transportation.gov/api/views/k4x2-7tix",
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
+            "landingPage": "https://data.transportation.gov/d/k4x2-7tix",
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
-            "identifier": "https://data.transportation.gov/api/views/k4x2-7tix",
-            "description": "This report contains summary level data for all open highway-rail crossings, broken out by crossing type (public, private, and not specified). There are four views of data: by (1) state, (2) county, (3) city, and (4) railroad.",
-            "title": "Crossing Inventory High-Level Summary (8.05)",
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
+            "title": "Crossing Inventory High-Level Summary (8.05)"
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
-            "landingPage": "https://data.transportation.gov/d/k563-ifj8",
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
+            "identifier": "130.1",
+            "isPartOf": "DOT-130",
+            "issued": "2009-03-15",
             "keyword": [
                 "authority grated",
                 "compliance review",
@@ -65471,120 +65486,83 @@
                 "safety audit",
                 "violation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "130.1",
+            "landingPage": "https://data.transportation.gov/d/k563-ifj8",
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
-            "title": "A&I - Passenger Carrier Statistics - Pasenger Carrier Safety Data",
-            "isPartOf": "DOT-130",
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
-            "categoryDesignation": "Research",
-            "analysisUnit": "Passenger Carriers",
-            "phone": "202-366-4869",
-            "language": [
-                "en-US"
-            ]
+            "title": "A&I - Passenger Carrier Statistics - Pasenger Carrier Safety Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/k65c-hne3",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2020-04-13",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-29",
-            "keyword": [
-                "multifactor productivity",
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
-            "identifier": "https://data.transportation.gov/api/views/k65c-hne3",
             "description": "Transportation total factor productivity",
-            "title": "Transportation Economic Trends: Productivity - Total Factor",
+            "identifier": "https://data.transportation.gov/api/views/k65c-hne3",
+            "issued": "2020-04-13",
+            "keyword": [
+                "multifactor productivity",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/k65c-hne3",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-29",
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
+            "title": "Transportation Economic Trends: Productivity - Total Factor"
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
-            "landingPage": "https://data.transportation.gov/d/k6aw-iugq",
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
-            "identifier": "18.102",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - March 2006",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -65593,57 +65571,55 @@
                     "title": "March 2006"
                 }
             ],
+            "identifier": "18.102",
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
+            "landingPage": "https://data.transportation.gov/d/k6aw-iugq",
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
+            "title": "Monthly Traffic Volume Trends - March 2006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/k74u-yqu6",
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
-            "identifier": "https://data.transportation.gov/api/views/k74u-yqu6",
+            "dataQuality": true,
             "description": "The data describe freeway car-following behavior (such as velocity, acceleration, and relative position) for the car-following instances observed during 59 data collection runs, performed through the Federal Highway Administration (FHWA) Turner Fairbank Highway Research Center\u2019s (TFHRC) Living Laboratory (LL). Data were collected using an Instrumented Research Vehicle (IRV) along freeways in northern Virginia to better understand work zone driver behaviors. The USDOT Volpe National Transportation Systems Center (Volpe Center) identified, isolated, and classified individual car following instances from within the raw datasets (classification parameters included roadway type, level of congestion, and speed limit), then processed, refined, and cleaned the dataset.\n\nThis table contains the car-following instances recorded by Volpe staff. See also the runs table (https://datahub.transportation.gov/Automobiles/Enhancing-Microsimulation-Models-for-Improved-Work/285w-yjf5) and radar table (https://datahub.transportation.gov/Automobiles/Enhancing-Microsimulation-Models-for-Improved-Work/uvrt-varj).",
-            "title": "Enhancing Microsimulation Models for Improved Work Zone Planning: Car-Following Data from Northern Virginia (Instances)",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -65651,127 +65627,133 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/k74u-yqu6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/k74u-yqu6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/k74u-yqu6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/k74u-yqu6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/k74u-yqu6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/k74u-yqu6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/k74u-yqu6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/k74u-yqu6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/k74u-yqu6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "-77.0573,38.7046,-77.2278,38.9563",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/k74u-yqu6",
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
+            "landingPage": "https://data.transportation.gov/d/k74u-yqu6",
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
+            "title": "Enhancing Microsimulation Models for Improved Work Zone Planning: Car-Following Data from Northern Virginia (Instances)"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/k74v-6hdm",
-            "issued": "2022-02-16",
             "@type": "dcat:Dataset",
-            "modified": "2022-02-16",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Admin Team",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
+            "description": "Once you've picked an automation method, get help getting it set up!",
             "identifier": "https://data.transportation.gov/api/views/k74v-6hdm",
+            "issued": "2022-02-16",
+            "landingPage": "https://data.transportation.gov/d/k74v-6hdm",
+            "modified": "2022-02-16",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "Once you've picked an automation method, get help getting it set up!",
-            "title": "DOT Automation - New Automation Landing Page",
             "theme": [
                 "Administrative"
-            ]
+            ],
+            "title": "DOT Automation - New Automation Landing Page"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/k798-qm7g",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Economic concepts related to the contribution of transportation to the economy",
+            "identifier": "https://data.transportation.gov/api/views/k798-qm7g",
             "issued": "2020-02-12",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
             "keyword": [
                 "contribution of transportation",
                 "economics",
                 "transportation",
                 "transportation satellite accounts"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/k798-qm7g",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-18",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/k798-qm7g",
-            "description": "Economic concepts related to the contribution of transportation to the economy",
-            "title": "Transportation Economic Concepts: Contribution of Transportation",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Transportation Economic Concepts: Contribution of Transportation"
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
-            "landingPage": "https://data.transportation.gov/d/k7u5-7fke",
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
-            "identifier": "364.30",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2012",
-            "isPartOf": "DOT-364",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
-            "primaryITInvestmentUII": "021-621341357",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -65780,35 +65762,68 @@
                     "title": "Event Data Records Reports - 2012"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.30",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/k7u5-7fke",
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
+            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2012"
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
-            "landingPage": "https://data.transportation.gov/d/k8bj-3zn2",
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
+                    "downloadURL": "http://www.safercar.gov/Vehicle+Shoppers/5-Star+Safety+Ratings/1990-2010+Vehicles",
+                    "mediaType": "text/html",
+                    "title": "1990-2010 Models"
+                }
             ],
+            "identifier": "248.6",
+            "isPartOf": "DOT-248",
+            "issued": "2010-01-05",
             "keyword": [
                 "5",
                 "assessment",
@@ -65822,85 +65837,42 @@
                 "safety",
                 "star"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "248.6",
+            "landingPage": "https://data.transportation.gov/d/k8bj-3zn2",
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
-            "title": "New Car Assessment Program (NCAP) - 5 Star Safety Ratings - 1990-2010 Models",
-            "isPartOf": "DOT-248",
-            "agencyProgramURL": "http://www.safercar.gov/Vehicle+Shoppers",
-            "programCode": [
-                "021:031"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.safercar.gov/Vehicle+Shoppers/5-Star+Safety+Ratings/1990-2010+Vehicles",
-                    "mediaType": "text/html",
-                    "title": "1990-2010 Models"
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
+            "title": "New Car Assessment Program (NCAP) - 5 Star Safety Ratings - 1990-2010 Models"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/kaak-2432",
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
-            "identifier": "https://data.transportation.gov/api/views/kaak-2432",
             "description": "Part of Wyoming Department of Transportation Connected Vehicle Pilot Phase 4. Verify that OBUs use different LTE-V2X Configuration Profiles based on the vehicle's speed.\nHost and remote vehicles travelling below 120 kmph\nHost and remote vehicles travelling above 120 kmph",
-            "title": "LTE-V2X Wyoming Connected Vehicle Pilot test ID WV2IMCT-1 Vehicle 2 80 mph",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -65908,44 +65880,90 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/kaak-2432/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/kaak-2432/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/kaak-2432/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/kaak-2432/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/kaak-2432/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/kaak-2432/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/kaak-2432/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/kaak-2432/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/kaak-2432/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Wyoming",
+            "identifier": "https://data.transportation.gov/api/views/kaak-2432",
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
+            "landingPage": "https://data.transportation.gov/d/kaak-2432",
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
+            "title": "LTE-V2X Wyoming Connected Vehicle Pilot test ID WV2IMCT-1 Vehicle 2 80 mph"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/kagd-275f",
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
+                    "description": "2013 District of Columbia HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/district2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 District of Columbia"
+                }
+            ],
+            "identifier": "678.155",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -65959,60 +65977,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.155",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
```

