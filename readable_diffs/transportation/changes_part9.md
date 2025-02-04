# Change History for transportation.json (Part 9)

### Changes from 31606f9 to dd2190f (Part 8/9)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
                     "describedBy": "https://data.transportation.gov/api/views/ug5e-ztkm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ug5e-ztkm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ug5e-ztkm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ug5e-ztkm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ug5e-ztkm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/ug5e-ztkm",
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
+            "title": "Historic HPMS Data (Sample) - 1992"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/ugsa-uzac",
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
+                    "description": "2011 Kansas HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/kansas2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Kansas"
+                }
+            ],
+            "identifier": "678.18",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -92581,64 +92599,36 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.18",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Kansas",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/ugsa-uzac",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/kansas2011.zip",
-                    "description": "2011 Kansas HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Kansas"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Kansas"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ugux-y9xm",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/ugux-y9xm",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "The FRA Milepost is a spatial file that originates of multiple sources and contains point locations of mileposts along the FRA's rail network.  The mileposts was developed from varies sources and should only be used as a reference file.  The railroad lines and their mileposts are privately owned and are subjected of changed based on the rail owner.  If used for identifying specific locations, please contact the railroad to verify the mileposts numbers and their locations.",
-            "title": "Rail Mileposts",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -92646,40 +92636,54 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ugux-y9xm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ugux-y9xm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ugux-y9xm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/ugux-y9xm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ugux-y9xm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ugux-y9xm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/ugux-y9xm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/ugux-y9xm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/ugux-y9xm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/ugux-y9xm",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/ugux-y9xm",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Rail Mileposts"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/uh27-649n",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Ken Notis",
+                "hasEmail": "mailto:ken.notis@dot.gov"
+            },
+            "description": "Page describes the U.S. Department of Transportation, Bureau of Transportation Statistics' Transportation Services Index (TSI) which measures for-hire freight and passenger transportation volumes moved monthly",
+            "identifier": "https://data.transportation.gov/api/views/uh27-649n",
             "issued": "2020-12-15",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-09",
             "keyword": [
                 "economics",
                 "for-hire transportation",
@@ -92687,53 +92691,33 @@
                 "transportation",
                 "transportation volume"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Ken Notis",
-                "hasEmail": "mailto:ken.notis@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/uh27-649n",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-01-09",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/uh27-649n",
-            "description": "Page describes the U.S. Department of Transportation, Bureau of Transportation Statistics' Transportation Services Index (TSI) which measures for-hire freight and passenger transportation volumes moved monthly",
-            "title": "Transportation Services Index (TSI) for TRB",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Transportation Services Index (TSI) for TRB"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/uhb6-dvuq",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2024-02-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-02-15",
-            "keyword": [
-                "vius"
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
-            "identifier": "https://data.transportation.gov/api/views/uhb6-dvuq",
             "description": "This is a recoded version of the 2021 VIUS Public Use file. \n\nThe Original is found at https://www2.census.gov/programs-surveys/vius/datasets/2021/ and should be used as the most up to date version. This version will be updated as need be and was extracted 2/2/2024.\n\nThe main difference between the files is that the data dictionary has been incorporated into the database to minimize cross-checking.",
-            "title": "VIUS Public Use File Data",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -92741,69 +92725,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/uhb6-dvuq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/uhb6-dvuq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/uhb6-dvuq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/uhb6-dvuq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/uhb6-dvuq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/uhb6-dvuq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/uhb6-dvuq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/uhb6-dvuq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/uhb6-dvuq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/uhb6-dvuq",
+            "issued": "2024-02-15",
+            "keyword": [
+                "vius"
+            ],
+            "landingPage": "https://data.transportation.gov/d/uhb6-dvuq",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-02-15",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
             "theme": [
                 "Automobiles"
-            ]
+            ],
+            "title": "VIUS Public Use File Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://pvnpms.phmsa.dot.gov/PublicViewer/",
+            "agencyProgramURL": "https://www.npms.phmsa.dot.gov/PublicViewer/",
+            "analysisUnit": "Pipeline",
             "bureauCode": [
                 "021:50"
             ],
-            "landingPage": "https://data.transportation.gov/d/uhry-zmej",
-            "issued": "1999-01-01",
-            "temporal": "R/1999-01-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-29",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "https://www.npms.phmsa.dot.gov/data/PublicViewer_HelpUserGuide.pd"
-            ],
-            "keyword": [
-                "location",
-                "map",
-                "pipeline"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "PHMSA-Datahub",
                 "hasEmail": "mailto:PHMSAPHPDataandStatistics@dot.gov"
             },
-            "identifier": "228.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Pipeline and Hazardous Materials Safety Administration"
-            },
+            "dataQuality": true,
             "description": "The NPMS Public Map Viewer allows everyone, including the general public to view maps of Gas Ttransmission, Hazardous Liquid and Carbon dioxide pipelines, Liquefied Natural Gas (LNG) plants, and Hazardous Liquid breakout tanks in one selected county. Gas Distribution and Gas Gathering systems are not included in NPMS. Users are permitted to print maps of the data, but the data is not downloadable. Always call 811 before digging. Visit https://call811.com/Before-You-Dig for more information.",
-            "title": "National Pipeline Mapping System - Map Tool",
-            "isPartOf": "DOT-228",
-            "agencyProgramURL": "https://www.npms.phmsa.dot.gov/PublicViewer/",
-            "primaryITInvestmentUII": "021-500121018",
-            "programCode": [
-                "021:044"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -92812,32 +92793,69 @@
                     "title": "Map Tool"
                 }
             ],
-            "spatial": "latitude/longitude, with accuracy of +/- 500 feet",
-            "dataQuality": true,
+            "identifier": "228.2",
+            "isPartOf": "DOT-228",
+            "issued": "1999-01-01",
+            "keyword": [
+                "location",
+                "map",
+                "pipeline"
+            ],
+            "landingPage": "https://data.transportation.gov/d/uhry-zmej",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "https://pvnpms.phmsa.dot.gov/PublicViewer/",
+            "modified": "2024-07-29",
+            "phone": "202-366-1878",
+            "primaryITInvestmentUII": "021-500121018",
+            "programCode": [
+                "021:044"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Pipeline and Hazardous Materials Safety Administration"
+            },
+            "references": [
+                "https://www.npms.phmsa.dot.gov/data/PublicViewer_HelpUserGuide.pd"
+            ],
+            "spatial": "latitude/longitude, with accuracy of +/- 500 feet",
+            "temporal": "R/1999-01-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Pipeline",
-            "phone": "202-366-1878",
-            "language": [
-                "en-US"
-            ]
+            "title": "National Pipeline Mapping System - Map Tool"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/ui7z-fran",
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
+                    "description": "2011 Ohio HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/ohio2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Ohio"
+                }
+            ],
+            "identifier": "678.37",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -92851,64 +92869,36 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.37",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Ohio",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/ui7z-fran",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/ohio2011.zip",
-                    "description": "2011 Ohio HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Ohio"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Ohio"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/uic2-y76i",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/uic2-y76i",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "Class 2's & 3s",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -92916,45 +92906,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/uic2-y76i/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/uic2-y76i/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/uic2-y76i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/uic2-y76i/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/uic2-y76i/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/uic2-y76i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/uic2-y76i/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/uic2-y76i/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/uic2-y76i/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/uic2-y76i",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/uic2-y76i",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Class 2's & 3s"
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
-            "landingPage": "https://data.transportation.gov/d/ujqc-6nxi",
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
+            "identifier": "83.13",
+            "isPartOf": "DOT-83",
+            "issued": "2002-12-16",
             "keyword": [
                 "air bag",
                 "air bags",
@@ -92981,63 +92998,61 @@
                 "vin",
                 "vin search"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "83.13",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Manufacturers who determine that a product or piece of original equipment either has a safety defect or is not in compliance with Federal safety standards are required to notify the National Highway Traffic Safety Administration (NHTSA) within 5 business days. NHTSA requires that manufacturers file a Defect and Noncompliance report as well as quarterly recall status reports, in compliance with Federal Regulation 49 (the National Traffic and Motor Safety Act) Part 573, which identifies the requirements for safety recalls. This information is stored in the NHTSA database. Use this data to search for recall information related to:-\tSpecific NHTSA campaigns -\tProduct types Access to public searches of NHTSA recall databases for tires, vehicles, car seats and equipment.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - Recalls - Car Seats",
-            "isPartOf": "DOT-83",
-            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
-            "describedByType": "text/plain",
+            "landingPage": "https://data.transportation.gov/d/ujqc-6nxi",
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
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www-nrd.nhtsa.dot.gov/Pubs/809-315.pdf",
+            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
+            "analysisUnit": "Vehicle",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/ump6-5a95",
-            "issued": "2001-08-01",
-            "temporal": "2001-02-01/2001-02-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www-nrd.nhtsa.dot.gov/CMSWeb/listpublications.aspx%3FId=21&ShowBy=Category"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.nhtsa.gov/content/nhtsa-ftp/2941",
+            "description": "Tire Pressure Special Study (TPSS) was conducted in order to obtain data to draft FMVSS 138, NVS-432.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.nhtsa.gov/DOT/NHTSA/NCSA/Content/DataFile/TPS/TPSdata.ZIP",
+                    "mediaType": "text/plain",
+                    "title": "2001 TPSS Data (SAS)"
+                }
             ],
+            "identifier": "378.0",
+            "issued": "2001-08-01",
             "keyword": [
                 "dot",
                 "nhtsa",
@@ -93047,64 +93062,39 @@
                 "tpms",
                 "vehicle"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "378.0",
+            "landingPage": "https://data.transportation.gov/d/ump6-5a95",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-05-01",
+            "phone": "202-366-4696",
+            "programCode": [
+                "021:035"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Highway Traffic Safety Administration"
             },
-            "description": "Tire Pressure Special Study (TPSS) was conducted in order to obtain data to draft FMVSS 138, NVS-432.",
-            "title": "TPMS - Tire Pressure Special Study (TPSS 2001) - 2001 TPSS Data (SAS)",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:035"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.nhtsa.gov/DOT/NHTSA/NCSA/Content/DataFile/TPS/TPSdata.ZIP",
-                    "mediaType": "text/plain",
-                    "title": "2001 TPSS Data (SAS)"
-                }
+            "references": [
+                "http://www-nrd.nhtsa.dot.gov/CMSWeb/listpublications.aspx%3FId=21&ShowBy=Category"
             ],
             "spatial": "NASS CDS PSUs",
-            "describedBy": "https://www.nhtsa.gov/content/nhtsa-ftp/2941",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www-nrd.nhtsa.dot.gov/Pubs/809-315.pdf",
+            "temporal": "2001-02-01/2001-02-14",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Research",
-            "analysisUnit": "Vehicle",
-            "phone": "202-366-4696",
-            "language": [
-                "en-US"
-            ]
+            "title": "TPMS - Tire Pressure Special Study (TPSS 2001) - 2001 TPSS Data (SAS)"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/unww-uhxd",
-            "issued": "2023-04-27",
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
-            "identifier": "https://data.transportation.gov/api/views/unww-uhxd",
             "description": "This dataset is the source dataset and contains raw data values. It will replace the current data download (https://safetydata.fra.dot.gov/OfficeofSafety/publicsite/on_the_fly_download.aspx) when the safetydata.fra.dot.gov site is decommissioned in 2024. To download data that contains data is a user-friendly human-readable format, please reference https://data.transportation.gov/Railroads/Injury-Illness-Summary-Operational-Data/m8i6-zdsy.",
-            "title": "Injury/Illness Summary - Operational Source Data (Form 55)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -93112,43 +93102,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/unww-uhxd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/unww-uhxd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/unww-uhxd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/unww-uhxd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/unww-uhxd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/unww-uhxd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/unww-uhxd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/unww-uhxd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/unww-uhxd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/unww-uhxd",
+            "issued": "2023-04-27",
+            "landingPage": "https://data.transportation.gov/d/unww-uhxd",
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
+            "title": "Injury/Illness Summary - Operational Source Data (Form 55)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/up33-ud4u",
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
+                    "description": "2011 Tennessee HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/tennessee2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Tennessee"
+                }
+            ],
+            "identifier": "678.44",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -93162,58 +93180,54 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.44",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Tennessee",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/up33-ud4u",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/tennessee2011.zip",
-                    "description": "2011 Tennessee HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Tennessee"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Tennessee"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Data set contains controlled unclassified information (Draft rules and polices). Some public reports are available.",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/upa9-8sxq",
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
+            "identifier": "458.2",
+            "isPartOf": "DOT-458",
+            "issued": "2018-12-18",
             "keyword": [
                 "economically significant",
                 "effects",
@@ -93236,64 +93250,37 @@
                 "tribalism",
                 "unfunded mandate"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DOT Socrata",
-                "hasEmail": "mailto:Socrata@dot.gov"
-            },
-            "identifier": "458.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
-            "description": "RMS is a DOT-wide system developed for the Office of the General Counsel (OGC) to track the status of rulemakings, document required concurrences, serve as a repository for documents under development, and generate management and compliance reports from the data within the system.  The system allows senior leaders throughout DOT to identify not only the status of rulemakings, but areas where steps can be taken to streamline rulemaking operations at DOT.",
-            "title": "Rulemaking Management System (RMS) - Public Effects Reports",
-            "isPartOf": "DOT-458",
+            "landingPage": "https://data.transportation.gov/d/upa9-8sxq",
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
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/urir-txqm",
-            "issued": "2024-10-04",
             "@type": "dcat:Dataset",
-            "modified": "2025-01-23",
-            "keyword": [
-                "public transit"
-            ],
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NTD Program Support",
                 "hasEmail": "mailto:NTDHelp@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
-            "identifier": "https://data.transportation.gov/api/views/urir-txqm",
             "description": "Counts of Non-Major Safety and Security Events are reported to the National Transit Database on a monthly basis, by transit agency and transit mode. These include minor fires on transit property requiring suppression, transit worker assaults not involving transport for medical attention, and other safety events that are not reportable as Major Events because a Major Event reporting threshold is not met (see Safety and Security Events dataset for a list of Major Events). \n\nIn this file you will find the number of occurrences or safety incidents per month and the number of injuries in Safety Events (Safety/Security = SAF) where an individual was immediately transported away from the scene for medical attention due to those occurrences. There will be one entry for any transit mode/location with at least one occurrence for the given month. \n\nThe file also contains Transit Worker Assaults which did not immediately transport away from the scene for 2023-present, as well as other Security Events (Safety/Security = SEC) reported historically but no longer collected by FTA. Note that an assault involving transport away from the scene for medical attention meets the Injury threshold and is not counted in this dataset. \n\nAgencies are not required to provide details for these events, and any description provided is omitted. The description can be available upon request.\n\nUpdate 5/6/24: FTA has updated its validation procedure for Non-Major S&S events to allow for inclusion in the data publication sooner in certain cases. This month, users of this dataset may notice a larger increase in S&S events than normal for certain records in 2023-2024 (only years for which data collection and validation is presently ongoing) compared to prior releases. This was done to allow for a more timely release of validated data.",
-            "title": "Non-Major Safety and Security Events",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -93301,46 +93288,76 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/urir-txqm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/urir-txqm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/urir-txqm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/urir-txqm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/urir-txqm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/urir-txqm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/urir-txqm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/urir-txqm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/urir-txqm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/urir-txqm",
+            "issued": "2024-10-04",
+            "keyword": [
+                "public transit"
+            ],
+            "landingPage": "https://data.transportation.gov/d/urir-txqm",
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
+            "title": "Non-Major Safety and Security Events"
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
-            "landingPage": "https://data.transportation.gov/d/usdu-fawi",
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
+                    "downloadURL": "http://lai.locationaffordability.info/download_csv.php%3Fgeography=cbsa",
+                    "mediaType": "text/csv",
+                    "title": "All Core Based Statistical Areas (CBSAs)"
+                }
             ],
+            "identifier": "337.3",
+            "isPartOf": "DOT-337",
+            "issued": "2013-11-19",
             "keyword": [
                 "access",
                 "affordability",
@@ -93353,72 +93370,42 @@
                 "transit",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "337.3",
+            "landingPage": "https://data.transportation.gov/d/usdu-fawi",
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
-            "title": "Location Affordability Index - All Core Based Statistical Areas (CBSAs)",
-            "isPartOf": "DOT-337",
-            "agencyProgramURL": "http://www.locationaffordability.info/",
-            "describedByType": "application/pdf",
-            "programCode": [
-                "021:058"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://lai.locationaffordability.info/download_csv.php%3Fgeography=cbsa",
-                    "mediaType": "text/csv",
-                    "title": "All Core Based Statistical Areas (CBSAs)"
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
+            "title": "Location Affordability Index - All Core Based Statistical Areas (CBSAs)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/usuf-55kz",
-            "issued": "2024-09-16",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-16",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "TBD",
                 "hasEmail": "mailto:patricia.dijoseph@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/usuf-55kz",
             "description": "2022 data",
-            "title": "Top 25 Ports by Tonnage",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -93426,40 +93413,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/usuf-55kz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/usuf-55kz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/usuf-55kz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/usuf-55kz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/usuf-55kz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/usuf-55kz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/usuf-55kz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/usuf-55kz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/usuf-55kz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "https://data.transportation.gov/api/views/usuf-55kz",
+            "issued": "2024-09-16",
+            "landingPage": "https://data.transportation.gov/d/usuf-55kz",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-09-16",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Top 25 Ports by Tonnage"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/usz6-chkb",
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
+                    "description": "2011 Kentucky HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/kentucky2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Kentucky"
+                }
+            ],
+            "identifier": "678.19",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -93473,73 +93491,40 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.19",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Kentucky",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/usz6-chkb",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/kentucky2011.zip",
-                    "description": "2011 Kentucky HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Kentucky"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Kentucky"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/utf2-qtaq",
             "bureauCode": [
                 "021:15"
             ],
-            "rights": "No Restriction",
-            "issued": "2023-10-10",
-            "temporal": "Annual",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "US Department of Transportation"
-            },
-            "identifier": "https://data.transportation.gov/api/views/utf2-qtaq",
+            "dataQuality": true,
             "description": "Motor Vehicle Registration Data by Energy Source :2016 -Present\n\nVehicle types are compatible with FHWA Highway Statistics VM-1 \n\"Total\" counts of vehicles for a year are compatible with FHWA Highway Statistics  MV-1 minus \"Motorcycle.\"\nMotorcycle data are not included.",
-            "title": "Motor Vehicle Registration Data by Energy Source :2016 -Present",
-            "primaryITInvestmentUII": "021-938741189",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -93547,55 +93532,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/utf2-qtaq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/utf2-qtaq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/utf2-qtaq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/utf2-qtaq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/utf2-qtaq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/utf2-qtaq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/utf2-qtaq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/utf2-qtaq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/utf2-qtaq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/utf2-qtaq",
+            "issued": "2023-10-10",
+            "landingPage": "https://data.transportation.gov/d/utf2-qtaq",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-12-16",
+            "primaryITInvestmentUII": "021-938741189",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
+            "rights": "No Restriction",
             "spatial": "National",
             "systemOfRecords": "https://www.govinfo.gov/content/pkg/FR-2019-10-15/pdf/2019-22398.pdf",
-            "dataQuality": true,
+            "temporal": "Annual",
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Motor Vehicle Registration Data by Energy Source :2016 -Present"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/uu8q-4q2g",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/uu8q-4q2g",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "Total Reported Block Crossings",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -93603,45 +93593,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/uu8q-4q2g/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/uu8q-4q2g/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/uu8q-4q2g/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/uu8q-4q2g/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/uu8q-4q2g/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/uu8q-4q2g/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/uu8q-4q2g/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/uu8q-4q2g/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/uu8q-4q2g/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/uu8q-4q2g",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/uu8q-4q2g",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Total Reported Block Crossings"
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
-            "landingPage": "https://data.transportation.gov/d/uumg-9ig2",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/05augtvt/05augtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "August 2005"
+                }
             ],
+            "identifier": "18.109",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -93651,56 +93666,52 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.109",
+            "landingPage": "https://data.transportation.gov/d/uumg-9ig2",
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
-            "title": "Monthly Traffic Volume Trends - August 2005",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/05augtvt/05augtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "August 2005"
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
+            "title": "Monthly Traffic Volume Trends - August 2005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/uv3e-y54k",
             "bureauCode": [
                 "021:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kate Hartman",
+                "hasEmail": "mailto:kate.hartman@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "As part of the Federal Highway Administration\u2019s (FHWA) Next Generation Simulation (NGSIM) project, video data were collected on June 16th, 2005 on an arterial segment on Lankershim Boulevard located in Los Angeles, California. The data represents 30 minutes total, segmented into two periods (8:30 a.m. to 8:45 a.m. and 8:45 a.m. to 9:00 a.m.). The dataset includes files for both raw and processed video data from each of the five cameras for the two time periods available for download. Camera numbering is in order of southern-most (1) to northern-most (5). The raw videos give the original vehicle movement data and offer users a view of how the section was observed. The processed video files provide videos of the vehicles along with a superimposition of the vehicle identification numbers. These videos can be used alone or can be used for cross referencing of the textual vehicle trajectory data provided in the NGSIM trajectory data with the corresponding video.\n\nFor related datasets please see the following:\n- NGSIM Vehicle Trajectories and Supporting Data: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Vehicle-Trajector/8ect-6jqj\n- NGSIM I-80 Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-I-80-Vide/2577-gpny\n- NGSIM US-101 Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-US-101-Vi/4qzi-thur\n- NGSIM Peachtree Street Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-Peachtree/mupt-aksf",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/download/uv3e-y54k/application/pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/uv3e-y54k",
             "issued": "2016-01-01",
-            "@type": "dcat:Dataset",
-            "temporal": "2005-06-16",
-            "modified": "2016-01-01",
             "keyword": [
                 "arterial",
                 "california",
@@ -93711,74 +93722,39 @@
                 "next generation simulation (ngsim)",
                 "video"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/uv3e-y54k",
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
-            "identifier": "https://data.transportation.gov/api/views/uv3e-y54k",
-            "description": "As part of the Federal Highway Administration\u2019s (FHWA) Next Generation Simulation (NGSIM) project, video data were collected on June 16th, 2005 on an arterial segment on Lankershim Boulevard located in Los Angeles, California. The data represents 30 minutes total, segmented into two periods (8:30 a.m. to 8:45 a.m. and 8:45 a.m. to 9:00 a.m.). The dataset includes files for both raw and processed video data from each of the five cameras for the two time periods available for download. Camera numbering is in order of southern-most (1) to northern-most (5). The raw videos give the original vehicle movement data and offer users a view of how the section was observed. The processed video files provide videos of the vehicles along with a superimposition of the vehicle identification numbers. These videos can be used alone or can be used for cross referencing of the textual vehicle trajectory data provided in the NGSIM trajectory data with the corresponding video.\n\nFor related datasets please see the following:\n- NGSIM Vehicle Trajectories and Supporting Data: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Vehicle-Trajector/8ect-6jqj\n- NGSIM I-80 Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-I-80-Vide/2577-gpny\n- NGSIM US-101 Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-US-101-Vi/4qzi-thur\n- NGSIM Peachtree Street Videos: https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Program-Peachtree/mupt-aksf",
-            "title": "Next Generation Simulation (NGSIM) Program Lankershim Boulevard Videos",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/download/uv3e-y54k/application/pdf",
-                    "mediaType": "application/pdf"
-                }
-            ],
             "spatial": "Los Angeles, California",
-            "dataQuality": true,
-            "license": "http://creativecommons.org/licenses/by-sa/4.0/legalcode",
+            "temporal": "2005-06-16",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Next Generation Simulation (NGSIM) Program Lankershim Boulevard Videos"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/uvrt-varj",
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
-            "identifier": "https://data.transportation.gov/api/views/uvrt-varj",
+            "dataQuality": true,
             "description": "The data describe freeway car-following behavior (such as velocity, acceleration, and relative position) for the car-following instances observed during 59 data collection runs, performed through the Federal Highway Administration (FHWA) Turner Fairbank Highway Research Center\u2019s (TFHRC) Living Laboratory (LL). Data were collected using an Instrumented Research Vehicle (IRV) along freeways in northern Virginia to better understand work zone driver behaviors. The USDOT Volpe National Transportation Systems Center (Volpe Center) identified, isolated, and classified individual car following instances from within the raw datasets (classification parameters included roadway type, level of congestion, and speed limit), then processed, refined, and cleaned the dataset. \n\nThis table contains the instantaneous data processed from radar and GPS. See also the instances table (https://datahub.transportation.gov/Automobiles/Enhancing-Microsimulation-Models-for-Improved-Work/k74u-yqu6) and runs table (https://datahub.transportation.gov/Automobiles/Enhancing-Microsimulation-Models-for-Improved-Work/285w-yjf5).",
-            "title": "Enhancing Microsimulation Models for Improved Work Zone Planning: Car-Following Data from Northern Virginia (Radar Points)",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -93786,70 +93762,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/uvrt-varj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/uvrt-varj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/uvrt-varj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/uvrt-varj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/uvrt-varj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/uvrt-varj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/uvrt-varj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/uvrt-varj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/uvrt-varj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "-77.0573,38.7046,-77.2278,38.9563",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/uvrt-varj",
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
+            "landingPage": "https://data.transportation.gov/d/uvrt-varj",
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
+            "title": "Enhancing Microsimulation Models for Improved Work Zone Planning: Car-Following Data from Northern Virginia (Radar Points)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Access restricted under the Privacy Act of 1974; various SORNs apply \u2013 see Privacy Impact Assessment at http://www.dot.gov/individuals/privacy/pia-security-operations-systems-sos",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/ux4d-qf34",
-            "issued": "2014-09-16",
-            "temporal": "R/2014-09-16/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Law Enforcement, Courts, and Prisons",
-            "keyword": [
-                "disposition",
-                "incident",
-                "investigation",
-                "offense",
-                "personnel",
-                "security"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "430.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
             "description": "This data set contains information on security incidents at the DOT headquarters building, as collected on GSA Form 3155 (http://www.gsa.gov/portal/forms/download/114742) as well as investigation status and disposition.",
-            "title": "DOT Headquarters Security Incident Reports -",
-            "primaryITInvestmentUII": "021-686225834",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -93857,52 +93836,54 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "theme": [
-                "Law Enforcement, Courts, and Prisons"
+            "identifier": "430.0",
+            "issued": "2014-09-16",
+            "keyword": [
+                "disposition",
+                "incident",
+                "investigation",
+                "offense",
+                "personnel",
+                "security"
             ],
-            "accrualPeriodicity": "R/P1D",
-            "categoryDesignation": "Administrative",
+            "landingPage": "https://data.transportation.gov/d/ux4d-qf34",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-8020"
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
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
+            "temporal": "R/2014-09-16/P1D",
+            "theme": [
+                "Law Enforcement, Courts, and Prisons"
+            ],
+            "title": "DOT Headquarters Security Incident Reports -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Access restricted under the Privacy Act of 1974; SORN issued by OPM; see reference on DOT Privacy Act page www.dot.gov/privacy under Government-wide System of Records",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/uydw-95gk",
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
-            "identifier": "1634.2",
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
@@ -93911,29 +93892,66 @@
                     "title": "Workforce Statistics Archive"
                 }
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "theme": [
-                "Transportation"
+            "identifier": "1634.2",
+            "isPartOf": "DOT-1634",
+            "issued": "2014-11-21",
+            "keyword": [
+                "hr",
+                "payroll",
+                "personnel"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Administrative",
+            "landingPage": "https://data.transportation.gov/d/uydw-95gk",
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
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/uyja-vcxu",
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
+                    "description": "2012 North Dakota HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/northdakota2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 North Dakota"
+                }
+            ],
+            "identifier": "678.88",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -93947,64 +93965,36 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.88",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 North Dakota",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/uyja-vcxu",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/northdakota2012.zip",
-                    "description": "2012 North Dakota HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 North Dakota"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 North Dakota"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/uykm-sgqj",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/uykm-sgqj",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "Reported Blocked Crossings",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -94012,91 +94002,87 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/uykm-sgqj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/uykm-sgqj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/uykm-sgqj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/uykm-sgqj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/uykm-sgqj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/uykm-sgqj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/uykm-sgqj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/uykm-sgqj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/uykm-sgqj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/uykm-sgqj",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/uykm-sgqj",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "Reported Blocked Crossings"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/uyr2-7q4x",
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
-            "identifier": "https://data.transportation.gov/api/views/uyr2-7q4x",
             "description": "Rail carload traffic is comprised of mostly bulk commodities, such as coal and agricultural products. The Association of American Railroads releases data on carloads and intermodal units originated by U.S. railroads on a weekly and monthly basis.",
-            "title": "Freight Rail Traffic - Carloads",
+            "identifier": "https://data.transportation.gov/api/views/uyr2-7q4x",
+            "issued": "2025-01-21",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/uyr2-7q4x",
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
+            "title": "Freight Rail Traffic - Carloads"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/uyv8-9jek",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-12-16",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
-            "keyword": [
-                "employee",
-                "operator"
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
-            "identifier": "https://data.transportation.gov/api/views/uyv8-9jek",
             "description": "This dataset contains data on transit agency employees as reported to the National Transit Database in the 2022 and 2023 report years. It is organized by agency, mode, type of service, and Employee Type (Full Time or Part Time Employee). \n\nThe NTD Data Tables organize and summarize data from the 2022 and 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis\n\nThis dataset is based on the 2022 and 2023 Employees database files, which are published to the NTD at https://transit.dot.gov/ntd/ntd-data.\n\nOnly Full Reporters report data on employees, and only for Directly Operated modes. Other reporter types, and Purchased Transportation service, do not appear in this file.",
-            "title": "2022 - 2023 NTD Annual Data - Employees (by Mode and Employee Type)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -94104,62 +94090,94 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/uyv8-9jek/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/uyv8-9jek/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/uyv8-9jek/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/uyv8-9jek/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/uyv8-9jek/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/uyv8-9jek/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/uyv8-9jek/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/uyv8-9jek/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/uyv8-9jek/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/uyv8-9jek",
+            "issued": "2024-12-16",
+            "keyword": [
+                "employee",
+                "operator"
+            ],
+            "landingPage": "https://data.transportation.gov/d/uyv8-9jek",
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
+            "title": "2022 - 2023 NTD Annual Data - Employees (by Mode and Employee Type)"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/uzij-3ksd",
-            "issued": "2022-04-25",
             "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joe McGill",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "Five data sets describing ferry operators, terminals, vessels and segments.",
             "identifier": "https://data.transportation.gov/api/views/uzij-3ksd",
+            "issued": "2022-04-25",
+            "landingPage": "https://data.transportation.gov/d/uzij-3ksd",
+            "modified": "2022-04-28",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "Five data sets describing ferry operators, terminals, vessels and segments.",
             "title": "NCFO Data Files"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/v2sf-qn93",
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
+                    "description": "2013 Rhode Island HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/rhodeisland2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Rhode Island"
+                }
+            ],
+            "identifier": "678.143",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -94173,80 +94191,46 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.143",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Rhode Island",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/v2sf-qn93",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/rhodeisland2013.zip",
-                    "description": "2013 Rhode Island HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Rhode Island"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Rhode Island"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "https://www.phmsa.dot.gov/field-operations/operational-guidance-policies",
+            "agencyProgramURL": "https://www.phmsa.dot.gov/field-operations",
+            "analysisUnit": "Case",
             "bureauCode": [
                 "021:50"
             ],
-            "landingPage": "https://data.transportation.gov/d/v45s-dfsz",
-            "issued": "2011-03-31",
-            "temporal": "1998-01-01/2013-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-02",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www.phmsa.dot.gov/foia."
-            ],
-            "keyword": [
-                "civil penalty action",
-                "enforcement notice"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Adam Lucas",
                 "hasEmail": "mailto:adam.lucas@dot.gov"
             },
-            "identifier": "DOT-29",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Pipeline and Hazardous Materials Safety Administration"
-            },
+            "dataQuality": true,
             "description": "Civil Penalty Action Reports (summary tables in PDF format)",
-            "title": "Hazmat Enforcement Notices",
-            "agencyProgramURL": "https://www.phmsa.dot.gov/field-operations",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -94255,30 +94239,50 @@
                     "title": "2006"
                 }
             ],
-            "spatial": "City",
-            "dataQuality": true,
+            "identifier": "DOT-29",
+            "issued": "2011-03-31",
+            "keyword": [
+                "civil penalty action",
+                "enforcement notice"
+            ],
+            "landingPage": "https://data.transportation.gov/d/v45s-dfsz",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "https://www.phmsa.dot.gov/field-operations/operational-guidance-policies",
+            "modified": "2024-08-02",
+            "phone": "202-366-3373",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Pipeline and Hazardous Materials Safety Administration"
+            },
+            "references": [
+                "http://www.phmsa.dot.gov/foia."
+            ],
+            "spatial": "City",
+            "temporal": "1998-01-01/2013-12-31",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "analysisUnit": "Case",
-            "categoryDesignation": "Research",
-            "phone": "202-366-3373",
-            "language": [
-                "en-US"
-            ]
+            "title": "Hazmat Enforcement Notices"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/v67s-yiqd",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Transportation Spending by Income Quintile and Vehicle Ownership. Looking at number of vehicles per household by income quintile; percent of households with no vehicle by income quintile; transportation spend by households with no vehicles; and transportation spend by households with at least one vehicle.",
+            "identifier": "https://data.transportation.gov/api/views/v67s-yiqd",
             "issued": "2023-09-12",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
             "keyword": [
                 "income quintile characteristics",
                 "income quintiles",
@@ -94294,66 +94298,42 @@
                 "vehicle miles traveled",
                 "vehicle trips"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/v67s-yiqd",
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
-            "identifier": "https://data.transportation.gov/api/views/v67s-yiqd",
-            "description": "Transportation Spending by Income Quintile and Vehicle Ownership. Looking at number of vehicles per household by income quintile; percent of households with no vehicle by income quintile; transportation spend by households with no vehicles; and transportation spend by households with at least one vehicle.",
-            "title": "Transportation Cost Burden: Transportation Spending by Income Quintile and Vehicle Ownership",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Transportation Cost Burden: Transportation Spending by Income Quintile and Vehicle Ownership"
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
-            "landingPage": "https://data.transportation.gov/d/v6bx-yzki",
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
-            "identifier": "559.1",
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
@@ -94362,96 +94342,89 @@
                     "title": "Search Appeals and Decisions"
                 }
             ],
-            "spatial": "Address",
-            "describedBy": "https://www.civilrights.dot.gov/disadvantaged-business-enterprise/search-dbe-appeals-and-denials",
-            "dataQuality": true,
+            "identifier": "559.1",
+            "isPartOf": "DOT-559",
+            "issued": "2014-10-31",
+            "keyword": [
+                "appeal",
+                "certification",
+                "dbe",
+                "decertification",
+                "disadvantaged business enterprise"
+            ],
+            "landingPage": "https://data.transportation.gov/d/v6bx-yzki",
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
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/v6kf-46ur",
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
-            "identifier": "https://data.transportation.gov/api/views/v6kf-46ur",
             "description": "Labor force participation rate is the percent of persons classified as employed or unemployed as a percent of the civilian noninstitutional population. The Bureau of Labor Statistics produces industry estimates of nonfarm payroll employment as part of the Current Population Survey. Employment data are seasonally adjusted to remove the effects of normal seasonal variation.",
-            "title": "Labor Force Participation Rate - Seasonally Adjusted",
+            "identifier": "https://data.transportation.gov/api/views/v6kf-46ur",
+            "issued": "2025-01-02",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/v6kf-46ur",
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
+            "title": "Labor Force Participation Rate - Seasonally Adjusted"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/v6zb-d5rv",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2023-01-23",
-            "temporal": "R/2002-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-23",
-            "keyword": [
-                "average fares",
-                "boarding",
-                "cost per hour",
-                "cost per passenger",
-                "cost per passenger mile",
-                "farebox",
-                "fare earnings",
-                "fare per trip",
-                "fare recovery ratio",
-                "fare revenues",
-                "operating cost",
-                "operating expense",
-                "passengers per hour",
-                "ridership",
-                "unlinked passenger trip"
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
-            "identifier": "https://data.transportation.gov/api/views/v6zb-d5rv",
+            "dataQuality": true,
             "description": "Contains ratios describing service and cost for each agency, mode, and type of service.",
-            "title": "2017 Annual Metrics - National Transit Database",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -94459,74 +94432,81 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/v6zb-d5rv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/v6zb-d5rv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/v6zb-d5rv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/v6zb-d5rv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/v6zb-d5rv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/v6zb-d5rv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/v6zb-d5rv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/v6zb-d5rv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/v6zb-d5rv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/v6zb-d5rv",
+            "issued": "2023-01-23",
+            "keyword": [
+                "average fares",
+                "boarding",
+                "cost per hour",
+                "cost per passenger",
+                "cost per passenger mile",
+                "farebox",
+                "fare earnings",
+                "fare per trip",
+                "fare recovery ratio",
+                "fare revenues",
+                "operating cost",
+                "operating expense",
+                "passengers per hour",
+                "ridership",
+                "unlinked passenger trip"
+            ],
+            "landingPage": "https://data.transportation.gov/d/v6zb-d5rv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-23",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Transit Administration"
+            },
+            "spatial": "United States",
+            "temporal": "R/2002-01-01/P1M",
             "theme": [
                 "Public Transit"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2017 Annual Metrics - National Transit Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyProgramURL": "http://www.transportation.gov/digitalstrategy",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/v7ju-sfbt",
-            "issued": "2015-09-30",
-            "temporal": "R/2015-09-30/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Federal Government Finances and Employment",
-            "modified": "2024-11-14",
-            "references": [
-                "http://www.transportation.gov/digitalstrategy"
-            ],
-            "keyword": [
-                "chief information officer",
-                "fitara",
-                "governance",
-                "information technology"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "1856.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.transportation.gov/digitalstrategy",
             "description": "The DOT CIO Governance Board Membership List include all governance boards of which the CIO is a member.",
-            "title": "DOT IT Governance Boards - Download",
-            "primaryITInvestmentUII": "021-748752384",
-            "agencyProgramURL": "http://www.transportation.gov/digitalstrategy",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -94535,53 +94515,57 @@
                     "title": "Download"
                 }
             ],
-            "describedBy": "http://www.transportation.gov/digitalstrategy",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Federal Government Finances and Employment"
+            "identifier": "1856.0",
+            "issued": "2015-09-30",
+            "keyword": [
+                "chief information officer",
+                "fitara",
+                "governance",
+                "information technology"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Administrative",
+            "landingPage": "https://data.transportation.gov/d/v7ju-sfbt",
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
+            "temporal": "R/2015-09-30/P1Y",
+            "theme": [
+                "Federal Government Finances and Employment"
+            ],
+            "title": "DOT IT Governance Boards - Download"
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
-            "landingPage": "https://data.transportation.gov/d/v8dr-t6p4",
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
-                "purchased vehicles"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "13.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
+            "describedBy": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Transaction+Data+and+Reports",
             "description": "The Car Allowance Rebate System (CARS), otherwise known as Cash for Clunkers, was a program intended to provide economic incentives to United States residents to purchase a new and more fuel efficient vehicle when trading in a less full efficient vehicle. The program was promoted as providing stimulus to the economy by boosting auto sales, while putting safer, cleaner and more fuel efficient vehicles on the road.",
-            "title": "Car Allowance Rebate System (CARS) - Purchased Vehicles - Purchased Vehicles xls file",
-            "agencyProgramURL": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Officially+Ended",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -94590,70 +94574,103 @@
                     "title": "Purchased Vehicles xls file"
                 }
             ],
-            "spatial": "N/A",
-            "describedBy": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Transaction+Data+and+Reports",
-            "dataQuality": false,
+            "identifier": "13.0",
+            "issued": "2018-12-17",
+            "keyword": [
+                "cars",
+                "purchased vehicles"
+            ],
+            "landingPage": "https://data.transportation.gov/d/v8dr-t6p4",
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
+            "title": "Car Allowance Rebate System (CARS) - Purchased Vehicles - Purchased Vehicles xls file"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/v8vk-h5g4",
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
-            "identifier": "https://data.transportation.gov/api/views/v8vk-h5g4",
             "description": "Employed persons include people aged 16 years and older in the civilian noninstitutional population who did any work at all as paid employees; worked in their own business, profession, or on their own farm, or worked 15 hours or more as unpaid workers in an enterprise operated by a member of the family; and all those who were not working but who had jobs or businesses from which they were temporarily absent. The Bureau of Labor Statistics produces industry estimates of nonfarm payroll employment as part of the Current Population Survey.",
-            "title": "Transportation Employment - Transit and Ground Passenger Transportation",
+            "identifier": "https://data.transportation.gov/api/views/v8vk-h5g4",
+            "issued": "2025-01-02",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/v8vk-h5g4",
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
+            "title": "Transportation Employment - Transit and Ground Passenger Transportation"
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
-            "landingPage": "https://data.transportation.gov/d/v8yv-iqpe",
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
+                    "mediaType": "application/json",
+                    "title": "NHTSA API"
+                }
             ],
+            "identifier": "83.4",
+            "isPartOf": "DOT-83",
+            "issued": "2002-12-16",
             "keyword": [
                 "air bag",
                 "air bags",
@@ -94680,92 +94697,44 @@
                 "vin",
                 "vin search"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "83.4",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Manufacturers who determine that a product or piece of original equipment either has a safety defect or is not in compliance with Federal safety standards are required to notify the National Highway Traffic Safety Administration (NHTSA) within 5 business days. NHTSA requires that manufacturers file a Defect and Noncompliance report as well as quarterly recall status reports, in compliance with Federal Regulation 49 (the National Traffic and Motor Safety Act) Part 573, which identifies the requirements for safety recalls. This information is stored in the NHTSA database. Use this data to search for recall information related to:-\tSpecific NHTSA campaigns -\tProduct types Access to public searches of NHTSA recall databases for tires, vehicles, car seats and equipment.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - NHTSA API",
-            "isPartOf": "DOT-83",
-            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
-            "describedByType": "text/plain",
+            "landingPage": "https://data.transportation.gov/d/v8yv-iqpe",
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
-                    "mediaType": "application/json",
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
-            "landingPage": "https://data.transportation.gov/d/v9ae-hsuk",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2020-12-21",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
-            "references": [
-                "https://www.fhwa.dot.gov/policyinformation/hpms/fieldmanual/"
-            ],
-            "keyword": [
-                "alaska",
-                "arizona",
-                "california",
-                "colorado",
-                "hawaii",
-                "hpms",
-                "idaho",
-                "montana",
-                "nevada",
-                "oregon",
-                "utah",
-                "washington",
-                "west",
-                "wyoming"
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
-            "identifier": "https://data.transportation.gov/api/views/v9ae-hsuk",
+            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
             "description": "State DOT HPMS Section Attributes for Western States",
-            "title": "Roadway Sections West 2018",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -94773,75 +94742,79 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/v9ae-hsuk/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/v9ae-hsuk/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/v9ae-hsuk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/v9ae-hsuk/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/v9ae-hsuk/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/v9ae-hsuk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/v9ae-hsuk/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/v9ae-hsuk/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/v9ae-hsuk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "USA",
-            "describedBy": "https://data.transportation.gov/resource/3enx-g69f.csv?data_asset_abbreviation=HPMS",
+            "identifier": "https://data.transportation.gov/api/views/v9ae-hsuk",
+            "issued": "2020-12-21",
+            "keyword": [
+                "alaska",
+                "arizona",
+                "california",
+                "colorado",
+                "hawaii",
+                "hpms",
+                "idaho",
+                "montana",
+                "nevada",
+                "oregon",
+                "utah",
+                "washington",
+                "west",
+                "wyoming"
+            ],
+            "landingPage": "https://data.transportation.gov/d/v9ae-hsuk",
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
+            "title": "Roadway Sections West 2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/va72-z8hz",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2023-01-09",
-            "@type": "dcat:Dataset",
-            "temporal": "2016",
-            "modified": "2025-01-23",
-            "keyword": [
-                "household",
-                "local",
-                "person miles traveled",
-                "person trips",
-                "pmt",
-                "pt",
-                "tract",
-                "vehicle miles traveled",
-                "vehicle trips",
-                "vmt",
-                "vt"
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
-            "identifier": "https://data.transportation.gov/api/views/va72-z8hz",
             "description": "Estimates of average weekday household person trips, vehicle trips, person miles traveled, and vehicle miles traveled (per day), for all Census tracts in the United States for 2017.",
-            "title": "Local Area Transportation Characteristics by Household 2017",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -94849,59 +94822,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/va72-z8hz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/va72-z8hz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/va72-z8hz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/va72-z8hz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/va72-z8hz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/va72-z8hz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/va72-z8hz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/va72-z8hz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/va72-z8hz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S. Census tract",
+            "identifier": "https://data.transportation.gov/api/views/va72-z8hz",
+            "issued": "2023-01-09",
+            "keyword": [
+                "household",
+                "local",
+                "person miles traveled",
+                "person trips",
+                "pmt",
+                "pt",
+                "tract",
+                "vehicle miles traveled",
+                "vehicle trips",
+                "vmt",
+                "vt"
+            ],
+            "landingPage": "https://data.transportation.gov/d/va72-z8hz",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2025-01-23",
+            "phone": "202-366-DATA(3282) ",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "spatial": "U.S. Census tract",
+            "temporal": "2016",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282) "
+            "title": "Local Area Transportation Characteristics by Household 2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/vaik-frhy",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2023-01-23",
-            "temporal": "R/2002-01-01/P1M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-31",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NTD Program Support",
                 "hasEmail": "mailto:NTDHelp@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Transit Administration"
-            },
-            "identifier": "https://data.transportation.gov/api/views/vaik-frhy",
+            "dataQuality": true,
             "description": "Contains metrics describing service consumption and service cost for each public transportation agency, by mode and type of service.",
-            "title": "2021 Annual Metrics - National Transit Database",
-            "programCode": [
-                "021:017"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -94909,51 +94896,79 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/vaik-frhy/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vaik-frhy/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vaik-frhy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/vaik-frhy/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vaik-frhy/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vaik-frhy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/vaik-frhy/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vaik-frhy/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vaik-frhy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/vaik-frhy",
+            "issued": "2023-01-23",
+            "landingPage": "https://data.transportation.gov/d/vaik-frhy",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-05-31",
+            "programCode": [
+                "021:017"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Transit Administration"
+            },
+            "spatial": "United States",
+            "temporal": "R/2002-01-01/P1M",
             "theme": [
                 "Public Transit"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2021 Annual Metrics - National Transit Database"
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
-            "landingPage": "https://data.transportation.gov/d/vc48-t9f5",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12febtvt/12febtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "February 2012"
+                }
             ],
+            "identifier": "18.1",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -94963,75 +94978,43 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.1",
+            "landingPage": "https://data.transportation.gov/d/vc48-t9f5",
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
-            "title": "Monthly Traffic Volume Trends - February 2012",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12febtvt/12febtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "February 2012"
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
+            "title": "Monthly Traffic Volume Trends - February 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/vc8a-zq94",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-10-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-01",
-            "keyword": [
-                "containers",
-                "international trade",
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
-            "identifier": "https://data.transportation.gov/api/views/vc8a-zq94",
             "description": "Source: U.S. Department of Transportation, Bureau of Transportation Statistics, based upon U.S. Department of Commerce, U.S. Census Bureau, Foreign Trade Division, USA Trade Online, \"HS Port-level Data\", available at https://usatrade.census.gov/ as of Sept 2024.",
-            "title": "Containerized Exports' Value and Weight by Port in 2023",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -95039,72 +95022,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/vc8a-zq94/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vc8a-zq94/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vc8a-zq94/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/vc8a-zq94/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vc8a-zq94/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vc8a-zq94/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/vc8a-zq94/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vc8a-zq94/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vc8a-zq94/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/vc8a-zq94",
+            "issued": "2024-10-01",
+            "keyword": [
+                "containers",
+                "international trade",
+                "ports"
+            ],
+            "landingPage": "https://data.transportation.gov/d/vc8a-zq94",
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
+            "title": "Containerized Exports' Value and Weight by Port in 2023"
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
-            "landingPage": "https://data.transportation.gov/d/vdzw-isyi",
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
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "484.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
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
@@ -95113,32 +95093,68 @@
                     "title": "Comprehensive Record Schedule"
                 }
             ],
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "484.1",
+            "isPartOf": "DOT-484",
+            "issued": "2018-12-18",
+            "keyword": [
+                "archives",
+                "disposition",
+                "nara",
+                "record schedules"
             ],
-            "accrualPeriodicity": "R/PT1S",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/vdzw-isyi",
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
+            "title": "Comprehensive Records Schedule - Comprehensive Record Schedule"
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
-            "landingPage": "https://data.transportation.gov/d/ve39-aq2j",
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
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2014_database/NTDdatabase.htm",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2014 Database"
+                }
             ],
+            "identifier": "21.18",
+            "isPartOf": "DOT-21",
+            "issued": "2010-10-01",
             "keyword": [
                 "agency",
                 "allocation",
@@ -95157,95 +95173,61 @@
                 "urbanized",
                 "vehicles"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NTD Program Support",
-                "hasEmail": "mailto:NTDHelp@dot.gov"
-            },
-            "identifier": "21.18",
+            "landingPage": "https://data.transportation.gov/d/ve39-aq2j",
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
-            "title": "NTD Annual Module Data Set - 2014 Database",
-            "isPartOf": "DOT-21",
-            "agencyProgramURL": "http://www.ntdprogram.gov",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2014_database/NTDdatabase.htm",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "2014 Database"
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
+            "title": "NTD Annual Module Data Set - 2014 Database"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/ve3u-fuxw",
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
             "identifier": "https://data.transportation.gov/api/views/ve3u-fuxw",
+            "issued": "2020-12-10",
+            "landingPage": "https://data.transportation.gov/d/ve3u-fuxw",
+            "modified": "2022-01-10",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "NCFO for TRB"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/venb-5asu",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-12-16",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
-            "keyword": [
-                "geographic",
-                "public transit",
-                "weblinks"
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
-            "identifier": "https://data.transportation.gov/api/views/venb-5asu",
             "description": "As of Report Year (RY) 2023, FTA requires that reporters with fixed route modes create and maintain a public domain general transit feed specification (GTFS) dataset that reflects their fixed route service. This specification allows for the mapping and other geospatial data visualization and analyses of key transit elements such as stops, routes, and trips. At least one GTFS weblink is provided by the transit agency for each fixed route bus mode and type of service. These include all Rail modes as well as Bus, Bus Rapid Transit, Commuter Bus, Ferryboat and Trolleybus.\n\nGTFS requires that an overarching compressed file contain, at a minimum, seven underlying text files: (a) Agency; (b) Stops; (c) Routes; (d) Trips; (e) Stop Times; (f) Calendar or Calendar Dates.txt; and (g) Feed Info.txt. An eighth file, Shapes.txt, is an optional file. FTA collects and publishes these links for further analysis using related GTFS files. FTA is not responsible for managing the websites that host these files, and users with questions regarding the GTFS data are encouraged to contact the transit agency.\n\nIn many cases, publicly hosted weblinks could not be provided (i.e., due to constraints within the transit agency), but the agency was able to produce a zip file of the required GTFS data. Demand Response, Vanpool, and other non-fixed route modes are excluded. The column \"Alternate Format\" indicates that the agency provided FTA a weblink in an alternate format with some justification for doing so. The file \"Waived\" indicates that no GTFS files were produced and FTA granted the agency a waiver from the requirement in Report Year 2023.\n\nNTD Data Tables organize and summarize data from the  2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. This dataset is based on the 2023 General Transit Feed Specification database file.\n\nIf you have any other questions about this table, please contact the NTD Help Desk at NTDHelp@dot.gov.",
-            "title": "2023 NTD Annual Data - General Transit Feed Specification (GTFS) Weblinks",
-            "programCode": [
-                "021:061"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -95253,132 +95235,130 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/venb-5asu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/venb-5asu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/venb-5asu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/venb-5asu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/venb-5asu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/venb-5asu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/venb-5asu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/venb-5asu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/venb-5asu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/venb-5asu",
+            "issued": "2024-12-16",
+            "keyword": [
+                "geographic",
+                "public transit",
+                "weblinks"
+            ],
+            "landingPage": "https://data.transportation.gov/d/venb-5asu",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-12-16",
+            "programCode": [
+                "021:061"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Transit Administration"
+            },
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "2023 NTD Annual Data - General Transit Feed Specification (GTFS) Weblinks"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/vf2d-wcyz",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2023-01-20",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-20",
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
-            "identifier": "https://data.transportation.gov/api/views/vf2d-wcyz",
             "description": "National Highway Traffic Safety Administration releases data on highway fatalities in the Fatality Analysis Reporting System (FARS). Data for the most recent year are preliminary estimates.",
-            "title": "Highway Fatalities Per 100 Million Vehicle Miles Traveled",
+            "identifier": "https://data.transportation.gov/api/views/vf2d-wcyz",
+            "issued": "2023-01-20",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/vf2d-wcyz",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-20",
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
+            "title": "Highway Fatalities Per 100 Million Vehicle Miles Traveled"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/vfi4-ceay",
             "bureauCode": [
                 "021:27"
             ],
-            "issued": "2024-11-20",
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
-            "identifier": "https://data.transportation.gov/api/views/vfi4-ceay",
+            "dataQuality": true,
             "description": "This is the landing page to download Form 55 Injury/Illness Summary [Operational Data].",
-            "title": "Form 55 Data Downloads",
+            "identifier": "https://data.transportation.gov/api/views/vfi4-ceay",
+            "issued": "2024-11-20",
+            "landingPage": "https://data.transportation.gov/d/vfi4-ceay",
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
+            "title": "Form 55 Data Downloads"
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
-            "identifier": "https://data.transportation.gov/api/views/vg2j-m9mb",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 2006",
-            "title": "Historic HPMS Data (Sample) - 2006",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -95386,50 +95366,85 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/vg2j-m9mb/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vg2j-m9mb/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vg2j-m9mb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/vg2j-m9mb/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vg2j-m9mb/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vg2j-m9mb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/vg2j-m9mb/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vg2j-m9mb/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vg2j-m9mb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/vg2j-m9mb",
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
+            "title": "Historic HPMS Data (Sample) - 2006"
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
-            "landingPage": "https://data.transportation.gov/d/vg6g-2nty",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/03jultvt/03jultvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "July 2003"
+                }
             ],
+            "identifier": "18.134",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -95439,96 +95454,92 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.134",
+            "landingPage": "https://data.transportation.gov/d/vg6g-2nty",
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
-            "title": "Monthly Traffic Volume Trends - July 2003",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/03jultvt/03jultvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "July 2003"
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
+            "title": "Monthly Traffic Volume Trends - July 2003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/vgvy-yf2j",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This report summarizes highway-rail grade crossing incidents, with the ability to display data by state, county, city, railroad, warning device, and highway user.",
+            "identifier": "https://data.transportation.gov/api/views/vgvy-yf2j",
             "issued": "2023-08-04",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "grade crossing incident",
                 "highway-rail",
                 "hrgc",
                 "summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/vgvy-yf2j",
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
-            "identifier": "https://data.transportation.gov/api/views/vgvy-yf2j",
-            "description": "This report summarizes highway-rail grade crossing incidents, with the ability to display data by state, county, city, railroad, warning device, and highway user.",
-            "title": "Highway-Rail Grade Crossing Incident Summary",
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
+            "title": "Highway-Rail Grade Crossing Incident Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.21949/1503764",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2013-11-30",
-            "@type": "dcat:Dataset",
-            "modified": "2016-12-20",
-            "references": [
-                "https://rosap.ntl.bts.gov/view/dot/3606"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Transportation Library Data Curator",
+                "hasEmail": "mailto:ntldatacurator@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The Highway Capacity Manual (HCM) historically has been among the most important reference guides used by transportation professionals seeking a systematic basis for evaluating the capacity, level of service, and performance measures for elements of the surface transportation system, particularly highways but also other modes. The objective of this project was to determine how data and information on the impacts of differing causes of nonrecurrent congestion (incidents, weather, work zones, special events, etc.) in the context of highway capacity can be incorporated into the performance measure estimation procedures contained in the HCM. The methodologies contained in the HCM for predicting delay, speed, queuing, and other performance measures for alternative highway designs are not currently sensitive to traffic management techniques and other operation/design measures for reducing nonrecurrent congestion. A further objective was to develop methodologies to predict travel time reliability on selected types of facilities and within corridors. This project developed new analytical procedures and prepared chapters about freeway facilities and urban streets for potential incorporation of travel-time reliability into the HCM. The methods are embodied in two computational engines, and a final report documents the research.  This zip file contains comma separated value (.csv) files of data to support SHRP 2 report S2-L08-RW-1, Incorporating travel time reliability into the Highway Capacity Manual. Zip size is 1.83 MB. Files were accessed in Microsoft Excel 2016. Data will be preserved as is. To view publication see: https://rosap.ntl.bts.gov/view/dot/3606",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The Highway Capacity Manual (HCM) historically has been among the most important reference guides used by transportation professionals seeking a systematic basis for evaluating the capacity, level of service, and performance measures for elements of the surface transportation system, particularly highways but also other modes. The objective of this project was to determine how data and information on the impacts of differing causes of nonrecurrent congestion (incidents, weather, work zones, special events, etc.) in the context of highway capacity can be incorporated into the performance measure estimation procedures contained in the HCM. The methodologies contained in the HCM for predicting delay, speed, queuing, and other performance measures for alternative highway designs are not currently sensitive to traffic management techniques and other operation/design measures for reducing nonrecurrent congestion. A further objective was to develop methodologies to predict travel time reliability on selected types of facilities and within corridors. This project developed new analytical procedures and prepared chapters about freeway facilities and urban streets for potential incorporation of travel-time reliability into the HCM. The methods are embodied in two computational engines, and a final report documents the research.  This zip file contains comma separated value (.csv) files of data to support SHRP 2 report S2-L08-RW-1, Incorporating travel time reliability into the Highway Capacity Manual. Zip size is 1.83 MB. Files were accessed in Microsoft Excel 2016. Data will be preserved as is. To view publication see: https://rosap.ntl.bts.gov/view/dot/3606",
+                    "downloadURL": "https://doi.org/10.21949/1503764",
+                    "mediaType": "application/zip",
+                    "title": "Incorporating travel time reliability into the Highway Capacity Manual [supporting datasets]"
+                }
             ],
+            "identifier": "https://data.transportation.gov/api/views/vgwp-6ysf",
+            "issued": "2013-11-30",
             "keyword": [
                 "forecasting",
                 "freeways",
@@ -95543,70 +95554,41 @@
                 "travel time",
                 "travel time reliability"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Transportation Library Data Curator",
-                "hasEmail": "mailto:ntldatacurator@dot.gov"
-            },
+            "landingPage": "https://doi.org/10.21949/1503764",
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
-            "identifier": "https://data.transportation.gov/api/views/vgwp-6ysf",
-            "description": "The Highway Capacity Manual (HCM) historically has been among the most important reference guides used by transportation professionals seeking a systematic basis for evaluating the capacity, level of service, and performance measures for elements of the surface transportation system, particularly highways but also other modes. The objective of this project was to determine how data and information on the impacts of differing causes of nonrecurrent congestion (incidents, weather, work zones, special events, etc.) in the context of highway capacity can be incorporated into the performance measure estimation procedures contained in the HCM. The methodologies contained in the HCM for predicting delay, speed, queuing, and other performance measures for alternative highway designs are not currently sensitive to traffic management techniques and other operation/design measures for reducing nonrecurrent congestion. A further objective was to develop methodologies to predict travel time reliability on selected types of facilities and within corridors. This project developed new analytical procedures and prepared chapters about freeway facilities and urban streets for potential incorporation of travel-time reliability into the HCM. The methods are embodied in two computational engines, and a final report documents the research.  This zip file contains comma separated value (.csv) files of data to support SHRP 2 report S2-L08-RW-1, Incorporating travel time reliability into the Highway Capacity Manual. Zip size is 1.83 MB. Files were accessed in Microsoft Excel 2016. Data will be preserved as is. To view publication see: https://rosap.ntl.bts.gov/view/dot/3606",
-            "title": "Incorporating travel time reliability into the Highway Capacity Manual [supporting datasets]",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://doi.org/10.21949/1503764",
-                    "description": "The Highway Capacity Manual (HCM) historically has been among the most important reference guides used by transportation professionals seeking a systematic basis for evaluating the capacity, level of service, and performance measures for elements of the surface transportation system, particularly highways but also other modes. The objective of this project was to determine how data and information on the impacts of differing causes of nonrecurrent congestion (incidents, weather, work zones, special events, etc.) in the context of highway capacity can be incorporated into the performance measure estimation procedures contained in the HCM. The methodologies contained in the HCM for predicting delay, speed, queuing, and other performance measures for alternative highway designs are not currently sensitive to traffic management techniques and other operation/design measures for reducing nonrecurrent congestion. A further objective was to develop methodologies to predict travel time reliability on selected types of facilities and within corridors. This project developed new analytical procedures and prepared chapters about freeway facilities and urban streets for potential incorporation of travel-time reliability into the HCM. The methods are embodied in two computational engines, and a final report documents the research.  This zip file contains comma separated value (.csv) files of data to support SHRP 2 report S2-L08-RW-1, Incorporating travel time reliability into the Highway Capacity Manual. Zip size is 1.83 MB. Files were accessed in Microsoft Excel 2016. Data will be preserved as is. To view publication see: https://rosap.ntl.bts.gov/view/dot/3606",
-                    "@type": "dcat:Distribution",
-                    "title": "Incorporating travel time reliability into the Highway Capacity Manual [supporting datasets]"
-                }
+            "references": [
+                "https://rosap.ntl.bts.gov/view/dot/3606"
             ],
             "spatial": "United States",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "language": [
-                "en-US"
-            ]
+            "title": "Incorporating travel time reliability into the Highway Capacity Manual [supporting datasets]"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "The data set contains controlled unclassified procurement information, confidential business information, and information protected by statute or regulation.",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/vh6y-y2ts",
-            "issued": "2014-12-29",
-            "temporal": "R/2014-12-29/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "asset details",
-                "depreciation calculation",
-                "distribution details"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "737.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
             "description": "Delphi assets module contains the following data elements, but is not limited to header ID, asset and distribution details, and depreciation calculation.",
-            "title": "Delphi Asset Module -",
-            "primaryITInvestmentUII": "021-105731835",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -95614,32 +95596,66 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
+            "identifier": "737.0",
+            "issued": "2014-12-29",
+            "keyword": [
+                "asset details",
+                "depreciation calculation",
+                "distribution details"
+            ],
+            "landingPage": "https://data.transportation.gov/d/vh6y-y2ts",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
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
             "theme": [
                 "Transportation"
             ],
+            "title": "Delphi Asset Module -"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "language": [
-                "en-US"
+            "agencyDataSeriesURL": "http://www.ntdprogram.gov/ntdprogram/data.htm",
+            "agencyProgramURL": "http://www.ntdprogram.gov",
+            "analysisUnit": "Transit Agency, some data by Mode and Type of Service",
+            "bureauCode": [
+                "021:36"
             ],
-            "phone": "202-366-9646"
+            "categoryDesignation": "Research",
+            "collectionInstrument": "Transportation",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John D. Giorgis",
+                "hasEmail": "mailto:john.giorgis@dot.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.ntdprogram.gov/ntdprogram/data.htm",
+            "description": "Data reported to the NTD by urbanized area transit systems in their annual reports.   Includes contact information, contractural relationshps, subrecipient informatino, service area, sources of funds, operating expenditures by object class and function, capital expenditures by object class and function, fixed guideway information, revenue vehicle inventory, fuel consumption, employees, and labor hours, and urbanized area allocation information.   Also includes service supplied and consumed by annual total, average weekday, average saturday, and average sunday.",
+            "distribution": [
                 {
-            "accessLevel": "public",
-            "bureauCode": [
-                "021:36"
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2007_database/2007NTDxls.exe",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2007 Database"
+                }
             ],
-            "landingPage": "https://data.transportation.gov/d/vhcq-jesf",
+            "identifier": "21.11",
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
@@ -95658,79 +95674,42 @@
                 "urbanized",
                 "vehicles"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John D. Giorgis",
-                "hasEmail": "mailto:john.giorgis@dot.gov"
-            },
-            "identifier": "21.11",
+            "landingPage": "https://data.transportation.gov/d/vhcq-jesf",
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
-            "title": "NTD Annual Module Data Set - 2007 Database",
-            "isPartOf": "DOT-21",
-            "agencyProgramURL": "http://www.ntdprogram.gov",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2007_database/2007NTDxls.exe",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "2007 Database"
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
+            "title": "NTD Annual Module Data Set - 2007 Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/vhwz-raag",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2023-12-12",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
-            "keyword": [
-                "crossing",
-                "crossing inventory",
-                "form 71",
-                "highway-rail",
-                "highway-rail grade crossing",
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
-            "identifier": "https://data.transportation.gov/api/views/vhwz-raag",
             "description": "This dataset is in a user-friendly human-readable format. It contains the historical crossing inventory. To download the current inventory data, go here: https://data.transportation.gov/Railroads/Crossing-Inventory-Data-Form-71-Current/m2f8-22s6.",
-            "title": "Crossing Inventory Data (Form 71) - Historical",
-            "programCode": [
-                "021:036"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -95738,70 +95717,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/vhwz-raag/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vhwz-raag/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vhwz-raag/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/vhwz-raag/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vhwz-raag/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vhwz-raag/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/vhwz-raag/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vhwz-raag/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vhwz-raag/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/vhwz-raag",
+            "issued": "2023-12-12",
+            "keyword": [
+                "crossing",
+                "crossing inventory",
+                "form 71",
+                "highway-rail",
+                "highway-rail grade crossing",
+                "inventory"
+            ],
+            "landingPage": "https://data.transportation.gov/d/vhwz-raag",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-31",
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
+            "title": "Crossing Inventory Data (Form 71) - Historical"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/vhz2-exyi",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2023-08-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
-            "keyword": [
-                "advanced driver assistance system (adas)",
-                "automated vehicles",
-                "central ohio",
-                "connected vehicles",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "naturalistic driving study",
-                "sae level 2",
-                "trajectories"
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
-            "identifier": "https://data.transportation.gov/api/views/vhz2-exyi",
+            "dataQuality": true,
             "description": "Dataset contains two subject vehicles\u2019 trajectory data connected in naturalistic traffic conditions in central Ohio. Instrumented subject vehicles were either a discreet or readily-identifiable ADAS-equipped vehicle with SAE L2 capabilities. Dataset also contains trajectories for adjacent vehicles in traffic (observed by the subject vehicles\u2019 onboard sensors).",
-            "title": "Advanced Driver Assistance System (ADAS)-Equipped Two-Vehicle Data for Central Ohio",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -95809,47 +95786,84 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/vhz2-exyi/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vhz2-exyi/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vhz2-exyi/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/vhz2-exyi/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vhz2-exyi/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vhz2-exyi/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/vhz2-exyi/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vhz2-exyi/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vhz2-exyi/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/vhz2-exyi",
+            "issued": "2023-08-23",
+            "keyword": [
+                "advanced driver assistance system (adas)",
+                "automated vehicles",
+                "central ohio",
+                "connected vehicles",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "naturalistic driving study",
+                "sae level 2",
+                "trajectories"
+            ],
+            "landingPage": "https://data.transportation.gov/d/vhz2-exyi",
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
-            ]
+            ],
+            "title": "Advanced Driver Assistance System (ADAS)-Equipped Two-Vehicle Data for Central Ohio"
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
-            "landingPage": "https://data.transportation.gov/d/vi6n-gn6r",
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
+            "identifier": "304.1",
+            "isPartOf": "DOT-304",
+            "issued": "2011-01-18",
             "keyword": [
                 "data.gov",
                 "highway",
@@ -95860,56 +95874,60 @@
                 "stimulus",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "304.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "Specific Federal Highway Administration Policy and Guidance Statements relating to the American Recovery and Reinvestment Act of 2009",
-            "title": "Federal Highway Administration American Recovery and Reinvestment Act of 2009 Policy and Guidance -",
-            "isPartOf": "DOT-304",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/economicrecovery/",
+            "landingPage": "https://data.transportation.gov/d/vi6n-gn6r",
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
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/vi9f-tk72",
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
+                    "description": "2013 Missouri HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/missouri2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Missouri"
+                }
+            ],
+            "identifier": "678.129",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -95923,85 +95941,46 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.129",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Missouri",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/vi9f-tk72",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/missouri2013.zip",
-                    "description": "2013 Missouri HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Missouri"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Missouri"
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
-            "landingPage": "https://data.transportation.gov/d/vjqs-xi3h",
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
-            "identifier": "524.11",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
             "description": "STATE DATA REPORTING SYSTEMS. Annual reports on the Fatality Analysis Reporting System (FARS) which is data regarding fatalities that is collected by a FARS analyst from each State and provided to NHTSA.",
-            "title": "GES Reports - 2009",
-            "isPartOf": "DOT-524",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -96010,54 +95989,90 @@
                     "title": "2009"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
-            "dataQuality": true,
+            "identifier": "524.11",
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
+            "landingPage": "https://data.transportation.gov/d/vjqs-xi3h",
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
+            "title": "GES Reports - 2009"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/vk5b-b8sa",
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
             "identifier": "https://data.transportation.gov/api/views/vk5b-b8sa",
+            "issued": "2020-12-10",
+            "landingPage": "https://data.transportation.gov/d/vk5b-b8sa",
+            "modified": "2022-01-10",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "VIUS for TRB"
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
-            "landingPage": "https://data.transportation.gov/d/vkpd-ueqy",
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
+                    "downloadURL": "http://www.nhtsa.gov/staticfiles/nti/MVOSS/MVOSS2007_SAS_VersionA_Data.sas7bdat",
+                    "mediaType": "text/plain",
+                    "title": "Seat Belt Issues (v1) (SAS)"
+                }
             ],
+            "identifier": "408.2",
+            "isPartOf": "DOT-408",
+            "issued": "2008-08-31",
             "keyword": [
                 "air bag",
                 "child safety",
@@ -96068,88 +96083,91 @@
                 "protection",
                 "seat belt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "408.2",
+            "landingPage": "https://data.transportation.gov/d/vkpd-ueqy",
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
-            "title": "Motor Vehicle Occupant Safety Survey 2007 (MVOSS) - Seat Belt Issues (v1) (SAS)",
-            "isPartOf": "DOT-408",
-            "agencyProgramURL": "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/National+Telephone+Surveys",
-            "programCode": [
-                "021:032"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.nhtsa.gov/staticfiles/nti/MVOSS/MVOSS2007_SAS_VersionA_Data.sas7bdat",
-                    "mediaType": "text/plain",
-                    "title": "Seat Belt Issues (v1) (SAS)"
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
+            "title": "Motor Vehicle Occupant Safety Survey 2007 (MVOSS) - Seat Belt Issues (v1) (SAS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/vktv-jrbs",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2020-03-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
-            "keyword": [
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
-            "identifier": "https://data.transportation.gov/api/views/vktv-jrbs",
             "description": "Transportation costs faced by producers",
-            "title": "Transportation Economic Trends: Transportation Costs - Producers",
+            "identifier": "https://data.transportation.gov/api/views/vktv-jrbs",
+            "issued": "2020-03-01",
+            "keyword": [
+                "transportation cost"
+            ],
+            "landingPage": "https://data.transportation.gov/d/vktv-jrbs",
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
+            "title": "Transportation Economic Trends: Transportation Costs - Producers"
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
+                    "description": "2011 National Highway System Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/pa_nhs_2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 National Highway System"
+                }
             ],
-            "landingPage": "https://data.transportation.gov/d/vku2-9dum",
+            "identifier": "678.157",
+            "isPartOf": "DOT-678",
             "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
-            "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
             "keyword": [
                 "aadt",
                 "condition",
@@ -96163,85 +96181,47 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.157",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 National Highway System",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/vku2-9dum",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/pa_nhs_2011.zip",
-                    "description": "2011 National Highway System Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 National Highway System"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 National Highway System"
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
-            "landingPage": "https://data.transportation.gov/d/vmjs-fjrt",
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
-            "identifier": "693.5",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
             "description": "The NBI System is the collection of bridge inspection information and costs associated with bridge replacements of structurally deficient bridges on and off the NHS. This data is collected under the auspices of the National Bridge Inspection Standards (NBIS) as prescribed by law. The NBI System collects the information that is used to determine eligibility for NHS projects, performance measure reporting, NHS penalty determination, and reporting to Congress.  It supports oversight of the NBIS through various report tools, and provides data reporting that supports agency strategic goals.",
-            "title": "National Bridge Inventory System (NBI) - 1996",
-            "isPartOf": "DOT-693",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
-            "primaryITInvestmentUII": "021-012940226",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -96250,63 +96230,60 @@
                     "title": "1996"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
-            "dataQuality": true,
+            "identifier": "693.5",
+            "isPartOf": "DOT-693",
+            "issued": "1992-12-31",
+            "keyword": [
+                "bridge",
+                "condition",
+                "deck",
+                "inspection",
+                "structure"
+            ],
+            "landingPage": "https://data.transportation.gov/d/vmjs-fjrt",
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
+            "title": "National Bridge Inventory System (NBI) - 1996"
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
-            "landingPage": "https://data.transportation.gov/d/vmnb-zxn4",
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
-            "identifier": "1841.3",
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
@@ -96315,44 +96292,55 @@
                     "title": "Latest Tests"
                 }
             ],
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/bio/schema.htm",
-            "dataQuality": false,
+            "identifier": "1841.3",
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
+            "landingPage": "https://data.transportation.gov/d/vmnb-zxn4",
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
-            "landingPage": "https://data.transportation.gov/d/vpgu-kvxj",
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
-            "identifier": "https://data.transportation.gov/api/views/vpgu-kvxj",
             "description": "Source: U.S. Department of Transportation, Bureau of Transportation Statistics, based upon U.S. Department of Commerce, U.S. Census Bureau, Foreign Trade Division, USA Trade Online, \"HS Port-level Data\", available at https://usatrade.census.gov/ as of Sept 2024.",
-            "title": "Top 10 Containerized Import Commodities by Shipping Weight (short tons) and Coast 2023",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -96360,45 +96348,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/vpgu-kvxj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vpgu-kvxj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vpgu-kvxj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/vpgu-kvxj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vpgu-kvxj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vpgu-kvxj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/vpgu-kvxj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vpgu-kvxj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vpgu-kvxj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/vpgu-kvxj",
+            "issued": "2024-10-03",
+            "landingPage": "https://data.transportation.gov/d/vpgu-kvxj",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-10-03",
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
+            "title": "Top 10 Containerized Import Commodities by Shipping Weight (short tons) and Coast 2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/vq2r-5pm7",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRA Safety Data Team",
+                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This is the page for Accident Detail Listing (3.18).",
+            "identifier": "https://data.transportation.gov/api/views/vq2r-5pm7",
             "issued": "2024-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "collision",
                 "derailment",
@@ -96406,39 +96411,46 @@
                 "train",
                 "train accident"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRA Safety Data Team",
-                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/vq2r-5pm7",
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
-            "identifier": "https://data.transportation.gov/api/views/vq2r-5pm7",
-            "description": "This is the page for Accident Detail Listing (3.18).",
-            "title": "Accident Detail Listing (3.18)",
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
+            "title": "Accident Detail Listing (3.18)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://its.dot.gov/isc/",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ITS JPO Data Support",
+                "hasEmail": "mailto:data.itsjpo@dot.gov"
+            },
+            "description": "This dataset was collected as part of the U.S. Department of Transportation (U.S. DOT) Intersection Safety Challenge (hereafter, \u201cthe Challenge\u201d) for Stage 1B: System Assessment and Virtual Testing. Multi-sensor data were collected at a controlled test roadway intersection the Federal Highway Administration (FHWA) Turner-Fairbank Highway Research Center (TFHRC) Smart Intersection facility in McLean, VA from October 2023 through March 2024. The data include potential conflict-based and non-conflict-based experimental scenarios between vulnerable road users (e.g., pedestrians, bicyclists) and vehicles during both daytime and nighttime conditions. Note that no actual human vulnerable road users were put at risk of being involved in a collision during the data collection efforts. The provided data (hereafter, \u201cthe Challenge Dataset\u201d) are unlabeled training data (without ground truth) that were collected to be used for intersection safety system algorithm training, refinement, tuning, and/or validation, but may have additional uses. For a summary of the Stage 1B data collection effort, please see this video: https://youtu.be/csirVHFa2Cc.\n\nThe Challenge Dataset includes data at a single, signalized four-way intersection from 20 roadside sensors and traffic control devices, including eight closed-circuit television (CCTV) visual cameras, five thermal cameras, two light detection and ranging (LiDAR) sensors, and four radar sensors. Intrinsic calibration was performed for all visual and thermal cameras. Extrinsic calibration was performed for specific pairs of roadside sensors. Additionally, the traffic signal phase and timing data and vehicle and/or pedestrian calls to the traffic signal controller (if any) are also provided.\n\nThe total number of unique runs in the Challenge Dataset is 1,104, bringing the total size of the dataset to approximately 1 TB. A sample of 20 unique runs from the Challenge Dataset is provided here for download, inspection, and use. If, after inspecting this sample, a potential data user would like access to download the full Challenge Dataset, a request can be made via the form here: https://its.dot.gov/data/data-request\n\nFor more details about the data collection, supplemental files, organization and dictionary, and sensor calibration, see the attached \u201cU.S. DOT ISC Stage 1B ITS DataHub Metadata_v1.0.pdf\u201d document. For more information on the background of the Intersection Safety Challenge Stage 1B, please visit: its.dot.gov/isc.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The link below goes to the form to request the full dataset and is NOT the sample data. The sample dataset can be found below in the ATTACHMENTS section of the metadata. If you are ready to request the full dataset, you can use the link below to submit a request. ",
+                    "downloadURL": "https://its.dot.gov/data/data-request",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/vq7s-mv3v",
             "issued": "2025-01-07",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-31",
             "keyword": [
                 "bicycles & pedestrians",
                 "intelligent transportation systems (its)",
@@ -96451,51 +96463,55 @@
                 "sensor data",
                 "traffic safety"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "ITS JPO Data Support",
-                "hasEmail": "mailto:data.itsjpo@dot.gov"
-            },
+            "landingPage": "https://its.dot.gov/isc/",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-31",
+            "programCode": [
+                "021:042"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Department of Transportation"
             },
-            "identifier": "https://data.transportation.gov/api/views/vq7s-mv3v",
-            "description": "This dataset was collected as part of the U.S. Department of Transportation (U.S. DOT) Intersection Safety Challenge (hereafter, \u201cthe Challenge\u201d) for Stage 1B: System Assessment and Virtual Testing. Multi-sensor data were collected at a controlled test roadway intersection the Federal Highway Administration (FHWA) Turner-Fairbank Highway Research Center (TFHRC) Smart Intersection facility in McLean, VA from October 2023 through March 2024. The data include potential conflict-based and non-conflict-based experimental scenarios between vulnerable road users (e.g., pedestrians, bicyclists) and vehicles during both daytime and nighttime conditions. Note that no actual human vulnerable road users were put at risk of being involved in a collision during the data collection efforts. The provided data (hereafter, \u201cthe Challenge Dataset\u201d) are unlabeled training data (without ground truth) that were collected to be used for intersection safety system algorithm training, refinement, tuning, and/or validation, but may have additional uses. For a summary of the Stage 1B data collection effort, please see this video: https://youtu.be/csirVHFa2Cc.\n\nThe Challenge Dataset includes data at a single, signalized four-way intersection from 20 roadside sensors and traffic control devices, including eight closed-circuit television (CCTV) visual cameras, five thermal cameras, two light detection and ranging (LiDAR) sensors, and four radar sensors. Intrinsic calibration was performed for all visual and thermal cameras. Extrinsic calibration was performed for specific pairs of roadside sensors. Additionally, the traffic signal phase and timing data and vehicle and/or pedestrian calls to the traffic signal controller (if any) are also provided.\n\nThe total number of unique runs in the Challenge Dataset is 1,104, bringing the total size of the dataset to approximately 1 TB. A sample of 20 unique runs from the Challenge Dataset is provided here for download, inspection, and use. If, after inspecting this sample, a potential data user would like access to download the full Challenge Dataset, a request can be made via the form here: https://its.dot.gov/data/data-request\n\nFor more details about the data collection, supplemental files, organization and dictionary, and sensor calibration, see the attached \u201cU.S. DOT ISC Stage 1B ITS DataHub Metadata_v1.0.pdf\u201d document. For more information on the background of the Intersection Safety Challenge Stage 1B, please visit: its.dot.gov/isc.",
-            "title": "Intersection Safety Challenge Stage 1B Training Data Sample",
-            "programCode": [
-                "021:042"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://its.dot.gov/data/data-request",
-                    "mediaType": "text/html",
-                    "description": "The link below goes to the form to request the full dataset and is NOT the sample data. The sample dataset can be found below in the ATTACHMENTS section of the metadata. If you are ready to request the full dataset, you can use the link below to submit a request. "
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Intersection Safety Challenge Stage 1B Training Data Sample"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www-nrd.nhtsa.dot.gov/CMSWeb/listpublications.aspx%3FId=19&ShowBy=Category",
+            "agencyProgramURL": "http://www.nhtsa.gov/Research/Human+Factors/Seatbelt+and+Child+Seat+Use",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/vqd9-277u",
-            "issued": "2006-12-31",
-            "temporal": "2005-04-01/2005-08-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www-nrd.nhtsa.dot.gov/Pubs/811852.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "ftp://ftp.nhtsa.dot.gov/Child_Seat_Usage_Surveys/LATCH_Use_and_Misuse_Study_2006/contents.pdf",
+            "describedByType": "application/pdf",
+            "description": "Provide information on the impact of LATCH on child seat use. It will show if consumers are using LATCH to install child safety seats, if they are easy to install and if they are installed correctly.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/Child_Seat_Usage_Surveys/LATCH_Use_and_Misuse_Study_2006/tblvehicle.sas7bdat",
+                    "mediaType": "text/plain",
+                    "title": "SAS Vehicle Data"
+                }
             ],
+            "identifier": "539.2",
+            "isPartOf": "DOT-539",
+            "issued": "2006-12-31",
             "keyword": [
                 "child restraint systems",
                 "css",
@@ -96506,60 +96522,60 @@
                 "research methodology",
                 "use and misuse"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "539.2",
+            "landingPage": "https://data.transportation.gov/d/vqd9-277u",
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
-            "title": "Child Restraint Use Survey:  LATCH Use and Misuse - SAS Vehicle Data",
-            "isPartOf": "DOT-539",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Human+Factors/Seatbelt+and+Child+Seat+Use",
-            "describedByType": "application/pdf",
-            "programCode": [
-                "021:032"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/Child_Seat_Usage_Surveys/LATCH_Use_and_Misuse_Study_2006/tblvehicle.sas7bdat",
-                    "mediaType": "text/plain",
-                    "title": "SAS Vehicle Data"
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
+            "title": "Child Restraint Use Survey:  LATCH Use and Misuse - SAS Vehicle Data"
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
-            "landingPage": "https://data.transportation.gov/d/vqf2-bk2w",
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
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/inctab.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Accident Summary Tables"
+                }
             ],
+            "identifier": "199.15",
+            "isPartOf": "DOT-199",
+            "issued": "2010-09-29",
             "keyword": [
                 "acts of god",
                 "collisions",
@@ -96570,61 +96586,60 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "199.15",
+            "landingPage": "https://data.transportation.gov/d/vqf2-bk2w",
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
-            "title": "Rail Equipment Accidents - Accident Summary Tables",
-            "isPartOf": "DOT-199",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:036"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/inctab.aspx",
-                    "mediaType": "text/csv",
-                    "title": "Accident Summary Tables"
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
+            "title": "Rail Equipment Accidents - Accident Summary Tables"
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
-            "landingPage": "https://data.transportation.gov/d/vr27-gvvk",
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
+            "identifier": "124.2",
+            "isPartOf": "DOT-124",
+            "issued": "2000-01-01",
             "keyword": [
                 "90 day failure to pay.",
                 "bus",
@@ -96643,60 +96658,61 @@
                 "safety and fitness electronic records",
                 "unsatifactory = unfit"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "124.2",
+            "landingPage": "https://data.transportation.gov/d/vr27-gvvk",
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
+            "agencyDataSeriesURL": "http://www.infopave.com/",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/research/tfhrc/programs/infrastructure/pavements/ltpp/",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/vrpk-kqgf",
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
+                    "description": "This access point provides access to the LTPP InfoPave non-LTPP data set including C-LTPP.",
+                    "downloadURL": "https://infopave.fhwa.dot.gov/%3FGoto=NON-LTPP",
+                    "mediaType": "application/atom+xml",
+                    "title": "Non-LTTP"
+                }
             ],
+            "identifier": "679.10",
+            "isPartOf": "DOT-679",
+            "issued": "1993-07-01",
             "keyword": [
                 "asphalt concrete",
                 "continuously reinforced concrete pavement",
@@ -96713,57 +96729,59 @@
                 "texture",
                 "traffic loading"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "679.10",
+            "landingPage": "https://data.transportation.gov/d/vrpk-kqgf",
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
-            "title": "Long-Term Pavement Performance (LTPP) - Non-LTTP",
-            "isPartOf": "DOT-679",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/research/tfhrc/programs/infrastructure/pavements/ltpp/",
-            "programCode": [
-                "021:009"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/atom+xml",
-                    "downloadURL": "https://infopave.fhwa.dot.gov/%3FGoto=NON-LTPP",
-                    "description": "This access point provides access to the LTPP InfoPave non-LTPP data set including C-LTPP.",
-                    "@type": "dcat:Distribution",
-                    "title": "Non-LTTP"
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
+            "title": "Long-Term Pavement Performance (LTPP) - Non-LTTP"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/vt34-qn6n",
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
+                    "description": "2012 Georgia HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/georgia2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Georgia"
+                }
+            ],
+            "identifier": "678.64",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -96777,64 +96795,36 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.64",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Georgia",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/vt34-qn6n",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/georgia2012.zip",
-                    "description": "2012 Georgia HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Georgia"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Georgia"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/vtsb-5rxn",
-            "issued": "2023-11-09",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/vtsb-5rxn",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "Rail Crossings",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -96842,40 +96832,54 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/vtsb-5rxn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vtsb-5rxn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vtsb-5rxn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/vtsb-5rxn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vtsb-5rxn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vtsb-5rxn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/vtsb-5rxn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vtsb-5rxn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vtsb-5rxn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/vtsb-5rxn",
+            "issued": "2023-11-09",
+            "landingPage": "https://data.transportation.gov/d/vtsb-5rxn",
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
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/vu39-vtqh",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Transportation Analysis",
+                "hasEmail": "mailto:long.nguyen@dot.gov"
+            },
+            "description": "Freight Facts and Figures - Freight Transportation Safety",
+            "identifier": "https://data.transportation.gov/api/views/vu39-vtqh",
             "issued": "2019-09-24",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-09",
             "keyword": [
                 "bts",
                 "bureau of transportation statistics",
@@ -96886,58 +96890,33 @@
                 "freight transportation",
                 "safety"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Transportation Analysis",
-                "hasEmail": "mailto:long.nguyen@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/vu39-vtqh",
+            "modified": "2023-03-09",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statisitics"
             },
-            "identifier": "https://data.transportation.gov/api/views/vu39-vtqh",
-            "description": "Freight Facts and Figures - Freight Transportation Safety",
-            "title": "Freight Transportation Safety",
-            "programCode": [
-                "021:053"
-            ],
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Freight Transportation Safety"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/vudg-jaa5",
             "bureauCode": [
                 "021:04"
             ],
-            "rights": "Business-sensitive data has been removed from this dataset",
-            "issued": "2020-05-05",
-            "@type": "dcat:Dataset",
-            "temporal": "2017-01-01/2017-12-31",
-            "modified": "2020-07-07",
-            "keyword": [
-                "ferry",
-                "passenger ferry",
-                "terminal",
-                "transit",
-                "transportation"
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
-            "identifier": "https://data.transportation.gov/api/views/vudg-jaa5",
+            "dataQuality": true,
             "description": "Reported 2017 calendar year ferry terminals as surveyed by the 2018 NCFO. \n\nSome terminals are reported by more than one ferry operator.",
-            "title": "National Census of Ferry Operators (NCFO) 2018: Operator Terminal data",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -96945,52 +96924,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/vudg-jaa5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vudg-jaa5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vudg-jaa5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/vudg-jaa5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vudg-jaa5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vudg-jaa5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/vudg-jaa5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vudg-jaa5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vudg-jaa5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S., U.S. Territories, and applicable Canadian providences",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/vudg-jaa5",
+            "issued": "2020-05-05",
+            "keyword": [
+                "ferry",
+                "passenger ferry",
+                "terminal",
+                "transit",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/vudg-jaa5",
             "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
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
+            "title": "National Census of Ferry Operators (NCFO) 2018: Operator Terminal data"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/vv3u-45rg",
-            "issued": "2023-01-05",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/vv3u-45rg",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "North American Rail Network (NARN)",
-            "title": "NARN",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -96998,72 +96988,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/vv3u-45rg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vv3u-45rg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vv3u-45rg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/vv3u-45rg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vv3u-45rg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vv3u-45rg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/vv3u-45rg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vv3u-45rg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vv3u-45rg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/vv3u-45rg",
+            "issued": "2023-01-05",
+            "landingPage": "https://data.transportation.gov/d/vv3u-45rg",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "NARN"
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
-            "landingPage": "https://data.transportation.gov/d/vv4k-w3xw",
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
-            "identifier": "97.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
-            "description": "The Large Truck* Crash Causation Study (LTCCS) is based on a three-year data collection project conducted by the Federal Motor Carrier Safety Administration (FMCSA) and the National Highway Traffic Safety Administration (NHTSA) of the U.S. Department of Transportation (DOT). LTCCS is the first-ever national study to attempt to determine the critical events and associated factors that contribute to serious large truck crashes allowing DOT and others to implement effective countermeasures to reduce the occurrence and severity of these crashes.",
-            "title": "Large Truck Crash Causation Study (LTCCS) - File 1 (Excel)",
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
@@ -97072,40 +97051,51 @@
                     "title": "File 1 (Excel)"
                 }
             ],
-            "spatial": "National estimates",
-            "describedBy": "http://ai.fmcsa.dot.gov/ltccs/data/documents/LTCCS_Codebook.pdf",
-            "dataQuality": true,
+            "identifier": "97.1",
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
+            "landingPage": "https://data.transportation.gov/d/vv4k-w3xw",
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
+            "title": "Large Truck Crash Causation Study (LTCCS) - File 1 (Excel)"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/vv73-zjhi",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/vv73-zjhi",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "World",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -97113,40 +97103,54 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/vv73-zjhi/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vv73-zjhi/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vv73-zjhi/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/vv73-zjhi/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vv73-zjhi/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vv73-zjhi/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/vv73-zjhi/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vv73-zjhi/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vv73-zjhi/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/vv73-zjhi",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/vv73-zjhi",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "World"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/vvk5-xjjp",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Transportation Analysis",
+                "hasEmail": "mailto:long.nguyen@dot.gov"
+            },
+            "description": "Freight Facts and Figures - Freight Transportation System Condition and Performance",
+            "identifier": "https://data.transportation.gov/api/views/vvk5-xjjp",
             "issued": "2019-07-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-26",
             "keyword": [
                 "bts",
                 "bureau of transportation statistics",
@@ -97158,65 +97162,39 @@
                 "freight transportation",
                 "performance"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Transportation Analysis",
-                "hasEmail": "mailto:long.nguyen@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/vvk5-xjjp",
+            "modified": "2024-09-26",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statisitics"
             },
-            "identifier": "https://data.transportation.gov/api/views/vvk5-xjjp",
-            "description": "Freight Facts and Figures - Freight Transportation System Condition and Performance",
-            "title": "Freight Transportation System Condition & Performance",
-            "programCode": [
-                "021:053"
-            ],
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Freight Transportation System Condition & Performance"
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
-            "landingPage": "https://data.transportation.gov/d/vvms-qhyg",
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
-            "identifier": "18.26",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "The Traffic Volume Trends montly report is a natinal data report that provides quality controlled vehicle miles traveled data for each State for all roadways",
-            "title": "Monthly Traffic Volume Trends - January 2010",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -97225,35 +97203,73 @@
                     "title": "January 2010"
                 }
             ],
+            "identifier": "18.26",
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
+            "landingPage": "https://data.transportation.gov/d/vvms-qhyg",
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
+            "title": "Monthly Traffic Volume Trends - January 2010"
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
-            "landingPage": "https://data.transportation.gov/d/vvt3-t628",
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
+                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/gxrtab.aspx",
+                    "mediaType": "text/csv",
+                    "title": "Hwy/Rail Incidents Summary Tables"
+                }
             ],
+            "identifier": "214.13",
+            "isPartOf": "DOT-214",
+            "issued": "2010-09-29",
             "keyword": [
                 "accident",
                 "casualty",
@@ -97266,122 +97282,84 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "214.13",
+            "landingPage": "https://data.transportation.gov/d/vvt3-t628",
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
-            "title": "Highway Rail Accidents - Hwy/Rail Incidents Summary Tables",
-            "isPartOf": "DOT-214",
-            "agencyProgramURL": "http://safetydata.fra.dot.gov/OfficeofSafety/",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://safetydata.fra.dot.gov/OfficeofSafety/publicsite/Query/gxrtab.aspx",
-                    "mediaType": "text/csv",
-                    "title": "Hwy/Rail Incidents Summary Tables"
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
+            "title": "Highway Rail Accidents - Hwy/Rail Incidents Summary Tables"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/vw6b-h97a",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Ken Notis",
+                "hasEmail": "mailto:ken.notis@dot.gov"
+            },
+            "description": "Page describes the U.S. Department of Transportation, Bureau of Transportation Statistics' Government Transportation Financial Statistics (GTFS).",
+            "identifier": "https://data.transportation.gov/api/views/vw6b-h97a",
             "issued": "2020-12-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-02-28",
             "keyword": [
                 "finance",
                 "government expenditures",
                 "government revenue",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Ken Notis",
-                "hasEmail": "mailto:ken.notis@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/vw6b-h97a",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-02-28",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/vw6b-h97a",
-            "description": "Page describes the U.S. Department of Transportation, Bureau of Transportation Statistics' Government Transportation Financial Statistics (GTFS).",
-            "title": "Government Transportation Financial Statistics (GTFS) for TRB",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
-            ]
+            ],
+            "title": "Government Transportation Financial Statistics (GTFS) for TRB"
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
-            "landingPage": "https://data.transportation.gov/d/vwt9-bpwz",
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
-            "identifier": "1840.1",
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
@@ -97390,65 +97368,54 @@
                     "title": "Browse the latest tests"
                 }
             ],
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/database/veh/vehdb-export-fields.htm",
-            "dataQuality": true,
+            "identifier": "1840.1",
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
+            "landingPage": "https://data.transportation.gov/d/vwt9-bpwz",
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
-            "landingPage": "https://www.its.dot.gov/pilots/pilots_nycdot.htm",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2021-06-04",
-            "temporal": "2021-01/P12M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
-            "references": [
-                "https://www.its.dot.gov/pilots/technical_assistance_events.htm"
-            ],
-            "keyword": [
-                "aftermarket safety device (asd)",
-                "arterial",
-                "basic safety message (bsm)",
-                "connected vehicle message",
-                "connected vehicle pilot (cvp)",
-                "field test",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "new york city",
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
-            "identifier": "https://data.transportation.gov/api/views/vxmm-9bi5",
+            "dataQuality": true,
             "description": "This dataset contains a one-month sample of flattened EVENT data records from the New York City (NYC) Connected Vehicle (CV) Pilot that have undergone obfuscation of precise time and location details as well as other vehicle identifiers. The full unflattened event data from NYC CV pilot can be found in the <a href=\"http://usdot-its-cvpilot-publicdata.s3.amazonaws.com/index.html\" target=\"_blank\" >ITS Sandbox</a>.\n\nEach EVENT record documents the details of one application warning that occurred on an Aftermarket Safety Device (ASD) in an equipped host vehicle and includes CV messages from a defined recording time both before and after the warning was generated by the host ASD. Messages in the recording time window include the Basic Safety Messages (BSM) of the host vehicle that received the warning, as well as other BSMs received from the warning target equipped vehicle (for V2V applications) or other nearby equipped vehicles. Depending on the application warning type, MAP messages, Signal Phase and Timing (SPaT) messages, and Traveler Information Messages (TIM) that were heard by the host vehicle may also be included in the event record.",
-            "title": "New York City CV Pilot EVENT Data One Month Sample",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -97456,50 +97423,98 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/vxmm-9bi5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vxmm-9bi5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vxmm-9bi5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/vxmm-9bi5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vxmm-9bi5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vxmm-9bi5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/vxmm-9bi5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vxmm-9bi5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vxmm-9bi5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/vxmm-9bi5",
+            "issued": "2021-06-04",
+            "keyword": [
+                "aftermarket safety device (asd)",
+                "arterial",
+                "basic safety message (bsm)",
+                "connected vehicle message",
+                "connected vehicle pilot (cvp)",
+                "field test",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "new york city",
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
+                "021:013"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
+            "references": [
+                "https://www.its.dot.gov/pilots/technical_assistance_events.htm"
+            ],
             "spatial": "New York City",
-            "dataQuality": true,
+            "temporal": "2021-01/P12M",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "New York City CV Pilot EVENT Data One Month Sample"
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
-            "landingPage": "https://data.transportation.gov/d/vxsc-3jii",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/09septvt/09septvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "September 2009"
+                }
             ],
+            "identifier": "18.30",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -97509,79 +97524,47 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.30",
+            "landingPage": "https://data.transportation.gov/d/vxsc-3jii",
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
-            "title": "Monthly Traffic Volume Trends - September 2009",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/09septvt/09septvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "September 2009"
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
+            "title": "Monthly Traffic Volume Trends - September 2009"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "This data set contains personally identifiable information (PII) and is not made available to the public.",
+            "accrualPeriodicity": "R/P1Y",
+            "analysisUnit": "employee",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/vy9h-ek4k",
-            "issued": "2014-12-08",
-            "temporal": "R/2014-12-08/P1Y",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "modified": "2024-11-14",
-            "keyword": [
-                "leave",
-                "shift",
-                "time"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "1650.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
             "description": "Consolidated Automated Time and Labor Entry (CASTLE) contains the following data elements, but is not limited to work stop and start times, leave hours used, personally identifiable information (PII), project and tasks of reimbursable work being performed, and Common Accounting Number (CAN).",
-            "title": "CASTLE -",
-            "primaryITInvestmentUII": "021-129153447",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -97589,58 +97572,54 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "theme": [
-                "Transportation"
+            "identifier": "1650.0",
+            "issued": "2014-12-08",
+            "keyword": [
+                "leave",
+                "shift",
+                "time"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "analysisUnit": "employee",
-            "categoryDesignation": "Administrative",
+            "landingPage": "https://data.transportation.gov/d/vy9h-ek4k",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-9646"
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-14",
+            "phone": "202-366-9646",
+            "primaryITInvestmentUII": "021-129153447",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "rights": "This data set contains personally identifiable information (PII) and is not made available to the public.",
+            "temporal": "R/2014-12-08/P1Y",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "CASTLE -"
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
-            "landingPage": "https://data.transportation.gov/d/vyed-gnx5",
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
-            "identifier": "524.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
             "description": "STATE DATA REPORTING SYSTEMS. Annual reports on the Fatality Analysis Reporting System (FARS) which is data regarding fatalities that is collected by a FARS analyst from each State and provided to NHTSA.",
-            "title": "GES Reports - 2001",
-            "isPartOf": "DOT-524",
-            "agencyProgramURL": "http://www.nhtsa.gov/NASS",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -97649,62 +97628,101 @@
                     "title": "2001"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www-nrd.nhtsa.dot.gov/cats/listpublications.aspx%3FId=k&ShowBy=DocType",
-            "dataQuality": true,
+            "identifier": "524.1",
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
+            "landingPage": "https://data.transportation.gov/d/vyed-gnx5",
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
+            "title": "GES Reports - 2001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/vyng-663x",
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
-            "identifier": "https://data.transportation.gov/api/views/vyng-663x",
             "description": "Facts and figures on ferry ridership",
-            "title": "National Census of Ferry Operators (NCFO) 2018: Ferry Passenger and Vehicle Boarding Counts",
+            "identifier": "https://data.transportation.gov/api/views/vyng-663x",
+            "issued": "2020-05-28",
+            "landingPage": "https://data.transportation.gov/d/vyng-663x",
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
+            "title": "National Census of Ferry Operators (NCFO) 2018: Ferry Passenger and Vehicle Boarding Counts"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/vyy4-7cq3",
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
+                    "description": "2013 Montana HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/montana2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 Montana"
+                }
+            ],
+            "identifier": "678.130",
+            "isPartOf": "DOT-678",
             "issued": "1981-11-01",
-            "temporal": "R/1981-11-01/P1Y",
-            "@type": "dcat:Dataset",
-            "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
             "keyword": [
                 "aadt",
                 "condition",
@@ -97718,96 +97736,68 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.130",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 Montana",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/vyy4-7cq3",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/montana2013.zip",
-                    "description": "2013 Montana HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 Montana"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 Montana"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:36"
             ],
-            "landingPage": "https://data.transportation.gov/d/vz8r-cbsv",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NTD Program Support",
+                "hasEmail": "mailto:NTDHelp@dot.gov"
+            },
+            "description": "A national summary of capital expenses based on data reported by transit agencies to the National Transit Database (NTD) in Report Year 2023.\r\n\r\nNTD Data Summaries organize and summarize data from the 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis.\r\n\r\nThis summary is based on the 2023 Capital Use file on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
+            "identifier": "https://data.transportation.gov/api/views/vz8r-cbsv",
             "issued": "2024-10-16",
-            "@type": "dcat:Dataset",
-            "modified": "2024-10-17",
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
+            "landingPage": "https://data.transportation.gov/d/vz8r-cbsv",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-10-17",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Transit Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/vz8r-cbsv",
-            "description": "A national summary of capital expenses based on data reported by transit agencies to the National Transit Database (NTD) in Report Year 2023.\r\n\r\nNTD Data Summaries organize and summarize data from the 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis.\r\n\r\nThis summary is based on the 2023 Capital Use file on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
-            "title": "2023 NTD Annual Data Summary - Capital Expenses",
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "2023 NTD Annual Data Summary - Capital Expenses"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/vzh3-3a5q",
-            "issued": "2023-02-04",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/vzh3-3a5q",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "CSXT",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -97815,45 +97805,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/vzh3-3a5q/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vzh3-3a5q/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vzh3-3a5q/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/vzh3-3a5q/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vzh3-3a5q/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vzh3-3a5q/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/vzh3-3a5q/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/vzh3-3a5q/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/vzh3-3a5q/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/vzh3-3a5q",
+            "issued": "2023-02-04",
+            "landingPage": "https://data.transportation.gov/d/vzh3-3a5q",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "CSXT"
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
-            "landingPage": "https://data.transportation.gov/d/vzqv-j5g4",
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
+            "identifier": "25.1",
+            "isPartOf": "DOT-25",
+            "issued": "1980-01-01",
             "keyword": [
                 "crash",
                 "death",
@@ -97864,61 +97880,60 @@
                 "injury",
                 "vehicle"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "25.1",
+            "landingPage": "https://data.transportation.gov/d/vzqv-j5g4",
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
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://safer.fmcsa.dot.gov/CSP_Order.asp",
+            "agencyProgramURL": "http://safer.fmcsa.dot.gov/CSP_Order.asp",
+            "analysisUnit": "Motor Carrier",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/w25h-dsbi",
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
+            "identifier": "123.1",
+            "isPartOf": "DOT-123",
+            "issued": "2000-01-01",
             "keyword": [
                 "bus",
                 "company safety profile",
@@ -97935,77 +97950,43 @@
                 "safersys",
                 "safety and fitness electronic records"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "123.1",
+            "landingPage": "https://data.transportation.gov/d/w25h-dsbi",
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
-            "identifier": "https://data.transportation.gov/api/views/w2yw-84zu",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 2001",
-            "title": "Historic HPMS Data (Universe) - 2001",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -98013,64 +97994,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/w2yw-84zu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/w2yw-84zu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/w2yw-84zu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/w2yw-84zu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/w2yw-84zu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/w2yw-84zu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/w2yw-84zu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/w2yw-84zu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/w2yw-84zu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/w2yw-84zu",
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
+            "title": "Historic HPMS Data (Universe) - 2001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/w3m5-t2w3",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2022-02-17",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-13",
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
-            "identifier": "https://data.transportation.gov/api/views/w3m5-t2w3",
             "description": "Historic data updated on 07/14/2023. Q4 of 2023 and data for all years on systems allowing parking outside of a docking station updated on 06/04/2024.\r\n\r\nBikeshare ridership by system, year, month, and station at which trip ended for bikeshare systems with docking stations. Data available by month starting in January 2019. Months are rearranged to include the same number of days of the week across years (see below). Data designed to show the impacts of COVID-19 on bikeshare ridership as featured at https://maps.dot.gov/BTS/dockedbikeshare-COVID/\r\n\r\nRidership data not available for all docked bikeshare systems. Only docked bikeshare systems with ridership data shown. Some systems included in the data permit users to leave a bicycle outside of a docking station; these trips are not counted. Trips defined as rides from point A to B. If user makes trip from B to A on same day, counted as a second trip. Trips labeled as round trips in Metro Bike Share and Indego trip files counted as 2 trips. Trips with no trip time are not counted. Trips with no start station identifier and/or end station id are not counted in totals. Trips shorter than 1 minute or greater than 2 hours excluded. Days aligned to include the same days of weeks in 2019 and 2020. \r\n\r\nDays included in each month can be found in the attachment (https://data.bts.gov/api/views/6cfa-ipzd/files/36fde1b8-57c3-4d31-b9dc-bbc896ba346e?download=true&filename=days_included_in_docked_bikeshare_monthly_summaries.xlsx) \r\n\r\nTrips beginning on 12/31/2019 but ending on 01/01/2020 not included in totals. Data visualizations available at: https://data.bts.gov/stories/s/Summary-of-Docked-Bikeshare-Trips-by-System-and-Ot/7fgy-2zkf/",
-            "title": "Docked Bikeshare Ridership by System, Year, Month, and End Station",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -98078,68 +98061,66 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/w3m5-t2w3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/w3m5-t2w3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/w3m5-t2w3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/w3m5-t2w3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/w3m5-t2w3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/w3m5-t2w3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/w3m5-t2w3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/w3m5-t2w3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/w3m5-t2w3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/w3m5-t2w3",
+            "issued": "2022-02-17",
+            "keyword": [
+                "bikeshare",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/w3m5-t2w3",
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
+            "title": "Docked Bikeshare Ridership by System, Year, Month, and End Station"
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
-            "landingPage": "https://data.transportation.gov/d/w3zu-m99k",
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
-            "identifier": "696.3",
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
@@ -98148,58 +98129,57 @@
                     "title": "The Interstate System"
                 }
             ],
-            "spatial": "National",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "696.3",
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
+            "landingPage": "https://data.transportation.gov/d/w3zu-m99k",
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
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/bridge/nbi/ascii.cfm",
+            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
+            "analysisUnit": "Bridge structure",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/w43u-asr6",
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
-            "identifier": "693.9",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
             "description": "The NBI System is the collection of bridge inspection information and costs associated with bridge replacements of structurally deficient bridges on and off the NHS. This data is collected under the auspices of the National Bridge Inspection Standards (NBIS) as prescribed by law. The NBI System collects the information that is used to determine eligibility for NHS projects, performance measure reporting, NHS penalty determination, and reporting to Congress.  It supports oversight of the NBIS through various report tools, and provides data reporting that supports agency strategic goals.",
-            "title": "National Bridge Inventory System (NBI) - 2000",
-            "isPartOf": "DOT-693",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/bridge/nbi.cfm",
-            "primaryITInvestmentUII": "021-012940226",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -98208,71 +98188,105 @@
                     "title": "2000"
                 }
             ],
-            "spatial": "Point",
-            "describedBy": "http://www.fhwa.dot.gov/bridge/nbi/format.cfm",
-            "dataQuality": true,
+            "identifier": "693.9",
+            "isPartOf": "DOT-693",
+            "issued": "1992-12-31",
+            "keyword": [
+                "bridge",
+                "condition",
+                "deck",
+                "inspection",
+                "structure"
+            ],
+            "landingPage": "https://data.transportation.gov/d/w43u-asr6",
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
+            "title": "National Bridge Inventory System (NBI) - 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/w4cf-2j4p",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Government transportation revenue vs. expenditures",
+            "identifier": "https://data.transportation.gov/api/views/w4cf-2j4p",
             "issued": "2020-04-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-30",
             "keyword": [
                 "government",
                 "transportation expenditure",
                 "transportation revenue"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/w4cf-2j4p",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-12-30",
+            "phone": "202-366-DATA(3282)",
+            "programCode": [
+                "021:053"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Bureau of Transportation Statistics"
             },
-            "identifier": "https://data.transportation.gov/api/views/w4cf-2j4p",
-            "description": "Government transportation revenue vs. expenditures",
-            "title": "Transportation Economic Trends: Government Transportation Revenue vs Expenditure",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Transportation Economic Trends: Government Transportation Revenue vs Expenditure"
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
-            "landingPage": "https://data.transportation.gov/d/w4qn-hd8p",
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
+            "identifier": "322.1",
+            "isPartOf": "DOT-322",
+            "issued": "2011-01-18",
             "keyword": [
                 "administrative law judge opinions",
                 "airline citizenship",
@@ -98289,80 +98303,43 @@
                 "motor carriers",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DOT Socrata",
-                "hasEmail": "mailto:Socrata@dot.gov"
-            },
-            "identifier": "322.1",
+            "landingPage": "https://data.transportation.gov/d/w4qn-hd8p",
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
-            "landingPage": "https://data.transportation.gov/d/w6v2-vk5z",
             "bureauCode": [
                 "021:04"
             ],
-            "rights": "Business-sensitive data has been removed from this dataset",
-            "issued": "2018-03-06",
-            "@type": "dcat:Dataset",
-            "temporal": "2015-01-01/2015-12-31",
-            "modified": "2019-04-24",
-            "keyword": [
-                "ferry operators",
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
-            "identifier": "https://data.transportation.gov/api/views/w6v2-vk5z",
+            "dataQuality": true,
+            "describedBy": "https://www.bts.dot.gov/surveys/national-census-ferry-operators-ncfo/statement-methodology",
             "description": "The 2016 NCFO dataset is comprised of the responses of all operators who completed the 2016 Census, reporting 2015 calendar year ferry operations. The NCFO Flat File includes all five data files: ferry operator, vessel, terminal, segment, and operator segment data files in a single dataset.",
-            "title": "2016 National Census of Ferry Operators (Revised 03/18)",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -98370,59 +98347,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/w6v2-vk5z/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/w6v2-vk5z/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/w6v2-vk5z/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/w6v2-vk5z/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/w6v2-vk5z/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/w6v2-vk5z/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/w6v2-vk5z/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/w6v2-vk5z/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/w6v2-vk5z/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S., U.S. Territories, and applicable Canadian providences",
-            "describedBy": "https://www.bts.dot.gov/surveys/national-census-ferry-operators-ncfo/statement-methodology",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/w6v2-vk5z",
+            "issued": "2018-03-06",
+            "keyword": [
+                "ferry operators",
+                "freight",
+                "maritime",
+                "passenger",
+                "terminals",
+                "transit",
+                "travel",
+                "vessels"
+            ],
+            "landingPage": "https://data.transportation.gov/d/w6v2-vk5z",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2019-04-24",
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
+            "title": "2016 National Census of Ferry Operators (Revised 03/18)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/w8ea-nba4",
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
-            "identifier": "https://data.transportation.gov/api/views/w8ea-nba4",
             "description": "",
-            "title": "AFF - P12a - Air Carrier Fuel Efficiency by Year",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -98430,41 +98417,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/w8ea-nba4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/w8ea-nba4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/w8ea-nba4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/w8ea-nba4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/w8ea-nba4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/w8ea-nba4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/w8ea-nba4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/w8ea-nba4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/w8ea-nba4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/w8ea-nba4",
+            "issued": "2024-12-09",
+            "landingPage": "https://data.transportation.gov/d/w8ea-nba4",
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
+            "title": "AFF - P12a - Air Carrier Fuel Efficiency by Year"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:36"
             ],
-            "landingPage": "https://data.transportation.gov/d/w8ik-iy5a",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NTD Program Support",
+                "hasEmail": "mailto:NTDHelp@dot.gov"
+            },
+            "description": "A summary of public transit service data reported by transit agencies to the National Transit Database (NTD) in Report Year 2022.\r\n\r\nNTD Data Summaries organize and summarize data from the 2022 National Transit Database in a manner that is more useful for quick reference and summary analysis. \r\n\r\nThis summary is based on the 2022 Service database file on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
+            "identifier": "https://data.transportation.gov/api/views/w8ik-iy5a",
             "issued": "2023-09-11",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-10",
             "keyword": [
                 "passenger car service",
                 "passenger miles traveled",
@@ -98475,34 +98479,48 @@
                 "vehicle revenue miles",
                 "vehicles operated in maximum service"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NTD Program Support",
-                "hasEmail": "mailto:NTDHelp@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/w8ik-iy5a",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-09-10",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Transit Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/w8ik-iy5a",
-            "description": "A summary of public transit service data reported by transit agencies to the National Transit Database (NTD) in Report Year 2022.\r\n\r\nNTD Data Summaries organize and summarize data from the 2022 National Transit Database in a manner that is more useful for quick reference and summary analysis. \r\n\r\nThis summary is based on the 2022 Service database file on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.",
-            "title": "2022 NTD Annual Data Summary - Service",
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Public Transit"
-            ]
+            ],
+            "title": "2022 NTD Annual Data Summary - Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/w8q9-qktu",
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
+                    "description": "2012 New Jersey HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/newjersey2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 New Jersey"
+                }
+            ],
+            "identifier": "678.84",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -98516,79 +98534,39 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.84",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 New Jersey",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/w8q9-qktu",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/newjersey2012.zip",
-                    "description": "2012 New Jersey HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 New Jersey"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 New Jersey"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/w8r7-b5tm",
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
-            "identifier": "https://data.transportation.gov/api/views/w8r7-b5tm",
             "description": "Data for Artificial Intelligence: Data-Centric AI for Transportation: Work Zone Use Case proposes a data integration pipeline that enhances the utilization of work zone and traffic data from diversified platforms and introduces a novel deep learning model to predict the traffic speed and traffic collision likelihood during planned work zone events. This dataset is a raw sample of Maryland roadway speed data",
-            "title": "Data for Artificial Intelligence: Data-Centric AI for Transportation: Work Zone Use Case Raw Maryland Speed Data",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -98596,64 +98574,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/w8r7-b5tm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/w8r7-b5tm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/w8r7-b5tm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/w8r7-b5tm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/w8r7-b5tm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/w8r7-b5tm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/w8r7-b5tm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/w8r7-b5tm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/w8r7-b5tm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Maryland highway network",
+            "identifier": "https://data.transportation.gov/api/views/w8r7-b5tm",
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
+            "landingPage": "https://data.transportation.gov/d/w8r7-b5tm",
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
+            "title": "Data for Artificial Intelligence: Data-Centric AI for Transportation: Work Zone Use Case Raw Maryland Speed Data"
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
-            "identifier": "https://data.transportation.gov/api/views/w95q-6nqw",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System universe data for the year 2006",
-            "title": "Historic HPMS Data (Universe) - 2006",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -98661,47 +98642,84 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/w95q-6nqw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/w95q-6nqw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/w95q-6nqw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/w95q-6nqw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/w95q-6nqw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/w95q-6nqw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/w95q-6nqw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/w95q-6nqw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/w95q-6nqw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/w95q-6nqw",
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
+            "title": "Historic HPMS Data (Universe) - 2006"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/w96j-wdjt",
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
+                    "description": "2011 Alaska HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/alaska2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Alaska"
+                }
+            ],
+            "identifier": "678.3",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -98715,86 +98733,41 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.3",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Alaska",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/w96j-wdjt",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/alaska2011.zip",
-                    "description": "2011 Alaska HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Alaska"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Alaska"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/w96p-f2qv",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2021-08-17",
-            "@type": "dcat:Dataset",
-            "temporal": "2019-2023",
-            "modified": "2024-04-30",
-            "references": [
-                "https://rosap.ntl.bts.gov/view/dot/67520"
-            ],
-            "keyword": [
-                "counties",
-                "county",
-                "covid-19",
-                "distance",
-                "mobility",
-                "state",
-                "states",
-                "travel",
-                "trip",
-                "trips"
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
-            "identifier": "https://data.transportation.gov/api/views/w96p-f2qv",
+            "dataQuality": true,
             "description": "How many people are staying at home? How far are people traveling when they don\u2019t stay home? Which states and counties have more people taking trips? The Bureau of Transportation Statistics (BTS) now provides answers to those questions through our mobility statistics program.\n\nThe \"Trips by Distance\" data and number of people staying home and not staying home are estimated for the Bureau of Transportation Statistics by the Maryland Transportation Institute and Center for Advanced Transportation Technology Laboratory at the University of Maryland. The travel statistics are produced from an anonymized national panel of mobile device data from multiple sources. All data sources used in the creation of the metrics contain no personal information. Data analysis is conducted at the aggregate national, state, and county levels. A weighting procedure expands the sample of millions of mobile devices, so the results are representative of the entire population in a nation, state, or county. To assure confidentiality and support data quality, no data are reported for a county if it has fewer than 50 devices in the sample on any given day.\n\nTrips are defined as movements that include a stay of longer than 10 minutes at an anonymized location away from home. Home locations are imputed on a weekly basis. A movement with multiple stays of longer than 10 minutes before returning home is counted as multiple trips. Trips capture travel by all modes of transportation. including driving, rail, transit, and air.\n\nThe daily travel estimates are from a mobile device data panel from merged multiple data sources that address the geographic and temporal sample variation issues often observed in a single data source. The merged data panel only includes mobile devices whose anonymized location data meet a set of data quality standards, which further ensures the overall data quality and consistency. The data quality standards consider both temporal frequency and spatial accuracy of anonymized location point observations, temporal coverage and representativeness at the device level, spatial representativeness at the sample and county level, etc. A multi-level weighting method that employs both device and trip-level weights expands the sample to the underlying population at the county and state levels, before travel statistics are computed.\n\nThese data are experimental and may not meet all of our quality standards.  Experimental data products are created using new data sources or methodologies that benefit data users in the absence of other relevant products. We are seeking feedback from data users and stakeholders on the quality and usefulness of these new products. Experimental data products that meet our quality standards and demonstrate sufficient user demand may enter regular production if resources permit.\n\nThese data are made available under a public domain license. Data should be attributed to the \"Maryland Transportation Institute and Center for Advanced Transportation Technology Laboratory at the University of Maryland and the United States Bureau of Transportation Statistics.\" \n\nDaily data for a given week will be uploaded to the BTS website within 9-10 days of the end of the week in question (e.g., data for Sunday September 17-Saturday September 23 would be updated on Tuesday, October 3). All BTS visualizations and tables that rely on these data will update at approximately 10am ET on days when new data are received, processed, and uploaded. \n\nThe methodology used to develop these data can be found at: https://rosap.ntl.bts.gov/view/dot/67520.",
-            "title": "Trips by Distance",
-            "programCode": [
-                "021:052"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -98802,75 +98775,80 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/w96p-f2qv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/w96p-f2qv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/w96p-f2qv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/w96p-f2qv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/w96p-f2qv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/w96p-f2qv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/w96p-f2qv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/w96p-f2qv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/w96p-f2qv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/w96p-f2qv",
+            "issued": "2021-08-17",
+            "keyword": [
+                "counties",
+                "county",
+                "covid-19",
+                "distance",
+                "mobility",
+                "state",
+                "states",
+                "travel",
+                "trip",
+                "trips"
+            ],
+            "landingPage": "https://data.transportation.gov/d/w96p-f2qv",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-04-30",
+            "programCode": [
+                "021:052"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "references": [
+                "https://rosap.ntl.bts.gov/view/dot/67520"
+            ],
             "spatial": "U.S. counties, U.S. states",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1W",
+            "temporal": "2019-2023",
             "theme": [
                 "Mobility"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Trips by Distance"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Access restricted under the Privacy Act of 1974; see Privacy Impact Assessment at http://www.dot.gov/individuals/privacy/pia-parking-and-transit-benefit-system-ptbs",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/w9dc-wn89",
-            "issued": "2014-10-24",
-            "temporal": "R/2013-01-01/PT1S",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "benefit",
-                "employee",
-                "funding",
-                "inter-agency",
-                "supervisor",
-                "transaction",
-                "transit"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "588.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
             "description": "This data set contains information about any US government agency participating in the transit benefits program, funding agreements, individual participating Federal employees and details about commutes, supervisors and supervisory approvals, fare media in use, and transaction histories.",
-            "title": "Transit Benefit Program Data -",
-            "primaryITInvestmentUII": "021-132481137",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -98878,43 +98856,51 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "theme": [
-                "Transportation"
+            "identifier": "588.0",
+            "issued": "2014-10-24",
+            "keyword": [
+                "benefit",
+                "employee",
+                "funding",
+                "inter-agency",
+                "supervisor",
+                "transaction",
+                "transit"
             ],
-            "accrualPeriodicity": "R/PT1S",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/w9dc-wn89",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-7022"
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-14",
+            "phone": "202-366-7022",
+            "primaryITInvestmentUII": "021-132481137",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "rights": "Access restricted under the Privacy Act of 1974; see Privacy Impact Assessment at http://www.dot.gov/individuals/privacy/pia-parking-and-transit-benefit-system-ptbs",
+            "temporal": "R/2013-01-01/PT1S",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Transit Benefit Program Data -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/wahn-z3rq",
             "bureauCode": [
                 "021:17"
             ],
-            "issued": "2023-12-08",
-            "@type": "dcat:Dataset",
-            "modified": "2025-02-01",
-            "keyword": [
-                "operating authority",
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
-            "identifier": "https://data.transportation.gov/api/views/wahn-z3rq",
             "description": "Records showing the history of each authority granted to a carrier/broker/freight forwarder, along with the dates of the original authority action (e.g., \u201cgranted\u201d) and the final authority action (e.g., \u201crevoked\u201d). The dataset contains the DOT number and docket number of the entity that holds or held the authority. As there can be multiple authorities for a single entity, there may be multiple records for an entity.  See dataset attachment \"FMCSA Dataset Description and Data Definitions - Select Datasets\" for more information.",
-            "title": "AuthHist - All With History",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -98922,20 +98908,38 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/wahn-z3rq",
+            "issued": "2023-12-08",
+            "keyword": [
+                "operating authority",
+                "motor carrier"
+            ],
+            "landingPage": "https://data.transportation.gov/d/wahn-z3rq",
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
+            "title": "AuthHist - All With History"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/wb5m-jbi7",
             "bureauCode": [
                 "021:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bureau of Transportation Statistics",
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
+            },
+            "description": "Transportation Expenditures by Selected Household Characteristics by Income Quintile. Investigates transportation by income quintile by region, urban vs rural, households with earners, work status, households with a member 65 and over, family type, race, and ethnicity. Vehicle trips, vehicle miles traveled, person trips, and person miles traveled by income quintile and select characteristics. Percent of after-tax income spent on transportation by income quintile and select characteristics. Change in share of after-tax income spent on transportation by income quintile and select characteristics.",
+            "identifier": "https://data.transportation.gov/api/views/wb5m-jbi7",
             "issued": "2023-09-12",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
             "keyword": [
                 "income quintile characteristics",
                 "income quintiles",
@@ -98951,41 +98955,53 @@
                 "vehicle miles traveled",
                 "vehicle trips"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
+            "landingPage": "https://data.transportation.gov/d/wb5m-jbi7",
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
-            "identifier": "https://data.transportation.gov/api/views/wb5m-jbi7",
-            "description": "Transportation Expenditures by Selected Household Characteristics by Income Quintile. Investigates transportation by income quintile by region, urban vs rural, households with earners, work status, households with a member 65 and over, family type, race, and ethnicity. Vehicle trips, vehicle miles traveled, person trips, and person miles traveled by income quintile and select characteristics. Percent of after-tax income spent on transportation by income quintile and select characteristics. Change in share of after-tax income spent on transportation by income quintile and select characteristics.",
-            "title": "Transportation Cost Burden: Transportation Expenditures by Selected Household Characteristics by Income Quintile",
-            "programCode": [
-                "021:053"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282)"
+            "title": "Transportation Cost Burden: Transportation Expenditures by Selected Household Characteristics by Income Quintile"
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
-            "landingPage": "https://data.transportation.gov/d/wbeg-8di7",
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
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2013_database/NTDdatabase.htm",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2013 Database"
+                }
             ],
+            "identifier": "21.17",
+            "isPartOf": "DOT-21",
+            "issued": "2010-10-01",
             "keyword": [
                 "agency",
                 "allocation",
@@ -99004,58 +99020,60 @@
                 "urbanized",
                 "vehicles"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John D. Giorgis",
-                "hasEmail": "mailto:john.giorgis@dot.gov"
-            },
-            "identifier": "21.17",
+            "landingPage": "https://data.transportation.gov/d/wbeg-8di7",
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
-            "title": "NTD Annual Module Data Set - 2013 Database",
-            "isPartOf": "DOT-21",
-            "agencyProgramURL": "http://www.ntdprogram.gov",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/2013_database/NTDdatabase.htm",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "2013 Database"
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
+            "title": "NTD Annual Module Data Set - 2013 Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/wbhc-pcym",
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
+                    "description": "2011 Georgia HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/georgia2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Georgia"
+                }
+            ],
+            "identifier": "678.12",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -99069,79 +99087,76 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.12",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Georgia",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/wbhc-pcym",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/georgia2011.zip",
-                    "description": "2011 Georgia HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Georgia"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Georgia"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/wbt4-7aaq",
-            "issued": "2023-12-13",
             "@type": "dcat:Dataset",
-            "modified": "2023-12-13",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sean Jahanmir",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/wbt4-7aaq",
+            "issued": "2023-12-13",
+            "landingPage": "https://data.transportation.gov/d/wbt4-7aaq",
+            "modified": "2023-12-13",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Corey Sinnott"
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
-            "landingPage": "https://data.transportation.gov/d/wcjd-cvs7",
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
+            "identifier": "113.2",
+            "isPartOf": "DOT-113",
+            "issued": "2004-03-15",
             "keyword": [
                 "accuracy",
                 "completeness",
@@ -99158,59 +99173,75 @@
                 "state safety data quality map",
                 "timelines"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "113.2",
+            "landingPage": "https://data.transportation.gov/d/wcjd-cvs7",
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
-            "landingPage": "https://data.transportation.gov/d/wd94-wugt",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2019-10-18",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-18",
-            "references": [
-                "https://www.transportation.gov/av/data/wzdx",
-                "http://aztech.org/"
+            "conformsTo": "https://www.transportation.gov/av/data/wzdx",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kate Hartman",
+                "hasEmail": "mailto:kate.hartman@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://github.com/usdot-jpo-ode/jpo-wzdx/tree/v1.1",
+            "description": "The WZDx Specification enables infrastructure owners and operators (IOOs) to make harmonized work zone data available for third party use. The intent is to make travel on public roads safer and more efficient through ubiquitous access to data on work zone activity. Specifically, the project aims to get data on work zones into vehicles to help automated driving systems (ADS) and human drivers navigate more safely.\n\nMCDOT leads the effort to aggregate and collect work zone data from the AZTech Regional Partners. A continuously updating archive of the WZDx feed data can be found at <a href=\"http://usdot-its-workzone-publicdata.s3.amazonaws.com/index.html\" target=\"_blank\" rel=\"noopener\">ITS WorkZone Data Sandbox</a>.  The live feed is currently compliant with <a href=\"https://github.com/usdot-jpo-ode/jpo-wzdx/tree/v1.1\" target=\"_blank\" rel=\"noopener\">WZDx specification version 1.1</a>.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/api/views/wd94-wugt/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.transportation.gov/api/views/wd94-wugt/columns.rdf",
+                    "describedByType": "application/rdf+xml",
+                    "downloadURL": "https://data.transportation.gov/api/views/wd94-wugt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.transportation.gov/api/views/wd94-wugt/columns.json",
+                    "describedByType": "application/json",
+                    "downloadURL": "https://data.transportation.gov/api/views/wd94-wugt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://data.transportation.gov/api/views/wd94-wugt/columns.xml",
+                    "describedByType": "application/xml",
+                    "downloadURL": "https://data.transportation.gov/api/views/wd94-wugt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
             ],
+            "identifier": "https://data.transportation.gov/api/views/wd94-wugt",
+            "issued": "2019-10-18",
             "keyword": [
                 "arizona",
                 "arizona department of transportation (adot)",
@@ -99243,89 +99274,63 @@
                 "trucking & motorcoaches",
                 "work zone data exchange (wzdx)"
             ],
-            "conformsTo": "https://www.transportation.gov/av/data/wzdx",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "US Department of Transportation"
-            },
-            "identifier": "https://data.transportation.gov/api/views/wd94-wugt",
-            "description": "The WZDx Specification enables infrastructure owners and operators (IOOs) to make harmonized work zone data available for third party use. The intent is to make travel on public roads safer and more efficient through ubiquitous access to data on work zone activity. Specifically, the project aims to get data on work zones into vehicles to help automated driving systems (ADS) and human drivers navigate more safely.\n\nMCDOT leads the effort to aggregate and collect work zone data from the AZTech Regional Partners. A continuously updating archive of the WZDx feed data can be found at <a href=\"http://usdot-its-workzone-publicdata.s3.amazonaws.com/index.html\" target=\"_blank\" rel=\"noopener\">ITS WorkZone Data Sandbox</a>.  The live feed is currently compliant with <a href=\"https://github.com/usdot-jpo-ode/jpo-wzdx/tree/v1.1\" target=\"_blank\" rel=\"noopener\">WZDx specification version 1.1</a>.",
-            "title": "Maricopa County Regional Work Zone Data Exchange (WZDx) v1.1 Feed Sample",
+            "landingPage": "https://data.transportation.gov/d/wd94-wugt",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
+            "modified": "2019-10-18",
             "programCode": [
                 "021:013"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/api/views/wd94-wugt/rows.csv?accessType=DOWNLOAD",
-                    "mediaType": "text/csv"
-                },
-                {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/wd94-wugt/rows.rdf?accessType=DOWNLOAD",
-                    "describedBy": "https://data.transportation.gov/api/views/wd94-wugt/columns.rdf",
-                    "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
-                },
-                {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/wd94-wugt/rows.json?accessType=DOWNLOAD",
-                    "describedBy": "https://data.transportation.gov/api/views/wd94-wugt/columns.json",
-                    "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
             },
-                {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/wd94-wugt/rows.xml?accessType=DOWNLOAD",
-                    "describedBy": "https://data.transportation.gov/api/views/wd94-wugt/columns.xml",
-                    "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
-                }
+            "references": [
+                "https://www.transportation.gov/av/data/wzdx",
+                "http://aztech.org/"
             ],
             "spatial": "Maricopa County, AZ",
-            "describedBy": "https://github.com/usdot-jpo-ode/jpo-wzdx/tree/v1.1",
-            "dataQuality": true,
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Maricopa County Regional Work Zone Data Exchange (WZDx) v1.1 Feed Sample"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/wdag-fwuu",
-            "issued": "2020-12-09",
             "@type": "dcat:Dataset",
-            "modified": "2020-12-09",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Alpha Wingfield",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/wdag-fwuu",
+            "issued": "2020-12-09",
+            "landingPage": "https://data.transportation.gov/d/wdag-fwuu",
+            "modified": "2020-12-09",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "NTAD for TRB"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/wdd4-qi38",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Railroad Safety",
+                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This report contains highway-rail grade crossing incidents, fatalities and injuries, broken out by public and private crossings and by groups of highway users involved (motor vehicle, pedestrian, or other). There are three views of data: (1) incidents where the rail equipment struck the highway user or was struck by the highway user, with breakouts by highway user type, (2) incidents where the rail equipment struck the highway user or was struck by the highway user, with breakouts by warning device at the crossings and (3) by railroad.",
+            "identifier": "https://data.transportation.gov/api/views/wdd4-qi38",
             "issued": "2023-08-04",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "crossings",
                 "fatalities",
@@ -99340,40 +99345,52 @@
                 "injury",
                 "railroad"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/wdd4-qi38",
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
-            "identifier": "https://data.transportation.gov/api/views/wdd4-qi38",
-            "description": "This report contains highway-rail grade crossing incidents, fatalities and injuries, broken out by public and private crossings and by groups of highway users involved (motor vehicle, pedestrian, or other). There are three views of data: (1) incidents where the rail equipment struck the highway user or was struck by the highway user, with breakouts by highway user type, (2) incidents where the rail equipment struck the highway user or was struck by the highway user, with breakouts by warning device at the crossings and (3) by railroad.",
-            "title": "Public and Private Highway-Rail Grade Crossing Incidents, Fatalities and Injuries (5.14)",
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
+            "title": "Public and Private Highway-Rail Grade Crossing Incidents, Fatalities and Injuries (5.14)"
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
-            "landingPage": "https://data.transportation.gov/d/wdrj-k6vb",
-            "issued": "2007-01-01",
-            "temporal": "2007-01-01/2014-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Geospatial",
             "collectionInstrument": "Transportation",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://hepgis.fhwa.dot.gov/hepgismaps11/ViewMap.aspx%3Fmap=Highway+Information%7CFederal+Aid+Functional+Class#",
+                    "mediaType": "text/html",
+                    "title": "Federal Aid Functional Class"
+                }
+            ],
+            "identifier": "692.4",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
             "keyword": [
                 "arra planning",
                 "fhwa",
@@ -99381,57 +99398,58 @@
                 "geospatial",
                 "map"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "692.4",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - Federal Aid Functional Class",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
+            "landingPage": "https://data.transportation.gov/d/wdrj-k6vb",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-08",
+            "phone": "708-283-3554",
             "primaryITInvestmentUII": "021-845083703",
             "programCode": [
                 "021:009"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://hepgis.fhwa.dot.gov/hepgismaps11/ViewMap.aspx%3Fmap=Highway+Information%7CFederal+Aid+Functional+Class#",
-                    "mediaType": "text/html",
-                    "title": "Federal Aid Functional Class"
-                }
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
             "spatial": "National, State, County",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "http://hepgis.fhwa.dot.gov/hepgismaps11/#",
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
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/weed-fa2u",
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
+                    "description": "2013 California HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/california2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 California"
+                }
+            ],
+            "identifier": "678.109",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -99445,71 +99463,39 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.109",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 California",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/weed-fa2u",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/california2013.zip",
-                    "description": "2013 California HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 California"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 California"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/wfz2-eft6",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-16",
-            "keyword": [
-                "transit mode",
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
-            "identifier": "https://data.transportation.gov/api/views/wfz2-eft6",
             "description": "This dataset details stations for each agency and mode for stations reported to the National Transit Database in report years 2022 and 2023. These data include the type of facility and the decade in which it was built.\n\nIn many cases, stations are reported by each mode and type of service that uses them. For example, a single station used by bus - directly operated, bus - purchased transportation, and commuter bus - directly operated would be reported three times. For more detail, please see the NTD Policy Manual.\n\nRural reporters do not report passenger stations and are not included in this file. Modes Demand Response, Demand Response - Taxi, Vanpool, and Publico also do not report stations and are also excluded.\n\nNTD Data Tables organize and summarize data from the 2022 and 2023 National Transit Database in a manner that is more useful for quick reference and summary analysis. This dataset is based on the 2022 and 2023 Facility Inventory database files.\n\nIn years 2015-2021, you can find this data in the \"Stations\" data table on NTD Program website, at https://transit.dot.gov/ntd/ntd-data.\n\nIf you have any other questions about this table, please contact the NTD Help Desk at NTDHelp@dot.gov.",
-            "title": "2022 - 2023 NTD Annual Data - Stations (by Mode and Age)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -99517,46 +99503,75 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/wfz2-eft6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wfz2-eft6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wfz2-eft6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/wfz2-eft6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wfz2-eft6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wfz2-eft6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/wfz2-eft6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wfz2-eft6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wfz2-eft6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/wfz2-eft6",
+            "issued": "2024-09-10",
+            "keyword": [
+                "transit mode",
+                "transit stations"
+            ],
+            "landingPage": "https://data.transportation.gov/d/wfz2-eft6",
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
+            "title": "2022 - 2023 NTD Annual Data - Stations (by Mode and Age)"
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
-            "landingPage": "https://data.transportation.gov/d/wgec-636f",
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
+            "identifier": "248.7",
+            "isPartOf": "DOT-248",
+            "issued": "2010-01-05",
             "keyword": [
                 "5",
                 "assessment",
@@ -99570,57 +99585,60 @@
                 "safety",
                 "star"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "248.7",
+            "landingPage": "https://data.transportation.gov/d/wgec-636f",
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
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/wgp2-azj4",
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
+                    "description": "2011 South Dakota HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/southdakota2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 South Dakota"
+                }
+            ],
+            "identifier": "678.43",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -99634,81 +99652,46 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.43",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 South Dakota",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/wgp2-azj4",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/southdakota2011.zip",
-                    "description": "2011 South Dakota HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 South Dakota"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 South Dakota"
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
-            "landingPage": "https://data.transportation.gov/d/wgtm-erw4",
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
-            "identifier": "11.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
+            "describedBy": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Transaction+Data+and+Reports",
             "description": "The Car Allowance Rebate System (CARS), otherwise known as Cash for Clunkers, was a program intended to provide economic incentives to United States residents to purchase a new and more fuel efficient vehicle when trading in a less full efficient vehicle. The program was promoted as providing stimulus to the economy by boosting auto sales, while putting safer, cleaner and more fuel efficient vehicles on the road.",
-            "title": "Car Allowance Rebate System (CARS) - Trade-In Vehicles - Consumer Survey csv file",
-            "isPartOf": "DOT-11",
-            "agencyProgramURL": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Officially+Ended",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -99717,54 +99700,49 @@
                     "title": "Consumer Survey csv file"
                 }
             ],
-            "spatial": "N/A",
-            "describedBy": "http://www.nhtsa.gov/Laws+&+Regulations/CARS+Program+Transaction+Data+and+Reports",
-            "dataQuality": false,
+            "identifier": "11.1",
+            "isPartOf": "DOT-11",
+            "issued": "2018-12-17",
+            "keyword": [
+                "cars",
+                "trade-in"
+            ],
+            "landingPage": "https://data.transportation.gov/d/wgtm-erw4",
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
+            "title": "Car Allowance Rebate System (CARS) - Trade-In Vehicles - Consumer Survey csv file"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/wgzf-9czk",
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
-                "water transportation",
-                "waterways tonnage"
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
-            "identifier": "https://data.transportation.gov/api/views/wgzf-9czk",
             "description": "This is the Operators file for the 2020 National Census of Ferry Operators. It is one of five data sets that make up the 2020 NCFO",
-            "title": "2020 NCFO Operators File",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -99772,92 +99750,101 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/wgzf-9czk/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wgzf-9czk/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wgzf-9czk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/wgzf-9czk/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wgzf-9czk/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wgzf-9czk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/wgzf-9czk/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wgzf-9czk/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wgzf-9czk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States. 50 States, WAshington DC and Territories",
+            "identifier": "https://data.transportation.gov/api/views/wgzf-9czk",
+            "issued": "2022-04-01",
+            "keyword": [
+                "ferry",
+                "ferry operators",
+                "ferry transit",
+                "passenger ferry",
+                "transportation",
+                "water transportation",
+                "waterways tonnage"
+            ],
+            "landingPage": "https://data.transportation.gov/d/wgzf-9czk",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2022-04-28",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "spatial": "United States. 50 States, WAshington DC and Territories",
             "theme": [
                 "Maritime and Waterways"
-            ]
+            ],
+            "title": "2020 NCFO Operators File"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/wgzr-nyxc",
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
                 "hasEmail": "mailto:answers@bts.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/wgzr-nyxc",
             "description": "The Federal Highway Administration's National Highway Construction Cost Index (NHCCI) is a quarterly price index intended to measure the average changes in the prices of highway construction costs over time and to convert current-dollar highway construction expenditures to real dollar expenditures.",
-            "title": "National Highway Construction Cost Index (NHCCI)",
+            "identifier": "https://data.transportation.gov/api/views/wgzr-nyxc",
+            "issued": "2025-01-03",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/wgzr-nyxc",
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
+            "title": "National Highway Construction Cost Index (NHCCI)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/whes-7fzk",
-            "issued": "2024-03-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-17",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Zereyakob Mekonnen",
                 "hasEmail": "mailto:z.mekonnen.ctr@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/whes-7fzk",
             "description": "",
-            "title": "Motor Vehicle Fuel Prices-Petroleum",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -99865,43 +99852,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/whes-7fzk/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/whes-7fzk/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/whes-7fzk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/whes-7fzk/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/whes-7fzk/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/whes-7fzk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/whes-7fzk/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/whes-7fzk/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/whes-7fzk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "https://data.transportation.gov/api/views/whes-7fzk",
+            "issued": "2024-03-20",
+            "landingPage": "https://data.transportation.gov/d/whes-7fzk",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-04-17",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Motor Vehicle Fuel Prices-Petroleum"
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
-            "landingPage": "https://data.transportation.gov/d/whp5-bu8t",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/04jantvt/04jantvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "January 2004"
+                }
             ],
+            "identifier": "18.128",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -99911,79 +99926,47 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.128",
+            "landingPage": "https://data.transportation.gov/d/whp5-bu8t",
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
-            "title": "Monthly Traffic Volume Trends - January 2004",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/04jantvt/04jantvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "January 2004"
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
+            "title": "Monthly Traffic Volume Trends - January 2004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/highwaytrustfund/",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/whz4-a496",
-            "issued": "2014-12-29",
-            "temporal": "R/2014-12-29/P1M",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative - Financial",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
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
-            "identifier": "685.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": false,
             "description": "Status of the Highway Trust Fund - The actual receipts, outlays and balances, posted each month shortly after month-end as the information becomes available.",
-            "title": "Status of the Highway Trust Fund - Status of the Highway Trust Fund",
-            "isPartOf": "DOT-685",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -99992,81 +99975,103 @@
                     "title": "Status of the Highway Trust Fund"
                 }
             ],
-            "spatial": "National",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "685.2",
+            "isPartOf": "DOT-685",
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
+            "landingPage": "https://data.transportation.gov/d/whz4-a496",
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
+            "title": "Status of the Highway Trust Fund - Status of the Highway Trust Fund"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/wini-d8gt",
-            "issued": "2022-04-06",
             "@type": "dcat:Dataset",
-            "modified": "2022-04-26",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joe McGill",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "Facts and figures related to terminals and their connecting segments.",
             "identifier": "https://data.transportation.gov/api/views/wini-d8gt",
+            "issued": "2022-04-06",
+            "landingPage": "https://data.transportation.gov/d/wini-d8gt",
+            "modified": "2022-04-26",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "Facts and figures related to terminals and their connecting segments.",
             "title": "Terminals and Segments"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/wj8z-p9dd",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2020-04-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
-            "keyword": [
-                "transportation productivity",
-                "transportation revenue"
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
-            "identifier": "https://data.transportation.gov/api/views/wj8z-p9dd",
             "description": "Freight and passenger transportation revenue per unit of output.",
-            "title": "Transportation Economic Trends: Productivity - Revenue per Unit of Output",
+            "identifier": "https://data.transportation.gov/api/views/wj8z-p9dd",
+            "issued": "2020-04-13",
+            "keyword": [
+                "transportation productivity",
+                "transportation revenue"
+            ],
+            "landingPage": "https://data.transportation.gov/d/wj8z-p9dd",
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
+            "title": "Transportation Economic Trends: Productivity - Revenue per Unit of Output"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/wjun-6kqb",
             "bureauCode": [
                 "021:27"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FRA Safety Data Team",
+                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "This is the landing page for data for Form 6180.54 Rail Equipment Accidents/Incidents.",
+            "identifier": "https://data.transportation.gov/api/views/wjun-6kqb",
             "issued": "2024-07-19",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-27",
             "keyword": [
                 "collision",
                 "derailment",
@@ -100074,41 +100079,54 @@
                 "train",
                 "train accident"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FRA Safety Data Team",
-                "hasEmail": "mailto:list-fra-safeteam@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/wjun-6kqb",
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
-            "identifier": "https://data.transportation.gov/api/views/wjun-6kqb",
-            "description": "This is the landing page for data for Form 6180.54 Rail Equipment Accidents/Incidents.",
-            "title": "Train Accident Reports - Landing Page",
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
+            "title": "Train Accident Reports - Landing Page"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/wjy3-ww6k",
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
+                    "description": "2012 Oklahoma HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/oklahoma2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Oklahoma"
+                }
+            ],
+            "identifier": "678.90",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -100122,60 +100140,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.90",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Oklahoma",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/wjy3-ww6k",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/oklahoma2012.zip",
-                    "description": "2012 Oklahoma HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Oklahoma"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Oklahoma"
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
-            "landingPage": "https://data.transportation.gov/d/wkec-wuw7",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/10septvt/10septvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "September 2010"
+                }
             ],
+            "identifier": "18.18",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -100185,58 +100200,54 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.18",
+            "landingPage": "https://data.transportation.gov/d/wkec-wuw7",
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
-            "title": "Monthly Traffic Volume Trends - September 2010",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/10septvt/10septvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "September 2010"
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
+            "title": "Monthly Traffic Volume Trends - September 2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.21949/1503749",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2016-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2017-07-25",
-            "references": [
-                "https://rosap.ntl.bts.gov/view/dot/32530"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Transportation Library Data Curator",
+                "hasEmail": "mailto:ntldatacurator@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "The datasets in this zip file are in support of Intelligent Transportation Systems Joint Program Office (ITS JPO) report FHWA-JPO-16-385, \"Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs \u2014 Evaluation Report for ATDM Program,\" and FHWA-JPO-16-389, \"Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs : Evaluation Report for the San Diego Testbed : Draft Report\". The files in this zip file are specifically related to the San Diego Testbed. The compressed zip files total 3.17 GB in size. The files have been uploaded as-is; no further documentation was supplied by NTL.  Direct download of data zip file: https://doi.org/10.21949/1500873 All located .docx files were converted to .pdf document files which are an open, archival format. These pdfs were then added to the zip file alongside the original .docx files. These files can be unzipped using any zip compression/decompression software. This zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .cvs text files which can be read using any text editor; .txt text files which can be read using any text editor; .docx document files which can be read in Microsoft Word and some other word processing programs; . xlsx spreadsheet files which can be read in Microsoft Excel and some other spreadsheet programs; .dat data files which may be text or multimedia; as well as GIS or mapping files in the following formats: .mxd, .dbf, .prj, .sbn, .shp., .shp.xml; which may be opened in ArcGIS or other GIS software. [software requirements] These files were last accessed in 2017.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "The datasets in this zip file are in support of Intelligent Transportation Systems Joint Program Office (ITS JPO) report FHWA-JPO-16-385, \"Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs \u2014 Evaluation Report for ATDM Program,\" and FHWA-JPO-16-389, \"Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs : Evaluation Report for the San Diego Testbed : Draft Report\". The files in this zip file are specifically related to the San Diego Testbed. The compressed zip files total 3.17 GB in size. The files have been uploaded as-is; no further documentation was supplied by NTL.  Direct download of data zip file: https://doi.org/10.21949/1500873 All located .docx files were converted to .pdf document files which are an open, archival format. These pdfs were then added to the zip file alongside the original .docx files. These files can be unzipped using any zip compression/decompression software. This zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .cvs text files which can be read using any text editor; .txt text files which can be read using any text editor; .docx document files which can be read in Microsoft Word and some other word processing programs; . xlsx spreadsheet files which can be read in Microsoft Excel and some other spreadsheet programs; .dat data files which may be text or multimedia; as well as GIS or mapping files in the following formats: .mxd, .dbf, .prj, .sbn, .shp., .shp.xml; which may be opened in ArcGIS or other GIS software. [software requirements] These files were last accessed in 2017.",
+                    "downloadURL": "https://doi.org/10.21949/1503749",
+                    "mediaType": "application/zip",
+                    "title": "Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs: Evaluation Report for the San Diego Testbed [supporting datasets]"
+                }
             ],
+            "identifier": "https://data.transportation.gov/api/views/wkrd-a869",
+            "issued": "2016-06-26",
             "keyword": [
                 "active transportation and demand management",
                 "ams san diego",
@@ -100252,82 +100263,89 @@
                 "traffic flow",
                 "travel demand"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Transportation Library Data Curator",
-                "hasEmail": "mailto:ntldatacurator@dot.gov"
-            },
+            "landingPage": "https://doi.org/10.21949/1503749",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2017-07-25",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/wkrd-a869",
-            "description": "The datasets in this zip file are in support of Intelligent Transportation Systems Joint Program Office (ITS JPO) report FHWA-JPO-16-385, \"Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs \u2014 Evaluation Report for ATDM Program,\" and FHWA-JPO-16-389, \"Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs : Evaluation Report for the San Diego Testbed : Draft Report\". The files in this zip file are specifically related to the San Diego Testbed. The compressed zip files total 3.17 GB in size. The files have been uploaded as-is; no further documentation was supplied by NTL.  Direct download of data zip file: https://doi.org/10.21949/1500873 All located .docx files were converted to .pdf document files which are an open, archival format. These pdfs were then added to the zip file alongside the original .docx files. These files can be unzipped using any zip compression/decompression software. This zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .cvs text files which can be read using any text editor; .txt text files which can be read using any text editor; .docx document files which can be read in Microsoft Word and some other word processing programs; . xlsx spreadsheet files which can be read in Microsoft Excel and some other spreadsheet programs; .dat data files which may be text or multimedia; as well as GIS or mapping files in the following formats: .mxd, .dbf, .prj, .sbn, .shp., .shp.xml; which may be opened in ArcGIS or other GIS software. [software requirements] These files were last accessed in 2017.",
-            "title": "Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs: Evaluation Report for the San Diego Testbed [supporting datasets]",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://doi.org/10.21949/1503749",
-                    "description": "The datasets in this zip file are in support of Intelligent Transportation Systems Joint Program Office (ITS JPO) report FHWA-JPO-16-385, \"Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs \u2014 Evaluation Report for ATDM Program,\" and FHWA-JPO-16-389, \"Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs : Evaluation Report for the San Diego Testbed : Draft Report\". The files in this zip file are specifically related to the San Diego Testbed. The compressed zip files total 3.17 GB in size. The files have been uploaded as-is; no further documentation was supplied by NTL.  Direct download of data zip file: https://doi.org/10.21949/1500873 All located .docx files were converted to .pdf document files which are an open, archival format. These pdfs were then added to the zip file alongside the original .docx files. These files can be unzipped using any zip compression/decompression software. This zip file contains files in the following formats: .pdf document files which can be read using any pdf reader; .cvs text files which can be read using any text editor; .txt text files which can be read using any text editor; .docx document files which can be read in Microsoft Word and some other word processing programs; . xlsx spreadsheet files which can be read in Microsoft Excel and some other spreadsheet programs; .dat data files which may be text or multimedia; as well as GIS or mapping files in the following formats: .mxd, .dbf, .prj, .sbn, .shp., .shp.xml; which may be opened in ArcGIS or other GIS software. [software requirements] These files were last accessed in 2017.",
-                    "@type": "dcat:Distribution",
-                    "title": "Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs: Evaluation Report for the San Diego Testbed [supporting datasets]"
-                }
+            "references": [
+                "https://rosap.ntl.bts.gov/view/dot/32530"
             ],
             "spatial": "United States, California, San Diego",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "language": [
-                "en-US"
-            ]
+            "title": "Analysis, Modeling, and Simulation (AMS) Testbed Development and Evaluation to Support Dynamic Mobility Applications (DMA) and Active Transportation and Demand Management (ATDM) Programs: Evaluation Report for the San Diego Testbed [supporting datasets]"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/wkw2-rxsq",
             "bureauCode": [
                 "021:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FHWA-Datahub",
+                "hasEmail": "mailto:Highway-Data@dot.gov"
+            },
+            "description": "",
+            "identifier": "https://data.transportation.gov/api/views/wkw2-rxsq",
             "issued": "2020-08-12",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-16",
             "keyword": [
                 "hpms",
                 "national roads network",
                 "roads"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/wkw2-rxsq",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2023-11-16",
+            "programCode": [
+                "021:009"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Federal Highway Administration"
             },
-            "identifier": "https://data.transportation.gov/api/views/wkw2-rxsq",
-            "description": "",
-            "title": "HPMS Pilot Project",
-            "programCode": [
-                "021:009"
-            ],
-            "license": "https://www.usa.gov/government-works",
             "theme": [
                 "Roadways and Bridges"
-            ]
+            ],
+            "title": "HPMS Pilot Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/wmrz-kh3z",
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
+                    "description": "2011 California HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/california2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 California"
+                }
+            ],
+            "identifier": "678.6",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -100341,119 +100359,116 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.6",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 California",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/wmrz-kh3z",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/california2011.zip",
-                    "description": "2011 California HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 California"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 California"
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
-            "landingPage": "https://data.transportation.gov/d/wmxb-b5a3",
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
-            "identifier": "364.9",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "R&D Database provides Vehicle Crash Test data, Biomechanics Test Data, and  Component Test Data to support NHTSA's motor vehicle and traffic safety goals.",
-            "title": "Vehicle Safety Research and Development Database - Vehicle Event Data Recorder Reports",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www-nrd.nhtsa.dot.gov/database/VSR/EventData.aspx",
+                    "mediaType": "text/html",
+                    "title": "Vehicle Event Data Recorder Reports"
+                }
+            ],
+            "identifier": "364.9",
             "isPartOf": "DOT-364",
-            "agencyProgramURL": "http://www.nhtsa.gov/Research/Databases+and+Software",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/wmxb-b5a3",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-01",
+            "phone": "202-366-4712",
             "primaryITInvestmentUII": "021-621341357",
             "programCode": [
                 "021:035"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www-nrd.nhtsa.dot.gov/database/VSR/EventData.aspx",
-                    "mediaType": "text/html",
-                    "title": "Vehicle Event Data Recorder Reports"
-                }
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
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
+            "title": "Vehicle Safety Research and Development Database - Vehicle Event Data Recorder Reports"
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
-            "landingPage": "https://data.transportation.gov/d/wnic-imer",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/05octtvt/05octtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "October 2005"
+                }
             ],
+            "identifier": "18.107",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -100463,85 +100478,44 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.107",
+            "landingPage": "https://data.transportation.gov/d/wnic-imer",
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
-            "title": "Monthly Traffic Volume Trends - October 2005",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/05octtvt/05octtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "October 2005"
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
+            "title": "Monthly Traffic Volume Trends - October 2005"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/wpek-zziu",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2018-07-09",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-09",
-            "keyword": [
-                "aberdeen",
-                "automated lane change and merge",
-                "closed track testing",
-                "connected equipment",
-                "cooperative automated driving system (cads)",
-                "cooperative automated research mobility applications (carma) platform",
-                "eco approach and departure at signalized intersections",
-                "integrated highway prototype",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "maryland",
-                "speed harmonization",
-                "vehicle platooning"
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
-            "identifier": "https://data.transportation.gov/api/views/wpek-zziu",
+            "dataQuality": true,
             "description": "The data represent the performance of a proof-of-concept vehicle platooning based on the Cooperative Adaptive Cruise Control (CACC) application. The Federal Highway Administration\u2019s Turner Fairbank Highway Research Center (TFHRC), in conjunction with the Volpe National Transportation Systems Center,  tested and evaluated this prototype system in 2016. Researchers in the Saxton Transportation Operations Laboratory at TFHRC designed and built the Cooperative Automated Research Mobility Applications (CARMA) platform version 1 that enables the implementation of the proof-of-concept CACC-based platooning in passenger vehicles equipped with production adaptive cruise control, and vehicle-to-vehicle communications using dedicated short-range communications (DSRC). The data characterize the state-of-the-art capability of the CACC application based on engineering tests that were performed on closed tracks by professional drivers and using prescribed test procedures. The test data are separated into sets that correspond to test date and time, and test run number. The data include performance parameters that were collected from the CACC application and data acquisition systems, including vehicle controller area network data, CARMA's MicroAutoBox, DSRC radios, and an independent measurement system. The tests were conducted at US Army\u2019s Aberdeen Test Center located at Aberdeen Proving Grounds, MD. Further documentation can be found here: https://rosap.ntl.bts.gov/view/dot/1038.",
-            "title": "Test Data of Proof-of-Concept Vehicle Platooning Based on Cooperative Adaptive Cruise Control (CACC)",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -100549,51 +100523,92 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/wpek-zziu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wpek-zziu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wpek-zziu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/wpek-zziu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wpek-zziu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wpek-zziu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/wpek-zziu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wpek-zziu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wpek-zziu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/wpek-zziu",
+            "issued": "2018-07-09",
+            "keyword": [
+                "aberdeen",
+                "automated lane change and merge",
+                "closed track testing",
+                "connected equipment",
+                "cooperative automated driving system (cads)",
+                "cooperative automated research mobility applications (carma) platform",
+                "eco approach and departure at signalized intersections",
+                "integrated highway prototype",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "maryland",
+                "speed harmonization",
+                "vehicle platooning"
+            ],
+            "landingPage": "https://data.transportation.gov/d/wpek-zziu",
+            "language": [
+                "us-en"
+            ],
             "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "irregular",
+            "modified": "2018-07-09",
+            "programCode": [
+                "021:013"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "USDOT"
+            },
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "us-en"
-            ]
+            "title": "Test Data of Proof-of-Concept Vehicle Platooning Based on Cooperative Adaptive Cruise Control (CACC)"
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
-            "landingPage": "https://data.transportation.gov/d/wpps-ara4",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/11maytvt/11maytvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "May 2011"
+                }
             ],
+            "identifier": "18.10",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -100603,82 +100618,48 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.10",
+            "landingPage": "https://data.transportation.gov/d/wpps-ara4",
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
-            "title": "Monthly Traffic Volume Trends - May 2011",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/11maytvt/11maytvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "May 2011"
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
+            "title": "Monthly Traffic Volume Trends - May 2011"
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
-            "landingPage": "https://data.transportation.gov/d/wpun-ific",
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
-            "identifier": "692.39",
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
@@ -100687,59 +100668,52 @@
                     "title": "Total Pollutants by County"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.39",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/wpun-ific",
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
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/wqch-9e2e",
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
-                "basic mobility control message (bmcm)",
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
-            "identifier": "https://data.transportation.gov/api/views/wqch-9e2e",
+            "dataQuality": true,
             "description": "Contains all Basic Mobility Control Message (BMCMs) generated during the Advanced Messaging Concept Development (AMCD) field testing program. While there is no specific standard in existence that addresses the content of a BMCM, the following format was derived to control the configuration and content of BMMs requested from the vehicle. All BMCMs are generated by the VCC Cloud server and transmitted to OBU clients through either a DSRC or cellular communications channel.",
-            "title": "Advanced Messaging Concept Development Basic Mobility Control Message",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -100747,71 +100721,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/wqch-9e2e/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wqch-9e2e/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wqch-9e2e/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/wqch-9e2e/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wqch-9e2e/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wqch-9e2e/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/wqch-9e2e/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wqch-9e2e/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wqch-9e2e/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Tyson\u2019s Corner, Fairfax County, Virginia",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/wqch-9e2e",
+            "issued": "2016-09-01",
+            "keyword": [
+                "advanced messaging concept development (amcd)",
+                "arterial",
+                "basic mobility control message (bmcm)",
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
+            "landingPage": "https://data.transportation.gov/d/wqch-9e2e",
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
+            "title": "Advanced Messaging Concept Development Basic Mobility Control Message"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/wqw2-rjgd",
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
-                "city summary",
-                "consumer airfare report",
-                "fare levels",
-                "fares",
-                "office of aviation analysis",
-                "table 2"
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
-            "identifier": "https://data.transportation.gov/api/views/wqw2-rjgd",
+            "dataQuality": true,
             "description": "Data summarized by city, includes the number of city-pair markets in the top 1,000 in either comparison period that involve each city, the number of passengers traveling to and from each city, the average fare, average fare per mile (yield), and average distance traveled.  All records are aggregated as directionless city pair markets.  All traffic traveling in both directions is added together.  https://www.transportation.gov/policy/aviation-policy/competition-data-analysis/research-reports",
-            "title": "Consumer Airfare Report: Table 2 - Top 1,000 City-Pair Markets",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -100819,55 +100796,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/wqw2-rjgd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wqw2-rjgd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wqw2-rjgd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/wqw2-rjgd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wqw2-rjgd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wqw2-rjgd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/wqw2-rjgd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wqw2-rjgd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wqw2-rjgd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/wqw2-rjgd",
+            "issued": "2017-10-31",
+            "keyword": [
+                "airfares",
+                "aviation",
+                "aviation policy",
+                "city pair",
+                "city summary",
+                "consumer airfare report",
+                "fare levels",
+                "fares",
+                "office of aviation analysis",
+                "table 2"
+            ],
+            "landingPage": "https://data.transportation.gov/d/wqw2-rjgd",
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
+            "title": "Consumer Airfare Report: Table 2 - Top 1,000 City-Pair Markets"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:17"
             ],
-            "landingPage": "https://data.transportation.gov/d/wt8s-2hbx",
-            "issued": "2024-04-25",
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
-            "identifier": "https://data.transportation.gov/api/views/wt8s-2hbx",
             "description": "Identifies the type, make, company number, license plate, license plate state, VIN, CVSA Decal, and CVSA Number. There can be multiple Inspection Units per inspection.",
-            "title": "Inspections Per Unit",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -100875,67 +100865,56 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/wt8s-2hbx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wt8s-2hbx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wt8s-2hbx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/wt8s-2hbx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wt8s-2hbx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wt8s-2hbx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/wt8s-2hbx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wt8s-2hbx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wt8s-2hbx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/wt8s-2hbx",
+            "issued": "2024-04-25",
+            "landingPage": "https://data.transportation.gov/d/wt8s-2hbx",
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
+            "title": "Inspections Per Unit"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://catalog.data.faa.gov/dataset/28-day-set-vfr-charts---aeronautical-information-services-digital-products",
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
-            "identifier": "74b18f7e-84c1-4c2b-a6ee-4ecc690526ab",
             "description": "The following files contain just the set of the Digital Visual charts that have changed during the previous 28 day cycle.",
-            "title": "28-Day Set VFR Charts - Aeronautical Information Services Digital Products",
-            "primaryITInvestmentUII": "021-129509270",
-            "programCode": [
-                "021:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -100944,29 +100923,63 @@
                     "title": "Aeronautical Information Services Digital Products"
                 }
             ],
+            "identifier": "74b18f7e-84c1-4c2b-a6ee-4ecc690526ab",
+            "issued": "2020-11-14",
+            "keyword": [
+                "georeference",
+                "geospatial",
+                "raster",
+                "vfr",
+                "visual-chart"
+            ],
+            "landingPage": "https://catalog.data.faa.gov/dataset/28-day-set-vfr-charts---aeronautical-information-services-digital-products",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2021-11-09",
+            "primaryITInvestmentUII": "021-129509270",
+            "programCode": [
+                "021:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Aviation Administration"
+            },
             "systemOfRecords": "https://www.govinfo.gov/content/pkg/FR-2016-08-15/pdf/2016-19354.pdf",
-            "license": "https://project-open-data.cio.gov/unknown-license/",
             "theme": [
                 "Aviation"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "28-Day Set VFR Charts - Aeronautical Information Services Digital Products"
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
-            "landingPage": "https://data.transportation.gov/d/wtq3-mm6i",
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
+            "identifier": "DOT-304",
+            "issued": "2011-01-18",
             "keyword": [
                 "data.gov",
                 "highway",
@@ -100977,77 +100990,47 @@
                 "stimulus",
                 "transportation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "DOT-304",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "Specific Federal Highway Administration Policy and Guidance Statements relating to the American Recovery and Reinvestment Act of 2009",
-            "title": "Federal Highway Administration American Recovery and Reinvestment Act of 2009 Policy and Guidance",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/economicrecovery/",
+            "landingPage": "https://data.transportation.gov/d/wtq3-mm6i",
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
-            "analysisUnit": "Regulations",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4308",
-            "language": [
-                "en-US"
-            ]
+            "title": "Federal Highway Administration American Recovery and Reinvestment Act of 2009 Policy and Guidance"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "agencyDataSeriesURL": "http://www.fhwa.dot.gov/highwaytrustfund/",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/wu3j-ynnc",
-            "issued": "2014-12-29",
-            "temporal": "R/2014-12-29/P1M",
-            "@type": "dcat:Dataset",
+            "categoryDesignation": "Administrative - Financial",
             "collectionInstrument": "Transportation",
-            "modified": "2024-05-08",
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
-            "identifier": "685.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": false,
             "description": "Status of the Highway Trust Fund - The actual receipts, outlays and balances, posted each month shortly after month-end as the information becomes available.",
-            "title": "Status of the Highway Trust Fund - Status of the Highway Trust Fund",
-            "isPartOf": "DOT-685",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -101056,31 +101039,66 @@
                     "title": "Status of the Highway Trust Fund"
                 }
             ],
-            "spatial": "National",
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "685.1",
+            "isPartOf": "DOT-685",
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
+            "landingPage": "https://data.transportation.gov/d/wu3j-ynnc",
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
+            "title": "Status of the Highway Trust Fund - Status of the Highway Trust Fund"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/wu5u-inqm",
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
+                    "description": "2012 South Carolina HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/southcarolina2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 South Carolina"
+                }
+            ],
+            "identifier": "678.94",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -101094,91 +101112,39 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.94",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 South Carolina",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/wu5u-inqm",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/southcarolina2012.zip",
-                    "description": "2012 South Carolina HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 South Carolina"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 South Carolina"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/wusc-iwue",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2024-04-17",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
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
-            "identifier": "https://data.transportation.gov/api/views/wusc-iwue",
             "description": "The Mobility Trends County Modeling dataset consists of the accumulation of the three performance metrics: VMT, GHG, and TMS, alongside each of the trend indicators: GDP, Population, Lane Miles, Unemployment Rate, Charging Stations, Telework, Unlinked Passenger Trips, E-commerce, Population Density, and on-demand service revenue. The goal of Mobility Trends and Future Demand research project is to enhance FHWA\u2019s empirical understanding of the impact of trends on travel behavior and transportation demand, and ultimately system performance and the user experience. At the core of this research project is the identification and analysis of trends to support a variety of modeling, forecasting, and \u2018what if\u2019 projections to support policy and decision making.",
-            "title": "Mobility Trends County Modeling Dataset",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -101186,61 +101152,79 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/wusc-iwue/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wusc-iwue/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wusc-iwue/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/wusc-iwue/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wusc-iwue/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wusc-iwue/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/wusc-iwue/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wusc-iwue/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wusc-iwue/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/wusc-iwue",
+            "issued": "2024-04-17",
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
+            "landingPage": "https://data.transportation.gov/d/wusc-iwue",
             "license": "https://www.usa.gov/government-works",
+            "modified": "2024-08-08",
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
+            "title": "Mobility Trends County Modeling Dataset"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/wwdp-t4re",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "021:36"
             ],
-            "issued": "2024-12-16",
-            "@type": "dcat:Dataset",
-            "temporal": "R/2002-01-01/P1M",
-            "modified": "2025-01-23",
-            "keyword": [
-                "service",
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
-            "identifier": "https://data.transportation.gov/api/views/wwdp-t4re",
+            "dataQuality": true,
             "description": "This represents the Service data reported to the NTD by transit agencies to the NTD.\n\nIn versions of the data tables from before 2014, you can find data on service in the file called \"Transit Operating Statistics: Service Supplied and Consumed.\"\n\nIf you have any other questions about this table, please contact the NTD Help Desk at NTDHelp@dot.gov.",
-            "title": "2022 - 2023 NTD Annual Data - Service (by Mode and Time Period)",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -101248,77 +101232,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/wwdp-t4re/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wwdp-t4re/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wwdp-t4re/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/wwdp-t4re/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wwdp-t4re/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wwdp-t4re/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/wwdp-t4re/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wwdp-t4re/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wwdp-t4re/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "United States",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/wwdp-t4re",
+            "issued": "2024-12-16",
+            "keyword": [
+                "service",
+                "transit"
+            ],
+            "landingPage": "https://data.transportation.gov/d/wwdp-t4re",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2025-01-23",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Transit Administration"
+            },
+            "spatial": "United States",
+            "temporal": "R/2002-01-01/P1M",
             "theme": [
                 "Public Transit"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2022 - 2023 NTD Annual Data - Service (by Mode and Time Period)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/wxyj-6dfq",
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
-                "basic mobility message (bmm)",
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
-            "identifier": "https://data.transportation.gov/api/views/wxyj-6dfq",
+            "dataQuality": true,
             "description": "Contains all Basic Mobility Messages (BMMs) collected during the Advanced Messaging Concept Development (AMCD) field testing program. While there is no specific standard in existence that addresses the content of a BMM, the descriptive definitions of the variables were derived from the J2735 standard where applicable. All BMMs are generated by OBUs and ultimately received by the VCC Cloud server.",
-            "title": "Advanced Messaging Concept Development: Basic Mobility Message",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -101326,89 +101300,95 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/wxyj-6dfq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wxyj-6dfq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wxyj-6dfq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/wxyj-6dfq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wxyj-6dfq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wxyj-6dfq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/wxyj-6dfq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wxyj-6dfq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wxyj-6dfq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Tyson\u2019s Corner, Fairfax County, Virginia",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/wxyj-6dfq",
+            "issued": "2016-09-01",
+            "keyword": [
+                "advanced messaging concept development (amcd)",
+                "arterial",
+                "basic mobility message (bmm)",
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
+            "landingPage": "https://data.transportation.gov/d/wxyj-6dfq",
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
+            "title": "Advanced Messaging Concept Development: Basic Mobility Message"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/wyez-ckqz",
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
             "identifier": "https://data.transportation.gov/api/views/wyez-ckqz",
+            "issued": "2024-04-05",
+            "landingPage": "https://data.transportation.gov/d/wyez-ckqz",
+            "modified": "2024-04-05",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Chapter 5. Safety, Energy, and Environmental Impacts"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Access restricted under the Privacy Act of 1974; see Privacy Impact Assessment at http://www.dot.gov/individuals/privacy/pia-parking-and-transit-benefit-system-ptbs",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:04"
             ],
-            "landingPage": "https://data.transportation.gov/d/wz63-adj9",
-            "issued": "2014-10-24",
-            "temporal": "R/2013-01-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "benefit",
-                "contractor",
-                "employee",
-                "parking",
-                "transaction"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOT Socrata",
                 "hasEmail": "mailto:Socrata@dot.gov"
             },
-            "identifier": "589.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
+            "dataQuality": false,
             "description": "This data set contains information about any DOT employees and contractors participating in the parking permit program at DOT Headquarters, details about their vehicles, and transaction histories.",
-            "title": "DOT Headquarters Parking data -",
-            "primaryITInvestmentUII": "021-132481137",
-            "programCode": [
-                "021:058"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -101416,58 +101396,51 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "theme": [
-                "Transportation"
+            "identifier": "589.0",
+            "issued": "2014-10-24",
+            "keyword": [
+                "benefit",
+                "contractor",
+                "employee",
+                "parking",
+                "transaction"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/wz63-adj9",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-7022"
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-11-14",
+            "phone": "202-366-7022",
+            "primaryITInvestmentUII": "021-132481137",
+            "programCode": [
+                "021:058"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Secretary of Transportation"
+            },
+            "rights": "Access restricted under the Privacy Act of 1974; see Privacy Impact Assessment at http://www.dot.gov/individuals/privacy/pia-parking-and-transit-benefit-system-ptbs",
+            "temporal": "R/2013-01-01/P1Y",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "DOT Headquarters Parking data -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/wz7m-693m",
+            "accrualPeriodicity": "R/PT0.1S",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2016-02-17",
-            "@type": "dcat:Dataset",
-            "temporal": "2015-01-12/2015-01-16",
-            "modified": "2016-02-17",
-            "keyword": [
-                "arterial",
-                "basic safety message (bsm)",
-                "connected vehicle message",
-                "dedicated short range communication (dsrc)",
-                "freeway",
-                "i-5",
-                "intelligent network flow optimization (inflo)",
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "roadside equipment (rse)",
-                "seattle",
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
-            "identifier": "https://data.transportation.gov/api/views/wz7m-693m",
+            "dataQuality": true,
             "description": "Data is from the small-scale demonstration of the Intelligent Network Flow Optimization (INFLO) Prototype System and applications in Seattle, Washington. Connected vehicle systems were deployed in 21 vehicles in a scripted driving scenario circuiting this I-5 corridor northbound and southbound during morning rush hour. Basic Safety Messages (BSM) sent by connected vehicles (CVs) through either the cellular network or Dedicated Short Range Communication (DSRC) when the vehicle is in the range of Roadside Units (RSU). These messages were received by the traffic management center (TMC).",
-            "title": "Intelligent Network Flow Optimization Prototype Basic Safety Messages",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -101475,69 +101448,76 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/wz7m-693m/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wz7m-693m/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wz7m-693m/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/wz7m-693m/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wz7m-693m/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wz7m-693m/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/wz7m-693m/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wz7m-693m/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wz7m-693m/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Seattle, Washington",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/wz7m-693m",
+            "issued": "2016-02-17",
+            "keyword": [
+                "arterial",
+                "basic safety message (bsm)",
+                "connected vehicle message",
+                "dedicated short range communication (dsrc)",
+                "freeway",
+                "i-5",
+                "intelligent network flow optimization (inflo)",
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "roadside equipment (rse)",
+                "seattle",
+                "washington",
+                "washington state department of transportation (wsdot)"
+            ],
+            "landingPage": "https://data.transportation.gov/d/wz7m-693m",
+            "language": [
+                "en-US"
+            ],
             "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "R/PT0.1S",
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
+            "title": "Intelligent Network Flow Optimization Prototype Basic Safety Messages"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://us-datacloud.one.network/wzdx-north-carolina.json?app_key=db73336d-85c4-7d0b-258b71e36573",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2022-01-15",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-07",
-            "keyword": [
-                "intelligent transportation systems (its)",
-                "its joint program office (jpo)",
-                "north carolina",
-                "north carolina department of transportation (ncdot)",
-                "smart work zones manager (swzm)",
-                "smart work zones (swz)",
-                "work zone data exchange (wzdx)",
-                "work zones"
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
-            "identifier": "https://data.transportation.gov/api/views/wzfs-4rgw",
             "description": "This dataset provides information on work zones in the state of North Carolina in a tabular format and is updated daily based on the live NCDOT Work Zone Data Exchange (WZDx) Feed.\n\nA continuously updating archive of the NCDOT WZDx feed data can be found at the <a href=\"http://usdot-its-workzone-raw-publicdata.s3.amazonaws.com/index.html\" target=\"_blank\" rel=\"noopener noreferrer\">ITS WorkZone Raw Data Sandbox</a> and the <a href=\"https://usdot-its-workzone-publicdata.s3.amazonaws.com/index.html\" target=\"_blank\" rel=\"noopener noreferrer\">ITS Work Zone Semi-Processed Data Sandbox</a>. The live feed is currently compliant with the WZDx Specification v3.1.",
-            "title": "North Carolina Department of Transportation (NCDOT) Work Zone Data Exchange (WZDx)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -101545,75 +101525,75 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/wzfs-4rgw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wzfs-4rgw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wzfs-4rgw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/wzfs-4rgw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wzfs-4rgw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wzfs-4rgw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/wzfs-4rgw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/wzfs-4rgw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/wzfs-4rgw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/wzfs-4rgw",
+            "issued": "2022-01-15",
+            "keyword": [
+                "intelligent transportation systems (its)",
+                "its joint program office (jpo)",
+                "north carolina",
+                "north carolina department of transportation (ncdot)",
+                "smart work zones manager (swzm)",
+                "smart work zones (swz)",
+                "work zone data exchange (wzdx)",
+                "work zones"
+            ],
+            "landingPage": "https://us-datacloud.one.network/wzdx-north-carolina.json?app_key=db73336d-85c4-7d0b-258b71e36573",
+            "language": [
+                "en-US"
+            ],
             "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
+            "modified": "2024-11-07",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
             "theme": [
                 "Roadways and Bridges"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "North Carolina Department of Transportation (NCDOT) Work Zone Data Exchange (WZDx)"
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
-            "landingPage": "https://data.transportation.gov/d/wzry-h98v",
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
-            "identifier": "224.1",
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
@@ -101622,59 +101602,59 @@
                     "title": "Crossing Inventory - Public Site"
                 }
             ],
-            "spatial": "Latitude/Longitude",
-            "describedBy": "http://safetydata.fra.dot.gov/OfficeofSafety/Documents/GCIS%20Electronic%20Submissions%20Instructions.pdf",
-            "dataQuality": true,
+            "identifier": "224.1",
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
+            "landingPage": "https://data.transportation.gov/d/wzry-h98v",
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
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "The data system is not available to the general public because it contains data related to recipients of Federal highway funding and limited access is integral to system controls.",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "https://collaboration.fhwa.dot.gov/dot/fhwa/default.aspx",
+            "agencyProgramURL": "https://collaboration.fhwa.dot.gov/default.aspx",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/x2kp-fzkp",
-            "issued": "2014-12-29",
-            "temporal": "2014-12-29/2014-12-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-08",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Transportation",
-            "references": [
-                "https://collaboration.fhwa.dot.gov/support/default.aspx"
-            ],
-            "keyword": [
-                "collaboration",
-                "community exchange",
-                "discussion board"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "714.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "This is an FHWA initiative to promote knowledge sharing across the organization; it includes a FHWA external Microsoft SharePoint 2010 services, internal Microsoft SharePoint 2010 services, and Adobe Connect Professional Web conferencing services for knowledge sharing communities. There are two SharePoint environments that are not connected. The two environments are totally separate.The internal environment is non-Public and accessible to DOT only. The internal environment is managed by OST. It hosts 184 top level SharePoint sites serving the FHWA. The external environment is Public with some restricted SharePoint sites. External environment is managed by FHWA.The external SharePoint environment hosts 16 top level SharePoint sites serving the FHWA, state and local DOTs, and the surface transportation community.",
-            "title": "Knowledge Management -",
-            "agencyProgramURL": "https://collaboration.fhwa.dot.gov/default.aspx",
-            "primaryITInvestmentUII": "021-394701131",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -101682,32 +101662,64 @@
                     "mediaType": "text/html"
                 }
             ],
-            "spatial": "National",
-            "dataQuality": true,
+            "identifier": "714.0",
+            "issued": "2014-12-29",
+            "keyword": [
+                "collaboration",
+                "community exchange",
+                "discussion board"
+            ],
+            "landingPage": "https://data.transportation.gov/d/x2kp-fzkp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://project-open-data.cio.gov/unknown-license/",
-            "agencyDataSeriesURL": "https://collaboration.fhwa.dot.gov/dot/fhwa/default.aspx",
+            "modified": "2024-05-08",
+            "phone": "785-273-2659",
+            "primaryITInvestmentUII": "021-394701131",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Highway Administration"
+            },
+            "references": [
+                "https://collaboration.fhwa.dot.gov/support/default.aspx"
+            ],
+            "rights": "The data system is not available to the general public because it contains data related to recipients of Federal highway funding and limited access is integral to system controls.",
+            "spatial": "National",
+            "temporal": "2014-12-29/2014-12-29",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "irregular",
-            "categoryDesignation": "Administrative",
-            "phone": "785-273-2659",
-            "language": [
-                "en-US"
-            ]
+            "title": "Knowledge Management -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "supports internal processes",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/x3dv-k7vf",
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
+            "description": "Forms HS-7, declaration on motor vehicles and motor vehicle equipment subject to Federal Motor Vehicle Safety Standards. Customs reports of declarations and inspections. Records relating to refusal of entry or penalties, and in some instances law enforcement and court records in alleged fraud cases.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.transportation.gov/mission/data-inventory-not-available",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "420.0",
+            "issued": "2018-12-18",
             "keyword": [
                 "cbp",
                 "compliance",
@@ -101723,71 +101735,77 @@
                 "penalties",
                 "records"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "420.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Forms HS-7, declaration on motor vehicles and motor vehicle equipment subject to Federal Motor Vehicle Safety Standards. Customs reports of declarations and inspections. Records relating to refusal of entry or penalties, and in some instances law enforcement and court records in alleged fraud cases.",
-            "title": "Motor Vehicle Importation Information (MVII) -",
+            "landingPage": "https://data.transportation.gov/d/x3dv-k7vf",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-01",
+            "phone": "202-366-5308",
             "primaryITInvestmentUII": "021-158063122",
             "programCode": [
                 "021:031"
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
+            "rights": "supports internal processes",
+            "temporal": "R/2013/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
-            "language": [
-                "en-US"
-            ],
-            "phone": "202-366-5308"
+            "title": "Motor Vehicle Importation Information (MVII) -"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/x3fb-aeda",
-            "issued": "2021-04-07",
             "@type": "dcat:Dataset",
-            "modified": "2024-07-30",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Chambers",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "",
             "identifier": "https://data.transportation.gov/api/views/x3fb-aeda",
+            "issued": "2021-04-07",
+            "landingPage": "https://data.transportation.gov/d/x3fb-aeda",
+            "modified": "2024-07-30",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "",
             "title": "Container / TEU"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/x3xy-vkpe",
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
+                    "description": "2011 Arkansas HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/arkansas2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Arkansas"
+                }
+            ],
+            "identifier": "678.5",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -101801,108 +101819,75 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.5",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Arkansas",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/x3xy-vkpe",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/arkansas2011.zip",
-                    "description": "2011 Arkansas HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Arkansas"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Arkansas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/x5f7-q5tn",
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
-            "identifier": "https://data.transportation.gov/api/views/x5f7-q5tn",
             "description": "Regular gasoline price is the average retail price for regular grade formulations. The U.S. Energy Information Administration releases weekly gasoline and diesel price estimates.",
-            "title": "Fuel Prices - Regular Gasoline",
+            "identifier": "https://data.transportation.gov/api/views/x5f7-q5tn",
+            "issued": "2025-01-03",
+            "keyword": [
+                "monthly transportation statistics"
+            ],
+            "landingPage": "https://data.transportation.gov/d/x5f7-q5tn",
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
+            "title": "Fuel Prices - Regular Gasoline"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/x5vg-yqea",
             "bureauCode": [
                 "021:27"
             ],
-            "issued": "2020-08-27",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
-            "keyword": [
-                "railroad"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
-            "identifier": "https://data.transportation.gov/api/views/x5vg-yqea",
+            "dataQuality": true,
             "description": "All Railroads covered by Part 225 Accident/Injury reporting are required to provide monthly summary statistics via the form F6180.55.",
-            "title": "Monthly Railroad Operational Summaries",
-            "programCode": [
-                "021:036"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -101910,60 +101895,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/x5vg-yqea/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/x5vg-yqea/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/x5vg-yqea/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/x5vg-yqea/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/x5vg-yqea/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/x5vg-yqea/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/x5vg-yqea/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/x5vg-yqea/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/x5vg-yqea/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/x5vg-yqea",
+            "issued": "2020-08-27",
+            "keyword": [
+                "railroad"
+            ],
+            "landingPage": "https://data.transportation.gov/d/x5vg-yqea",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-08-08",
+            "programCode": [
+                "021:036"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Railroad Operational Summaries"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/x6rh-cpwu",
-            "issued": "2024-01-11",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-28",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "TBD",
                 "hasEmail": "mailto:sean.jahanmir@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/x6rh-cpwu",
             "description": "",
-            "title": "Monthly TEU Capacity of Container Ships Calling at U.S. Ports January 2020 to September 2023",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -101971,43 +101958,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/x6rh-cpwu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/x6rh-cpwu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/x6rh-cpwu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/x6rh-cpwu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/x6rh-cpwu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/x6rh-cpwu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/x6rh-cpwu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/x6rh-cpwu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/x6rh-cpwu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+            "identifier": "https://data.transportation.gov/api/views/x6rh-cpwu",
+            "issued": "2024-01-11",
+            "landingPage": "https://data.transportation.gov/d/x6rh-cpwu",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2025-01-28",
+            "programCode": [
+                "021:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "title": "Monthly TEU Capacity of Container Ships Calling at U.S. Ports January 2020 to September 2023"
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
-            "landingPage": "https://data.transportation.gov/d/x734-i34z",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/04novtvt/04novtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "November 2004"
+                }
             ],
+            "identifier": "18.118",
+            "isPartOf": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -102017,57 +102032,59 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "18.118",
+            "landingPage": "https://data.transportation.gov/d/x734-i34z",
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
-            "title": "Monthly Traffic Volume Trends - November 2004",
-            "isPartOf": "DOT-18",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/ohim/tvtw/04novtvt/04novtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "November 2004"
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
+            "title": "Monthly Traffic Volume Trends - November 2004"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/x76a-tbx7",
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
+                    "title": "2012 NHS"
+                }
+            ],
+            "identifier": "678.53",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -102081,59 +102098,57 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.53",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 NHS",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/x76a-tbx7",
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
-                    "title": "2012 NHS"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 NHS"
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
-            "landingPage": "https://data.transportation.gov/d/x7wj-xh7c",
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
+                    "downloadURL": "http://www.nhtsa.gov/staticfiles/nti/MVOSS/MVOSS2007_SAS_VersionB_Data.sas7bdat",
+                    "mediaType": "text/plain",
+                    "title": "Child Restraint Use (v2) (SAS)"
+                }
             ],
+            "identifier": "408.4",
+            "isPartOf": "DOT-408",
+            "issued": "2008-08-31",
             "keyword": [
                 "air bag",
                 "child safety",
@@ -102144,79 +102159,46 @@
                 "protection",
                 "seat belt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "408.4",
+            "landingPage": "https://data.transportation.gov/d/x7wj-xh7c",
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
-            "title": "Motor Vehicle Occupant Safety Survey 2007 (MVOSS) - Child Restraint Use (v2) (SAS)",
-            "isPartOf": "DOT-408",
-            "agencyProgramURL": "http://www.nhtsa.gov/Driving+Safety/Research+&+Evaluation/National+Telephone+Surveys",
-            "programCode": [
-                "021:032"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.nhtsa.gov/staticfiles/nti/MVOSS/MVOSS2007_SAS_VersionB_Data.sas7bdat",
-                    "mediaType": "text/plain",
-                    "title": "Child Restraint Use (v2) (SAS)"
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
+            "title": "Motor Vehicle Occupant Safety Survey 2007 (MVOSS) - Child Restraint Use (v2) (SAS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "Survey has not started",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyProgramURL": "http://www.nhtsa.gov/testing/young",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/x8hb-hwt5",
-            "issued": "2018-12-17",
-            "temporal": "R/2016/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "behavior",
-                "drivers",
-                "survey",
-                "young"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "382.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
             "description": "The survey will explore the frequency and context of unsafe driver behaviors among this age group, types of risky situations that people of young driver age experience as vehicle passengers, parental influence on young drivers, driver training and education, and young driver attitudes and perceptions concerning selected traffic safety issues.",
-            "title": "Young Driver Survey -",
-            "agencyProgramURL": "http://www.nhtsa.gov/testing/young",
-            "programCode": [
-                "021:032"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -102224,54 +102206,54 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "382.0",
+            "issued": "2018-12-17",
+            "keyword": [
+                "behavior",
+                "drivers",
+                "survey",
+                "young"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/x8hb-hwt5",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-6401"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-01",
+            "phone": "202-366-6401",
+            "programCode": [
+                "021:032"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "rights": "Survey has not started",
+            "temporal": "R/2016/P1Y",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "Young Driver Survey -"
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
-            "landingPage": "https://data.transportation.gov/d/x8z7-jjwa",
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
-            "identifier": "DOT-305",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Motor Carrier Safety Administration"
-            },
+            "dataQuality": true,
             "description": "A list of Significant Guidance documents, which include guidance document disseminated to regulated entities or the general public that may reasonably be anticipated to lead to an annual effect on the economy of $100 million or more or adversely affect in a material way the economy, a sector of the economy, productivity, competition, jobs, the environment, public health or safety, or State, local, or tribal governments or communities; create a serious inconsistency or otherwise interfere with an action taken or planned by another agency; materially alter the budgetary impact of entitlements, grants, user fees, or loan programs or the rights and obligations of recipients thereof; or raise novel legal or policy issues arising out of legal mandates, the President's priorities, or the principles set forth in Executive Order 12866, as further amended.",
-            "title": "Significant Guidance Issued by the Federal Motor Carrier Safety Administration",
-            "agencyProgramURL": "http://www.fmcsa.dot.gov/rules-regulations/administration/fmcsr/fmcsrguide.aspx%3Fsection_type=G",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -102279,61 +102261,58 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "DOT-305",
+            "issued": "2011-01-18",
+            "keyword": [
+                "data.gov",
+                "law",
+                "significant guidance",
+                "transportation"
+            ],
+            "landingPage": "https://data.transportation.gov/d/x8z7-jjwa",
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
+            "title": "Significant Guidance Issued by the Federal Motor Carrier Safety Administration"
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
-            "landingPage": "https://data.transportation.gov/d/x9he-c6mu",
-            "issued": "2002-12-16",
-            "temporal": "R/1965-01-01/P1D",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
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
-            "identifier": "DOT-84",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "The National Highway Traffic Safety Administration (NHTSA) has the right to investigate reports of defective products. Information about defective products can come from manufacturers, consumers or law enforcement agencies. NHTSA stores defect investigation information in a database. It uses this information to generate monthly defect reports. It also makes this information available to consumers through the NHTSA web site. You can search for defect investigation information for the following product categories: -\tVehicles -\tEquipment -\tChild Restraints -\tTires",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Investigations",
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
@@ -102342,33 +102321,65 @@
                     "title": "Investigations Flat File"
                 }
             ],
-            "describedBy": "http://www-odi.nhtsa.dot.gov/downloads/folders/Investigations/INV.txt",
-            "dataQuality": true,
+            "identifier": "DOT-84",
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
+            "landingPage": "https://data.transportation.gov/d/x9he-c6mu",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/downloads/folders/Investigations/FLAT_INV.zip",
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
+                "http://www-odi.nhtsa.dot.gov/downloads/folders/Investigations/INV.txt"
+            ],
+            "temporal": "R/1965-01-01/P1D",
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
+            "title": "NHTSA's Office of Defects Investigation (ODI) - Investigations"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.21949/1503766",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2014-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2016-12-21",
-            "references": [
-                "https://rosap.ntl.bts.gov/view/dot/3609"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Transportation Library Data Curator",
+                "hasEmail": "mailto:ntldatacurator@dot.gov"
+            },
+            "dataQuality": true,
+            "description": "\"SHRP 2 initiated the L38 project to pilot test products from five of the program\u2019s completed projects. The products support reliability estimation and use based on data analyses, analytical techniques, and decision-making framework. The L38 project has two main objectives: (1) to assist agencies in using travel time reliability as a measure in their business practices and (2) to receive feedback from the project research teams on the applicability and usefulness of the products tested, along with their suggested possible refinements. SHRP 2 selected four teams from California, Minnesota, Florida, and Washington. Project L38C tested elements from Projects L02, L05, L07, and L08. Project L02 identified methods to collect, archive, and integrate required data for reliability estimation and methods for analyzing and visualizing the causes of unreliability based on the collected data. Projects L07 and L08 produced analytical techniques and tools for estimating reliability based on developed models and allowing the estimation of reliability and the impacts on reliability of alternative mitigating strategies. Project L05 provided guidance regarding how to use reliability assessments to support the business processes of transportation agencies. The datasets in this zip file, which is 7.83 MB in size, support of SHRP 2 reliability project L38C, \"Pilot testing of SHRP 2 reliability data and analytical products: Florida.\" The accompanying report can be accessed at the following URL: https://rosap.ntl.bts.gov/view/dot/3609 There are 12 datasets in this zip file, including 2 Microsoft Excel worksheets (XLSX) and 10 Comma Separated Values (CSV) files. The Microsoft Excel worksheets can be opened using the 2010 and 2016 versions of Microsoft Word, the CSV files can be opened using most text editors.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "\"SHRP 2 initiated the L38 project to pilot test products from five of the program\u2019s completed projects. The products support reliability estimation and use based on data analyses, analytical techniques, and decision-making framework. The L38 project has two main objectives: (1) to assist agencies in using travel time reliability as a measure in their business practices and (2) to receive feedback from the project research teams on the applicability and usefulness of the products tested, along with their suggested possible refinements. SHRP 2 selected four teams from California, Minnesota, Florida, and Washington. Project L38C tested elements from Projects L02, L05, L07, and L08. Project L02 identified methods to collect, archive, and integrate required data for reliability estimation and methods for analyzing and visualizing the causes of unreliability based on the collected data. Projects L07 and L08 produced analytical techniques and tools for estimating reliability based on developed models and allowing the estimation of reliability and the impacts on reliability of alternative mitigating strategies. Project L05 provided guidance regarding how to use reliability assessments to support the business processes of transportation agencies. The datasets in this zip file, which is 7.83 MB in size, support of SHRP 2 reliability project L38C, \"Pilot testing of SHRP 2 reliability data and analytical products: Florida.\" The accompanying report can be accessed at the following URL: https://rosap.ntl.bts.gov/view/dot/3609 There are 12 datasets in this zip file, including 2 Microsoft Excel worksheets (XLSX) and 10 Comma Separated Values (CSV) files. The Microsoft Excel worksheets can be opened using the 2010 and 2016 versions of Microsoft Word, the CSV files can be opened using most text editors.",
+                    "downloadURL": "https://doi.org/10.21949/1503766",
+                    "mediaType": "application/zip",
+                    "title": "Pilot Testing of SHRP 2 Reliability Data and Analytical Products: Florida [supporting datasets]"
+                }
             ],
+            "identifier": "https://data.transportation.gov/api/views/x9hu-qxyc",
+            "issued": "2014-01-01",
             "keyword": [
                 "business practices",
                 "data analysis",
@@ -102382,48 +102393,55 @@
                 "travel time",
                 "travel time reliability"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "National Transportation Library Data Curator",
-                "hasEmail": "mailto:ntldatacurator@dot.gov"
-            },
+            "landingPage": "https://doi.org/10.21949/1503766",
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
-            "identifier": "https://data.transportation.gov/api/views/x9hu-qxyc",
-            "description": "\"SHRP 2 initiated the L38 project to pilot test products from five of the program\u2019s completed projects. The products support reliability estimation and use based on data analyses, analytical techniques, and decision-making framework. The L38 project has two main objectives: (1) to assist agencies in using travel time reliability as a measure in their business practices and (2) to receive feedback from the project research teams on the applicability and usefulness of the products tested, along with their suggested possible refinements. SHRP 2 selected four teams from California, Minnesota, Florida, and Washington. Project L38C tested elements from Projects L02, L05, L07, and L08. Project L02 identified methods to collect, archive, and integrate required data for reliability estimation and methods for analyzing and visualizing the causes of unreliability based on the collected data. Projects L07 and L08 produced analytical techniques and tools for estimating reliability based on developed models and allowing the estimation of reliability and the impacts on reliability of alternative mitigating strategies. Project L05 provided guidance regarding how to use reliability assessments to support the business processes of transportation agencies. The datasets in this zip file, which is 7.83 MB in size, support of SHRP 2 reliability project L38C, \"Pilot testing of SHRP 2 reliability data and analytical products: Florida.\" The accompanying report can be accessed at the following URL: https://rosap.ntl.bts.gov/view/dot/3609 There are 12 datasets in this zip file, including 2 Microsoft Excel worksheets (XLSX) and 10 Comma Separated Values (CSV) files. The Microsoft Excel worksheets can be opened using the 2010 and 2016 versions of Microsoft Word, the CSV files can be opened using most text editors.",
-            "title": "Pilot Testing of SHRP 2 Reliability Data and Analytical Products: Florida [supporting datasets]",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/zip",
-                    "downloadURL": "https://doi.org/10.21949/1503766",
-                    "description": "\"SHRP 2 initiated the L38 project to pilot test products from five of the program\u2019s completed projects. The products support reliability estimation and use based on data analyses, analytical techniques, and decision-making framework. The L38 project has two main objectives: (1) to assist agencies in using travel time reliability as a measure in their business practices and (2) to receive feedback from the project research teams on the applicability and usefulness of the products tested, along with their suggested possible refinements. SHRP 2 selected four teams from California, Minnesota, Florida, and Washington. Project L38C tested elements from Projects L02, L05, L07, and L08. Project L02 identified methods to collect, archive, and integrate required data for reliability estimation and methods for analyzing and visualizing the causes of unreliability based on the collected data. Projects L07 and L08 produced analytical techniques and tools for estimating reliability based on developed models and allowing the estimation of reliability and the impacts on reliability of alternative mitigating strategies. Project L05 provided guidance regarding how to use reliability assessments to support the business processes of transportation agencies. The datasets in this zip file, which is 7.83 MB in size, support of SHRP 2 reliability project L38C, \"Pilot testing of SHRP 2 reliability data and analytical products: Florida.\" The accompanying report can be accessed at the following URL: https://rosap.ntl.bts.gov/view/dot/3609 There are 12 datasets in this zip file, including 2 Microsoft Excel worksheets (XLSX) and 10 Comma Separated Values (CSV) files. The Microsoft Excel worksheets can be opened using the 2010 and 2016 versions of Microsoft Word, the CSV files can be opened using most text editors.",
-                    "@type": "dcat:Distribution",
-                    "title": "Pilot Testing of SHRP 2 Reliability Data and Analytical Products: Florida [supporting datasets]"
-                }
+            "references": [
+                "https://rosap.ntl.bts.gov/view/dot/3609"
             ],
             "spatial": "United States, Florida, Miami (Florida)",
-            "dataQuality": true,
-            "license": "https://www.usa.gov/government-works",
-            "language": [
-                "en-US"
-            ]
+            "title": "Pilot Testing of SHRP 2 Reliability Data and Analytical Products: Florida [supporting datasets]"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/xafm-hn6h",
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
+                    "description": "2013 South Dakota HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/southdakota2013.zip",
+                    "mediaType": "application/zip",
+                    "title": "2013 South Dakota"
+                }
+            ],
+            "identifier": "678.145",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -102437,96 +102455,92 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.145",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2013 South Dakota",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/xafm-hn6h",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/southdakota2013.zip",
-                    "description": "2013 South Dakota HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2013 South Dakota"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2013 South Dakota"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/xaj5-jhwd",
             "bureauCode": [
                 "021:27"
             ],
-            "issued": "2024-09-25",
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
-            "identifier": "https://data.transportation.gov/api/views/xaj5-jhwd",
+            "dataQuality": true,
             "description": "lindsay.petersdawson@dot.gov",
-            "title": "Trespasser & Suicide Reports - Landing Page",
+            "identifier": "https://data.transportation.gov/api/views/xaj5-jhwd",
+            "issued": "2024-09-25",
+            "keyword": [
+                "trespasser. suicide"
+            ],
+            "landingPage": "https://data.transportation.gov/d/xaj5-jhwd",
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
+            "title": "Trespasser & Suicide Reports - Landing Page"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyProgramURL": "http://www.nhtsa.gov/fuel-economy",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/xap9-jrxg",
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
+            "identifier": "1862.8",
+            "isPartOf": "DOT-1862",
+            "issued": "2015-12-16",
             "keyword": [
                 "amfa",
                 "civil penalties",
@@ -102543,58 +102557,61 @@
                 "report",
                 "shortfall"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "1862.8",
+            "landingPage": "https://data.transportation.gov/d/xap9-jrxg",
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
+            "accrualPeriodicity": "R/P1D",
+            "agencyDataSeriesURL": "http://www-odi.nhtsa.dot.gov/downloads/folders/Recalls/FLAT_RCL.zip",
+            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
+            "analysisUnit": "Vehicles , Tires, Child Safety Seats, Equipment",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/xb2y-suuz",
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
+            "identifier": "83.15",
+            "isPartOf": "DOT-83",
+            "issued": "2002-12-16",
             "keyword": [
                 "air bag",
                 "air bags",
@@ -102621,81 +102638,43 @@
                 "vin",
                 "vin search"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "83.15",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "Manufacturers who determine that a product or piece of original equipment either has a safety defect or is not in compliance with Federal safety standards are required to notify the National Highway Traffic Safety Administration (NHTSA) within 5 business days. NHTSA requires that manufacturers file a Defect and Noncompliance report as well as quarterly recall status reports, in compliance with Federal Regulation 49 (the National Traffic and Motor Safety Act) Part 573, which identifies the requirements for safety recalls. This information is stored in the NHTSA database. Use this data to search for recall information related to:-\tSpecific NHTSA campaigns -\tProduct types Access to public searches of NHTSA recall databases for tires, vehicles, car seats and equipment.",
-            "title": "NHTSA's Office of Defects Investigation (ODI) - Recalls - Recalls - Equipment",
-            "isPartOf": "DOT-83",
-            "agencyProgramURL": "http://www-odi.nhtsa.dot.gov/downloads/index.cfm",
-            "describedByType": "text/plain",
+            "landingPage": "https://data.transportation.gov/d/xb2y-suuz",
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
-            "landingPage": "https://data.transportation.gov/d/xdkm-ken4",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2023-07-28",
-            "@type": "dcat:Dataset",
-            "temporal": "2022-04-27/2022-09-23",
-            "modified": "2024-07-18",
-            "keyword": [
-                "bicycle",
-                "e-bike",
-                "gps",
-                "public lands",
-                "trail"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jonah Chiarenza",
                 "hasEmail": "mailto:Volpe_Dataset_POCs@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "US Department of Transportation"
-            },
-            "identifier": "https://data.transportation.gov/api/views/xdkm-ken4",
             "description": "GPS pings collected by study participants who rode conventional and e-bikes at Minute Man National Historic Park between April and September 2022.",
-            "title": "E-Bike Field Study Data",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -102703,47 +102682,83 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xdkm-ken4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xdkm-ken4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xdkm-ken4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/xdkm-ken4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xdkm-ken4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xdkm-ken4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xdkm-ken4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xdkm-ken4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xdkm-ken4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "-71.3244,42.4473,42.4615,-71.2562",
+            "identifier": "https://data.transportation.gov/api/views/xdkm-ken4",
+            "issued": "2023-07-28",
+            "keyword": [
+                "bicycle",
+                "e-bike",
+                "gps",
+                "public lands",
+                "trail"
+            ],
+            "landingPage": "https://data.transportation.gov/d/xdkm-ken4",
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-07-18",
+            "programCode": [
+                "021:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "US Department of Transportation"
+            },
+            "spatial": "-71.3244,42.4473,42.4615,-71.2562",
+            "temporal": "2022-04-27/2022-09-23",
             "theme": [
                 "Bicycles and Pedestrians"
-            ]
+            ],
+            "title": "E-Bike Field Study Data"
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
-            "landingPage": "https://data.transportation.gov/d/xdpv-m434",
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
+            "identifier": "DOT-199",
+            "issued": "2010-09-29",
             "keyword": [
                 "acts of god",
                 "collisions",
@@ -102754,60 +102769,59 @@
                 "suicide",
                 "trespasser"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Office of Railroad Safety",
-                "hasEmail": "mailto:List-FRA-SAFETEAM@dot.gov"
-            },
-            "identifier": "DOT-199",
+            "landingPage": "https://data.transportation.gov/d/xdpv-m434",
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
-            "title": "Rail Equipment Accidents",
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
+            "title": "Rail Equipment Accidents"
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
-            "landingPage": "https://data.transportation.gov/d/xean-25kh",
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
+            "identifier": "DOT-121",
+            "issued": "2000-01-01",
             "keyword": [
                 "bus",
                 "company safety profile.",
@@ -102822,59 +102836,60 @@
                 "safersys",
                 "safety and fitness electronic records"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "DOT-121",
+            "landingPage": "https://data.transportation.gov/d/xean-25kh",
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
-            "title": "Safety and Fitness Electronic Records (SAFER)",
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
-            "analysisUnit": "Motor Carriers",
-            "categoryDesignation": "Research",
-            "phone": "202-493-0215",
-            "language": [
-                "en-US"
-            ]
+            "title": "Safety and Fitness Electronic Records (SAFER)"
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
-            "landingPage": "https://data.transportation.gov/d/xegp-m7m8",
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
+                    "mediaType": "text/csv",
+                    "title": "Vehicle API CSV"
+                }
             ],
+            "identifier": "65.8",
+            "isPartOf": "DOT-65",
+            "issued": "2015-10-05",
             "keyword": [
                 "49",
                 "551",
@@ -102911,61 +102926,62 @@
                 "vin",
                 "vpic"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "65.8",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
-            "description": "The NHTSA Product Information Catalog and Vehicle Listing (vPIC) is a consolidated platform that presents data collected within the manufacturer reported data from CFR 49 Parts 551 - 574 for use in a variety of modern tools. NHTSA's vPIC platform is intended to serve as a centralized source for basic Vehicle Identification Number (VIN) decoding, Manufacturer Information Database (MID), Manufacturer Equipment Plant Identification and associated data. vPIC is intended to support the Open Data and Transparency initiatives of the agency by allowing the data to be freely used by the public without the burden of manual retrieval from a library of electronic documents (PDFs). While these documents will still be available online for viewing within the Manufacturer Information Database (MID) module of vPIC one can view and use the actual data through the VIN Decoder and Application Programming Interface (API) modules.",
-            "title": "NHTSA Product Information Catalog and Vehicle Listing (vPIC) - Vehicle API CSV",
-            "isPartOf": "DOT-65",
-            "agencyProgramURL": "http://vpic.nhtsa.dot.gov/",
+            "landingPage": "https://data.transportation.gov/d/xegp-m7m8",
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
-                    "mediaType": "text/csv",
-                    "downloadURL": "http://vpic.nhtsa.dot.gov/api/",
-                    "description": "APIs for use by developers, programmers or researchers interested in obtaining raw Vehicle or Manufacturer data from vPIC.",
-                    "@type": "dcat:Distribution",
-                    "title": "Vehicle API CSV"
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
+            "title": "NHTSA Product Information Catalog and Vehicle Listing (vPIC) - Vehicle API CSV"
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
-            "landingPage": "https://data.transportation.gov/d/xemh-6vde",
-            "issued": "2013-11-27",
-            "temporal": "R/2013-11-30/P3M",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-14",
+            "categoryDesignation": "Administrative",
             "collectionInstrument": "Metadata Registry",
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
+            "identifier": "DOT-336",
+            "issued": "2013-11-27",
             "keyword": [
                 "api",
                 "data",
@@ -102975,59 +102991,61 @@
                 "public data listing",
                 "raw data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "DOT Socrata",
-                "hasEmail": "mailto:Socrata@dot.gov"
-            },
-            "identifier": "DOT-336",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Secretary of Transportation"
-            },
-            "description": "United States Department of Transportation Public Data Listing. The file is formatted to comply with project open data common core metadata requirements (http://project-open-data.github.io/schema/) and conforms to schema version 1.1",
-            "title": "Department of Transportation Public Data Listing",
-            "agencyProgramURL": "https://www.transportation.gov/data",
+            "landingPage": "https://data.transportation.gov/d/xemh-6vde",
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
-            "spatial": "N/A",
-            "describedBy": "https://project-open-data.cio.gov/v1.1/schema/",
-            "dataQuality": true,
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "http://www.dot.gov/data.json",
+            "spatial": "N/A",
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
+            "title": "Department of Transportation Public Data Listing"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/xeuj-kht9",
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
+                    "description": "2012 Nevada HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/nevada2012.zip",
+                    "mediaType": "application/zip",
+                    "title": "2012 Nevada"
+                }
+            ],
+            "identifier": "678.82",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -103041,82 +103059,46 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.82",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2012 Nevada",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/xeuj-kht9",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/nevada2012.zip",
-                    "description": "2012 Nevada HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2012 Nevada"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2012 Nevada"
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
-            "landingPage": "https://data.transportation.gov/d/xfgk-y53h",
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
-            "identifier": "364.13",
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
@@ -103125,84 +103107,82 @@
                     "title": "Biomechanics Test Database Interactive Access"
                 }
             ],
-            "spatial": "N/A",
-            "dataQuality": true,
+            "identifier": "364.13",
+            "isPartOf": "DOT-364",
+            "issued": "1998-12-24",
+            "keyword": [
+                "nhtsa crash test database",
+                "nhtsa vehicle crash test database"
+            ],
+            "landingPage": "https://data.transportation.gov/d/xfgk-y53h",
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
-            "landingPage": "https://data.transportation.gov/d/xfi2-tdqt",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2020-05-28",
-            "temporal": "2017-01-01/2017-12-31",
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
-            "identifier": "https://data.transportation.gov/api/views/xfi2-tdqt",
             "description": "Facts and figures on ferry vessels",
-            "title": "National Census of Ferry Operators (NCFO) 2018: Ferry Vessels: Calendar Year 2017",
+            "identifier": "https://data.transportation.gov/api/views/xfi2-tdqt",
+            "issued": "2020-05-28",
+            "landingPage": "https://data.transportation.gov/d/xfi2-tdqt",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2020-07-06",
             "programCode": [
                 "021:042"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "temporal": "2017-01-01/2017-12-31",
             "theme": [
                 "Ferry Transit"
-            ]
+            ],
+            "title": "National Census of Ferry Operators (NCFO) 2018: Ferry Vessels: Calendar Year 2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/xfkb-3bxx",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2025-01-30",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-30",
-            "keyword": [
-                "age groups",
-                "automobile drivers",
-                "driver licenses",
-                "driver licensing",
-                "licenses",
-                "licensing",
-                "sex"
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
-            "identifier": "https://data.transportation.gov/api/views/xfkb-3bxx",
+            "dataQuality": true,
             "description": "Licensed driver data from Highway Statistics table DL-22, broken down by state, sex, and age group.",
-            "title": "Licensed Drivers, by state, sex, and age group",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -103210,51 +103190,84 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xfkb-3bxx/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xfkb-3bxx/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xfkb-3bxx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/xfkb-3bxx/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xfkb-3bxx/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xfkb-3bxx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xfkb-3bxx/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xfkb-3bxx/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xfkb-3bxx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/xfkb-3bxx",
+            "issued": "2025-01-30",
+            "keyword": [
+                "age groups",
+                "automobile drivers",
+                "driver licenses",
+                "driver licensing",
+                "licenses",
+                "licensing",
+                "sex"
+            ],
+            "landingPage": "https://data.transportation.gov/d/xfkb-3bxx",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2025-01-30",
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
+            "title": "Licensed Drivers, by state, sex, and age group"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyProgramURL": "http://www.nhtsa.gov/fuel-economy",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/xfrs-2qdu",
-            "issued": "2015-12-16",
-            "temporal": "2015/2016",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Administrative - Regulatory",
             "collectionInstrument": "Transportation",
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
+            "identifier": "DOT-1862",
+            "issued": "2015-12-16",
             "keyword": [
                 "amfa",
                 "civil penalties",
@@ -103271,73 +103284,78 @@
                 "report",
                 "shortfall"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "DOT-1862",
+            "landingPage": "https://data.transportation.gov/d/xfrs-2qdu",
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
-            "title": "CAFE (Corporate Average Fuel Economy)",
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
+            "title": "CAFE (Corporate Average Fuel Economy)"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/xg5t-c92f",
-            "issued": "2022-10-31",
             "@type": "dcat:Dataset",
-            "modified": "2022-11-21",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joe McGill",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "These Charts show the value, tons and ton-miles using each state as an origin and destination. The Years available are 1997-2017",
             "identifier": "https://data.transportation.gov/api/views/xg5t-c92f",
+            "issued": "2022-10-31",
+            "landingPage": "https://data.transportation.gov/d/xg5t-c92f",
+            "modified": "2022-11-21",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "These Charts show the value, tons and ton-miles using each state as an origin and destination. The Years available are 1997-2017",
             "title": "Value, Tons, and Ton-Miles by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.fhwa.dot.gov/policyinformation/hpms.cfm",
             "bureauCode": [
                 "021:15"
             ],
-            "landingPage": "https://data.transportation.gov/d/xh98-85pd",
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
+                    "description": "2011 Oklahoma HPMS Shapefile",
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/oklahoma2011.zip",
+                    "mediaType": "application/zip",
+                    "title": "2011 Oklahoma"
+                }
+            ],
+            "identifier": "678.38",
+            "isPartOf": "DOT-678",
+            "issued": "1981-11-01",
             "keyword": [
                 "aadt",
                 "condition",
@@ -103351,56 +103369,50 @@
                 "use",
                 "vmt"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "678.38",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
-            "description": "HPMS compiles data on highway network extent, use, condition, and performance.  The system consists of a geospatially-enabled database that is used to generate reports and provides tools for data analysis.  Information from HPMS is used by many stakeholders across the US DOT, the Administration, Congress, and the transportation community.",
-            "title": "Highway Performance Monitoring System (HPMS) - 2011 Oklahoma",
-            "isPartOf": "DOT-678",
+            "landingPage": "https://data.transportation.gov/d/xh98-85pd",
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
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/hpms/shapefiles/oklahoma2011.zip",
-                    "description": "2011 Oklahoma HPMS Shapefile",
-                    "@type": "dcat:Distribution",
-                    "title": "2011 Oklahoma"
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
+            "title": "Highway Performance Monitoring System (HPMS) - 2011 Oklahoma"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/xig6-cb63",
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
+            "description": "The purpose of the data environment is to provide multi-modal data and contextual information (weather and incidents) that can be used to research and develop Intelligent Transportation System applications. This data set contains the following data for the two months of September and October 2011 in Pasadena, California: Highway network data, Demand data, Sample mobile sightings provided for a two-hour period, provided by AirSage (see note 1 below), Network performance data (measured and forecast), Work zone data, Weather data, and Changeable message sign data.\r\n\r\nThis legacy dataset was created before data.transportation.gov and is only currently available via the attached file(s). Please contact the dataset owner if there is a need for users to work with this data using the data.transportation.gov analysis features (online viewing, API, graphing, etc.) and the USDOT will consider modifying the dataset to fully integrate in data.transportation.gov.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.transportation.gov/download/xig6-cb63/application/msword",
+                    "mediaType": "application/msword"
+                }
+            ],
+            "identifier": "https://data.transportation.gov/api/views/xig6-cb63",
             "issued": "2012-06-15",
-            "@type": "dcat:Dataset",
-            "temporal": "2011-09-01/2011-10-31",
-            "modified": "2012-06-15",
             "keyword": [
                 "arterial",
                 "california",
@@ -103415,53 +103427,55 @@
                 "usdot data capture and management program (dcm)",
                 "weather"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kate Hartman",
-                "hasEmail": "mailto:kate.hartman@dot.gov"
-            },
+            "landingPage": "https://data.transportation.gov/d/xig6-cb63",
+            "language": [
+                "en-US"
+            ],
+            "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
+            "modified": "2012-06-15",
+            "programCode": [
+                "021:013"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "US Department of Transportation"
             },
-            "identifier": "https://data.transportation.gov/api/views/xig6-cb63",
-            "description": "The purpose of the data environment is to provide multi-modal data and contextual information (weather and incidents) that can be used to research and develop Intelligent Transportation System applications. This data set contains the following data for the two months of September and October 2011 in Pasadena, California: Highway network data, Demand data, Sample mobile sightings provided for a two-hour period, provided by AirSage (see note 1 below), Network performance data (measured and forecast), Work zone data, Weather data, and Changeable message sign data.\r\n\r\nThis legacy dataset was created before data.transportation.gov and is only currently available via the attached file(s). Please contact the dataset owner if there is a need for users to work with this data using the data.transportation.gov analysis features (online viewing, API, graphing, etc.) and the USDOT will consider modifying the dataset to fully integrate in data.transportation.gov.",
-            "title": "Pasadena Test Data Sets",
-            "programCode": [
-                "021:013"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://data.transportation.gov/download/xig6-cb63/application/msword",
-                    "mediaType": "application/msword"
-                }
-            ],
             "spatial": "Pasadena, California",
-            "dataQuality": true,
-            "license": "http://creativecommons.org/licenses/by-sa/3.0/legalcode",
-            "accrualPeriodicity": "irregular",
+            "temporal": "2011-09-01/2011-10-31",
             "theme": [
                 "Automobiles"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Pasadena Test Data Sets"
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
-            "landingPage": "https://data.transportation.gov/d/xj3g-6eev",
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
+                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12febtvt/12febtvt.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "February 2012"
+                }
             ],
+            "identifier": "DOT-18",
+            "issued": "1970-01-01",
             "keyword": [
                 "aadt",
                 "'fhwa",
@@ -103471,75 +103485,42 @@
                 "vmt",
                 "volume data"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "DOT-18",
+            "landingPage": "https://data.transportation.gov/d/xj3g-6eev",
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
-            "title": "Monthly Traffic Volume Trends",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/policyinformation/index.cfm",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.fhwa.dot.gov/policyinformation/travel_monitoring/12febtvt/12febtvt.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "February 2012"
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
-            "analysisUnit": "Vehicles and Vehicle Miles Traveled",
-            "categoryDesignation": "Administrative",
-            "phone": "202-366-1067",
-            "language": [
-                "en-US"
-            ]
+            "title": "Monthly Traffic Volume Trends"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/xjbt-2jz9",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2021-12-21",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-21",
-            "keyword": [
-                "accessibility",
-                "bikeshare",
-                "docked bikeshare",
-                "micromobility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
-                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
+                "hasEmail": "mailto:https://transportation.libanswers.com/form?queue_id=1810"
             },
-            "identifier": "https://data.transportation.gov/api/views/xjbt-2jz9",
             "description": "Docked bikeshare stations that can be reached traveling via the road network in a given amount of time (10 or 20 minutes) when starting at a specified docking station. Times were calculated using the street network and a travel speed of 10 miles per hour but straight lines are used to represent the docked bikeshare stations that can be reached. Topography is not taken into account but the type of road is taken in account.\r\n\r\nVisualization available at: https://data.bts.gov/stories/s/8s3h-vvui",
-            "title": "Bikeshare Isochrones: Line Representation of Stations Accessible",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -103547,47 +103528,82 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xjbt-2jz9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xjbt-2jz9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xjbt-2jz9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/xjbt-2jz9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xjbt-2jz9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xjbt-2jz9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xjbt-2jz9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xjbt-2jz9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xjbt-2jz9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/xjbt-2jz9",
+            "issued": "2021-12-21",
+            "keyword": [
+                "accessibility",
+                "bikeshare",
+                "docked bikeshare",
+                "micromobility"
+            ],
+            "landingPage": "https://data.transportation.gov/d/xjbt-2jz9",
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
+            "title": "Bikeshare Isochrones: Line Representation of Stations Accessible"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "agencyDataSeriesURL": "http://www-nrd.nhtsa.dot.gov/CMSWeb/listpublications.aspx%3FId=19&ShowBy=Category",
+            "agencyProgramURL": "http://www.nhtsa.gov/Research/Human+Factors/Seatbelt+and+Child+Seat+Use",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/xjk2-qksr",
-            "issued": "2006-12-31",
-            "temporal": "2005-04-01/2005-08-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "references": [
-                "http://www-nrd.nhtsa.dot.gov/Pubs/811852.pdf"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NHTSA-Datahub",
+                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "ftp://ftp.nhtsa.dot.gov/Child_Seat_Usage_Surveys/LATCH_Use_and_Misuse_Study_2006/contents.pdf",
+            "describedByType": "application/pdf",
+            "description": "Provide information on the impact of LATCH on child seat use. It will show if consumers are using LATCH to install child safety seats, if they are easy to install and if they are installed correctly.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/Child_Seat_Usage_Surveys/LATCH_Use_and_Misuse_Study_2006/tbloccupant.sas7bdat",
+                    "mediaType": "text/plain",
+                    "title": "SAS Occupant Data"
+                }
             ],
+            "identifier": "539.1",
+            "isPartOf": "DOT-539",
+            "issued": "2006-12-31",
             "keyword": [
                 "child restraint systems",
                 "css",
@@ -103598,82 +103614,45 @@
                 "research methodology",
                 "use and misuse"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "539.1",
+            "landingPage": "https://data.transportation.gov/d/xjk2-qksr",
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
-            "title": "Child Restraint Use Survey:  LATCH Use and Misuse - SAS Occupant Data",
-            "isPartOf": "DOT-539",
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
+            "title": "Child Restraint Use Survey:  LATCH Use and Misuse - SAS Occupant Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "rights": "internal application",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/xk9f-ry57",
-            "issued": "2018-12-18",
-            "temporal": "R/2013/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "Transportation",
-            "keyword": [
-                "grantee oversight",
-                "grants",
-                "highway safety",
-                "management",
-                "post-award",
-                "vouchers"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "485.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": false,
             "description": "database program developed by NHTSA to assist states in the financial management of Federal grants.  The GTS system is a post-award system and does not manage Grant Applications.",
-            "title": "The Grants Tracking System -",
-            "primaryITInvestmentUII": "021-100515114",
-            "programCode": [
-                "021:033"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -103681,50 +103660,50 @@
                     "mediaType": "text/html"
                 }
             ],
-            "dataQuality": false,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "theme": [
-                "Transportation"
+            "identifier": "485.0",
+            "issued": "2018-12-18",
+            "keyword": [
+                "grantee oversight",
+                "grants",
+                "highway safety",
+                "management",
+                "post-award",
+                "vouchers"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "categoryDesignation": "Research",
+            "landingPage": "https://data.transportation.gov/d/xk9f-ry57",
             "language": [
                 "en-US"
             ],
-            "phone": "202-366-5649"
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2024-05-01",
+            "phone": "202-366-5649",
+            "primaryITInvestmentUII": "021-100515114",
+            "programCode": [
+                "021:033"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "rights": "internal application",
+            "temporal": "R/2013/P1Y",
+            "theme": [
+                "Transportation"
+            ],
+            "title": "The Grants Tracking System -"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/xkmg-ff2t",
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
-            "identifier": "https://data.transportation.gov/api/views/xkmg-ff2t",
             "description": "*This is a \"daily difference\" dataset.  See dataset attachment \"FMCSA Dataset Description and Data Definitions - Select Datasets\" for more information.*  This dataset contains information on a carrier\u2019s/broker\u2019s/freight forwarder\u2019s previous insurance policy(ies). This dataset contains the DOT number and docket number of the entity. Additionally, it contains the cancellation method (cancelled, replaced, name change, transferred), the type of policy, the policy number, and the effective and cancellation dates of the policy.",
-            "title": "InsHist",
-            "programCode": [
-                "021:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -103732,36 +103711,43 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/xkmg-ff2t",
+            "issued": "2023-04-14",
+            "keyword": [
+                "active",
+                "for-hire motor carriers",
+                "operating authority",
+                "registration status",
+                "revoked",
+                "suspended"
+            ],
+            "landingPage": "https://data.transportation.gov/d/xkmg-ff2t",
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
+            "title": "InsHist"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/xkn3-5fci",
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
-            "identifier": "https://data.transportation.gov/api/views/xkn3-5fci",
             "description": "Records for carrier/broker/freight forwarder active or pending individual insurance policies. The records are linked to the entities by docket numbers included in the dataset. The dataset contains information on the insurance policy, including insurance company name, policy number and type of insurance. Entities can hold multiple insurance policies, so there may be multiple records associated with a particular entity.  See dataset attachment \"FMCSA Dataset Description and Data Definitions - Select Datasets\" for more information.",
-            "title": "Insur - All With History",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -103769,38 +103755,39 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/xkn3-5fci",
+            "issued": "2023-12-08",
+            "keyword": [
+                "insurance",
+                "motor carrier"
+            ],
+            "landingPage": "https://data.transportation.gov/d/xkn3-5fci",
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
-            "landingPage": "https://data.transportation.gov/d/xkuc-f3hj",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2024-05-01",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-30",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Joe McGill",
                 "hasEmail": "mailto:joseph.mcgill@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/xkuc-f3hj",
             "description": "A data base of responses to the 2022 National Census of Ferries.\n\nThis file gives information about ferry vessels.",
-            "title": "2022 NCFO Vessels File",
-            "programCode": [
-                "021:042"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -103808,68 +103795,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xkuc-f3hj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xkuc-f3hj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xkuc-f3hj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/xkuc-f3hj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xkuc-f3hj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xkuc-f3hj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xkuc-f3hj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xkuc-f3hj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xkuc-f3hj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/xkuc-f3hj",
+            "issued": "2024-05-01",
+            "landingPage": "https://data.transportation.gov/d/xkuc-f3hj",
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
+            "title": "2022 NCFO Vessels File"
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
-            "landingPage": "https://data.transportation.gov/d/xkv5-xwbd",
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
-            "identifier": "692.1",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - MAP-21 National Highway System",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "primaryITInvestmentUII": "021-845083703",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -103878,56 +103859,56 @@
                     "title": "MAP-21 National Highway System"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.1",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/xkv5-xwbd",
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
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - MAP-21 National Highway System"
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
-            "landingPage": "https://data.transportation.gov/d/xmn8-5gjc",
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
-            "identifier": "692.21",
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
@@ -103936,62 +103917,51 @@
                     "title": "2012 Fatal Crashes"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.21",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/xmn8-5gjc",
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
-                "signal phasing and timing (spat)",
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
-            "identifier": "https://data.transportation.gov/api/views/xn7c-yu2n",
+            "dataQuality": true,
             "description": "The Tampa CV Pilot generates  data from the interaction between vehicles and between vehicles and infrastructure. This dataset consists of Signal Phasing and Timing Message (SPaT) Messages transmitted by road-side units (RSU) located throughout the Tampa CV Pilot Study area. The full set of raw, SPaT data from Tampa CV Pilot can be found in the <a href=\"http://usdot-its-cvpilot-publicdata.s3.amazonaws.com/index.html\" target=\"_blank\" >ITS Sandbox</a>. The data fields follow SAE J2735 data frames (Section 6) and structure (Section 7).\n\nThis dataset holds a flattened sample of the SPaT data from Tampa CV Pilot. A column of random numbers (randomNum) was added to allow for random sampling of data points within Socrata.",
-            "title": "Tampa CV Pilot Signal Phasing and Timing (SPaT) Sample",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -103999,46 +103969,88 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xn7c-yu2n/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xn7c-yu2n/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xn7c-yu2n/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/xn7c-yu2n/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xn7c-yu2n/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xn7c-yu2n/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xn7c-yu2n/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xn7c-yu2n/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xn7c-yu2n/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Tampa, Florida",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/xn7c-yu2n",
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
+                "signal phasing and timing (spat)",
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
+            "title": "Tampa CV Pilot Signal Phasing and Timing (SPaT) Sample"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://catalog.data.faa.gov/dataset/chart-supplements---aeronautical-information-services-digital-products",
             "bureauCode": [
                 "021:12"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Chief Data Office",
+                "hasEmail": "mailto:9-EIM-InfoLink@faa.gov"
+            },
+            "description": "The Chart Supplements are searchable by individual airport in PDF format. They contain data on public and joint use airports, seaplane bases, heliports, VFR airport sketches, NAVAIDs, communications data, weather data, airspace, special notices, and operational procedures.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/",
+                    "mediaType": "application/zip",
+                    "title": "Aeronautical Information Services Digital Products"
+                }
+            ],
+            "identifier": "8fa3e4cb-513b-4c1b-9348-30da21c722cb",
             "issued": "2020-11-14",
-            "@type": "dcat:Dataset",
-            "modified": "2021-11-09",
             "keyword": [
                 "aircraft",
                 "airport",
@@ -104050,71 +104062,38 @@
                 "procedure",
                 "vfr"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Chief Data Office",
-                "hasEmail": "mailto:9-EIM-InfoLink@faa.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Aviation Administration"
-            },
-            "identifier": "8fa3e4cb-513b-4c1b-9348-30da21c722cb",
-            "description": "The Chart Supplements are searchable by individual airport in PDF format. They contain data on public and joint use airports, seaplane bases, heliports, VFR airport sketches, NAVAIDs, communications data, weather data, airspace, special notices, and operational procedures.",
-            "title": "Chart Supplements - Aeronautical Information Services Digital Products",
+            "landingPage": "https://catalog.data.faa.gov/dataset/chart-supplements---aeronautical-information-services-digital-products",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2021-11-09",
             "primaryITInvestmentUII": "021-129509270",
             "programCode": [
                 "021:001"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/",
-                    "mediaType": "application/zip",
-                    "title": "Aeronautical Information Services Digital Products"
-                }
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Federal Aviation Administration"
+            },
             "systemOfRecords": "https://www.govinfo.gov/content/pkg/FR-2016-08-15/pdf/2016-19354.pdf",
-            "license": "https://project-open-data.cio.gov/unknown-license/",
             "theme": [
                 "Aviation"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Chart Supplements - Aeronautical Information Services Digital Products"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://data.transportation.gov/d/xnub-2sc4",
             "bureauCode": [
                 "021:00"
             ],
-            "rights": "Non commercial use only. Creative Commons Attribution: Non-commercial 4.0 International (CC-BY-NC 4.0) license",
-            "issued": "2023-09-25",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-19",
-            "keyword": [
-                "air",
-                "intercity bus",
-                "intercity transportation",
-                "rail",
-                "rural"
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
-            "identifier": "https://data.transportation.gov/api/views/xnub-2sc4",
             "description": "Airports with scheduled service and intercity bus and intercity rail (Amtrak/Alaska rail) facilities for years 2006, 2012, 2018, and 2021. Used to find rural areas with access to one or more of these transportation modes: https://data.bts.gov/Research-and-Statistics/Access-to-Intercity-Air-Bus-and-Rail-Transportatio/m2bh-93w3 . \n\nAirports with scheduled service and intercity bus and intercity rail (Amtrak/Alaska rail) facilities for years 2006, 2012, 2018, and 2023. Used to find rural areas with access to one or more of these transportation modes: https://data.bts.gov/Research-and-Statistics/Access-to-Intercity-Air-Bus-and-Rail-Transportatio/m2bh-93w3 . In 2021, bus stops are from the Intercity Bus Atlas (https://geodata.bts.gov/datasets/usdot::intercity-bus-atlas-stops/explore). To allow the use of the Intercity Bus Atlas (ICBA) datasets, intercity bus providers grant the USDOT a Creative Commons Attribution \u2013 Non-commercial 4.0 International (CC-BY-NC 4.0) license. The CC-BY-NC 4.0 license is available at, https://creativecommons.org/licenses/by-nc/4.0/legalcode. For more information about the memorandum of understanding between partner intercity bus providers and BTS underlying the ICBA, please consult https://www.bts.gov/national-intercity-bus-atlas-partnerships. ICBA data are permitted and encouraged for research, analysis, and planning. The data are not intended for trip planning, scheduling, navigation, or any real-time or near real-time use by passengers, transportation operators, service providers, or transportation planners. Commercial and all other reuse of the data is prohibited. As part of the license agreement for the data, BTS are also not permitted to make substantive material alterations to the submitted GTFS data. All other uses or re-uses of the data are prohibited. Finally, BTS expressly disclaims all liability for the unauthorized use of or misuse of any data collected as a part of this effort by third parties. BTS furthermore does not guarantee the real-time or near real-time accuracy or quality of the data as route service information, bus stop location information and other data collected may change over time. \n\nInteractive map showing access to intercity transportation in rural areas:\nhttps://datahub.transportation.gov/stories/s/Rural-Access-to-Intercity-Transportation/gr9y-9gjq/edit\n\nMethodology:\nhttps://datahub.transportation.gov/stories/s/dbb4-pr2c",
-            "title": "Intercity Air, Bus, and Rail Transportation Facilities",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -104122,73 +104101,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xnub-2sc4/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xnub-2sc4/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xnub-2sc4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/xnub-2sc4/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xnub-2sc4/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xnub-2sc4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xnub-2sc4/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xnub-2sc4/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xnub-2sc4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/xnub-2sc4",
+            "issued": "2023-09-25",
+            "keyword": [
+                "air",
+                "intercity bus",
+                "intercity transportation",
+                "rail",
+                "rural"
+            ],
+            "landingPage": "https://data.transportation.gov/d/xnub-2sc4",
+            "modified": "2024-11-19",
+            "phone": "202-366-DATA(3282) ",
+            "programCode": [
+                "021:053"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Transportation Statistics"
+            },
+            "rights": "Non commercial use only. Creative Commons Attribution: Non-commercial 4.0 International (CC-BY-NC 4.0) license",
             "spatial": "United States",
             "theme": [
                 "Research and Statistics"
             ],
-            "phone": "202-366-DATA(3282) "
+            "title": "Intercity Air, Bus, and Rail Transportation Facilities"
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
-            "landingPage": "https://data.transportation.gov/d/xnz7-d59c",
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
-            "identifier": "224.4",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Railroad Administration"
-            },
-            "description": "The entire National Highway-Rail Crossing Inventory is available in three separate downloadble files. There is a file of all current Public-at-Grade crossings. There is a file of all current Private and grade-separated crossings. There is also a file which contains about 10 years of archival records for all types of crossings.",
-            "title": "Highway-Rail Crossings Inventory Data - GCIS Secure API",
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
@@ -104197,40 +104177,50 @@
                     "title": "GCIS Secure API"
                 }
             ],
-            "spatial": "Latitude/Longitude",
-            "describedBy": "http://safetydata.fra.dot.gov/OfficeofSafety/Documents/GCIS%20Electronic%20Submissions%20Instructions.pdf",
-            "dataQuality": true,
+            "identifier": "224.4",
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
+            "landingPage": "https://data.transportation.gov/d/xnz7-d59c",
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
+            "title": "Highway-Rail Crossings Inventory Data - GCIS Secure API"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/xp92-5xme",
-            "issued": "2023-06-26",
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
-            "identifier": "https://data.transportation.gov/api/views/xp92-5xme",
             "description": "This dataset is the source dataset and contains raw data values. It will replace the current data download (https://safetydata.fra.dot.gov/OfficeofSafety/publicsite/DownloadCrossingInventoryData.aspx) when the safetydata.fra.dot.gov site is decommissioned in 2024. To download data that contains data in a user-friendly human-readable format, please reference https://data.transportation.gov/Railroads/Crossing-Inventory-Data-Current/m2f8-22s6.",
-            "title": "Crossing Inventory Source Data (Form 71) - Current",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -104238,96 +104228,84 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xp92-5xme/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xp92-5xme/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xp92-5xme/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/xp92-5xme/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xp92-5xme/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xp92-5xme/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xp92-5xme/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xp92-5xme/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xp92-5xme/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/xp92-5xme",
+            "issued": "2023-06-26",
+            "landingPage": "https://data.transportation.gov/d/xp92-5xme",
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
+            "title": "Crossing Inventory Source Data (Form 71) - Current"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "021:00"
             ],
-            "landingPage": "https://data.transportation.gov/d/xpex-3jnz",
-            "issued": "2024-11-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-15",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:answers@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/xpex-3jnz",
             "description": "General aviation performance and inventory.",
-            "title": "General Aviation",
+            "identifier": "https://data.transportation.gov/api/views/xpex-3jnz",
+            "issued": "2024-11-13",
+            "landingPage": "https://data.transportation.gov/d/xpex-3jnz",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-11-15",
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
+            "title": "General Aviation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://wzdx.massdot-swzm.com/index.html",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "021:15"
             ],
-            "issued": "2020-09-30",
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
             "conformsTo": "https://github.com/usdot-jpo-ode/jpo-wzdx/releases/tag/v2.0",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kate Hartman",
                 "hasEmail": "mailto:kate.hartman@dot.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "US Department of Transportation"
-            },
-            "identifier": "https://data.transportation.gov/api/views/xqcj-nkn2",
             "description": "This dataset provides information on work zones in the state of Massachusetts in a tabular format and is updated daily based on the <a href=\"https://wzdx.massdot-swzm.com/massdot_wzdx_v2.0.geojson\" target=\"_blank\" rel=\"noopener\">live MassDOT Work Zone Data Exchange (WZDx) Feed</a>.\n\nA continuously updating archive of the MassDOT WZDx feed data can be found at <a href=\"http://usdot-its-workzone-raw-publicdata.s3.amazonaws.com/index.html\" target=\"_blank\" rel=\"noopener\">ITS WorkZone Raw Data Sandbox</a> and the <a href=\"http://usdot-its-workzone-publicdata.s3.amazonaws.com/index.html\" target=\"_blank\" rel=\"noopener\">ITS WorkZone Semi-Processed Data Sandbox</a>.  The <a href=\"https://wzdx.massdot-swzm.com/massdot_wzdx_v2.0.geojson\" target=\"_blank\" rel=\"noopener\">live feed</a> is currently compliant with the <a href=\"https://github.com/usdot-jpo-ode/jpo-wzdx/tree/v2.0\" target=\"_blank\" rel=\"noopener\">WZDx Specification v2.0</a>.",
-            "title": "Massachusetts Department of Transportation (MassDOT) Work Zone Data Exchange (WZDx) v2.0 Feed Sample",
-            "programCode": [
-                "021:013"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -104335,48 +104313,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xqcj-nkn2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xqcj-nkn2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xqcj-nkn2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/xqcj-nkn2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xqcj-nkn2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xqcj-nkn2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xqcj-nkn2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xqcj-nkn2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xqcj-nkn2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "Massachusetts",
+            "identifier": "https://data.transportation.gov/api/views/xqcj-nkn2",
+            "issued": "2020-09-30",
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
+            "language": [
+                "en-US"
+            ],
             "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
-            "accrualPeriodicity": "irregular",
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
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Massachusetts Department of Transportation (MassDOT) Work Zone Data Exchange (WZDx) v2.0 Feed Sample"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/xqz2-92fw",
-            "issued": "2021-05-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-09-27",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Matthew Chambers",
                 "hasEmail": "mailto:no-reply@data.bts.gov"
             },
+            "description": "PPFSP 24",
+            "identifier": "https://data.transportation.gov/api/views/xqz2-92fw",
+            "issued": "2021-05-03",
             "keyword": [
                 "bureau",
                 "container",
@@ -104394,52 +104393,33 @@
                 "transportation",
                 "vessel"
             ],
-            "identifier": "https://data.transportation.gov/api/views/xqz2-92fw",
+            "landingPage": "https://data.transportation.gov/d/xqz2-92fw",
+            "modified": "2024-09-27",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "data.transportation.gov"
             },
-            "description": "PPFSP 24",
             "title": "Measuring Port Performance"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "agencyDataSeriesURL": "https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/NASS/",
+            "agencyProgramURL": "https://www.nhtsa.gov/national-automotive-sampling-system-nass/crashworthiness-data-system",
+            "analysisUnit": "Police reported motor vehicle crash",
             "bureauCode": [
                 "021:18"
             ],
-            "landingPage": "https://data.transportation.gov/d/xrgf-q6dn",
-            "issued": "1989-08-01",
-            "temporal": "R/1988-01-01/P1Y",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-01",
+            "categoryDesignation": "Research",
             "collectionInstrument": "NASSMAIN",
-            "references": [
-                "http://www-nrd.nhtsa.dot.gov/CATS/listpublications.aspx%3FId=l&ShowBy=DocType"
-            ],
-            "keyword": [
-                "automobile",
-                "crash",
-                "crashworthiness",
-                "data",
-                "injury",
-                "occupant"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NHTSA-Datahub",
                 "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
             },
-            "identifier": "242.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Highway Traffic Safety Administration"
-            },
+            "dataQuality": true,
             "description": "The National Automotive Sampling System (NASS) Crashworthiness Data System (CDS) is a nationwide crash data collection program sponsored by the U.S. Department of Transportation.  It is operated by the National Center for Statistics and Analysis (NCSA) of the National Highway Traffic Safety Administration (NHTSA).  The NASS CDS provides an automated, comprehensive national traffic crash database, and collects detailed information on a sample of all police-reported light ]motor vehicle traffic crashes.  Data collection is accomplished at 24 geographic sites, called Primary Sampling Units (PSUs).  These data are weighted to represent all police reported motor vehicle crashes occurring in the USA during the year involving passenger cars, light trucks and vans that were towed due to damage.",
-            "title": "National Automotive Sampling System - Crashworthiness Data System (NASS-CDS) - NASS-CDS (multiyear)",
-            "agencyProgramURL": "https://www.nhtsa.gov/national-automotive-sampling-system-nass/crashworthiness-data-system",
-            "programCode": [
-                "021:031"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -104448,45 +104428,52 @@
                     "title": "NASS-CDS (multiyear)"
                 }
             ],
-            "spatial": "Cities, counties, groups of counties.   Northeast, Southeast, Northern Midwest, Southern Midwest, Northwest, Southwest",
-            "dataQuality": true,
+            "identifier": "242.0",
+            "issued": "1989-08-01",
+            "keyword": [
+                "automobile",
+                "crash",
+                "crashworthiness",
+                "data",
+                "injury",
+                "occupant"
+            ],
+            "landingPage": "https://data.transportation.gov/d/xrgf-q6dn",
+            "language": [
+                "en-US"
+            ],
             "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "agencyDataSeriesURL": "https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/NASS/",
+            "modified": "2024-05-01",
+            "phone": "202-366-4998",
+            "programCode": [
+                "021:031"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Highway Traffic Safety Administration"
+            },
+            "references": [
+                "http://www-nrd.nhtsa.dot.gov/CATS/listpublications.aspx%3FId=l&ShowBy=DocType"
+            ],
+            "spatial": "Cities, counties, groups of counties.   Northeast, Southeast, Northern Midwest, Southern Midwest, Northwest, Southwest",
+            "temporal": "R/1988-01-01/P1Y",
             "theme": [
                 "Transportation"
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "analysisUnit": "Police reported motor vehicle crash",
-            "categoryDesignation": "Research",
-            "phone": "202-366-4998",
-            "language": [
-                "en-US"
-            ]
+            "title": "National Automotive Sampling System - Crashworthiness Data System (NASS-CDS) - NASS-CDS (multiyear)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/xrt2-b7j8",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2024-12-11",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-12",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bureau of Transportation Statistics",
                 "hasEmail": "mailto:answers@bts.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Bureau of Transportation Statistics"
-            },
-            "identifier": "https://data.transportation.gov/api/views/xrt2-b7j8",
             "description": "",
-            "title": "AFF - Air Carrier Aircraft Fleet Age",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -104494,100 +104481,94 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xrt2-b7j8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xrt2-b7j8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xrt2-b7j8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/xrt2-b7j8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xrt2-b7j8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xrt2-b7j8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xrt2-b7j8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xrt2-b7j8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xrt2-b7j8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/xrt2-b7j8",
+            "issued": "2024-12-11",
+            "landingPage": "https://data.transportation.gov/d/xrt2-b7j8",
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
+            "title": "AFF - Air Carrier Aircraft Fleet Age"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/xs2y-h68w",
             "bureauCode": [
                 "021:00"
             ],
-            "issued": "2020-04-10",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-18",
-            "keyword": [
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
-            "identifier": "https://data.transportation.gov/api/views/xs2y-h68w",
             "description": "Subtopic list of transportation costs faced by purchasers of transportation services (businesses and households)",
-            "title": "Transportation Economic Trends: Transportation Costs - Purchasers",
+            "identifier": "https://data.transportation.gov/api/views/xs2y-h68w",
+            "issued": "2020-04-10",
+            "keyword": [
+                "transportation cost"
+            ],
+            "landingPage": "https://data.transportation.gov/d/xs2y-h68w",
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
+            "title": "Transportation Economic Trends: Transportation Costs - Purchasers"
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
-            "landingPage": "https://data.transportation.gov/d/xsta-z8gv",
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
-            "identifier": "692.2",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
             "description": "HEPGIS is a web-based interactive geographic map server that allows users to navigate and view geo-spatial data, print maps, and obtain data on specific features using only a web browser.  It includes geo-spatial data used for transportation planning. HEPGIS previously received ARRA funding for development of Economically distressed Area maps. It is also being used to demonstrate emerging trends to address MPO and statewide planning  regulations/requirements , enhanced National Highway System,  Primary Freight Networks, commodity flows and safety data . HEPGIS has been used to help implement MAP-21 regulations and will help implement the Grow America Act, particularly related to Ladder of Opportunities and MPO reforms.",
-            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - MAP-21 National Highway System",
-            "isPartOf": "DOT-692",
-            "agencyProgramURL": "http://www.fhwa.dot.gov/planning/",
-            "primaryITInvestmentUII": "021-845083703",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -104596,52 +104577,51 @@
                     "title": "MAP-21 National Highway System"
                 }
             ],
-            "spatial": "National, State, County",
-            "dataQuality": true,
+            "identifier": "692.2",
+            "isPartOf": "DOT-692",
+            "issued": "2007-01-01",
+            "keyword": [
+                "arra planning",
+                "fhwa",
+                "geographic",
+                "geospatial",
+                "map"
+            ],
+            "landingPage": "https://data.transportation.gov/d/xsta-z8gv",
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
+            "title": "Rural & Statewide GIS/Data Needs (HEPGIS) - MAP-21 National Highway System"
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
-            "identifier": "https://data.transportation.gov/api/views/xsxk-bi22",
+            "dataQuality": true,
             "description": "Historic Highway Performance Monitoring System sample data for the year 2004",
-            "title": "Historic HPMS Data (Sample) - 2004",
-            "programCode": [
-                "021:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -104649,50 +104629,85 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xsxk-bi22/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xsxk-bi22/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xsxk-bi22/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/xsxk-bi22/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xsxk-bi22/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xsxk-bi22/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xsxk-bi22/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xsxk-bi22/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xsxk-bi22/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/xsxk-bi22",
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
+            "title": "Historic HPMS Data (Sample) - 2004"
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
-            "landingPage": "https://data.transportation.gov/d/xtmu-68fs",
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
+            "identifier": "115.3",
+            "isPartOf": "DOT-115",
+            "issued": "2005-08-09",
             "keyword": [
                 "compliance review",
                 "compliance review effectiveness model",
@@ -104702,64 +104717,39 @@
                 "program effectiveness",
                 "roadside inspection traffic enforcement"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FMCSA CDO",
-                "hasEmail": "mailto:fmcsa.cdo@dot.gov"
-            },
-            "identifier": "115.3",
+            "landingPage": "https://data.transportation.gov/d/xtmu-68fs",
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
-            "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/xtxm-f297",
-            "issued": "2022-03-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-08-08",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FRA Safety Admin",
                 "hasEmail": "mailto:no-reply@data.transportation.gov"
             },
-            "identifier": "https://data.transportation.gov/api/views/xtxm-f297",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "data.transportation.gov"
-            },
             "description": "",
-            "title": "BNSF Ownership",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -104767,45 +104757,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xtxm-f297/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xtxm-f297/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xtxm-f297/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/xtxm-f297/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xtxm-f297/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xtxm-f297/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xtxm-f297/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xtxm-f297/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xtxm-f297/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://data.transportation.gov/api/views/xtxm-f297",
+            "issued": "2022-03-03",
+            "landingPage": "https://data.transportation.gov/d/xtxm-f297",
+            "modified": "2024-08-08",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "data.transportation.gov"
+            },
             "theme": [
                 "Railroads"
-            ]
+            ],
+            "title": "BNSF Ownership"
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
-            "landingPage": "https://data.transportation.gov/d/xun5-tu36",
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
+            "identifier": "679.3",
+            "isPartOf": "DOT-679",
+            "issued": "1993-07-01",
             "keyword": [
                 "asphalt concrete",
                 "continuously reinforced concrete pavement",
@@ -104822,79 +104838,42 @@
                 "texture",
                 "traffic loading"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "FHWA-Datahub",
-                "hasEmail": "mailto:Highway-Data@dot.gov"
-            },
-            "identifier": "679.3",
+            "landingPage": "https://data.transportation.gov/d/xun5-tu36",
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
-            "landingPage": "https://data.transportation.gov/d/xx9i-2dhw",
             "bureauCode": [
                 "021:04"
             ],
-            "rights": "Business-sensitive data has been removed from this dataset",
-            "issued": "2020-05-05",
-            "@type": "dcat:Dataset",
-            "temporal": "2017-01-01/2017-12-31",
-            "modified": "2020-07-07",
-            "keyword": [
-                "ferry",
-                "passenger ferry",
-                "route",
-                "route segment",
-                "segment"
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
-            "identifier": "https://data.transportation.gov/api/views/xx9i-2dhw",
+            "dataQuality": true,
             "description": "Unique listing of reported 2017 calendar year ferry segments as surveyed in the 2018 NCFO.",
-            "title": "National Census of Ferry Operators (NCFO) 2018: Segment Data",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -104902,60 +104881,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xx9i-2dhw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xx9i-2dhw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xx9i-2dhw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/xx9i-2dhw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xx9i-2dhw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xx9i-2dhw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xx9i-2dhw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xx9i-2dhw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xx9i-2dhw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S., U.S. Territories, and applicable Canadian providences",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/xx9i-2dhw",
+            "issued": "2020-05-05",
+            "keyword": [
+                "ferry",
+                "passenger ferry",
+                "route",
+                "route segment",
+                "segment"
+            ],
+            "landingPage": "https://data.transportation.gov/d/xx9i-2dhw",
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
+            "title": "National Census of Ferry Operators (NCFO) 2018: Segment Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/xxtv-94gu",
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
-            "identifier": "https://data.transportation.gov/api/views/xxtv-94gu",
+            "dataQuality": true,
             "description": "Responding 2018 NCFO ferry operators",
-            "title": "National Census of Ferry Operators (NCFO) 2018: Operator data",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -104963,48 +104949,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xxtv-94gu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xxtv-94gu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xxtv-94gu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/xxtv-94gu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xxtv-94gu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xxtv-94gu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xxtv-94gu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xxtv-94gu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xxtv-94gu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "U.S., U.S. Territories, and applicable Canadian providences",
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/xxtv-94gu",
+            "issued": "2020-05-05",
+            "landingPage": "https://data.transportation.gov/d/xxtv-94gu",
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
+            "title": "National Census of Ferry Operators (NCFO) 2018: Operator data"
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
-            "landingPage": "https://data.transportation.gov/d/xy85-mwi3",
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
+                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/nits/Nontraffic%20crashes/2007/NiTS%202007%20nontraffic%20crashes.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2007 Nontraffic crashes"
+                }
             ],
+            "identifier": "288.4",
+            "isPartOf": "DOT-288",
+            "issued": "2009-01-27",
             "keyword": [
                 "crash",
                 "death",
@@ -105020,76 +105036,44 @@
                 "vehicle",
                 "victim"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "NHTSA-Datahub",
-                "hasEmail": "mailto:NHTSA-Datahub@dot.gov"
-            },
-            "identifier": "288.4",
+            "landingPage": "https://data.transportation.gov/d/xy85-mwi3",
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
-            "title": "Not in Traffic Surveillance (NiTS) - 2007 Nontraffic crashes",
-            "isPartOf": "DOT-288",
-            "agencyProgramURL": "http://www.nhtsa.gov/Data/State+Data+Programs",
-            "programCode": [
-                "021:032"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "ftp://ftp.nhtsa.dot.gov/nits/Nontraffic%20crashes/2007/NiTS%202007%20nontraffic%20crashes.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "2007 Nontraffic crashes"
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
+            "title": "Not in Traffic Surveillance (NiTS) - 2007 Nontraffic crashes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/xyfb-hgtv",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "021:04"
             ],
-            "issued": "2022-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-31",
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
-            "identifier": "https://data.transportation.gov/api/views/xyfb-hgtv",
+            "dataQuality": true,
             "description": "Number of air travel passengers boarded and denied boarding by month",
-            "title": "Commercial Aviation - Involuntary Denied Boarding",
-            "programCode": [
-                "021:053"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -105097,52 +105081,84 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xyfb-hgtv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xyfb-hgtv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xyfb-hgtv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://data.transportation.gov/api/views/xyfb-hgtv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xyfb-hgtv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xyfb-hgtv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://data.transportation.gov/api/views/xyfb-hgtv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://data.transportation.gov/api/views/xyfb-hgtv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://data.transportation.gov/api/views/xyfb-hgtv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://data.transportation.gov/api/views/xyfb-hgtv",
+            "issued": "2022-02-23",
+            "keyword": [
+                "air carriers",
+                "airlines",
+                "passengers"
+            ],
+            "landingPage": "https://data.transportation.gov/d/xyfb-hgtv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://www.usa.gov/government-works",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2022-03-31",
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
+            "title": "Commercial Aviation - Involuntary Denied Boarding"
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
-            "landingPage": "https://data.transportation.gov/d/xyfp-kxx5",
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
+                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/1999NTDxls.exe",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "1999 Database"
+                }
             ],
+            "identifier": "21.3",
+            "isPartOf": "DOT-21",
+            "issued": "2010-10-01",
             "keyword": [
                 "agency",
                 "allocation",
@@ -105161,87 +105177,48 @@
                 "urbanized",
                 "vehicles"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John D. Giorgis",
-                "hasEmail": "mailto:john.giorgis@dot.gov"
-            },
-            "identifier": "21.3",
+            "landingPage": "https://data.transportation.gov/d/xyfp-kxx5",
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
-            "title": "NTD Annual Module Data Set - 1999 Database",
-            "isPartOf": "DOT-21",
-            "agencyProgramURL": "http://www.ntdprogram.gov",
-            "programCode": [
-                "021:000"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.ntdprogram.gov/ntdprogram/datbase/1999NTDxls.exe",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "1999 Database"
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
+            "title": "NTD Annual Module Data Set - 1999 Database"
         },
         {
-            "accessLevel": "restricted public",
-            "rights": "https://wxde.fhwa.dot.gov/termsOfUse.jsp",
-            "bureauCode": [
-                "021:15"
-            ],
-            "landingPage": "https://data.transportation.gov/d/xyms-k8zz",
-            "issued": "2013-01-01",
-            "temporal": "R/2013-01-01/PT1S",
-            "@type": "dcat:Dataset",
-            "collectionInstrument": "Transportation",
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
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "accrualPeriodicity": "R/PT1S",
+            "agencyProgramURL": "https://ops.fhwa.dot.gov/weather/index.asp",
+            "bureauCode": [
+                "021:15"
             ],
+            "categoryDesignation": "Research",
+            "collectionInstrument": "Transportation",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "FHWA-Datahub",
                 "hasEmail": "mailto:Highway-Data@dot.gov"
             },
-            "identifier": "DOT-2068",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Federal Highway Administration"
-            },
+            "dataQuality": true,
+            "describedBy": "https://wxde.fhwa.dot.gov/auth2/metadata.jsp",
             "description": "The Weather Data Environment (WxDE) collects and shares transportation-related weather data with a particular focus on weather data related to connected vehicle applications. The WxDE collects data in real time from both fixed environmental sensor stations and mobile sources. The WxDE computes value-added enhancements to this data, such as checking the quality of observed data and inferring weather parameters from vehicle data (e.g., inferring precipitation based on windshield wiper activation). The WxDE archives both collected and computed data. The WxDE supports subscriptions for access to real-time data in near real time generated by individual weather-related connected vehicle projects.",
-            "title": "Weather Data Environment",
-            "agencyProgramURL": "https://ops.fhwa.dot.gov/weather/index.asp",
-            "programCode": [
-                "021:011"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -105250,29 +105227,64 @@
                     "title": "Data Catalog"
                 }
             ],
-            "describedBy": "https://wxde.fhwa.dot.gov/auth2/metadata.jsp",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/licenses/by-sa/3.0/",
-            "theme": [
-                "Transportation"
+            "identifier": "DOT-2068",
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
+            "landingPage": "https://data.transportation.gov/d/xyms-k8zz",
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
+            "title": "Weather Data Environment"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.transportation.gov/d/xz9a-9kps",
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
```

