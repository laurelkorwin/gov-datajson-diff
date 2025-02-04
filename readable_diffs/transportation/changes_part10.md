# Change History for transportation.json (Part 10)

### Changes from 31606f9 to dd2190f (Part 9/9)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+            "description": "The first major set of trials conducted at the Michigan Test Bed was the Proof of Concept (POC) trials during 2008. The POC trials featured fifty-two RSEs within 45 square miles, 27 vehicles configured with OBEs, and a Dedicated Short-Range Communications (DSRC) network. The testing program had three major phases: subsystem test, system integration and test, and public and private applications test. The public application testing portion of the POC trials were conducted during August 2008. RSE data for the public application tests were available for eight days in August 2008. The data in this data environment consists of RSE and OBE data for the middle six of these days. These six days were chosen for inclusion in the data environment because the first and last days had much higher number of duplicate records and questionable data values.\r\n\r\nIn April 2009 and April 2010 a second and third set of trials was conducted at the Michigan Test Bed, directed by the National Center for Atmospheric Research (NCAR). These trials used a smaller set of vehicles. The April 2009 data concentrated on collecting data during periods of rainy or snowy weather. The April 2010 concentrated on comparing atmospheric data from vehicle-mounted sensors to data from a nearby fixed weather observing station.\r\n\r\nThis legacy dataset was created before data.transportation.gov and is only currently available via the attached file(s). Please contact the dataset owner if there is a need for users to work with this data using the data.transportation.gov analysis features (online viewing, API, graphing, etc.) and the USDOT will consider modifying the dataset to fully integrate in data.transportation.gov.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/download/xz9a-9kps/application/msword",
+                    "mediaType": "application/msword"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/xz9a-9kps",
             "issued": "2012-05-31",
-            "@type": "dcat:Dataset",
-            "temporal": "2009-01-01/2010-12-31",
-            "modified": "2012-05-31",
             "keyword": [
                 "arterial",
                 "connected vehicles",
@@ -105290,50 +105302,56 @@
                 "vehicle infrastructure initiative proof of concept (vii poc)",
                 "weather"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/xz9a-9kps",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://creativecommons.org/licenses/by-nc-sa/3.0/legalcode",
+            "modified": "2012-05-31",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Department of Transportation"
             },
-            "identifier": "https://data.transportation.gov/api/views/xz9a-9kps",
-            "description": "The first major set of trials conducted at the Michigan Test Bed was the Proof of Concept (POC) trials during 2008. The POC trials featured fifty-two RSEs within 45 square miles, 27 vehicles configured with OBEs, and a Dedicated Short-Range Communications (DSRC) network. The testing program had three major phases: subsystem test, system integration and test, and public and private applications test. The public application testing portion of the POC trials were conducted during August 2008. RSE data for the public application tests were available for eight days in August 2008. The data in this data environment consists of RSE and OBE data for the middle six of these days. These six days were chosen for inclusion in the data environment because the first and last days had much higher number of duplicate records and questionable data values.\r\n\r\nIn April 2009 and April 2010 a second and third set of trials was conducted at the Michigan Test Bed, directed by the National Center for Atmospheric Research (NCAR). These trials used a smaller set of vehicles. The April 2009 data concentrated on collecting data during periods of rainy or snowy weather. The April 2010 concentrated on comparing atmospheric data from vehicle-mounted sensors to data from a nearby fixed weather observing station.\r\n\r\nThis legacy dataset was created before data.transportation.gov and is only currently available via the attached file(s). Please contact the dataset owner if there is a need for users to work with this data using the data.transportation.gov analysis features (online viewing, API, graphing, etc.) and the USDOT will consider modifying the dataset to fully integrate in data.transportation.gov.",
-            "title": "NCAR 2009+2010 and VII POC Weather Data",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/download/xz9a-9kps/application/msword",
-                    "mediaType": "application/msword"
-                }
-            ],
             "spatial": "Michigan",
-            "dataQuality": true,
-            "license": "http://creativecommons.org/licenses/by-nc-sa/3.0/legalcode",
-            "accrualPeriodicity": "irregular",
+            "temporal": "2009-01-01/2010-12-31",
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NCAR 2009+2010 and VII POC Weather Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/xzbu-gi3u",
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
+                    "description": "2011 Nebraska HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/nebraska20913.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Nebraska"
+                }
+            ],
+            "identifier": "678.29",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -105347,87 +105365,46 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.29",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Nebraska",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/xzbu-gi3u",
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
-                    "description": "2011 Nebraska HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Nebraska"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Nebraska"
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
-            "landingPage": "https://data.transportation.gov/d/xzge-vx69",
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
-            "identifier": "1841.4",
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
@@ -105436,56 +105413,60 @@
                     "title": "Interactive Access"
                 }
             ],
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/bio/schema.htm",
-            "dataQuality": false,
+            "identifier": "1841.4",
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
+            "landingPage": "https://data.transportation.gov/d/xzge-vx69",
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
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/tollpage/",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/tollpage/",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/y338-mjrk",
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
-            "identifier": "684.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "Biennial report containing selected information on toll facilities in the United States that has been provided to FHWA by the States and/or various toll authorities regarding toll facilities in operation, financed, or under construction as of January 1.",
-            "title": "Toll Facilities in the United States - Toll Facilities in the United States",
-            "isPartOf": "DOT-684",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/tollpage/",
-            "programCode": [
-                "021:011"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -105494,34 +105475,68 @@
                     "title": "Toll Facilities in the United States"
                 }
             ],
-            "spatial": "National, State, Local",
-            "dataQuality": true,
+            "identifier": "684.1",
+            "isPartOf": "DOT-684",
+            "issued": "2013-09-01",
+            "keyword": [
+                "bridges",
+                "highways",
+                "toll facilities"
+            ],
+            "landingPage": "https://data.transportation.gov/d/y338-mjrk",
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
+            "title": "Toll Facilities in the United States - Toll Facilities in the United States"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/frecalls/",
+            "agencyProgramURL": "http://www.nhtsa.gov/",
+            "analysisUnit": "Vehicles , Tires, Child Safety Seats, Equipment",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/y3zb-btaq",
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
+            "identifier": "258.2",
+            "isPartOf": "DOT-258",
+            "issued": "2002-12-16",
             "keyword": [
                 "campaign",
                 "car",
@@ -105533,58 +105548,54 @@
                 "tire",
                 "vehicle"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "258.2",
+            "landingPage": "https://data.transportation.gov/d/y3zb-btaq",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-2315",
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
-            "agencyProgramURL": "http://www.nhtsa.gov/",
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
-            "phone": "202-366-2315",
-            "language": [
-                "en-US"
-            ]
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Foreign Campaigns - Foreign Recalls Search"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.21949/1503770",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2014-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2016-12-20",
-            "references": [
-                "https://rosap.ntl.bts.gov/view/dot/4039"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Transportation Library Data Curator",
+                "hasEmail": "mailto:ntldatacurator@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The objective of this project was to develop system designs for programs to monitor travel time reliability and to prepare a guidebook that practitioners and others can use to design, build, operate, and maintain such systems. Generally, such travel time reliability monitoring systems are built on top of existing traffic monitoring systems. The focus of this project was on travel time reliability. The data from the monitoring systems developed in this project \u2013 from both public and private sources \u2013included, wherever cost-effective, information on the seven sources of non-recurring congestion. This data was used to construct performance measures or to perform various types of analyses useful for operations management as well as performance measurement, planning, and programming. The work on Project L02 began with a research phase. The primary results of Project L02 research were a guidebook and a final report. An additional contribution of the research showed that it may be possible to add the variability of travel time from one segment to another. Another contribution of the research was the development of a queuing point model, an application that analytically determines travel time reliability over a freeway segment. The supporting zip file contains case study datasets for SHRP 2 Report S2-L02-RR1: Establishing Monitoring Programs for Travel Time Reliability, https://rosap.ntl.bts.gov/view/dot/4039  The files are in comma separated value (.csv) format. The compressed zip file is 84.15 MB. These files can be unzipped using any zip compression/decompression software. The .csv files can be read with any basic text editor.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The objective of this project was to develop system designs for programs to monitor travel time reliability and to prepare a guidebook that practitioners and others can use to design, build, operate, and maintain such systems. Generally, such travel time reliability monitoring systems are built on top of existing traffic monitoring systems. The focus of this project was on travel time reliability. The data from the monitoring systems developed in this project \u2013 from both public and private sources \u2013included, wherever cost-effective, information on the seven sources of non-recurring congestion. This data was used to construct performance measures or to perform various types of analyses useful for operations management as well as performance measurement, planning, and programming. The work on Project L02 began with a research phase. The primary results of Project L02 research were a guidebook and a final report. An additional contribution of the research showed that it may be possible to add the variability of travel time from one segment to another. Another contribution of the research was the development of a queuing point model, an application that analytically determines travel time reliability over a freeway segment. The supporting zip file contains case study datasets for SHRP 2 Report S2-L02-RR1: Establishing Monitoring Programs for Travel Time Reliability, https://rosap.ntl.bts.gov/view/dot/4039  The files are in comma separated value (.csv) format. The compressed zip file is 84.15 MB. These files can be unzipped using any zip compression/decompression software. The .csv files can be read with any basic text editor.",
+                    "downloadURL": "https://doi.org/10.21949/1503770",
+                    "mediaType": "application/zip",
+                    "title": "Establishing Monitoring Programs for Travel Time Reliability [supporting datasets]"
+                }
             ],
+            "identifier": "https://data.transportation.gov/api/views/y5rj-ijjm",
+            "issued": "2014-01-01",
             "keyword": [
                 "case studies",
                 "data collection",
@@ -105599,62 +105610,37 @@
                 "travel time",
                 "travel time reliability"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Transportation Library Data Curator",
-                "hasEmail": "mailto:ntldatacurator@dot.gov"
-            },
+            "landingPage": "https://doi.org/10.21949/1503770",
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
-            "identifier": "https://data.transportation.gov/api/views/y5rj-ijjm",
-            "description": "The objective of this project was to develop system designs for programs to monitor travel time reliability and to prepare a guidebook that practitioners and others can use to design, build, operate, and maintain such systems. Generally, such travel time reliability monitoring systems are built on top of existing traffic monitoring systems. The focus of this project was on travel time reliability. The data from the monitoring systems developed in this project \u2013 from both public and private sources \u2013included, wherever cost-effective, information on the seven sources of non-recurring congestion. This data was used to construct performance measures or to perform various types of analyses useful for operations management as well as performance measurement, planning, and programming. The work on Project L02 began with a research phase. The primary results of Project L02 research were a guidebook and a final report. An additional contribution of the research showed that it may be possible to add the variability of travel time from one segment to another. Another contribution of the research was the development of a queuing point model, an application that analytically determines travel time reliability over a freeway segment. The supporting zip file contains case study datasets for SHRP 2 Report S2-L02-RR1: Establishing Monitoring Programs for Travel Time Reliability, https://rosap.ntl.bts.gov/view/dot/4039  The files are in comma separated value (.csv) format. The compressed zip file is 84.15 MB. These files can be unzipped using any zip compression/decompression software. The .csv files can be read with any basic text editor.",
-            "title": "Establishing Monitoring Programs for Travel Time Reliability [supporting datasets]",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://doi.org/10.21949/1503770",
-                    "description": "The objective of this project was to develop system designs for programs to monitor travel time reliability and to prepare a guidebook that practitioners and others can use to design, build, operate, and maintain such systems. Generally, such travel time reliability monitoring systems are built on top of existing traffic monitoring systems. The focus of this project was on travel time reliability. The data from the monitoring systems developed in this project \u2013 from both public and private sources \u2013included, wherever cost-effective, information on the seven sources of non-recurring congestion. This data was used to construct performance measures or to perform various types of analyses useful for operations management as well as performance measurement, planning, and programming. The work on Project L02 began with a research phase. The primary results of Project L02 research were a guidebook and a final report. An additional contribution of the research showed that it may be possible to add the variability of travel time from one segment to another. Another contribution of the research was the development of a queuing point model, an application that analytically determines travel time reliability over a freeway segment. The supporting zip file contains case study datasets for SHRP 2 Report S2-L02-RR1: Establishing Monitoring Programs for Travel Time Reliability, https://rosap.ntl.bts.gov/view/dot/4039  The files are in comma separated value (.csv) format. The compressed zip file is 84.15 MB. These files can be unzipped using any zip compression/decompression software. The .csv files can be read with any basic text editor.",
-                    "@type": "dcat:Distribution",
-                    "title": "Establishing Monitoring Programs for Travel Time Reliability [supporting datasets]"
-                }
+            "references": [
+                "https://rosap.ntl.bts.gov/view/dot/4039"
             ],
             "spatial": "United States, California, New York, Virginia, New Jersey, San Diego (California), Sacramento (California), Atlanta (Georgia)",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "language": [
-                "en-US"
-            ]
+            "title": "Establishing Monitoring Programs for Travel Time Reliability [supporting datasets]"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/y77m-3nfx",
             "bureauCode": [
                 "021:17"
             ],
-            "issued": "2023-12-08",
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
-            "identifier": "https://data.transportation.gov/api/views/y77m-3nfx",
             "description": "Information on the implementation dates of an active or pending insurance policy (posted date, effective date and cancel effective date). In addition to these dates, the record contains the insurance company name, the BI&PD underlying limit and maximum limit amounts, and the DOT number and docket number of the carrier/broker/freight forwarder that holds the policy.\nSee dataset attachment \"FMCSA Dataset Description and Data Definitions - Select Datasets\" for more information.",
-            "title": "ActPendInsur - All With History",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -105662,28 +105648,57 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/y77m-3nfx",
+            "issued": "2023-12-08",
+            "keyword": [
+                "insurance",
+                "motor carrier"
+            ],
+            "landingPage": "https://data.transportation.gov/d/y77m-3nfx",
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
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
+            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/y84d-q5z5",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/11juntvt/11juntvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "June 2011"
+                }
             ],
+            "identifier": "18.9",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -105693,95 +105708,95 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.9",
+            "landingPage": "https://data.transportation.gov/d/y84d-q5z5",
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
-            "title": "Monthly Traffic Volume Trends - June 2011",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/11juntvt/11juntvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "June 2011"
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
+            "title": "Monthly Traffic Volume Trends - June 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/y84q-ayg5",
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
-            "identifier": "https://data.transportation.gov/api/views/y84q-ayg5",
             "description": "Employed persons include people aged 16 years and older in the civilian noninstitutional population who did any work at all as paid employees; worked in their own business, profession, or on their own farm, or worked 15 hours or more as unpaid workers in an enterprise operated by a member of the family; and all those who were not working but who had jobs or businesses from which they were temporarily absent. The Bureau of Labor Statistics produces industry estimates of nonfarm payroll employment as part of the Current Population Survey.",
-            "title": "Transportation Employment - Rail Transportation",
+            "identifier": "https://data.transportation.gov/api/views/y84q-ayg5",
+            "issued": "2025-01-02",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/y84q-ayg5",
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
+            "title": "Transportation Employment - Rail Transportation"
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
-            "landingPage": "https://data.transportation.gov/d/y926-k9b7",
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
+            "identifier": "65.1",
+            "isPartOf": "DOT-65",
+            "issued": "2015-10-05",
             "keyword": [
                 "49",
                 "551",
@@ -105818,61 +105833,62 @@
                 "vin",
                 "vpic"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "65.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "The NHTSA Product Information Catalog and Vehicle Listing (vPIC) is a consolidated platform that presents data collected within the manufacturer reported data from CFR 49 Parts 551 - 574 for use in a variety of modern tools. NHTSA's vPIC platform is intended to serve as a centralized source for basic Vehicle Identification Number (VIN) decoding, Manufacturer Information Database (MID), Manufacturer Equipment Plant Identification and associated data. vPIC is intended to support the Open Data and Transparency initiatives of the agency by allowing the data to be freely used by the public without the burden of manual retrieval from a library of electronic documents (PDFs). While these documents will still be available online for viewing within the Manufacturer Information Database (MID) module of vPIC one can view and use the actual data through the VIN Decoder and Application Programming Interface (API) modules.",
-            "title": "NHTSA Product Information Catalog and Vehicle Listing (vPIC) - MID",
-            "isPartOf": "DOT-65",
-            "agencyProgramURL": "http://vpic.nhtsa.dot.gov/",
+            "landingPage": "https://data.transportation.gov/d/y926-k9b7",
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
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "ftp://ftp.nhtsa.dot.gov/Nits",
+            "agencyProgramURL": "http://www.nhtsa.gov/Data/State+Data+Programs",
+            "analysisUnit": "vehicle crash",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/y9nz-4cdw",
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
+                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/nits/Nontraffic%20crashes/2008/",
+                    "mediaType": "text/plain",
+                    "title": "2008 Nontraffic Crashes"
+                }
             ],
+            "identifier": "288.7",
+            "isPartOf": "DOT-288",
+            "issued": "2009-01-27",
             "keyword": [
                 "crash",
                 "death",
@@ -105888,85 +105904,49 @@
                 "vehicle",
                 "victim"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "288.7",
+            "landingPage": "https://data.transportation.gov/d/y9nz-4cdw",
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
-            "title": "Not in Traffic Surveillance (NiTS) - 2008 Nontraffic Crashes",
-            "isPartOf": "DOT-288",
-            "agencyProgramURL": "http://www.nhtsa.gov/Data/State+Data+Programs",
-            "programCode": [
-                "021:032"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/nits/Nontraffic%20crashes/2008/",
-                    "mediaType": "text/plain",
-                    "title": "2008 Nontraffic Crashes"
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
+            "title": "Not in Traffic Surveillance (NiTS) - 2008 Nontraffic Crashes"
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
-            "landingPage": "https://data.transportation.gov/d/y9rs-6d2f",
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
-            "identifier": "373.3",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": true,
             "description": "Each Freedom of Information Act office uses a case log to track FOIA requests. The logs typically include the dates on which requests were received and closed, control numbers, requester names and descriptions of the requested records.",
-            "title": "Freedom of Information Act Logs for the Office of the Secretary of Transportation - 2009",
-            "isPartOf": "DOT-373",
-            "agencyProgramURL": "http://www.dot.gov/foia",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -105975,45 +105955,52 @@
                     "title": "2009"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "373.3",
+            "isPartOf": "DOT-373",
+            "issued": "2007-12-31",
+            "keyword": [
+                "foia",
+                "freedom of information act",
+                "log",
+                "request"
+            ],
+            "landingPage": "https://data.transportation.gov/d/y9rs-6d2f",
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
+            "title": "Freedom of Information Act Logs for the Office of the Secretary of Transportation - 2009"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://data.transportation.gov/d/y9wr-xk52",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2022-01-27",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-31",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Todd Solomon",
                 "hasEmail": "mailto:todd.solomon@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/y9wr-xk52",
             "description": "",
-            "title": "2017 Commodity Flow Survey Public Use File (CFS PUF)",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -106021,42 +106008,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/y9wr-xk52/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/y9wr-xk52/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/y9wr-xk52/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/y9wr-xk52/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/y9wr-xk52/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/y9wr-xk52/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/y9wr-xk52/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/y9wr-xk52/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/y9wr-xk52/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/y9wr-xk52",
+            "issued": "2022-01-27",
+            "landingPage": "https://data.transportation.gov/d/y9wr-xk52",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2022-01-31",
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
-            "phone": "2023660573"
+            "title": "2017 Commodity Flow Survey Public Use File (CFS PUF)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/yb5b-yd7t",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Devin Simmons",
+                "hasEmail": "mailto:no-reply@data.bts.gov"
+            },
+            "description": "Documentation describing how the 2018 NCFO ferry segment geometry was determined",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/download/yb5b-yd7t/application/pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/yb5b-yd7t",
             "issued": "2020-04-14",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-17",
             "keyword": [
                 "census",
                 "ferry",
@@ -106068,41 +106079,48 @@
                 "transit",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Devin Simmons",
-                "hasEmail": "mailto:no-reply@data.bts.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/yb5b-yd7t",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-06-17",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/yb5b-yd7t",
-            "description": "Documentation describing how the 2018 NCFO ferry segment geometry was determined",
-            "title": "NCFO 2018 Segment Documentation",
-            "programCode": [
-                "021:053"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/download/yb5b-yd7t/application/pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "title": "NCFO 2018 Segment Documentation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/yb7e-tai7",
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
+                    "description": "2013 Hawaii HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/hawaii2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Hawaii"
+                }
+            ],
+            "identifier": "678.115",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -106116,60 +106134,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.115",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Hawaii",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/yb7e-tai7",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/hawaii2013.zip",
-                    "description": "2013 Hawaii HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Hawaii"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Hawaii"
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
-            "landingPage": "https://data.transportation.gov/d/ybah-sew2",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/03dectvt/03dectvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "December 2003"
+                }
             ],
+            "identifier": "18.129",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -106179,118 +106194,83 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.129",
+            "landingPage": "https://data.transportation.gov/d/ybah-sew2",
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
-            "title": "Monthly Traffic Volume Trends - December 2003",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/03dectvt/03dectvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "December 2003"
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
+            "title": "Monthly Traffic Volume Trends - December 2003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ybdw-ip2g",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2025-01-29",
-            "@type": "dcat:Dataset",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:answers@dot.gov"
+            },
+            "description": "Number of trucks entering the United States from Mexico. The Bureau of Transportation of Statistics releases incoming border crossing statistics using data collected at ports of entry by U.S. Customs and Border Protection.",
+            "identifier": "https://data.transportation.gov/api/views/ybdw-ip2g",
+            "issued": "2025-01-29",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ybdw-ip2g",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2025-01-29",
-            "keyword": [
-                "monthly transportation statistics"
+            "programCode": [
+                "021:053"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:answers@dot.gov"
-            },
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/ybdw-ip2g",
-            "description": "Number of trucks entering the United States from Mexico. The Bureau of Transportation of Statistics releases incoming border crossing statistics using data collected at ports of entry by U.S. Customs and Border Protection.",
-            "title": "U.S.-Mexico Incoming Truck Crossings",
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
+            "title": "U.S.-Mexico Incoming Truck Crossings"
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
-            "landingPage": "https://data.transportation.gov/d/ycdf-ukwt",
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
-            "identifier": "125.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": true,
             "description": "Searchable list of cargo tank manufacturers and repair facilities.",
-            "title": "SAFER - Cargo Tank Facility - SAFER - Cargo Tank Facility",
-            "isPartOf": "DOT-125",
-            "agencyProgramURL": "http://mcmis.volpe.dot.gov/mcs150t/pkg_ct_public.prc_ct_public_search",
-            "programCode": [
-                "021:020"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -106299,72 +106279,74 @@
                     "title": "SAFER - Cargo Tank Facility"
                 }
             ],
-            "spatial": "State, National",
-            "dataQuality": true,
+            "identifier": "125.1",
+            "isPartOf": "DOT-125",
+            "issued": "2010-01-26",
+            "keyword": [
+                "cargo tank",
+                "safer",
+                "tank registration.",
+                "usdot number"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ycdf-ukwt",
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
+            "title": "SAFER - Cargo Tank Facility - SAFER - Cargo Tank Facility"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/yd6y-eswf",
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
             "identifier": "https://data.transportation.gov/api/views/yd6y-eswf",
+            "issued": "2024-04-05",
+            "landingPage": "https://data.transportation.gov/d/yd6y-eswf",
+            "modified": "2024-04-05",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Passenger Travel Facts and Figures"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "This dataset contains controlled unclassified information (Information technology systems security information)",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/ydaq-xnhc",
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
-            "identifier": "1632.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
             "description": "This data set contains information about the security and compliance status of FISMA systems within the Department.  The information contains detailed descriptions of FISMA systems, their associated security programs and control configurations, detailed design documentation, audit findings, and Plans of Action and Milestones for any corrective action efforts.",
-            "title": "DOT Cyber Security Assessment Management -",
-            "primaryITInvestmentUII": "021-325711125",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -106372,30 +106354,59 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "theme": [
-                "Transportation"
+            "identifier": "1632.0",
+            "issued": "2014-11-21",
+            "keyword": [
+                "cybersecurity",
+                "information technology",
+                "transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/ydaq-xnhc",
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
+            "title": "DOT Cyber Security Assessment Management -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.21949/1503754",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2016-10-03",
-            "references": [
-                "https://rosap.ntl.bts.gov/view/dot/30882"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Transportation Library Data Curator",
+                "hasEmail": "mailto:ntldatacurator@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The datasets in this zip file are in support of Intelligent Transportation Systems Joint Program Office (ITS JPO) report FHWA-JPO-16-385, \"Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs \u2014 Evaluation Report for ATDM Program,\" https://rosap.ntl.bts.gov/view/dot/32520 and FHWA-JPO-16-373, \"Analysis, modeling, and simulation (AMS) testbed development and evaluation to support dynamic mobility applications (DMA) and active transportation and demand management (ATDM) programs : Dallas testbed analysis plan,\" https://rosap.ntl.bts.gov/view/dot/32106  The files in this zip file are specifically related to the Dallas Testbed. The compressed zip files total 2.2 GB in size. The files have been uploaded as-is; no further documentation was supplied by NTL. All located .docx files were converted to .pdf document files which are an open, archival format. These pdfs were then added to the zip file alongside the original .docx files. These files can be unzipped using any zip compression/decompression software. This zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .cvs text files which can be read using any text editor; .txt text files which can be read using any text editor; .docx document files which can be read in Microsoft Word and some other word processing programs; . xlsx spreadsheet files which can be read in Microsoft Excel and some other spreadsheet programs; .dat data files which may be text or multimedia; as well as GIS or mapping files in the fowlling formats: .mxd, .dbf, .prj, .sbn, .shp., .shp.xml; which may be opened in ArcGIS or other GIS software. [software requirements] These files were last accessed in 2017.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The datasets in this zip file are in support of Intelligent Transportation Systems Joint Program Office (ITS JPO) report FHWA-JPO-16-385, \"Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs \u2014 Evaluation Report for ATDM Program,\" https://rosap.ntl.bts.gov/view/dot/32520 and FHWA-JPO-16-373, \"Analysis, modeling, and simulation (AMS) testbed development and evaluation to support dynamic mobility applications (DMA) and active transportation and demand management (ATDM) programs : Dallas testbed analysis plan,\" https://rosap.ntl.bts.gov/view/dot/32106  The files in this zip file are specifically related to the Dallas Testbed. The compressed zip files total 2.2 GB in size. The files have been uploaded as-is; no further documentation was supplied by NTL. All located .docx files were converted to .pdf document files which are an open, archival format. These pdfs were then added to the zip file alongside the original .docx files. These files can be unzipped using any zip compression/decompression software. This zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .cvs text files which can be read using any text editor; .txt text files which can be read using any text editor; .docx document files which can be read in Microsoft Word and some other word processing programs; . xlsx spreadsheet files which can be read in Microsoft Excel and some other spreadsheet programs; .dat data files which may be text or multimedia; as well as GIS or mapping files in the fowlling formats: .mxd, .dbf, .prj, .sbn, .shp., .shp.xml; which may be opened in ArcGIS or other GIS software. [software requirements] These files were last accessed in 2017.",
+                    "downloadURL": "https://doi.org/10.21949/1503754",
+                    "mediaType": "application/zip",
+                    "title": "Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs: Dallas Testbed Analysis Plan [supporting datasets]"
+                }
             ],
+            "identifier": "https://data.transportation.gov/api/views/ye89-ffft",
+            "issued": "2017-07-26",
             "keyword": [
                 "active transportation and demand management",
                 "ams dallas",
@@ -106411,51 +106422,55 @@
                 "traffic flow",
                 "travel demand"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Transportation Library Data Curator",
-                "hasEmail": "mailto:ntldatacurator@dot.gov"
-            },
+            "landingPage": "https://doi.org/10.21949/1503754",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2016-10-03",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/ye89-ffft",
-            "description": "The datasets in this zip file are in support of Intelligent Transportation Systems Joint Program Office (ITS JPO) report FHWA-JPO-16-385, \"Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs \u2014 Evaluation Report for ATDM Program,\" https://rosap.ntl.bts.gov/view/dot/32520 and FHWA-JPO-16-373, \"Analysis, modeling, and simulation (AMS) testbed development and evaluation to support dynamic mobility applications (DMA) and active transportation and demand management (ATDM) programs : Dallas testbed analysis plan,\" https://rosap.ntl.bts.gov/view/dot/32106  The files in this zip file are specifically related to the Dallas Testbed. The compressed zip files total 2.2 GB in size. The files have been uploaded as-is; no further documentation was supplied by NTL. All located .docx files were converted to .pdf document files which are an open, archival format. These pdfs were then added to the zip file alongside the original .docx files. These files can be unzipped using any zip compression/decompression software. This zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .cvs text files which can be read using any text editor; .txt text files which can be read using any text editor; .docx document files which can be read in Microsoft Word and some other word processing programs; . xlsx spreadsheet files which can be read in Microsoft Excel and some other spreadsheet programs; .dat data files which may be text or multimedia; as well as GIS or mapping files in the fowlling formats: .mxd, .dbf, .prj, .sbn, .shp., .shp.xml; which may be opened in ArcGIS or other GIS software. [software requirements] These files were last accessed in 2017.",
-            "title": "Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs: Dallas Testbed Analysis Plan [supporting datasets]",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://doi.org/10.21949/1503754",
-                    "description": "The datasets in this zip file are in support of Intelligent Transportation Systems Joint Program Office (ITS JPO) report FHWA-JPO-16-385, \"Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs \u2014 Evaluation Report for ATDM Program,\" https://rosap.ntl.bts.gov/view/dot/32520 and FHWA-JPO-16-373, \"Analysis, modeling, and simulation (AMS) testbed development and evaluation to support dynamic mobility applications (DMA) and active transportation and demand management (ATDM) programs : Dallas testbed analysis plan,\" https://rosap.ntl.bts.gov/view/dot/32106  The files in this zip file are specifically related to the Dallas Testbed. The compressed zip files total 2.2 GB in size. The files have been uploaded as-is; no further documentation was supplied by NTL. All located .docx files were converted to .pdf document files which are an open, archival format. These pdfs were then added to the zip file alongside the original .docx files. These files can be unzipped using any zip compression/decompression software. This zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .cvs text files which can be read using any text editor; .txt text files which can be read using any text editor; .docx document files which can be read in Microsoft Word and some other word processing programs; . xlsx spreadsheet files which can be read in Microsoft Excel and some other spreadsheet programs; .dat data files which may be text or multimedia; as well as GIS or mapping files in the fowlling formats: .mxd, .dbf, .prj, .sbn, .shp., .shp.xml; which may be opened in ArcGIS or other GIS software. [software requirements] These files were last accessed in 2017.",
-                    "@type": "dcat:Distribution",
-                    "title": "Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs: Dallas Testbed Analysis Plan [supporting datasets]"
-                }
+            "references": [
+                "https://rosap.ntl.bts.gov/view/dot/30882"
             ],
             "spatial": "United States, Texas, Dallas",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "language": [
-                "en-US"
-            ]
+            "title": "Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs: Dallas Testbed Analysis Plan [supporting datasets]"
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
-            "landingPage": "https://data.transportation.gov/d/yeac-qr2g",
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
+                    "downloadURL": "http://ai.fmcsa.dot.gov/pe/IRModelPg.aspx",
+                    "mediaType": "text/html",
+                    "title": "Intervention Model"
+                }
             ],
+            "identifier": "115.4",
+            "isPartOf": "DOT-115",
+            "issued": "2005-08-09",
             "keyword": [
                 "compliance review",
                 "compliance review effectiveness model",
@@ -106465,80 +106480,43 @@
                 "program effectiveness",
                 "roadside inspection traffic enforcement"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "115.4",
+            "landingPage": "https://data.transportation.gov/d/yeac-qr2g",
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
-            "title": "A&I - Program Effectiveness - Intervention Model",
-            "isPartOf": "DOT-115",
-            "agencyProgramURL": "http://ai.fmcsa.dot.gov/pe/Home.aspx",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://ai.fmcsa.dot.gov/pe/IRModelPg.aspx",
-                    "mediaType": "text/html",
-                    "title": "Intervention Model"
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
+            "title": "A&I - Program Effectiveness - Intervention Model"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2021-01-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "fhwa",
-                "traffic volume trends",
-                "travel",
-                "tvt",
-                "vehicle miles traveled",
-                "vmt",
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
-            "identifier": "https://data.transportation.gov/api/views/yeig-3uz6",
+            "dataQuality": true,
             "description": "This dataset contains the estimates of the vehicle miles traveled (VMT) for interstate highways and how the total travel measured by VMT compares with travel that occurred in the same week of the previous year.",
-            "title": "Weekly Traffic Volume",
-            "primaryITInvestmentUII": "021-938741189",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -106546,51 +106524,88 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/yeig-3uz6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/yeig-3uz6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/yeig-3uz6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/yeig-3uz6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/yeig-3uz6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/yeig-3uz6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/yeig-3uz6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/yeig-3uz6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/yeig-3uz6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "systemOfRecords": "https://www.govinfo.gov/content/pkg/FR-2006-05-03/pdf/E6-6510.pdf",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/yeig-3uz6",
+            "issued": "2021-01-13",
+            "keyword": [
+                "fhwa",
+                "traffic volume trends",
+                "travel",
+                "tvt",
+                "vehicle miles traveled",
+                "vmt",
+                "weekly"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-05-08",
+            "primaryITInvestmentUII": "021-938741189",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "systemOfRecords": "https://www.govinfo.gov/content/pkg/FR-2006-05-03/pdf/E6-6510.pdf",
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Weekly Traffic Volume"
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
-            "landingPage": "https://data.transportation.gov/d/yeq6-t3dk",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/04maytvt/04maytvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "May 2004"
+                }
             ],
+            "identifier": "18.124",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -106600,86 +106615,51 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.124",
+            "landingPage": "https://data.transportation.gov/d/yeq6-t3dk",
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
-            "title": "Monthly Traffic Volume Trends - May 2004",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/04maytvt/04maytvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "May 2004"
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
+            "title": "Monthly Traffic Volume Trends - May 2004"
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
-            "landingPage": "https://data.transportation.gov/d/yerr-upki",
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
-            "identifier": "81.6",
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
@@ -106688,40 +106668,50 @@
                     "title": "Complaints Search"
                 }
             ],
-            "spatial": "N/A",
-            "describedBy": "http://www-odi.nhtsa.dot.gov/downloads/folders/Complaints/CMPL.txt",
-            "dataQuality": true,
+            "identifier": "81.6",
+            "isPartOf": "DOT-81",
+            "issued": "2002-12-16",
+            "keyword": [
+                "complaints",
+                "email",
+                "paper",
+                "phone",
+                "safercar.gov"
+            ],
+            "landingPage": "https://data.transportation.gov/d/yerr-upki",
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
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Complaints - Complaints Search"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/yfpm-y6yv",
-            "issued": "2023-11-09",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/yfpm-y6yv",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "Rail Crossings",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -106729,96 +106719,89 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/yfpm-y6yv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/yfpm-y6yv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/yfpm-y6yv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/yfpm-y6yv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/yfpm-y6yv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/yfpm-y6yv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/yfpm-y6yv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/yfpm-y6yv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/yfpm-y6yv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/yfpm-y6yv",
+            "issued": "2023-11-09",
+            "landingPage": "https://data.transportation.gov/d/yfpm-y6yv",
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
-            "landingPage": "https://data.transportation.gov/d/yh67-9te8",
             "bureauCode": [
                 "021:27"
             ],
-            "issued": "2024-08-06",
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
-            "identifier": "https://data.transportation.gov/api/views/yh67-9te8",
+            "dataQuality": true,
             "description": "This is the landing page for 49 CFR Part 225 Railroad Accident, incident, Casualty and Operational data.",
-            "title": "Data Downloads - Landing Page",
+            "identifier": "https://data.transportation.gov/api/views/yh67-9te8",
+            "issued": "2024-08-06",
+            "landingPage": "https://data.transportation.gov/d/yh67-9te8",
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
+            "title": "Data Downloads - Landing Page"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://data.transportation.gov/d/yhdk-w2wt",
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
-                "automation",
-                "building",
-                "control"
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
-            "identifier": "427.0",
+            "dataQuality": false,
             "description": "This data set contains information integral to the operation for the DOT Headquarters building, to include floor plans, fire control systems, air handling systems, lighting systems, and elevator systems.",
-            "title": "Building Automation Data -",
-            "primaryITInvestmentUII": "021-378427864",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -106826,55 +106809,53 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
+            "identifier": "427.0",
+            "issued": "2014-09-16",
+            "keyword": [
+                "automation",
+                "building",
+                "control"
+            ],
+            "landingPage": "https://data.transportation.gov/d/yhdk-w2wt",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "accrualPeriodicity": "R/PT1S",
+            "modified": "2024-11-14",
+            "phone": "202-366-0046",
+            "primaryITInvestmentUII": "021-378427864",
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
+            "title": "Building Automation Data -"
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
-            "landingPage": "https://data.transportation.gov/d/yiqj-3kme",
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
-            "identifier": "319.2",
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
@@ -106882,49 +106863,51 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "319.2",
+            "isPartOf": "DOT-319",
+            "issued": "2011-01-18",
+            "keyword": [
+                "data.gov",
+                "law",
+                "significant guidance",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/yiqj-3kme",
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
-            "landingPage": "https://data.transportation.gov/d/yirh-jy8u",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-09-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-30",
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
-            "identifier": "https://data.transportation.gov/api/views/yirh-jy8u",
             "description": "Source: U.S. Department of Transportation, Bureau of Transportation Statistics, based upon U.S. Department of Commerce, U.S. Census Bureau, Foreign Trade Division, USA Trade Online \"HS Port-level Data\", available at https://usatrade.census.gov/ as of Sept 2024.",
-            "title": "Top 10 Containerized Export Commodities Shipping Weight (kg) by Coast, 2023",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -106932,69 +106915,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/yirh-jy8u/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/yirh-jy8u/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/yirh-jy8u/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/yirh-jy8u/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/yirh-jy8u/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/yirh-jy8u/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/yirh-jy8u/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/yirh-jy8u/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/yirh-jy8u/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/yirh-jy8u",
+            "issued": "2024-09-30",
+            "keyword": [
+                "commodity",
+                "containers",
+                "ports"
+            ],
+            "landingPage": "https://data.transportation.gov/d/yirh-jy8u",
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-09-30",
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
+            "title": "Top 10 Containerized Export Commodities Shipping Weight (kg) by Coast, 2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/yj5y-b2ir",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2019-02-21",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
-            "keyword": [
-                "airfares",
-                "aviation",
-                "aviation policy",
-                "city pair",
-                "city pair markets",
-                "consumer airfare report",
-                "fare levels",
-                "fares",
-                "office of aviation analysis",
-                "table 6"
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
-            "identifier": "https://data.transportation.gov/api/views/yj5y-b2ir",
+            "dataQuality": true,
             "description": "Available on the internet only, this table is an expanded version of Table 1 that lists all city-pair markets in the contiguous United States that average at least 10 passengers each day.  All records are aggregated as directionless city pair markets.  All traffic traveling in both directions is added together.\r\nhttps://www.transportation.gov/policy/aviation-policy/competition-data-analysis/research-reports",
-            "title": "Consumer Airfare Report: Table 6 - Contiguous State City-Pair Markets That Average At Least 10 Passengers Per Day",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -107002,73 +106979,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/yj5y-b2ir/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/yj5y-b2ir/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/yj5y-b2ir/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/yj5y-b2ir/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/yj5y-b2ir/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/yj5y-b2ir/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/yj5y-b2ir/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/yj5y-b2ir/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/yj5y-b2ir/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/yj5y-b2ir",
+            "issued": "2019-02-21",
+            "keyword": [
+                "airfares",
+                "aviation",
+                "aviation policy",
+                "city pair",
+                "city pair markets",
+                "consumer airfare report",
+                "fare levels",
+                "fares",
+                "office of aviation analysis",
+                "table 6"
+            ],
+            "landingPage": "https://data.transportation.gov/d/yj5y-b2ir",
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
+            "title": "Consumer Airfare Report: Table 6 - Contiguous State City-Pair Markets That Average At Least 10 Passengers Per Day"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/yjfw-8zsx",
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
-            "identifier": "https://data.transportation.gov/api/views/yjfw-8zsx",
             "description": "Part of Wyoming Department of Transportation Connected Vehicle Pilot Phase 4. Test case WV2IMCT-1 Verify V2I communication for log file offload.",
-            "title": "LTE-V2X Wyoming Connected Vehicle Pilot test ID WV2IMCT-1",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -107076,118 +107048,123 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/yjfw-8zsx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/yjfw-8zsx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/yjfw-8zsx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/yjfw-8zsx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/yjfw-8zsx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/yjfw-8zsx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/yjfw-8zsx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/yjfw-8zsx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/yjfw-8zsx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Wyoming",
+            "identifier": "https://data.transportation.gov/api/views/yjfw-8zsx",
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
+            "landingPage": "https://data.transportation.gov/d/yjfw-8zsx",
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
+            "title": "LTE-V2X Wyoming Connected Vehicle Pilot test ID WV2IMCT-1"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/yjr3-piic",
-            "issued": "2022-09-20",
             "@type": "dcat:Dataset",
-            "modified": "2022-09-28",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/yjr3-piic",
+            "issued": "2022-09-20",
+            "landingPage": "https://data.transportation.gov/d/yjr3-piic",
+            "modified": "2022-09-28",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
-            "title": "Population and Geography",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "Population and Geography"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/yjuu-vthc",
-            "issued": "2022-06-21",
             "@type": "dcat:Dataset",
-            "modified": "2022-09-20",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/yjuu-vthc",
+            "issued": "2022-06-21",
+            "landingPage": "https://data.transportation.gov/d/yjuu-vthc",
+            "modified": "2022-09-20",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
-            "title": "Travel Demand",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "Travel Demand"
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
-            "landingPage": "https://data.transportation.gov/d/ykhq-jh4a",
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
-            "identifier": "1841.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/bio/schema.htm",
             "description": "The NHTSA Biomechanics Test Database is a repository of experimental data used by NHTSA for developing Anthropomophic Test Devices and associated Injury Criteria. The data is disseminated via this website for use by academia, the automotive industry, and the public to improve the safety of automobiles and reduce death and injuries on our nations highway. Because of the nature of the testing, the applicability of the data extends far beyond auto safety, and may be useful for those in the sports medicine, space travel, aircraft, military or any activity where the human body is exposed impact.",
-            "title": "Biomechanics Test Database - Zipped ASCII Export",
-            "isPartOf": "DOT-1841",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research",
-            "primaryITInvestmentUII": "021-961265599",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -107196,31 +107173,72 @@
                     "title": "Zipped ASCII Export"
                 }
             ],
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/bio/schema.htm",
-            "dataQuality": false,
+            "identifier": "1841.1",
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
+            "landingPage": "https://data.transportation.gov/d/ykhq-jh4a",
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
+            "title": "Biomechanics Test Database - Zipped ASCII Export"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/ykj2-6cf4",
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
+                    "description": "2011 South Carolina HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/southcarolina2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 South Carolina"
+                }
+            ],
+            "identifier": "678.42",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -107234,80 +107252,46 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.42",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 South Carolina",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/ykj2-6cf4",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/southcarolina2011.zip",
-                    "description": "2011 South Carolina HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 South Carolina"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 South Carolina"
         },
         {
-            "accessLevel": "public",
-            "bureauCode": [
-                "021:18"
-            ],
-            "landingPage": "https://data.transportation.gov/d/ykmj-nsd9",
-            "issued": "2018-12-17",
-            "temporal": "2009-07-01/2011-09-30",
             "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
-            "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Transaction+Data+and+Reports"
-            ],
-            "keyword": [
-                "cars",
-                "trade-in"
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Transaction+Data+and+Reports",
+            "agencyProgramURL": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Officially+Ended",
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
-            "identifier": "DOT-11",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
+            "describedBy": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Transaction+Data+and+Reports",
             "description": "The Car Allowance Rebate System (CARS), otherwise known as Cash for Clunkers, was a program intended to provide economic incentives to United States residents to purchase a new and more fuel efficient vehicle when trading in a less full efficient vehicle. The program was promoted as providing stimulus to the economy by boosting auto sales, while putting safer, cleaner and more fuel efficient vehicles on the road.",
-            "title": "Car Allowance Rebate System (CARS) - Trade-In Vehicles",
-            "agencyProgramURL": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Officially+Ended",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -107316,60 +107300,55 @@
                     "title": "Consumer Survey csv file"
                 }
             ],
-            "spatial": "N/A",
-            "describedBy": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Transaction+Data+and+Reports",
-            "dataQuality": false,
+            "identifier": "DOT-11",
+            "issued": "2018-12-17",
+            "keyword": [
+                "cars",
+                "trade-in"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ykmj-nsd9",
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
+            "title": "Car Allowance Rebate System (CARS) - Trade-In Vehicles"
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
-            "landingPage": "https://data.transportation.gov/d/ykp9-f22h",
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
-            "identifier": "524.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
             "description": "STATE DATA REPORTING SYSTEMS. Annual reports on the Fatality Analysis Reporting System (FARS) which is data regarding fatalities that is collected by a FARS analyst from each State and provided to NHTSA.",
-            "title": "GES Reports - 2000",
-            "isPartOf": "DOT-524",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -107378,48 +107357,54 @@
                     "title": "2000"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
-            "dataQuality": true,
+            "identifier": "524.2",
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
+            "landingPage": "https://data.transportation.gov/d/ykp9-f22h",
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
+            "title": "GES Reports - 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ykrj-s4zj",
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
-            "identifier": "https://data.transportation.gov/api/views/ykrj-s4zj",
+            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
             "description": "State DOTs provide the location limits of highway sections to be used to represent statewide aggregations based on a statistically valid Sample Panel.\nThe South contains data for the following States: Alabama, Arkansas, Florida, Georgia, Kentucky, Louisiana, Mississippi, North Carolina, South Carolina, Tennessee, Virginia, West Virginia, and Puerto Rico.",
-            "title": "Roadway Sections South 2019",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -107427,48 +107412,81 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ykrj-s4zj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ykrj-s4zj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ykrj-s4zj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ykrj-s4zj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ykrj-s4zj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ykrj-s4zj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ykrj-s4zj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ykrj-s4zj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ykrj-s4zj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "USA",
-            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
+            "identifier": "https://data.transportation.gov/api/views/ykrj-s4zj",
+            "issued": "2020-12-28",
+            "landingPage": "https://data.transportation.gov/d/ykrj-s4zj",
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
+            "title": "Roadway Sections South 2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/ym77-x9wi",
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
+                    "description": "2012 South Dakota HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/southdakota2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 South Dakota"
+                }
+            ],
+            "identifier": "678.95",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -107482,82 +107500,46 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.95",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 South Dakota",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/ym77-x9wi",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/southdakota2012.zip",
-                    "description": "2012 South Dakota HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 South Dakota"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 South Dakota"
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
-            "landingPage": "https://data.transportation.gov/d/ym7g-3qzs",
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
-            "identifier": "364.22",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2004",
-            "isPartOf": "DOT-364",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
-            "primaryITInvestmentUII": "021-621341357",
-            "programCode": [
-                "021:035"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -107566,49 +107548,51 @@
                     "title": "Event Data Records Reports - 2004"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.22",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ym7g-3qzs",
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
+            "title": "Vehicle Safety Research and Development Database - Event Data Records Reports - 2004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ymmm-mwzp",
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
-            "identifier": "https://data.transportation.gov/api/views/ymmm-mwzp",
+            "dataQuality": true,
             "description": "2020 Traffic Volume Data - FHWA's TMAS Data Program (based on unweighted raw continuous traffic count information collected by state highway agencies)",
-            "title": "TMAS 2020",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -107616,48 +107600,82 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ymmm-mwzp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ymmm-mwzp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ymmm-mwzp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ymmm-mwzp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ymmm-mwzp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ymmm-mwzp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ymmm-mwzp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ymmm-mwzp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ymmm-mwzp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/ymmm-mwzp",
+            "issued": "2021-04-30",
+            "keyword": [
+                "traffic",
+                "traffic volume trends"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ymmm-mwzp",
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
+            "title": "TMAS 2020"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/ynu4-6saz",
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
+                    "description": "2013 New Mexico HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/newmexico2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 New Mexico"
+                }
+            ],
+            "identifier": "678.135",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -107671,71 +107689,39 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.135",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 New Mexico",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/ynu4-6saz",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/newmexico2013.zip",
-                    "description": "2013 New Mexico HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 New Mexico"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 New Mexico"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ypjt-5ydn",
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
-            "identifier": "https://data.transportation.gov/api/views/ypjt-5ydn",
             "description": "*Dataset*  Records for carrier/broker/freight forwarder active or pending individual insurance policies. The records are linked to the entities by docket numbers included in the dataset. The dataset contains information on the insurance policy, including insurance company name, policy number and type of insurance. Entities can hold multiple insurance policies, so there may be multiple records associated with a particular entity. See dataset attachment \"FMCSA Dataset Description and Data Definitions - Select Datasets\" for more information.",
-            "title": "Insur - All With History",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -107743,70 +107729,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ypjt-5ydn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ypjt-5ydn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ypjt-5ydn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ypjt-5ydn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ypjt-5ydn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ypjt-5ydn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ypjt-5ydn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ypjt-5ydn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ypjt-5ydn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/ypjt-5ydn",
+            "issued": "2024-02-02",
+            "keyword": [
+                "insurance",
+                "motor carrier"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ypjt-5ydn",
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
+            "title": "Insur - All With History"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/statistics.cfm",
+            "accrualPeriodicity": "Annual",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2018-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "keyword": [
-                "fatalities",
-                "functional system",
-                "lane-miles",
-                "mileage",
-                "rural/urban",
-                "state",
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
-            "identifier": "https://data.transportation.gov/api/views/ystz-43ti",
+            "dataQuality": true,
             "description": "Select summary highway statistics, 1980 - 2017, mileage, lane-miles, vehicle miles traveled, and fatalities by state and functional system.",
-            "title": "Select Summary Highway Statistics, by State and Functional System",
-            "isPartOf": "Highway Statistics",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -107814,169 +107792,206 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ystz-43ti/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ystz-43ti/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ystz-43ti/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ystz-43ti/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ystz-43ti/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ystz-43ti/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ystz-43ti/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ystz-43ti/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ystz-43ti/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/ystz-43ti",
+            "isPartOf": "Highway Statistics",
+            "issued": "2018-12-31",
+            "keyword": [
+                "fatalities",
+                "functional system",
+                "lane-miles",
+                "mileage",
+                "rural/urban",
+                "state",
+                "vehicle miles traveled",
+                "vmt"
+            ],
+            "landingPage": "https://www.fhwa.dot.gov/policyinformation/statistics.cfm",
+            "language": [
+                "English"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "Annual",
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
+            "title": "Select Summary Highway Statistics, by State and Functional System"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ytc4-m58z",
-            "issued": "2020-12-07",
             "@type": "dcat:Dataset",
-            "modified": "2021-08-04",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/ytc4-m58z",
+            "issued": "2020-12-07",
+            "landingPage": "https://data.transportation.gov/d/ytc4-m58z",
+            "modified": "2021-08-04",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
-            "title": "Geospatial (GIS) Metadata User Guide",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "Geospatial (GIS) Metadata User Guide"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ytfx-7hgq",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2020-06-29",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-16",
-            "keyword": [
-                "arterial",
-                "automated vehicles",
-                "connected vehicles",
-                "deployment tracking survey (dts)",
-                "freeway",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "its knowledge resources",
-                "survey data",
-                "transit"
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
-            "identifier": "https://data.transportation.gov/api/views/ytfx-7hgq",
+            "dataQuality": true,
             "description": "The Intelligent Transportation Systems (ITS) Deployment Tracking Survey (DTS) Data Repository contains a set of downloadable electronic files related to a series of ITS surveys conducted over the past twenty years. Surveys included in the repository are divided into three main categories: ITS Deployment Tracking Surveys (1999 to 2020), the 2019 Connected and Automated Vehicle (CV/AV) Survey, and Special Topic Deployment Surveys.\n\nThis data is a product of the ITS JPO's ITS Evaluation Program.",
-            "title": "Intelligent Transportation Systems (ITS) Deployment Tracking Survey Data Repository",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.itskrs.its.dot.gov/deployment/2020DTS",
-                    "description": "The 2020 ITS Deployment Tracking Survey Data Repository page includes: 1) the survey instruments that were administered to Arterial, Freeway, and Transit Management agencies to collect deployment data, 2) data file workbooks associated with the survey responses, and 3) final reports summarizing key findings from the surveys.",
                     "@type": "dcat:Distribution",
+                    "description": "The 2020 ITS Deployment Tracking Survey Data Repository page includes: 1) the survey instruments that were administered to Arterial, Freeway, and Transit Management agencies to collect deployment data, 2) data file workbooks associated with the survey responses, and 3) final reports summarizing key findings from the surveys.",
+                    "downloadURL": "https://www.itskrs.its.dot.gov/deployment/2020DTS",
+                    "mediaType": "text/html",
                     "title": "ITS Deployment - Survey Instruments, Survey Data, Survey Reports (2020)"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.itskrs.its.dot.gov/deployment/2019cvav",
-                    "description": "The ITS Deployment Tracking Survey (DTS) Data Repository page holding the 2019 Connected Vehicle and Automated Vehicle (CV/AV) Survey data, codebook, and final report. The 2019 CV/AV Survey was administered as part of an ongoing effort by the ITS JPO to track the deployment of ITS. The 2019 CV/AV survey differs from previous DTS surveys, focusing only on CV and AV technologies. It was designed to understand the current levels of CV and AV testing/deployment, agencies\u2019 level of readiness with respect to CV and AV, key challenges and barriers to CV and AV deployment, and the assistance/resources needed to overcome challenges and barriers.",
                     "@type": "dcat:Distribution",
+                    "description": "The ITS Deployment Tracking Survey (DTS) Data Repository page holding the 2019 Connected Vehicle and Automated Vehicle (CV/AV) Survey data, codebook, and final report. The 2019 CV/AV Survey was administered as part of an ongoing effort by the ITS JPO to track the deployment of ITS. The 2019 CV/AV survey differs from previous DTS surveys, focusing only on CV and AV technologies. It was designed to understand the current levels of CV and AV testing/deployment, agencies\u2019 level of readiness with respect to CV and AV, key challenges and barriers to CV and AV deployment, and the assistance/resources needed to overcome challenges and barriers.",
+                    "downloadURL": "https://www.itskrs.its.dot.gov/deployment/2019cvav",
+                    "mediaType": "text/html",
                     "title": "ITS Deployment - Connected Vehicle and Automated Vehicle (CV/AV) Survey (2019)"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.itskrs.its.dot.gov/deployment/othersurveys",
-                    "description": "The ITS Deployment Tracking Survey Data Repository page holding downloadable Special Topic Deployment Survey data such as the 2019 Small Urban and Rural Transit survey.",
                     "@type": "dcat:Distribution",
+                    "description": "The ITS Deployment Tracking Survey Data Repository page holding downloadable Special Topic Deployment Survey data such as the 2019 Small Urban and Rural Transit survey.",
+                    "downloadURL": "https://www.itskrs.its.dot.gov/deployment/othersurveys",
+                    "mediaType": "text/html",
                     "title": "ITS Deployment - Special Topic Deployment Surveys"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.itskrs.its.dot.gov/deployment/finalreports",
-                    "description": "The ITS Deployment Tracking Survey Data Repository page holding the complete set of downloadable Final Reports associated with each Intelligent Transportation Systems (ITS) Deployment Tracking Survey (DTS) conducted from 1999 to 2016.",
                     "@type": "dcat:Distribution",
+                    "description": "The ITS Deployment Tracking Survey Data Repository page holding the complete set of downloadable Final Reports associated with each Intelligent Transportation Systems (ITS) Deployment Tracking Survey (DTS) conducted from 1999 to 2016.",
+                    "downloadURL": "https://www.itskrs.its.dot.gov/deployment/finalreports",
+                    "mediaType": "text/html",
                     "title": "ITS Deployment - Final Reports (1999-2016)"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.itskrs.its.dot.gov/deployment/commonquestions",
-                    "description": "The ITS Deployment Tracking Survey Data Repository page holding three files (one for each survey type \u2013 Freeway, Arterial, and Transit) that group common questions across the surveys conducted from 1999 to 2016. The questions are organized by key topic areas (e.g., in the Arterial file, a user can view all questions on adaptive signal control and how they were asked across the survey years).",
                     "@type": "dcat:Distribution",
+                    "description": "The ITS Deployment Tracking Survey Data Repository page holding three files (one for each survey type \u2013 Freeway, Arterial, and Transit) that group common questions across the surveys conducted from 1999 to 2016. The questions are organized by key topic areas (e.g., in the Arterial file, a user can view all questions on adaptive signal control and how they were asked across the survey years).",
+                    "downloadURL": "https://www.itskrs.its.dot.gov/deployment/commonquestions",
+                    "mediaType": "text/html",
                     "title": "ITS Deployment - Common Survey Questions (1999-2016)"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.itskrs.its.dot.gov/deployment/surveys",
-                    "description": "The ITS Deployment Tracking Survey Data Repository page holding Arterial, Freeway, and Transit Management survey instruments used to collect deployment data each year a survey was conducted.",
                     "@type": "dcat:Distribution",
+                    "description": "The ITS Deployment Tracking Survey Data Repository page holding Arterial, Freeway, and Transit Management survey instruments used to collect deployment data each year a survey was conducted.",
+                    "downloadURL": "https://www.itskrs.its.dot.gov/deployment/surveys",
+                    "mediaType": "text/html",
                     "title": "ITS Deployment - Survey Instruments (1999 - 2016)"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.itskrs.its.dot.gov/deployment/depdata",
-                    "description": "The ITS Deployment Tracking Survey Data Repository page holding Excel data file workbooks associated with the Arterial, Freeway, and Transit surveys. Each Excel data file workbook contains three worksheets (Data, Data Dictionary, and Variable Summary Statistics).",
                     "@type": "dcat:Distribution",
+                    "description": "The ITS Deployment Tracking Survey Data Repository page holding Excel data file workbooks associated with the Arterial, Freeway, and Transit surveys. Each Excel data file workbook contains three worksheets (Data, Data Dictionary, and Variable Summary Statistics).",
+                    "downloadURL": "https://www.itskrs.its.dot.gov/deployment/depdata",
+                    "mediaType": "text/html",
                     "title": "ITS Deployment - Survey Data (1999-2016)"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/ytfx-7hgq",
+            "issued": "2020-06-29",
+            "keyword": [
+                "arterial",
+                "automated vehicles",
+                "connected vehicles",
+                "deployment tracking survey (dts)",
+                "freeway",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "its knowledge resources",
+                "survey data",
+                "transit"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ytfx-7hgq",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2021-02-16",
+            "programCode": [
+                "021:013"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Intelligent Transportation Systems (ITS) Deployment Tracking Survey Data Repository"
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
-            "landingPage": "https://data.transportation.gov/d/ytkb-2vxm",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/10augtvt/10augtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "August 2010"
+                }
             ],
+            "identifier": "18.19",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -107986,90 +108001,80 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.19",
+            "landingPage": "https://data.transportation.gov/d/ytkb-2vxm",
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
-            "title": "Monthly Traffic Volume Trends - August 2010",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/10augtvt/10augtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "August 2010"
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
+            "title": "Monthly Traffic Volume Trends - August 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/yu2w-ew3p",
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
-            "identifier": "https://data.transportation.gov/api/views/yu2w-ew3p",
             "description": "Employed persons include people aged 16 years and older in the civilian noninstitutional population who did any work at all as paid employees; worked in their own business, profession, or on their own farm, or worked 15 hours or more as unpaid workers in an enterprise operated by a member of the family; and all those who were not working but who had jobs or businesses from which they were temporarily absent. The Bureau of Labor Statistics produces industry estimates of nonfarm payroll employment as part of the Current Population Survey.",
-            "title": "Transportation Employment - Truck Transportation",
+            "identifier": "https://data.transportation.gov/api/views/yu2w-ew3p",
+            "issued": "2025-01-02",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/yu2w-ew3p",
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
+            "title": "Transportation Employment - Truck Transportation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/yu7w-ucji",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRA Safety Data Team",
+                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This is the report for Fatalities, Injuries, and Illnesses in Train Accidents, Highway-Rail Incidents, and Other Incidents (4.08).",
+            "identifier": "https://data.transportation.gov/api/views/yu7w-ucji",
             "issued": "2024-08-19",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "casualties",
                 "casualty",
@@ -108087,64 +108092,43 @@
                 "trespassers",
                 "worker on duty"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRA Safety Data Team",
-                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/yu7w-ucji",
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
-            "identifier": "https://data.transportation.gov/api/views/yu7w-ucji",
-            "description": "This is the report for Fatalities, Injuries, and Illnesses in Train Accidents, Highway-Rail Incidents, and Other Incidents (4.08).",
-            "title": "Fatalities, Injuries, and Illnesses in Train Accidents, Highway-Rail Incidents, and Other Incidents (4.08)",
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
+            "title": "Fatalities, Injuries, and Illnesses in Train Accidents, Highway-Rail Incidents, and Other Incidents (4.08)"
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
-            "landingPage": "https://data.transportation.gov/d/yu8v-sjhe",
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
-            "identifier": "1836.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
             "description": "SAS programs and auxiliary files used in report no. DOT HS 812 069, Lives Saved by Vehicle Safety Technologies & Associated FMVSS, 1960 to 2012 Passenger Cars & LTV's",
-            "title": "Lives Saved by Vehicle Safety Technologies and Associated Federal Motor Vehicle Safety Standards - SAS Programs",
-            "isPartOf": "DOT-1836",
-            "agencyProgramURL": "http://www-nrd.nhtsa.dot.gov/Pubs/812069.pdf",
-            "programCode": [
-                "021:031"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -108153,46 +108137,47 @@
                     "title": "SAS Programs"
                 }
             ],
-            "dataQuality": false,
+            "identifier": "1836.1",
+            "isPartOf": "DOT-1836",
+            "issued": "2015-01-31",
+            "keyword": [
+                "fars; statistical analysis; evaluation; benefits; effec-tiveness; fatality reduction; injury reduction; crashwor-thiness; crash avoidance"
+            ],
+            "landingPage": "https://data.transportation.gov/d/yu8v-sjhe",
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
+            "title": "Lives Saved by Vehicle Safety Technologies and Associated Federal Motor Vehicle Safety Standards - SAS Programs"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/yuaq-zdvc",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-09-05",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
-            "keyword": [
-                "directly generated",
-                "fares",
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
-            "identifier": "https://data.transportation.gov/api/views/yuaq-zdvc",
             "description": "This dataset details directly generated funding for each agency. Examples include Fares, Concessions and Advertising.\n\nNTD Data Tables organize and summarize data from the 2022 and 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. This dataset is based on the 2022 and 2023 Revenue Sources database files.\n\nIn years 2015-2021, you can find this data in the \"Funding Sources\" data table on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.\n\nIf you have any other questions about this table, please contact the NTD Help Desk at NTDHelp@dot.gov.",
-            "title": "2022 - 2023 NTD Annual Data - Funding Sources (Directly Generated)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -108200,62 +108185,59 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/yuaq-zdvc/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/yuaq-zdvc/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/yuaq-zdvc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/yuaq-zdvc/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/yuaq-zdvc/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/yuaq-zdvc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/yuaq-zdvc/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/yuaq-zdvc/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/yuaq-zdvc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/yuaq-zdvc",
+            "issued": "2024-09-05",
+            "keyword": [
+                "directly generated",
+                "fares",
+                "funding"
+            ],
+            "landingPage": "https://data.transportation.gov/d/yuaq-zdvc",
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
+            "title": "2022 - 2023 NTD Annual Data - Funding Sources (Directly Generated)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.fhwa.dot.gov/policyinformation/",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2020-10-15",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-15",
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
-            "identifier": "https://data.transportation.gov/api/views/yuth-jt4g",
+            "dataQuality": true,
             "description": "This dataset offers insight on weekly fluctuation of the gasoline product supply, which is an important part of any analysis of construction trends, materials and operating costs associated with highway repair and construction, and changes in traffic volume. These data come directly from the Energy Information Administration (EIA) website. The EIA publishes the average daily amount of gasoline supplied in barrels, which HPPI converts to an average number of gallons of gasoline per week.",
-            "title": "Weekly Gasoline Product Supplied",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -108263,45 +108245,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/yuth-jt4g/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/yuth-jt4g/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/yuth-jt4g/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/yuth-jt4g/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/yuth-jt4g/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/yuth-jt4g/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/yuth-jt4g/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/yuth-jt4g/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/yuth-jt4g/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/yuth-jt4g",
+            "issued": "2020-10-15",
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
+            "modified": "2025-01-15",
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
-            "landingPage": "https://data.transportation.gov/d/yv6b-ag3b",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "State revenue collected from motor fuel sales tax, compare same month of different years",
+            "identifier": "https://data.transportation.gov/api/views/yv6b-ag3b",
             "issued": "2022-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
             "keyword": [
                 "census",
                 "economic",
@@ -108314,63 +108318,40 @@
                 "state transportation",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/yv6b-ag3b",
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
-            "identifier": "https://data.transportation.gov/api/views/yv6b-ag3b",
-            "description": "State revenue collected from motor fuel sales tax, compare same month of different years",
-            "title": "Monthly Motor Fuel Sales Tax Revenue Collection by State",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Monthly Motor Fuel Sales Tax Revenue Collection by State"
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
-            "landingPage": "https://data.transportation.gov/d/ywku-gj4b",
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
-            "identifier": "692.14",
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
@@ -108379,19 +108360,38 @@
                     "title": "Cyclist Fatal Crashes 2009-2012"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.14",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/ywku-gj4b",
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
         }
-    ]
+    ],
+    "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json"
 }
```

