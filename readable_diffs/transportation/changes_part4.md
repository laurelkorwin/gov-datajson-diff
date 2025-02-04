# Change History for transportation.json (Part 4)

### Changes from 31606f9 to dd2190f (Part 3/9)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-            "phone": "202-366-4869",
-            "language": [
-                "en-US"
-            ]
+            "title": "A&I - Safety Programs - Data Mining Tool"
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
-            "identifier": "https://data.transportation.gov/api/views/9g29-2wbf",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 1990",
-            "title": "Historic HPMS Data (Sample) - 1990",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26225,72 +26205,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9g29-2wbf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9g29-2wbf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9g29-2wbf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/9g29-2wbf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9g29-2wbf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9g29-2wbf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9g29-2wbf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9g29-2wbf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9g29-2wbf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/9g29-2wbf",
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
+            "title": "Historic HPMS Data (Sample) - 1990"
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
-            "landingPage": "https://data.transportation.gov/d/9gq9-j3w2",
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
-            "identifier": "364.15",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2000",
-            "isPartOf": "DOT-364",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
-            "primaryITInvestmentUII": "021-621341357",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26299,109 +26281,143 @@
                     "title": "Event Data Records Reports - 2000"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.15",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/9gq9-j3w2",
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
+            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/9h78-phpi",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Economic concepts related to transportation assets and transportation capital stock",
+            "identifier": "https://data.transportation.gov/api/views/9h78-phpi",
             "issued": "2020-02-24",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
             "keyword": [
                 "capital stock",
                 "transportation",
                 "transportation assets",
                 "transportation economics"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/9h78-phpi",
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
-            "identifier": "https://data.transportation.gov/api/views/9h78-phpi",
-            "description": "Economic concepts related to transportation assets and transportation capital stock",
-            "title": "Transportation Economic Concepts: Value of Transportation - Transportation Assets and Capital Stock",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Transportation Economic Concepts: Value of Transportation - Transportation Assets and Capital Stock"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/9hnw-nt86",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Reports for highway-rail grade crossing incidents can be found within this portal. All impacts between railroad on-track equipment and highway users at a highway-rail grade crossing are reported by railroads to the FRA on Form FRA F 6180.57 Highway-Rail Grade Crossing Accident/Incident Report.",
+            "identifier": "https://data.transportation.gov/api/views/9hnw-nt86",
             "issued": "2023-08-04",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "highway-rail crossing incidents",
                 "highway-rail grade crossing",
                 "incidents",
                 "road or pathway crosses one or more railroad tracks"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/9hnw-nt86",
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
-            "identifier": "https://data.transportation.gov/api/views/9hnw-nt86",
-            "description": "Reports for highway-rail grade crossing incidents can be found within this portal. All impacts between railroad on-track equipment and highway users at a highway-rail grade crossing are reported by railroads to the FRA on Form FRA F 6180.57 Highway-Rail Grade Crossing Accident/Incident Report.",
-            "title": "Highway-Rail Crossing Incidents - Landing Page",
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
+            "title": "Highway-Rail Crossing Incidents - Landing Page"
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
-            "landingPage": "https://data.transportation.gov/d/9hpd-e2mi",
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
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/on_the_fly_download.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Download Accident Data"
+                }
             ],
+            "identifier": "199.1",
+            "isPartOf": "DOT-199",
+            "issued": "2010-09-29",
             "keyword": [
                 "acts of god",
                 "collisions",
@@ -26412,83 +26428,48 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "199.1",
+            "landingPage": "https://data.transportation.gov/d/9hpd-e2mi",
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
-            "title": "Rail Equipment Accidents - Download Accident Data",
-            "isPartOf": "DOT-199",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:036"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/on_the_fly_download.aspx",
-                    "mediaType": "text/csv",
-                    "title": "Download Accident Data"
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
+            "title": "Rail Equipment Accidents - Download Accident Data"
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
-            "landingPage": "https://data.transportation.gov/d/9ib2-dmqz",
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
-            "identifier": "692.17",
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
@@ -26497,32 +26478,62 @@
                     "title": "2010 Fatal Crashes"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.17",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/9ib2-dmqz",
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
-            "landingPage": "https://doi.org/10.21949/1503765",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2014-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2016-12-21",
-            "references": [
-                "https://rosap.ntl.bts.gov/view/dot/3610"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Transportation Library Data Curator",
+                "hasEmail": "mailto:ntldatacurator@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Washington site used the reliability guide from Project L02, analysis tools for forecasting reliability and estimating impacts from Project L07, Project L08, and Project C11 as well as the guide on reliability performance measures from the Project L05 product. The Washington site focused on the I-5 and I-405 corridors from Lynnwood to Tukwila (approximately 30 miles long for each corridor running through the Puget Sound metropolitan region), and the SR-522 urban arterial near Seattle. The pilot testing demonstrated that the SHRP 2 Reliability data and analytical products clearly addressed the practical challenges that transportation agencies face when monitoring and analyzing travel time reliability. However, most tools require significant improvements at the application level. Project L38D was intended to evaluate a suite of projects to determine their readiness for implementation. Those projects had a logical structure consisting of data collection, analysis, and project prioritization.  The datasets in this zip file, which is 90.5 MB in size, are in support of SHRP 2 reliability project L38D, \"Pilot testing of SHRP 2 reliability data and analytical products: Washington.\" The project report can be accessed via the following URL: https://rosap.ntl.bts.gov/view/dot/3610  This zip file contains 20 Comma Separated Values (CSV) files, which can be opened using most text editing programs.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The Washington site used the reliability guide from Project L02, analysis tools for forecasting reliability and estimating impacts from Project L07, Project L08, and Project C11 as well as the guide on reliability performance measures from the Project L05 product. The Washington site focused on the I-5 and I-405 corridors from Lynnwood to Tukwila (approximately 30 miles long for each corridor running through the Puget Sound metropolitan region), and the SR-522 urban arterial near Seattle. The pilot testing demonstrated that the SHRP 2 Reliability data and analytical products clearly addressed the practical challenges that transportation agencies face when monitoring and analyzing travel time reliability. However, most tools require significant improvements at the application level. Project L38D was intended to evaluate a suite of projects to determine their readiness for implementation. Those projects had a logical structure consisting of data collection, analysis, and project prioritization.  The datasets in this zip file, which is 90.5 MB in size, are in support of SHRP 2 reliability project L38D, \"Pilot testing of SHRP 2 reliability data and analytical products: Washington.\" The project report can be accessed via the following URL: https://rosap.ntl.bts.gov/view/dot/3610  This zip file contains 20 Comma Separated Values (CSV) files, which can be opened using most text editing programs.",
+                    "downloadURL": "https://doi.org/10.21949/1503765",
+                    "mediaType": "application/zip",
+                    "title": "Pilot Testing of SHRP 2 Reliability Data and Analytical Products: Washington [supporting datasets]"
+                }
             ],
+            "identifier": "https://data.transportation.gov/api/views/9ijv-gbfe",
+            "issued": "2014-01-01",
             "keyword": [
                 "business practices",
                 "data analysis",
@@ -26535,67 +26546,39 @@
                 "travel time",
                 "travel time reliability"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Transportation Library Data Curator",
-                "hasEmail": "mailto:ntldatacurator@dot.gov"
-            },
+            "landingPage": "https://doi.org/10.21949/1503765",
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
-            "identifier": "https://data.transportation.gov/api/views/9ijv-gbfe",
-            "description": "The Washington site used the reliability guide from Project L02, analysis tools for forecasting reliability and estimating impacts from Project L07, Project L08, and Project C11 as well as the guide on reliability performance measures from the Project L05 product. The Washington site focused on the I-5 and I-405 corridors from Lynnwood to Tukwila (approximately 30 miles long for each corridor running through the Puget Sound metropolitan region), and the SR-522 urban arterial near Seattle. The pilot testing demonstrated that the SHRP 2 Reliability data and analytical products clearly addressed the practical challenges that transportation agencies face when monitoring and analyzing travel time reliability. However, most tools require significant improvements at the application level. Project L38D was intended to evaluate a suite of projects to determine their readiness for implementation. Those projects had a logical structure consisting of data collection, analysis, and project prioritization.  The datasets in this zip file, which is 90.5 MB in size, are in support of SHRP 2 reliability project L38D, \"Pilot testing of SHRP 2 reliability data and analytical products: Washington.\" The project report can be accessed via the following URL: https://rosap.ntl.bts.gov/view/dot/3610  This zip file contains 20 Comma Separated Values (CSV) files, which can be opened using most text editing programs.",
-            "title": "Pilot Testing of SHRP 2 Reliability Data and Analytical Products: Washington [supporting datasets]",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://doi.org/10.21949/1503765",
-                    "description": "The Washington site used the reliability guide from Project L02, analysis tools for forecasting reliability and estimating impacts from Project L07, Project L08, and Project C11 as well as the guide on reliability performance measures from the Project L05 product. The Washington site focused on the I-5 and I-405 corridors from Lynnwood to Tukwila (approximately 30 miles long for each corridor running through the Puget Sound metropolitan region), and the SR-522 urban arterial near Seattle. The pilot testing demonstrated that the SHRP 2 Reliability data and analytical products clearly addressed the practical challenges that transportation agencies face when monitoring and analyzing travel time reliability. However, most tools require significant improvements at the application level. Project L38D was intended to evaluate a suite of projects to determine their readiness for implementation. Those projects had a logical structure consisting of data collection, analysis, and project prioritization.  The datasets in this zip file, which is 90.5 MB in size, are in support of SHRP 2 reliability project L38D, \"Pilot testing of SHRP 2 reliability data and analytical products: Washington.\" The project report can be accessed via the following URL: https://rosap.ntl.bts.gov/view/dot/3610  This zip file contains 20 Comma Separated Values (CSV) files, which can be opened using most text editing programs.",
-                    "@type": "dcat:Distribution",
-                    "title": "Pilot Testing of SHRP 2 Reliability Data and Analytical Products: Washington [supporting datasets]"
-                }
+            "references": [
+                "https://rosap.ntl.bts.gov/view/dot/3610"
             ],
             "spatial": "United States, Washington",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "language": [
-                "en-US"
-            ]
+            "title": "Pilot Testing of SHRP 2 Reliability Data and Analytical Products: Washington [supporting datasets]"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/9ivb-8ae9",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2025-01-07",
-            "temporal": "R/2014-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-23",
-            "keyword": [
-                "safety",
-                "security",
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
-            "identifier": "https://data.transportation.gov/api/views/9ivb-8ae9",
+            "dataQuality": true,
             "description": "This is a list of all Major Safety and Security Events from January of 2014 to the most recently published data within the Federal Transit Administration's major event time series.",
-            "title": "Major Safety Events",
-            "programCode": [
-                "021:061"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26603,51 +26586,85 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9ivb-8ae9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9ivb-8ae9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9ivb-8ae9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/9ivb-8ae9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9ivb-8ae9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9ivb-8ae9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9ivb-8ae9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9ivb-8ae9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9ivb-8ae9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1M",
-            "theme": [
-                "Public Transit"
+            "identifier": "https://data.transportation.gov/api/views/9ivb-8ae9",
+            "issued": "2025-01-07",
+            "keyword": [
+                "safety",
+                "security",
+                "transit"
             ],
+            "landingPage": "https://data.transportation.gov/d/9ivb-8ae9",
             "language": [
                 "en-US"
-            ]
+            ],
+            "modified": "2025-01-23",
+            "programCode": [
+                "021:061"
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
+            "title": "Major Safety Events"
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
-            "landingPage": "https://data.transportation.gov/d/9j9x-3hz2",
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
+            "identifier": "337.4",
+            "isPartOf": "DOT-337",
+            "issued": "2013-11-19",
             "keyword": [
                 "access",
                 "affordability",
@@ -26660,61 +26677,74 @@
                 "transit",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "337.4",
+            "landingPage": "https://data.transportation.gov/d/9j9x-3hz2",
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
-            "landingPage": "https://data.transportation.gov/d/9jif-8qi5",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2020-10-21",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
-            "references": [
-                "https://www.transportation.gov/av/data/wzdx",
-                "http://aztech.org/"
+            "conformsTo": "https://www.transportation.gov/av/data/wzdx",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kate Hartman",
+                "hasEmail": "mailto:kate.hartman@dot.gov"
+            },
+            "describedBy": "https://github.com/usdot-jpo-ode/jpo-wzdx/tree/v3.0",
+            "description": "The WZDx Specification enables infrastructure owners and operators (IOOs) to make harmonized work zone data available for third party use. The intent is to make travel on public roads safer and more efficient through ubiquitous access to data on work zone activity. Specifically, the project aims to get data on work zones into vehicles to help automated driving systems (ADS) and human drivers navigate more safely.\n\nMCDOT leads the effort to aggregate and collect work zone data from the AZTech Regional Partners. A continuously updating archive of the WZDx feed data can be found at <a href=\"http://usdot-its-workzone-publicdata.s3.amazonaws.com/index.html\" target=\"_blank\" rel=\"noopener\">ITS WorkZone Data Sandbox</a>.  The live feed is currently compliant with <a href=\"https://github.com/usdot-jpo-ode/jpo-wzdx/tree/v3.0\" target=\"_blank\" rel=\"noopener\">WZDx specification version 3.0</a>.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/api/views/9jif-8qi5/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.transportation.gov/api/views/9jif-8qi5/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.transportation.gov/api/views/9jif-8qi5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.transportation.gov/api/views/9jif-8qi5/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.transportation.gov/api/views/9jif-8qi5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.transportation.gov/api/views/9jif-8qi5/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.transportation.gov/api/views/9jif-8qi5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
             ],
+            "identifier": "https://data.transportation.gov/api/views/9jif-8qi5",
+            "issued": "2020-10-21",
             "keyword": [
                 "arizona",
                 "arizona department of transportation (adot)",
@@ -26746,69 +26776,71 @@
                 "trucking & motorcoaches",
                 "work zone data exchange (wzdx)"
             ],
-            "conformsTo": "https://www.transportation.gov/av/data/wzdx",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/9jif-8qi5",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
+            "modified": "2024-11-07",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Department of Transportation"
             },
-            "identifier": "https://data.transportation.gov/api/views/9jif-8qi5",
-            "description": "The WZDx Specification enables infrastructure owners and operators (IOOs) to make harmonized work zone data available for third party use. The intent is to make travel on public roads safer and more efficient through ubiquitous access to data on work zone activity. Specifically, the project aims to get data on work zones into vehicles to help automated driving systems (ADS) and human drivers navigate more safely.\n\nMCDOT leads the effort to aggregate and collect work zone data from the AZTech Regional Partners. A continuously updating archive of the WZDx feed data can be found at <a href=\"http://usdot-its-workzone-publicdata.s3.amazonaws.com/index.html\" target=\"_blank\" rel=\"noopener\">ITS WorkZone Data Sandbox</a>.  The live feed is currently compliant with <a href=\"https://github.com/usdot-jpo-ode/jpo-wzdx/tree/v3.0\" target=\"_blank\" rel=\"noopener\">WZDx specification version 3.0</a>.",
-            "title": "Maricopa County Regional Work Zone Data Exchange (WZDx) v3.0 Feed Sample",
-            "programCode": [
-                "021:013"
+            "references": [
+                "https://www.transportation.gov/av/data/wzdx",
+                "http://aztech.org/"
             ],
+            "spatial": "Maricopa County, AZ",
+            "theme": [
+                "Roadways and Bridges"
+            ],
+            "title": "Maricopa County Regional Work Zone Data Exchange (WZDx) v3.0 Feed Sample"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "021:15"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kate Hartman",
+                "hasEmail": "mailto:kate.hartman@dot.gov"
+            },
+            "description": "WFCW-2 Stopped Vehicle Message Prioritization Rep 2",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/api/views/9jif-8qi5/rows.csv?accessType=DOWNLOAD",
+                    "downloadURL": "https://data.transportation.gov/api/views/9k38-2n3v/rows.csv?accessType=DOWNLOAD",
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9jif-8qi5/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.transportation.gov/api/views/9jif-8qi5/columns.rdf",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.transportation.gov/api/views/9k38-2n3v/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9k38-2n3v/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/9jif-8qi5/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.transportation.gov/api/views/9jif-8qi5/columns.json",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.transportation.gov/api/views/9k38-2n3v/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9k38-2n3v/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9jif-8qi5/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.transportation.gov/api/views/9jif-8qi5/columns.xml",
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.transportation.gov/api/views/9k38-2n3v/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9k38-2n3v/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Maricopa County, AZ",
-            "describedBy": "https://github.com/usdot-jpo-ode/jpo-wzdx/tree/v3.0",
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
-            "theme": [
-                "Roadways and Bridges"
-            ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/9k38-2n3v",
-            "bureauCode": [
-                "021:15"
-            ],
+            "identifier": "https://data.transportation.gov/api/views/9k38-2n3v",
             "issued": "2024-09-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
             "keyword": [
                 "connected equipment",
                 "connected vehicle",
@@ -26826,116 +26858,69 @@
                 "vehicle to infrastructure",
                 "vehicle to vehicle"
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
-            "identifier": "https://data.transportation.gov/api/views/9k38-2n3v",
-            "description": "WFCW-2 Stopped Vehicle Message Prioritization Rep 2",
-            "title": "LTE-V2X Wyoming Connected Vehicle Pilot test ID WFCW-2 Rep 2",
+            "landingPage": "https://data.transportation.gov/d/9k38-2n3v",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-20",
             "programCode": [
                 "021:042"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/api/views/9k38-2n3v/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9k38-2n3v/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.transportation.gov/api/views/9k38-2n3v/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/9k38-2n3v/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.transportation.gov/api/views/9k38-2n3v/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9k38-2n3v/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.transportation.gov/api/views/9k38-2n3v/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
             "spatial": "Wyoming",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "theme": [
                 "Automobiles"
-            ]
+            ],
+            "title": "LTE-V2X Wyoming Connected Vehicle Pilot test ID WFCW-2 Rep 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/9kj8-x76q",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "National Highway Construction Cost Index",
+            "identifier": "https://data.transportation.gov/api/views/9kj8-x76q",
             "issued": "2020-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-28",
             "keyword": [
                 "construction costs",
                 "highways",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/9kj8-x76q",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-28",
+            "phone": "202-366-DATA(3282)",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/9kj8-x76q",
-            "description": "National Highway Construction Cost Index",
-            "title": "Transportation Economic Trends: Value of Transportation - Construction Cost",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Transportation Economic Trends: Value of Transportation - Construction Cost"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/9m5y-imtw",
             "bureauCode": [
                 "021:17"
             ],
-            "issued": "2023-12-08",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
-            "keyword": [
-                "insurance",
-                "motor carrier",
-                "insurance rejection"
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
-            "identifier": "https://data.transportation.gov/api/views/9m5y-imtw",
             "description": "Information on insurance forms that were rejected by FMCSA. The dataset contains information on the insurance policy associated with the form, along with the date that the form was rejected and the reason for rejection (e.g., \u201cPolicy is already cancelled\u201d). The dataset contains the DOT number and docket number of the carrier/broker/freight forwarder associated with the policy.  See dataset attachment \"FMCSA Dataset Description and Data Definitions - Select Datasets\" for more information.",
-            "title": "Rejected - All With History",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26943,39 +26928,40 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/9m5y-imtw",
+            "issued": "2023-12-08",
+            "keyword": [
+                "insurance",
+                "motor carrier",
+                "insurance rejection"
+            ],
+            "landingPage": "https://data.transportation.gov/d/9m5y-imtw",
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
-            "landingPage": "https://data.transportation.gov/d/9mw4-x3tu",
             "bureauCode": [
                 "021:17"
             ],
-            "issued": "2024-02-02",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
-            "keyword": [
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
-            "identifier": "https://data.transportation.gov/api/views/9mw4-x3tu",
             "description": "*Dataset*  Records showing the history of each authority granted to a carrier/broker/freight forwarder, along with the dates of the original authority action (e.g., \u201cgranted\u201d) and the final authority action (e.g., \u201crevoked\u201d). The dataset contains the DOT number and docket number of the entity that holds or held the authority. As there can be multiple authorities for a single entity, there may be multiple records for an entity. See dataset attachment \"FMCSA Dataset Description and Data Definitions - Select Datasets\" for more information.",
-            "title": "AuthHist - All With History",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26983,67 +26969,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9mw4-x3tu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9mw4-x3tu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9mw4-x3tu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/9mw4-x3tu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9mw4-x3tu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9mw4-x3tu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9mw4-x3tu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9mw4-x3tu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9mw4-x3tu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/9mw4-x3tu",
+            "issued": "2024-02-02",
+            "keyword": [
+                "motor carrier",
+                "operating authority"
+            ],
+            "landingPage": "https://data.transportation.gov/d/9mw4-x3tu",
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
+            "title": "AuthHist - All With History"
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
-            "identifier": "https://data.transportation.gov/api/views/9nnb-g2yz",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 1994",
-            "title": "Historic HPMS Data (Sample) - 1994",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27051,54 +27031,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9nnb-g2yz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9nnb-g2yz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9nnb-g2yz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/9nnb-g2yz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9nnb-g2yz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9nnb-g2yz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9nnb-g2yz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9nnb-g2yz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9nnb-g2yz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/9nnb-g2yz",
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
+            "title": "Historic HPMS Data (Sample) - 1994"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/9nnx-7iix",
-            "issued": "2023-11-08",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/9nnx-7iix",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "STRACNET",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27106,73 +27096,88 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9nnx-7iix/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9nnx-7iix/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9nnx-7iix/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/9nnx-7iix/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9nnx-7iix/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9nnx-7iix/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9nnx-7iix/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9nnx-7iix/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9nnx-7iix/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/9nnx-7iix",
+            "issued": "2023-11-08",
+            "landingPage": "https://data.transportation.gov/d/9nnx-7iix",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "STRACNET"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/9q4x-3dwy",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2024-09-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
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
-            "identifier": "https://data.transportation.gov/api/views/9q4x-3dwy",
             "description": "Domestic and international freight and mail by year and carrier.",
-            "title": "Freight",
+            "identifier": "https://data.transportation.gov/api/views/9q4x-3dwy",
+            "issued": "2024-09-18",
+            "keyword": [
+                "aff",
+                "aviation facts & figures"
+            ],
+            "landingPage": "https://data.transportation.gov/d/9q4x-3dwy",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-20",
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
+            "title": "Freight"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/9qih-je6q",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRA Safety Data Team",
+                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This is the landing page for crossing incident data from Form 6180.57 Highway-Rail  Incidents, with crossing inventory data from Form 6180.71 USDOT Crossing Inventory.",
+            "identifier": "https://data.transportation.gov/api/views/9qih-je6q",
             "issued": "2024-09-11",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "crossing inventory",
                 "grade crossing incident",
@@ -27180,44 +27185,54 @@
                 "quiet zone",
                 "train horn"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRA Safety Data Team",
-                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/9qih-je6q",
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
-            "identifier": "https://data.transportation.gov/api/views/9qih-je6q",
-            "description": "This is the landing page for crossing incident data from Form 6180.57 Highway-Rail  Incidents, with crossing inventory data from Form 6180.71 USDOT Crossing Inventory.",
-            "title": "Quiet Zone Reports - Landing Page",
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
+            "title": "Quiet Zone Reports - Landing Page"
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
-            "landingPage": "https://data.transportation.gov/d/9riq-dhaf",
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
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/pubs/MonthlyData/S&STimeSeries-July2015-MajorOnly-11022015.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Safety & Security Major-Only Time Series Data"
+                }
             ],
+            "identifier": "22.4",
+            "isPartOf": "DOT-22",
+            "issued": "2002-01-01",
             "keyword": [
                 "bicyclist",
                 "collision",
@@ -27236,104 +27251,70 @@
                 "transit",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John D. Giorgis",
-                "hasEmail": "mailto:john.giorgis@dot.gov"
-            },
-            "identifier": "22.4",
+            "landingPage": "https://data.transportation.gov/d/9riq-dhaf",
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
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/pubs/MonthlyData/S&STimeSeries-July2015-MajorOnly-11022015.xls",
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
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/9rky-htmr",
-            "issued": "2020-08-27",
             "@type": "dcat:Dataset",
-            "modified": "2021-07-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/9rky-htmr",
+            "issued": "2020-08-27",
+            "landingPage": "https://data.transportation.gov/d/9rky-htmr",
+            "modified": "2021-07-08",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
-            "title": "Roadway Sections",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "Roadway Sections"
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
-            "landingPage": "https://data.transportation.gov/d/9ruv-tyis",
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
-            "identifier": "717.2",
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
@@ -27342,33 +27323,67 @@
                     "title": "PlanWorks: Better Planning. Better Projects"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "717.2",
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
+            "landingPage": "https://data.transportation.gov/d/9ruv-tyis",
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
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/9sas-ups5",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/06jantvt/jan06tvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "January 2006"
+                }
             ],
+            "identifier": "18.104",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -27378,60 +27393,60 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.104",
+            "landingPage": "https://data.transportation.gov/d/9sas-ups5",
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
-            "title": "Monthly Traffic Volume Trends - January 2006",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/06jantvt/jan06tvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "January 2006"
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
+            "title": "Monthly Traffic Volume Trends - January 2006"
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
-            "landingPage": "https://data.transportation.gov/d/9t6s-gd2g",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/02dectvt/tvtdec02.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "December 2002"
+                }
             ],
+            "identifier": "18.141",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -27441,76 +27456,42 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.141",
+            "landingPage": "https://data.transportation.gov/d/9t6s-gd2g",
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
-            "title": "Monthly Traffic Volume Trends - December 2002",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/02dectvt/tvtdec02.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "December 2002"
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
+            "title": "Monthly Traffic Volume Trends - December 2002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/9tn7-rkk2",
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
-            "identifier": "https://data.transportation.gov/api/views/9tn7-rkk2",
             "description": "Operating revenues by air carrier.",
-            "title": "AFF - P12 Operating Revenues by Carrier",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27518,46 +27499,80 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9tn7-rkk2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9tn7-rkk2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9tn7-rkk2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/9tn7-rkk2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9tn7-rkk2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9tn7-rkk2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9tn7-rkk2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9tn7-rkk2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9tn7-rkk2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/9tn7-rkk2",
+            "issued": "2024-10-02",
+            "keyword": [
+                "aff",
+                "air carriers",
+                "aviation facts & figures",
+                "transportation finance"
+            ],
+            "landingPage": "https://data.transportation.gov/d/9tn7-rkk2",
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
+            "title": "AFF - P12 Operating Revenues by Carrier"
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
-            "landingPage": "https://data.transportation.gov/d/9u6u-4p67",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12jultvt/12jultvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "July 2012"
+                }
             ],
+            "identifier": "18.40",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -27567,82 +27582,42 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.40",
+            "landingPage": "https://data.transportation.gov/d/9u6u-4p67",
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
-            "title": "Monthly Traffic Volume Trends - July 2012",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12jultvt/12jultvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "July 2012"
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
+            "title": "Monthly Traffic Volume Trends - July 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/9uas-hf8b",
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
-            "identifier": "https://data.transportation.gov/api/views/9uas-hf8b",
             "description": "The main dataset is a 304 MB file of trajectory data (I90_94_stationary_final.csv) that contains position, speed, and acceleration data for small and large automated (L2) vehicles and non-automated vehicles on a highway in an urban environment. Supporting files include aerial reference images for six distinct data collection \u201cRuns\u201d (I90_94_Stationary_Run_X_ref_image.png, where X equals 1, 2, 3, 4, 5, and 6). Associated centerline files are also provided for each \u201cRun\u201d (I-90-stationary-Run_X-geometry-with-ramps.csv). In each centerline file, x and y coordinates (in meters) marking each lane centerline are provided. The origin point of the reference image is located at the top left corner. Additionally, in each centerline file, an indicator variable is used for each lane to define the following types of road sections: 0=no ramp, 1=on-ramps, 2=off-ramps, and 3=weaving segments. The number attached to each column header is the numerical ID assigned for the specific lane (see \u201cTGSIM \u2013 Centerline Data Dictionary \u2013 I90_94Stationary.csv\u201d for more details). The dataset defines six northbound lanes using these centerline files. Twelve different numerical IDs are used to define the six northbound lanes (1, 2, 3, 4, 5, 6, 10, 11, 12, 13, 14, and 15) depending on the run. Images that map the lanes of interest to the numerical lane IDs referenced in the trajectory dataset are stored in the folder titled \u201cAnnotation on Regions.zip\u201d. Lane IDs are provided in the reference images in red text for each data collection run (I90_94_Stationary_Run_X_ref_image_annotated.jpg, where X equals 1, 2, 3, 4, 5, and 6). \n\nThis dataset was collected as part of the Third Generation Simulation Data (TGSIM): A Closer Look at the Impacts of Automated Driving Systems on Human Behavior project. During the project, six trajectory datasets capable of characterizing human-automated vehicle interactions under a diverse set of scenarios in highway and city environments were collected and processed. For more information, see the project report found here: https://rosap.ntl.bts.gov/view/dot/74647. This dataset, which is one of the six collected as part of the TGSIM project, contains data collected using the fixed location aerial videography approach with one high-resolution 8K camera mounted on a helicopter hovering over a short segment of I-94 focusing on the merge and diverge points in Chicago, IL. The altitude of the helicopter (approximately 213 meters) enabled the camera to capture 1.3 km of highway driving and a major weaving section in each direction (where I-90 and I-94 diverge in the northbound direction and merge in the southbound direction). The segment has two off-ramps and two on-ramps in the northbound direction. All roads have 88 kph (55 mph) speed limits. The camera captured footage during the evening rush hour (4:00 PM-6:00 PM CT) on a cloudy day. During this period, two SAE Level 2 ADAS-equipped vehicles drove through the segment, entering the northbound direction upstream of the target section, exiting the target section on the right through I-94, and attempting to perform a total of three lane-changing maneuvers (if safe to do so). These vehicles are indicated in the dataset.\n\nAs part of this dataset, the following files were provided:\n<ul><li>I90_94_stationary_final.csv contains the numerical data to be used for analysis that includes vehicle level trajectory data at every 0.1 second. Vehicle type, width, and length are provided with instantaneous location, speed, and acceleration data. All distance measurements (width, length, location) were converted from pixels to meters using the following conversion factor: 1 pixel = 0.3-meter conversion.</li>\n<li>I90_94_Stationary_Run_X_ref_image.png are the aerial reference images that define the geographic region for each run X.</li>\n<li>I-90-stationary-Run_X-geometry-with-ramps.csv contain the coordinates that define the lane centerlines for each Run X. The \"x\" and \"y\" columns represent the horizontal and ve",
-            "title": "Third Generation Simulation Data (TGSIM) I-90/I-94 Stationary Trajectories",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27650,43 +27625,80 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9uas-hf8b/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9uas-hf8b/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9uas-hf8b/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/9uas-hf8b/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9uas-hf8b/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9uas-hf8b/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9uas-hf8b/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9uas-hf8b/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9uas-hf8b/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "I-90/I94 in Chicago, IL; I-294 near Hinsdale, IL; I-395 in Washington DC; George Washington University Campus, Washington DC (Foggy Bottom)",
+            "identifier": "https://data.transportation.gov/api/views/9uas-hf8b",
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
+            "landingPage": "https://data.transportation.gov/d/9uas-hf8b",
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
+            "title": "Third Generation Simulation Data (TGSIM) I-90/I-94 Stationary Trajectories"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/9v5g-t8u8",
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
+            "description": "The purpose of the data set is to provide multi-modal data and contextual information (weather and incidents) that can be used to research and develop applications for the USDOT Dynamic Mobility Applications (DMA) program.\n\nThis legacy dataset was created before data.transportation.gov and is only currently available via the attached file(s). Please contact the dataset owner if there is a need for users to work with this data using the data.transportation.gov analysis features (online viewing, API, graphing, etc.) and the USDOT will consider modifying the dataset to fully integrate in data.transportation.gov.\n\nAdditional related data can be found here: https://data.transportation.gov/Automobiles/Seattle-20-Second-Freeway/ixg2-6cni",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/download/9v5g-t8u8/application/msword",
+                    "mediaType": "application/msword"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/9v5g-t8u8",
             "issued": "2012-05-31",
-            "@type": "dcat:Dataset",
-            "temporal": "2011-05-01/2011-10-31",
-            "modified": "2012-05-31",
             "keyword": [
                 "arterial",
                 "freeway",
@@ -27708,70 +27720,39 @@
                 "washington state department of transportation (wsdot)",
                 "weather"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/9v5g-t8u8",
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
-            "identifier": "https://data.transportation.gov/api/views/9v5g-t8u8",
-            "description": "The purpose of the data set is to provide multi-modal data and contextual information (weather and incidents) that can be used to research and develop applications for the USDOT Dynamic Mobility Applications (DMA) program.\n\nThis legacy dataset was created before data.transportation.gov and is only currently available via the attached file(s). Please contact the dataset owner if there is a need for users to work with this data using the data.transportation.gov analysis features (online viewing, API, graphing, etc.) and the USDOT will consider modifying the dataset to fully integrate in data.transportation.gov.\n\nAdditional related data can be found here: https://data.transportation.gov/Automobiles/Seattle-20-Second-Freeway/ixg2-6cni",
-            "title": "Seattle Freeway Travel Times",
-            "programCode": [
-                "021:013"
+            "spatial": "Seattle, Washington",
+            "temporal": "2011-05-01/2011-10-31",
+            "theme": [
+                "Automobiles"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/download/9v5g-t8u8/application/msword",
-                    "mediaType": "application/msword"
-                }
-            ],
-            "spatial": "Seattle, Washington",
-            "dataQuality": true,
-            "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "irregular",
-            "theme": [
-                "Automobiles"
-            ],
-            "language": [
-                "en-US"
-            ]
-        },
+            "title": "Seattle Freeway Travel Times"
+        },
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
-            "identifier": "https://data.transportation.gov/api/views/9vq4-dn8b",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 2007",
-            "title": "Historic HPMS Data (Universe) - 2007",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27779,63 +27760,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9vq4-dn8b/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9vq4-dn8b/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9vq4-dn8b/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/9vq4-dn8b/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9vq4-dn8b/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9vq4-dn8b/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9vq4-dn8b/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9vq4-dn8b/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9vq4-dn8b/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/9vq4-dn8b",
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
+            "title": "Historic HPMS Data (Universe) - 2007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/9wrh-mnib",
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
-            "identifier": "https://data.transportation.gov/api/views/9wrh-mnib",
+            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
             "description": "State DOT will provide Local Vehicle-Miles-Traveled (VMT) summarized by FHWA Adjusted Urban Area.",
-            "title": "Urban Summaries 2018",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27843,48 +27828,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9wrh-mnib/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9wrh-mnib/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9wrh-mnib/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/9wrh-mnib/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9wrh-mnib/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9wrh-mnib/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9wrh-mnib/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9wrh-mnib/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9wrh-mnib/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "USA",
-            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
+            "identifier": "https://data.transportation.gov/api/views/9wrh-mnib",
+            "issued": "2020-11-10",
+            "landingPage": "https://data.transportation.gov/d/9wrh-mnib",
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
+            "title": "Urban Summaries 2018"
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
-            "landingPage": "https://data.transportation.gov/d/9wtw-ztm4",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/07augtvt/07augtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "August 2007"
+                }
             ],
+            "identifier": "18.85",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -27894,60 +27909,60 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.85",
+            "landingPage": "https://data.transportation.gov/d/9wtw-ztm4",
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
-            "title": "Monthly Traffic Volume Trends - August 2007",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/07augtvt/07augtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "August 2007"
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
+            "title": "Monthly Traffic Volume Trends - August 2007"
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
-            "landingPage": "https://data.transportation.gov/d/9wwz-dc4j",
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
+                    "downloadURL": "http://www.nhtsa.gov/DOT/NHTSA/Traffic%20Injury%20Control/Articles/2007MVOSS/2007MVOSS_SPSS_VersionB.sav",
+                    "mediaType": "text/plain",
+                    "title": "Child Restraint Use (v2) (SPSS)"
+                }
             ],
+            "identifier": "408.3",
+            "isPartOf": "DOT-408",
+            "issued": "2008-08-31",
             "keyword": [
                 "air bag",
                 "child safety",
@@ -27958,59 +27973,59 @@
                 "protection",
                 "seat belt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "408.3",
+            "landingPage": "https://data.transportation.gov/d/9wwz-dc4j",
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
-            "title": "Motor Vehicle Occupant Safety Survey 2007 (MVOSS) - Child Restraint Use (v2) (SPSS)",
-            "isPartOf": "DOT-408",
-            "agencyProgramURL": "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/National+Telephone+Surveys",
-            "programCode": [
-                "021:032"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.nhtsa.gov/DOT/NHTSA/Traffic%20Injury%20Control/Articles/2007MVOSS/2007MVOSS_SPSS_VersionB.sav",
-                    "mediaType": "text/plain",
-                    "title": "Child Restraint Use (v2) (SPSS)"
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
+            "title": "Motor Vehicle Occupant Safety Survey 2007 (MVOSS) - Child Restraint Use (v2) (SPSS)"
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
-            "landingPage": "https://data.transportation.gov/d/9xg6-c3af",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/08jantvt/08jantvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "January 2008"
+                }
             ],
+            "identifier": "18.80",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -28020,55 +28035,45 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.80",
+            "landingPage": "https://data.transportation.gov/d/9xg6-c3af",
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
-            "title": "Monthly Traffic Volume Trends - January 2008",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/08jantvt/08jantvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "January 2008"
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
+            "title": "Monthly Traffic Volume Trends - January 2008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/9xju-xwze",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This report contains a map of highway-rail grade crossing incidents, as well as a data table for incidents, fatalities and injuries, broken out by public and private crossings.",
+            "identifier": "https://data.transportation.gov/api/views/9xju-xwze",
             "issued": "2023-08-04",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "crossing",
                 "fatalities",
@@ -28078,54 +28083,35 @@
                 "injuries",
                 "map"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/9xju-xwze",
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
-            "identifier": "https://data.transportation.gov/api/views/9xju-xwze",
-            "description": "This report contains a map of highway-rail grade crossing incidents, as well as a data table for incidents, fatalities and injuries, broken out by public and private crossings.",
-            "title": "Highway-Rail Incidents Map (5.10)",
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
+            "title": "Highway-Rail Incidents Map (5.10)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/9yj4-fiiz",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
-            "keyword": [
-                "transit facility ownership",
-                "transit facility size"
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
-            "identifier": "https://data.transportation.gov/api/views/9yj4-fiiz",
             "description": "This dataset details maintenance facility capacities and counts for each applicable agency reporting to the National Transit Database in the 2022 and 2023 report years.\n\nPlease note that because Rural Reporters are not required to report facility size counts, for these reporters null values appear under facility size columns, yet non-zero values may appear under Total Facilities.\n\nNTD Data Tables organize and summarize data from the 2022 and 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. This dataset is based on the 2022 and 2023 Transit Facilities database files.\n\nIn years 2015-2021, you can find this data in the \"Maintenance Facilities\" data table on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.\n\nIf you have any other questions about this table, please contact the NTD Help Desk at NTDHelp@dot.gov.",
-            "title": "2022 - 2023 NTD Annual Data - Maintenance Facilities",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28133,78 +28119,107 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9yj4-fiiz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9yj4-fiiz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9yj4-fiiz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/9yj4-fiiz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9yj4-fiiz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9yj4-fiiz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/9yj4-fiiz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/9yj4-fiiz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/9yj4-fiiz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/9yj4-fiiz",
+            "issued": "2024-09-10",
+            "keyword": [
+                "transit facility ownership",
+                "transit facility size"
+            ],
+            "landingPage": "https://data.transportation.gov/d/9yj4-fiiz",
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
+            "title": "2022 - 2023 NTD Annual Data - Maintenance Facilities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:36"
             ],
-            "landingPage": "https://data.transportation.gov/d/9yqm-gpku",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NTD Program Support",
+                "hasEmail": "mailto:NTDHelp@dot.gov"
+            },
+            "description": "A national summary of transit Vehicles and Energy Consumption based on data reported by transit agencies to the National Transit Database (NTD) in Report Year 2022. Only Full Reporters report energy consumption, while other reporter types report vehicles.\r\n\r\n\r\nNTD Data Tables organize and summarize data from the 2022 National Transit Database in a manner that is more useful for quick reference and summary analysis. This dataset is based on the 2022 Energy Consumption database file and Revenue Vehicles Inventory database file. In years 2014-2021 the data tables that underlie these data were \"Vehicles\" and \"Fuel and Energy\".",
+            "identifier": "https://data.transportation.gov/api/views/9yqm-gpku",
             "issued": "2023-09-11",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-10",
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
+            "landingPage": "https://data.transportation.gov/d/9yqm-gpku",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-09-10",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Transit Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/9yqm-gpku",
-            "description": "A national summary of transit Vehicles and Energy Consumption based on data reported by transit agencies to the National Transit Database (NTD) in Report Year 2022. Only Full Reporters report energy consumption, while other reporter types report vehicles.\r\n\r\n\r\nNTD Data Tables organize and summarize data from the 2022 National Transit Database in a manner that is more useful for quick reference and summary analysis. This dataset is based on the 2022 Energy Consumption database file and Revenue Vehicles Inventory database file. In years 2014-2021 the data tables that underlie these data were \"Vehicles\" and \"Fuel and Energy\".",
-            "title": "2022 NTD Annual Data Summary - Vehicles and Energy Consumption",
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "2022 NTD Annual Data Summary - Vehicles and Energy Consumption"
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
-            "landingPage": "https://data.transportation.gov/d/9zjn-ju8h",
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
+                    "mediaType": "application/json",
+                    "title": "Vehicle API JSON"
+                }
             ],
+            "identifier": "65.5",
+            "isPartOf": "DOT-65",
+            "issued": "2015-10-05",
             "keyword": [
                 "49",
                 "551",
@@ -28241,86 +28256,50 @@
                 "vin",
                 "vpic"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "65.5",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "The NHTSA Product Information Catalog and Vehicle Listing (vPIC) is a consolidated platform that presents data collected within the manufacturer reported data from CFR 49 Parts 551 - 574 for use in a variety of modern tools. NHTSA's vPIC platform is intended to serve as a centralized source for basic Vehicle Identification Number (VIN) decoding, Manufacturer Information Database (MID), Manufacturer Equipment Plant Identification and associated data. vPIC is intended to support the Open Data and Transparency initiatives of the agency by allowing the data to be freely used by the public without the burden of manual retrieval from a library of electronic documents (PDFs). While these documents will still be available online for viewing within the Manufacturer Information Database (MID) module of vPIC one can view and use the actual data through the VIN Decoder and Application Programming Interface (API) modules.",
-            "title": "NHTSA Product Information Catalog and Vehicle Listing (vPIC) - Vehicle API JSON",
-            "isPartOf": "DOT-65",
-            "agencyProgramURL": "http://vpic.nhtsa.dot.gov/",
+            "landingPage": "https://data.transportation.gov/d/9zjn-ju8h",
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
-                    "mediaType": "application/json",
-                    "downloadURL": "http://vpic.nhtsa.dot.gov/api/",
-                    "description": "APIs for use by developers, programmers or researchers interested in obtaining raw Vehicle or Manufacturer data from vPIC.",
-                    "@type": "dcat:Distribution",
-                    "title": "Vehicle API JSON"
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
+            "title": "NHTSA Product Information Catalog and Vehicle Listing (vPIC) - Vehicle API JSON"
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
-            "landingPage": "https://data.transportation.gov/d/a25h-ft62",
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
-            "identifier": "524.23",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
             "description": "STATE DATA REPORTING SYSTEMS. Annual reports on the Fatality Analysis Reporting System (FARS) which is data regarding fatalities that is collected by a FARS analyst from each State and provided to NHTSA.",
-            "title": "GES Reports - 1990",
-            "isPartOf": "DOT-524",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28329,32 +28308,71 @@
                     "title": "1990"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
-            "dataQuality": true,
+            "identifier": "524.23",
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
+            "landingPage": "https://data.transportation.gov/d/a25h-ft62",
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
+            "title": "GES Reports - 1990"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/a4d7-c6wm",
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
+                    "description": "2012 Arizona HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/arizona2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Arizona"
+                }
+            ],
+            "identifier": "678.56",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -28368,57 +28386,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.56",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Arizona",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/a4d7-c6wm",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/arizona2012.zip",
-                    "description": "2012 Arizona HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Arizona"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Arizona"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/a4dg-79g2",
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
+                    "description": "2012 Alaska HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/alaska2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Alaska"
+                }
+            ],
+            "identifier": "678.55",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -28432,113 +28450,78 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.55",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Alaska",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/a4dg-79g2",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/alaska2012.zip",
-                    "description": "2012 Alaska HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Alaska"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Alaska"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/a54a-9hsb",
-            "issued": "2021-03-18",
             "@type": "dcat:Dataset",
-            "modified": "2022-11-29",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Chambers",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/a54a-9hsb",
+            "issued": "2021-03-18",
+            "landingPage": "https://data.transportation.gov/d/a54a-9hsb",
+            "modified": "2022-11-29",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Port Capacity Metrics"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/a5ae-2bbf",
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
             "identifier": "https://data.transportation.gov/api/views/a5ae-2bbf",
+            "issued": "2021-01-21",
+            "landingPage": "https://data.transportation.gov/d/a5ae-2bbf",
+            "modified": "2021-01-21",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "County Transportation Profiles"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/a5sc-aujx",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-09-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-01",
-            "keyword": [
-                "commodity",
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
-            "identifier": "https://data.transportation.gov/api/views/a5sc-aujx",
             "description": "Source: U.S. Department of Transportation, Bureau of Transportation Statistics, based upon U.S. Department of Commerce, U.S. Census Bureau, Foreign Trade Division, USA Trade Online \"HS Port-level Data\", available at https://usatrade.census.gov/ as of Sept 2024.",
-            "title": "Top 10 Containerized Export Commodities by Value and Coast 2023",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28546,50 +28529,83 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/a5sc-aujx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/a5sc-aujx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/a5sc-aujx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/a5sc-aujx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/a5sc-aujx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/a5sc-aujx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/a5sc-aujx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/a5sc-aujx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/a5sc-aujx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/a5sc-aujx",
+            "issued": "2024-09-30",
+            "keyword": [
+                "commodity",
+                "containers",
+                "ports"
+            ],
+            "landingPage": "https://data.transportation.gov/d/a5sc-aujx",
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
+            "title": "Top 10 Containerized Export Commodities by Value and Coast 2023"
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
-            "landingPage": "https://data.transportation.gov/d/a5zk-66zv",
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
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/tenyr1a.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Ten Year Accident/Incident Overview by Railroad"
+                }
             ],
+            "identifier": "214.6",
+            "isPartOf": "DOT-214",
+            "issued": "2010-09-29",
             "keyword": [
                 "accident",
                 "casualty",
@@ -28602,61 +28618,59 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "214.6",
+            "landingPage": "https://data.transportation.gov/d/a5zk-66zv",
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
-            "title": "Highway Rail Accidents - Ten Year Accident/Incident Overview by Railroad",
-            "isPartOf": "DOT-214",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:000"
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
+            "title": "Highway Rail Accidents - Ten Year Accident/Incident Overview by Railroad"
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
-            "landingPage": "https://data.transportation.gov/d/a6dq-6s8m",
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
+            "identifier": "DOT-22",
+            "issued": "2002-01-01",
             "keyword": [
                 "bicyclist",
                 "collision",
@@ -28675,59 +28689,60 @@
                 "transit",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NTD Program Support",
-                "hasEmail": "mailto:NTDHelp@dot.gov"
-            },
-            "identifier": "DOT-22",
+            "landingPage": "https://data.transportation.gov/d/a6dq-6s8m",
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
-            "title": "NTD Safety & Security Summary Data Set",
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
-            "analysisUnit": "transit agency, mode, type of service",
-            "categoryDesignation": "Research",
-            "phone": "202-366-5430",
-            "language": [
-                "en-US"
-            ]
+            "title": "NTD Safety & Security Summary Data Set"
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
-            "landingPage": "https://data.transportation.gov/d/a763-yc4d",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/08febtvt/08febtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "February 2008"
+                }
             ],
+            "identifier": "18.79",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -28737,87 +28752,44 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.79",
+            "landingPage": "https://data.transportation.gov/d/a763-yc4d",
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
-            "title": "Monthly Traffic Volume Trends - February 2008",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/08febtvt/08febtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "February 2008"
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
+            "title": "Monthly Traffic Volume Trends - February 2008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/a79b-e3wn",
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
-                "incident data",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "pasadena",
-                "performance measurement system (pems)",
-                "sr 134",
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
-            "identifier": "https://data.transportation.gov/api/views/a79b-e3wn",
+            "dataQuality": true,
             "description": "The data in this data environment was collected from the Pasadena, California testbed, namely I-210, SR 134, and nearby arterials. The source of these data is from the Caltrans \u2013 Performance Measurement System (PeMS). Speed data from this dataset were used to derive the freeway travel time. There are three separate text files with one for each operational condition.",
-            "title": "AMS Pasadena Main Data",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28825,71 +28797,80 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/a79b-e3wn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/a79b-e3wn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/a79b-e3wn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/a79b-e3wn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/a79b-e3wn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/a79b-e3wn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/a79b-e3wn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/a79b-e3wn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/a79b-e3wn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "I-210, SR 134, Pasadena, California, Los Angeles County",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/a79b-e3wn",
+            "issued": "2017-09-20",
+            "keyword": [
+                "ams pasadena testbed",
+                "analysis modeling and simulation (ams) testbed development",
+                "arterial",
+                "california",
+                "cluster analysis",
+                "freeway",
+                "i-210",
+                "incident data",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "pasadena",
+                "performance measurement system (pems)",
+                "sr 134",
+                "travel time"
+            ],
+            "landingPage": "https://data.transportation.gov/d/a79b-e3wn",
             "license": "http://creativecommons.org/licenses/by-nc-sa/3.0/legalcode",
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
                 "Transportation"
-            ]
+            ],
+            "title": "AMS Pasadena Main Data"
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
-            "landingPage": "https://data.transportation.gov/d/a7md-2xav",
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
-            "identifier": "692.22",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - 2012 Fatal Crashes",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "primaryITInvestmentUII": "021-845083703",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28898,68 +28879,52 @@
                     "title": "2012 Fatal Crashes"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.22",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/a7md-2xav",
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
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - 2012 Fatal Crashes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/a7qq-9vfe",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2014-10-28",
-            "@type": "dcat:Dataset",
-            "temporal": "2012-10-01/2013-04-30",
-            "modified": "2014-10-28",
-            "keyword": [
-                "aftermarket safety device (asd)",
-                "ann arbor",
-                "arterial",
-                "basic safety message (bsm)",
-                "connected equipment",
-                "connected vehicle message",
-                "field test",
-                "freeway",
-                "integrated safety device (isd)",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "michigan",
-                "national highway traffic safety administration (nhtsa)",
-                "public safety",
-                "roadside equipment (rse)",
-                "safety pilot model deployment (spmd)",
-                "signal phase and timing (spat)",
-                "transit safety retrofit package (trp)",
-                "traveler information message (tim)",
-                "vehicle awareness device (vad)",
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
-            "identifier": "https://data.transportation.gov/api/views/a7qq-9vfe",
+            "dataQuality": true,
             "description": "This data were collected during the Safety Pilot Model Deployment (SPMD). The data sets that these entities will provide include basic safety messages (BSM), vehicle trajectories, and various driver-vehicle interaction data, as well as contextual data that describes the circumstances under which the Model Deployment data was collected. Large portion of the data contained in this environment is obtained from on board vehicle devices and roadside units.\r\n\r\nThis legacy dataset was created before data.transportation.gov and is only currently available via the attached file(s). Please contact the dataset owner if there is a need for users to work with this data using the data.transportation.gov analysis features (online viewing, API, graphing, etc.) and the USDOT will consider modifying the dataset to fully integrate in data.transportation.gov.",
-            "title": "Safety Pilot Model Deployment Data",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29220,29 +29185,75 @@
                     "title": "WiperStatusFrontEvents"
                 }
             ],
-            "spatial": "Ann Arbor, Michigan",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/a7qq-9vfe",
+            "issued": "2014-10-28",
+            "keyword": [
+                "aftermarket safety device (asd)",
+                "ann arbor",
+                "arterial",
+                "basic safety message (bsm)",
+                "connected equipment",
+                "connected vehicle message",
+                "field test",
+                "freeway",
+                "integrated safety device (isd)",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "michigan",
+                "national highway traffic safety administration (nhtsa)",
+                "public safety",
+                "roadside equipment (rse)",
+                "safety pilot model deployment (spmd)",
+                "signal phase and timing (spat)",
+                "transit safety retrofit package (trp)",
+                "traveler information message (tim)",
+                "vehicle awareness device (vad)",
+                "weather"
+            ],
+            "landingPage": "https://data.transportation.gov/d/a7qq-9vfe",
+            "language": [
+                "en-US"
+            ],
             "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "irregular",
+            "modified": "2014-10-28",
+            "programCode": [
+                "021:013"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
+            "spatial": "Ann Arbor, Michigan",
+            "temporal": "2012-10-01/2013-04-30",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Safety Pilot Model Deployment Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.21949/1503777",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2015-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2016-12-24",
-            "references": [
-                "https://rosap.ntl.bts.gov/view/dot/3604"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Transportation Library Data Curator",
+                "hasEmail": "mailto:ntldatacurator@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The goal of the SHRP 2 Project L33 Validation of Urban Freeway Models was to assess and enhance the predictive travel time reliability models developed in the SHRP 2 Project L03, Analytic Procedures for Determining the Impacts of Reliability Mitigation Strategies. SHRP 2 Project L03, which concluded in 2010, developed two categories of reliability models to be used for the estimation or prediction of travel time reliability within planning, programming, and systems management contexts: data-rich and data-poor models. The objectives of Project L33 were the following: \u2022 The first was to validate the most important models \u2013 the \u201cData Poor\u201d and \u201cData Rich\u201d models with new datasets. \u2022 The second objective was to assess the validation outcomes to recommend potential enhancements. \u2022 The third was to explore enhancements and develop a final set of predictive equations. \u2022 The fourth was to validate the enhanced models. \u2022 The last was to develop a clear set of application guidelines for practitioner use of the project outputs.  The datasets in these 5 zip files are in support of SHRP 2 Report S2-L33-RW-1, Validation of Urban Freeway Models, https://rosap.ntl.bts.gov/view/dot/3604   The 5 zip files contain a total of 60 comma separated value (.csv) files. The compressed zip files total 3.8 GB in size. The files have been uploaded as-is; no further documentation was supplied. These files can be unzipped using any zip compression/decompression software. The files can be read in any simple text editor.  [software requirements]  Note: Data files larger than 1GB each. Direct data download links: L03-01: https://doi.org/10.21949/1500858 L03-02: https://doi.org/10.21949/1500868 L03-03: https://doi.org/10.21949/1500869 L03-04: https://doi.org/10.21949/1500870 L03-05: https://doi.org/10.21949/1500871",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The goal of the SHRP 2 Project L33 Validation of Urban Freeway Models was to assess and enhance the predictive travel time reliability models developed in the SHRP 2 Project L03, Analytic Procedures for Determining the Impacts of Reliability Mitigation Strategies. SHRP 2 Project L03, which concluded in 2010, developed two categories of reliability models to be used for the estimation or prediction of travel time reliability within planning, programming, and systems management contexts: data-rich and data-poor models. The objectives of Project L33 were the following: \u2022 The first was to validate the most important models \u2013 the \u201cData Poor\u201d and \u201cData Rich\u201d models with new datasets. \u2022 The second objective was to assess the validation outcomes to recommend potential enhancements. \u2022 The third was to explore enhancements and develop a final set of predictive equations. \u2022 The fourth was to validate the enhanced models. \u2022 The last was to develop a clear set of application guidelines for practitioner use of the project outputs.  The datasets in these 5 zip files are in support of SHRP 2 Report S2-L33-RW-1, Validation of Urban Freeway Models, https://rosap.ntl.bts.gov/view/dot/3604   The 5 zip files contain a total of 60 comma separated value (.csv) files. The compressed zip files total 3.8 GB in size. The files have been uploaded as-is; no further documentation was supplied. These files can be unzipped using any zip compression/decompression software. The files can be read in any simple text editor.  [software requirements]  Note: Data files larger than 1GB each. Direct data download links: L03-01: https://doi.org/10.21949/1500858 L03-02: https://doi.org/10.21949/1500868 L03-03: https://doi.org/10.21949/1500869 L03-04: https://doi.org/10.21949/1500870 L03-05: https://doi.org/10.21949/1500871",
+                    "downloadURL": "https://doi.org/10.21949/1503777",
+                    "mediaType": "application/zip",
+                    "title": "Validation of Urban Freeway Models [supporting datasets]"
+                }
             ],
+            "identifier": "https://data.transportation.gov/api/views/a8g4-5cgg",
+            "issued": "2015-01-01",
             "keyword": [
                 "freeways",
                 "intelligent transportation systems",
@@ -29255,51 +29266,55 @@
                 "urban highways",
                 "validation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Transportation Library Data Curator",
-                "hasEmail": "mailto:ntldatacurator@dot.gov"
-            },
+            "landingPage": "https://doi.org/10.21949/1503777",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2016-12-24",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/a8g4-5cgg",
-            "description": "The goal of the SHRP 2 Project L33 Validation of Urban Freeway Models was to assess and enhance the predictive travel time reliability models developed in the SHRP 2 Project L03, Analytic Procedures for Determining the Impacts of Reliability Mitigation Strategies. SHRP 2 Project L03, which concluded in 2010, developed two categories of reliability models to be used for the estimation or prediction of travel time reliability within planning, programming, and systems management contexts: data-rich and data-poor models. The objectives of Project L33 were the following: \u2022 The first was to validate the most important models \u2013 the \u201cData Poor\u201d and \u201cData Rich\u201d models with new datasets. \u2022 The second objective was to assess the validation outcomes to recommend potential enhancements. \u2022 The third was to explore enhancements and develop a final set of predictive equations. \u2022 The fourth was to validate the enhanced models. \u2022 The last was to develop a clear set of application guidelines for practitioner use of the project outputs.  The datasets in these 5 zip files are in support of SHRP 2 Report S2-L33-RW-1, Validation of Urban Freeway Models, https://rosap.ntl.bts.gov/view/dot/3604   The 5 zip files contain a total of 60 comma separated value (.csv) files. The compressed zip files total 3.8 GB in size. The files have been uploaded as-is; no further documentation was supplied. These files can be unzipped using any zip compression/decompression software. The files can be read in any simple text editor.  [software requirements]  Note: Data files larger than 1GB each. Direct data download links: L03-01: https://doi.org/10.21949/1500858 L03-02: https://doi.org/10.21949/1500868 L03-03: https://doi.org/10.21949/1500869 L03-04: https://doi.org/10.21949/1500870 L03-05: https://doi.org/10.21949/1500871",
-            "title": "Validation of Urban Freeway Models [supporting datasets]",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://doi.org/10.21949/1503777",
-                    "description": "The goal of the SHRP 2 Project L33 Validation of Urban Freeway Models was to assess and enhance the predictive travel time reliability models developed in the SHRP 2 Project L03, Analytic Procedures for Determining the Impacts of Reliability Mitigation Strategies. SHRP 2 Project L03, which concluded in 2010, developed two categories of reliability models to be used for the estimation or prediction of travel time reliability within planning, programming, and systems management contexts: data-rich and data-poor models. The objectives of Project L33 were the following: \u2022 The first was to validate the most important models \u2013 the \u201cData Poor\u201d and \u201cData Rich\u201d models with new datasets. \u2022 The second objective was to assess the validation outcomes to recommend potential enhancements. \u2022 The third was to explore enhancements and develop a final set of predictive equations. \u2022 The fourth was to validate the enhanced models. \u2022 The last was to develop a clear set of application guidelines for practitioner use of the project outputs.  The datasets in these 5 zip files are in support of SHRP 2 Report S2-L33-RW-1, Validation of Urban Freeway Models, https://rosap.ntl.bts.gov/view/dot/3604   The 5 zip files contain a total of 60 comma separated value (.csv) files. The compressed zip files total 3.8 GB in size. The files have been uploaded as-is; no further documentation was supplied. These files can be unzipped using any zip compression/decompression software. The files can be read in any simple text editor.  [software requirements]  Note: Data files larger than 1GB each. Direct data download links: L03-01: https://doi.org/10.21949/1500858 L03-02: https://doi.org/10.21949/1500868 L03-03: https://doi.org/10.21949/1500869 L03-04: https://doi.org/10.21949/1500870 L03-05: https://doi.org/10.21949/1500871",
-                    "@type": "dcat:Distribution",
-                    "title": "Validation of Urban Freeway Models [supporting datasets]"
-                }
+            "references": [
+                "https://rosap.ntl.bts.gov/view/dot/3604"
             ],
             "spatial": "United States",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "language": [
-                "en-US"
-            ]
+            "title": "Validation of Urban Freeway Models [supporting datasets]"
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
-            "landingPage": "https://data.transportation.gov/d/a8gk-dvsv",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/03aprtvt/tvtapr03.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "April 2003"
+                }
             ],
+            "identifier": "18.137",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -29309,60 +29324,60 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.137",
+            "landingPage": "https://data.transportation.gov/d/a8gk-dvsv",
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
-            "title": "Monthly Traffic Volume Trends - April 2003",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/03aprtvt/tvtapr03.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "April 2003"
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
+            "title": "Monthly Traffic Volume Trends - April 2003"
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
-            "landingPage": "https://data.transportation.gov/d/a9e6-abpz",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/05febtvt/05febtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "February 2005"
+                }
             ],
+            "identifier": "18.115",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -29372,82 +29387,48 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.115",
+            "landingPage": "https://data.transportation.gov/d/a9e6-abpz",
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
-            "title": "Monthly Traffic Volume Trends - February 2005",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/05febtvt/05febtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "February 2005"
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
+            "title": "Monthly Traffic Volume Trends - February 2005"
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
-            "landingPage": "https://data.transportation.gov/d/a9g8-gdb9",
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
-            "identifier": "692.29",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - PM 2.5",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "primaryITInvestmentUII": "021-845083703",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29456,60 +29437,57 @@
                     "title": "PM 2.5"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.29",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/a9g8-gdb9",
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
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - PM 2.5"
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
-            "landingPage": "https://data.transportation.gov/d/aapw-xufn",
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
-            "identifier": "18.62",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - May 2014",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29518,84 +29496,92 @@
                     "title": "May 2014"
                 }
             ],
-            "spatial": "Vehicles by type of functional classified roadway",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
-            "theme": [
-                "Transportation"
+            "identifier": "18.62",
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
+            "landingPage": "https://data.transportation.gov/d/aapw-xufn",
             "language": [
                 "en-US"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/aaty-mapf",
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
+            "title": "Monthly Traffic Volume Trends - May 2014"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRA Safety Data Team",
+                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This is the landing page for Form 6180.71 US DOT Crossing Inventory data.",
+            "identifier": "https://data.transportation.gov/api/views/aaty-mapf",
             "issued": "2024-11-22",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "crossing inventory",
                 "highway-rail",
                 "highway-rail grade crossing"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRA Safety Data Team",
-                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/aaty-mapf",
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
-            "identifier": "https://data.transportation.gov/api/views/aaty-mapf",
-            "description": "This is the landing page for Form 6180.71 US DOT Crossing Inventory data.",
-            "title": "Form 71 Data Downloads",
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
+            "title": "Form 71 Data Downloads"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/aayw-vxb3",
             "bureauCode": [
                 "021:17"
             ],
-            "issued": "2024-04-25",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
-            "keyword": [
-                "accident",
-                "crash"
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
-            "identifier": "https://data.transportation.gov/api/views/aayw-vxb3",
             "description": "The FMCSA Crash File contains data from state police crash reports involving drivers and vehicles of motor carriers operating in the U.S. Each report contains about 80 data elements pertaining to the motor carrier, driver, vehicles, and circumstances of a crash. Due to sensitive and/or privacy restrictions, driver, and hazardous materials data are not included in any crash files released to the public.\n\nThe Crash File may contain multiple records for a crash. Separate reports are entered for each commercial motor vehicle involved in a crash. These multiple reports can be distinguished by the Crash Report Number field.",
-            "title": "Crash File",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29603,49 +29589,79 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/aayw-vxb3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/aayw-vxb3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/aayw-vxb3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/aayw-vxb3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/aayw-vxb3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/aayw-vxb3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/aayw-vxb3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/aayw-vxb3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/aayw-vxb3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/aayw-vxb3",
+            "issued": "2024-04-25",
+            "keyword": [
+                "accident",
+                "crash"
+            ],
+            "landingPage": "https://data.transportation.gov/d/aayw-vxb3",
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
+            "title": "Crash File"
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
-            "landingPage": "https://data.transportation.gov/d/ab6s-pbuv",
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
+                    "downloadURL": "http://www.fra.dot.gov/eLib/Details/L04106",
+                    "mediaType": "text/csv",
+                    "title": "Dispatcher Daily Log"
+                }
             ],
+            "identifier": "283.2",
+            "isPartOf": "DOT-283",
+            "issued": "2008-03-01",
             "keyword": [
                 "alertness",
                 "employee",
@@ -29656,104 +29672,75 @@
                 "sleep",
                 "work"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "283.2",
+            "landingPage": "https://data.transportation.gov/d/ab6s-pbuv",
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
-            "title": "Work Schedules and Sleep Patterns of Railroad Employees - Dispatcher Daily Log",
-            "isPartOf": "DOT-283",
-            "agencyProgramURL": "http://www.fra.dot.gov/Page/P0068",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fra.dot.gov/eLib/Details/L04106",
-                    "mediaType": "text/csv",
-                    "title": "Dispatcher Daily Log"
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
+            "title": "Work Schedules and Sleep Patterns of Railroad Employees - Dispatcher Daily Log"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ab7y-wzpz",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2020-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-12",
-            "keyword": [
-                "transportation capital stock"
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
-            "identifier": "https://data.transportation.gov/api/views/ab7y-wzpz",
             "description": "Transportation capital stock",
-            "title": "Transportation Economic Trends: Value of Transportation - Capital Stock",
+            "identifier": "https://data.transportation.gov/api/views/ab7y-wzpz",
+            "issued": "2020-02-23",
+            "keyword": [
+                "transportation capital stock"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ab7y-wzpz",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-12-12",
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
+            "title": "Transportation Economic Trends: Value of Transportation - Capital Stock"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/abu9-jbyq",
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
-            "identifier": "https://data.transportation.gov/api/views/abu9-jbyq",
             "description": "",
-            "title": "Tanker/Liquid Bulk Vessel Dwell Times at the Top U.S. Ports January 2019 to June 2023",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29761,71 +29748,102 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/abu9-jbyq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/abu9-jbyq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/abu9-jbyq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/abu9-jbyq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/abu9-jbyq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/abu9-jbyq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/abu9-jbyq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/abu9-jbyq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/abu9-jbyq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "https://data.transportation.gov/api/views/abu9-jbyq",
+            "issued": "2024-01-10",
+            "landingPage": "https://data.transportation.gov/d/abu9-jbyq",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-01-10",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Tanker/Liquid Bulk Vessel Dwell Times at the Top U.S. Ports January 2019 to June 2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/aczc-7vu4",
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
-            "identifier": "https://data.transportation.gov/api/views/aczc-7vu4",
             "description": "Personal spending on motor vehicles and parts includes spending on new motor vehicles, used vehicle purchases, and vehicle parts and accessories. The Bureau of Economic Analysis estimates personal consumption expenditures, the primary measure of consumer spending on goods and services in the U.S. economy, for each quarter and releases new statistics every month. Quarterly PCE data are seasonally adjusted at annual rates to remove the effects of normal seasonal variation.",
-            "title": "Motor Vehicles and Parts - Seasonally Adjusted",
+            "identifier": "https://data.transportation.gov/api/views/aczc-7vu4",
+            "issued": "2025-01-02",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/aczc-7vu4",
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
+            "title": "Motor Vehicles and Parts - Seasonally Adjusted"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/adtm-ugqm",
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
+                    "description": "2013 Washington HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/washington2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Washington"
+                }
+            ],
+            "identifier": "678.150",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -29839,64 +29857,36 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.150",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Washington",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/adtm-ugqm",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/washington2013.zip",
-                    "description": "2013 Washington HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Washington"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Washington"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/aeeh-bp8c",
-            "issued": "2023-09-26",
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
-            "identifier": "https://data.transportation.gov/api/views/aeeh-bp8c",
             "description": "",
-            "title": "Highway-Rail Grade Crossing Accident Data (Form 57) - Last 5 years Geocoded",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29904,46 +29894,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/aeeh-bp8c/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/aeeh-bp8c/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/aeeh-bp8c/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/aeeh-bp8c/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/aeeh-bp8c/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/aeeh-bp8c/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/aeeh-bp8c/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/aeeh-bp8c/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/aeeh-bp8c/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/aeeh-bp8c",
+            "issued": "2023-09-26",
+            "landingPage": "https://data.transportation.gov/d/aeeh-bp8c",
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
+            "title": "Highway-Rail Grade Crossing Accident Data (Form 57) - Last 5 years Geocoded"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.phmsa.dot.gov/data-and-statistics/pipeline/gas-distribution-gas-gathering-gas-transmission-hazardous-liquids",
+            "agencyProgramURL": "http://www.phmsa.dot.gov/pipeline",
+            "analysisUnit": "Annual Report information from pipeline operators",
             "bureauCode": [
                 "021:50"
             ],
-            "landingPage": "https://data.transportation.gov/d/aemm-7pyq",
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
+            "description": "The Code of Federal Regulations (49 CFR Parts 191, 195) requires operators of Gas Distribution, Gas Gathering, Gas Transmission, Hazardous Liquids, Liquefied Natural Gas (LNG), and Underground Natural Gas Storage (UNGS) to submit annual reports to PHMSA. Annual reports include information such as total pipeline mileage, facilities, commodities transported, miles by material, and installation dates. These annual reports are widely used by safety researchers, government agencies, industry professionals, and by PHMSA personnel for inspection planning.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Hazardous Liquid Pipeline Systems Annual Report Data from 2010 to Present",
+                    "downloadURL": "http://www.phmsa.dot.gov/staticfiles/PHMSA/DownloadableFiles/Pipeline2data/annual_hazardous_liquid_2010_present.zip",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Annual Hazardous Liquid - 2010 to Present (zip)"
+                }
             ],
+            "identifier": "33.5",
+            "isPartOf": "DOT-33",
+            "issued": "2000-03-15",
             "keyword": [
                 "annual",
                 "distribution",
@@ -29954,59 +29970,61 @@
                 "safety",
                 "transmission"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "PHMSA-Datahub",
-                "hasEmail": "mailto:PHMSAPHPDataandStatistics@dot.gov"
-            },
-            "identifier": "33.5",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Pipeline and Hazardous Materials Safety Administration"
-            },
-            "description": "The Code of Federal Regulations (49 CFR Parts 191, 195) requires operators of Gas Distribution, Gas Gathering, Gas Transmission, Hazardous Liquids, Liquefied Natural Gas (LNG), and Underground Natural Gas Storage (UNGS) to submit annual reports to PHMSA. Annual reports include information such as total pipeline mileage, facilities, commodities transported, miles by material, and installation dates. These annual reports are widely used by safety researchers, government agencies, industry professionals, and by PHMSA personnel for inspection planning.",
-            "title": "Gas Distribution, Gas Gathering, Gas Transmission, Hazardous Liquids, Liquefied Natural Gas (LNG), and Underground Natural Gas Storage (UNGS) Annual Report Data",
-            "isPartOf": "DOT-33",
-            "agencyProgramURL": "http://www.phmsa.dot.gov/pipeline",
+            "landingPage": "https://data.transportation.gov/d/aemm-7pyq",
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
-                    "downloadURL": "http://www.phmsa.dot.gov/staticfiles/PHMSA/DownloadableFiles/Pipeline2data/annual_hazardous_liquid_2010_present.zip",
-                    "description": "Hazardous Liquid Pipeline Systems Annual Report Data from 2010 to Present",
-                    "@type": "dcat:Distribution",
-                    "title": "Annual Hazardous Liquid - 2010 to Present (zip)"
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
-            "agencyDataSeriesURL": "https://www.phmsa.dot.gov/data-and-statistics/pipeline/gas-distribution-gas-gathering-gas-transmission-hazardous-liquids",
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
+            "title": "Gas Distribution, Gas Gathering, Gas Transmission, Hazardous Liquids, Liquefied Natural Gas (LNG), and Underground Natural Gas Storage (UNGS) Annual Report Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/afey-nkpf",
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
+                    "description": "2013 Delaware HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/delaware2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Delaware"
+                }
+            ],
+            "identifier": "678.112",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -30020,77 +30038,40 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.112",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Delaware",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/afey-nkpf",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/delaware2013.zip",
-                    "description": "2013 Delaware HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Delaware"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Delaware"
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
-            "identifier": "https://data.transportation.gov/api/views/affx-yhsw",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 1994",
-            "title": "Historic HPMS Data (Universe) - 1994",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30098,70 +30079,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/affx-yhsw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/affx-yhsw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/affx-yhsw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/affx-yhsw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/affx-yhsw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/affx-yhsw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/affx-yhsw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/affx-yhsw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/affx-yhsw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/affx-yhsw",
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
+            "title": "Historic HPMS Data (Universe) - 1994"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ag7u-9n3t",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2024-09-16",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-20",
-            "keyword": [
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "maryland",
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
-            "identifier": "https://data.transportation.gov/api/views/ag7u-9n3t",
             "description": "Data for Artificial Intelligence: Data-Centric AI for Transportation: Work Zone Use Case proposes a data integration pipeline that enhances the utilization of work zone and traffic data from diversified platforms and introduces a novel deep learning model to predict the traffic speed and traffic collision likelihood during planned work zone events. This dataset is the processed integrated traffic data with work zone and incident information. Attached below are the number of lanes data and impacted work zone .pkl file.",
-            "title": "Data for Artificial Intelligence: Data-Centric AI for Transportation: Work Zone Use Case Processed Integrated Traffic Work Zone Data",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30169,67 +30146,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ag7u-9n3t/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ag7u-9n3t/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ag7u-9n3t/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ag7u-9n3t/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ag7u-9n3t/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ag7u-9n3t/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ag7u-9n3t/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ag7u-9n3t/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ag7u-9n3t/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Maryland highway network",
+            "identifier": "https://data.transportation.gov/api/views/ag7u-9n3t",
+            "issued": "2024-09-16",
+            "keyword": [
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "maryland",
+                "speed data",
+                "traffic detectors",
+                "traffic flow",
+                "travel time",
+                "work zones"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ag7u-9n3t",
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
+            "title": "Data for Artificial Intelligence: Data-Centric AI for Transportation: Work Zone Use Case Processed Integrated Traffic Work Zone Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Access restricted under the Privacy Act of 1974; various SORNs apply \u2013 see Privacy Impact Assessment at http://www.dot.gov/individuals/privacy/pia-security-operations-systems-sos",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/agzh-6y3k",
-            "issued": "2014-09-16",
-            "temporal": "R/2014-09-16/PT1S",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Other",
-            "keyword": [
-                "access",
-                "card",
-                "personnel",
-                "security"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "429.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
             "description": "This data set contains the personnel access card data (photo, name, activation/expiration dates, card number, and access level) as well as data about turnstiles and security panels at the DOT headquarters building. It tracks which personnel have been provided what type of access and swipes at access card readers.",
-            "title": "Physical Access Control Database -",
-            "primaryITInvestmentUII": "021-686225834",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30237,55 +30218,55 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Other"
+            "identifier": "429.0",
+            "issued": "2014-09-16",
+            "keyword": [
+                "access",
+                "card",
+                "personnel",
+                "security"
             ],
-            "accrualPeriodicity": "R/PT1S",
-            "categoryDesignation": "Administrative",
+            "landingPage": "https://data.transportation.gov/d/agzh-6y3k",
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
+            "title": "Physical Access Control Database -"
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
-            "landingPage": "https://data.transportation.gov/d/ai6d-fd6j",
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
-            "identifier": "687.1",
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
@@ -30294,35 +30275,69 @@
                     "title": "Highway Safety Improvement Program"
                 }
             ],
-            "spatial": "National, State",
-            "describedBy": "http://safety.fhwa.dot.gov/tools/data_tools/memohsip072911/",
-            "dataQuality": true,
+            "identifier": "687.1",
+            "isPartOf": "DOT-687",
+            "issued": "2014-12-29",
+            "keyword": [
+                "highway",
+                "safety"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ai6d-fd6j",
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
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/ak53-ndk2",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/04aprtvt/04aprtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "April 2004"
+                }
             ],
+            "identifier": "18.125",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -30332,60 +30347,59 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.125",
+            "landingPage": "https://data.transportation.gov/d/ak53-ndk2",
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
-            "title": "Monthly Traffic Volume Trends - April 2004",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/04aprtvt/04aprtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "April 2004"
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
+            "title": "Monthly Traffic Volume Trends - April 2004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "https://crashviewer.nhtsa.dot.gov/LegacyLTCCS/Search",
+            "agencyProgramURL": "https://www.fmcsa.dot.gov/research-and-analysis/research/large-truck-crash-causation-study",
+            "analysisUnit": "Crash / Vehicle / Driver / Person",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/akau-xuhz",
-            "issued": "2006-07-14",
-            "temporal": "2003-01-01/2003-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-29",
+            "categoryDesignation": "Research",
             "collectionInstrument": "https://crashviewer.nhtsa.dot.gov/LegacyLTCCS/Search",
-            "references": [
-                "https://crashviewer.nhtsa.dot.gov/LegacyLTCCS/Search"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FMCSA CDO",
+                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.fmcsa.dot.gov/research-and-analysis/research/large-truck-crash-causation-study",
+            "description": "The Large Truck* Crash Causation Study (LTCCS) is based on a three-year data collection project conducted by the Federal Motor Carrier Safety Administration (FMCSA) and the National Highway Traffic Safety Administration (NHTSA) of the U.S. Department of Transportation (DOT). LTCCS is the first-ever national study to attempt to determine the critical events and associated factors that contribute to serious large truck crashes allowing DOT and others to implement effective countermeasures to reduce the occurrence and severity of these crashes.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://crashviewer.nhtsa.dot.gov/LegacyLTCCS/Search",
+                    "mediaType": "text/html"
+                }
             ],
+            "identifier": "DOT-97",
+            "issued": "2006-07-14",
             "keyword": [
                 "crash",
                 "federal motor carrier safety administration",
@@ -30394,124 +30408,95 @@
                 "large truck crash causation study",
                 "ltccs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "DOT-97",
+            "landingPage": "https://data.transportation.gov/d/akau-xuhz",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-07-29",
+            "phone": "202-366-0324",
+            "programCode": [
+                "021:022"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Motor Carrier Safety Administration"
             },
-            "description": "The Large Truck* Crash Causation Study (LTCCS) is based on a three-year data collection project conducted by the Federal Motor Carrier Safety Administration (FMCSA) and the National Highway Traffic Safety Administration (NHTSA) of the U.S. Department of Transportation (DOT). LTCCS is the first-ever national study to attempt to determine the critical events and associated factors that contribute to serious large truck crashes allowing DOT and others to implement effective countermeasures to reduce the occurrence and severity of these crashes.",
-            "title": "Large Truck Crash Causation Study (LTCCS)",
-            "agencyProgramURL": "https://www.fmcsa.dot.gov/research-and-analysis/research/large-truck-crash-causation-study",
-            "programCode": [
-                "021:022"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://crashviewer.nhtsa.dot.gov/LegacyLTCCS/Search",
-                    "mediaType": "text/html"
-                }
+            "references": [
+                "https://crashviewer.nhtsa.dot.gov/LegacyLTCCS/Search"
             ],
             "spatial": "National estimates",
-            "describedBy": "https://www.fmcsa.dot.gov/research-and-analysis/research/large-truck-crash-causation-study",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "https://crashviewer.nhtsa.dot.gov/LegacyLTCCS/Search",
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
+            "title": "Large Truck Crash Causation Study (LTCCS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.bts.gov/stories/s/akum-hkrx",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2020-09-16",
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
-            "identifier": "https://data.transportation.gov/api/views/akum-hkrx",
             "description": "This page shows BLS-CPS data of monthly employment in transportation and warehousing sector by race and Hispanic or Latino ethnicity.",
-            "title": "Employment-Transportation and Warehousing Sector by Race and Ethnicity",
+            "identifier": "https://data.transportation.gov/api/views/akum-hkrx",
+            "issued": "2020-09-16",
+            "keyword": [
+                "employment",
+                "transportation employment"
+            ],
+            "landingPage": "https://data.bts.gov/stories/s/akum-hkrx",
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
+            "title": "Employment-Transportation and Warehousing Sector by Race and Ethnicity"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/am5x-xp9v",
-            "issued": "2024-05-02",
             "@type": "dcat:Dataset",
-            "modified": "2024-05-29",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joe McGill",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/am5x-xp9v",
+            "issued": "2024-05-02",
+            "landingPage": "https://data.transportation.gov/d/am5x-xp9v",
+            "modified": "2024-05-29",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "National Census of Ferry Operators (NCFO) 2022: Landing Page"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/amkt-4ehs",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
-            "keyword": [
-                "mechanical failures",
-                "vehicle maintenance",
-                "vehicles"
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
-            "identifier": "https://data.transportation.gov/api/views/amkt-4ehs",
             "description": "This dataset details mechanical failures for each applicable agency, mode, and type of service (TOS) reporting to the National Transit Database in the 2022 and 2023 report years.\n\nOnly Full Reporters report breakdowns.\n\nNTD Data Tables organize and summarize data from the 2022 and 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. This dataset is based on the 2022 and 2023 Vehicle Maintenance database files.\n\nIn years 2015-2021, you can find this data in the \"Breakdowns\" data table on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.\n\nIf you have any other questions about this table, please contact the NTD Help Desk at NTDHelp@dot.gov.",
-            "title": "2022 - 2023 NTD Annual Data - Breakdowns",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30519,62 +30504,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/amkt-4ehs/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/amkt-4ehs/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/amkt-4ehs/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/amkt-4ehs/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/amkt-4ehs/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/amkt-4ehs/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/amkt-4ehs/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/amkt-4ehs/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/amkt-4ehs/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/amkt-4ehs",
+            "issued": "2024-09-10",
+            "keyword": [
+                "mechanical failures",
+                "vehicle maintenance",
+                "vehicles"
+            ],
+            "landingPage": "https://data.transportation.gov/d/amkt-4ehs",
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
+            "title": "2022 - 2023 NTD Annual Data - Breakdowns"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ammt-7772",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2019-08-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-09",
-            "keyword": [
-                "amtrak",
-                "opportunity zone",
-                "rail",
-                "railroad"
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
-            "identifier": "https://data.transportation.gov/api/views/ammt-7772",
+            "dataQuality": true,
             "description": "This data set shows Amtrak industrial, office, and commercial real estate in opportunity zones",
-            "title": "Amtrak Real Estate Properties in Oppurtunity Zones - Industrial, Office and Commercial",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30582,61 +30565,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ammt-7772/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ammt-7772/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ammt-7772/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ammt-7772/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ammt-7772/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ammt-7772/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ammt-7772/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ammt-7772/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ammt-7772/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/ammt-7772",
+            "issued": "2019-08-28",
+            "keyword": [
+                "amtrak",
+                "opportunity zone",
+                "rail",
+                "railroad"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ammt-7772",
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
-            ]
+            ],
+            "title": "Amtrak Real Estate Properties in Oppurtunity Zones - Industrial, Office and Commercial"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://data.transportation.gov/d/amn9-4jcb",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-01-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-01-29",
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
-            "identifier": "https://data.transportation.gov/api/views/amn9-4jcb",
             "description": "",
-            "title": "Pocket Guide to Transportation-Daily Passenger Travel",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30644,43 +30628,76 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/amn9-4jcb/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/amn9-4jcb/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/amn9-4jcb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/amn9-4jcb/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/amn9-4jcb/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/amn9-4jcb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/amn9-4jcb/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/amn9-4jcb/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/amn9-4jcb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "https://data.transportation.gov/api/views/amn9-4jcb",
+            "issued": "2024-01-29",
+            "keyword": [
+                "pocket guide to transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/amn9-4jcb",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-01-29",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Pocket Guide to Transportation-Daily Passenger Travel"
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
-            "landingPage": "https://data.transportation.gov/d/amr3-cz7s",
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
+                    "downloadURL": "http://www-odi.nhtsa.dot.gov/downloads/folders/Complaints/FLAT_CMPL.zip",
+                    "mediaType": "application/zip",
+                    "title": "Complaints Flat File"
+                }
             ],
+            "identifier": "83.16",
+            "isPartOf": "DOT-83",
+            "issued": "2002-12-16",
             "keyword": [
                 "air bag",
                 "air bags",
@@ -30707,76 +30724,43 @@
                 "vin",
                 "vin search"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "83.16",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Manufacturers who determine that a product or piece of original equipment either has a safety defect or is not in compliance with Federal safety standards are required to notify the National Highway Traffic Safety Administration (NHTSA) within 5 business days. NHTSA requires that manufacturers file a Defect and Noncompliance report as well as quarterly recall status reports, in compliance with Federal Regulation 49 (the National Traffic and Motor Safety Act) Part 573, which identifies the requirements for safety recalls. This information is stored in the NHTSA database. Use this data to search for recall information related to:-\tSpecific NHTSA campaigns -\tProduct types Access to public searches of NHTSA recall databases for tires, vehicles, car seats and equipment.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - Complaints Flat File",
-            "isPartOf": "DOT-83",
-            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
-            "describedByType": "text/plain",
+            "landingPage": "https://data.transportation.gov/d/amr3-cz7s",
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
-                    "downloadURL": "http://www-odi.nhtsa.dot.gov/downloads/folders/Complaints/FLAT_CMPL.zip",
-                    "mediaType": "application/zip",
-                    "title": "Complaints Flat File"
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
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - Complaints Flat File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/anet-6eas",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2022-10-31",
-            "@type": "dcat:Dataset",
-            "modified": "2022-12-21",
-            "keyword": [
-                "cfs"
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
-            "identifier": "https://data.transportation.gov/api/views/anet-6eas",
             "description": "An aggregation of historical CFS data at a state level. This dataset comprises all historical CFS data from 1997-2017.Data is presented at its most granular level. The sum of sublevels may not equal the totals due to individual data items being suppressed due to preserve confidentiality",
-            "title": "Historical CFS Data 1997-2017",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30784,46 +30768,77 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/anet-6eas/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/anet-6eas/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/anet-6eas/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/anet-6eas/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/anet-6eas/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/anet-6eas/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/anet-6eas/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/anet-6eas/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/anet-6eas/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/anet-6eas",
+            "issued": "2022-10-31",
+            "keyword": [
+                "cfs"
+            ],
+            "landingPage": "https://data.transportation.gov/d/anet-6eas",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2022-12-21",
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
+            "title": "Historical CFS Data 1997-2017"
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
-            "landingPage": "https://data.transportation.gov/d/angv-9262",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/09jantvt/09jantvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "January 2009"
+                }
             ],
+            "identifier": "18.68",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -30833,79 +30848,43 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.68",
+            "landingPage": "https://data.transportation.gov/d/angv-9262",
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
-            "title": "Monthly Traffic Volume Trends - January 2009",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/09jantvt/09jantvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "January 2009"
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
+            "title": "Monthly Traffic Volume Trends - January 2009"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/anj8-k6f5",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2022-03-18",
-            "@type": "dcat:Dataset",
-            "temporal": "2022-03-18/2022-03-18",
-            "modified": "2024-11-14",
-            "keyword": [
-                "ai use case",
-                "artificial intelligence",
-                "eo 13960",
-                "inventory",
-                "trustworthy ai"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "US Department of Transportation"
-            },
-            "identifier": "https://data.transportation.gov/api/views/anj8-k6f5",
+            "dataQuality": true,
             "description": "This dataset is a list of Department of Transportation (DOT) Artificial Intelligence (AI) use cases.\n\nArtificial intelligence (AI) promises to drive the growth of the United States economy and improve the quality of life of all Americans. Pursuant to Section 5 of Executive Order (EO) 13960, \"Promoting the Use of Trustworthy Artificial Intelligence in the Federal Government,\" Federal agencies are required to inventory their AI use cases and share their inventories with other government agencies and the public.\n\nIn accordance with the requirements of EO 13960, this spreadsheet provides the mechanism for federal agencies to create their inaugural AI use case inventories.\n\nhttps://www.federalregister.gov/documents/2020/12/08/2020-27065/promoting-the-use-of-trustworthy-artificial-intelligence-in-the-federal-government",
-            "title": "Department of Transportation Inventory of Artificial Intelligence Use Cases",
-            "primaryITInvestmentUII": "021-040221132",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30913,71 +30892,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/anj8-k6f5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/anj8-k6f5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/anj8-k6f5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/anj8-k6f5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/anj8-k6f5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/anj8-k6f5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/anj8-k6f5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/anj8-k6f5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/anj8-k6f5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/anj8-k6f5",
+            "issued": "2022-03-18",
+            "keyword": [
+                "ai use case",
+                "artificial intelligence",
+                "eo 13960",
+                "inventory",
+                "trustworthy ai"
+            ],
+            "landingPage": "https://data.transportation.gov/d/anj8-k6f5",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-14",
+            "primaryITInvestmentUII": "021-040221132",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
+            "spatial": "United States",
+            "temporal": "2022-03-18/2022-03-18",
             "theme": [
                 "Administrative"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Transportation Inventory of Artificial Intelligence Use Cases"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://catalog.data.faa.gov/dataset/terminal-procedures-publicationairport-diagrams---aeronautical-information-services-digita",
             "bureauCode": [
                 "021:12"
             ],
-            "issued": "2020-11-14",
-            "@type": "dcat:Dataset",
-            "modified": "2021-11-09",
-            "keyword": [
-                "approach",
-                "arrival",
-                "departure",
-                "instrument",
-                "procedure",
-                "radar",
-                "takeoff"
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
-            "identifier": "a7622fac-345f-486c-8a4e-b9316ecb165c",
             "description": "The U.S. Terminal Procedure Publications (TPPs) is a 26 volume set of printed paper books containing Instrument Approach Procedure charts (IAP), Departure Procedure charts (DP), Standard Terminal Arrival charts (STAR), and Airport Diagrams. Also included are Takeoff, Radar, and Alternate Minima textual procedures.",
-            "title": "Terminal Procedures Publication/Airport Diagrams - Aeronautical Information Services Digital Products",
-            "primaryITInvestmentUII": "021-129509270",
-            "programCode": [
-                "021:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30986,51 +30963,55 @@
                     "title": "Aeronautical Information Services Digital Products"
                 }
             ],
-            "systemOfRecords": "https://www.govinfo.gov/content/pkg/FR-2016-08-15/pdf/2016-19354.pdf",
+            "identifier": "a7622fac-345f-486c-8a4e-b9316ecb165c",
+            "issued": "2020-11-14",
+            "keyword": [
+                "approach",
+                "arrival",
+                "departure",
+                "instrument",
+                "procedure",
+                "radar",
+                "takeoff"
+            ],
+            "landingPage": "https://catalog.data.faa.gov/dataset/terminal-procedures-publicationairport-diagrams---aeronautical-information-services-digita",
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
+            "title": "Terminal Procedures Publication/Airport Diagrams - Aeronautical Information Services Digital Products"
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
-            "landingPage": "https://data.transportation.gov/d/aqbe-8eey",
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
-            "identifier": "692.19",
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
@@ -31039,49 +31020,50 @@
                     "title": "2011 Fatal Crashes"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.19",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/aqbe-8eey",
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
-            "landingPage": "https://data.transportation.gov/d/aqct-knjk",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-09-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
-            "keyword": [
-                "maintenance facilities",
-                "passenger facilities",
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
-            "identifier": "https://data.transportation.gov/api/views/aqct-knjk",
             "description": "This dataset details station/facility types and counts for each applicable agency reported to the National Transit Database for report years 2022 and 2023.\n\nNTD Data Tables organize and summarize data from the 2022 and 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. This dataset is based on the 2022 and 2023 Transit Facilities and Transit Stations database files.\n\nIn years 2015-2021, you can find this data in the \"Facilities and Stations\" data table on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.\n\nIf you have any other questions about this table, please contact the NTD Help Desk at NTDHelp@dot.gov.",
-            "title": "2022 - 2023 NTD Annual Data - Stations and Facilities (by Agency and Facility Type)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31089,46 +31071,81 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/aqct-knjk/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/aqct-knjk/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/aqct-knjk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/aqct-knjk/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/aqct-knjk/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/aqct-knjk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/aqct-knjk/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/aqct-knjk/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/aqct-knjk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/aqct-knjk",
+            "issued": "2024-09-06",
+            "keyword": [
+                "maintenance facilities",
+                "passenger facilities",
+                "transit administrative facilities",
+                "transit facilities",
+                "transit parking facilities",
+                "transit stations"
+            ],
+            "landingPage": "https://data.transportation.gov/d/aqct-knjk",
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
+            "title": "2022 - 2023 NTD Annual Data - Stations and Facilities (by Agency and Facility Type)"
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
-            "landingPage": "https://data.transportation.gov/d/aqh3-3rri",
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
+                    "mediaType": "text/csv",
+                    "title": "NHTSA API"
+                }
             ],
+            "identifier": "83.2",
+            "isPartOf": "DOT-83",
+            "issued": "2002-12-16",
             "keyword": [
                 "air bag",
                 "air bags",
@@ -31155,67 +31172,40 @@
                 "vin",
                 "vin search"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "83.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Manufacturers who determine that a product or piece of original equipment either has a safety defect or is not in compliance with Federal safety standards are required to notify the National Highway Traffic Safety Administration (NHTSA) within 5 business days. NHTSA requires that manufacturers file a Defect and Noncompliance report as well as quarterly recall status reports, in compliance with Federal Regulation 49 (the National Traffic and Motor Safety Act) Part 573, which identifies the requirements for safety recalls. This information is stored in the NHTSA database. Use this data to search for recall information related to:-\tSpecific NHTSA campaigns -\tProduct types Access to public searches of NHTSA recall databases for tires, vehicles, car seats and equipment.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - NHTSA API",
-            "isPartOf": "DOT-83",
-            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
-            "describedByType": "text/plain",
+            "landingPage": "https://data.transportation.gov/d/aqh3-3rri",
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
-                    "mediaType": "text/csv",
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
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/aqxq-n5hy",
-            "issued": "2023-04-04",
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
-            "identifier": "https://data.transportation.gov/api/views/aqxq-n5hy",
             "description": "This dataset is the source dataset and contains raw data values. It will replace the current data download (https://safetydata.fra.dot.gov/OfficeofSafety/publicsite/on_the_fly_download.aspx) when the safetydata.fra.dot.gov site is decommissioned in 2024. To download data that contains data in a user-friendly human-readable format, please reference https://data.transportation.gov/Railroads/Rail-Equipment-Accident-Incident-Data/85tf-25kj.",
-            "title": "Railroad Equipment Accident/Incident Source Data (Form 54)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31223,46 +31213,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/aqxq-n5hy/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/aqxq-n5hy/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/aqxq-n5hy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/aqxq-n5hy/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/aqxq-n5hy/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/aqxq-n5hy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/aqxq-n5hy/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/aqxq-n5hy/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/aqxq-n5hy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/aqxq-n5hy",
+            "issued": "2023-04-04",
+            "landingPage": "https://data.transportation.gov/d/aqxq-n5hy",
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
+            "title": "Railroad Equipment Accident/Incident Source Data (Form 54)"
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
-            "landingPage": "https://data.transportation.gov/d/ara3-mcn5",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/14augtvt/14augtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "August 2014"
+                }
             ],
+            "identifier": "18.65",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -31272,57 +31287,41 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.65",
+            "landingPage": "https://data.transportation.gov/d/ara3-mcn5",
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
-            "title": "Monthly Traffic Volume Trends - August 2014",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/14augtvt/14augtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "August 2014"
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
+            "title": "Monthly Traffic Volume Trends - August 2014"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ari2-ub6a",
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
+            "identifier": "https://data.transportation.gov/api/views/ari2-ub6a",
+            "issued": "2021-04-26",
             "keyword": [
                 "bureau",
                 "container",
@@ -31340,32 +31339,23 @@
                 "transportation",
                 "vessel"
             ],
-            "identifier": "https://data.transportation.gov/api/views/ari2-ub6a",
+            "landingPage": "https://data.transportation.gov/d/ari2-ub6a",
+            "modified": "2024-02-07",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "PPFSP 24",
             "title": "Tanker Vessel Dwell Times"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/art6-ye9i",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/art6-ye9i",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "Amtrak Rail Stations",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31373,62 +31363,52 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/art6-ye9i/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/art6-ye9i/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/art6-ye9i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/art6-ye9i/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/art6-ye9i/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/art6-ye9i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/art6-ye9i/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/art6-ye9i/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/art6-ye9i/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/art6-ye9i",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/art6-ye9i",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Amtrak Rail Stations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/as3z-m8rd",
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
-            "identifier": "https://data.transportation.gov/api/views/as3z-m8rd",
             "description": "A data base of responses to the 2022 National Census of Ferries.\n\nThis file gives information about segments for particular operators.",
-            "title": "2022 NCFO Operator Segments File",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31436,42 +31416,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/as3z-m8rd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/as3z-m8rd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/as3z-m8rd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/as3z-m8rd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/as3z-m8rd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/as3z-m8rd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/as3z-m8rd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/as3z-m8rd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/as3z-m8rd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/as3z-m8rd",
+            "issued": "2024-05-01",
+            "keyword": [
+                "ferry",
+                "ferry operators",
+                "ferry transit",
+                "ncfo",
+                "passenger ferry"
+            ],
+            "landingPage": "https://data.transportation.gov/d/as3z-m8rd",
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
+            "title": "2022 NCFO Operator Segments File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/as63-iaxk",
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
+            "description": "The majority of this set of data files was acquired under USDOT FHWA cooperative agreement DTFH61-12-D-00040 by Battelle and transferred to Volpe, The National Transportation Systems Center. Battelle and the Volpe Center coordinated to determine and attain the data necessary for the IDTO Impact Assessment. The Volpe Center was also under a cooperative agreement with USDOT FHWA (DTFH61-13-V-00008). Other data files within the set were generated by the Volpe Center for the purposes of the assessment.\r\n\r\nThis legacy dataset was created before data.transportation.gov and is only currently available via the attached file(s). Please contact the dataset owner if there is a need for users to work with this data using the data.transportation.gov analysis features (online viewing, API, graphing, etc.) and the USDOT will consider modifying the dataset to fully integrate in data.transportation.gov.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/download/as63-iaxk/application/vnd.openxmlformats-officedocument.wordprocessingml.document",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/as63-iaxk",
             "issued": "2015-01-04",
-            "@type": "dcat:Dataset",
-            "temporal": "2013-01-04/2015-01-04",
-            "modified": "2015-01-04",
             "keyword": [
                 "central ohio transit authority (cota)",
                 "columbus",
@@ -31488,50 +31500,53 @@
                 "survey data",
                 "technical feasibility"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/as63-iaxk",
+            "license": "http://creativecommons.org/licenses/by-nc-sa/3.0/legalcode",
+            "modified": "2015-01-04",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Department of Transportation"
             },
-            "identifier": "https://data.transportation.gov/api/views/as63-iaxk",
-            "description": "The majority of this set of data files was acquired under USDOT FHWA cooperative agreement DTFH61-12-D-00040 by Battelle and transferred to Volpe, The National Transportation Systems Center. Battelle and the Volpe Center coordinated to determine and attain the data necessary for the IDTO Impact Assessment. The Volpe Center was also under a cooperative agreement with USDOT FHWA (DTFH61-13-V-00008). Other data files within the set were generated by the Volpe Center for the purposes of the assessment.\r\n\r\nThis legacy dataset was created before data.transportation.gov and is only currently available via the attached file(s). Please contact the dataset owner if there is a need for users to work with this data using the data.transportation.gov analysis features (online viewing, API, graphing, etc.) and the USDOT will consider modifying the dataset to fully integrate in data.transportation.gov.",
-            "title": "Integrated Dynamic Transit Operations (IDTO) Impact Assessment (IA)",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/download/as63-iaxk/application/vnd.openxmlformats-officedocument.wordprocessingml.document",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
-                }
-            ],
             "spatial": "Columbus, Orlando",
-            "dataQuality": true,
-            "license": "http://creativecommons.org/licenses/by-nc-sa/3.0/legalcode",
-            "accrualPeriodicity": "irregular",
+            "temporal": "2013-01-04/2015-01-04",
             "theme": [
                 "Automobiles"
-            ]
+            ],
+            "title": "Integrated Dynamic Transit Operations (IDTO) Impact Assessment (IA)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "https://www.phmsa.dot.gov/approvals-and-permits/hazmat/approvals-search",
+            "agencyProgramURL": "http://www.phmsa.dot.gov/hazmat/regs/sp-a/special-permits",
+            "analysisUnit": "Special Permit",
             "bureauCode": [
                 "021:50"
             ],
-            "landingPage": "https://data.transportation.gov/d/au37-96ku",
-            "issued": "2012-01-18",
-            "temporal": "1970-01-01/2013-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-29",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "https://www.phmsa.dot.gov/approvals-and-permits/hazmat/special-permits-search"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Donald Burger",
+                "hasEmail": "mailto:donald.burger@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Pipeline and Hazardous Materials Safety Administration has the primary responsibility for the issuance of DOT Special Permits and Approvals to the Hazardous Materials Regulations (HMR). A Special Permit or Approval is a document which authorizes a person to perform a function that is not currently authorized under the authority of the HMR. Also, in many instances, the Regulations require approvals and/or registrations prior to transportation in commerce.   The Special Permits Search tool allows a user to search for active Special permits.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.phmsa.dot.gov/hazmat/regs/sp-a/special-permits/search",
+                    "mediaType": "text/html",
+                    "title": "Data Mining Tool"
+                }
             ],
+            "identifier": "31.2",
+            "isPartOf": "DOT-31",
+            "issued": "2012-01-18",
             "keyword": [
                 "competent authority",
                 "cylinders",
@@ -31541,52 +31556,41 @@
                 "packaging labs",
                 "special permits"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Donald Burger",
-                "hasEmail": "mailto:donald.burger@dot.gov"
-            },
-            "identifier": "31.2",
+            "landingPage": "https://data.transportation.gov/d/au37-96ku",
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
-            "description": "The Pipeline and Hazardous Materials Safety Administration has the primary responsibility for the issuance of DOT Special Permits and Approvals to the Hazardous Materials Regulations (HMR). A Special Permit or Approval is a document which authorizes a person to perform a function that is not currently authorized under the authority of the HMR. Also, in many instances, the Regulations require approvals and/or registrations prior to transportation in commerce.   The Special Permits Search tool allows a user to search for active Special permits.",
-            "title": "Hazmat Special Permits - Data Mining Tool",
-            "isPartOf": "DOT-31",
-            "agencyProgramURL": "http://www.phmsa.dot.gov/hazmat/regs/sp-a/special-permits",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.phmsa.dot.gov/hazmat/regs/sp-a/special-permits/search",
-                    "mediaType": "text/html",
-                    "title": "Data Mining Tool"
-                }
+            "references": [
+                "https://www.phmsa.dot.gov/approvals-and-permits/hazmat/special-permits-search"
             ],
             "spatial": "City",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "https://www.phmsa.dot.gov/approvals-and-permits/hazmat/approvals-search",
+            "temporal": "1970-01-01/2013-12-31",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Special Permit",
-            "phone": "202-493-0550",
-            "language": [
-                "en-US"
-            ]
+            "title": "Hazmat Special Permits - Data Mining Tool"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/auu6-iy49",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "description": "NHTSA Investigations by Manufacturer",
+            "identifier": "https://data.transportation.gov/api/views/auu6-iy49",
             "issued": "2024-02-05",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-25",
             "keyword": [
                 "air bag",
                 "air bags",
@@ -31616,37 +31620,48 @@
                 "vin",
                 "vin search"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/auu6-iy49",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-07-25",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/auu6-iy49",
-            "description": "NHTSA Investigations by Manufacturer",
-            "title": "NHTSA Investigations by Manufacturer",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "theme": [
                 "Automobiles"
-            ]
+            ],
+            "title": "NHTSA Investigations by Manufacturer"
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
-            "landingPage": "https://data.transportation.gov/d/avu6-eimd",
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
+            "identifier": "248.5",
+            "isPartOf": "DOT-248",
+            "issued": "2010-01-05",
             "keyword": [
                 "5",
                 "assessment",
@@ -31660,58 +31675,55 @@
                 "safety",
                 "star"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "248.5",
+            "landingPage": "https://data.transportation.gov/d/avu6-eimd",
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
             "accessLevel": "non-public",
-            "rights": "The data set contains controlled unclassified procurement information, confidential business information, and information protected by statute or regulation.",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/awju-pvhc",
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
+            "description": "Delphi acconts payable module contains the following data elements, but are not limited to vendor information, bank account information, invoice numbers, invoice amounts, line of accounting details, interest payment information, 1099 details, invoice aging, invoice approver information, income tax types, and employee information.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.transportation.gov/mission/data-inventory-not-available",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "597.0",
+            "issued": "2014-12-29",
             "keyword": [
                 "1099",
                 "bank account",
@@ -31725,76 +31737,44 @@
                 "line of accounting",
                 "vendor"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DOT Socrata",
-                "hasEmail": "mailto:Socrata@dot.gov"
-            },
-            "identifier": "597.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
-            "description": "Delphi acconts payable module contains the following data elements, but are not limited to vendor information, bank account information, invoice numbers, invoice amounts, line of accounting details, interest payment information, 1099 details, invoice aging, invoice approver information, income tax types, and employee information.",
-            "title": "Delphi Accounts Payable Module -",
+            "landingPage": "https://data.transportation.gov/d/awju-pvhc",
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
+            "title": "Delphi Accounts Payable Module -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://data.transportation.gov/d/awpb-pj3u",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:18"
             ],
-            "rights": "internal system with named users.",
-            "issued": "2018-12-18",
-            "@type": "dcat:Dataset",
-            "temporal": "R/2013/P1Y",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-01",
-            "keyword": [
-                "highway",
-                "hsp",
-                "plans",
-                "safety",
-                "strap",
-                "triprs"
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
-            "identifier": "534.0",
+            "dataQuality": false,
             "description": "A document management system & a database for collecting/assessing information on State Traffic Records Systems & a data analytic system for aggregating States data. related to TRIPRS system",
-            "title": "State Traffic Records Assessment Process  STRAP -",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31802,54 +31782,56 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P1Y",
-            "theme": [
-                "Transportation"
-            ],
-            "categoryDesignation": "Research",
-            "phone": "202-366-5649",
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "bureauCode": [
-                "021:18"
+            "identifier": "534.0",
+            "issued": "2018-12-18",
+            "keyword": [
+                "highway",
+                "hsp",
+                "plans",
+                "safety",
+                "strap",
+                "triprs"
             ],
-            "landingPage": "https://data.transportation.gov/d/ax3a-4jzp",
-            "issued": "1998-12-24",
-            "temporal": "R/1998-12-14/P1D",
-            "@type": "dcat:Dataset",
+            "landingPage": "https://data.transportation.gov/d/awpb-pj3u",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2024-05-01",
-            "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.nhtsa.gov/Research/Databases+and+Software/NHTSA+Test+Reference+Guides"
+            "phone": "202-366-5649",
+            "programCode": [
+                "021:000"
             ],
-            "keyword": [
-                "nhtsa crash test database",
-                "nhtsa vehicle crash test database"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "rights": "internal system with named users.",
+            "temporal": "R/2013/P1Y",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "State Traffic Records Assessment Process  STRAP -"
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
             ],
+            "categoryDesignation": "Research",
+            "collectionInstrument": "Transportation",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "364.4",
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
@@ -31858,32 +31840,68 @@
                     "title": "Vehicle Test Query by Vehicle Table Parameters"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.4",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ax3a-4jzp",
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
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/axib-3aaz",
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
+                    "description": "2013 South Carolina HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/southcarolina2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 South Carolina"
+                }
+            ],
+            "identifier": "678.144",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -31897,79 +31915,39 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.144",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 South Carolina",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/axib-3aaz",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/southcarolina2013.zip",
-                    "description": "2013 South Carolina HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 South Carolina"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 South Carolina"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ayqp-ckmi",
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
-            "identifier": "https://data.transportation.gov/api/views/ayqp-ckmi",
             "description": "Data for Artificial Intelligence: Data-Centric AI for Transportation: Work Zone Use Case proposes a data integration pipeline that enhances the utilization of work zone and traffic data from diversified platforms and introduces a novel deep learning model to predict the traffic speed and traffic collision likelihood during planned work zone events. This dataset is raw Maryland roadway incident data",
-            "title": "Data for Artificial Intelligence: Data-Centric AI for Transportation: Work Zone Use Case Raw Maryland Incidents",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31977,59 +31955,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ayqp-ckmi/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ayqp-ckmi/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ayqp-ckmi/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ayqp-ckmi/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ayqp-ckmi/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ayqp-ckmi/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ayqp-ckmi/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ayqp-ckmi/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ayqp-ckmi/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Maryland highway network",
+            "identifier": "https://data.transportation.gov/api/views/ayqp-ckmi",
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
+            "landingPage": "https://data.transportation.gov/d/ayqp-ckmi",
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
+            "title": "Data for Artificial Intelligence: Data-Centric AI for Transportation: Work Zone Use Case Raw Maryland Incidents"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/az4n-8mr2",
             "bureauCode": [
                 "021:17"
             ],
-            "issued": "2024-08-16",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
-            "keyword": [
-                "census",
-                "mcmis.",
-                "usdot number"
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
-            "identifier": "https://data.transportation.gov/api/views/az4n-8mr2",
             "description": "The Company Census File contains records for active entities registered with FMCSA. Active entities include those entities subject to the FMCSR, HMR, or intrastate non-Hazardous Material (HM) carriers. To identify each entity, FMCSA assigns a unique number to each entity record. This number is referred to as the USDOT number.\nEach Census record contains entity identifying data, business operations data, equipment and driver data, and carrier review data.",
-            "title": "Company Census File",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32037,73 +32022,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/az4n-8mr2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/az4n-8mr2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/az4n-8mr2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/az4n-8mr2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/az4n-8mr2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/az4n-8mr2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/az4n-8mr2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/az4n-8mr2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/az4n-8mr2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/az4n-8mr2",
+            "issued": "2024-08-16",
+            "keyword": [
+                "census",
+                "mcmis.",
+                "usdot number"
+            ],
+            "landingPage": "https://data.transportation.gov/d/az4n-8mr2",
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
+            "title": "Company Census File"
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
-            "landingPage": "https://data.transportation.gov/d/azfu-uj32",
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
-            "identifier": "1841.5",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/bio/schema.htm",
             "description": "The NHTSA Biomechanics Test Database is a repository of experimental data used by NHTSA for developing Anthropomophic Test Devices and associated Injury Criteria. The data is disseminated via this website for use by academia, the automotive industry, and the public to improve the safety of automobiles and reduce death and injuries on our nations highway. Because of the nature of the testing, the applicability of the data extends far beyond auto safety, and may be useful for those in the sports medicine, space travel, aircraft, military or any activity where the human body is exposed impact.",
-            "title": "Biomechanics Test Database - Interactive Access",
-            "isPartOf": "DOT-1841",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research",
-            "primaryITInvestmentUII": "021-961265599",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32112,32 +32089,66 @@
                     "title": "Interactive Access"
                 }
             ],
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/bio/schema.htm",
-            "dataQuality": false,
+            "identifier": "1841.5",
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
+            "landingPage": "https://data.transportation.gov/d/azfu-uj32",
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
+            "title": "Biomechanics Test Database - Interactive Access"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.21949/1503751",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2017-01-12",
-            "references": [
-                "https://rosap.ntl.bts.gov/view/dot/32105"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Transportation Library Data Curator",
+                "hasEmail": "mailto:ntldatacurator@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The datasets in this zip file are in support of FHWA-JPO-16-379, Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs - calibration Report for Phoenix Testbed : Final Report.   The compressed zip file totals 1.1 GB in size.   The zip file have been uploaded as-is; no further documentation was supplied by NTL, excepted as noted: All located .docx files were converted to .pdf document files which are an archival format. These .pdfs were then added to the zip file alongside the original .docx files. The initial zip file presented to NTL contained uncompressed datasets and duplicative zip files of the files. In order to make the overall size of the this zip file more manageable, duplicative files were deleted.  The zip file can be unzipped using any zip compression/decompression software. This zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .cvs text files which can be read using any text editor; .docx document files which can be read in Microsoft Word and some other word processing programs; .txt text files which can be opened with any text editor; .xlsx spreadsheet files which can be read in Microsoft Excel and some other spreadsheet programs; .cfg computer configuration files; .db database files, which can be opened with many database programs; .rif raster image files, these files may have been created by the Corel Painter image editing application, a proprietary software program, although other image programs may open the files [software requirements].   These files were last accessed in 2017.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The datasets in this zip file are in support of FHWA-JPO-16-379, Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs - calibration Report for Phoenix Testbed : Final Report.   The compressed zip file totals 1.1 GB in size.   The zip file have been uploaded as-is; no further documentation was supplied by NTL, excepted as noted: All located .docx files were converted to .pdf document files which are an archival format. These .pdfs were then added to the zip file alongside the original .docx files. The initial zip file presented to NTL contained uncompressed datasets and duplicative zip files of the files. In order to make the overall size of the this zip file more manageable, duplicative files were deleted.  The zip file can be unzipped using any zip compression/decompression software. This zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .cvs text files which can be read using any text editor; .docx document files which can be read in Microsoft Word and some other word processing programs; .txt text files which can be opened with any text editor; .xlsx spreadsheet files which can be read in Microsoft Excel and some other spreadsheet programs; .cfg computer configuration files; .db database files, which can be opened with many database programs; .rif raster image files, these files may have been created by the Corel Painter image editing application, a proprietary software program, although other image programs may open the files [software requirements].   These files were last accessed in 2017.",
+                    "downloadURL": "https://doi.org/10.21949/1503751",
+                    "mediaType": "application/zip",
+                    "title": "Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs: calibration Report for Phoenix Testbed  [supporting datasets - Phoenix]"
+                }
             ],
+            "identifier": "https://data.transportation.gov/api/views/azrt-pxbx",
+            "issued": "2017-07-26",
             "keyword": [
                 "active transportation and demand management",
                 "analysis modeling and simulation",
@@ -32152,76 +32163,45 @@
                 "traffic flow",
                 "travel demand"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Transportation Library Data Curator",
-                "hasEmail": "mailto:ntldatacurator@dot.gov"
-            },
+            "landingPage": "https://doi.org/10.21949/1503751",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2017-01-12",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Aviation Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/azrt-pxbx",
-            "description": "The datasets in this zip file are in support of FHWA-JPO-16-379, Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs - calibration Report for Phoenix Testbed : Final Report.   The compressed zip file totals 1.1 GB in size.   The zip file have been uploaded as-is; no further documentation was supplied by NTL, excepted as noted: All located .docx files were converted to .pdf document files which are an archival format. These .pdfs were then added to the zip file alongside the original .docx files. The initial zip file presented to NTL contained uncompressed datasets and duplicative zip files of the files. In order to make the overall size of the this zip file more manageable, duplicative files were deleted.  The zip file can be unzipped using any zip compression/decompression software. This zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .cvs text files which can be read using any text editor; .docx document files which can be read in Microsoft Word and some other word processing programs; .txt text files which can be opened with any text editor; .xlsx spreadsheet files which can be read in Microsoft Excel and some other spreadsheet programs; .cfg computer configuration files; .db database files, which can be opened with many database programs; .rif raster image files, these files may have been created by the Corel Painter image editing application, a proprietary software program, although other image programs may open the files [software requirements].   These files were last accessed in 2017.",
-            "title": "Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs: calibration Report for Phoenix Testbed  [supporting datasets]",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://doi.org/10.21949/1503751",
-                    "description": "The datasets in this zip file are in support of FHWA-JPO-16-379, Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs - calibration Report for Phoenix Testbed : Final Report.   The compressed zip file totals 1.1 GB in size.   The zip file have been uploaded as-is; no further documentation was supplied by NTL, excepted as noted: All located .docx files were converted to .pdf document files which are an archival format. These .pdfs were then added to the zip file alongside the original .docx files. The initial zip file presented to NTL contained uncompressed datasets and duplicative zip files of the files. In order to make the overall size of the this zip file more manageable, duplicative files were deleted.  The zip file can be unzipped using any zip compression/decompression software. This zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .cvs text files which can be read using any text editor; .docx document files which can be read in Microsoft Word and some other word processing programs; .txt text files which can be opened with any text editor; .xlsx spreadsheet files which can be read in Microsoft Excel and some other spreadsheet programs; .cfg computer configuration files; .db database files, which can be opened with many database programs; .rif raster image files, these files may have been created by the Corel Painter image editing application, a proprietary software program, although other image programs may open the files [software requirements].   These files were last accessed in 2017.",
-                    "@type": "dcat:Distribution",
-                    "title": "Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs: calibration Report for Phoenix Testbed  [supporting datasets - Phoenix]"
-                }
+            "references": [
+                "https://rosap.ntl.bts.gov/view/dot/32105"
             ],
             "spatial": "United States, Arizona, Phoenix",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "language": [
-                "en-US"
-            ]
+            "title": "Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs: calibration Report for Phoenix Testbed  [supporting datasets]"
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
-            "landingPage": "https://data.transportation.gov/d/b26f-mmwe",
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
-            "identifier": "693.12",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
             "description": "The NBI System is the collection of bridge inspection information and costs associated with bridge replacements of structurally deficient bridges on and off the NHS. This data is collected under the auspices of the National Bridge Inspection Standards (NBIS) as prescribed by law. The NBI System collects the information that is used to determine eligibility for NHS projects, performance measure reporting, NHS penalty determination, and reporting to Congress.  It supports oversight of the NBIS through various report tools, and provides data reporting that supports agency strategic goals.",
-            "title": "National Bridge Inventory System (NBI) - 2003",
-            "isPartOf": "DOT-693",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
-            "primaryITInvestmentUII": "021-012940226",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32230,62 +32210,60 @@
                     "title": "2003"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
-            "dataQuality": true,
+            "identifier": "693.12",
+            "isPartOf": "DOT-693",
+            "issued": "1992-12-31",
+            "keyword": [
+                "bridge",
+                "condition",
+                "deck",
+                "inspection",
+                "structure"
+            ],
+            "landingPage": "https://data.transportation.gov/d/b26f-mmwe",
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
+            "title": "National Bridge Inventory System (NBI) - 2003"
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
-            "landingPage": "https://data.transportation.gov/d/b29v-26fx",
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
-            "identifier": "18.48",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - March 2013",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32294,32 +32272,72 @@
                     "title": "March 2013"
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
+            "identifier": "18.48",
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
+            "landingPage": "https://data.transportation.gov/d/b29v-26fx",
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
+            "title": "Monthly Traffic Volume Trends - March 2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/b2ta-7rs5",
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
+                    "description": "2011 Delaware HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/delaware2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Delaware"
+                }
+            ],
+            "identifier": "678.9",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -32333,82 +32351,45 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.9",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Delaware",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/b2ta-7rs5",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/delaware2011.zip",
-                    "description": "2011 Delaware HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Delaware"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Delaware"
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
-            "landingPage": "https://data.transportation.gov/d/b2v7-cv3k",
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
-            "identifier": "692.3",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - Federal Aid Functional Class",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "primaryITInvestmentUII": "021-845083703",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32417,56 +32398,57 @@
                     "title": "Federal Aid Functional Class"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.3",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/b2v7-cv3k",
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
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - Federal Aid Functional Class"
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
-            "landingPage": "https://data.transportation.gov/d/b2yd-9p4p",
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
-            "identifier": "364.7",
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
@@ -32475,32 +32457,68 @@
                     "title": "Vehicle Browse Tests"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.7",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/b2yd-9p4p",
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
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/b35f-4efy",
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
+                    "description": "2013 Nebraska HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/nebraska20913.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Nebraska"
+                }
+            ],
+            "identifier": "678.131",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -32514,111 +32532,73 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.131",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Nebraska",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/b35f-4efy",
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
-                    "description": "2013 Nebraska HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Nebraska"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Nebraska"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/b39d-rg8e",
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
-            "identifier": "https://data.transportation.gov/api/views/b39d-rg8e",
+            "dataQuality": true,
             "description": "This is the summary of operational data for train miles, number of employee hours worked, yard switching miles, passenger miles, number of passengers transported and the number of reports submitted.",
-            "title": "Operational Data (1.02)",
+            "identifier": "https://data.transportation.gov/api/views/b39d-rg8e",
+            "issued": "2024-10-24",
+            "landingPage": "https://data.transportation.gov/d/b39d-rg8e",
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
+            "title": "Operational Data (1.02)"
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
-            "identifier": "https://data.transportation.gov/api/views/b3jd-9ue9",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 1984",
-            "title": "Historic HPMS Data (Sample) - 1984",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32626,71 +32606,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/b3jd-9ue9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/b3jd-9ue9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/b3jd-9ue9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/b3jd-9ue9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/b3jd-9ue9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/b3jd-9ue9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/b3jd-9ue9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/b3jd-9ue9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/b3jd-9ue9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/b3jd-9ue9",
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
+            "title": "Historic HPMS Data (Sample) - 1984"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/b3k6-qwyh",
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
-            "identifier": "https://data.transportation.gov/api/views/b3k6-qwyh",
+            "dataQuality": true,
             "description": "The data describe freeway car-following behavior (such as velocity, acceleration, and relative position) for the car-following instances observed during 6 data collection runs, collected using an Instrumented Research Vehicle (IRV) along freeways and arterials in western Massachusetts in the summer of 2016 to better understand work zone driver behaviors. The USDOT Volpe National Transportation Systems Center (Volpe Center) identified, isolated, and classified individual car following instances from within the raw datasets (classification parameters included roadway type, level of congestion, and speed limit), then processed, refined, and cleaned the dataset.\n\nThis table contains metadata about each data collection run. See also the instances table (https://datahub.transportation.gov/Automobiles/Enhancing-Microsimulation-Models-for-Improved-Work/74ug-57tr) and radar table (https://datahub.transportation.gov/Automobiles/Enhancing-Microsimulation-Models-for-Improved-Work/4qbx-egtn).",
-            "title": "Enhancing Microsimulation Models for Improved Work Zone Planning: Car-Following Data from Western Massachusetts (Runs)",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32698,61 +32675,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/b3k6-qwyh/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/b3k6-qwyh/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/b3k6-qwyh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/b3k6-qwyh/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/b3k6-qwyh/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/b3k6-qwyh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/b3k6-qwyh/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/b3k6-qwyh/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/b3k6-qwyh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "-72.5339,42.0211,-72.6494,42.3927",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/b3k6-qwyh",
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
+            "landingPage": "https://data.transportation.gov/d/b3k6-qwyh",
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
+            "title": "Enhancing Microsimulation Models for Improved Work Zone Planning: Car-Following Data from Western Massachusetts (Runs)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://data.transportation.gov/d/b3ps-driu",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-02-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-09",
-            "keyword": [
-                "pocket guide to transportation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vasu Rapolu",
                 "hasEmail": "mailto:vasu.rapolu.ctr@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/b3ps-driu",
             "description": "",
-            "title": "Pocket Guide to Transportation-Moving People",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32760,78 +32744,57 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/b3ps-driu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/b3ps-driu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/b3ps-driu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/b3ps-driu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/b3ps-driu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/b3ps-driu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/b3ps-driu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/b3ps-driu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/b3ps-driu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/b3ps-driu",
+            "issued": "2024-02-20",
+            "keyword": [
+                "pocket guide to transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/b3ps-driu",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-09",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "Pocket Guide to Transportation-Moving People"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://nhtsa.gov/recalls",
-            "issued": "2024-02-21",
             "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
-            "keyword": [
-                "air bag",
-                "air bags",
-                "auto",
-                "campaign",
-                "car",
-                "cars",
-                "car seat",
-                "child safety seats",
-                "defect",
-                "defects",
-                "email",
-                "equipment",
-                "fmvss",
-                "investigation",
-                "investigations",
-                "office of defect investigations",
-                "potential affected",
-                "recall",
-                "recalls",
-                "safety",
-                "tire",
-                "tires",
-                "vehicles"
-            ],
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/b3rp-be92",
+            "dataQuality": true,
             "description": "About the Data\nThe dataset includes publicly available NHTSA investigation information related to the identification and correction of safety-related defects in motor vehicles and vehicle equipment. For more information on NHTSA investigations, including safety defect investigations, please visit https://www.nhtsa.gov/resources-investigations-recalls.",
-            "title": "Investigations Data",
-            "programCode": [
-                "021:031"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32839,50 +32802,100 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/b3rp-be92/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/b3rp-be92/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/b3rp-be92/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/b3rp-be92/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/b3rp-be92/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/b3rp-be92/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/b3rp-be92/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/b3rp-be92/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/b3rp-be92/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/b3rp-be92",
+            "issued": "2024-02-21",
+            "keyword": [
+                "air bag",
+                "air bags",
+                "auto",
+                "campaign",
+                "car",
+                "cars",
+                "car seat",
+                "child safety seats",
+                "defect",
+                "defects",
+                "email",
+                "equipment",
+                "fmvss",
+                "investigation",
+                "investigations",
+                "office of defect investigations",
+                "potential affected",
+                "recall",
+                "recalls",
+                "safety",
+                "tire",
+                "tires",
+                "vehicles"
+            ],
+            "landingPage": "https://nhtsa.gov/recalls",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "dataQuality": true,
+            "modified": "2025-02-01",
+            "programCode": [
+                "021:031"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Investigations Data"
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
-            "landingPage": "https://data.transportation.gov/d/b4ni-c2as",
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
+            "identifier": "DOT-321",
+            "issued": "2011-01-18",
             "keyword": [
                 "control",
                 "data.gov",
@@ -32893,80 +32906,48 @@
                 "traffic",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "DOT-321",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "NHTSA's issues statements of policy on traffic injury control",
-            "title": "Traffic Injury Control Statements of Policy",
-            "agencyProgramURL": "http://www.nhtsa.gov/About+NHTSA/NHTSA+Electronic+Reading+Room+(ERR)",
+            "landingPage": "https://data.transportation.gov/d/b4ni-c2as",
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
-            "analysisUnit": "Regulated Entity",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4308",
-            "language": [
-                "en-US"
-            ]
+            "title": "Traffic Injury Control Statements of Policy"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://mcmis.volpe.dot.gov/mcs150t/pkg_shipper.prc_shipper_request",
+            "agencyProgramURL": "http://mcmis.volpe.dot.gov/mcs150t/pkg_shipper.prc_shipper_request",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/b5i8-jqb9",
-            "issued": "2015-01-21",
-            "temporal": "R/2015-01-21/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://safer.fmcsa.dot.gov/"
-            ],
-            "keyword": [
-                "hazardous material.",
-                "safer",
-                "shipper verification"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO",
                 "hasEmail": "mailto:fmcsa.cdo@dot.gov"
             },
-            "identifier": "127.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": false,
             "description": "The Shipper Verification of Carrier Hazardous Material Safety Permit (HMSP) function allows HM shippers of hazardous materials registered with FMCSA to check the status of a carrier's permit to transport those materials. The result will indicate whether or not the carrier associated with the USDOT Number entered by the user has a current active HMSP. This function is only available to hazardous material shippers that have registered with FMCSA and have a USDOT number and associated Personal Identification Number (PIN).",
-            "title": "Shipper Verification of Carrier Hazardous Material Safety Permit (HMSP) - Shipper Verification of Carrier Hazardous Material Safety Permit (HMSP)",
-            "agencyProgramURL": "http://mcmis.volpe.dot.gov/mcs150t/pkg_shipper.prc_shipper_request",
-            "primaryITInvestmentUII": "021-000001018",
-            "programCode": [
-                "021:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32975,70 +32956,100 @@
                     "title": "Shipper Verification of Carrier Hazardous Material Safety Permit (HMSP)"
                 }
             ],
-            "spatial": "State, Shipper, National",
-            "dataQuality": false,
+            "identifier": "127.0",
+            "issued": "2015-01-21",
+            "keyword": [
+                "hazardous material.",
+                "safer",
+                "shipper verification"
+            ],
+            "landingPage": "https://data.transportation.gov/d/b5i8-jqb9",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://mcmis.volpe.dot.gov/mcs150t/pkg_shipper.prc_shipper_request",
+            "modified": "2024-05-24",
+            "phone": "202-385-2307",
+            "primaryITInvestmentUII": "021-000001018",
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
+            "spatial": "State, Shipper, National",
+            "temporal": "R/2015-01-21/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "phone": "202-385-2307",
-            "language": [
-                "en-US"
-            ]
+            "title": "Shipper Verification of Carrier Hazardous Material Safety Permit (HMSP) - Shipper Verification of Carrier Hazardous Material Safety Permit (HMSP)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/b5kg-g3e7",
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
-            "identifier": "https://data.transportation.gov/api/views/b5kg-g3e7",
             "description": "Employed persons include people aged 16 years and older in the civilian noninstitutional population who did any work at all as paid employees; worked in their own business, profession, or on their own farm, or worked 15 hours or more as unpaid workers in an enterprise operated by a member of the family; and all those who were not working but who had jobs or businesses from which they were temporarily absent. The Bureau of Labor Statistics produces industry estimates of nonfarm payroll employment as part of the Current Population Survey.",
-            "title": "Transportation Employment - Air Transportation",
+            "identifier": "https://data.transportation.gov/api/views/b5kg-g3e7",
+            "issued": "2025-01-02",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/b5kg-g3e7",
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
+            "title": "Transportation Employment - Air Transportation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "The data system is not publicly available because it is related solely to internal agency management and may contain sensitive data.",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "https://eebacs.fhwa.dot.gov",
+            "agencyProgramURL": "http://flh.fhwa.dot.gov/resources/pse/estimate/",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/b5ma-6sic",
-            "issued": "2014-12-29",
-            "temporal": "R/2014-12-29/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative - Financial",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://flh.fhwa.dot.gov/resources/pse/estimate/guide.htm"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "EEBACS is used to develop engineer's estimates, track projects in the field, prepare contract modifications, evaluate contractor's bids, and track construction progress and cost.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.transportation.gov/mission/data-inventory-not-available",
+                    "mediaType": "text/html"
+                }
             ],
+            "identifier": "701.0",
+            "issued": "2014-12-29",
             "keyword": [
                 "awards",
                 "bidding",
@@ -33050,80 +33061,83 @@
                 "projects",
                 "project tracking"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "701.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "EEBACS is used to develop engineer's estimates, track projects in the field, prepare contract modifications, evaluate contractor's bids, and track construction progress and cost.",
-            "title": "FLH Engineer's Estimate Bidding Award Construction System (EEBACS) -",
-            "agencyProgramURL": "http://flh.fhwa.dot.gov/resources/pse/estimate/",
+            "landingPage": "https://data.transportation.gov/d/b5ma-6sic",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "720-963-3386",
             "primaryITInvestmentUII": "021-122452529",
             "programCode": [
                 "021:009"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.transportation.gov/mission/data-inventory-not-available",
-                    "mediaType": "text/html"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "references": [
+                "http://flh.fhwa.dot.gov/resources/pse/estimate/guide.htm"
             ],
+            "rights": "The data system is not publicly available because it is related solely to internal agency management and may contain sensitive data.",
             "spatial": "National, Project",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "https://eebacs.fhwa.dot.gov",
+            "temporal": "R/2014-12-29/P1D",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "categoryDesignation": "Administrative - Financial",
-            "phone": "720-963-3386",
-            "language": [
-                "en-US"
-            ]
+            "title": "FLH Engineer's Estimate Bidding Award Construction System (EEBACS) -"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/b5mz-4par",
-            "issued": "2023-02-09",
             "@type": "dcat:Dataset",
-            "modified": "2024-02-05",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/b5mz-4par",
+            "issued": "2023-02-09",
+            "landingPage": "https://data.transportation.gov/d/b5mz-4par",
+            "modified": "2024-02-05",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
-            "title": "Motor Vehicle Information by Energy Sources",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "Motor Vehicle Information by Energy Sources"
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
-            "landingPage": "https://data.transportation.gov/d/b5ri-8se6",
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
+            "identifier": "335.1",
+            "isPartOf": "DOT-335",
+            "issued": "2007-10-01",
             "keyword": [
                 "amtrak stations",
                 "grade crossing",
@@ -33139,59 +33153,62 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "335.1",
+            "landingPage": "https://data.transportation.gov/d/b5ri-8se6",
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
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/FLAT_RCL.zip",
+            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
+            "analysisUnit": "Vehicles , Tires, Child Safety Seats, Equipment",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/b6a2-cuwf",
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
+            "identifier": "83.10",
+            "isPartOf": "DOT-83",
+            "issued": "2002-12-16",
             "keyword": [
                 "air bag",
                 "air bags",
@@ -33218,89 +33235,62 @@
                 "vin",
                 "vin search"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "83.10",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Manufacturers who determine that a product or piece of original equipment either has a safety defect or is not in compliance with Federal safety standards are required to notify the National Highway Traffic Safety Administration (NHTSA) within 5 business days. NHTSA requires that manufacturers file a Defect and Noncompliance report as well as quarterly recall status reports, in compliance with Federal Regulation 49 (the National Traffic and Motor Safety Act) Part 573, which identifies the requirements for safety recalls. This information is stored in the NHTSA database. Use this data to search for recall information related to:-\tSpecific NHTSA campaigns -\tProduct types Access to public searches of NHTSA recall databases for tires, vehicles, car seats and equipment.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - Recalls - Tires",
-            "isPartOf": "DOT-83",
-            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
-            "describedByType": "text/plain",
+            "landingPage": "https://data.transportation.gov/d/b6a2-cuwf",
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
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/b6eb-v5km",
-            "issued": "2020-08-14",
             "@type": "dcat:Dataset",
-            "modified": "2021-07-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/b6eb-v5km",
+            "issued": "2020-08-14",
+            "landingPage": "https://data.transportation.gov/d/b6eb-v5km",
+            "modified": "2021-07-08",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
-            "title": "HPMS Samples",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "HPMS Samples"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/b7fw-syb5",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/b7fw-syb5",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "SMT 2 - TOURIST",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33308,45 +33298,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/b7fw-syb5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/b7fw-syb5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/b7fw-syb5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/b7fw-syb5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/b7fw-syb5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/b7fw-syb5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/b7fw-syb5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/b7fw-syb5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/b7fw-syb5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/b7fw-syb5",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/b7fw-syb5",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "SMT 2 - TOURIST"
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
-            "landingPage": "https://data.transportation.gov/d/b7ze-k5u4",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/13dectvt/13dectvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "December 2013"
+                }
             ],
+            "identifier": "18.57",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -33356,60 +33371,61 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.57",
+            "landingPage": "https://data.transportation.gov/d/b7ze-k5u4",
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
-            "title": "Monthly Traffic Volume Trends - December 2013",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/13dectvt/13dectvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "December 2013"
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
+            "title": "Monthly Traffic Volume Trends - December 2013"
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
-            "landingPage": "https://data.transportation.gov/d/b84f-zxwx",
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
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/stateoverview.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Accident/Incident Overview by State/Region"
+                }
             ],
+            "identifier": "214.5",
+            "isPartOf": "DOT-214",
+            "issued": "2010-09-29",
             "keyword": [
                 "accident",
                 "casualty",
@@ -33422,61 +33438,60 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "214.5",
+            "landingPage": "https://data.transportation.gov/d/b84f-zxwx",
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
-            "title": "Highway Rail Accidents - Accident/Incident Overview by State/Region",
-            "isPartOf": "DOT-214",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:000"
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
+            "title": "Highway Rail Accidents - Accident/Incident Overview by State/Region"
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
-            "landingPage": "https://data.transportation.gov/d/b883-sc4u",
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
+                    "downloadURL": "https://cms.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/docs/closedByEnforcement_FY2005_04-26-2013.xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Fiscal Year 2005"
+                }
             ],
+            "identifier": "96.6",
+            "isPartOf": "DOT-96",
+            "issued": "2018-12-17",
             "keyword": [
                 "bus",
                 "civil penalties",
@@ -33489,57 +33504,60 @@
                 "motor carrier",
                 "truck"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "96.6",
+            "landingPage": "https://data.transportation.gov/d/b883-sc4u",
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
-            "title": "Closed Enforcement Cases - Fiscal Year 2005",
-            "isPartOf": "DOT-96",
-            "agencyProgramURL": "http://www.fmcsa.dot.gov/regulations/enforcement/civil-penalties",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://cms.fmcsa.dot.gov/sites/fmcsa.dot.gov/files/docs/closedByEnforcement_FY2005_04-26-2013.xlsx",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "Fiscal Year 2005"
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
+            "title": "Closed Enforcement Cases - Fiscal Year 2005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/b8d7-u7e3",
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
+                    "description": "2011 Arizona HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/arizona2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Arizona"
+                }
+            ],
+            "identifier": "678.4",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -33553,81 +33571,45 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.4",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Arizona",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/b8d7-u7e3",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/arizona2011.zip",
-                    "description": "2011 Arizona HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Arizona"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Arizona"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Contains driver PII and possibly medical test results.",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://ai.fmcsa.dot.gov/CrashStatistics/Default.aspx",
+            "agencyProgramURL": "https://ai.fmcsa.dot.gov/CrashStatistics/Default.aspx",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/b8e5-isfj",
-            "issued": "2015-01-21",
-            "temporal": "R/2015-01-21/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "crash",
-                "crash data",
-                "crash statistics",
-                "fatality analysis reporting system (fars)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO",
                 "hasEmail": "mailto:fmcsa.cdo@dot.gov"
             },
-            "identifier": "93.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": true,
             "description": "Contains data on large trucks and buses involved in Federally reportable crashes as per Title 49 U.S.C. Part 390.5 (crashes involving a commercial motor vehicle, and that either involve a fatalities, injury requiring treatmentaway from the scene of the crash, or a tow-away due to disabling damage).  This information is reported by the States to FMCSA.",
-            "title": "Motor Carrier Crash Data -",
-            "agencyProgramURL": "https://ai.fmcsa.dot.gov/CrashStatistics/Default.aspx",
-            "primaryITInvestmentUII": "021-000001006",
-            "programCode": [
-                "021:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33635,62 +33617,58 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "State Incidents resulting in fatal or non-fatal crashed.",
-            "dataQuality": true,
+            "identifier": "93.0",
+            "issued": "2015-01-21",
+            "keyword": [
+                "crash",
+                "crash data",
+                "crash statistics",
+                "fatality analysis reporting system (fars)"
+            ],
+            "landingPage": "https://data.transportation.gov/d/b8e5-isfj",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "https://ai.fmcsa.dot.gov/CrashStatistics/Default.aspx",
+            "modified": "2024-05-24",
+            "phone": "202-366-4869",
+            "primaryITInvestmentUII": "021-000001006",
+            "programCode": [
+                "021:020"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "rights": "Contains driver PII and possibly medical test results.",
+            "spatial": "State Incidents resulting in fatal or non-fatal crashed.",
+            "temporal": "R/2015-01-21/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4869",
-            "language": [
-                "en-US"
-            ]
+            "title": "Motor Carrier Crash Data -"
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
-            "landingPage": "https://data.transportation.gov/d/b8re-2icq",
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
-            "identifier": "84.3",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "The National Highway Traffic Safety Administration (NHTSA) has the right to investigate reports of defective products. Information about defective products can come from manufacturers, consumers or law enforcement agencies. NHTSA stores defect investigation information in a database. It uses this information to generate monthly defect reports. It also makes this information available to consumers through the NHTSA web site. You can search for defect investigation information for the following product categories: -\tVehicles -\tEquipment -\tChild Restraints -\tTires",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Investigations - 2016 April - Report",
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
@@ -33699,35 +33677,73 @@
                     "title": "2016 April - Report"
                 }
             ],
-            "describedBy": "http://www-odi.nhtsa.dot.gov/downloads/folders/Investigations/INV.txt",
-            "dataQuality": true,
+            "identifier": "84.3",
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
+            "landingPage": "https://data.transportation.gov/d/b8re-2icq",
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
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Investigations - 2016 April - Report"
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
-            "landingPage": "https://data.transportation.gov/d/b8w8-64tt",
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
+                    "downloadURL": "http://www.fra.dot.gov/eLib/Details/L04108",
+                    "mediaType": "text/csv",
+                    "title": "Maintenance of Way Background Survey"
+                }
             ],
+            "identifier": "283.3",
+            "isPartOf": "DOT-283",
+            "issued": "2008-03-01",
             "keyword": [
                 "alertness",
                 "employee",
@@ -33738,61 +33754,60 @@
                 "sleep",
                 "work"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "283.3",
+            "landingPage": "https://data.transportation.gov/d/b8w8-64tt",
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
-            "title": "Work Schedules and Sleep Patterns of Railroad Employees - Maintenance of Way Background Survey",
-            "isPartOf": "DOT-283",
-            "agencyProgramURL": "http://www.fra.dot.gov/Page/P0068",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fra.dot.gov/eLib/Details/L04108",
-                    "mediaType": "text/csv",
-                    "title": "Maintenance of Way Background Survey"
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
+            "title": "Work Schedules and Sleep Patterns of Railroad Employees - Maintenance of Way Background Survey"
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
-            "landingPage": "https://data.transportation.gov/d/b92n-w638",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/05septvt/05septvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "September 2005"
+                }
             ],
+            "identifier": "18.108",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -33802,79 +33817,79 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.108",
+            "landingPage": "https://data.transportation.gov/d/b92n-w638",
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
-            "title": "Monthly Traffic Volume Trends - September 2005",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/05septvt/05septvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "September 2005"
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
+            "title": "Monthly Traffic Volume Trends - September 2005"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/b99s-dekj",
-            "issued": "2021-04-07",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-07",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Chambers",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/b99s-dekj",
+            "issued": "2021-04-07",
+            "landingPage": "https://data.transportation.gov/d/b99s-dekj",
+            "modified": "2024-08-07",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Dry Bulk"
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
-            "landingPage": "https://data.transportation.gov/d/b9ee-emzv",
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
+            "identifier": "130.2",
+            "isPartOf": "DOT-130",
+            "issued": "2009-03-15",
             "keyword": [
                 "authority grated",
                 "compliance review",
@@ -33886,89 +33901,44 @@
                 "safety audit",
                 "violation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "130.2",
+            "landingPage": "https://data.transportation.gov/d/b9ee-emzv",
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
-            "landingPage": "https://data.transportation.gov/d/bagt-569v",
+            "accrualPeriodicity": "R/PT60S",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2012-04-16",
-            "@type": "dcat:Dataset",
-            "temporal": "2011-09-15/2011-11-15",
-            "modified": "2012-04-16",
-            "keyword": [
-                "arterial",
-                "freeway",
-                "incident data",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "loop detector",
-                "occupancy data",
-                "oregon",
-                "portland",
-                "portland oregon test data set",
-                "portland state university (psu)",
-                "sensor data",
-                "transit",
-                "usdot data capture and management program (dcm)",
-                "volume data",
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
-            "identifier": "https://data.transportation.gov/api/views/bagt-569v",
+            "dataQuality": true,
             "description": "This set of data files was acquired under USDOT FHWA cooperative agreement DTFH61-11-H-00025 as one of the four test data sets acquired by the USDOT Data Capture and Management program. This is the primary loop detector data table. It contains one-minute volume, occupancy, and data quality flags for the arterial loop detector data.",
-            "title": "Portland, Oregon Test Data Set Arterial Loop Detector Data",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33976,76 +33946,86 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/bagt-569v/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bagt-569v/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bagt-569v/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/bagt-569v/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bagt-569v/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bagt-569v/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/bagt-569v/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bagt-569v/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bagt-569v/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Portland, Oregon",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/bagt-569v",
+            "issued": "2012-04-16",
+            "keyword": [
+                "arterial",
+                "freeway",
+                "incident data",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "loop detector",
+                "occupancy data",
+                "oregon",
+                "portland",
+                "portland oregon test data set",
+                "portland state university (psu)",
+                "sensor data",
+                "transit",
+                "usdot data capture and management program (dcm)",
+                "volume data",
+                "weather"
+            ],
+            "landingPage": "https://data.transportation.gov/d/bagt-569v",
+            "language": [
+                "en-US"
+            ],
             "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "R/PT60S",
+            "modified": "2012-04-16",
+            "programCode": [
+                "021:013"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
+            "spatial": "Portland, Oregon",
+            "temporal": "2011-09-15/2011-11-15",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Portland, Oregon Test Data Set Arterial Loop Detector Data"
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
-            "landingPage": "https://data.transportation.gov/d/banf-2j89",
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
-            "identifier": "80.4",
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
@@ -34054,35 +34034,70 @@
                     "title": "NHTSA API"
                 }
             ],
-            "spatial": "Zip, State, Geo co-ordinates",
-            "dataQuality": false,
+            "identifier": "80.4",
+            "isPartOf": "DOT-80",
+            "issued": "2010-01-05",
+            "keyword": [
+                "child seat",
+                "inspection",
+                "safety",
+                "station",
+                "stations"
+            ],
+            "landingPage": "https://data.transportation.gov/d/banf-2j89",
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
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/bb59-ke38",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/08aprtvt/08aprtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "April 2008"
+                }
             ],
+            "identifier": "18.77",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -34092,95 +34107,97 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.77",
+            "landingPage": "https://data.transportation.gov/d/bb59-ke38",
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
-            "title": "Monthly Traffic Volume Trends - April 2008",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/08aprtvt/08aprtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "April 2008"
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
+            "title": "Monthly Traffic Volume Trends - April 2008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/bbnn-jurw",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:answers@bts.gov"
+            },
+            "description": "Air taxis include smaller aircraft for commuter and on-demand operations included under FAR Part 135. The National Transportation Safety Board releases aviation fatality data in the Aviation Accident Database.",
+            "identifier": "https://data.transportation.gov/api/views/bbnn-jurw",
             "issued": "2025-01-03",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-03",
             "keyword": [
                 "monthly transportation statistics"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:answers@bts.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/bbnn-jurw",
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
-            "identifier": "https://data.transportation.gov/api/views/bbnn-jurw",
-            "description": "Air taxis include smaller aircraft for commuter and on-demand operations included under FAR Part 135. The National Transportation Safety Board releases aviation fatality data in the Aviation Accident Database.",
-            "title": "Air Taxi and Commuter Fatalities",
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
+            "title": "Air Taxi and Commuter Fatalities"
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
-            "landingPage": "https://data.transportation.gov/d/bc4v-auvx",
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
+                    "mediaType": "application/xml",
+                    "title": "NHTSA API"
+                }
             ],
+            "identifier": "83.3",
+            "isPartOf": "DOT-83",
+            "issued": "2002-12-16",
             "keyword": [
                 "air bag",
                 "air bags",
@@ -34207,58 +34224,45 @@
                 "vin",
                 "vin search"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "83.3",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Manufacturers who determine that a product or piece of original equipment either has a safety defect or is not in compliance with Federal safety standards are required to notify the National Highway Traffic Safety Administration (NHTSA) within 5 business days. NHTSA requires that manufacturers file a Defect and Noncompliance report as well as quarterly recall status reports, in compliance with Federal Regulation 49 (the National Traffic and Motor Safety Act) Part 573, which identifies the requirements for safety recalls. This information is stored in the NHTSA database. Use this data to search for recall information related to:-\tSpecific NHTSA campaigns -\tProduct types Access to public searches of NHTSA recall databases for tires, vehicles, car seats and equipment.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - NHTSA API",
-            "isPartOf": "DOT-83",
-            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
-            "describedByType": "text/plain",
+            "landingPage": "https://data.transportation.gov/d/bc4v-auvx",
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
-                    "mediaType": "application/xml",
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
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/bcyt-rqmu",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Transportation Analysis",
+                "hasEmail": "mailto:long.nguyen@dot.gov"
+            },
+            "description": "Freight Facts and Figures - Moving Goods in the United States",
+            "identifier": "https://data.transportation.gov/api/views/bcyt-rqmu",
             "issued": "2019-07-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-09",
             "keyword": [
                 "bts",
                 "bureau of transportation statistics",
@@ -34268,39 +34272,50 @@
                 "freight facts & figures",
                 "freight transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Transportation Analysis",
-                "hasEmail": "mailto:long.nguyen@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/bcyt-rqmu",
+            "modified": "2024-12-09",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statisitics"
             },
-            "identifier": "https://data.transportation.gov/api/views/bcyt-rqmu",
-            "description": "Freight Facts and Figures - Moving Goods in the United States",
-            "title": "Moving Goods in the United States",
-            "programCode": [
-                "021:053"
-            ],
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Moving Goods in the United States"
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
-            "landingPage": "https://data.transportation.gov/d/bd8j-bttr",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/07febtvt/07febtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "February 2007"
+                }
             ],
+            "identifier": "18.91",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -34310,55 +34325,45 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.91",
+            "landingPage": "https://data.transportation.gov/d/bd8j-bttr",
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
-            "title": "Monthly Traffic Volume Trends - February 2007",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/07febtvt/07febtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "February 2007"
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
+            "title": "Monthly Traffic Volume Trends - February 2007"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/bda5-32at",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This report contains data for highway-rail grade crossing incidents, fatalities and injuries, with the ability to display the data by highway user, state, county, city, railroad, or warning device (e.g. gates, crossbucks, etc.).",
+            "identifier": "https://data.transportation.gov/api/views/bda5-32at",
             "issued": "2023-08-04",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "fatalities",
                 "grade crossing incident",
@@ -34367,43 +34372,53 @@
                 "incidents",
                 "injuries"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/bda5-32at",
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
-            "identifier": "https://data.transportation.gov/api/views/bda5-32at",
-            "description": "This report contains data for highway-rail grade crossing incidents, fatalities and injuries, with the ability to display the data by highway user, state, county, city, railroad, or warning device (e.g. gates, crossbucks, etc.).",
-            "title": "Highway-Rail Grade Crossing Incidents, Fatalities and Injuries (2.08)",
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
+            "title": "Highway-Rail Grade Crossing Incidents, Fatalities and Injuries (2.08)"
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
-            "landingPage": "https://data.transportation.gov/d/beat-px3g",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12jantvt/12jantvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "January 2012"
+                }
             ],
+            "identifier": "18.2",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -34413,60 +34428,60 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.2",
+            "landingPage": "https://data.transportation.gov/d/beat-px3g",
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
-            "title": "Monthly Traffic Volume Trends - January 2012",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12jantvt/12jantvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "January 2012"
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
+            "title": "Monthly Traffic Volume Trends - January 2012"
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
-            "landingPage": "https://data.transportation.gov/d/bevm-n7d2",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/10febtvt/10febtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "February 2010"
+                }
             ],
+            "identifier": "18.25",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -34476,80 +34491,48 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.25",
+            "landingPage": "https://data.transportation.gov/d/bevm-n7d2",
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
-            "title": "Monthly Traffic Volume Trends - February 2010",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/10febtvt/10febtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "February 2010"
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
+            "title": "Monthly Traffic Volume Trends - February 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "The data system is not publicly available because it is related solely to internal agency management and may contain sensitive data.",
+            "accrualPeriodicity": "R/P3M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/research/tfhrc/projects/projectsdb/",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/research/tfhrc/",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/bew3-4v36",
-            "issued": "2011-05-01",
-            "temporal": "R/2011-05-01/P3M",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
-            "keyword": [
-                "projects",
-                "research",
-                "status"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "708.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "This system will produce reports to enable FHWA to better and more effectively manage R&D projects on cost, schedule and performance criteria. It will also allow Turner Fairbank Highway Research center managers to more efficiently respond to data calls from internal and external sources (such as TRB and NSF) regarding the research that is performed at TFHRC.",
-            "title": "RD&T Project Management Support System (PMSS) -",
-            "primaryITInvestmentUII": "021-295717044",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/research/tfhrc/",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34557,33 +34540,65 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "National, Project",
-            "dataQuality": true,
+            "identifier": "708.0",
+            "issued": "2011-05-01",
+            "keyword": [
+                "projects",
+                "research",
+                "status"
+            ],
+            "landingPage": "https://data.transportation.gov/d/bew3-4v36",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "primaryITInvestmentUII": "021-295717044",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "rights": "The data system is not publicly available because it is related solely to internal agency management and may contain sensitive data.",
+            "spatial": "National, Project",
+            "temporal": "R/2011-05-01/P3M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P3M",
-            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/research/tfhrc/projects/projectsdb/",
-            "categoryDesignation": "Research",
-            "language": [
-                "en-US"
-            ]
+            "title": "RD&T Project Management Support System (PMSS) -"
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
-            "landingPage": "https://data.transportation.gov/d/bexm-uqye",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/14aprtvt/14aprtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "April 2014"
+                }
             ],
+            "identifier": "18.61",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -34593,60 +34608,59 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.61",
+            "landingPage": "https://data.transportation.gov/d/bexm-uqye",
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
-            "title": "Monthly Traffic Volume Trends - April 2014",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/14aprtvt/14aprtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "April 2014"
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
+            "title": "Monthly Traffic Volume Trends - April 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.nhtsa.gov/nti/811841",
+            "agencyProgramURL": "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/National+Telephone+Surveys",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/bezd-gez6",
-            "issued": "2013-10-31",
-            "temporal": "2012-07-12/2012-11-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.nhtsa.gov/nti/811841"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": false,
+            "description": "Information from the public to ascertain the current frequency and characteristics of bicyclist and pedestrian activity, and identify deterrents to bicycling and walking. The data will also be compared to data collected by a previous NHTSA survey, conducted in 2002, to determine if major changes have occurred over that 10-year span. The information will be used to help update and refine safety programs. A national telephone survey will be administered to 9,000 randomly selected respondents 16 and older drawn from all 50 States and the District of Columbia. The survey will ask about the characteristics of bicycling and walking trips, conspicuity, community design for bicycling and walking, bicycle helmet use, and general opinions about bicycling and walking. Interview length will average 20 minutes.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.nhtsa.gov/staticfiles/nti/other/2012survey/BikePed-Data_revFINAL2.csv",
+                    "mediaType": "text/csv",
+                    "title": "2012 Survey"
+                }
             ],
+            "identifier": "415.1",
+            "isPartOf": "DOT-415",
+            "issued": "2013-10-31",
             "keyword": [
                 "activity",
                 "attitude",
@@ -34658,74 +34672,41 @@
                 "knowledge",
                 "pedestrian"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "415.1",
+            "landingPage": "https://data.transportation.gov/d/bezd-gez6",
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
-            "description": "Information from the public to ascertain the current frequency and characteristics of bicyclist and pedestrian activity, and identify deterrents to bicycling and walking. The data will also be compared to data collected by a previous NHTSA survey, conducted in 2002, to determine if major changes have occurred over that 10-year span. The information will be used to help update and refine safety programs. A national telephone survey will be administered to 9,000 randomly selected respondents 16 and older drawn from all 50 States and the District of Columbia. The survey will ask about the characteristics of bicycling and walking trips, conspicuity, community design for bicycling and walking, bicycle helmet use, and general opinions about bicycling and walking. Interview length will average 20 minutes.",
-            "title": "National Survey of Pedestrian and Bicyclist Attitudes, Knowledge, and Behaviors - 2012 Survey",
-            "isPartOf": "DOT-415",
-            "agencyProgramURL": "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/National+Telephone+Surveys",
-            "programCode": [
-                "021:032"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.nhtsa.gov/staticfiles/nti/other/2012survey/BikePed-Data_revFINAL2.csv",
-                    "mediaType": "text/csv",
-                    "title": "2012 Survey"
-                }
+            "references": [
+                "http://www.nhtsa.gov/nti/811841"
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.nhtsa.gov/nti/811841",
+            "temporal": "2012-07-12/2012-11-18",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "phone": "202-366-6401",
-            "language": [
-                "en-US"
-            ]
+            "title": "National Survey of Pedestrian and Bicyclist Attitudes, Knowledge, and Behaviors - 2012 Survey"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://catalog.data.faa.gov/dataset/56-day-complete-set-of-all-of-the-digital-enroute-charts---aeronautical-information-servic",
             "bureauCode": [
                 "021:12"
             ],
-            "issued": "2020-11-14",
-            "@type": "dcat:Dataset",
-            "modified": "2021-11-09",
-            "keyword": [
-                "altitude",
-                "digital-chart",
-                "enroute"
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
-            "identifier": "3ec9a4a2-c653-460b-b812-90ded2fbe093",
             "description": "The following ZIP files contain all of the Digital Enroute charts, except for Caribbean charts, for a given effective date range. Due to the large file sizes, it is best to download one zip file at a time using a broadband internet connection during off-peak internet hours. Each zip file contains multiple zip files each of which contain a mixture of PDF and HTML files.",
-            "title": "56-Day Complete Set of all of the Digital Enroute Charts - Aeronautical Information Services Digital Products",
-            "primaryITInvestmentUII": "021-129509270",
-            "programCode": [
-                "021:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34734,49 +34715,49 @@
                     "title": "Aeronautical Information Services Digital Products"
                 }
             ],
-            "systemOfRecords": "https://www.govinfo.gov/content/pkg/FR-2016-08-15/pdf/2016-19354.pdf",
+            "identifier": "3ec9a4a2-c653-460b-b812-90ded2fbe093",
+            "issued": "2020-11-14",
+            "keyword": [
+                "altitude",
+                "digital-chart",
+                "enroute"
+            ],
+            "landingPage": "https://catalog.data.faa.gov/dataset/56-day-complete-set-of-all-of-the-digital-enroute-charts---aeronautical-information-servic",
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
+            "title": "56-Day Complete Set of all of the Digital Enroute Charts - Aeronautical Information Services Digital Products"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Contains FMCSA system design and documentation.",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/bhb5-ai78",
-            "issued": "2018-12-18",
-            "temporal": "R/2013/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-31",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "data",
-                "entity",
-                "management",
-                "relationship"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO",
                 "hasEmail": "mailto:fmcsa.cdo@dot.gov"
             },
-            "identifier": "1642.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": false,
             "description": "FMCSA Data management team server. Allows viewing/collaboration of entity relation diagram.",
-            "title": "Embarcadero Connect -",
-            "primaryITInvestmentUII": "021-000001000",
-            "programCode": [
-                "021:027"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34784,32 +34765,66 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "1642.0",
+            "issued": "2018-12-18",
+            "keyword": [
+                "data",
+                "entity",
+                "management",
+                "relationship"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/bhb5-ai78",
             "language": [
                 "en-US"
             ],
-            "phone": "202-493-0215"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-31",
+            "phone": "202-493-0215",
+            "primaryITInvestmentUII": "021-000001000",
+            "programCode": [
+                "021:027"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "rights": "Contains FMCSA system design and documentation.",
+            "temporal": "R/2013/P1Y",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Embarcadero Connect -"
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
-            "landingPage": "https://data.transportation.gov/d/biqg-knxr",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/07jultvt/07jultvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "July 2007"
+                }
             ],
+            "identifier": "18.86",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -34819,78 +34834,49 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.86",
+            "landingPage": "https://data.transportation.gov/d/biqg-knxr",
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
-            "title": "Monthly Traffic Volume Trends - July 2007",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/07jultvt/07jultvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "July 2007"
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
+            "title": "Monthly Traffic Volume Trends - July 2007"
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
-            "landingPage": "https://data.transportation.gov/d/biwa-ffs3",
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
-            "identifier": "102.1",
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
@@ -34899,30 +34885,49 @@
                     "title": "Online Form"
                 }
             ],
-            "spatial": "State",
-            "dataQuality": true,
+            "identifier": "102.1",
+            "isPartOf": "DOT-102",
+            "issued": "1974-06-01",
+            "keyword": [
+                "carrier",
+                "registration"
+            ],
+            "landingPage": "https://data.transportation.gov/d/biwa-ffs3",
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
-            "landingPage": "https://data.transportation.gov/d/bjuv-4sxp",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRA Safety Data Team",
+                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This is the page for Accident Cause by Railroad.",
+            "identifier": "https://data.transportation.gov/api/views/bjuv-4sxp",
             "issued": "2024-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "collision",
                 "derailment",
@@ -34930,48 +34935,33 @@
                 "train",
                 "train accident"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRA Safety Data Team",
-                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/bjuv-4sxp",
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
-            "identifier": "https://data.transportation.gov/api/views/bjuv-4sxp",
-            "description": "This is the page for Accident Cause by Railroad.",
-            "title": "Accident Cause by Railroad",
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
+            "title": "Accident Cause by Railroad"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/bk7f-yqs4",
-            "issued": "2022-05-20",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/bk7f-yqs4",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "Trespassers",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34979,102 +34969,128 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/bk7f-yqs4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bk7f-yqs4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bk7f-yqs4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/bk7f-yqs4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bk7f-yqs4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bk7f-yqs4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/bk7f-yqs4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bk7f-yqs4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bk7f-yqs4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/bk7f-yqs4",
+            "issued": "2022-05-20",
+            "landingPage": "https://data.transportation.gov/d/bk7f-yqs4",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Trespassers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/bk9e-kthi",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "Reports for highway rail crossing inventory can be found within this portal. A highway-rail crossing is a location where a public highway, road, street, or private roadway, including associated sidewalks and pathways, crosses one or more railroad tracks. All such crossings are reported by railroads and state Department of Transportations to the FRA on Form FRA F 6180.71 U.S. DOT Crossing Inventory Form.",
+            "identifier": "https://data.transportation.gov/api/views/bk9e-kthi",
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
+            "landingPage": "https://data.transportation.gov/d/bk9e-kthi",
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
-            "identifier": "https://data.transportation.gov/api/views/bk9e-kthi",
-            "description": "Reports for highway rail crossing inventory can be found within this portal. A highway-rail crossing is a location where a public highway, road, street, or private roadway, including associated sidewalks and pathways, crosses one or more railroad tracks. All such crossings are reported by railroads and state Department of Transportations to the FRA on Form FRA F 6180.71 U.S. DOT Crossing Inventory Form.",
-            "title": "Crossing Inventory - Landing Page",
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
+            "title": "Crossing Inventory - Landing Page"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/bk9z-wp56",
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
             "identifier": "https://data.transportation.gov/api/views/bk9z-wp56",
+            "issued": "2021-01-21",
+            "landingPage": "https://data.transportation.gov/d/bk9z-wp56",
+            "modified": "2021-01-21",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Border Crossing"
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
-            "landingPage": "https://data.transportation.gov/d/bkgp-28p3",
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
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/inctally2.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Train Accident Rates"
+                }
             ],
+            "identifier": "199.9",
+            "isPartOf": "DOT-199",
+            "issued": "2010-09-29",
             "keyword": [
                 "acts of god",
                 "collisions",
@@ -35085,85 +35101,44 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "199.9",
+            "landingPage": "https://data.transportation.gov/d/bkgp-28p3",
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
-            "title": "Rail Equipment Accidents - Train Accident Rates",
-            "isPartOf": "DOT-199",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:036"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/inctally2.aspx",
-                    "mediaType": "text/csv",
-                    "title": "Train Accident Rates"
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
+            "title": "Rail Equipment Accidents - Train Accident Rates"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/bkh6-tj42",
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
-                "fares",
-                "highest",
-                "lowest",
-                "markets under 750 miles",
-                "office of aviation analysis",
-                "table 5"
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
-            "identifier": "https://data.transportation.gov/api/views/bkh6-tj42",
+            "dataQuality": true,
             "description": "Provides detailed fare information for highest and lowest fare markets under 750 miles. For a more complete explanation, please read the introductory information at the beginning of Table 5 itself in the report (https://www.transportation.gov/office-policy/aviation-policy/domestic-airline-consumer-airfare-report-pdf).",
-            "title": "Consumer Airfare Report: Table 5 - Detailed Fare Information For Highest and Lowest Fare Markets Under 750 Miles",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35171,58 +35146,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/bkh6-tj42/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bkh6-tj42/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bkh6-tj42/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/bkh6-tj42/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bkh6-tj42/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bkh6-tj42/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/bkh6-tj42/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bkh6-tj42/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bkh6-tj42/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/bkh6-tj42",
+            "issued": "2017-10-31",
+            "keyword": [
+                "airfares",
+                "aviation",
+                "aviation policy",
+                "city pair",
+                "consumer airfare report",
+                "fare levels",
+                "fares",
+                "highest",
+                "lowest",
+                "markets under 750 miles",
+                "office of aviation analysis",
+                "table 5"
+            ],
+            "landingPage": "https://data.transportation.gov/d/bkh6-tj42",
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
+            "title": "Consumer Airfare Report: Table 5 - Detailed Fare Information For Highest and Lowest Fare Markets Under 750 Miles"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/bm4c-faz3",
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
-            "identifier": "https://data.transportation.gov/api/views/bm4c-faz3",
+            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
             "description": "State DOTs provide the location limits of highway sections to be used to represent statewide aggregations based on a statistically valid Sample Panel.\nThe North contains data for the following States: Maine, New Hampshire, Vermont, New York, Massachusetts, Rhode Island, Connecticut, New Jersey, Pennsylvania, Ohio, Maryland, District of Columbia, and Delaware.",
-            "title": "Roadway Sections North 2018",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35230,74 +35218,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/bm4c-faz3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bm4c-faz3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bm4c-faz3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/bm4c-faz3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bm4c-faz3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bm4c-faz3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/bm4c-faz3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bm4c-faz3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bm4c-faz3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "USA",
-            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
+            "identifier": "https://data.transportation.gov/api/views/bm4c-faz3",
+            "issued": "2021-01-05",
+            "landingPage": "https://data.transportation.gov/d/bm4c-faz3",
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
+            "title": "Roadway Sections North 2018"
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
-            "landingPage": "https://data.transportation.gov/d/bmnd-knki",
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
-            "identifier": "664.2",
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
@@ -35306,40 +35288,48 @@
                     "title": "Online Tool"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "https://gradedec.fra.dot.gov/",
-            "dataQuality": true,
+            "identifier": "664.2",
+            "isPartOf": "DOT-664",
+            "issued": "2014-11-21",
+            "keyword": [
+                "fra system for highway-rail grade crossing",
+                "gade crossing invetment analysis"
+            ],
+            "landingPage": "https://data.transportation.gov/d/bmnd-knki",
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
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/bmqt-qydn",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/bmqt-qydn",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "SMT 2 - RJ CORMAN",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35347,45 +35337,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/bmqt-qydn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bmqt-qydn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bmqt-qydn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/bmqt-qydn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bmqt-qydn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bmqt-qydn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/bmqt-qydn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bmqt-qydn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bmqt-qydn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/bmqt-qydn",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/bmqt-qydn",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "SMT 2 - RJ CORMAN"
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
-            "landingPage": "https://data.transportation.gov/d/bng9-s6vh",
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
+            "identifier": "285.1",
+            "isPartOf": "DOT-285",
+            "issued": "1990-01-01",
             "keyword": [
                 "axle load",
                 "carried load",
@@ -35401,61 +35417,61 @@
                 "weight-in-motion",
                 "wim"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "285.1",
+            "landingPage": "https://data.transportation.gov/d/bng9-s6vh",
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
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/",
+            "agencyProgramURL": "http://www.ops.fhwa.dot.gov/freight/freight_analysis/faf/",
+            "analysisUnit": "Region",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/bnny-mkab",
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
+            "identifier": "286.4",
+            "isPartOf": "DOT-286",
+            "issued": "2013-03-20",
             "keyword": [
                 "commodity",
                 "consumption",
@@ -35480,74 +35496,43 @@
                 "value",
                 "wear"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "286.4",
+            "landingPage": "https://data.transportation.gov/d/bnny-mkab",
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
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/bpg8-byn2",
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
-            "identifier": "https://data.transportation.gov/api/views/bpg8-byn2",
+            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
             "description": "This data is the road section attribute data for HPMS. The HPMS Field Manual and HPMS 8.0 identifies a record by its Data Item. This data contains approximately 70 data items that is linked to ARNOLD through a Dynamic Segmentation process using the linear referencing components. Table 4.2 contains a list of the current Data Items.",
-            "title": "Roadway Samples 2019",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35555,72 +35540,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/bpg8-byn2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bpg8-byn2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bpg8-byn2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/bpg8-byn2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bpg8-byn2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bpg8-byn2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/bpg8-byn2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bpg8-byn2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bpg8-byn2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "USA",
-            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
+            "identifier": "https://data.transportation.gov/api/views/bpg8-byn2",
+            "issued": "2020-12-28",
+            "landingPage": "https://data.transportation.gov/d/bpg8-byn2",
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
+            "title": "Roadway Samples 2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Data document agency grant award decisions prior to obligation of funds. Once obligation is completed, data are available through USASpending.",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/bpi2-hspm",
-            "issued": "2014-09-16",
-            "temporal": "2014-09-16/2014-09-16",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Federal Government Finances and Employment",
-            "keyword": [
-                "award",
-                "congress",
-                "congressional",
-                "grants",
-                "notification"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "433.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
             "description": "This data set contains information on Congressional members, staff, and committees that must be notified about DOT discretionary grant awards. Data also include summary information about awards, including: project name, place of performance, amount, and a brief abstract of the project.",
-            "title": "Grants Notification Data -",
-            "primaryITInvestmentUII": "021-457554813",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35628,65 +35608,103 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "theme": [
-                "Federal Government Finances and Employment"
+            "identifier": "433.0",
+            "issued": "2014-09-16",
+            "keyword": [
+                "award",
+                "congress",
+                "congressional",
+                "grants",
+                "notification"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Administrative",
+            "landingPage": "https://data.transportation.gov/d/bpi2-hspm",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-5696"
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-14",
+            "phone": "202-366-5696",
+            "primaryITInvestmentUII": "021-457554813",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "rights": "Data document agency grant award decisions prior to obligation of funds. Once obligation is completed, data are available through USASpending.",
+            "temporal": "2014-09-16/2014-09-16",
+            "theme": [
+                "Federal Government Finances and Employment"
+            ],
+            "title": "Grants Notification Data -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/bpj8-8amm",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Transportation cost burden concepts and definitions and how they are related to equity.",
+            "identifier": "https://data.transportation.gov/api/views/bpj8-8amm",
             "issued": "2023-09-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
             "keyword": [
                 "income quintiles",
                 "transportation",
                 "transportation cost",
                 "transportation spend"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/bpj8-8amm",
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
-            "identifier": "https://data.transportation.gov/api/views/bpj8-8amm",
-            "description": "Transportation cost burden concepts and definitions and how they are related to equity.",
-            "title": "Transportation Cost Burden: Concepts",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Transportation Cost Burden: Concepts"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/bpmp-revw",
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
+                    "description": "2011 Alabama HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/alabama2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Alabama"
+                }
+            ],
+            "identifier": "678.2",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -35700,57 +35718,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Alabama",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/bpmp-revw",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/alabama2011.zip",
-                    "description": "2011 Alabama HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Alabama"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Alabama"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
             "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
-            "categoryDesignation": "Administrative",
-            "language": [
-                "en-US"
+            "bureauCode": [
+                "021:15"
             ],
-            "phone": "202-366-5035"
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
+                    "description": "2012 Michigan HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/michigan2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Michigan"
+                }
             ],
-            "landingPage": "https://data.transportation.gov/d/bppr-3tnr",
+            "identifier": "678.76",
+            "isPartOf": "DOT-678",
             "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
-            "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
             "keyword": [
                 "aadt",
                 "condition",
@@ -35764,70 +35782,41 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.76",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Michigan",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/bppr-3tnr",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/michigan2012.zip",
-                    "description": "2012 Michigan HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Michigan"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Michigan"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://data.transportation.gov/d/bpqk-hyst",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2020-08-07",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-30",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Todd Solomon",
                 "hasEmail": "mailto:todd.solomon@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/bpqk-hyst",
+            "dataQuality": true,
             "description": "Number of commercial aviation departures, domestic and international, by day. Also the number of people screened by TSA in total and at large hub airports by day.",
-            "title": "Commercial Aviation Departures",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35835,47 +35824,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/bpqk-hyst/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bpqk-hyst/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bpqk-hyst/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/bpqk-hyst/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bpqk-hyst/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bpqk-hyst/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/bpqk-hyst/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bpqk-hyst/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bpqk-hyst/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/bpqk-hyst",
+            "issued": "2020-08-07",
+            "landingPage": "https://data.transportation.gov/d/bpqk-hyst",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1W",
+            "modified": "2022-03-30",
+            "phone": "2023660573",
+            "programCode": [
+                "021:053"
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
+            "title": "Commercial Aviation Departures"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/bpqs-dpf8",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRA Safety Data Team",
+                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This is the landing page for rail safety overview reports, which contain summary-level data about train accidents, highway-rail accidents, casualties and operational data.",
+            "identifier": "https://data.transportation.gov/api/views/bpqs-dpf8",
             "issued": "2024-12-11",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "highway-rail",
                 "operational",
@@ -35884,59 +35889,40 @@
                 "railroad safety",
                 "train accident"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRA Safety Data Team",
-                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/bpqs-dpf8",
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
-            "identifier": "https://data.transportation.gov/api/views/bpqs-dpf8",
-            "description": "This is the landing page for rail safety overview reports, which contain summary-level data about train accidents, highway-rail accidents, casualties and operational data.",
-            "title": "Overview Reports Landing Page",
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
+            "title": "Overview Reports Landing Page"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://data.transportation.gov/d/bpzg-ctjr",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2014-09-24",
-            "temporal": "R/2014-09-24/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "modified": "2024-11-14",
-            "keyword": [
-                "directives"
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
-            "identifier": "456.0",
+            "dataQuality": false,
             "description": "This data set contains information about Departmental directives, to include publication number, publication date, title, responsible office, and key words.",
-            "title": "Departmental Directives Tracking -",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35944,32 +35930,62 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
+            "identifier": "456.0",
+            "issued": "2014-09-24",
+            "keyword": [
+                "directives"
+            ],
+            "landingPage": "https://data.transportation.gov/d/bpzg-ctjr",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-11-14",
+            "phone": "202-366-4309",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "temporal": "R/2014-09-24/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "categoryDesignation": "Research",
-            "phone": "202-366-4309",
-            "language": [
-                "en-US"
-            ]
+            "title": "Departmental Directives Tracking -"
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
-            "landingPage": "https://data.transportation.gov/d/bqud-7rbb",
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
+                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/nits/Noncrash%20injuries/2011-2012/2011-2012%20Noncrash%20Injujries.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2011-2012 Noncrash Injuries"
+                }
             ],
+            "identifier": "288.11",
+            "isPartOf": "DOT-288",
+            "issued": "2009-01-27",
             "keyword": [
                 "crash",
                 "death",
@@ -35985,74 +36001,42 @@
                 "vehicle",
                 "victim"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "288.11",
+            "landingPage": "https://data.transportation.gov/d/bqud-7rbb",
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
-            "title": "Not in Traffic Surveillance (NiTS) - 2011-2012 Noncrash Injuries",
-            "isPartOf": "DOT-288",
-            "agencyProgramURL": "http://www.nhtsa.gov/Data/State+Data+Programs",
-            "programCode": [
-                "021:032"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/nits/Noncrash%20injuries/2011-2012/2011-2012%20Noncrash%20Injujries.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "2011-2012 Noncrash Injuries"
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
+            "title": "Not in Traffic Surveillance (NiTS) - 2011-2012 Noncrash Injuries"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://data.transportation.gov/d/bqx9-a7yw",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-01-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-20",
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
-            "identifier": "https://data.transportation.gov/api/views/bqx9-a7yw",
             "description": "",
-            "title": "Pocket Guide to Transportation-Passenger Miles Traveled",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36060,60 +36044,57 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/bqx9-a7yw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bqx9-a7yw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bqx9-a7yw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/bqx9-a7yw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bqx9-a7yw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bqx9-a7yw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/bqx9-a7yw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bqx9-a7yw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bqx9-a7yw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "https://data.transportation.gov/api/views/bqx9-a7yw",
+            "issued": "2024-01-28",
+            "keyword": [
+                "pocket guide to transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/bqx9-a7yw",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-20",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Pocket Guide to Transportation-Passenger Miles Traveled"
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
-            "identifier": "https://data.transportation.gov/api/views/brry-xrw9",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 2002",
-            "title": "Historic HPMS Data (Universe) - 2002",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36121,72 +36102,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/brry-xrw9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/brry-xrw9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/brry-xrw9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/brry-xrw9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/brry-xrw9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/brry-xrw9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/brry-xrw9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/brry-xrw9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/brry-xrw9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/brry-xrw9",
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
+            "title": "Historic HPMS Data (Universe) - 2002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/brzy-6zfh",
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
-            "identifier": "https://data.transportation.gov/api/views/brzy-6zfh",
             "description": "The main dataset is a 350 MB file of trajectory data (TGSIM-Foggy Bottom-Data.csv) that contains position, speed, and acceleration data for pedestrians, bicycles, scooters, non-automated passenger cars, automated vehicles, motorcycles, buses, and trucks in an urban environment. Supporting files include an aerial reference image (Reference_Image_Foggy Bottom.png) and a list of polygon boundaries (Foggy_Bottom_boundaries.txt) and associated images (i1.png, i2.png, \u2026, i49.png stored in the folder titled \u201cAnnotation on Regions.zip\u201d) to map physical roadway segments to numerical IDs (as referenced in the trajectory dataset). \n\nThis dataset was collected as part of the Third Generation Simulation Data (TGSIM): A Closer Look at the Impacts of Automated Driving Systems on Human Behavior project. During the project, six trajectory datasets capable of characterizing human-automated vehicle interactions under a diverse set of scenarios in highway and city environments were collected and processed. For more information, see the project report found here: https://rosap.ntl.bts.gov/view/dot/74647. This dataset, which is one of the six collected as part of the TGSIM project, contains data collected from twelve 4K stationary infrastructure cameras installed in the Foggy Bottom neighborhood of Washington, D.C. The cameras captured four intersections, adjacent crosswalks, road segments between the intersections, and partial road segments extending out from the intersections totaling more than one full block of coverage. These segments are represented by polygons to bound travel lanes, parking lanes, crosswalks, and intersections for detection and analysis purposes (see Reference_Image_Foggy Bottom.png for details). The cameras captured continuous footage during a weekday commute between 3:00PM-5:00PM ET on a sunny day. During this period, one test vehicle equipped with SAE Level 3 automation was deployed to perform various complex maneuvers at both stop signs and traffic signals, including both protected and permitted left turns, to capture human driving behaviors when interacting with automated vehicles. The automated vehicles are indicated in the dataset.\n\nAs part of this dataset, the following files were provided:\n<ul><li>TGSIM-Foggy Bottom-Data.csv contains the numerical data to be used for analysis that includes vehicle/bicycle/pedestrian trajectory data at every 0.1 second. Road user type, width, and length are provided with instantaneous location, speed, and acceleration data. All distance measurements (width, length, location) were converted from pixels to meters using the following conversion factor: 1 pixel = 0.0186613838586-meter conversion.</li>\n<li>Reference_Image_Foggy Bottom.png is the aerial reference image that defines the geographic region and the associated roadway segments.</li>\t\n<li>Foggy_Bottom_boundaries.txt contains the coordinates that define the roadway segments (n = 49). Each polygon is a list of four to six coordinate pairs measured in pixels (which can be converted to meters using the provided 1 pixel = 0.0186613838586-meter conversion), with (0,0) global reference coordinates at the top-left of the reference image.</li>\n<li>Annotation on Regions.zip, which includes i1.png, i2.png,..., i49.png, are images that visually map the road segment IDs (indicated by the number following the i in the file name) to the reference image.</li></ul>",
-            "title": "Third Generation Simulation Data (TGSIM) Foggy Bottom Trajectories",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36194,66 +36169,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/brzy-6zfh/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/brzy-6zfh/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/brzy-6zfh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/brzy-6zfh/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/brzy-6zfh/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/brzy-6zfh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/brzy-6zfh/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/brzy-6zfh/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/brzy-6zfh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "I-90/I94 in Chicago, IL; I-294 near Hinsdale, IL; I-395 in Washington DC; George Washington University Campus, Washington DC (Foggy Bottom)",
+            "identifier": "https://data.transportation.gov/api/views/brzy-6zfh",
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
+            "landingPage": "https://data.transportation.gov/d/brzy-6zfh",
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
+            "title": "Third Generation Simulation Data (TGSIM) Foggy Bottom Trajectories"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/btpt-uxhx",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2020-09-01",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-25",
-            "keyword": [
-                "border crossing",
-                "freight",
-                "frieight trucking",
-                "inbound border crossing entries",
-                "passengers",
-                "personal vehicles",
-                "trucks"
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
-            "identifier": "https://data.transportation.gov/api/views/btpt-uxhx",
             "description": "Number of passenger vehicles crossing into the United States via Canada and Mexico, and number of freight trucks crossing into U.S. via Niagara Falls.",
-            "title": "Vehicles Entering U.S. by Country",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36261,51 +36240,88 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/btpt-uxhx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/btpt-uxhx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/btpt-uxhx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/btpt-uxhx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/btpt-uxhx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/btpt-uxhx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/btpt-uxhx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/btpt-uxhx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/btpt-uxhx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/btpt-uxhx",
+            "issued": "2020-09-01",
+            "keyword": [
+                "border crossing",
+                "freight",
+                "frieight trucking",
+                "inbound border crossing entries",
+                "passengers",
+                "personal vehicles",
+                "trucks"
+            ],
+            "landingPage": "https://data.transportation.gov/d/btpt-uxhx",
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
                 "Roadways and Bridges"
             ],
-            "phone": "2023660573",
-            "language": [
-                "en-US"
-            ]
+            "title": "Vehicles Entering U.S. by Country"
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
-            "landingPage": "https://data.transportation.gov/d/btpw-ru7c",
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
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/pubs/MonthlyData/December%202015%20Raw%20Database.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "December 2015 Raw Data"
+                }
             ],
+            "identifier": "19.5",
+            "isPartOf": "DOT-19",
+            "issued": "2011-10-07",
             "keyword": [
                 "boardings",
                 "bus",
@@ -36315,77 +36331,42 @@
                 "train",
                 "transit"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John D. Giorgis",
-                "hasEmail": "mailto:john.giorgis@dot.gov"
-            },
-            "identifier": "19.5",
+            "landingPage": "https://data.transportation.gov/d/btpw-ru7c",
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
-            "title": "NTD Monthly Module Data Set - December 2015 Raw Data",
-            "isPartOf": "DOT-19",
-            "agencyProgramURL": "http://www.ntdprogram.gov; http://www.ntdprogram.gov/ntdprogram/data.htm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/pubs/MonthlyData/December%202015%20Raw%20Database.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "December 2015 Raw Data"
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
+            "title": "NTD Monthly Module Data Set - December 2015 Raw Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/bu82-4pwz",
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
-            "identifier": "https://data.transportation.gov/api/views/bu82-4pwz",
             "description": "Commercial air passengers, seats, freight, and mail by year.",
-            "title": "AFF - T100 Segment Summary",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36393,76 +36374,81 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/bu82-4pwz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bu82-4pwz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bu82-4pwz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/bu82-4pwz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bu82-4pwz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bu82-4pwz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/bu82-4pwz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bu82-4pwz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bu82-4pwz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/bu82-4pwz",
+            "issued": "2024-09-26",
+            "keyword": [
+                "aff",
+                "air carriers",
+                "aviation facts & figures",
+                "passengers"
+            ],
+            "landingPage": "https://data.transportation.gov/d/bu82-4pwz",
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
+            "title": "AFF - T100 Segment Summary"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/buxa-ajt8",
-            "issued": "2022-04-26",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-02",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Chambers",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "2024",
             "identifier": "https://data.transportation.gov/api/views/buxa-ajt8",
+            "issued": "2022-04-26",
+            "landingPage": "https://data.transportation.gov/d/buxa-ajt8",
+            "modified": "2024-08-02",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "2024",
             "title": "Low Water Levels in Gatun Lake and the Panama Canal"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/dataset/Rural-Point-of-Contacts/buxa-ujat",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2021-10-28",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-26",
-            "keyword": [
-                "contact",
-                "rural"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alex Clegg",
                 "hasEmail": "mailto:alex.clegg@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
-            "identifier": "https://data.transportation.gov/api/views/buxa-ujat",
             "description": "This dataset combines contact information for the regional/district offices across the Department's operating administrations (OAs). The intent of this dataset is to allow stakeholders to easily identify and contact appropriate offices.",
-            "title": "Rural Point of Contacts",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36470,50 +36456,54 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/buxa-ujat/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/buxa-ujat/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/buxa-ujat/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/buxa-ujat/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/buxa-ujat/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/buxa-ujat/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/buxa-ujat/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/buxa-ujat/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/buxa-ujat/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/buxa-ujat",
+            "issued": "2021-10-28",
+            "keyword": [
+                "contact",
+                "rural"
+            ],
+            "landingPage": "https://data.transportation.gov/dataset/Rural-Point-of-Contacts/buxa-ujat",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-26",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
             "theme": [
                 "Administrative"
-            ]
+            ],
+            "title": "Rural Point of Contacts"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/bvag-c3cn",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/bvag-c3cn",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "FRA develop a spatial point layer of the rail bridges over road and water. The bridges are a snapshot and is not an offical or complete inventory of all bridges. Railroads change ownership, railroads are abandoned, bridges are replaced, etc. therefore it cannot be relied upon as being accurate.",
-            "title": "Railroad Bridges",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36521,40 +36511,83 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/bvag-c3cn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bvag-c3cn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bvag-c3cn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/bvag-c3cn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bvag-c3cn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bvag-c3cn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/bvag-c3cn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bvag-c3cn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bvag-c3cn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/bvag-c3cn",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/bvag-c3cn",
+            "modified": "2024-08-08",
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
-            "landingPage": "https://data.transportation.gov/d/bw6n-ddqk",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "About Transportation Services Index\r\n\r\nThe Transportation Services Index (TSI), created by the U.S. Department of Transportation (DOT), Bureau of Transportation Statistics (BTS), measures the movement of freight and passengers. The index, which is seasonally adjusted, combines available data on freight traffic, as well as passenger travel, that have been weighted to yield a monthly measure of transportation services output.\r\n\r\nFor charts and discussion on the relationship of the TSI to the economy, see our Transportation as an Economic Indicator: Transportation Services Index page  (https://data.bts.gov/stories/s/TET-indicator-1/9czv-tjte)\r\n\r\nFor release schedule see: https://www.bts.gov/newsroom/transportation-services-index-release-schedule\r\n\r\nAbout seasonally-adjusted data\r\n\r\nStatisticians use the process of seasonal-adjustment to uncover trends in data. Monthly data, for instance, are influenced by the number of days and the number of weekends in a month as well as by the timing of holidays and seasonal activity. These influences make it difficult to see underlying changes in the data. Statisticians use seasonal adjustment to control for these influences.\r\n\r\nControlling of seasonal influences allows measurement of real monthly changes; short and long term patterns of growth or decline; and turning points. Data for one month can be compared to data for any other month in the series and the data series can be ranked to find high and low points. Any observed differences are \u201creal\u201d differences; that is, they are differences brought about by changes in the data and not brought about by a change in the number of days or weekends in the month, the occurrence or non-occurrence of a holiday, or seasonal activity.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/api/views/bw6n-ddqk/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.transportation.gov/api/views/bw6n-ddqk/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.transportation.gov/api/views/bw6n-ddqk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.transportation.gov/api/views/bw6n-ddqk/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.transportation.gov/api/views/bw6n-ddqk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.transportation.gov/api/views/bw6n-ddqk/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.transportation.gov/api/views/bw6n-ddqk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/bw6n-ddqk",
             "issued": "2019-11-22",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-17",
             "keyword": [
                 "data",
                 "enplanements",
@@ -36583,93 +36616,64 @@
                 "vehicle miles",
                 "waterways tonnage"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/bw6n-ddqk",
-            "description": "About Transportation Services Index\r\n\r\nThe Transportation Services Index (TSI), created by the U.S. Department of Transportation (DOT), Bureau of Transportation Statistics (BTS), measures the movement of freight and passengers. The index, which is seasonally adjusted, combines available data on freight traffic, as well as passenger travel, that have been weighted to yield a monthly measure of transportation services output.\r\n\r\nFor charts and discussion on the relationship of the TSI to the economy, see our Transportation as an Economic Indicator: Transportation Services Index page  (https://data.bts.gov/stories/s/TET-indicator-1/9czv-tjte)\r\n\r\nFor release schedule see: https://www.bts.gov/newsroom/transportation-services-index-release-schedule\r\n\r\nAbout seasonally-adjusted data\r\n\r\nStatisticians use the process of seasonal-adjustment to uncover trends in data. Monthly data, for instance, are influenced by the number of days and the number of weekends in a month as well as by the timing of holidays and seasonal activity. These influences make it difficult to see underlying changes in the data. Statisticians use seasonal adjustment to control for these influences.\r\n\r\nControlling of seasonal influences allows measurement of real monthly changes; short and long term patterns of growth or decline; and turning points. Data for one month can be compared to data for any other month in the series and the data series can be ranked to find high and low points. Any observed differences are \u201creal\u201d differences; that is, they are differences brought about by changes in the data and not brought about by a change in the number of days or weekends in the month, the occurrence or non-occurrence of a holiday, or seasonal activity.",
-            "title": "Transportation Services Index and Seasonally-Adjusted Transportation Data",
+            "landingPage": "https://data.transportation.gov/d/bw6n-ddqk",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-17",
             "programCode": [
                 "021:053"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/api/views/bw6n-ddqk/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/bw6n-ddqk/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.transportation.gov/api/views/bw6n-ddqk/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/bw6n-ddqk/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.transportation.gov/api/views/bw6n-ddqk/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/bw6n-ddqk/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.transportation.gov/api/views/bw6n-ddqk/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1M",
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Transportation Services Index and Seasonally-Adjusted Transportation Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/bwcv-dxgx",
-            "issued": "2024-12-09",
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
-            "identifier": "https://data.transportation.gov/api/views/bwcv-dxgx",
             "description": "Fuel consumption and cost. Fuel efficiency of the air carrier fleet.",
-            "title": "Fuel Consumption",
+            "identifier": "https://data.transportation.gov/api/views/bwcv-dxgx",
+            "issued": "2024-12-09",
+            "landingPage": "https://data.transportation.gov/d/bwcv-dxgx",
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
+            "title": "Fuel Consumption"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:36"
             ],
-            "landingPage": "https://data.transportation.gov/d/bwgn-kfzn",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NTD Program Support",
+                "hasEmail": "mailto:NTDHelp@dot.gov"
+            },
+            "description": "A national summary of public transit service based on data reported by transit agencies to the National Transit Database (NTD) in Report Year 2023.",
+            "identifier": "https://data.transportation.gov/api/views/bwgn-kfzn",
             "issued": "2024-10-17",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-22",
             "keyword": [
                 "passenger car service",
                 "passenger miles traveled",
@@ -36680,71 +36684,82 @@
                 "vehicle revenue miles",
                 "vehicles operated in maximum service"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NTD Program Support",
-                "hasEmail": "mailto:NTDHelp@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/bwgn-kfzn",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-22",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Transit Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/bwgn-kfzn",
-            "description": "A national summary of public transit service based on data reported by transit agencies to the National Transit Database (NTD) in Report Year 2023.",
-            "title": "2023 NTD Annual Data Summary - Service",
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "2023 NTD Annual Data Summary - Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/bwvi-a3rr",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Economic concepts related to government transportation revenue and expenditures",
+            "identifier": "https://data.transportation.gov/api/views/bwvi-a3rr",
             "issued": "2020-04-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
             "keyword": [
                 "transportation economics",
                 "transportation expenditure",
                 "transportation revenue"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/bwvi-a3rr",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-18",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/bwvi-a3rr",
-            "description": "Economic concepts related to government transportation revenue and expenditures",
-            "title": "Transportation Economic Concepts: Government Transportation Revenue and Expenditure",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Transportation Economic Concepts: Government Transportation Revenue and Expenditure"
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
-            "landingPage": "https://data.transportation.gov/d/bx8m-29ta",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/11novtvt/11novtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "November 2011"
+                }
             ],
+            "identifier": "18.4",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -36754,60 +36769,61 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.4",
+            "landingPage": "https://data.transportation.gov/d/bx8m-29ta",
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
-            "title": "Monthly Traffic Volume Trends - November 2011",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/11novtvt/11novtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "November 2011"
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
+            "title": "Monthly Traffic Volume Trends - November 2011"
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
-            "landingPage": "https://data.transportation.gov/d/bxbd-bkc4",
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
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/inctally3.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Train Accidents by Railroad Groups"
+                }
             ],
+            "identifier": "199.10",
+            "isPartOf": "DOT-199",
+            "issued": "2010-09-29",
             "keyword": [
                 "acts of god",
                 "collisions",
@@ -36818,61 +36834,60 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "199.10",
+            "landingPage": "https://data.transportation.gov/d/bxbd-bkc4",
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
-            "title": "Rail Equipment Accidents - Train Accidents by Railroad Groups",
-            "isPartOf": "DOT-199",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:036"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/inctally3.aspx",
-                    "mediaType": "text/csv",
-                    "title": "Train Accidents by Railroad Groups"
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
+            "title": "Rail Equipment Accidents - Train Accidents by Railroad Groups"
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
-            "landingPage": "https://data.transportation.gov/d/bxet-gf74",
-            "issued": "1981-12-31",
-            "temporal": "1981/2015",
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
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/veh/vehdb-export-fields.htm",
+            "description": "The NHTSA Vehicle Crash Test Database contains engineering data measured during various types of research, the New Car Assessment Program (NCAP), and compliance crash tests. Information in this database refers to the performance and response of vehicles and other structures in impacts. This database is not intended to support general consumer safety issues. For general consumer information please see the NHTSA's information on buying a safer car.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www-nrd.nhtsa.dot.gov/database/VSR/veh/QueryTest.aspx",
+                    "mediaType": "text/html",
+                    "title": "Query by Test Parameters"
+                }
             ],
+            "identifier": "1840.5",
+            "isPartOf": "DOT-1840",
+            "issued": "1981-12-31",
             "keyword": [
                 "compliance",
                 "crash",
@@ -36881,64 +36896,39 @@
                 "test",
                 "vehicle"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "1840.5",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "The NHTSA Vehicle Crash Test Database contains engineering data measured during various types of research, the New Car Assessment Program (NCAP), and compliance crash tests. Information in this database refers to the performance and response of vehicles and other structures in impacts. This database is not intended to support general consumer safety issues. For general consumer information please see the NHTSA's information on buying a safer car.",
-            "title": "Vehicle Crash Test Database - Query by Test Parameters",
-            "isPartOf": "DOT-1840",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research",
+            "landingPage": "https://data.transportation.gov/d/bxet-gf74",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-4712",
             "primaryITInvestmentUII": "021-961265599",
             "programCode": [
                 "021:032"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www-nrd.nhtsa.dot.gov/database/VSR/veh/QueryTest.aspx",
-                    "mediaType": "text/html",
-                    "title": "Query by Test Parameters"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "http://www.nhtsa.gov/Research/Databases+and+Software/NHTSA+Test+Reference+Guides"
             ],
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/veh/vehdb-export-fields.htm",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.nhtsa.gov/Research/Databases+and+Software/NHTSA+Test+Reference+Guides",
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
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/bxx9-8s38",
-            "issued": "2023-11-08",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/bxx9-8s38",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "Rail Crossings",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36946,40 +36936,54 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/bxx9-8s38/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bxx9-8s38/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bxx9-8s38/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/bxx9-8s38/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bxx9-8s38/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bxx9-8s38/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/bxx9-8s38/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/bxx9-8s38/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/bxx9-8s38/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/bxx9-8s38",
+            "issued": "2023-11-08",
+            "landingPage": "https://data.transportation.gov/d/bxx9-8s38",
+            "modified": "2024-08-08",
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
                 "021:36"
             ],
-            "landingPage": "https://data.transportation.gov/d/byxi-22mk",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NTD Program Support",
+                "hasEmail": "mailto:NTDHelp@dot.gov"
+            },
+            "description": "A national summary of facilities and stations based on data reported by transit agencies to the National Transit Database (NTD) in Report Year 2022.\r\n\r\nNTD Data Summaries organize and summarize data from the 2022 National Transit Database in a manner that is more useful for quick reference and summary analysis.\r\n\r\nThis summary is based on the 2022 Facility Inventory, Transit Facilities, and Transit Stations files on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
+            "identifier": "https://data.transportation.gov/api/views/byxi-22mk",
             "issued": "2023-09-09",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-10",
             "keyword": [
                 "maintenance facilities",
                 "passenger terminals",
@@ -36987,41 +36991,27 @@
                 "stations",
                 "transit"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NTD Program Support",
-                "hasEmail": "mailto:NTDHelp@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/byxi-22mk",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-09-10",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Transit Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/byxi-22mk",
-            "description": "A national summary of facilities and stations based on data reported by transit agencies to the National Transit Database (NTD) in Report Year 2022.\r\n\r\nNTD Data Summaries organize and summarize data from the 2022 National Transit Database in a manner that is more useful for quick reference and summary analysis.\r\n\r\nThis summary is based on the 2022 Facility Inventory, Transit Facilities, and Transit Stations files on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
-            "title": "2022 NTD Annual Data Summary - Facilities and Stations",
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "2022 NTD Annual Data Summary - Facilities and Stations"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/byy5-w977",
-            "issued": "2023-07-19",
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
-                "name": "Federal Railroad Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/byy5-w977",
             "description": "Curated FRA Safety data pertaining to Rail Equipment Accidents (Form 54) Unique Train Accidents\n\nPlease note that this dataset displays unique train accidents. When an accident involves multiple railroads, each railroad must report its data. As a result, there can be multiple records for one accident. This dataset has been modified to pull and display one record for each accident.\n\nHighway-rail crossing incidents have also been removed from this dataset because they are not considered train accidents.\n\nTo see the full dataset with all reports with all data for all accidents, please visit https://data.transportation.gov/Railroads/Rail-Equipment-Accident-Incident-Data/85tf-25kj",
-            "title": "Rail Equipment Accident/Incident Data (Form 54) Subset \u2013 Unique Train Accidents (Not at Grade Crossings)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37029,69 +37019,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/byy5-w977/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/byy5-w977/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/byy5-w977/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/byy5-w977/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/byy5-w977/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/byy5-w977/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/byy5-w977/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/byy5-w977/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/byy5-w977/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/byy5-w977",
+            "issued": "2023-07-19",
+            "landingPage": "https://data.transportation.gov/d/byy5-w977",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-02-01",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Railroad Administration"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Rail Equipment Accident/Incident Data (Form 54) Subset \u2013 Unique Train Accidents (Not at Grade Crossings)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/SQCVSP/default.aspx",
+            "agencyProgramURL": "https://ai.fmcsa.dot.gov/Default.aspx",
+            "analysisUnit": "State",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/bzgp-cpqk",
-            "issued": "1974-06-01",
-            "temporal": "R/1974-06-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-24",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "https://ai.fmcsa.dot.gov/Default.aspx"
-            ],
-            "keyword": [
-                "commercial vehicle safety program.",
-                "cvsp",
-                "mcsap",
-                "safety measurement system",
-                "sms"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FMCSA CDO",
                 "hasEmail": "mailto:fmcsa.cdo@dot.gov"
             },
-            "identifier": "118.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": true,
             "description": "Mini screen view of Data DashboardThe State Quarterly Report and CVSP Data Dashboard (Data Dashboard) is a tool that presents quarterly updated safety data to assist states with preparing their Motor Carrier Safety Assistance Program (MCSAP) Formula Grant Quarterly Reports and monitoring MCSAP-funded activities identified in their Commercial Vehicle Safety Plan (CVSP). Note: The Data Dashboard presents all safety data reported to the FMCSA Motor Carrier Management Information System (MCMIS) regardless of the funding source.",
-            "title": "A&I - MCSAP Program - State Quarterly Report and CVSP Data Dashboard - A&I Login",
-            "agencyProgramURL": "https://ai.fmcsa.dot.gov/Default.aspx",
-            "programCode": [
-                "021:019"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37100,94 +37081,92 @@
                     "title": "A&I Login"
                 }
             ],
-            "spatial": "State",
-            "dataQuality": true,
+            "identifier": "118.0",
+            "issued": "1974-06-01",
+            "keyword": [
+                "commercial vehicle safety program.",
+                "cvsp",
+                "mcsap",
+                "safety measurement system",
+                "sms"
+            ],
+            "landingPage": "https://data.transportation.gov/d/bzgp-cpqk",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://ai.fmcsa.dot.gov/SQCVSP/default.aspx",
+            "modified": "2024-05-24",
+            "phone": "202-366-3030",
+            "programCode": [
+                "021:019"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Motor Carrier Safety Administration"
+            },
+            "references": [
+                "https://ai.fmcsa.dot.gov/Default.aspx"
+            ],
+            "spatial": "State",
+            "temporal": "R/1974-06-01/P1M",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1M",
-            "analysisUnit": "State",
-            "categoryDesignation": "Research",
-            "phone": "202-366-3030",
-            "language": [
-                "en-US"
-            ]
+            "title": "A&I - MCSAP Program - State Quarterly Report and CVSP Data Dashboard - A&I Login"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/bzt6-t8cd",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Transportation spending per vehicle mile",
+            "identifier": "https://data.transportation.gov/api/views/bzt6-t8cd",
             "issued": "2020-03-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-13",
             "keyword": [
                 "cost per vehicle mile",
                 "transportation",
                 "vehicle costs"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/bzt6-t8cd",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-12-13",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/bzt6-t8cd",
-            "description": "Transportation spending per vehicle mile",
-            "title": "Transportation Economic Trends: Transportation Spending - Per Vehicle Mile",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Transportation Economic Trends: Transportation Spending - Per Vehicle Mile"
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
-            "landingPage": "https://data.transportation.gov/d/c34f-ft5s",
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
-            "identifier": "524.21",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
             "description": "STATE DATA REPORTING SYSTEMS. Annual reports on the Fatality Analysis Reporting System (FARS) which is data regarding fatalities that is collected by a FARS analyst from each State and provided to NHTSA.",
-            "title": "GES Reports - 1992",
-            "isPartOf": "DOT-524",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37196,59 +37175,60 @@
                     "title": "1992"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
-            "dataQuality": true,
+            "identifier": "524.21",
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
+            "landingPage": "https://data.transportation.gov/d/c34f-ft5s",
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
+            "title": "GES Reports - 1992"
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
-            "landingPage": "https://data.transportation.gov/d/c4fn-2xhp",
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
-            "identifier": "373.5",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": true,
             "description": "Each Freedom of Information Act office uses a case log to track FOIA requests. The logs typically include the dates on which requests were received and closed, control numbers, requester names and descriptions of the requested records.",
-            "title": "Freedom of Information Act Logs for the Office of the Secretary of Transportation - 2011",
-            "isPartOf": "DOT-373",
-            "agencyProgramURL": "http://www.dot.gov/foia",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37257,70 +37237,108 @@
                     "title": "2011"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "373.5",
+            "isPartOf": "DOT-373",
+            "issued": "2007-12-31",
+            "keyword": [
+                "foia",
+                "freedom of information act",
+                "log",
+                "request"
+            ],
+            "landingPage": "https://data.transportation.gov/d/c4fn-2xhp",
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
+            "title": "Freedom of Information Act Logs for the Office of the Secretary of Transportation - 2011"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/c54b-peqd",
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
             "identifier": "https://data.transportation.gov/api/views/c54b-peqd",
+            "issued": "2023-03-16",
+            "landingPage": "https://data.transportation.gov/d/c54b-peqd",
+            "modified": "2023-03-16",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Robert_A"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/c5zf-dtju",
-            "issued": "2022-03-24",
             "@type": "dcat:Dataset",
-            "modified": "2022-04-21",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joe McGill",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "Preview and access the dataset.",
             "identifier": "https://data.transportation.gov/api/views/c5zf-dtju",
+            "issued": "2022-03-24",
+            "landingPage": "https://data.transportation.gov/d/c5zf-dtju",
+            "modified": "2022-04-21",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "Preview and access the dataset.",
             "title": "National Ferry Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/c7cy-r5pm",
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
+                    "description": "2013 West Virginia HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/westvirginia2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 West Virginia"
+                }
+            ],
+            "identifier": "678.151",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -37334,60 +37352,56 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.151",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 West Virginia",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/c7cy-r5pm",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/westvirginia2013.zip",
-                    "description": "2013 West Virginia HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 West Virginia"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 West Virginia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.nhtsa.gov/nti/811841",
+            "agencyProgramURL": "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/National+Telephone+Surveys",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/c7rj-efip",
-            "issued": "2013-10-31",
-            "temporal": "2012-07-12/2012-11-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.nhtsa.gov/nti/811841"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": false,
+            "description": "Information from the public to ascertain the current frequency and characteristics of bicyclist and pedestrian activity, and identify deterrents to bicycling and walking. The data will also be compared to data collected by a previous NHTSA survey, conducted in 2002, to determine if major changes have occurred over that 10-year span. The information will be used to help update and refine safety programs. A national telephone survey will be administered to 9,000 randomly selected respondents 16 and older drawn from all 50 States and the District of Columbia. The survey will ask about the characteristics of bicycling and walking trips, conspicuity, community design for bicycling and walking, bicycle helmet use, and general opinions about bicycling and walking. Interview length will average 20 minutes.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.nhtsa.gov/staticfiles/nti/other/2012survey/BikePed-Data_revFINAL2.sav",
+                    "mediaType": "text/csv",
+                    "title": "2012 Survey (SPSS)"
+                }
             ],
+            "identifier": "415.2",
+            "isPartOf": "DOT-415",
+            "issued": "2013-10-31",
             "keyword": [
                 "activity",
                 "attitude",
@@ -37399,68 +37413,41 @@
                 "knowledge",
                 "pedestrian"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "415.2",
+            "landingPage": "https://data.transportation.gov/d/c7rj-efip",
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
-            "description": "Information from the public to ascertain the current frequency and characteristics of bicyclist and pedestrian activity, and identify deterrents to bicycling and walking. The data will also be compared to data collected by a previous NHTSA survey, conducted in 2002, to determine if major changes have occurred over that 10-year span. The information will be used to help update and refine safety programs. A national telephone survey will be administered to 9,000 randomly selected respondents 16 and older drawn from all 50 States and the District of Columbia. The survey will ask about the characteristics of bicycling and walking trips, conspicuity, community design for bicycling and walking, bicycle helmet use, and general opinions about bicycling and walking. Interview length will average 20 minutes.",
-            "title": "National Survey of Pedestrian and Bicyclist Attitudes, Knowledge, and Behaviors - 2012 Survey (SPSS)",
-            "isPartOf": "DOT-415",
-            "agencyProgramURL": "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/National+Telephone+Surveys",
-            "programCode": [
-                "021:032"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.nhtsa.gov/staticfiles/nti/other/2012survey/BikePed-Data_revFINAL2.sav",
-                    "mediaType": "text/csv",
-                    "title": "2012 Survey (SPSS)"
-                }
+            "references": [
+                "http://www.nhtsa.gov/nti/811841"
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.nhtsa.gov/nti/811841",
+            "temporal": "2012-07-12/2012-11-18",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "phone": "202-366-6401",
-            "language": [
-                "en-US"
-            ]
+            "title": "National Survey of Pedestrian and Bicyclist Attitudes, Knowledge, and Behaviors - 2012 Survey (SPSS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/c7tj-sc2j",
-            "issued": "2024-08-07",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-07",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "TBD",
                 "hasEmail": "mailto:sean.jahanmir@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/c7tj-sc2j",
             "description": "",
-            "title": "Top 25 Ports by Dry Bulk Tonnage",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37468,55 +37455,53 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/c7tj-sc2j/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/c7tj-sc2j/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/c7tj-sc2j/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/c7tj-sc2j/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/c7tj-sc2j/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/c7tj-sc2j/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/c7tj-sc2j/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/c7tj-sc2j/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/c7tj-sc2j/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "https://data.transportation.gov/api/views/c7tj-sc2j",
+            "issued": "2024-08-07",
+            "landingPage": "https://data.transportation.gov/d/c7tj-sc2j",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-08-07",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Top 25 Ports by Dry Bulk Tonnage"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/c8k8-y2cj",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-09-05",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
-            "keyword": [
-                "fuel tax",
-                "funding",
-                "taxes"
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
-            "identifier": "https://data.transportation.gov/api/views/c8k8-y2cj",
             "description": "This dataset details funding from taxes levied by each applicable agency reporting to the National Transit Database in the 2022 and 2023 report years. Examples include Income, Sales, Property and Fuel taxes and Tolls.\n\nNTD Data Tables organize and summarize data from the 2022 and 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. This dataset is based on the 2022 and 2023 Revenue Sources database files.\n\nIn years 2015-2021, you can find this data in the \"Funding Sources\" data table on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.\n\nIf you have any other questions about this table, please contact the NTD Help Desk at NTDHelp@dot.gov.",
-            "title": "2022 - 2023 NTD Annual Data - Funding Sources (Taxes Levied by Agency)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37524,46 +37509,77 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/c8k8-y2cj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/c8k8-y2cj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/c8k8-y2cj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/c8k8-y2cj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/c8k8-y2cj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/c8k8-y2cj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/c8k8-y2cj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/c8k8-y2cj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/c8k8-y2cj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/c8k8-y2cj",
+            "issued": "2024-09-05",
+            "keyword": [
+                "fuel tax",
+                "funding",
+                "taxes"
+            ],
+            "landingPage": "https://data.transportation.gov/d/c8k8-y2cj",
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
+            "title": "2022 - 2023 NTD Annual Data - Funding Sources (Taxes Levied by Agency)"
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
-            "landingPage": "https://data.transportation.gov/d/c8ka-c7td",
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
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/pubs/MonthlyData/September%202015%20Raw%20Database.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "September 2015 Raw Data"
+                }
             ],
+            "identifier": "19.3",
+            "isPartOf": "DOT-19",
+            "issued": "2011-10-07",
             "keyword": [
                 "boardings",
                 "bus",
@@ -37573,61 +37589,59 @@
                 "train",
                 "transit"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John D. Giorgis",
-                "hasEmail": "mailto:john.giorgis@dot.gov"
-            },
-            "identifier": "19.3",
+            "landingPage": "https://data.transportation.gov/d/c8ka-c7td",
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
-            "title": "NTD Monthly Module Data Set - September 2015 Raw Data",
-            "isPartOf": "DOT-19",
-            "agencyProgramURL": "http://www.ntdprogram.gov; http://www.ntdprogram.gov/ntdprogram/data.htm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/pubs/MonthlyData/September%202015%20Raw%20Database.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "September 2015 Raw Data"
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
+            "title": "NTD Monthly Module Data Set - September 2015 Raw Data"
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
-            "landingPage": "https://data.transportation.gov/d/c8sy-d3p7",
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
+            "identifier": "DOT-376",
+            "issued": "2008-12-05",
             "keyword": [
                 "avoidance",
                 "causation",
@@ -37640,77 +37654,42 @@
                 "pre-crash",
                 "vehicle"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "DOT-376",
+            "landingPage": "https://data.transportation.gov/d/c8sy-d3p7",
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
-            "title": "National Motor Vehicle Crash Causation Survey (NMVCCS)",
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
+            "title": "National Motor Vehicle Crash Causation Survey (NMVCCS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ca7h-i9yt",
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
-            "identifier": "https://data.transportation.gov/api/views/ca7h-i9yt",
             "description": "This is the Terminals file for the 2020 National Census of Ferry Operators. It is one of five data sets that make up the 2020 NCFO",
-            "title": "2020 NCFO Terminals File",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37718,43 +37697,82 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ca7h-i9yt/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ca7h-i9yt/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ca7h-i9yt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ca7h-i9yt/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ca7h-i9yt/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ca7h-i9yt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ca7h-i9yt/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ca7h-i9yt/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ca7h-i9yt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/ca7h-i9yt",
+            "issued": "2022-04-01",
+            "keyword": [
+                "ferry",
+                "ferry operators",
+                "ferry transit",
+                "passenger ferry",
+                "transportation",
+                "water transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ca7h-i9yt",
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
+            "title": "2020 NCFO Terminals File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/caex-zjtz",
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
+                    "description": "2013 New York HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/newyork2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 New York"
+                }
+            ],
+            "identifier": "678.136",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -37768,79 +37786,43 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.136",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 New York",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/caex-zjtz",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/newyork2013.zip",
-                    "description": "2013 New York HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 New York"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 New York"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Access restricted under the Privacy Act of 1974; see SORN DOT/ALL 6 http://www.gpo.gov/fdsys/pkg/FR-2000-04-11/pdf/00-8505.pdf#page=78",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/cake-rgpt",
-            "issued": "2014-11-21",
-            "temporal": "R/2014-11-21/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "feca",
-                "owcp",
-                "workers compensation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "1636.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
             "description": "This data set contains DOT employee workers compensation claim data for current and past DOT employees.  Types of data include claim data consisting of PII data (SSN, Name, Date of Birth, Home Address, Financial Institution, medical, etc.) and claim data from the Department of Labor",
-            "title": "Workers Compensation Claim Data -",
-            "primaryITInvestmentUII": "021-257151844",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37848,62 +37830,98 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "theme": [
-                "Transportation"
+            "identifier": "1636.0",
+            "issued": "2014-11-21",
+            "keyword": [
+                "feca",
+                "owcp",
+                "workers compensation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/cake-rgpt",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-5140"
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-14",
+            "phone": "202-366-5140",
+            "primaryITInvestmentUII": "021-257151844",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "rights": "Access restricted under the Privacy Act of 1974; see SORN DOT/ALL 6 http://www.gpo.gov/fdsys/pkg/FR-2000-04-11/pdf/00-8505.pdf#page=78",
+            "temporal": "R/2014-11-21/P1Y",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Workers Compensation Claim Data -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/caxh-t8jd",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2020-03-09",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
-            "keyword": [
-                "transportation employment",
-                "transportation workforce"
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
-            "identifier": "https://data.transportation.gov/api/views/caxh-t8jd",
             "description": "Employment in transportation and related industries",
-            "title": "Transportation Economic Trends: Transportation Employment - Industry",
+            "identifier": "https://data.transportation.gov/api/views/caxh-t8jd",
+            "issued": "2020-03-09",
+            "keyword": [
+                "transportation employment",
+                "transportation workforce"
+            ],
+            "landingPage": "https://data.transportation.gov/d/caxh-t8jd",
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
+            "title": "Transportation Economic Trends: Transportation Employment - Industry"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/cayq-usiy",
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
+                    "description": "2013 Connecticut HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/connecticut2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Connecticut"
+                }
+            ],
+            "identifier": "678.111",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -37917,64 +37935,36 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.111",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Connecticut",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/cayq-usiy",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/connecticut2013.zip",
-                    "description": "2013 Connecticut HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Connecticut"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Connecticut"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/cchm-epc8",
-            "issued": "2023-02-06",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/cchm-epc8",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "CN",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37982,67 +37972,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/cchm-epc8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/cchm-epc8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/cchm-epc8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/cchm-epc8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/cchm-epc8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/cchm-epc8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/cchm-epc8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/cchm-epc8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/cchm-epc8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/cchm-epc8",
+            "issued": "2023-02-06",
+            "landingPage": "https://data.transportation.gov/d/cchm-epc8",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "CN"
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
-            "landingPage": "https://data.transportation.gov/d/ccjf-d9fq",
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
-            "identifier": "692.30",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - PM 2.5",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "primaryITInvestmentUII": "021-845083703",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38051,56 +38032,52 @@
                     "title": "PM 2.5"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.30",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ccjf-d9fq",
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
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - PM 2.5"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2019-05-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "condition",
-                "extent",
-                "highways",
-                "hpms",
-                "map",
-                "mileage",
-                "performance",
-                "travel",
-                "use"
-            ],
             "conformsTo": "https://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/ccjq-w54n",
+            "dataQuality": true,
             "description": "The Highway Performance Monitoring System (HPMS) compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially\u2010enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "2015 HPMS - Dynamically Segmented",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38108,51 +38085,89 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ccjq-w54n/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ccjq-w54n/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ccjq-w54n/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ccjq-w54n/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ccjq-w54n/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ccjq-w54n/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ccjq-w54n/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ccjq-w54n/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ccjq-w54n/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "systemOfRecords": "Highway Performance Monitoring System (HPMS)",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/ccjq-w54n",
+            "issued": "2019-05-01",
+            "keyword": [
+                "condition",
+                "extent",
+                "highways",
+                "hpms",
+                "map",
+                "mileage",
+                "performance",
+                "travel",
+                "use"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
+            "language": [
+                "English"
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
+            "systemOfRecords": "Highway Performance Monitoring System (HPMS)",
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "English"
-            ]
+            "title": "2015 HPMS - Dynamically Segmented"
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
-            "landingPage": "https://data.transportation.gov/d/ccz8-csfd",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/07martvt/07martvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "March 2007"
+                }
             ],
+            "identifier": "18.90",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -38162,138 +38177,101 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.90",
+            "landingPage": "https://data.transportation.gov/d/ccz8-csfd",
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
-            "title": "Monthly Traffic Volume Trends - March 2007",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/07martvt/07martvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "March 2007"
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
+            "title": "Monthly Traffic Volume Trends - March 2007"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/cd4n-nq6m",
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
             "identifier": "https://data.transportation.gov/api/views/cd4n-nq6m",
+            "issued": "2025-01-31",
+            "landingPage": "https://data.transportation.gov/d/cd4n-nq6m",
+            "modified": "2025-01-31",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Charts and Graphs"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/cf3b-7d2d",
             "bureauCode": [
                 "021:27"
             ],
-            "issued": "2024-09-26",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
-            "keyword": [
-                "trespasser. suicide"
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
-            "identifier": "https://data.transportation.gov/api/views/cf3b-7d2d",
+            "dataQuality": true,
             "description": "This is the report for suicide incidents, fatalities and injuries.",
-            "title": "Suicide Incidents, Fatalities, and Injuries",
+            "identifier": "https://data.transportation.gov/api/views/cf3b-7d2d",
+            "issued": "2024-09-26",
+            "keyword": [
+                "trespasser. suicide"
+            ],
+            "landingPage": "https://data.transportation.gov/d/cf3b-7d2d",
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
+            "title": "Suicide Incidents, Fatalities, and Injuries"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://data.transportation.gov/d/cfg4-fw68",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:18"
             ],
-            "rights": "sensitive information",
-            "issued": "2018-12-17",
-            "@type": "dcat:Dataset",
-            "temporal": "R/2013/P1Y",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-01",
-            "keyword": [
-                "automobile dealers",
-                "defendant",
-                "informants",
-                "investigation",
-                "odometer fraud.",
-                "suspect",
-                "victims",
-                "witnesses"
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
-            "identifier": "407.0",
+            "dataQuality": false,
             "description": "Information to be used in allegations of odometer fraud.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Odometer Fraud Data Base Files -",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38301,32 +38279,68 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
+            "identifier": "407.0",
+            "issued": "2018-12-17",
+            "keyword": [
+                "automobile dealers",
+                "defendant",
+                "informants",
+                "investigation",
+                "odometer fraud.",
+                "suspect",
+                "victims",
+                "witnesses"
+            ],
+            "landingPage": "https://data.transportation.gov/d/cfg4-fw68",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-05-01",
+            "phone": "202-366-5953",
+            "programCode": [
+                "021:035"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "rights": "sensitive information",
+            "temporal": "R/2013/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "categoryDesignation": "Research",
-            "phone": "202-366-5953",
-            "language": [
-                "en-US"
-            ]
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Odometer Fraud Data Base Files -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyProgramURL": "http://www.nhtsa.gov/fuel-economy",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/cfru-w26b",
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
+                    "description": "Manufacturers listed in this report either paid a civil penalty for their associated fleet\u2019s entire shortfall in the given model year or satisfied part of the shortfall with a civil penalty payment and executed another compliance flexibility for the remainder. Also available in PDF and XLS.",
+                    "downloadURL": "http://www.nhtsa.gov/CAFE_PIC/CAFE_PIC_Fines_LIVE.html",
+                    "mediaType": "text/html",
+                    "title": "Summary of CAFE Civil Penalties Collected"
+                }
             ],
+            "identifier": "1862.7",
+            "isPartOf": "DOT-1862",
+            "issued": "2015-12-16",
             "keyword": [
                 "amfa",
                 "civil penalties",
@@ -38343,55 +38357,59 @@
                 "report",
                 "shortfall"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "1862.7",
+            "landingPage": "https://data.transportation.gov/d/cfru-w26b",
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
-            "title": "CAFE (Corporate Average Fuel Economy) - Summary of CAFE Civil Penalties Collected",
-            "isPartOf": "DOT-1862",
-            "agencyProgramURL": "http://www.nhtsa.gov/fuel-economy",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://www.nhtsa.gov/CAFE_PIC/CAFE_PIC_Fines_LIVE.html",
-                    "description": "Manufacturers listed in this report either paid a civil penalty for their associated fleet\u2019s entire shortfall in the given model year or satisfied part of the shortfall with a civil penalty payment and executed another compliance flexibility for the remainder. Also available in PDF and XLS.",
-                    "@type": "dcat:Distribution",
-                    "title": "Summary of CAFE Civil Penalties Collected"
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
+            "title": "CAFE (Corporate Average Fuel Economy) - Summary of CAFE Civil Penalties Collected"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/cfsq-f5g6",
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
+                    "description": "2011 Wisconsin HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/wisconsin2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Wisconsin"
+                }
+            ],
+            "identifier": "678.51",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -38405,82 +38423,46 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.51",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Wisconsin",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/cfsq-f5g6",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/wisconsin2011.zip",
-                    "description": "2011 Wisconsin HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Wisconsin"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Wisconsin"
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
-            "landingPage": "https://data.transportation.gov/d/cfwf-u8w6",
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
-            "identifier": "364.28",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2010",
-            "isPartOf": "DOT-364",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
-            "primaryITInvestmentUII": "021-621341357",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38489,35 +38471,68 @@
                     "title": "Event Data Records Reports - 2010"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.28",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/cfwf-u8w6",
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
+            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2010"
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
-            "landingPage": "https://data.transportation.gov/d/ch6d-34vu",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/11dectvt/11dectvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "December 2011"
+                }
             ],
+            "identifier": "18.3",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -38527,83 +38542,48 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.3",
+            "landingPage": "https://data.transportation.gov/d/ch6d-34vu",
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
-            "title": "Monthly Traffic Volume Trends - December 2011",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/11dectvt/11dectvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "December 2011"
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
+            "title": "Monthly Traffic Volume Trends - December 2011"
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
-            "landingPage": "https://data.transportation.gov/d/ch7p-bus9",
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
-            "identifier": "1637.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
             "description": "The 2008 National Survey of Drinking and Driving Attitudes and Behaviors was composed of a single questionnaire administered to a sample of randomly selected individuals 16 and older, with ages 16 through 24 over-sampled. The respondents were asked about their drinking behavior, their drinking and driving behavior, use of designated drivers, their hosting events in which drinking occurred, risks they perceive associated with drinking and driving, experience with anti-DWI enforcement activity, and their attitudes concerning major intervention strategies.The survey was administered from September 10, 2008 to December 22, 2008. A total of 6,999 respondents completed the survey, including 5,392 landline interviews and 1,607 cell phone interviews. The total number of completed interviews for each of the four Census regions (Northeast, Midwest, South, and West) was 1,409, 1,654, 2,390, and 1,546, respectively.",
-            "title": "2008 National Survey of Drinking and Driving Attitudes and Behaviors - SPSS Database File",
-            "isPartOf": "DOT-1637",
-            "agencyProgramURL": "http://www.nhtsa.gov/Driving+Safety/Occupant+Protection/2008+National+Survey+of+Drinking+and+Driving+Attitudes+and+Behaviors",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38612,52 +38592,51 @@
                     "title": "SPSS Database File"
                 }
             ],
-            "spatial": "n/a",
-            "dataQuality": false,
+            "identifier": "1637.1",
+            "isPartOf": "DOT-1637",
+            "issued": "2010-08-31",
+            "keyword": [
+                "attitudes",
+                "behaviors",
+                "drinking",
+                "driving"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ch7p-bus9",
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
+            "title": "2008 National Survey of Drinking and Driving Attitudes and Behaviors - SPSS Database File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/chgs-tx6x",
             "bureauCode": [
                 "021:17"
             ],
-            "issued": "2023-04-13",
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
-            "identifier": "https://data.transportation.gov/api/views/chgs-tx6x",
             "description": "*This is a \"daily difference\" dataset.  See dataset attachment \"FMCSA Dataset Description and Data Definitions - Select Datasets\" for more information.*  Information on the implementation dates of an active or pending insurance policy (posted date, effective date and cancel effective date). In addition to these dates, the record contains the insurance company name, the BI&PD underlying limit and maximum limit amounts, and the DOT number and docket number of the carrier/broker/freight forwarder that holds the policy.",
-            "title": "ActPendInsur",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38665,50 +38644,50 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/chgs-tx6x",
+            "issued": "2023-04-13",
+            "keyword": [
+                "active",
+                "for-hire motor carriers",
+                "operating authority",
+                "registration status",
+                "revoked",
+                "suspended"
+            ],
+            "landingPage": "https://data.transportation.gov/d/chgs-tx6x",
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
+            "title": "ActPendInsur"
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
-            "landingPage": "https://data.transportation.gov/d/ci2e-bhk9",
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
-            "identifier": "524.10",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
             "description": "STATE DATA REPORTING SYSTEMS. Annual reports on the Fatality Analysis Reporting System (FARS) which is data regarding fatalities that is collected by a FARS analyst from each State and provided to NHTSA.",
-            "title": "GES Reports - 2008",
-            "isPartOf": "DOT-524",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38717,52 +38696,78 @@
                     "title": "2008"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
-            "dataQuality": true,
+            "identifier": "524.10",
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
+            "landingPage": "https://data.transportation.gov/d/ci2e-bhk9",
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
+            "title": "GES Reports - 2008"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ci7m-hmhv",
-            "issued": "2024-01-31",
             "@type": "dcat:Dataset",
-            "modified": "2024-03-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/ci7m-hmhv",
+            "issued": "2024-01-31",
+            "landingPage": "https://data.transportation.gov/d/ci7m-hmhv",
+            "modified": "2024-03-08",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
-            "title": "Highway-Rail Grade Crossing Accident Prediction System (GXAPS)",
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Highway-Rail Grade Crossing Accident Prediction System (GXAPS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ciip-qu8c",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The table below displays the name and URL of both the legacy reports and the reports replacing them on this site, where applicable. The legacy reports are currently located at https://safetydata.fra.dot.gov or https://railroads.dot.gov/safety-data. This new reports are being released throughout 2023. The legacy reports will remain active until May 2024.",
+            "identifier": "https://data.transportation.gov/api/views/ciip-qu8c",
             "issued": "2023-08-08",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-13",
             "keyword": [
                 "crosswalk",
                 "legacy",
@@ -38770,43 +38775,54 @@
                 "new site",
                 "old reports"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/ciip-qu8c",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-11-13",
+            "programCode": [
+                "021:036"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Railroad Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/ciip-qu8c",
-            "description": "The table below displays the name and URL of both the legacy reports and the reports replacing them on this site, where applicable. The legacy reports are currently located at https://safetydata.fra.dot.gov or https://railroads.dot.gov/safety-data. This new reports are being released throughout 2023. The legacy reports will remain active until May 2024.",
-            "title": "Legacy to New Site Crosswalk",
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
+            "title": "Legacy to New Site Crosswalk"
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
-            "landingPage": "https://data.transportation.gov/d/cjde-yg7a",
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
+                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/nits/Nontraffic%20crashes/2011/",
+                    "mediaType": "text/plain",
+                    "title": "2011 Nontraffic Crashes"
+                }
             ],
+            "identifier": "288.10",
+            "isPartOf": "DOT-288",
+            "issued": "2009-01-27",
             "keyword": [
                 "crash",
                 "death",
@@ -38822,65 +38838,39 @@
                 "vehicle",
                 "victim"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "288.10",
+            "landingPage": "https://data.transportation.gov/d/cjde-yg7a",
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
-            "title": "Not in Traffic Surveillance (NiTS) - 2011 Nontraffic Crashes",
-            "isPartOf": "DOT-288",
-            "agencyProgramURL": "http://www.nhtsa.gov/Data/State+Data+Programs",
-            "programCode": [
-                "021:032"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/nits/Nontraffic%20crashes/2011/",
-                    "mediaType": "text/plain",
-                    "title": "2011 Nontraffic Crashes"
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
+            "title": "Not in Traffic Surveillance (NiTS) - 2011 Nontraffic Crashes"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ck5e-th4k",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-09",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/ck5e-th4k",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "Rail Yards",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38888,45 +38878,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ck5e-th4k/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ck5e-th4k/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ck5e-th4k/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ck5e-th4k/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ck5e-th4k/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ck5e-th4k/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ck5e-th4k/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ck5e-th4k/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ck5e-th4k/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/ck5e-th4k",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/ck5e-th4k",
+            "modified": "2025-01-09",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Rail Yards"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://ntlsearch.bts.gov/repository/index.do",
+            "agencyProgramURL": "https://ntl.bts.gov/",
+            "analysisUnit": "N/A",
             "bureauCode": [
                 "021:53"
             ],
-            "landingPage": "https://data.transportation.gov/d/ckgn-n3pu",
-            "issued": "2012-01-01",
-            "temporal": "1920-01-01/2014-12-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://ntlsearch.bts.gov/repository/index.do"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DOT Socrata",
+                "hasEmail": "mailto:Socrata@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The National Transportation Library Catalog is charged with improving the availability of transportation-related information needed by Federal, state, and local decision-makers. Its mission is to increase timely access to the information that supports transportation policy, research, operations, and technology transfer activities. NTL catalogs contain metadata about full-text reports, data, transportation Web sites, books, eBooks, journals, and other special collections in the digital repository and traditional ibrary collections. All NTL holdings are available full text online.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://tlcat.worldcat.org/",
+                    "mediaType": "text/html",
+                    "title": "TLCat"
+                }
             ],
+            "identifier": "432.6",
+            "isPartOf": "DOT-432",
+            "issued": "2012-01-01",
             "keyword": [
                 "accidents",
                 "air quality",
@@ -38956,92 +38971,95 @@
                 "tunnels",
                 "vessels"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DOT Socrata",
-                "hasEmail": "mailto:Socrata@dot.gov"
-            },
-            "identifier": "432.6",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Research and Innovative Technology Administration"
-            },
-            "description": "The National Transportation Library Catalog is charged with improving the availability of transportation-related information needed by Federal, state, and local decision-makers. Its mission is to increase timely access to the information that supports transportation policy, research, operations, and technology transfer activities. NTL catalogs contain metadata about full-text reports, data, transportation Web sites, books, eBooks, journals, and other special collections in the digital repository and traditional ibrary collections. All NTL holdings are available full text online.",
-            "title": "National Transportation Library Catalog - TLCat",
-            "isPartOf": "DOT-432",
-            "agencyProgramURL": "https://ntl.bts.gov/",
+            "landingPage": "https://data.transportation.gov/d/ckgn-n3pu",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-11-14",
+            "phone": "202-366-0303",
             "primaryITInvestmentUII": "021-658036941",
             "programCode": [
                 "021:042"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://tlcat.worldcat.org/",
-                    "mediaType": "text/html",
-                    "title": "TLCat"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Research and Innovative Technology Administration"
+            },
+            "references": [
+                "http://ntlsearch.bts.gov/repository/index.do"
             ],
             "spatial": "N/A",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://ntlsearch.bts.gov/repository/index.do",
+            "temporal": "1920-01-01/2014-12-29",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "analysisUnit": "N/A",
-            "phone": "202-366-0303",
-            "language": [
-                "en-US"
-            ]
+            "title": "National Transportation Library Catalog - TLCat"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/cksf-e5wx",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2020-04-13",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-28",
-            "keyword": [
-                "labor productivity",
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
-            "identifier": "https://data.transportation.gov/api/views/cksf-e5wx",
             "description": "Transportation labor productivity",
-            "title": "Transportation Economic Trends: Productivity - Labor",
+            "identifier": "https://data.transportation.gov/api/views/cksf-e5wx",
+            "issued": "2020-04-13",
+            "keyword": [
+                "labor productivity",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/cksf-e5wx",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-28",
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
+            "title": "Transportation Economic Trends: Productivity - Labor"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/cm26-hk5p",
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
+                    "description": "2013 Massachusetts HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/massachusetts2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Massachusetts"
+                }
+            ],
+            "identifier": "678.125",
+            "isPartOf": "DOT-678",
             "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
-            "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
             "keyword": [
                 "aadt",
                 "condition",
@@ -39055,82 +39073,43 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.125",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Massachusetts",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/cm26-hk5p",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/massachusetts2013.zip",
-                    "description": "2013 Massachusetts HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Massachusetts"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Massachusetts"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "contains sensitive network infomration",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/cn83-b5ih",
-            "issued": "2010-12-31",
-            "temporal": "R/2010/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "asset",
-                "configuration",
-                "enteprise architecture",
-                "inventory",
-                "it standards",
-                "technical reference model"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "480.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
             "description": "Implements agency TRM. Temporary.  OFFICE OF CHIEF INFORMATION OFFICER (NPO-400).",
-            "title": "NHTSA Asset Framework -",
-            "primaryITInvestmentUII": "021-031601412",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39138,54 +39117,56 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "480.0",
+            "issued": "2010-12-31",
+            "keyword": [
+                "asset",
+                "configuration",
+                "enteprise architecture",
+                "inventory",
+                "it standards",
+                "technical reference model"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/cn83-b5ih",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-1015"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-01",
+            "phone": "202-366-1015",
+            "primaryITInvestmentUII": "021-031601412",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "rights": "contains sensitive network infomration",
+            "temporal": "R/2010/P1Y",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "NHTSA Asset Framework -"
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
-            "landingPage": "https://data.transportation.gov/d/cnm5-idw3",
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
-            "identifier": "692.37",
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
@@ -39194,29 +39175,52 @@
                     "title": "Sulfur Dioxide"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.37",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/cnm5-idw3",
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
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/cpci-ge2j",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "The Infrastructure Investment and Jobs Act (IIJA) also known as the Bipartisan infrastructure Law contains a large amount of formula funds. This report details those calculations.",
+            "identifier": "https://data.transportation.gov/api/views/cpci-ge2j",
             "issued": "2022-03-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-26",
             "keyword": [
                 "bil",
                 "bil funding",
@@ -39251,38 +39255,52 @@
                 "transportation spend",
                 "transportation spending in iija"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/cpci-ge2j",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-08-26",
+            "phone": "202-366-DATA(3282)",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/cpci-ge2j",
-            "description": "The Infrastructure Investment and Jobs Act (IIJA) also known as the Bipartisan infrastructure Law contains a large amount of formula funds. This report details those calculations.",
-            "title": "Infrastructure Investment and Jobs Act (BIL) Transportation Funding FHWA Formula Funds",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Infrastructure Investment and Jobs Act (BIL) Transportation Funding FHWA Formula Funds"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/cqa4-w97k",
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
+                    "description": "2013 New Hampshire HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/newhampshire2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 New Hampshire"
+                }
+            ],
+            "identifier": "678.133",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -39296,77 +39314,39 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.133",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 New Hampshire",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/cqa4-w97k",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/newhampshire2013.zip",
-                    "description": "2013 New Hampshire HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 New Hampshire"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 New Hampshire"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/cqdc-cm7d",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-07-24",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-29",
-            "keyword": [
-                "bikeshare",
-                "docked bikeshare",
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
-            "identifier": "https://data.transportation.gov/api/views/cqdc-cm7d",
             "description": "List of cities served by a bikeshare and/or e-scooter system in each year starting in 2015. Some systems serve more than one city. The layer lists just the primary city served. Bikeshare includes systems that are open to the general public, IT-automated, and station based (contain hubs to which users can grab and return a bike) as well as dockless systems. The layer includes a count of the number of docking stations, the number of dockless bikeshare systems, and the number of e-scooter systems serving a city (if applicable) in each year. Counts include systems that served an areas for only part of the year.",
-            "title": "Bikeshare (Docked and Dockless) and E-scooter Systems by Year and City Served",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39374,66 +39354,101 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/cqdc-cm7d/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/cqdc-cm7d/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/cqdc-cm7d/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/cqdc-cm7d/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/cqdc-cm7d/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/cqdc-cm7d/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/cqdc-cm7d/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/cqdc-cm7d/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/cqdc-cm7d/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/cqdc-cm7d",
+            "issued": "2024-07-24",
+            "keyword": [
+                "bikeshare",
+                "docked bikeshare",
+                "dockless bikeshare",
+                "e-scooters",
+                "micromobility"
+            ],
+            "landingPage": "https://data.transportation.gov/d/cqdc-cm7d",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-29",
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
+            "title": "Bikeshare (Docked and Dockless) and E-scooter Systems by Year and City Served"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/cqqf-edqf",
-            "issued": "2024-05-10",
             "@type": "dcat:Dataset",
-            "modified": "2024-05-29",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joe McGill",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/cqqf-edqf",
+            "issued": "2024-05-10",
+            "landingPage": "https://data.transportation.gov/d/cqqf-edqf",
+            "modified": "2024-05-29",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "2022 NCFO Ferry Operators"
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
-            "landingPage": "https://data.transportation.gov/d/cr2b-x8iw",
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
+            "identifier": "115.2",
+            "isPartOf": "DOT-115",
+            "issued": "2005-08-09",
             "keyword": [
                 "compliance review",
                 "compliance review effectiveness model",
@@ -39443,60 +39458,60 @@
                 "program effectiveness",
                 "roadside inspection traffic enforcement"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "115.2",
+            "landingPage": "https://data.transportation.gov/d/cr2b-x8iw",
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
```

