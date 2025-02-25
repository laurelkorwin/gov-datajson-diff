# Change History for justice.json

### Changes from acf49f0 to dd2190f (Part 1/22)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
diff --git a/justice.json b/justice.json
index 34e8ae9..5a2c31c 100644
--- a/justice.json
+++ b/justice.json
@@ -3,52 +3,21 @@
     "@id": "https://www.justice.gov/data.json",
     "@type": "dcat:Catalog",
     "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
-    "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json",
-    "generated": "2024-05-22T14:39:47.2007411-04:00",
     "dataset": [
         {
             "@type": "dcat:Dataset",
-            "title": "Federal Firearms Licensees - December 2021",
-            "description": "Complete listing of federal firearms licensees in December 2021",
-            "modified": "2022-01-01T00:00:00",
             "accessLevel": "public",
-            "identifier": "4092",
-            "publisher": {
-                "name": "Bureau of Alcohol, Tobacco, Firearms and Explosives",
-                "@type": "org:Organization",
-                "subOrganizationOf": {
-                    "id": 10,
-                    "acronym": "DOJ",
-                    "name": "Department of Justice"
-                }
-            },
+            "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "011:14"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data Bureau of Alcohol, Tobacco, Firearms, and Explosives (USDOJ)",
                 "hasEmail": "mailto:atfopendata@atf.gov"
             },
-            "keyword": [
-                "FFL",
-                "firearm"
-            ],
-            "bureauCode": [
-                "011:14"
-            ],
-            "programCode": [
-                "011:000"
-            ],
-            "spatial": "U.S. State/Territory",
-            "temporal": "2021-12-01T00:00:00.0000000/2021-12-31T00:00:00.0000000",
-            "accrualPeriodicity": "R/P1M",
             "dataQuality": false,
-            "issued": "2022-01-01T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "landingPage": "https://www.atf.gov/firearms/listing-federal-firearms-licensees",
-            "theme": [
-                "geospatial"
-            ],
+            "description": "Complete listing of federal firearms licensees in December 2021",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -63,29 +32,60 @@
                     "mediaType": "application/vnd.ms-excel",
                     "title": "Federal Firearms Licensees - December 2021"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Antitrust Division Select Appellate Briefs",
-            "description": "Index of select appellate cases and briefs filed by the U.S. Department of Justice, Antitrust Division since January 1993. Cases are listed in reverse chronological order by brief date and by name of individual defendants, by company name, or by the entity.",
-            "modified": "2024-03-14T00:00:00",
-            "accessLevel": "public",
-            "identifier": "1",
+            ],
+            "identifier": "4092",
+            "issued": "2022-01-01T00:00:00",
+            "keyword": [
+                "FFL",
+                "firearm"
+            ],
+            "landingPage": "https://www.atf.gov/firearms/listing-federal-firearms-licensees",
+            "language": [
+                "eng"
+            ],
+            "modified": "2022-01-01T00:00:00",
+            "programCode": [
+                "011:000"
+            ],
             "publisher": {
-                "name": "Antitrust Division",
                 "@type": "org:Organization",
+                "name": "Bureau of Alcohol, Tobacco, Firearms and Explosives",
                 "subOrganizationOf": {
-                    "id": 10,
                     "acronym": "DOJ",
+                    "id": 10,
                     "name": "Department of Justice"
                 }
             },
+            "spatial": "U.S. State/Territory",
+            "temporal": "2021-12-01T00:00:00.0000000/2021-12-31T00:00:00.0000000",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Federal Firearms Licensees - December 2021"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Richard Hess",
                 "hasEmail": "mailto:richard.hess2@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "Index of select appellate cases and briefs filed by the U.S. Department of Justice, Antitrust Division since January 1993. Cases are listed in reverse chronological order by brief date and by name of individual defendants, by company name, or by the entity.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.justice.gov/atr/appellate-briefs",
+                    "mediaType": "text/html",
+                    "title": "Antitrust Division Select Appellate Briefs"
+                }
+            ],
+            "identifier": "1",
+            "issued": "2017-02-15T00:00:00",
             "keyword": [
                 "Select Appellate Briefs",
                 "Antitrust Division",
@@ -108,49 +108,56 @@
                 "opposition",
                 "motion"
             ],
-            "bureauCode": [
-                "011:00"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-03-14T00:00:00",
             "programCode": [
                 "011:022"
             ],
-            "spatial": "United States and International Territories",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "2017-02-15T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.justice.gov/atr/appellate-briefs",
-                    "mediaType": "text/html",
-                    "title": "Antitrust Division Select Appellate Briefs"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Antitrust Division Select Case Filings",
-            "description": "Index of select cases and documents filed by the U.S. Department of Justice, Antitrust Division. Cases are listed alphabetically by the last name of individual defendants, by company name, or by the entity's first name.",
-            "modified": "2024-04-22T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2",
             "publisher": {
-                "name": "Antitrust Division",
                 "@type": "org:Organization",
+                "name": "Antitrust Division",
                 "subOrganizationOf": {
-                    "id": 10,
                     "acronym": "DOJ",
+                    "id": 10,
                     "name": "Department of Justice"
                 }
             },
+            "spatial": "United States and International Territories",
+            "title": "Antitrust Division Select Appellate Briefs"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Richard Hess",
                 "hasEmail": "mailto:richard.hess2@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "Index of select cases and documents filed by the U.S. Department of Justice, Antitrust Division. Cases are listed alphabetically by the last name of individual defendants, by company name, or by the entity's first name.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.justice.gov/atr/antitrust-case-filings",
+                    "conformsTo": "https://www.isotc211.org/2005/gmi/",
+                    "mediaType": "text/html",
+                    "title": "Antitrust Division Select Case Filings"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.justice.gov/atr/antitrust-case-filings-alpha",
+                    "mediaType": "text/html",
+                    "title": "Antitrust Division Select Case Filings - Alphabetical"
+                }
+            ],
+            "identifier": "2",
+            "issued": "2017-02-15T00:00:00",
             "keyword": [
                 "Select Case Filings",
                 "Antitrust Division",
@@ -176,93 +183,42 @@
                 "expert reports",
                 "testimony"
             ],
-            "bureauCode": [
-                "011:00"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2024-04-22T00:00:00",
             "programCode": [
                 "011:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Antitrust Division",
+                "subOrganizationOf": {
+                    "acronym": "DOJ",
+                    "id": 10,
+                    "name": "Department of Justice"
+                }
+            },
             "spatial": "United States and International Territories",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "2017-02-15T00:00:00",
-            "language": [
-                "eng"
-            ],
             "theme": [
                 "geospatial"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.justice.gov/atr/antitrust-case-filings",
-                    "conformsTo": "https://www.isotc211.org/2005/gmi/",
-                    "mediaType": "text/html",
             "title": "Antitrust Division Select Case Filings"
         },
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.justice.gov/atr/antitrust-case-filings-alpha",
-                    "mediaType": "text/html",
-                    "title": "Antitrust Division Select Case Filings - Alphabetical"
-                }
-            ]
-        },
         {
             "@type": "dcat:Dataset",
-            "title": "Antitrust Division Sherman Act Violations Yielding a Corporate Fine of $10 Million or More",
-            "description": "This dataset contains five elements for Sherman Act violations yielding a corporate fine of $10 million or more - Defendant name (Federal Government Fiscal Year) - Product - Fine ($ in millions) - Geographic scope (domestic or international) - Country",
-            "modified": "2023-09-13T00:00:00",
             "accessLevel": "public",
-            "identifier": "3",
-            "publisher": {
-                "name": "Antitrust Division",
-                "@type": "org:Organization",
-                "subOrganizationOf": {
-                    "id": 10,
-                    "acronym": "DOJ",
-                    "name": "Department of Justice"
-                }
-            },
+            "bureauCode": [
+                "011:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Richard Hess",
                 "hasEmail": "mailto:richard.hess2@usdoj.gov"
             },
-            "keyword": [
-                "Sherman Act Violations",
-                "Corporate Fine",
-                "Department of Justice",
-                "Antitrust Division",
-                "Defendant",
-                "country",
-                "company",
-                "enforcement",
-                "monopoly",
-                "monopolization",
-                "corporation",
-                "anticompetitive",
-                "protection of competition",
-                "product",
-                "bid-rigging",
-                "price fixing"
-            ],
-            "bureauCode": [
-                "011:00"
-            ],
-            "programCode": [
-                "011:022"
-            ],
-            "spatial": "United States and International Territories",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "dataQuality": false,
-            "issued": "2017-01-25T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "theme": [
-                "geospatial"
-            ],
+            "description": "This dataset contains five elements for Sherman Act violations yielding a corporate fine of $10 million or more - Defendant name (Federal Government Fiscal Year) - Product - Fine ($ in millions) - Geographic scope (domestic or international) - Country",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -287,29 +243,66 @@
                     "mediaType": "text/html",
                     "title": "Antitrust Division Sherman Act Violations Yielding a Corporate Fine of $10 Million or More (Webpage)"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Antitrust Division Historic Workload Statistics",
-            "description": "Final workload statistics were published in 2019. This index page of dataset summarizes the Antitrust Division workload statistics compiled in 10-year increments from 1970-2019. The 10-year data sets show: the number of investigations (premerger, civil, and criminal), cases (civil, criminal, administrative, and appellate), judgement enforcements, case results, confinements, and other activities.",
-            "modified": "2020-10-08T00:00:00",
-            "accessLevel": "public",
-            "identifier": "4",
+            ],
+            "identifier": "3",
+            "issued": "2017-01-25T00:00:00",
+            "keyword": [
+                "Sherman Act Violations",
+                "Corporate Fine",
+                "Department of Justice",
+                "Antitrust Division",
+                "Defendant",
+                "country",
+                "company",
+                "enforcement",
+                "monopoly",
+                "monopolization",
+                "corporation",
+                "anticompetitive",
+                "protection of competition",
+                "product",
+                "bid-rigging",
+                "price fixing"
+            ],
+            "language": [
+                "eng"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-09-13T00:00:00",
+            "programCode": [
+                "011:022"
+            ],
             "publisher": {
-                "name": "Antitrust Division",
                 "@type": "org:Organization",
+                "name": "Antitrust Division",
                 "subOrganizationOf": {
-                    "id": 10,
                     "acronym": "DOJ",
+                    "id": 10,
                     "name": "Department of Justice"
                 }
             },
+            "spatial": "United States and International Territories",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Antitrust Division Sherman Act Violations Yielding a Corporate Fine of $10 Million or More"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Richard Hess",
                 "hasEmail": "mailto:richard.hess2@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "Final workload statistics were published in 2019. This index page of dataset summarizes the Antitrust Division workload statistics compiled in 10-year increments from 1970-2019. The 10-year data sets show: the number of investigations (premerger, civil, and criminal), cases (civil, criminal, administrative, and appellate), judgement enforcements, case results, confinements, and other activities.",
+            "distribution": [],
+            "identifier": "4",
+            "issued": "2019-06-28T00:00:00",
             "keyword": [
                 "Workload Statistics",
                 "Department of Justice",
@@ -327,43 +320,53 @@
                 "civil case",
                 "criminal cases"
             ],
-            "bureauCode": [
-                "011:00"
+            "landingPage": "https://www.justice.gov/atr/division-operations",
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2020-10-08T00:00:00",
             "programCode": [
                 "011:022"
             ],
-            "spatial": "United States and International Territories",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "2019-06-28T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "landingPage": "https://www.justice.gov/atr/division-operations",
-            "distribution": []
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Antitrust Division Workload Statistics FY 2000-2009",
-            "description": "This dataset summarizes the Antitrust Division workload activities for fiscal years 2000-2009.",
-            "modified": "2012-04-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "6",
             "publisher": {
-                "name": "Antitrust Division",
                 "@type": "org:Organization",
+                "name": "Antitrust Division",
                 "subOrganizationOf": {
-                    "id": 10,
                     "acronym": "DOJ",
+                    "id": 10,
                     "name": "Department of Justice"
                 }
             },
+            "spatial": "United States and International Territories",
+            "title": "Antitrust Division Historic Workload Statistics"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Richard Hess",
                 "hasEmail": "mailto:richard.hess2@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This dataset summarizes the Antitrust Division workload activities for fiscal years 2000-2009.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "conformsTo": "https://www.isotc211.org/2005/gmi/",
+                    "downloadURL": "https://www.justice.gov/sites/default/files/atr/legacy/2012/04/04/281484.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Antitrust Division Workload Statistics FY 2000-2009"
+                }
+            ],
+            "identifier": "6",
+            "isPartOf": "4",
+            "issued": "2012-03-23T00:00:00",
             "keyword": [
                 "Workload Statistics",
                 "Department of Justice",
@@ -381,54 +384,53 @@
                 "civil case",
                 "criminal case"
             ],
-            "bureauCode": [
-                "011:00"
+            "landingPage": "https://www.justice.gov/atr/division-operations",
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2012-04-04T00:00:00",
             "programCode": [
                 "011:022"
             ],
-            "spatial": "United States and International Territories",
-            "temporal": "1999-10-01T00:00:00.0000000/2009-09-30T00:00:00.0000000",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "4",
-            "dataQuality": false,
-            "issued": "2012-03-23T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "landingPage": "https://www.justice.gov/atr/division-operations",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "conformsTo": "https://www.isotc211.org/2005/gmi/",
-                    "downloadURL": "https://www.justice.gov/sites/default/files/atr/legacy/2012/04/04/281484.pdf",
-                    "format": "pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Antitrust Division Workload Statistics FY 2000-2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Antitrust Division Workload Statistics FY 1990-1999",
-            "description": "This dataset summarizes the Antitrust Division workload activities for fiscal years 1990-1999.",
-            "modified": "2009-05-29T00:00:00",
-            "accessLevel": "public",
-            "identifier": "7",
             "publisher": {
-                "name": "Antitrust Division",
                 "@type": "org:Organization",
+                "name": "Antitrust Division",
                 "subOrganizationOf": {
-                    "id": 10,
                     "acronym": "DOJ",
+                    "id": 10,
                     "name": "Department of Justice"
                 }
             },
+            "spatial": "United States and International Territories",
+            "temporal": "1999-10-01T00:00:00.0000000/2009-09-30T00:00:00.0000000",
+            "title": "Antitrust Division Workload Statistics FY 2000-2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Richard Hess",
                 "hasEmail": "mailto:richard.hess2@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This dataset summarizes the Antitrust Division workload activities for fiscal years 1990-1999.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.justice.gov/sites/default/files/atr/legacy/2009/06/09/246419.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Antitrust Division Workload Statistics FY 1990-1999"
+                }
+            ],
+            "identifier": "7",
+            "isPartOf": "4",
+            "issued": "2009-05-29T00:00:00",
             "keyword": [
                 "Workload Statistics",
                 "Department of Justice",
@@ -446,53 +448,60 @@
                 "civil case",
                 "criminal case"
             ],
-            "bureauCode": [
-                "011:00"
+            "landingPage": "https://www.justice.gov/atr/division-operations",
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-05-29T00:00:00",
             "programCode": [
                 "011:022"
             ],
-            "spatial": "United States and International Territories",
-            "temporal": "1989-10-01T00:00:00.0000000/1999-09-30T00:00:00.0000000",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "4",
-            "dataQuality": false,
-            "issued": "2009-05-29T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "landingPage": "https://www.justice.gov/atr/division-operations",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.justice.gov/sites/default/files/atr/legacy/2009/06/09/246419.pdf",
-                    "format": "pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Antitrust Division Workload Statistics FY 1990-1999"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Antitrust Division Workload Statistics FY 1980-1989",
-            "description": "This dataset summarizes the Antitrust Division workload activities for fiscal years 1980-1989.",
-            "modified": "2011-09-13T00:00:00",
-            "accessLevel": "public",
-            "identifier": "8",
             "publisher": {
-                "name": "Antitrust Division",
                 "@type": "org:Organization",
+                "name": "Antitrust Division",
                 "subOrganizationOf": {
-                    "id": 10,
                     "acronym": "DOJ",
+                    "id": 10,
                     "name": "Department of Justice"
                 }
             },
+            "spatial": "United States and International Territories",
+            "temporal": "1989-10-01T00:00:00.0000000/1999-09-30T00:00:00.0000000",
+            "title": "Antitrust Division Workload Statistics FY 1990-1999"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Richard Hess",
                 "hasEmail": "mailto:richard.hess2@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This dataset summarizes the Antitrust Division workload activities for fiscal years 1980-1989.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.justice.gov/atr/antitrust-division-workload-statistics-fy-1980-1989",
+                    "format": "html",
+                    "mediaType": "text/html",
+                    "title": "Antitrust Division Workload Statistics FY 1980-1989"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.justice.gov/sites/default/files/atr/legacy/2011/09/13/215423.pdf",
+                    "format": "pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Antitrust Division Workload Statistics FY 1980-1989"
+                }
+            ],
+            "identifier": "8",
+            "isPartOf": "4",
+            "issued": "2006-07-24T00:00:00",
             "keyword": [
                 "Workload Statistics",
                 "Department of Justice",
@@ -510,60 +519,59 @@
                 "civil case",
                 "criminal case"
             ],
-            "bureauCode": [
-                "011:00"
+            "landingPage": "https://www.justice.gov/atr/division-operations",
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-09-13T00:00:00",
             "programCode": [
                 "011:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Antitrust Division",
+                "subOrganizationOf": {
+                    "acronym": "DOJ",
+                    "id": 10,
+                    "name": "Department of Justice"
+                }
+            },
             "spatial": "United States and International Territories",
             "temporal": "1979-10-01T00:00:00.0000000/1989-09-30T00:00:00.0000000",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "4",
-            "dataQuality": false,
-            "issued": "2006-07-24T00:00:00",
-            "language": [
-                "eng"
+            "title": "Antitrust Division Workload Statistics FY 1980-1989"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:00"
             ],
-            "landingPage": "https://www.justice.gov/atr/division-operations",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Richard Hess",
+                "hasEmail": "mailto:richard.hess2@usdoj.gov"
+            },
+            "dataQuality": false,
+            "description": "This dataset summarizes the Antitrust Division workload activities for fiscal years 1970-1979.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.justice.gov/atr/antitrust-division-workload-statistics-fy-1980-1989",
+                    "accessURL": "https://www.justice.gov/atr/antitrust-division-workload-statistics-fy-1970-1979",
                     "format": "html",
                     "mediaType": "text/html",
-                    "title": "Antitrust Division Workload Statistics FY 1980-1989"
+                    "title": "Antitrust Division Workload Statistics FY 1970-1979"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.justice.gov/sites/default/files/atr/legacy/2011/09/13/215423.pdf",
-                    "format": "pdf",
+                    "downloadURL": "https://www.justice.gov/sites/default/files/atr/legacy/2009/06/09/215792.pdf",
                     "mediaType": "application/pdf",
-                    "title": "Antitrust Division Workload Statistics FY 1980-1989"
+                    "title": "Antitrust Division Workload Statistics FY 1970-1979"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Antitrust Division Workload Statistics FY 1970-1979",
-            "description": "This dataset summarizes the Antitrust Division workload activities for fiscal years 1970-1979.",
-            "modified": "2016-11-28T00:00:00",
-            "accessLevel": "public",
+            ],
             "identifier": "9",
-            "publisher": {
-                "name": "Antitrust Division",
-                "@type": "org:Organization",
-                "subOrganizationOf": {
-                    "id": 10,
-                    "acronym": "DOJ",
-                    "name": "Department of Justice"
-                }
-            },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Richard Hess",
-                "hasEmail": "mailto:richard.hess2@usdoj.gov"
-            },
+            "isPartOf": "4",
+            "issued": "2006-07-24T00:00:00",
             "keyword": [
                 "Workload Statistics",
                 "Department of Justice",
@@ -581,59 +589,58 @@
                 "civil case",
                 "criminal case"
             ],
-            "bureauCode": [
-                "011:00"
+            "landingPage": "https://www.justice.gov/atr/division-operations",
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-11-28T00:00:00",
             "programCode": [
                 "011:022"
             ],
-            "spatial": "United States and International Territories",
-            "temporal": "1969-10-01T00:00:00.0000000/1979-09-30T00:00:00.0000000",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "4",
-            "dataQuality": false,
-            "issued": "2006-07-24T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "landingPage": "https://www.justice.gov/atr/division-operations",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.justice.gov/atr/antitrust-division-workload-statistics-fy-1970-1979",
-                    "format": "html",
-                    "mediaType": "text/html",
-                    "title": "Antitrust Division Workload Statistics FY 1970-1979"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.justice.gov/sites/default/files/atr/legacy/2009/06/09/215792.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Antitrust Division Workload Statistics FY 1970-1979"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Antitrust Division Appropriation Figures Since Fiscal Year 1903",
-            "description": "This dataset contains five elements for Antitrust Division Appropriation Figures since Fiscal Year 1903: Fiscal year; Direct Appropriation Amount Included in Appropriations Bill; Filing Fee Revenue Amount; Total Funding Appropriated; and Notes. (Amounts are reported as $ in thousands).",
-            "modified": "2023-02-01T00:00:00",
-            "accessLevel": "public",
-            "identifier": "10",
             "publisher": {
-                "name": "Antitrust Division",
                 "@type": "org:Organization",
+                "name": "Antitrust Division",
                 "subOrganizationOf": {
-                    "id": 10,
                     "acronym": "DOJ",
+                    "id": 10,
                     "name": "Department of Justice"
                 }
             },
+            "spatial": "United States and International Territories",
+            "temporal": "1969-10-01T00:00:00.0000000/1979-09-30T00:00:00.0000000",
+            "title": "Antitrust Division Workload Statistics FY 1970-1979"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "011:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Richard Hess",
                 "hasEmail": "mailto:richard.hess2@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This dataset contains five elements for Antitrust Division Appropriation Figures since Fiscal Year 1903: Fiscal year; Direct Appropriation Amount Included in Appropriations Bill; Filing Fee Revenue Amount; Total Funding Appropriated; and Notes. (Amounts are reported as $ in thousands).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.justice.gov/media/1122916/dl?inline",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Antitrust Division Appropriation Figures Since Fiscal Year 1903"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.justice.gov/atr/appropriation-figures-antitrust-division",
+                    "mediaType": "text/html",
+                    "title": "Antitrust Division Appropriation Figures Since Fiscal Year 1903 (Webpage)"
+                }
+            ],
+            "identifier": "10",
+            "issued": "2015-10-27T00:00:00",
             "keyword": [
                 "Appropriation Figures",
                 "Appropriation",
@@ -648,56 +655,56 @@
                 "Notes",
                 "President's Budget Request"
             ],
-            "bureauCode": [
-                "011:00"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-02-01T00:00:00",
             "programCode": [
                 "011:022"
             ],
-            "spatial": "United States and International Territories",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "R/P1Y",
-            "dataQuality": false,
-            "issued": "2015-10-27T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.justice.gov/media/1122916/dl?inline",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "Antitrust Division Appropriation Figures Since Fiscal Year 1903"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.justice.gov/atr/appropriation-figures-antitrust-division",
-                    "mediaType": "text/html",
-                    "title": "Antitrust Division Appropriation Figures Since Fiscal Year 1903 (Webpage)"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Antitrust Division Workload Statistics FY 2010-2019",
-            "description": "This dataset summarizes the Antitrust Division workload activities for fiscal years 2010-2019.",
-            "modified": "2020-10-08T00:00:00",
-            "accessLevel": "public",
-            "identifier": "4309",
             "publisher": {
-                "name": "Antitrust Division",
                 "@type": "org:Organization",
+                "name": "Antitrust Division",
                 "subOrganizationOf": {
-                    "id": 10,
                     "acronym": "DOJ",
+                    "id": 10,
                     "name": "Department of Justice"
                 }
             },
+            "spatial": "United States and International Territories",
+            "title": "Antitrust Division Appropriation Figures Since Fiscal Year 1903"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Richard Hess",
                 "hasEmail": "mailto:richard.hess2@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This dataset summarizes the Antitrust Division workload activities for fiscal years 2010-2019.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.justice.gov/atr/file/788426/download",
+                    "mediaType": "application/pdf",
+                    "title": "Antitrust Division Workload Statistics FY 2010-2019"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.justice.gov/atr/file/788421/download",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Antitrust Division Workload Statistics FY 2010-2019 Excel"
+                }
+            ],
+            "identifier": "4309",
+            "isPartOf": "4",
+            "issued": "2020-10-08T00:00:00",
             "keyword": [
                 "Workload Statistics",
                 "Department of Justice",
@@ -715,63 +722,50 @@
                 "civil case",
                 "criminal case"
             ],
-            "bureauCode": [
-                "011:00"
+            "landingPage": "https://www.justice.gov/atr/division-operations",
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2020-10-08T00:00:00",
             "programCode": [
                 "011:022"
             ],
-            "temporal": "2009-10-01T00:00:00.0000000/2019-09-30T00:00:00.0000000",
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "4",
-            "dataQuality": false,
-            "issued": "2020-10-08T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "landingPage": "https://www.justice.gov/atr/division-operations",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.justice.gov/atr/file/788426/download",
-                    "mediaType": "application/pdf",
-                    "title": "Antitrust Division Workload Statistics FY 2010-2019"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.justice.gov/atr/file/788421/download",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "Antitrust Division Workload Statistics FY 2010-2019 Excel"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Parole Survey, 2000",
-            "description": "The 2000 Annual Parole Survey provides a count of the\r\ntotal number of persons supervised in the community on January 1 and\r\nDecember 31, 2000, and a count of the number entering and leaving\r\nsupervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and cause of death. This survey covers all 50 states, the District of Columbia, and the Federal System.",
-            "modified": "2013-05-07T15:10:36",
-            "accessLevel": "public",
-            "identifier": "11",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Antitrust Division",
                 "subOrganizationOf": {
-                    "id": 22,
-                    "acronym": "OJP",
-                    "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
-                    "parentOrganization": {
-                        "id": 10,
                     "acronym": "DOJ",
+                    "id": 10,
                     "name": "Department of Justice"
                 }
-                }
             },
+            "temporal": "2009-10-01T00:00:00.0000000/2019-09-30T00:00:00.0000000",
+            "title": "Antitrust Division Workload Statistics FY 2010-2019"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2000 Annual Parole Survey provides a count of the\r\ntotal number of persons supervised in the community on January 1 and\r\nDecember 31, 2000, and a count of the number entering and leaving\r\nsupervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and cause of death. This survey covers all 50 states, the District of Columbia, and the Federal System.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR31325.v1",
+                    "title": "Annual Parole Survey, 2000"
+                }
+            ],
+            "identifier": "11",
+            "isPartOf": "2631",
+            "issued": "2013-05-07T15:10:36",
             "keyword": [
                 "causes of death",
                 "criminal justice system",
@@ -780,54 +774,54 @@
                 "parolees",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-05-07T15:10:36",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2631",
-            "dataQuality": false,
-            "issued": "2013-05-07T15:10:36",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR31325.v1",
-                    "title": "Annual Parole Survey, 2000"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Parole Survey, 2001",
-            "description": "The 2001 Annual Parole Survey provides a count of the\r\ntotal number of persons supervised in the community on January 1 and\r\nDecember 31, 2001, and a count of the number entering and leaving\r\nsupervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, and supervision status. This survey covers all 50 states, the District of Columbia, and the Federal System.",
-            "modified": "2013-05-08T14:22:49",
-            "accessLevel": "public",
-            "identifier": "12",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Parole Survey, 2000"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2001 Annual Parole Survey provides a count of the\r\ntotal number of persons supervised in the community on January 1 and\r\nDecember 31, 2001, and a count of the number entering and leaving\r\nsupervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, and supervision status. This survey covers all 50 states, the District of Columbia, and the Federal System.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR31326.v1",
+                    "title": "Annual Parole Survey, 2001"
+                }
+            ],
+            "identifier": "12",
+            "isPartOf": "2631",
+            "issued": "2013-05-08T14:22:49",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -835,54 +829,54 @@
                 "parolees",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-05-08T14:22:49",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2631",
-            "dataQuality": false,
-            "issued": "2013-05-08T14:22:49",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR31326.v1",
-                    "title": "Annual Parole Survey, 2001"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Parole Survey, 2002",
-            "description": "The 2002 Annual Parole Survey provides a count of the\r\ntotal number of persons supervised in the community on January 1 and\r\nDecember 31, 2002, and a count of the number entering and leaving\r\nsupervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and type of offense. This survey covers all 50 states, the District of Columbia, and the Federal System.",
-            "modified": "2013-05-10T10:29:05",
-            "accessLevel": "public",
-            "identifier": "13",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Parole Survey, 2001"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2002 Annual Parole Survey provides a count of the\r\ntotal number of persons supervised in the community on January 1 and\r\nDecember 31, 2002, and a count of the number entering and leaving\r\nsupervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and type of offense. This survey covers all 50 states, the District of Columbia, and the Federal System.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR31327.v1",
+                    "title": "Annual Parole Survey, 2002"
+                }
+            ],
+            "identifier": "13",
+            "isPartOf": "2631",
+            "issued": "2013-05-10T10:29:05",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -890,54 +884,54 @@
                 "parolees",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-05-10T10:29:05",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2631",
-            "dataQuality": false,
-            "issued": "2013-05-10T10:29:05",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR31327.v1",
-                    "title": "Annual Parole Survey, 2002"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Parole Survey, 2003",
-            "description": "The 2003 Annual Parole Survey provides a count of the\r\ntotal number of persons supervised in the community on January 1 and\r\nDecember 31, 2003, and a count of the number entering and leaving\r\nsupervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and type of offense. This survey covers all 50 states, the District of Columbia, and the Federal System.",
-            "modified": "2013-05-10T10:32:34",
-            "accessLevel": "public",
-            "identifier": "14",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Parole Survey, 2002"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2003 Annual Parole Survey provides a count of the\r\ntotal number of persons supervised in the community on January 1 and\r\nDecember 31, 2003, and a count of the number entering and leaving\r\nsupervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and type of offense. This survey covers all 50 states, the District of Columbia, and the Federal System.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR31328.v1",
+                    "title": "Annual Parole Survey, 2003"
+                }
+            ],
+            "identifier": "14",
+            "isPartOf": "2631",
+            "issued": "2013-05-10T10:32:34",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -945,54 +939,54 @@
                 "parolees",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-05-10T10:32:34",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2631",
-            "dataQuality": false,
-            "issued": "2013-05-10T10:32:34",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR31328.v1",
-                    "title": "Annual Parole Survey, 2003"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Parole Survey, 2004",
-            "description": "The 2004 Annual Parole Survey provides a count of the\r\ntotal number of persons supervised in the community on January 1 and\r\nDecember 31, 2004, and a count of the number entering and leaving\r\nsupervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and type of offense. This survey covers all 50 states, the District of Columbia, and the Federal System.",
-            "modified": "2013-05-16T10:28:05",
-            "accessLevel": "public",
-            "identifier": "15",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Parole Survey, 2003"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2004 Annual Parole Survey provides a count of the\r\ntotal number of persons supervised in the community on January 1 and\r\nDecember 31, 2004, and a count of the number entering and leaving\r\nsupervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and type of offense. This survey covers all 50 states, the District of Columbia, and the Federal System.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR31329.v1",
+                    "title": "Annual Parole Survey, 2004"
+                }
+            ],
+            "identifier": "15",
+            "isPartOf": "2631",
+            "issued": "2013-05-16T10:28:05",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -1000,54 +994,54 @@
                 "parolees",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-05-16T10:28:05",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2631",
-            "dataQuality": false,
-            "issued": "2013-05-16T10:28:05",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR31329.v1",
-                    "title": "Annual Parole Survey, 2004"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Parole Survey, 2005",
-            "description": "The 2005 Annual Parole Survey provides a count of the\r\ntotal number of persons supervised in the community on January 1 and\r\nDecember 31, 2005, and a count of the number entering and leaving\r\nsupervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and type of offense. This survey covers all 50 states, the District of Columbia, and the Federal System.",
-            "modified": "2013-05-15T11:10:57",
-            "accessLevel": "public",
-            "identifier": "16",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Parole Survey, 2004"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2005 Annual Parole Survey provides a count of the\r\ntotal number of persons supervised in the community on January 1 and\r\nDecember 31, 2005, and a count of the number entering and leaving\r\nsupervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and type of offense. This survey covers all 50 states, the District of Columbia, and the Federal System.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR31330.v1",
+                    "title": "Annual Parole Survey, 2005"
+                }
+            ],
+            "identifier": "16",
+            "isPartOf": "2631",
+            "issued": "2013-05-15T11:10:57",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -1055,54 +1049,54 @@
                 "parolees",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-05-15T11:10:57",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2631",
-            "dataQuality": false,
-            "issued": "2013-05-15T11:10:57",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR31330.v1",
-                    "title": "Annual Parole Survey, 2005"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Parole Survey, 2006",
-            "description": "The 2006 Annual Parole Survey provides a count of the\r\ntotal number of persons supervised in the community on January 1 and\r\nDecember 31, 2006, and a count of the number entering and leaving\r\nsupervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and type of offense. This survey covers all 50 states, the District of Columbia, and the Federal System.",
-            "modified": "2013-05-16T10:29:14",
-            "accessLevel": "public",
-            "identifier": "17",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Parole Survey, 2005"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2006 Annual Parole Survey provides a count of the\r\ntotal number of persons supervised in the community on January 1 and\r\nDecember 31, 2006, and a count of the number entering and leaving\r\nsupervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and type of offense. This survey covers all 50 states, the District of Columbia, and the Federal System.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR31331.v1",
+                    "title": "Annual Parole Survey, 2006"
+                }
+            ],
+            "identifier": "17",
+            "isPartOf": "2631",
+            "issued": "2013-05-16T10:29:14",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -1110,54 +1104,54 @@
                 "parolees",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-05-16T10:29:14",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2631",
-            "dataQuality": false,
-            "issued": "2013-05-16T10:29:14",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR31331.v1",
-                    "title": "Annual Parole Survey, 2006"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Parole Survey, 2007",
-            "description": "The 2007 Annual Parole Survey provides a count of the\r\ntotal number of persons supervised in the community on January 1 and\r\nDecember 31, 2007, and a count of the number entering and leaving\r\nsupervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and type of offense. This survey covers all 50 states, the District of Columbia, and the Federal System.",
-            "modified": "2013-05-24T10:23:54",
-            "accessLevel": "public",
-            "identifier": "18",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Parole Survey, 2006"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2007 Annual Parole Survey provides a count of the\r\ntotal number of persons supervised in the community on January 1 and\r\nDecember 31, 2007, and a count of the number entering and leaving\r\nsupervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and type of offense. This survey covers all 50 states, the District of Columbia, and the Federal System.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR31332.v1",
+                    "title": "Annual Parole Survey, 2007"
+                }
+            ],
+            "identifier": "18",
+            "isPartOf": "2631",
+            "issued": "2013-05-24T10:23:54",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -1165,54 +1159,54 @@
                 "parolees",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-05-24T10:23:54",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2631",
-            "dataQuality": false,
-            "issued": "2013-05-24T10:23:54",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR31332.v1",
-                    "title": "Annual Parole Survey, 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Parole Survey, 2008",
-            "description": "The 2008 Annual Parole Survey provides a count of the\r\ntotal number of persons supervised in the community on January 1 and\r\nDecember 31, 2008, and a count of the number entering and leaving\r\nsupervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and type of offense. This survey covers all 50 states, the District of Columbia, and the Federal System.",
-            "modified": "2013-05-31T10:37:05",
-            "accessLevel": "public",
-            "identifier": "19",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Parole Survey, 2007"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2008 Annual Parole Survey provides a count of the\r\ntotal number of persons supervised in the community on January 1 and\r\nDecember 31, 2008, and a count of the number entering and leaving\r\nsupervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and type of offense. This survey covers all 50 states, the District of Columbia, and the Federal System.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34380.v1",
+                    "title": "Annual Parole Survey, 2008"
+                }
+            ],
+            "identifier": "19",
+            "isPartOf": "2631",
+            "issued": "2013-05-31T10:37:05",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -1220,54 +1214,54 @@
                 "parolees",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-05-31T10:37:05",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2631",
-            "dataQuality": false,
-            "issued": "2013-05-31T10:37:05",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34380.v1",
-                    "title": "Annual Parole Survey, 2008"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Parole Survey, 2009",
-            "description": "The 2009 Annual Parole Survey provides a count of the\r\ntotal number of persons supervised in the community on January 1 and\r\nDecember 31, 2009, and a count of the number entering and leaving\r\nsupervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and type of offense. This survey covers all 50 states, the District of Columbia, and the Federal System.",
-            "modified": "2013-05-30T12:03:49",
-            "accessLevel": "public",
-            "identifier": "20",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Parole Survey, 2008"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2009 Annual Parole Survey provides a count of the\r\ntotal number of persons supervised in the community on January 1 and\r\nDecember 31, 2009, and a count of the number entering and leaving\r\nsupervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and type of offense. This survey covers all 50 states, the District of Columbia, and the Federal System.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34381.v1",
+                    "title": "Annual Parole Survey, 2009"
+                }
+            ],
+            "identifier": "20",
+            "isPartOf": "2631",
+            "issued": "2013-05-30T12:03:49",
             "keyword": [
                 "Hispanic or Latino origins",
                 "criminal justice system",
@@ -1276,54 +1270,54 @@
                 "parolees",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-05-30T12:03:49",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2631",
-            "dataQuality": false,
-            "issued": "2013-05-30T12:03:49",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34381.v1",
-                    "title": "Annual Parole Survey, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Parole Survey, 2010",
-            "description": "The 2010 Annual Parole Survey provides a count of the\r\ntotal number of persons supervised in the community on January 1 and\r\nDecember 31, 2010, and a count of the number entering and leaving\r\nsupervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and type of offense. This survey covers all 50 states, the District of Columbia, and the Federal System.",
-            "modified": "2013-05-31T10:38:32",
-            "accessLevel": "public",
-            "identifier": "21",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Parole Survey, 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2010 Annual Parole Survey provides a count of the\r\ntotal number of persons supervised in the community on January 1 and\r\nDecember 31, 2010, and a count of the number entering and leaving\r\nsupervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and type of offense. This survey covers all 50 states, the District of Columbia, and the Federal System.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34382.v1",
+                    "title": "Annual Parole Survey, 2010"
+                }
+            ],
+            "identifier": "21",
+            "isPartOf": "2631",
+            "issued": "2013-05-31T10:38:32",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -1331,54 +1325,54 @@
                 "parolees",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-05-31T10:38:32",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2631",
-            "dataQuality": false,
-            "issued": "2013-05-31T10:38:32",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34382.v1",
-                    "title": "Annual Parole Survey, 2010"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Parole Survey, 2011",
-            "description": "The 2011 Annual Parole Survey provides a count of the\r\ntotal number of persons supervised in the community on January 1 and\r\nDecember 31, 2011, and a count of the number entering and leaving\r\nsupervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and type of offense. This survey covers all 50 states, the District of Columbia, and the Federal System.",
-            "modified": "2013-10-28T10:30:14",
-            "accessLevel": "public",
-            "identifier": "22",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Parole Survey, 2010"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2011 Annual Parole Survey provides a count of the\r\ntotal number of persons supervised in the community on January 1 and\r\nDecember 31, 2011, and a count of the number entering and leaving\r\nsupervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and type of offense. This survey covers all 50 states, the District of Columbia, and the Federal System.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34718.v1",
+                    "title": "Annual Parole Survey, 2011"
+                }
+            ],
+            "identifier": "22",
+            "isPartOf": "2631",
+            "issued": "2013-10-28T10:30:14",
             "keyword": [
                 "causes of death",
                 "criminal justice system",
@@ -1387,54 +1381,54 @@
                 "parolees",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-10-28T10:30:14",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2631",
-            "dataQuality": false,
-            "issued": "2013-10-28T10:30:14",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34718.v1",
-                    "title": "Annual Parole Survey, 2011"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Probation Survey, 1994",
-            "description": "The 1994 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 1994, and a count of the number of persons entering and exiting probation supervision during 1994. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race and Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
-            "modified": "2012-12-10T11:48:36",
-            "accessLevel": "public",
-            "identifier": "23",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Parole Survey, 2011"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 1994 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 1994, and a count of the number of persons entering and exiting probation supervision during 1994. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race and Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR29668.v2",
+                    "title": "Annual Probation Survey, 1994"
+                }
+            ],
+            "identifier": "23",
+            "isPartOf": "2444",
+            "issued": "2011-06-22T18:02:48",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -1442,54 +1436,54 @@
                 "probationers",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2012-12-10T11:48:36",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2444",
-            "dataQuality": false,
-            "issued": "2011-06-22T18:02:48",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR29668.v2",
-                    "title": "Annual Probation Survey, 1994"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Probation Survey, 1995",
-            "description": "The 1995 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 1995, and a count of the number of persons entering and exiting probation supervision during 1995. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race and Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
-            "modified": "2013-02-14T16:16:46",
-            "accessLevel": "public",
-            "identifier": "24",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Probation Survey, 1994"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 1995 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 1995, and a count of the number of persons entering and exiting probation supervision during 1995. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race and Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR29669.v2",
+                    "title": "Annual Probation Survey, 1995"
+                }
+            ],
+            "identifier": "24",
+            "isPartOf": "2444",
+            "issued": "2011-06-22T18:04:14",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -1497,54 +1491,54 @@
                 "probationers",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-02-14T16:16:46",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2444",
-            "dataQuality": false,
-            "issued": "2011-06-22T18:04:14",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR29669.v2",
-                    "title": "Annual Probation Survey, 1995"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Probation Survey, 1996",
-            "description": "The 1996 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 1996, and a count of the number of persons entering and exiting probation supervision during 1996. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race and Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
-            "modified": "2013-02-14T16:18:13",
-            "accessLevel": "public",
-            "identifier": "25",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Probation Survey, 1995"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 1996 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 1996, and a count of the number of persons entering and exiting probation supervision during 1996. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race and Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR29670.v2",
+                    "title": "Annual Probation Survey, 1996"
+                }
+            ],
+            "identifier": "25",
+            "isPartOf": "2444",
+            "issued": "2011-06-22T18:05:29",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -1552,54 +1546,54 @@
                 "probationers",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-02-14T16:18:13",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2444",
-            "dataQuality": false,
-            "issued": "2011-06-22T18:05:29",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR29670.v2",
-                    "title": "Annual Probation Survey, 1996"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Probation Survey, 1997",
-            "description": "The 1997 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 1997, and a count of the number of persons entering and exiting probation supervision during 1997. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race and Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
-            "modified": "2013-02-14T16:19:15",
-            "accessLevel": "public",
-            "identifier": "26",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Probation Survey, 1996"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 1997 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 1997, and a count of the number of persons entering and exiting probation supervision during 1997. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race and Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR29671.v2",
+                    "title": "Annual Probation Survey, 1997"
+                }
+            ],
+            "identifier": "26",
+            "isPartOf": "2444",
+            "issued": "2011-06-22T18:07:08",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -1607,54 +1601,54 @@
                 "probationers",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-02-14T16:19:15",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2444",
-            "dataQuality": false,
-            "issued": "2011-06-22T18:07:08",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR29671.v2",
-                    "title": "Annual Probation Survey, 1997"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Probation Survey, 1998",
-            "description": "The 1998 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 1998, and a count of the number of persons entering and exiting probation supervision during 1998. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race and Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
-            "modified": "2013-02-14T16:22:37",
-            "accessLevel": "public",
-            "identifier": "27",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Probation Survey, 1997"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 1998 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 1998, and a count of the number of persons entering and exiting probation supervision during 1998. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race and Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR29672.v2",
+                    "title": "Annual Probation Survey, 1998"
+                }
+            ],
+            "identifier": "27",
+            "isPartOf": "2444",
+            "issued": "2011-06-22T18:08:54",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -1662,54 +1656,54 @@
                 "probationers",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-02-14T16:22:37",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2444",
-            "dataQuality": false,
-            "issued": "2011-06-22T18:08:54",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR29672.v2",
-                    "title": "Annual Probation Survey, 1998"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Probation Survey, 1999",
-            "description": "The 1999 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 1999, and a count of the number of persons entering and exiting probation supervision during 1999. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race and Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
-            "modified": "2013-02-14T16:22:59",
-            "accessLevel": "public",
-            "identifier": "28",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Probation Survey, 1998"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 1999 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 1999, and a count of the number of persons entering and exiting probation supervision during 1999. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race and Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR29673.v2",
+                    "title": "Annual Probation Survey, 1999"
+                }
+            ],
+            "identifier": "28",
+            "isPartOf": "2444",
+            "issued": "2011-06-22T18:10:04",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -1717,54 +1711,54 @@
                 "probationers",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-02-14T16:22:59",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2444",
-            "dataQuality": false,
-            "issued": "2011-06-22T18:10:04",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR29673.v2",
-                    "title": "Annual Probation Survey, 1999"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Probation Survey, 2000",
-            "description": "The 2000 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2000, and a count of the number of persons entering and exiting probation supervision during 2000. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race and Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
-            "modified": "2013-02-26T09:21:55",
-            "accessLevel": "public",
-            "identifier": "29",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Probation Survey, 1999"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2000 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2000, and a count of the number of persons entering and exiting probation supervision during 2000. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race and Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR28361.v1",
+                    "title": "Annual Probation Survey, 2000"
+                }
+            ],
+            "identifier": "29",
+            "isPartOf": "2444",
+            "issued": "2013-02-26T09:21:55",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -1772,54 +1766,54 @@
                 "probationers",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-02-26T09:21:55",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2444",
-            "dataQuality": false,
-            "issued": "2013-02-26T09:21:55",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR28361.v1",
-                    "title": "Annual Probation Survey, 2000"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Probation Survey, 2001",
-            "description": "The 2001 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2001, and a count of the number of persons entering and exiting probation supervision during 2001. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race and Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
-            "modified": "2013-02-26T09:24:46",
-            "accessLevel": "public",
-            "identifier": "30",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Probation Survey, 2000"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2001 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2001, and a count of the number of persons entering and exiting probation supervision during 2001. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race and Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR28362.v1",
+                    "title": "Annual Probation Survey, 2001"
+                }
+            ],
+            "identifier": "30",
+            "isPartOf": "2444",
+            "issued": "2013-02-26T09:24:46",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -1827,54 +1821,54 @@
                 "probationers",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-02-26T09:24:46",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2444",
-            "dataQuality": false,
-            "issued": "2013-02-26T09:24:46",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR28362.v1",
-                    "title": "Annual Probation Survey, 2001"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Probation Survey, 2002",
-            "description": "The 2002 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2002, and a count of the number of persons entering and exiting probation supervision during 2002. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race and Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
-            "modified": "2013-02-26T09:27:07",
-            "accessLevel": "public",
-            "identifier": "31",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Probation Survey, 2001"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2002 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2002, and a count of the number of persons entering and exiting probation supervision during 2002. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race and Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR28363.v1",
+                    "title": "Annual Probation Survey, 2002"
+                }
+            ],
+            "identifier": "31",
+            "isPartOf": "2444",
+            "issued": "2013-02-26T09:27:07",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -1882,54 +1876,54 @@
                 "probationers",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-02-26T09:27:07",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2444",
-            "dataQuality": false,
-            "issued": "2013-02-26T09:27:07",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR28363.v1",
-                    "title": "Annual Probation Survey, 2002"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Probation Survey, 2003",
-            "description": "The 2003 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2003, and a count of the number of persons entering and exiting probation supervision during 2003. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race and Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
-            "modified": "2013-02-26T13:08:40",
-            "accessLevel": "public",
-            "identifier": "32",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Probation Survey, 2002"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2003 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2003, and a count of the number of persons entering and exiting probation supervision during 2003. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race and Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR28364.v1",
+                    "title": "Annual Probation Survey, 2003"
+                }
+            ],
+            "identifier": "32",
+            "isPartOf": "2444",
+            "issued": "2013-02-26T13:08:40",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -1937,54 +1931,54 @@
                 "probationers",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-02-26T13:08:40",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2444",
-            "dataQuality": false,
-            "issued": "2013-02-26T13:08:40",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR28364.v1",
-                    "title": "Annual Probation Survey, 2003"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Probation Survey, 2004",
-            "description": "The 2004 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2004, and a count of the number of persons entering and exiting probation supervision during 2004. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race and Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
-            "modified": "2013-03-06T13:30:51",
-            "accessLevel": "public",
-            "identifier": "33",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Probation Survey, 2003"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2004 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2004, and a count of the number of persons entering and exiting probation supervision during 2004. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race and Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR28365.v1",
+                    "title": "Annual Probation Survey, 2004"
+                }
+            ],
+            "identifier": "33",
+            "isPartOf": "2444",
+            "issued": "2013-03-06T13:30:51",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -1992,54 +1986,54 @@
                 "probationers",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-03-06T13:30:51",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2444",
-            "dataQuality": false,
-            "issued": "2013-03-06T13:30:51",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR28365.v1",
-                    "title": "Annual Probation Survey, 2004"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Probation Survey, 2005",
-            "description": "The 2005 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2005, and a count of the number of persons entering and exiting probation supervision during 2005. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race and Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
-            "modified": "2013-03-06T13:32:27",
-            "accessLevel": "public",
-            "identifier": "34",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Probation Survey, 2004"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2005 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2005, and a count of the number of persons entering and exiting probation supervision during 2005. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race and Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR28366.v1",
+                    "title": "Annual Probation Survey, 2005"
+                }
+            ],
+            "identifier": "34",
+            "isPartOf": "2444",
+            "issued": "2013-03-06T13:32:27",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -2047,54 +2041,54 @@
                 "probationers",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-03-06T13:32:27",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2444",
-            "dataQuality": false,
-            "issued": "2013-03-06T13:32:27",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR28366.v1",
-                    "title": "Annual Probation Survey, 2005"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Probation Survey, 2006",
-            "description": "The 2006 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2006, and a count of the number of persons entering and exiting probation supervision during 2006. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race, Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
-            "modified": "2013-03-08T10:14:51",
-            "accessLevel": "public",
-            "identifier": "35",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Probation Survey, 2005"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2006 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2006, and a count of the number of persons entering and exiting probation supervision during 2006. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race, Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR31323.v1",
+                    "title": "Annual Probation Survey, 2006"
+                }
+            ],
+            "identifier": "35",
+            "isPartOf": "2444",
+            "issued": "2013-03-08T10:14:51",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -2102,54 +2096,54 @@
                 "probationers",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-03-08T10:14:51",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2444",
-            "dataQuality": false,
-            "issued": "2013-03-08T10:14:51",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR31323.v1",
-                    "title": "Annual Probation Survey, 2006"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Probation Survey, 2007",
-            "description": "The 2007 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2007, and a count of the number of persons entering and exiting probation supervision during 2007. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race, Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
-            "modified": "2013-03-08T10:16:58",
-            "accessLevel": "public",
-            "identifier": "36",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Probation Survey, 2006"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2007 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2007, and a count of the number of persons entering and exiting probation supervision during 2007. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race, Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR31324.v1",
+                    "title": "Annual Probation Survey, 2007"
+                }
+            ],
+            "identifier": "36",
+            "isPartOf": "2444",
+            "issued": "2013-03-08T10:16:58",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -2157,54 +2151,54 @@
                 "probationers",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-03-08T10:16:58",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2444",
-            "dataQuality": false,
-            "issued": "2013-03-08T10:16:58",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR31324.v1",
-                    "title": "Annual Probation Survey, 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Probation Survey, 2008",
-            "description": "The 2008 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2008, and a count of the number of persons entering and exiting probation supervision during 2008. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race, Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
-            "modified": "2013-03-22T11:16:28",
-            "accessLevel": "public",
-            "identifier": "37",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Probation Survey, 2007"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2008 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2008, and a count of the number of persons entering and exiting probation supervision during 2008. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race, Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34319.v1",
+                    "title": "Annual Probation Survey, 2008"
+                }
+            ],
+            "identifier": "37",
+            "isPartOf": "2444",
+            "issued": "2013-03-22T11:16:28",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -2212,54 +2206,54 @@
                 "probationers",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-03-22T11:16:28",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2444",
-            "dataQuality": false,
-            "issued": "2013-03-22T11:16:28",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34319.v1",
-                    "title": "Annual Probation Survey, 2008"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Probation Survey, 2009",
-            "description": "The 2009 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2009, and a count of the number of persons entering and exiting probation supervision during 2009. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race, Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
-            "modified": "2013-03-21T10:00:22",
-            "accessLevel": "public",
-            "identifier": "38",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Probation Survey, 2008"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2009 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2009, and a count of the number of persons entering and exiting probation supervision during 2009. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race, Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34320.v1",
+                    "title": "Annual Probation Survey, 2009"
+                }
+            ],
+            "identifier": "38",
+            "isPartOf": "2444",
+            "issued": "2013-03-21T10:00:22",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -2267,54 +2261,54 @@
                 "probationers",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-03-21T10:00:22",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2444",
-            "dataQuality": false,
-            "issued": "2013-03-21T10:00:22",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34320.v1",
-                    "title": "Annual Probation Survey, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Probation Survey, 2010",
-            "description": "The 2010 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2010, and a count of the number of persons entering and exiting probation supervision during 2010. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race, Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
-            "modified": "2013-03-27T13:40:54",
-            "accessLevel": "public",
-            "identifier": "39",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Probation Survey, 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2010 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2010, and a count of the number of persons entering and exiting probation supervision during 2010. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race, Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34321.v1",
+                    "title": "Annual Probation Survey, 2010"
+                }
+            ],
+            "identifier": "39",
+            "isPartOf": "2444",
+            "issued": "2013-03-27T13:40:54",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -2322,54 +2316,54 @@
                 "probationers",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-03-27T13:40:54",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2444",
-            "dataQuality": false,
-            "issued": "2013-03-27T13:40:54",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34321.v1",
-                    "title": "Annual Probation Survey, 2010"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Probation Survey, 2011",
-            "description": "The 2011 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2011, and a count of the number of persons entering and exiting probation supervision during 2011. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race, Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
-            "modified": "2013-10-31T10:41:34",
-            "accessLevel": "public",
-            "identifier": "40",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Probation Survey, 2010"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2011 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2011, and a count of the number of persons entering and exiting probation supervision during 2011. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race, Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34717.v1",
+                    "title": "Annual Probation Survey, 2011"
+                }
+            ],
+            "identifier": "40",
+            "isPartOf": "2444",
+            "issued": "2013-10-31T10:41:34",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -2377,54 +2371,54 @@
                 "probationers",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-10-31T10:41:34",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2444",
-            "dataQuality": false,
-            "issued": "2013-10-31T10:41:34",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34717.v1",
-                    "title": "Annual Probation Survey, 2011"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails in Indian Country, 1998:  [United States]  ",
-            "description": "The objective of the Survey of Jails in Indian Country is to\r\n gather data on all adult and juvenile jail facilities and detention\r\n centers in Indian country, which is defined for purposes of this\r\n collection as reservations, pueblos, rancherias, and other\r\n Native American and Alaska Native communities throughout the United\r\n States. The survey, a complete enumeration of all 69 confinement\r\n facilities operated by tribal authorities or by the Bureau of Indian\r\n Affairs (BIA), provides data on number of inmates, staffing, and\r\n facility characteristics and needs. Variables describe each facility,\r\n including who operated it, facility age, facility function, rated\r\n capacity, authority to house juveniles, number of juveniles held,\r\n number of admission and discharges in last 30 days, number of inmate\r\n deaths, peak population during June, number of inmates held by\r\n sex and conviction status on June 30, number of facility staff by sex\r\n and function, facility crowding, renovation and building plans, types\r\n of programs available to inmates, and overview of facility and\r\nstaffing needs.",
-            "modified": "2021-11-22T12:23:15",
-            "accessLevel": "restricted public",
-            "identifier": "41",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Probation Survey, 2011"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The objective of the Survey of Jails in Indian Country is to\r\n gather data on all adult and juvenile jail facilities and detention\r\n centers in Indian country, which is defined for purposes of this\r\n collection as reservations, pueblos, rancherias, and other\r\n Native American and Alaska Native communities throughout the United\r\n States. The survey, a complete enumeration of all 69 confinement\r\n facilities operated by tribal authorities or by the Bureau of Indian\r\n Affairs (BIA), provides data on number of inmates, staffing, and\r\n facility characteristics and needs. Variables describe each facility,\r\n including who operated it, facility age, facility function, rated\r\n capacity, authority to house juveniles, number of juveniles held,\r\n number of admission and discharges in last 30 days, number of inmate\r\n deaths, peak population during June, number of inmates held by\r\n sex and conviction status on June 30, number of facility staff by sex\r\n and function, facility crowding, renovation and building plans, types\r\n of programs available to inmates, and overview of facility and\r\nstaffing needs.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR02979.v2",
+                    "title": "Annual Survey of Jails in Indian Country, 1998:  [United States]  "
+                }
+            ],
+            "identifier": "41",
+            "isPartOf": "2435",
+            "issued": "2001-10-31T00:00:00",
             "keyword": [
                 "Native Americans",
                 "correctional facilities",
@@ -2434,55 +2428,55 @@
                 "jails",
                 "population characteristics"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-11-22T12:23:15",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2435",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2001-10-31T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR02979.v2",
-                    "title": "Annual Survey of Jails in Indian Country, 1998:  [United States]  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails in Indian Country, 1999:  [United States]  ",
-            "description": "The objective of the Survey of Jails in Indian Country is\r\n to gather data on all adult and juvenile jail facilities and detention\r\n centers in Indian country, which is defined for purposes of this\r\n collection as reservations, pueblos, rancherias, and other Native\r\n American and Alaska Native communities throughout the United States.\r\n The survey, a complete enumeration of all 69 confinement facilities\r\n operated by tribal authorities or the Bureau of Indian Affairs (BIA),\r\n provides data on number of inmates, staffing, and facility\r\n characteristics and needs. Variables describe each facility, including\r\n who operated it, facility age, facility function, rated capacity,\r\n authority to house juveniles, number of juveniles held, number of\r\n admission and discharges in last 30 days, number of inmate deaths, the\r\n peak population during June, number of inmates held by sex and\r\n conviction status on June 30, number of facility staff by sex and\r\n function, facility crowding, renovation and building plans, types of\r\n programs available to inmates, and overview of facility and staffing\r\nneeds.",
-            "modified": "2021-11-22T19:13:28",
-            "accessLevel": "restricted public",
-            "identifier": "42",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Annual Survey of Jails in Indian Country, 1998:  [United States]  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The objective of the Survey of Jails in Indian Country is\r\n to gather data on all adult and juvenile jail facilities and detention\r\n centers in Indian country, which is defined for purposes of this\r\n collection as reservations, pueblos, rancherias, and other Native\r\n American and Alaska Native communities throughout the United States.\r\n The survey, a complete enumeration of all 69 confinement facilities\r\n operated by tribal authorities or the Bureau of Indian Affairs (BIA),\r\n provides data on number of inmates, staffing, and facility\r\n characteristics and needs. Variables describe each facility, including\r\n who operated it, facility age, facility function, rated capacity,\r\n authority to house juveniles, number of juveniles held, number of\r\n admission and discharges in last 30 days, number of inmate deaths, the\r\n peak population during June, number of inmates held by sex and\r\n conviction status on June 30, number of facility staff by sex and\r\n function, facility crowding, renovation and building plans, types of\r\n programs available to inmates, and overview of facility and staffing\r\nneeds.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR02980.v2",
+                    "title": "Annual Survey of Jails in Indian Country, 1999:  [United States]  "
+                }
+            ],
+            "identifier": "42",
+            "isPartOf": "2435",
+            "issued": "2001-10-31T00:00:00",
             "keyword": [
                 "Native Americans",
                 "correctional facilities",
@@ -2492,55 +2486,55 @@
                 "jails",
                 "population characteristics"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-11-22T19:13:28",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2435",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2001-10-31T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR02980.v2",
-                    "title": "Annual Survey of Jails in Indian Country, 1999:  [United States]  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails in Indian Country, 2000:  [United States]    ",
-            "description": "The objective of the Survey of Jails in Indian Country is\r\n to gather data on all adult and juvenile jail facilities and detention\r\n centers in Indian country, which is defined for purposes of this\r\n collection as reservations, pueblos, rancherias, and other Native\r\n American and Alaska Native communities throughout the United\r\n States. The survey, a complete enumeration of all 69 confinement\r\n facilities operated by tribal authorities or the Bureau of Indian\r\n Affairs (BIA), provides data on the number of inmates and facility\r\n characteristics and needs. Variables describe each facility, including\r\n the rated capacity, number of adult inmates, number of juveniles held,\r\n number of inmates held by sex and conviction status on June 30, number\r\n of admissions and discharges in the last 30 days, number of inmate\r\n deaths, peak population during June, facility crowding, and renovation\r\nand building plans.",
-            "modified": "2021-11-22T19:08:08",
-            "accessLevel": "restricted public",
-            "identifier": "43",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Annual Survey of Jails in Indian Country, 1999:  [United States]  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The objective of the Survey of Jails in Indian Country is\r\n to gather data on all adult and juvenile jail facilities and detention\r\n centers in Indian country, which is defined for purposes of this\r\n collection as reservations, pueblos, rancherias, and other Native\r\n American and Alaska Native communities throughout the United\r\n States. The survey, a complete enumeration of all 69 confinement\r\n facilities operated by tribal authorities or the Bureau of Indian\r\n Affairs (BIA), provides data on the number of inmates and facility\r\n characteristics and needs. Variables describe each facility, including\r\n the rated capacity, number of adult inmates, number of juveniles held,\r\n number of inmates held by sex and conviction status on June 30, number\r\n of admissions and discharges in the last 30 days, number of inmate\r\n deaths, peak population during June, facility crowding, and renovation\r\nand building plans.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03196.v2",
+                    "title": "Annual Survey of Jails in Indian Country, 2000:  [United States]    "
+                }
+            ],
+            "identifier": "43",
+            "isPartOf": "2435",
+            "issued": "2001-11-14T00:00:00",
             "keyword": [
                 "Native Americans",
                 "correctional facilities",
@@ -2550,55 +2544,55 @@
                 "jails",
                 "population characteristics"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-11-22T19:08:08",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2435",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2001-11-14T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03196.v2",
-                    "title": "Annual Survey of Jails in Indian Country, 2000:  [United States]    "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails in Indian Country, 2001:  [United States]  ",
-            "description": "The objective of the Survey of Jails in Indian Country is\r\n to gather data on all adult and juvenile jail facilities and detention\r\n centers in Indian country, which is defined for purposes of this\r\n collection as reservations, pueblos, rancherias, and other Native\r\n American and Alaska Native communities throughout the United\r\n States. The survey, a complete enumeration of all 68 confinement\r\n facilities operated by tribal authorities or the Bureau of Indian\r\n Affairs (BIA), provides data on number of inmates and facility\r\n characteristics and needs. Variables describe each facility, including\r\n rated capacity, number of adult inmates, number of juveniles held,\r\n number of inmates held by sex and conviction status on June 29, number\r\n of admissions and discharges in the last 30 days, number of inmate\r\n deaths, the peak population during June, facility crowding, and\r\nrenovation and building plans.",
-            "modified": "2021-11-22T19:01:25",
-            "accessLevel": "restricted public",
-            "identifier": "44",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Annual Survey of Jails in Indian Country, 2000:  [United States]    "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The objective of the Survey of Jails in Indian Country is\r\n to gather data on all adult and juvenile jail facilities and detention\r\n centers in Indian country, which is defined for purposes of this\r\n collection as reservations, pueblos, rancherias, and other Native\r\n American and Alaska Native communities throughout the United\r\n States. The survey, a complete enumeration of all 68 confinement\r\n facilities operated by tribal authorities or the Bureau of Indian\r\n Affairs (BIA), provides data on number of inmates and facility\r\n characteristics and needs. Variables describe each facility, including\r\n rated capacity, number of adult inmates, number of juveniles held,\r\n number of inmates held by sex and conviction status on June 29, number\r\n of admissions and discharges in the last 30 days, number of inmate\r\n deaths, the peak population during June, facility crowding, and\r\nrenovation and building plans.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03472.v2",
+                    "title": "Annual Survey of Jails in Indian Country, 2001:  [United States]  "
+                }
+            ],
+            "identifier": "44",
+            "isPartOf": "2435",
+            "issued": "2003-02-13T00:00:00",
             "keyword": [
                 "Native Americans",
                 "correctional facilities",
@@ -2608,55 +2602,55 @@
                 "jails",
                 "population characteristics"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-11-22T19:01:25",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2435",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2003-02-13T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03472.v2",
-                    "title": "Annual Survey of Jails in Indian Country, 2001:  [United States]  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails in Indian Country, 2004",
-            "description": "The purpose of the Survey of Jails in Indian Country is  an enumeration of all known adult and juvenile facilities -- jails, confinement facilities, detention centers, and other correctional facilities operated by tribal authorities or by the Bureau of Indian Affairs (BIA) in the United States Department of the Interior. For the purpose of this collection, Indian country includes reservations, pueblos, rancherias, and other Native American and Alaska Native communities throughout the United States.\r\nThe survey collects data on the number of adults and juveniles held on the last weekday in June 2004, type of offense, average daily population in June, most crowded day in June, admissions and releases in June, number of inmate deaths and suicide attempts, rated capacity, and jail staffing.",
-            "modified": "2021-11-22T18:52:59",
-            "accessLevel": "restricted public",
-            "identifier": "45",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Annual Survey of Jails in Indian Country, 2001:  [United States]  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of the Survey of Jails in Indian Country is  an enumeration of all known adult and juvenile facilities -- jails, confinement facilities, detention centers, and other correctional facilities operated by tribal authorities or by the Bureau of Indian Affairs (BIA) in the United States Department of the Interior. For the purpose of this collection, Indian country includes reservations, pueblos, rancherias, and other Native American and Alaska Native communities throughout the United States.\r\nThe survey collects data on the number of adults and juveniles held on the last weekday in June 2004, type of offense, average daily population in June, most crowded day in June, admissions and releases in June, number of inmate deaths and suicide attempts, rated capacity, and jail staffing.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR31981.v2",
+                    "title": "Annual Survey of Jails in Indian Country, 2004"
+                }
+            ],
+            "identifier": "45",
+            "isPartOf": "2435",
+            "issued": "2012-09-20T10:16:29",
             "keyword": [
                 "Alaskan Natives",
                 "Native Americans",
@@ -2667,55 +2661,55 @@
                 "jails",
                 "population characteristics"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-11-22T18:52:59",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2435",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2012-09-20T10:16:29",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR31981.v2",
-                    "title": "Annual Survey of Jails in Indian Country, 2004"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails in Indian Country, 2007",
-            "description": "The purpose of the Survey of Jails in Indian Country is  an enumeration of all known adult and juvenile facilities -- jails, confinement facilities, detention centers, and other correctional facilities operated by tribal authorities or by the Bureau of Indian Affairs (BIA) in the United States Department of the Interior. For the purpose of this collection, Indian country includes reservations, pueblos, rancherias, and other Native American and Alaska Native communities throughout the United States.\r\nThe survey collects data on the number of adults and juveniles held on the last weekday in June 2007, type of offense, average daily population in June, most crowded day in June, admissions and releases in June, number of inmate deaths and suicide attempts, rated capacity, and jail staffing.",
-            "modified": "2021-11-22T18:45:46",
-            "accessLevel": "restricted public",
-            "identifier": "46",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Annual Survey of Jails in Indian Country, 2004"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of the Survey of Jails in Indian Country is  an enumeration of all known adult and juvenile facilities -- jails, confinement facilities, detention centers, and other correctional facilities operated by tribal authorities or by the Bureau of Indian Affairs (BIA) in the United States Department of the Interior. For the purpose of this collection, Indian country includes reservations, pueblos, rancherias, and other Native American and Alaska Native communities throughout the United States.\r\nThe survey collects data on the number of adults and juveniles held on the last weekday in June 2007, type of offense, average daily population in June, most crowded day in June, admissions and releases in June, number of inmate deaths and suicide attempts, rated capacity, and jail staffing.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR31924.v2",
+                    "title": "Annual Survey of Jails in Indian Country, 2007"
+                }
+            ],
+            "identifier": "46",
+            "isPartOf": "2435",
+            "issued": "2011-11-01T09:15:26",
             "keyword": [
                 "Alaskan Natives",
                 "Native Americans",
@@ -2726,55 +2720,55 @@
                 "jails",
                 "population characteristics"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-11-22T18:45:46",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2435",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-11-01T09:15:26",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR31924.v2",
-                    "title": "Annual Survey of Jails in Indian Country, 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails in Indian Country, 2008",
-            "description": "The purpose of the Survey of Jails in Indian Country is an enumeration of all known adult and juvenile facilities -- jails, confinement facilities, detention centers, and other correctional facilities operated by tribal authorities or by the Bureau of Indian Affairs (BIA) in the United States Department of the Interior. For the purpose of this collection, Indian country includes reservations, pueblos, rancherias, and other Native American and Alaska Native communities throughout the United States. The survey collects data on the number of adults and juveniles held on the last weekday in June 2008, type of offense, average daily population in June, most crowded day in June, admissions and releases in June, number of inmate deaths and suicide attempts, rated capacity, and jail staffing.",
-            "modified": "2021-11-22T18:39:51",
-            "accessLevel": "restricted public",
-            "identifier": "47",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Annual Survey of Jails in Indian Country, 2007"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of the Survey of Jails in Indian Country is an enumeration of all known adult and juvenile facilities -- jails, confinement facilities, detention centers, and other correctional facilities operated by tribal authorities or by the Bureau of Indian Affairs (BIA) in the United States Department of the Interior. For the purpose of this collection, Indian country includes reservations, pueblos, rancherias, and other Native American and Alaska Native communities throughout the United States. The survey collects data on the number of adults and juveniles held on the last weekday in June 2008, type of offense, average daily population in June, most crowded day in June, admissions and releases in June, number of inmate deaths and suicide attempts, rated capacity, and jail staffing.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR31923.v2",
+                    "title": "Annual Survey of Jails in Indian Country, 2008"
+                }
+            ],
+            "identifier": "47",
+            "isPartOf": "2435",
+            "issued": "2011-10-07T08:47:52",
             "keyword": [
                 "Native Americans",
                 "correctional facilities",
@@ -2784,55 +2778,55 @@
                 "jails",
                 "population characteristics"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-11-22T18:39:51",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2435",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-10-07T08:47:52",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR31923.v2",
-                    "title": "Annual Survey of Jails in Indian Country, 2008"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails in Indian Country, 2009",
-            "description": "The purpose of the Survey of Jails in Indian Country is  an enumeration of all known adult and juvenile facilities -- jails, confinement facilities, detention centers, and other correctional facilities operated by tribal authorities or by the Bureau of Indian Affairs (BIA)in the United States Department of the Interior. For the purpose of this collection, Indian country includes reservations, pueblos, rancherias, and other Native American and Alaska Native communities throughout the United States.\r\nThe survey collects data on the number of adults and juveniles held on the last weekday in June 2009, type of offense, average daily population in June, most crowded day in June, admissions and releases in June, number of inmate deaths and suicide attempts, rated capacity, and jail staffing.",
-            "modified": "2021-11-22T18:35:21",
-            "accessLevel": "restricted public",
-            "identifier": "48",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Annual Survey of Jails in Indian Country, 2008"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of the Survey of Jails in Indian Country is  an enumeration of all known adult and juvenile facilities -- jails, confinement facilities, detention centers, and other correctional facilities operated by tribal authorities or by the Bureau of Indian Affairs (BIA)in the United States Department of the Interior. For the purpose of this collection, Indian country includes reservations, pueblos, rancherias, and other Native American and Alaska Native communities throughout the United States.\r\nThe survey collects data on the number of adults and juveniles held on the last weekday in June 2009, type of offense, average daily population in June, most crowded day in June, admissions and releases in June, number of inmate deaths and suicide attempts, rated capacity, and jail staffing.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR31741.v2",
+                    "title": "Annual Survey of Jails in Indian Country, 2009"
+                }
+            ],
+            "identifier": "48",
+            "isPartOf": "2435",
+            "issued": "2011-08-17T15:25:33",
             "keyword": [
                 "Native Americans",
                 "correctional facilities",
@@ -2842,55 +2836,55 @@
                 "jails",
                 "population characteristics"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-11-22T18:35:21",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2435",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-08-17T15:25:33",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR31741.v2",
-                    "title": "Annual Survey of Jails in Indian Country, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails in Indian Country, 2010",
-            "description": "The purpose of the Survey of Jails in Indian Country is  an enumeration of all known adult and juvenile facilities -- jails, confinement facilities, detention centers, and other correctional facilities operated by tribal authorities or by the Bureau of Indian Affairs (BIA)in the United States Department of the Interior. For the purpose of this collection, Indian country includes reservations, pueblos, rancherias, and other Native American and Alaska Native communities throughout the United States.\r\nThe survey collects data on the number of adults and juveniles held on the last weekday in June 2010, type of offense, average daily population in June, most crowded day in June, admissions and releases in June, number of inmate deaths and suicide attempts, rated capacity, and jail staffing.",
-            "modified": "2021-11-22T18:22:04",
-            "accessLevel": "restricted public",
-            "identifier": "49",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Annual Survey of Jails in Indian Country, 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of the Survey of Jails in Indian Country is  an enumeration of all known adult and juvenile facilities -- jails, confinement facilities, detention centers, and other correctional facilities operated by tribal authorities or by the Bureau of Indian Affairs (BIA)in the United States Department of the Interior. For the purpose of this collection, Indian country includes reservations, pueblos, rancherias, and other Native American and Alaska Native communities throughout the United States.\r\nThe survey collects data on the number of adults and juveniles held on the last weekday in June 2010, type of offense, average daily population in June, most crowded day in June, admissions and releases in June, number of inmate deaths and suicide attempts, rated capacity, and jail staffing.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR32841.v2",
+                    "title": "Annual Survey of Jails in Indian Country, 2010"
+                }
+            ],
+            "identifier": "49",
+            "isPartOf": "2435",
+            "issued": "2011-12-05T08:21:12",
             "keyword": [
                 "Native Americans",
                 "correctional facilities",
@@ -2900,55 +2894,55 @@
                 "jails",
                 "population characteristics"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-11-22T18:22:04",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2435",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-12-05T08:21:12",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR32841.v2",
-                    "title": "Annual Survey of Jails in Indian Country, 2010"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails in Indian Country, 2011",
-            "description": "The purpose of the Survey of Jails in Indian Country is  an enumeration of all known adult and juvenile facilities -- jails, confinement facilities, detention centers, and other correctional facilities operated by tribal authorities or by the Bureau of Indian Affairs (BIA) in the United States Department of the Interior. For the purpose of this collection, Indian country includes reservations, pueblos, rancherias, and other Native American and Alaska Native communities throughout the United States.\r\nThe survey collects data on the number of adults and juveniles held on the last weekday in June 2011, type of offense, average daily population in June, most crowded day in June, admissions and releases in June, number of inmate deaths and suicide attempts, rated capacity, and jail staffing.",
-            "modified": "2021-11-22T17:57:04",
-            "accessLevel": "restricted public",
-            "identifier": "50",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Annual Survey of Jails in Indian Country, 2010"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of the Survey of Jails in Indian Country is  an enumeration of all known adult and juvenile facilities -- jails, confinement facilities, detention centers, and other correctional facilities operated by tribal authorities or by the Bureau of Indian Affairs (BIA) in the United States Department of the Interior. For the purpose of this collection, Indian country includes reservations, pueblos, rancherias, and other Native American and Alaska Native communities throughout the United States.\r\nThe survey collects data on the number of adults and juveniles held on the last weekday in June 2011, type of offense, average daily population in June, most crowded day in June, admissions and releases in June, number of inmate deaths and suicide attempts, rated capacity, and jail staffing.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34354.v2",
+                    "title": "Annual Survey of Jails in Indian Country, 2011"
+                }
+            ],
+            "identifier": "50",
+            "isPartOf": "2435",
+            "issued": "2012-09-24T08:59:14",
             "keyword": [
                 "Native Americans",
                 "correctional facilities",
@@ -2958,55 +2952,55 @@
                 "jails",
                 "population characteristics"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-11-22T17:57:04",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2435",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2012-09-24T08:59:14",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34354.v2",
-                    "title": "Annual Survey of Jails in Indian Country, 2011"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails in Indian Country, 2012",
-            "description": "The purpose of the Survey of Jails in Indian Country is an enumeration of all known adult and\r\njuvenile facilities -- jails, confinement facilities, detention centers, and other correctional\r\nfacilities operated by tribal authorities or the Bureau of Indian Affairs (BIA), United States Department of\r\nthe Interior. For the purpose of this collection, Indian country includes reservations, pueblos,\r\nrancherias, and other Native American and Alaska Native communities throughout the United States.\r\nThe survey collects data on the number of adults and juveniles held on the last weekday in June\r\n2012, type of offense, average daily population in June, most crowded day in June, admissions and\r\nreleases in June, number of inmate deaths and suicide attempts, rated capacity, and jail staffing.",
-            "modified": "2021-11-22T17:51:39",
-            "accessLevel": "restricted public",
-            "identifier": "51",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Annual Survey of Jails in Indian Country, 2011"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of the Survey of Jails in Indian Country is an enumeration of all known adult and\r\njuvenile facilities -- jails, confinement facilities, detention centers, and other correctional\r\nfacilities operated by tribal authorities or the Bureau of Indian Affairs (BIA), United States Department of\r\nthe Interior. For the purpose of this collection, Indian country includes reservations, pueblos,\r\nrancherias, and other Native American and Alaska Native communities throughout the United States.\r\nThe survey collects data on the number of adults and juveniles held on the last weekday in June\r\n2012, type of offense, average daily population in June, most crowded day in June, admissions and\r\nreleases in June, number of inmate deaths and suicide attempts, rated capacity, and jail staffing.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34704.v2",
+                    "title": "Annual Survey of Jails in Indian Country, 2012"
+                }
+            ],
+            "identifier": "51",
+            "isPartOf": "2435",
+            "issued": "2013-07-10T16:36:37",
             "keyword": [
                 "Native Americans",
                 "correctional facilities",
@@ -3016,55 +3010,54 @@
                 "jails",
                 "population characteristics"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-11-22T17:51:39",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2435",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2013-07-10T16:36:37",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34704.v2",
-                    "title": "Annual Survey of Jails in Indian Country, 2012"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails: Individual Reporting-Level Data, 2007",
-            "description": "The Annual Survey of Jails (ASJ) is the only data collection effort that provides an\r\nannual source of data on local jails and jail inmates.  Data on the size of the\r\njail population and selected inmate characteristics are obtained every five to\r\nsix years from the Census of Jails.  In each of the years between the full censuses,\r\na sample survey of jails is conducted to estimate\r\nbaseline characteristics of the Nation's jails and inmates housed in these jails.\r\nThe 2007 Annual Survey of Jails is the 20th such survey in a series begun in 1982.\r\nThe ASJ supplies data on characteristics of jails such as admissions and releases,\r\ngrowth in the number of jail facilities, changes in their rated capacities and level\r\nof occupancy, growth in the population supervised in the community, changes in methods\r\nof community supervision, and crowding issues.  The ASJ\r\nalso provides information on changes in the demographics of the jail population,\r\nsupervision status of persons held, and a count of non-citizens in custody.\r\nThe data presented in this study were collected in the Annual Survey of\r\nJails, 2007.  These data are used to track growth in the number of\r\njails and the capacities nationally, changes in the demographics of the\r\njail population and supervision status of persons held, the prevalence of\r\ncrowding issues, and a count of non-United States citizens within the jail\r\npopulation.  The data are intended for a variety of users, including\r\nFederal and State agencies, local officials in conjunction with jail\r\nadministrators, researchers, planners, and the public.  The reference date\r\nfor the survey is June 29, 2007.",
-            "modified": "2010-01-27T07:53:48",
-            "accessLevel": "public",
-            "identifier": "52",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Annual Survey of Jails in Indian Country, 2012"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The Annual Survey of Jails (ASJ) is the only data collection effort that provides an\r\nannual source of data on local jails and jail inmates.  Data on the size of the\r\njail population and selected inmate characteristics are obtained every five to\r\nsix years from the Census of Jails.  In each of the years between the full censuses,\r\na sample survey of jails is conducted to estimate\r\nbaseline characteristics of the Nation's jails and inmates housed in these jails.\r\nThe 2007 Annual Survey of Jails is the 20th such survey in a series begun in 1982.\r\nThe ASJ supplies data on characteristics of jails such as admissions and releases,\r\ngrowth in the number of jail facilities, changes in their rated capacities and level\r\nof occupancy, growth in the population supervised in the community, changes in methods\r\nof community supervision, and crowding issues.  The ASJ\r\nalso provides information on changes in the demographics of the jail population,\r\nsupervision status of persons held, and a count of non-citizens in custody.\r\nThe data presented in this study were collected in the Annual Survey of\r\nJails, 2007.  These data are used to track growth in the number of\r\njails and the capacities nationally, changes in the demographics of the\r\njail population and supervision status of persons held, the prevalence of\r\ncrowding issues, and a count of non-United States citizens within the jail\r\npopulation.  The data are intended for a variety of users, including\r\nFederal and State agencies, local officials in conjunction with jail\r\nadministrators, researchers, planners, and the public.  The reference date\r\nfor the survey is June 29, 2007.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24641.v1",
+                    "title": "Annual Survey of Jails: Individual Reporting-Level Data, 2007"
+                }
+            ],
+            "identifier": "52",
+            "issued": "2010-01-27T07:53:48",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -3074,53 +3067,54 @@
                 "population characteristics",
                 "probation"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-01-27T07:53:48",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "2010-01-27T07:53:48",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24641.v1",
-                    "title": "Annual Survey of Jails: Individual Reporting-Level Data, 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails: Jail-Level Data, 2008",
-            "description": "The Annual Survey of Jails (ASJ) is the only data collection effort that provides an\r\nannual source of data on local jails and jail inmates.  Data on the size of the\r\njail population and selected inmate characteristics are obtained every five to\r\nsix years from the Census of Jails.  In each of the years between the full censuses,\r\na sample survey of jails is conducted to estimate\r\nbaseline characteristics of the nation's jails and inmates housed in these jails.\r\nThe 2008 Annual Survey of Jails is the 21st such survey in a series begun in 1982.\r\nThe ASJ supplies data on characteristics of jails such as admissions and releases,\r\ngrowth in the number of jail facilities, changes in their rated capacities and level\r\nof occupancy, growth in the population supervised in the community, changes in methods\r\nof community supervision, and crowding issues.  The ASJ\r\nalso provides information on changes in the demographics of the jail population,\r\nsupervision status of persons held, and a count of non-citizens in custody.\r\nThe data presented in this study were collected in the Annual Survey of\r\nJails, 2008.  These data are used to track growth in the number of\r\njails and the capacities nationally, changes in the demographics of the\r\njail population and supervision status of persons held, the prevalence of\r\ncrowding issues, and a count of non-United States citizens within the jail\r\npopulation.  The data are intended for a variety of users, including\r\nfederal and state agencies, local officials in conjunction with jail\r\nadministrators, researchers, planners, and the public.  The reference date\r\nfor the survey is June 30, 2008.",
-            "modified": "2011-05-10T14:29:51",
-            "accessLevel": "public",
-            "identifier": "53",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Survey of Jails: Individual Reporting-Level Data, 2007"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The Annual Survey of Jails (ASJ) is the only data collection effort that provides an\r\nannual source of data on local jails and jail inmates.  Data on the size of the\r\njail population and selected inmate characteristics are obtained every five to\r\nsix years from the Census of Jails.  In each of the years between the full censuses,\r\na sample survey of jails is conducted to estimate\r\nbaseline characteristics of the nation's jails and inmates housed in these jails.\r\nThe 2008 Annual Survey of Jails is the 21st such survey in a series begun in 1982.\r\nThe ASJ supplies data on characteristics of jails such as admissions and releases,\r\ngrowth in the number of jail facilities, changes in their rated capacities and level\r\nof occupancy, growth in the population supervised in the community, changes in methods\r\nof community supervision, and crowding issues.  The ASJ\r\nalso provides information on changes in the demographics of the jail population,\r\nsupervision status of persons held, and a count of non-citizens in custody.\r\nThe data presented in this study were collected in the Annual Survey of\r\nJails, 2008.  These data are used to track growth in the number of\r\njails and the capacities nationally, changes in the demographics of the\r\njail population and supervision status of persons held, the prevalence of\r\ncrowding issues, and a count of non-United States citizens within the jail\r\npopulation.  The data are intended for a variety of users, including\r\nfederal and state agencies, local officials in conjunction with jail\r\nadministrators, researchers, planners, and the public.  The reference date\r\nfor the survey is June 30, 2008.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR28281.v1",
+                    "title": "Annual Survey of Jails: Jail-Level Data, 2008"
+                }
+            ],
+            "identifier": "53",
+            "isPartOf": "2586",
+            "issued": "2011-05-10T14:29:51",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -3130,111 +3124,111 @@
                 "population characteristics",
                 "probation"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-05-10T14:29:51",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2586",
-            "dataQuality": false,
-            "issued": "2011-05-10T14:29:51",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR28281.v1",
-                    "title": "Annual Survey of Jails: Jail-Level Data, 2008"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails: Jail-Level Data, 2009",
-            "description": "The Annual Survey of Jails (ASJ) is the only data collection effort that provides an\r\nannual source of data on local jails and jail inmates.  Data on the size of the\r\njail population and selected inmate characteristics are obtained every five to\r\nsix years from the Census of Jails.  In each of the years between the full censuses,\r\na sample survey of jails is conducted to estimate\r\nbaseline characteristics of the nation's jails and inmates housed in these jails.\r\nThe 2009 Annual Survey of Jails is the 22nd such survey in a series begun in 1982.\r\nThe ASJ supplies data on characteristics of jails such as admissions and releases,\r\ngrowth in the number of jail facilities, changes in their rated capacities and level\r\nof occupancy, growth in the population supervised in the community, changes in methods\r\nof community supervision, and crowding issues.  The ASJ\r\nalso provides information on changes in the demographics of the jail population,\r\nsupervision status of persons held, and a count of non-citizens in custody.\r\nThe data presented in this study were collected in the Annual Survey of\r\nJails, 2009.  These data are used to track growth in the number of\r\njails and the capacities nationally, changes in the demographics of the\r\njail population and supervision status of persons held, the prevalence of\r\ncrowding issues, and a count of non-United States citizens within the jail\r\npopulation.  The data are intended for a variety of users, including\r\nfederal and state agencies, local officials in conjunction with jail\r\nadministrators, researchers, planners, and the public.  The reference date\r\nfor the survey is June 30, 2009.",
-            "modified": "2011-05-11T11:32:42",
-            "accessLevel": "public",
-            "identifier": "54",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Survey of Jails: Jail-Level Data, 2008"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
-            "keyword": [
-                "correctional facilities",
-                "correctional system",
-                "demographic characteristics",
-                "jail inmates",
-                "jails",
-                "population characteristics",
-                "probation"
-            ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2586",
             "dataQuality": false,
-            "issued": "2011-05-11T11:32:42",
-            "language": [
-                "eng"
-            ],
+            "description": "The Annual Survey of Jails (ASJ) is the only data collection effort that provides an\r\nannual source of data on local jails and jail inmates.  Data on the size of the\r\njail population and selected inmate characteristics are obtained every five to\r\nsix years from the Census of Jails.  In each of the years between the full censuses,\r\na sample survey of jails is conducted to estimate\r\nbaseline characteristics of the nation's jails and inmates housed in these jails.\r\nThe 2009 Annual Survey of Jails is the 22nd such survey in a series begun in 1982.\r\nThe ASJ supplies data on characteristics of jails such as admissions and releases,\r\ngrowth in the number of jail facilities, changes in their rated capacities and level\r\nof occupancy, growth in the population supervised in the community, changes in methods\r\nof community supervision, and crowding issues.  The ASJ\r\nalso provides information on changes in the demographics of the jail population,\r\nsupervision status of persons held, and a count of non-citizens in custody.\r\nThe data presented in this study were collected in the Annual Survey of\r\nJails, 2009.  These data are used to track growth in the number of\r\njails and the capacities nationally, changes in the demographics of the\r\njail population and supervision status of persons held, the prevalence of\r\ncrowding issues, and a count of non-United States citizens within the jail\r\npopulation.  The data are intended for a variety of users, including\r\nfederal and state agencies, local officials in conjunction with jail\r\nadministrators, researchers, planners, and the public.  The reference date\r\nfor the survey is June 30, 2009.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://doi.org/10.3886/ICPSR29081.v1",
                     "title": "Annual Survey of Jails: Jail-Level Data, 2009"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails: Jail-Level Data, 2010",
-            "description": "The Annual Survey of Jails (ASJ) is the only data collection effort that provides an annual source of data on local jails and jail inmates. Data on the size of the jail population and selected inmate characteristics are obtained every five to six years from the Census of Jails.  In each of the years between the full censuses, a sample survey of jails is conducted to estimate\r\nbaseline characteristics of the nation's jails and inmates housed in these jails.  The 2010 Annual Survey of Jails is the 23rd such survey in a series begun in 1982.  The ASJ supplies data on characteristics of jails such as admissions and releases,\r\ngrowth in the number of jail facilities, changes in their rated capacities and level\r\nof occupancy, growth in the population supervised in the community, changes in methods\r\nof community supervision, and crowding issues.  The ASJ\r\nalso provides information on changes in the demographics of the jail population,\r\nsupervision status of persons held, and a count of non-citizens in custody.\r\nStarting in 2010, BJS enhanced the ASJ survey instruments to address topics on the number of convicted inmates that are unsentenced or sentenced and the number of unconvicted inmates awaiting trial/arraignment, or transfers/holds for other authorities. In order to reduce respondent burden, the ASJ no longer collects data on conviction status by sex.  Also new to 2010, data is collected on jails' operational capacity and design capacity.  Incorporating enhanced capacity measurements enables BJS to describe more accurately the variation and volatility of inmate bed space and crowding, especially as they relate to safety and security in jails.\r\nTo address more directly issues related to overcrowding and safety and security in jails, BJS started collecting data on staff and assaults against staff from the largest jails.  In the modifications to the ASJ, starting in 2010, 335 jail jurisdictions (370 respondents) included with certainty in the ASJ sample survey were asked to provide additional information (forms CJ-5D or CJ-5DA) on the flow of inmates going through jails and the distribution of time served, staff characteristics and assaults on staff resulting in death, and inmate misconduct.\r\nThe data presented in this study were collected in the Annual Survey of\r\nJails, 2010.  These data are used to track growth in the number of\r\njails and the capacities nationally, changes in the demographics of the\r\njail population and supervision status of persons held, the prevalence of\r\ncrowding issues, and a count of non-United States citizens within the jail\r\npopulation.  The data are intended for a variety of users, including\r\nfederal and state agencies, local officials in conjunction with jail\r\nadministrators, researchers, planners, and the public.  The reference date\r\nfor the survey is June 30, 2010.",
-            "modified": "2011-08-02T14:36:32",
-            "accessLevel": "public",
-            "identifier": "55",
+            ],
+            "identifier": "54",
+            "isPartOf": "2586",
+            "issued": "2011-05-11T11:32:42",
+            "keyword": [
+                "correctional facilities",
+                "correctional system",
+                "demographic characteristics",
+                "jail inmates",
+                "jails",
+                "population characteristics",
+                "probation"
+            ],
+            "language": [
+                "eng"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-05-11T11:32:42",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Survey of Jails: Jail-Level Data, 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The Annual Survey of Jails (ASJ) is the only data collection effort that provides an annual source of data on local jails and jail inmates. Data on the size of the jail population and selected inmate characteristics are obtained every five to six years from the Census of Jails.  In each of the years between the full censuses, a sample survey of jails is conducted to estimate\r\nbaseline characteristics of the nation's jails and inmates housed in these jails.  The 2010 Annual Survey of Jails is the 23rd such survey in a series begun in 1982.  The ASJ supplies data on characteristics of jails such as admissions and releases,\r\ngrowth in the number of jail facilities, changes in their rated capacities and level\r\nof occupancy, growth in the population supervised in the community, changes in methods\r\nof community supervision, and crowding issues.  The ASJ\r\nalso provides information on changes in the demographics of the jail population,\r\nsupervision status of persons held, and a count of non-citizens in custody.\r\nStarting in 2010, BJS enhanced the ASJ survey instruments to address topics on the number of convicted inmates that are unsentenced or sentenced and the number of unconvicted inmates awaiting trial/arraignment, or transfers/holds for other authorities. In order to reduce respondent burden, the ASJ no longer collects data on conviction status by sex.  Also new to 2010, data is collected on jails' operational capacity and design capacity.  Incorporating enhanced capacity measurements enables BJS to describe more accurately the variation and volatility of inmate bed space and crowding, especially as they relate to safety and security in jails.\r\nTo address more directly issues related to overcrowding and safety and security in jails, BJS started collecting data on staff and assaults against staff from the largest jails.  In the modifications to the ASJ, starting in 2010, 335 jail jurisdictions (370 respondents) included with certainty in the ASJ sample survey were asked to provide additional information (forms CJ-5D or CJ-5DA) on the flow of inmates going through jails and the distribution of time served, staff characteristics and assaults on staff resulting in death, and inmate misconduct.\r\nThe data presented in this study were collected in the Annual Survey of\r\nJails, 2010.  These data are used to track growth in the number of\r\njails and the capacities nationally, changes in the demographics of the\r\njail population and supervision status of persons held, the prevalence of\r\ncrowding issues, and a count of non-United States citizens within the jail\r\npopulation.  The data are intended for a variety of users, including\r\nfederal and state agencies, local officials in conjunction with jail\r\nadministrators, researchers, planners, and the public.  The reference date\r\nfor the survey is June 30, 2010.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR31261.v1",
+                    "title": "Annual Survey of Jails: Jail-Level Data, 2010"
+                }
+            ],
+            "identifier": "55",
+            "isPartOf": "2586",
+            "issued": "2011-08-02T14:36:32",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -3244,54 +3238,54 @@
                 "population characteristics",
                 "probation"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-08-02T14:36:32",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2586",
-            "dataQuality": false,
-            "issued": "2011-08-02T14:36:32",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR31261.v1",
-                    "title": "Annual Survey of Jails: Jail-Level Data, 2010"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails: Jail-Level Data, 2011",
-            "description": "The Annual Survey of Jails (ASJ) is the only data collection effort that provides an annual source of data on local jails and jail inmates. Data on the size of the jail population and selected inmate characteristics are obtained every five to six years from the Census of Jails.  In each of the years between the full censuses, a sample survey of jails is conducted to estimate\r\nbaseline characteristics of the nation's jails and inmates housed in these jails.  The 2011 Annual Survey of Jails is the 24th such survey in a series begun in 1982.  The ASJ supplies data on characteristics of jails such as admissions and releases,\r\ngrowth in the number of jail facilities, changes in their rated capacities and level\r\nof occupancy, growth in the population supervised in the community, changes in methods\r\nof community supervision, and crowding issues.  The ASJ\r\nalso provides information on changes in the demographics of the jail population,\r\nsupervision status of persons held, and a count of non-citizens in custody.\r\nStarting in 2010, BJS enhanced the ASJ survey instruments to address topics on the number of convicted inmates that are unsentenced or sentenced and the number of unconvicted inmates awaiting trial/arraignment, or transfers/holds for other authorities. In order to reduce respondent burden, the ASJ no longer collects data on conviction status by sex.  Also new to the survey, data are collected on jails' operational capacity and design capacity.  Incorporating enhanced capacity measurements enables BJS to describe more accurately the variation and volatility of inmate bed space and crowding, especially as they relate to safety and security in jails.\r\nTo address more directly issues related to overcrowding and safety and security in jails, BJS started collecting data on staff and assaults against staff from the largest jails.  In the modifications to the ASJ, starting in 2010, 335 jail jurisdictions (370 respondents) included with certainty in the ASJ sample survey were asked to provide additional information (forms CJ-5D or CJ-5DA) on the flow of inmates going through jails and the distribution of time served, staff characteristics and assaults on staff resulting in death, and inmate misconduct.\r\nThe data presented in this study were collected in the Annual Survey of\r\nJails, 2011.  These data are used to track growth in the number of\r\njails and the capacities nationally, changes in the demographics of the\r\njail population and supervision status of persons held, the prevalence of\r\ncrowding issues, and a count of non-United States citizens within the jail\r\npopulation.  The data are intended for a variety of users, including\r\nfederal and state agencies, local officials in conjunction with jail\r\nadministrators, researchers, planners, and the public.  The reference date\r\nfor the survey is June 30, 2011.",
-            "modified": "2012-04-25T09:32:46",
-            "accessLevel": "public",
-            "identifier": "56",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Survey of Jails: Jail-Level Data, 2010"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The Annual Survey of Jails (ASJ) is the only data collection effort that provides an annual source of data on local jails and jail inmates. Data on the size of the jail population and selected inmate characteristics are obtained every five to six years from the Census of Jails.  In each of the years between the full censuses, a sample survey of jails is conducted to estimate\r\nbaseline characteristics of the nation's jails and inmates housed in these jails.  The 2011 Annual Survey of Jails is the 24th such survey in a series begun in 1982.  The ASJ supplies data on characteristics of jails such as admissions and releases,\r\ngrowth in the number of jail facilities, changes in their rated capacities and level\r\nof occupancy, growth in the population supervised in the community, changes in methods\r\nof community supervision, and crowding issues.  The ASJ\r\nalso provides information on changes in the demographics of the jail population,\r\nsupervision status of persons held, and a count of non-citizens in custody.\r\nStarting in 2010, BJS enhanced the ASJ survey instruments to address topics on the number of convicted inmates that are unsentenced or sentenced and the number of unconvicted inmates awaiting trial/arraignment, or transfers/holds for other authorities. In order to reduce respondent burden, the ASJ no longer collects data on conviction status by sex.  Also new to the survey, data are collected on jails' operational capacity and design capacity.  Incorporating enhanced capacity measurements enables BJS to describe more accurately the variation and volatility of inmate bed space and crowding, especially as they relate to safety and security in jails.\r\nTo address more directly issues related to overcrowding and safety and security in jails, BJS started collecting data on staff and assaults against staff from the largest jails.  In the modifications to the ASJ, starting in 2010, 335 jail jurisdictions (370 respondents) included with certainty in the ASJ sample survey were asked to provide additional information (forms CJ-5D or CJ-5DA) on the flow of inmates going through jails and the distribution of time served, staff characteristics and assaults on staff resulting in death, and inmate misconduct.\r\nThe data presented in this study were collected in the Annual Survey of\r\nJails, 2011.  These data are used to track growth in the number of\r\njails and the capacities nationally, changes in the demographics of the\r\njail population and supervision status of persons held, the prevalence of\r\ncrowding issues, and a count of non-United States citizens within the jail\r\npopulation.  The data are intended for a variety of users, including\r\nfederal and state agencies, local officials in conjunction with jail\r\nadministrators, researchers, planners, and the public.  The reference date\r\nfor the survey is June 30, 2011.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR33722.v1",
+                    "title": "Annual Survey of Jails: Jail-Level Data, 2011"
+                }
+            ],
+            "identifier": "56",
+            "isPartOf": "2586",
+            "issued": "2012-04-25T09:32:46",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -3301,54 +3295,54 @@
                 "population characteristics",
                 "probation"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2012-04-25T09:32:46",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2586",
-            "dataQuality": false,
-            "issued": "2012-04-25T09:32:46",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR33722.v1",
-                    "title": "Annual Survey of Jails: Jail-Level Data, 2011"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails: Jail-Level Data, 2012",
-            "description": "The Annual Survey of Jails (ASJ) is the only data collection effort that provides an annual source of data on local jails and jail inmates. Data on the size of the jail population and selected inmate characteristics are obtained every five to six years from the Census of Jails.  In each of the years between the full censuses, a sample survey of jails is conducted to estimate\r\nbaseline characteristics of the nation's jails and inmates housed in these jails.  The 2012 Annual Survey of Jails is the 25th such survey in a series begun in 1982.  The ASJ supplies data on characteristics of jails such as admissions and releases,\r\ngrowth in the number of jail facilities, changes in their rated capacities and level\r\nof occupancy, growth in the population supervised in the community, changes in methods\r\nof community supervision, and crowding issues.  The ASJ\r\nalso provides information on changes in the demographics of the jail population,\r\nsupervision status of persons held, and a count of non-citizens in custody.\r\nStarting in 2010, BJS enhanced the ASJ survey instruments to address topics on the number of convicted inmates that are unsentenced or sentenced and the number of unconvicted inmates awaiting trial/arraignment, or transfers/holds for other authorities. In order to reduce respondent burden, the ASJ no longer collects data on conviction status by sex.  Also new to the survey, data are collected on jails' operational capacity and design capacity.  Incorporating enhanced capacity measurements enables BJS to describe more accurately the variation and volatility of inmate bed space and crowding, especially as they relate to safety and security in jails.\r\nTo address more directly issues related to overcrowding and safety and security in jails, BJS started collecting data on staff and assaults against staff from the largest jails.  In the modifications to the ASJ, starting in 2010, 335 jail jurisdictions (370 respondents) included with certainty in the ASJ sample survey were asked to provide additional information (forms CJ-5D or CJ-5DA) on the flow of inmates going through jails and the distribution of time served, staff characteristics and assaults on staff resulting in death, and inmate misconduct.\r\nThe data presented in this study were collected in the Annual Survey of\r\nJails, 2012.  These data are used to track growth in the number of\r\njails and the capacities nationally, changes in the demographics of the\r\njail population and supervision status of persons held, the prevalence of\r\ncrowding issues, and a count of non-United States citizens within the jail\r\npopulation.  The data are intended for a variety of users, including\r\nfederal and state agencies, local officials in conjunction with jail\r\nadministrators, researchers, planners, and the public.  The reference date\r\nfor the survey is June 29, 2012.",
-            "modified": "2013-10-30T09:27:43",
-            "accessLevel": "public",
-            "identifier": "57",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Survey of Jails: Jail-Level Data, 2011"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The Annual Survey of Jails (ASJ) is the only data collection effort that provides an annual source of data on local jails and jail inmates. Data on the size of the jail population and selected inmate characteristics are obtained every five to six years from the Census of Jails.  In each of the years between the full censuses, a sample survey of jails is conducted to estimate\r\nbaseline characteristics of the nation's jails and inmates housed in these jails.  The 2012 Annual Survey of Jails is the 25th such survey in a series begun in 1982.  The ASJ supplies data on characteristics of jails such as admissions and releases,\r\ngrowth in the number of jail facilities, changes in their rated capacities and level\r\nof occupancy, growth in the population supervised in the community, changes in methods\r\nof community supervision, and crowding issues.  The ASJ\r\nalso provides information on changes in the demographics of the jail population,\r\nsupervision status of persons held, and a count of non-citizens in custody.\r\nStarting in 2010, BJS enhanced the ASJ survey instruments to address topics on the number of convicted inmates that are unsentenced or sentenced and the number of unconvicted inmates awaiting trial/arraignment, or transfers/holds for other authorities. In order to reduce respondent burden, the ASJ no longer collects data on conviction status by sex.  Also new to the survey, data are collected on jails' operational capacity and design capacity.  Incorporating enhanced capacity measurements enables BJS to describe more accurately the variation and volatility of inmate bed space and crowding, especially as they relate to safety and security in jails.\r\nTo address more directly issues related to overcrowding and safety and security in jails, BJS started collecting data on staff and assaults against staff from the largest jails.  In the modifications to the ASJ, starting in 2010, 335 jail jurisdictions (370 respondents) included with certainty in the ASJ sample survey were asked to provide additional information (forms CJ-5D or CJ-5DA) on the flow of inmates going through jails and the distribution of time served, staff characteristics and assaults on staff resulting in death, and inmate misconduct.\r\nThe data presented in this study were collected in the Annual Survey of\r\nJails, 2012.  These data are used to track growth in the number of\r\njails and the capacities nationally, changes in the demographics of the\r\njail population and supervision status of persons held, the prevalence of\r\ncrowding issues, and a count of non-United States citizens within the jail\r\npopulation.  The data are intended for a variety of users, including\r\nfederal and state agencies, local officials in conjunction with jail\r\nadministrators, researchers, planners, and the public.  The reference date\r\nfor the survey is June 29, 2012.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34884.v1",
+                    "title": "Annual Survey of Jails: Jail-Level Data, 2012"
+                }
+            ],
+            "identifier": "57",
+            "isPartOf": "2586",
+            "issued": "2013-10-30T09:27:43",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -3358,54 +3352,54 @@
                 "population characteristics",
                 "probation"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-10-30T09:27:43",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2586",
-            "dataQuality": false,
-            "issued": "2013-10-30T09:27:43",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34884.v1",
-                    "title": "Annual Survey of Jails: Jail-Level Data, 2012"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails:  Jurisdiction-level and Jail-level Data, 1985  ",
-            "description": "The Bureau of Justice Statistics (BJS) sponsors the Sample \r\n Survey of Jails as part of a series of statistical programs measuring \r\n the correctional population. The Sample Survey meets BJS's need to \r\n analyze continuously the \"spillover\" effect on local jails of the \r\n growth in federal and state prison populations. The data are used in \r\n conjunction with statistics on federal and state prisoners to provide a \r\n complete picture of the adult correctional system and to measure \r\nchanges in that system.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "58",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Survey of Jails: Jail-Level Data, 2012"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The Bureau of Justice Statistics (BJS) sponsors the Sample \r\n Survey of Jails as part of a series of statistical programs measuring \r\n the correctional population. The Sample Survey meets BJS's need to \r\n analyze continuously the \"spillover\" effect on local jails of the \r\n growth in federal and state prison populations. The data are used in \r\n conjunction with statistics on federal and state prisoners to provide a \r\n complete picture of the adult correctional system and to measure \r\nchanges in that system.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08687.v1",
+                    "title": "Annual Survey of Jails:  Jurisdiction-level and Jail-level Data, 1985  "
+                }
+            ],
+            "identifier": "58",
+            "isPartOf": "2586",
+            "issued": "1987-10-12T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -3416,54 +3410,54 @@
                 "population characteristics",
                 "probation"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2586",
-            "dataQuality": false,
-            "issued": "1987-10-12T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08687.v1",
-                    "title": "Annual Survey of Jails:  Jurisdiction-level and Jail-level Data, 1985  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails:  Jurisdiction-Level and Jail-Level Data, 1991  ",
-            "description": "This collection provides annual data on jail populations\r\n across the nation and examines the \"spillover\" effect on local jails\r\n resulting from the dramatic growth in federal and state prison\r\n populations. These data permit an assessment of the demands placed on\r\n correctional resources and provide a comprehensive picture of the\r\n adult correctional system and changes that occur within the system.\r\n Information is available on the number of inmates by sex, race, adult\r\n or juvenile status, reason being held, and cause of death. Facility\r\n characteristics were collected regarding capacity, court orders,\r\nconditions of confinement, and alternative programs.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "59",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Survey of Jails:  Jurisdiction-level and Jail-level Data, 1985  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This collection provides annual data on jail populations\r\n across the nation and examines the \"spillover\" effect on local jails\r\n resulting from the dramatic growth in federal and state prison\r\n populations. These data permit an assessment of the demands placed on\r\n correctional resources and provide a comprehensive picture of the\r\n adult correctional system and changes that occur within the system.\r\n Information is available on the number of inmates by sex, race, adult\r\n or juvenile status, reason being held, and cause of death. Facility\r\n characteristics were collected regarding capacity, court orders,\r\nconditions of confinement, and alternative programs.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06511.v1",
+                    "title": "Annual Survey of Jails:  Jurisdiction-Level and Jail-Level Data, 1991  "
+                }
+            ],
+            "identifier": "59",
+            "isPartOf": "2586",
+            "issued": "1995-12-20T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -3474,54 +3468,54 @@
                 "population characteristics",
                 "probation"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2586",
-            "dataQuality": false,
-            "issued": "1995-12-20T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06511.v1",
-                    "title": "Annual Survey of Jails:  Jurisdiction-Level and Jail-Level Data, 1991  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails:  Jurisdiction-Level and Jail-Level Data, 1992  ",
-            "description": "This collection provides annual data on jail populations \r\n across the nation and examines the \"spillover\" effect on local jails \r\n resulting from the dramatic growth in federal and state prison \r\n populations. These data permit an assessment of the demands placed on \r\n correctional resources and provide a comprehensive picture of the adult \r\n correctional system and changes that occur within the system. \r\n Information is available on the number of inmates by sex, race, adult \r\n or juvenile status, reason being held, and cause of death. Also added \r\n in the 1992 survey were variables on citizenship, population movement, \r\n and total number of inmate deaths for inmates originally confined to \r\n the facility in question who died either at that facility or elsewhere. \r\n Also, the 1992 version included a more complete survey of jail programs \r\n and a supplemental questionnaire (CJ-5S), which dealt with AIDS-related \r\n questions. In addition, information was collected for the first time on \r\n drug testing, programs that treated or educated inmates, boot camps, work \r\n release, and alternatives to incarceration such as electronic \r\n monitoring, house arrest, community service, and weekend or day \r\nreporting.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "60",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Survey of Jails:  Jurisdiction-Level and Jail-Level Data, 1991  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This collection provides annual data on jail populations \r\n across the nation and examines the \"spillover\" effect on local jails \r\n resulting from the dramatic growth in federal and state prison \r\n populations. These data permit an assessment of the demands placed on \r\n correctional resources and provide a comprehensive picture of the adult \r\n correctional system and changes that occur within the system. \r\n Information is available on the number of inmates by sex, race, adult \r\n or juvenile status, reason being held, and cause of death. Also added \r\n in the 1992 survey were variables on citizenship, population movement, \r\n and total number of inmate deaths for inmates originally confined to \r\n the facility in question who died either at that facility or elsewhere. \r\n Also, the 1992 version included a more complete survey of jail programs \r\n and a supplemental questionnaire (CJ-5S), which dealt with AIDS-related \r\n questions. In addition, information was collected for the first time on \r\n drug testing, programs that treated or educated inmates, boot camps, work \r\n release, and alternatives to incarceration such as electronic \r\n monitoring, house arrest, community service, and weekend or day \r\nreporting.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06395.v1",
+                    "title": "Annual Survey of Jails:  Jurisdiction-Level and Jail-Level Data, 1992  "
+                }
+            ],
+            "identifier": "60",
+            "isPartOf": "2586",
+            "issued": "1995-06-06T00:00:00",
             "keyword": [
                 "alternatives to institutionalization",
                 "correctional facilities",
@@ -3535,54 +3529,54 @@
                 "prerelease programs",
                 "probation"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2586",
-            "dataQuality": false,
-            "issued": "1995-06-06T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06395.v1",
-                    "title": "Annual Survey of Jails:  Jurisdiction-Level and Jail-Level Data, 1992  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1987",
-            "description": "This data collection provides annual data on jail\r\n populations across the nation and examines the \"spillover\" effect on\r\n local jails resulting from the dramatic growth in federal and state\r\n prison populations. These data permit an assessment of the demands\r\n placed on correctional resources and provide a complete picture of the\r\n adult correctional system and the changes that occur in that system.\r\n Information is available on the number of inmates by sex, race, adult\r\nor juvenile status, reason being held, and cause of death.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "61",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Survey of Jails:  Jurisdiction-Level and Jail-Level Data, 1992  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides annual data on jail\r\n populations across the nation and examines the \"spillover\" effect on\r\n local jails resulting from the dramatic growth in federal and state\r\n prison populations. These data permit an assessment of the demands\r\n placed on correctional resources and provide a complete picture of the\r\n adult correctional system and the changes that occur in that system.\r\n Information is available on the number of inmates by sex, race, adult\r\nor juvenile status, reason being held, and cause of death.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09074.v2",
+                    "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1987"
+                }
+            ],
+            "identifier": "61",
+            "isPartOf": "2586",
+            "issued": "1989-09-26T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -3593,54 +3587,54 @@
                 "population characteristics",
                 "probation"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2586",
-            "dataQuality": false,
-            "issued": "1989-09-26T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09074.v2",
-                    "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1987"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1989  ",
-            "description": "This data collection provides annual data on jail\r\n populations across the nation and examines the \"spillover\" effect on\r\n local jails resulting from the dramatic growth in federal and state\r\n prison populations. These data permit an assessment of the demands\r\n placed on correctional resources and provide a complete picture of the\r\n adult correctional system and the changes that occur in that system.\r\n Information is available on the number of inmates by sex, race, adult\r\nor juvenile status, reason being held, and cause of death.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "62",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1987"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides annual data on jail\r\n populations across the nation and examines the \"spillover\" effect on\r\n local jails resulting from the dramatic growth in federal and state\r\n prison populations. These data permit an assessment of the demands\r\n placed on correctional resources and provide a complete picture of the\r\n adult correctional system and the changes that occur in that system.\r\n Information is available on the number of inmates by sex, race, adult\r\nor juvenile status, reason being held, and cause of death.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09373.v2",
+                    "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1989  "
+                }
+            ],
+            "identifier": "62",
+            "isPartOf": "2586",
+            "issued": "1990-10-16T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -3651,54 +3645,54 @@
                 "population characteristics",
                 "probation"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2586",
-            "dataQuality": false,
-            "issued": "1990-10-16T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09373.v2",
-                    "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1989  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1990",
-            "description": "This collection provides annual data on jail populations\r\n across the nation and examines the \"spillover\" effect on local jails\r\n resulting from the dramatic growth in federal and state prison\r\n populations. These data permit an assessment of the demands placed on\r\n correctional resources and provide a complete picture of the adult\r\n correctional system and the changes that occur in that system.\r\n Information is available on the number of inmates by sex, race, adult\r\n or juvenile status, reason being held, and cause of death. Facility\r\n characteristics were collected regarding capacity, court orders,\r\nconditions of confinement, and alternative programs.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "63",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1989  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This collection provides annual data on jail populations\r\n across the nation and examines the \"spillover\" effect on local jails\r\n resulting from the dramatic growth in federal and state prison\r\n populations. These data permit an assessment of the demands placed on\r\n correctional resources and provide a complete picture of the adult\r\n correctional system and the changes that occur in that system.\r\n Information is available on the number of inmates by sex, race, adult\r\n or juvenile status, reason being held, and cause of death. Facility\r\n characteristics were collected regarding capacity, court orders,\r\nconditions of confinement, and alternative programs.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09569.v1",
+                    "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1990"
+                }
+            ],
+            "identifier": "63",
+            "isPartOf": "2586",
+            "issued": "1992-01-10T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -3709,54 +3703,54 @@
                 "population characteristics",
                 "probation"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2586",
-            "dataQuality": false,
-            "issued": "1992-01-10T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09569.v1",
-                    "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1990"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1994  ",
-            "description": "This collection provides annual data on jail populations \r\n across the nation and examines the \"spillover\" effect on local jails \r\n resulting from the dramatic growth in federal and state prison \r\n populations. These data permit an assessment of the demands placed on \r\n correctional resources and provide a comprehensive picture of the adult \r\n correctional system and changes that occur within the system. \r\n Information is available on the number of inmates by sex, race, and \r\n adult or juvenile status. Facility characteristics were collected \r\nregarding capacity and average daily population.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "64",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1990"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This collection provides annual data on jail populations \r\n across the nation and examines the \"spillover\" effect on local jails \r\n resulting from the dramatic growth in federal and state prison \r\n populations. These data permit an assessment of the demands placed on \r\n correctional resources and provide a comprehensive picture of the adult \r\n correctional system and changes that occur within the system. \r\n Information is available on the number of inmates by sex, race, and \r\n adult or juvenile status. Facility characteristics were collected \r\nregarding capacity and average daily population.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06538.v1",
+                    "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1994  "
+                }
+            ],
+            "identifier": "64",
+            "isPartOf": "2586",
+            "issued": "1995-10-30T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -3767,54 +3761,54 @@
                 "population characteristics",
                 "probation"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2586",
-            "dataQuality": false,
-            "issued": "1995-10-30T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06538.v1",
-                    "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1994  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1995  ",
-            "description": "This collection provides annual data on jail populations\r\n across the nation and examines the \"spillover\" effect on local jails\r\n resulting from the dramatic growth in federal and state prison\r\n populations. These data permit an assessment of the demands placed on\r\n correctional resources and provide a comprehensive picture of the\r\n adult correctional system and changes that occur within the system.\r\n Information is available on the number of inmates by sex, race, and\r\n adult or juvenile status. Facility characteristics were collected\r\nregarding capacity and average daily population.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "65",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1994  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This collection provides annual data on jail populations\r\n across the nation and examines the \"spillover\" effect on local jails\r\n resulting from the dramatic growth in federal and state prison\r\n populations. These data permit an assessment of the demands placed on\r\n correctional resources and provide a comprehensive picture of the\r\n adult correctional system and changes that occur within the system.\r\n Information is available on the number of inmates by sex, race, and\r\n adult or juvenile status. Facility characteristics were collected\r\nregarding capacity and average daily population.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06784.v1",
+                    "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1995  "
+                }
+            ],
+            "identifier": "65",
+            "isPartOf": "2586",
+            "issued": "1997-05-16T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -3825,54 +3819,54 @@
                 "population characteristics",
                 "probation"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2586",
-            "dataQuality": false,
-            "issued": "1997-05-16T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06784.v1",
-                    "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1995  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1996  ",
-            "description": "This collection provides annual data on jail populations\r\n across the nation and examines the \"spillover\" effect on local jails\r\n resulting from the dramatic growth in federal and state prison\r\n populations. These data permit an assessment of the demands placed on\r\n correctional resources and provide a comprehensive picture of the\r\n adult correctional system and changes that occur within the system.\r\n Information is available on the number of inmates by sex, race, and\r\n adult or juvenile status. Facility characteristics were collected\r\nregarding capacity and average daily population.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "66",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1995  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This collection provides annual data on jail populations\r\n across the nation and examines the \"spillover\" effect on local jails\r\n resulting from the dramatic growth in federal and state prison\r\n populations. These data permit an assessment of the demands placed on\r\n correctional resources and provide a comprehensive picture of the\r\n adult correctional system and changes that occur within the system.\r\n Information is available on the number of inmates by sex, race, and\r\n adult or juvenile status. Facility characteristics were collected\r\nregarding capacity and average daily population.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06856.v1",
+                    "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1996  "
+                }
+            ],
+            "identifier": "66",
+            "isPartOf": "2586",
+            "issued": "1998-05-11T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -3883,54 +3877,54 @@
                 "population characteristics",
                 "probation"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2586",
-            "dataQuality": false,
-            "issued": "1998-05-11T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06856.v1",
-                    "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1996  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1997     ",
-            "description": "This collection provides annual data on jail populations\r\n across the nation and examines the \"spillover\" effect on local jails\r\n resulting from the dramatic growth in federal and state prison\r\n populations. These data permit an assessment of the demands placed on\r\n correctional resources and provide a comprehensive picture of the\r\n adult correctional system and changes that occur within the system.\r\n Information is available on the number of inmates by sex, race, and\r\n adult or juvenile status. Facility characteristics were collected\r\nregarding capacity and average daily population.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "67",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1996  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This collection provides annual data on jail populations\r\n across the nation and examines the \"spillover\" effect on local jails\r\n resulting from the dramatic growth in federal and state prison\r\n populations. These data permit an assessment of the demands placed on\r\n correctional resources and provide a comprehensive picture of the\r\n adult correctional system and changes that occur within the system.\r\n Information is available on the number of inmates by sex, race, and\r\n adult or juvenile status. Facility characteristics were collected\r\nregarding capacity and average daily population.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR02313.v1",
+                    "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1997     "
+                }
+            ],
+            "identifier": "67",
+            "isPartOf": "2586",
+            "issued": "1998-05-20T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -3941,54 +3935,54 @@
                 "population characteristics",
                 "probation"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2586",
-            "dataQuality": false,
-            "issued": "1998-05-20T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR02313.v1",
-                    "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1997     "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1998    ",
-            "description": "This collection provides annual data on jail populations\r\n across the nation and examines the \"spillover\" on local jails\r\n resulting from the dramatic growth in federal and state prison\r\n populations. These data are used to track growth in the number of\r\n jails and their capacities nationally, changes in the demographics of\r\n the jail population (including sex, race, and adult or juvenile\r\n status), supervision status of persons held, prevalence of crowding\r\n issues, and a count of non-U.S. citizens within the jail population. A\r\n special addendum to the 1998 survey included data on the prevalence\r\nand results of drug testing and treatment in jails.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "68",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1997     "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This collection provides annual data on jail populations\r\n across the nation and examines the \"spillover\" on local jails\r\n resulting from the dramatic growth in federal and state prison\r\n populations. These data are used to track growth in the number of\r\n jails and their capacities nationally, changes in the demographics of\r\n the jail population (including sex, race, and adult or juvenile\r\n status), supervision status of persons held, prevalence of crowding\r\n issues, and a count of non-U.S. citizens within the jail population. A\r\n special addendum to the 1998 survey included data on the prevalence\r\nand results of drug testing and treatment in jails.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR02682.v1",
+                    "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1998    "
+                }
+            ],
+            "identifier": "68",
+            "isPartOf": "2586",
+            "issued": "2001-07-26T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -4002,54 +3996,54 @@
                 "probation",
                 "treatment programs"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-11-04T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2586",
-            "dataQuality": false,
-            "issued": "2001-07-26T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR02682.v1",
-                    "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1998    "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails: Jurisdiction-Level Data, 2000",
-            "description": "This collection provides annual data on jail populations\r\n across the nation and examines the \"spillover\" on local jails\r\n resulting from the dramatic growth in federal and state prison\r\n populations. These data are used to track growth in the number of\r\n jails and their capacities nationally, changes in the demographics of\r\n the jail population (including sex, race, and adult or juvenile\r\n status), supervision status of persons held, prevalence of crowding\r\n issues, and a count of non-United States citizens within the jail\r\npopulation.",
-            "modified": "2008-03-27T10:09:27",
-            "accessLevel": "public",
-            "identifier": "69",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 1998    "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This collection provides annual data on jail populations\r\n across the nation and examines the \"spillover\" on local jails\r\n resulting from the dramatic growth in federal and state prison\r\n populations. These data are used to track growth in the number of\r\n jails and their capacities nationally, changes in the demographics of\r\n the jail population (including sex, race, and adult or juvenile\r\n status), supervision status of persons held, prevalence of crowding\r\n issues, and a count of non-United States citizens within the jail\r\npopulation.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03882.v1",
+                    "title": "Annual Survey of Jails: Jurisdiction-Level Data, 2000"
+                }
+            ],
+            "identifier": "69",
+            "isPartOf": "2586",
+            "issued": "2004-02-24T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -4060,54 +4054,54 @@
                 "population characteristics",
                 "probation"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-03-27T10:09:27",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2586",
-            "dataQuality": false,
-            "issued": "2004-02-24T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03882.v1",
-                    "title": "Annual Survey of Jails: Jurisdiction-Level Data, 2000"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 2001  ",
-            "description": "This collection provides annual data on jail populations\r\n across the nation and examines the \"spillover\" on local jails\r\n resulting from the dramatic growth in federal and state prison\r\n populations. These data are used to track growth in the number of\r\n jails and their capacities nationally, changes in the demographics of\r\n the jail population (including sex, race, and adult or juvenile\r\n status), supervision status of persons held, prevalence of crowding\r\n issues, and a count of non-United States citizens within the jail\r\npopulation.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "70",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Survey of Jails: Jurisdiction-Level Data, 2000"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This collection provides annual data on jail populations\r\n across the nation and examines the \"spillover\" on local jails\r\n resulting from the dramatic growth in federal and state prison\r\n populations. These data are used to track growth in the number of\r\n jails and their capacities nationally, changes in the demographics of\r\n the jail population (including sex, race, and adult or juvenile\r\n status), supervision status of persons held, prevalence of crowding\r\n issues, and a count of non-United States citizens within the jail\r\npopulation.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03883.v1",
+                    "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 2001  "
+                }
+            ],
+            "identifier": "70",
+            "isPartOf": "2586",
+            "issued": "2004-02-24T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -4118,54 +4112,54 @@
                 "population characteristics",
                 "probation"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-11-04T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2586",
-            "dataQuality": false,
-            "issued": "2004-02-24T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03883.v1",
-                    "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 2001  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 2002",
-            "description": "This collection provides annual data on jail populations\r\n across the nation and examines the \"spillover\" on local jails\r\n resulting from the dramatic growth in federal and state prison\r\n populations. These data are used to track growth in the number of\r\n jails and their capacities nationally, changes in the demographics of\r\n the jail population (including sex, race, and adult or juvenile\r\n status), supervision status of persons held, prevalence of crowding\r\n issues, and a count of non-United States citizens within the jail\r\npopulation.",
-            "modified": "2006-04-05T00:00:00",
-            "accessLevel": "public",
-            "identifier": "71",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 2001  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This collection provides annual data on jail populations\r\n across the nation and examines the \"spillover\" on local jails\r\n resulting from the dramatic growth in federal and state prison\r\n populations. These data are used to track growth in the number of\r\n jails and their capacities nationally, changes in the demographics of\r\n the jail population (including sex, race, and adult or juvenile\r\n status), supervision status of persons held, prevalence of crowding\r\n issues, and a count of non-United States citizens within the jail\r\npopulation.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04428.v1",
+                    "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 2002"
+                }
+            ],
+            "identifier": "71",
+            "isPartOf": "2586",
+            "issued": "2006-04-05T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -4176,54 +4170,54 @@
                 "population characteristics",
                 "probation"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2006-04-05T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2586",
-            "dataQuality": false,
-            "issued": "2006-04-05T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04428.v1",
-                    "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 2002"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails: Jurisdiction-Level Data, 2003",
-            "description": "This collection provides annual data on jail populations\r\n across the nation and examines the \"spillover\" on local jails\r\n resulting from the dramatic growth in federal and state prison\r\n populations. These data are used to track growth in the number of\r\n jails and their capacities nationally, changes in the demographics of\r\n the jail population (including sex, race, and adult or juvenile\r\n status), supervision status of persons held, prevalence of crowding\r\n issues, and a count of non-United States citizens within the jail\r\npopulation.",
-            "modified": "2008-03-27T13:15:14",
-            "accessLevel": "public",
-            "identifier": "72",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Survey of Jails:  Jurisdiction-Level Data, 2002"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This collection provides annual data on jail populations\r\n across the nation and examines the \"spillover\" on local jails\r\n resulting from the dramatic growth in federal and state prison\r\n populations. These data are used to track growth in the number of\r\n jails and their capacities nationally, changes in the demographics of\r\n the jail population (including sex, race, and adult or juvenile\r\n status), supervision status of persons held, prevalence of crowding\r\n issues, and a count of non-United States citizens within the jail\r\npopulation.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04635.v1",
+                    "title": "Annual Survey of Jails: Jurisdiction-Level Data, 2003"
+                }
+            ],
+            "identifier": "72",
+            "isPartOf": "2586",
+            "issued": "2007-05-25T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -4233,54 +4227,54 @@
                 "population characteristics",
                 "probation"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-03-27T13:15:14",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2586",
-            "dataQuality": false,
-            "issued": "2007-05-25T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04635.v1",
-                    "title": "Annual Survey of Jails: Jurisdiction-Level Data, 2003"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails: Jurisdiction-Level Data, 2004",
-            "description": "This collection provides annual data on jail populations\r\n across the nation and examines the \"spillover\" on local jails\r\n resulting from the dramatic growth in federal and state prison\r\n populations. These data are used to track growth in the number of\r\n jails and their capacities nationally, changes in the demographics of\r\n the jail population (including sex, race, and adult or juvenile\r\n status), supervision status of persons held, prevalence of crowding\r\n issues, and a count of non-United States citizens within the jail\r\npopulation.",
-            "modified": "2007-07-06T00:00:00",
-            "accessLevel": "public",
-            "identifier": "73",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Survey of Jails: Jurisdiction-Level Data, 2003"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This collection provides annual data on jail populations\r\n across the nation and examines the \"spillover\" on local jails\r\n resulting from the dramatic growth in federal and state prison\r\n populations. These data are used to track growth in the number of\r\n jails and their capacities nationally, changes in the demographics of\r\n the jail population (including sex, race, and adult or juvenile\r\n status), supervision status of persons held, prevalence of crowding\r\n issues, and a count of non-United States citizens within the jail\r\npopulation.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR20200.v1",
+                    "title": "Annual Survey of Jails: Jurisdiction-Level Data, 2004"
+                }
+            ],
+            "identifier": "73",
+            "isPartOf": "2586",
+            "issued": "2007-06-19T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -4290,54 +4284,54 @@
                 "population characteristics",
                 "probation"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2007-07-06T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2586",
-            "dataQuality": false,
-            "issued": "2007-06-19T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR20200.v1",
-                    "title": "Annual Survey of Jails: Jurisdiction-Level Data, 2004"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails: Jurisdiction-Level Data, 2006",
-            "description": "This collection provides annual data on jail populations\r\n across the nation and examines the \"spillover\" on local jails\r\n resulting from the dramatic growth in federal and state prison\r\n populations. These data are used to track growth in the number of\r\n jails and their capacities nationally, changes in the demographics of\r\n the jail population (including sex, race, and adult or juvenile\r\n status), supervision status of persons held, prevalence of crowding\r\n issues, and a count of non-United States citizens within the jail\r\npopulation.",
-            "modified": "2007-07-27T00:00:00",
-            "accessLevel": "public",
-            "identifier": "74",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Annual Survey of Jails: Jurisdiction-Level Data, 2004"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This collection provides annual data on jail populations\r\n across the nation and examines the \"spillover\" on local jails\r\n resulting from the dramatic growth in federal and state prison\r\n populations. These data are used to track growth in the number of\r\n jails and their capacities nationally, changes in the demographics of\r\n the jail population (including sex, race, and adult or juvenile\r\n status), supervision status of persons held, prevalence of crowding\r\n issues, and a count of non-United States citizens within the jail\r\npopulation.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR20368.v1",
+                    "title": "Annual Survey of Jails: Jurisdiction-Level Data, 2006"
+                }
+            ],
+            "identifier": "74",
+            "isPartOf": "2586",
+            "issued": "2007-07-27T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -4347,54 +4341,54 @@
                 "population characteristics",
                 "probation"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2007-07-27T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2586",
-            "dataQuality": false,
-            "issued": "2007-07-27T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR20368.v1",
-                    "title": "Annual Survey of Jails: Jurisdiction-Level Data, 2006"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Arrest Data",
-            "description": "The underlying data are from the FBI's Uniform Crime Reporting (UCR) Program. BJS has expanded upon the FBI's estimates to provide national arrest estimates detailed by offense, sex, age, and race.",
-            "modified": "2013-01-01T00:00:00",
-            "accessLevel": "public",
-            "identifier": "75",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Annual Survey of Jails: Jurisdiction-Level Data, 2006"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The underlying data are from the FBI's Uniform Crime Reporting (UCR) Program. BJS has expanded upon the FBI's estimates to provide national arrest estimates detailed by offense, sex, age, and race.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.bjs.gov/index.cfm?ty=datool&surl=/arrests/index.cfm",
+                    "mediaType": "text/html",
+                    "title": "Arrest Data"
+                }
+            ],
+            "identifier": "75",
+            "issued": "2013-01-01T00:00:00",
             "keyword": [
                 "Arrest rate",
                 "Violent Crime Index",
@@ -4411,54 +4405,54 @@
                 "Sex offenses",
                 "Drug"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-01-01T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "2013-01-01T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.bjs.gov/index.cfm?ty=datool&surl=/arrests/index.cfm",
-                    "mediaType": "text/html",
-                    "title": "Arrest Data"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Census of Jail Facilities, 2006",
-            "description": "To reduce respondent burden and improve data quality and timeliness, the Bureau of Justice Statistics (BJS) split the jail census into two parts: The Census of Jail Inmates was conducted with a reference date of June 30, 2005. The following spring it was followed by this enumeration, the Census of Jail Facilities, which collected data as of March 31, 2006. Previous jail enumerations were conducted in 1970 (ICPSR 7641), 1972 (ICPSR 7638), 1978 (ICPSR 7737), 1983 (ICPSR 8203), 1988 (ICPSR 9256), 1993 (ICPSR 6648), and 1999 (ICPSR 3318). The United States Census Bureau collected the data for the Bureau of Justice Statistics.\r\nThe 2006 Census of Jail Facilities gathered data from all jail detention facilities holding inmates beyond arraignment, a period normally exceeding 72 hours. Jail facilities were operated by cities and counties, by private entities under contract to correctional authorities, and by the Federal Bureau of Prisons (BOP).\r\nExcluded from the census were physically separate temporary holding facilities such as drunk tanks and police lockups that do not hold persons after being formally charged in court. Also excluded were state-operated facilities in Connecticut, Delaware, Hawaii, Rhode Island, Vermont, and Alaska, which have combined jail-prison systems. Fifteen independently operated jails in Alaska were included in the Census.\r\nThe census collected jurisdictional level information on the\r\nnumber of confined inmates; average daily population; number of\r\nseparate jail facilities; renovation and building plans; court\r\norders and consent decrees; staff by occupational category and\r\nrace/ethnicity; jail programs; and costs of operation. The\r\ncensus also collected individual jail facility information on\r\nthe purpose for which the jail held offenders; gender of the\r\ninmates authorized to house; functions, such as general adult\r\npopulation confinement, work release, and medical treatment;\r\nwhether a separate temporary holding area or lockup was\r\noperated; rated capacity; number of confined inmates by gender\r\nand adult or juvenile status; year of original construction;\r\nand whether the facility ever had a major renovation.",
-            "modified": "2010-01-26T16:16:17",
-            "accessLevel": "public",
-            "identifier": "76",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Arrest Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "To reduce respondent burden and improve data quality and timeliness, the Bureau of Justice Statistics (BJS) split the jail census into two parts: The Census of Jail Inmates was conducted with a reference date of June 30, 2005. The following spring it was followed by this enumeration, the Census of Jail Facilities, which collected data as of March 31, 2006. Previous jail enumerations were conducted in 1970 (ICPSR 7641), 1972 (ICPSR 7638), 1978 (ICPSR 7737), 1983 (ICPSR 8203), 1988 (ICPSR 9256), 1993 (ICPSR 6648), and 1999 (ICPSR 3318). The United States Census Bureau collected the data for the Bureau of Justice Statistics.\r\nThe 2006 Census of Jail Facilities gathered data from all jail detention facilities holding inmates beyond arraignment, a period normally exceeding 72 hours. Jail facilities were operated by cities and counties, by private entities under contract to correctional authorities, and by the Federal Bureau of Prisons (BOP).\r\nExcluded from the census were physically separate temporary holding facilities such as drunk tanks and police lockups that do not hold persons after being formally charged in court. Also excluded were state-operated facilities in Connecticut, Delaware, Hawaii, Rhode Island, Vermont, and Alaska, which have combined jail-prison systems. Fifteen independently operated jails in Alaska were included in the Census.\r\nThe census collected jurisdictional level information on the\r\nnumber of confined inmates; average daily population; number of\r\nseparate jail facilities; renovation and building plans; court\r\norders and consent decrees; staff by occupational category and\r\nrace/ethnicity; jail programs; and costs of operation. The\r\ncensus also collected individual jail facility information on\r\nthe purpose for which the jail held offenders; gender of the\r\ninmates authorized to house; functions, such as general adult\r\npopulation confinement, work release, and medical treatment;\r\nwhether a separate temporary holding area or lockup was\r\noperated; rated capacity; number of confined inmates by gender\r\nand adult or juvenile status; year of original construction;\r\nand whether the facility ever had a major renovation.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR26602.v1",
+                    "title": "Census of Jail Facilities, 2006"
+                }
+            ],
+            "identifier": "76",
+            "isPartOf": "2169",
+            "issued": "2010-01-26T16:16:17",
             "keyword": [
                 "census data",
                 "correctional facilities",
@@ -4473,54 +4467,54 @@
                 "jails",
                 "personnel"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-01-26T16:16:17",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2169",
-            "dataQuality": false,
-            "issued": "2010-01-26T16:16:17",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR26602.v1",
-                    "title": "Census of Jail Facilities, 2006"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Census of Jail Inmates: Individual-Level Data, 2005",
-            "description": "The Census of Jail Inmates is the eighth in a series of\r\n data collection efforts aimed at studying the nation's\r\n locally-administered jails. Beginning in 2005, the National Jail\r\n Census was broken out into two collections. The 2005 Census of Jail\r\n Inmates (CJI) collects data on the facilities' supervised populations,\r\n inmate counts and movements, and persons supervised in the community.\r\n The forthcoming 2006 Census of Jail Facilities collects information\r\n on staffing levels, programming, and facility policies. Previous\r\n censuses were conducted in 1970, 1972, 1978, 1983, 1988, 1993, and\r\n 1999. The 2005 CJI enumerated 2,960 locally administered confinement\r\n facilities that held inmates beyond arraignment and were staffed by\r\n municipal or county employees. Among these were 42 privately-operated\r\n jails under contract to local governments and 65 regional jails that\r\n were operated for two or more jail authorities. In addition, the\r\n census identified 12 facilities maintained by the Federal Bureau of\r\n Prisons that functioned as jails. These 12 facilities, together with\r\n the 2,960 nonfederal facilities, brought the number of jails in\r\n operation on June 30, 2005, to a nationwide total of 2,972. The CJI\r\n supplies data on characteristics of jails such as admissions and\r\n releases, growth in the number of jail facilities, changes in their\r\n rated capacities and level of occupancy, crowding issues, growth in\r\n the population supervised in the community, and changes in methods of\r\n community supervision. The CJI also provides information on changes in\r\n the demographics of the jail population, supervision status of persons\r\n held, and a count of non-United States citizens in custody. The data\r\n are intended for a variety of users, including federal and state\r\n agencies, local officials in conjunction with jail administrators,\r\nresearchers, planners, and the public.",
-            "modified": "2007-07-27T00:00:00",
-            "accessLevel": "public",
-            "identifier": "77",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Census of Jail Facilities, 2006"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The Census of Jail Inmates is the eighth in a series of\r\n data collection efforts aimed at studying the nation's\r\n locally-administered jails. Beginning in 2005, the National Jail\r\n Census was broken out into two collections. The 2005 Census of Jail\r\n Inmates (CJI) collects data on the facilities' supervised populations,\r\n inmate counts and movements, and persons supervised in the community.\r\n The forthcoming 2006 Census of Jail Facilities collects information\r\n on staffing levels, programming, and facility policies. Previous\r\n censuses were conducted in 1970, 1972, 1978, 1983, 1988, 1993, and\r\n 1999. The 2005 CJI enumerated 2,960 locally administered confinement\r\n facilities that held inmates beyond arraignment and were staffed by\r\n municipal or county employees. Among these were 42 privately-operated\r\n jails under contract to local governments and 65 regional jails that\r\n were operated for two or more jail authorities. In addition, the\r\n census identified 12 facilities maintained by the Federal Bureau of\r\n Prisons that functioned as jails. These 12 facilities, together with\r\n the 2,960 nonfederal facilities, brought the number of jails in\r\n operation on June 30, 2005, to a nationwide total of 2,972. The CJI\r\n supplies data on characteristics of jails such as admissions and\r\n releases, growth in the number of jail facilities, changes in their\r\n rated capacities and level of occupancy, crowding issues, growth in\r\n the population supervised in the community, and changes in methods of\r\n community supervision. The CJI also provides information on changes in\r\n the demographics of the jail population, supervision status of persons\r\n held, and a count of non-United States citizens in custody. The data\r\n are intended for a variety of users, including federal and state\r\n agencies, local officials in conjunction with jail administrators,\r\nresearchers, planners, and the public.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR20367.v1",
+                    "title": "Census of Jail Inmates: Individual-Level Data, 2005"
+                }
+            ],
+            "identifier": "77",
+            "isPartOf": "2169",
+            "issued": "2007-07-27T00:00:00",
             "keyword": [
                 "census data",
                 "correctional facilities",
@@ -4533,107 +4527,106 @@
                 "jail inmates",
                 "jails"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2007-07-27T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2169",
-            "dataQuality": false,
-            "issued": "2007-07-27T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR20367.v1",
-                    "title": "Census of Jail Inmates: Individual-Level Data, 2005"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Census of Law Enforcement Aviation Units, 2007 [United States]",
-            "description": "The 2007 Census of Law Enforcement Aviation Units is the first systematic, national-level data collection providing information about law enforcement aviation assets and functions.  In general, these units provide valuable airborne support for traditional ground-based police operations.  An additional role following the September 11, 2001 terrorist attacks is the provision of essential\r\nhomeland security functions, such as providing critical facility checks of buildings, ports and harbors, public utilities, inland waterways, oil refineries, bridges and spans, water storage/reservoirs, National and/or State monuments, water treatment plants, irrigation facilities, airports, and natural resources.  Aviation units are thought to be able to perform critical facility checks and routine patrol and support operations with greater efficiency than ground-based personnel. However, little is presently known about the equipment, personnel, operations, expenditures, and safety requirements of these units on a national level. This information is critical to law enforcement policy development, planning, and budgeting at all levels of government.\r\nThe data will supply law enforcement agencies with a benchmark for comparative analysis with other similarly situated agencies, and increase understanding of the support that aviation units provide to ground-based police operations.",
-            "modified": "2009-12-07T07:42:47",
-            "accessLevel": "public",
-            "identifier": "78",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Census of Jail Inmates: Individual-Level Data, 2005"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2007 Census of Law Enforcement Aviation Units is the first systematic, national-level data collection providing information about law enforcement aviation assets and functions.  In general, these units provide valuable airborne support for traditional ground-based police operations.  An additional role following the September 11, 2001 terrorist attacks is the provision of essential\r\nhomeland security functions, such as providing critical facility checks of buildings, ports and harbors, public utilities, inland waterways, oil refineries, bridges and spans, water storage/reservoirs, National and/or State monuments, water treatment plants, irrigation facilities, airports, and natural resources.  Aviation units are thought to be able to perform critical facility checks and routine patrol and support operations with greater efficiency than ground-based personnel. However, little is presently known about the equipment, personnel, operations, expenditures, and safety requirements of these units on a national level. This information is critical to law enforcement policy development, planning, and budgeting at all levels of government.\r\nThe data will supply law enforcement agencies with a benchmark for comparative analysis with other similarly situated agencies, and increase understanding of the support that aviation units provide to ground-based police operations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR25482.v1",
+                    "title": "Census of Law Enforcement Aviation Units, 2007 [United States]"
+                }
+            ],
+            "identifier": "78",
+            "issued": "2009-12-02T14:47:54",
             "keyword": [
                 "aircraft",
                 "law enforcement",
                 "national security",
                 "police equipment"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-12-07T07:42:47",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "2009-12-02T14:47:54",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR25482.v1",
-                    "title": "Census of Law Enforcement Aviation Units, 2007 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Census of Law Enforcement Gang Units, 2007",
-            "description": "The 2007 Census of Law Enforcement Gang Units (CLEGU) collected data from all state and local law enforcement agencies with 100 or more sworn officers and at least one officer dedicated solely to addressing gangs and gang activities. Law enforcement agencies are often the first line of response to the gang problems experienced across the country and are a critical component of most anti-gang initiatives. One way for law enforcement agencies to address gang-related problems is to form specialized gang units. The consolidation of an agency's gang enforcement activities and resources into a single unit can allow gang unit officers to develop specific expertise and technical skills related to local gang characteristics and behaviors and gang prevention and suppression.\r\nNo prior studies have collected data regarding the organization and operations of law enforcement gang units nationwide, the types of gang prevention tactics employed, or the characteristics and training of gang unit officers.\r\nThis CLEGU collected data on the operations, workload, policies, and procedures of gang units in large state and local law enforcement agencies in order to expand knowledge of gang prevention and enforcement tactics.  The CLEGU also collected summary measures of gang activity in the agencies' jurisdictions to allow for comparison across jurisdictions with similar gang problems.",
-            "modified": "2011-03-22T16:21:43",
-            "accessLevel": "public",
-            "identifier": "79",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Census of Law Enforcement Aviation Units, 2007 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2007 Census of Law Enforcement Gang Units (CLEGU) collected data from all state and local law enforcement agencies with 100 or more sworn officers and at least one officer dedicated solely to addressing gangs and gang activities. Law enforcement agencies are often the first line of response to the gang problems experienced across the country and are a critical component of most anti-gang initiatives. One way for law enforcement agencies to address gang-related problems is to form specialized gang units. The consolidation of an agency's gang enforcement activities and resources into a single unit can allow gang unit officers to develop specific expertise and technical skills related to local gang characteristics and behaviors and gang prevention and suppression.\r\nNo prior studies have collected data regarding the organization and operations of law enforcement gang units nationwide, the types of gang prevention tactics employed, or the characteristics and training of gang unit officers.\r\nThis CLEGU collected data on the operations, workload, policies, and procedures of gang units in large state and local law enforcement agencies in order to expand knowledge of gang prevention and enforcement tactics.  The CLEGU also collected summary measures of gang activity in the agencies' jurisdictions to allow for comparison across jurisdictions with similar gang problems.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR29503.v1",
+                    "title": "Census of Law Enforcement Gang Units, 2007"
+                }
+            ],
+            "identifier": "79",
+            "issued": "2011-03-22T16:21:43",
             "keyword": [
                 "gangs",
                 "law enforcement agencies",
@@ -4641,53 +4634,53 @@
                 "police departments",
                 "policies and procedures"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-22T16:21:43",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "2011-03-22T16:21:43",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR29503.v1",
-                    "title": "Census of Law Enforcement Gang Units, 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Census of Law Enforcement Training Academies, 2002: [United States]  ",
-            "description": "The 2002 Census of Law Enforcement Training Academies\r\n (CLETA02) was the first effort by the Bureau of Justice Statistics\r\n (BJS) to collect information from law enforcement training academies\r\n across the United States. The CLETA02 included all currently\r\n operating academies that provided basic law enforcement training.\r\n Academies that provided only in-service training,\r\n corrections/detention training, or other special types of training\r\n were excluded. Data were collected on personnel, expenditures,\r\n facilities, equipment, trainees, training curricula, and a variety of\r\n special topic areas. As of year-end 2002, a total of 626 law\r\n enforcement academies operating in the United States offered basic law\r\n enforcement training to individuals recruited or seeking to become law\r\nenforcement officers.",
-            "modified": "2005-06-09T00:00:00",
-            "accessLevel": "public",
-            "identifier": "80",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Census of Law Enforcement Gang Units, 2007"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2002 Census of Law Enforcement Training Academies\r\n (CLETA02) was the first effort by the Bureau of Justice Statistics\r\n (BJS) to collect information from law enforcement training academies\r\n across the United States. The CLETA02 included all currently\r\n operating academies that provided basic law enforcement training.\r\n Academies that provided only in-service training,\r\n corrections/detention training, or other special types of training\r\n were excluded. Data were collected on personnel, expenditures,\r\n facilities, equipment, trainees, training curricula, and a variety of\r\n special topic areas. As of year-end 2002, a total of 626 law\r\n enforcement academies operating in the United States offered basic law\r\n enforcement training to individuals recruited or seeking to become law\r\nenforcement officers.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04255.v1",
+                    "title": "Census of Law Enforcement Training Academies, 2002: [United States]  "
+                }
+            ],
+            "identifier": "80",
+            "issued": "2005-06-09T00:00:00",
             "keyword": [
                 "census data",
                 "law enforcement",
@@ -4695,53 +4688,53 @@
                 "police officers",
                 "police training"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-06-09T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "2005-06-09T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04255.v1",
-                    "title": "Census of Law Enforcement Training Academies, 2002: [United States]  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Census of Public Defender Offices: County-Based and Local Offices, 2007",
-            "description": "The Bureau of Justice Statistics' (BJS) 2007 Census of Public Defender Offices (CPDO) collected data from public defender offices located across 49 states and the District of Columbia.  Public defender offices are one of three methods through which states and localities ensure that indigent defendants are granted the Sixth and Fourteenth Amendment right to counsel. (In addition to defender offices, indigent defense services may also be provided by court-assigned private counsel or by a contract system in which private attorneys contractually agree to take on a specified number of indigent defendants or indigent defense cases.) Public defender offices have a salaried staff of full- or part-time attorneys who represent indigent defendants and are employed as direct government employees or through a public, nonprofit organization.\r\nPublic defenders play an important role in the United States criminal justice system.  Data from prior BJS surveys on indigent defense representation indicate that most criminal defendants rely on some form of publicly provided defense counsel, primarily public defenders. Although the United States Supreme Court has mandated that the states provide counsel for indigent persons accused of crime, documentation on the nature and provision of these services has not been readily available.\r\nStates have devised various systems, rules of organization, and funding mechanisms for indigent defense programs. While the operation and funding of public defender offices varies across states, public defender offices can be generally classified as being part of either a state program or a county-based system. The 22 state public defender programs functioned entirely under the direction of a central administrative office that funded and administered all the public defender offices in the state. For the 28 states with county-based offices, indigent defense services were administered at the county or local jurisdictional level and funded principally by the county or through a combination of county and state funds.\r\nThe CPDO collected data from both state- and county-based offices. All public defender offices that were principally funded by state or local governments and provided general criminal defense services, conflict services, or capital case representation were within the scope of the study. Federal public defender offices and offices that provided primarily contract or assigned counsel services with private attorneys were excluded from the data collection. In addition, public defender offices that were principally funded by a tribal government, or provided primarily appellate or juvenile services were outside the scope of the project and were also excluded.\r\nThe CPDO gathered information on public defender office staffing, expenditures, attorney training, standards and guidelines, and caseloads, including the number and type of cases received by the offices. The data collected by the CPDO can be compared to and analyzed against many of the existing national standards for the provision of indigent defense services.",
-            "modified": "2011-05-13T11:26:36",
-            "accessLevel": "public",
-            "identifier": "81",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Census of Law Enforcement Training Academies, 2002: [United States]  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The Bureau of Justice Statistics' (BJS) 2007 Census of Public Defender Offices (CPDO) collected data from public defender offices located across 49 states and the District of Columbia.  Public defender offices are one of three methods through which states and localities ensure that indigent defendants are granted the Sixth and Fourteenth Amendment right to counsel. (In addition to defender offices, indigent defense services may also be provided by court-assigned private counsel or by a contract system in which private attorneys contractually agree to take on a specified number of indigent defendants or indigent defense cases.) Public defender offices have a salaried staff of full- or part-time attorneys who represent indigent defendants and are employed as direct government employees or through a public, nonprofit organization.\r\nPublic defenders play an important role in the United States criminal justice system.  Data from prior BJS surveys on indigent defense representation indicate that most criminal defendants rely on some form of publicly provided defense counsel, primarily public defenders. Although the United States Supreme Court has mandated that the states provide counsel for indigent persons accused of crime, documentation on the nature and provision of these services has not been readily available.\r\nStates have devised various systems, rules of organization, and funding mechanisms for indigent defense programs. While the operation and funding of public defender offices varies across states, public defender offices can be generally classified as being part of either a state program or a county-based system. The 22 state public defender programs functioned entirely under the direction of a central administrative office that funded and administered all the public defender offices in the state. For the 28 states with county-based offices, indigent defense services were administered at the county or local jurisdictional level and funded principally by the county or through a combination of county and state funds.\r\nThe CPDO collected data from both state- and county-based offices. All public defender offices that were principally funded by state or local governments and provided general criminal defense services, conflict services, or capital case representation were within the scope of the study. Federal public defender offices and offices that provided primarily contract or assigned counsel services with private attorneys were excluded from the data collection. In addition, public defender offices that were principally funded by a tribal government, or provided primarily appellate or juvenile services were outside the scope of the project and were also excluded.\r\nThe CPDO gathered information on public defender office staffing, expenditures, attorney training, standards and guidelines, and caseloads, including the number and type of cases received by the offices. The data collected by the CPDO can be compared to and analyzed against many of the existing national standards for the provision of indigent defense services.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR29502.v1",
+                    "title": "Census of Public Defender Offices: County-Based and Local Offices, 2007"
+                }
+            ],
+            "identifier": "81",
+            "issued": "2011-05-13T11:26:36",
             "keyword": [
                 "expenditures",
                 "law enforcement agencies",
@@ -4750,53 +4743,53 @@
                 "police departments",
                 "policies and procedures"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-05-13T11:26:36",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "2011-05-13T11:26:36",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR29502.v1",
-                    "title": "Census of Public Defender Offices: County-Based and Local Offices, 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Census of Public Defender Offices: State Programs, 2007",
-            "description": "The Bureau of Justice Statistics' (BJS) 2007 Census of Public Defender Offices (CPDO) collected data from public defender offices located across 49 states and the District of Columbia.  Public defender offices are one of three methods through which states and localities ensure that indigent defendants are granted the Sixth and Fourteenth Amendment right to counsel. (In addition to defender offices, indigent defense services may also be provided by court-assigned private counsel or by a contract system in which private attorneys contractually agree to take on a specified number of indigent defendants or indigent defense cases.) Public defender offices have a salaried staff of full- or part-time attorneys who represent indigent defendants and are employed as direct government employees or through a public, nonprofit organization.\r\nPublic defenders play an important role in the United States criminal justice system.  Data from prior BJS surveys on indigent defense representation indicate that most criminal defendants rely on some form of publicly provided defense counsel, primarily public defenders. Although the United States Supreme Court has mandated that the states provide counsel for indigent persons accused of crime, documentation on the nature and provision of these services has not been readily available.\r\nStates have devised various systems, rules of organization, and funding mechanisms for indigent defense programs. While the operation and funding of public defender offices varies across states, public defender offices can be generally classified as being part of either a state program or a county-based system. The 22 state public defender programs functioned entirely under the direction of a central administrative office that funded and administered all the public defender offices in the state. For the 28 states with county-based offices, indigent defense services were administered at the county or local jurisdictional level and funded principally by the county or through a combination of county and state funds.\r\nThe CPDO collected data from both state- and county-based offices. All public defender offices that were principally funded by state or local governments and provided general criminal defense services, conflict services, or capital case representation were within the scope of the study. Federal public defender offices and offices that provided primarily contract or assigned counsel services with private attorneys were excluded from the data collection. In addition, public defender offices that were principally funded by a tribal government, or provided primarily appellate or juvenile services were outside the scope of the project and were also excluded.\r\nThe CPDO gathered information on public defender office staffing, expenditures, attorney training, standards and guidelines, and caseloads, including the number and type of cases received by the offices. The data collected by the CPDO can be compared to and analyzed against many of the existing national standards for the provision of indigent defense services.",
-            "modified": "2011-05-13T10:50:57",
-            "accessLevel": "public",
-            "identifier": "82",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Census of Public Defender Offices: County-Based and Local Offices, 2007"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The Bureau of Justice Statistics' (BJS) 2007 Census of Public Defender Offices (CPDO) collected data from public defender offices located across 49 states and the District of Columbia.  Public defender offices are one of three methods through which states and localities ensure that indigent defendants are granted the Sixth and Fourteenth Amendment right to counsel. (In addition to defender offices, indigent defense services may also be provided by court-assigned private counsel or by a contract system in which private attorneys contractually agree to take on a specified number of indigent defendants or indigent defense cases.) Public defender offices have a salaried staff of full- or part-time attorneys who represent indigent defendants and are employed as direct government employees or through a public, nonprofit organization.\r\nPublic defenders play an important role in the United States criminal justice system.  Data from prior BJS surveys on indigent defense representation indicate that most criminal defendants rely on some form of publicly provided defense counsel, primarily public defenders. Although the United States Supreme Court has mandated that the states provide counsel for indigent persons accused of crime, documentation on the nature and provision of these services has not been readily available.\r\nStates have devised various systems, rules of organization, and funding mechanisms for indigent defense programs. While the operation and funding of public defender offices varies across states, public defender offices can be generally classified as being part of either a state program or a county-based system. The 22 state public defender programs functioned entirely under the direction of a central administrative office that funded and administered all the public defender offices in the state. For the 28 states with county-based offices, indigent defense services were administered at the county or local jurisdictional level and funded principally by the county or through a combination of county and state funds.\r\nThe CPDO collected data from both state- and county-based offices. All public defender offices that were principally funded by state or local governments and provided general criminal defense services, conflict services, or capital case representation were within the scope of the study. Federal public defender offices and offices that provided primarily contract or assigned counsel services with private attorneys were excluded from the data collection. In addition, public defender offices that were principally funded by a tribal government, or provided primarily appellate or juvenile services were outside the scope of the project and were also excluded.\r\nThe CPDO gathered information on public defender office staffing, expenditures, attorney training, standards and guidelines, and caseloads, including the number and type of cases received by the offices. The data collected by the CPDO can be compared to and analyzed against many of the existing national standards for the provision of indigent defense services.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR29501.v1",
+                    "title": "Census of Public Defender Offices: State Programs, 2007"
+                }
+            ],
+            "identifier": "82",
+            "issued": "2011-05-13T10:50:57",
             "keyword": [
                 "defendants",
                 "expenditures",
@@ -4807,53 +4800,54 @@
                 "policies and procedures",
                 "public defenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-05-13T10:50:57",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "2011-05-13T10:50:57",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR29501.v1",
-                    "title": "Census of Public Defender Offices: State Programs, 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Census of Publicly Funded Forensic Crime Laboratories, 2002",
-            "description": "To obtain current baseline information about the workload\r\n and operations of the nation's forensic crime laboratories, the Bureau\r\n of Justice Statistics (BJS) conducted its first census of publicly\r\n funded forensic crime laboratories from 2003 to 2004. Data were\r\n collected on the organization, functions, budget, staffing, workload,\r\n and performance expectations of the nation's publicly funded federal,\r\nstate, and local forensic crime laboratories currently operating.",
-            "modified": "2005-09-02T00:00:00",
-            "accessLevel": "public",
-            "identifier": "83",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Census of Public Defender Offices: State Programs, 2007"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "To obtain current baseline information about the workload\r\n and operations of the nation's forensic crime laboratories, the Bureau\r\n of Justice Statistics (BJS) conducted its first census of publicly\r\n funded forensic crime laboratories from 2003 to 2004. Data were\r\n collected on the organization, functions, budget, staffing, workload,\r\n and performance expectations of the nation's publicly funded federal,\r\nstate, and local forensic crime laboratories currently operating.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04287.v1",
+                    "title": "Census of Publicly Funded Forensic Crime Laboratories, 2002"
+                }
+            ],
+            "identifier": "83",
+            "isPartOf": "2443",
+            "issued": "2005-09-02T00:00:00",
             "keyword": [
                 "DNA fingerprinting",
                 "budgets",
@@ -4864,54 +4858,54 @@
                 "personnel",
                 "policies and procedures"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-09-02T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2443",
-            "dataQuality": false,
-            "issued": "2005-09-02T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04287.v1",
-                    "title": "Census of Publicly Funded Forensic Crime Laboratories, 2002"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Census of Publicly Funded Forensic Crime Laboratories, 2002 and 2005",
-            "description": "This data collection contains data from censuses of publicly funded crime laboratories in 2002 and 2005. The data were collected to examine change and stability in the operations of crime laboratories serving federal, state, and local jurisdictions. The Bureau of Justice Statistics (BJS) first surveyed forensic crime laboratories in 1998, focusing solely on agencies that performed DNA analysis. The National Institute of Justice (NIJ) funded the 1998 study as part of its DNA Laboratory Improvement Program. The BJS' National Study of DNA Laboratories was repeated in 2001. An expanded version of the data collection, called the Census of Publicly Funded Forensic Crime Laboratories, was first conducted among all forensic crime laboratories in 2002. Data were collected from 2003 to 2004 on the organization, functions, budget, staffing, workload, and performance expectations of the nation's forensic crime laboratories operating in 2002. A total of 306 of the 351 crime laboratories operating in 2002 responded to the census. The latest census obtained data from 351 of the 389 laboratories operating in 2005, including at least 1 laboratory from every state. The nation's publicly funded forensic crime laboratories performed a variety of forensic services in 2005, including DNA testing and controlled substance identification for federal, state, and local jurisdictions. The 2005 Census of Publicly Funded Forensic Crime Laboratories obtained detailed information on the types of forensic requests received by these laboratories and the resources needed to complete them. The census also collected data on crime laboratory budgets, personnel, accreditations, and backlogged cases.",
-            "modified": "2008-10-24T13:33:38",
-            "accessLevel": "public",
-            "identifier": "84",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Census of Publicly Funded Forensic Crime Laboratories, 2002"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection contains data from censuses of publicly funded crime laboratories in 2002 and 2005. The data were collected to examine change and stability in the operations of crime laboratories serving federal, state, and local jurisdictions. The Bureau of Justice Statistics (BJS) first surveyed forensic crime laboratories in 1998, focusing solely on agencies that performed DNA analysis. The National Institute of Justice (NIJ) funded the 1998 study as part of its DNA Laboratory Improvement Program. The BJS' National Study of DNA Laboratories was repeated in 2001. An expanded version of the data collection, called the Census of Publicly Funded Forensic Crime Laboratories, was first conducted among all forensic crime laboratories in 2002. Data were collected from 2003 to 2004 on the organization, functions, budget, staffing, workload, and performance expectations of the nation's forensic crime laboratories operating in 2002. A total of 306 of the 351 crime laboratories operating in 2002 responded to the census. The latest census obtained data from 351 of the 389 laboratories operating in 2005, including at least 1 laboratory from every state. The nation's publicly funded forensic crime laboratories performed a variety of forensic services in 2005, including DNA testing and controlled substance identification for federal, state, and local jurisdictions. The 2005 Census of Publicly Funded Forensic Crime Laboratories obtained detailed information on the types of forensic requests received by these laboratories and the resources needed to complete them. The census also collected data on crime laboratory budgets, personnel, accreditations, and backlogged cases.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23120.v1",
+                    "title": "Census of Publicly Funded Forensic Crime Laboratories, 2002 and 2005"
+                }
+            ],
+            "identifier": "84",
+            "isPartOf": "2443",
+            "issued": "2008-10-24T13:33:38",
             "keyword": [
                 "DNA fingerprinting",
                 "budgets",
@@ -4922,54 +4916,54 @@
                 "personnel",
                 "policies and procedures"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-10-24T13:33:38",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2443",
-            "dataQuality": false,
-            "issued": "2008-10-24T13:33:38",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23120.v1",
-                    "title": "Census of Publicly Funded Forensic Crime Laboratories, 2002 and 2005"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Census of Publicly Funded Forensic Crime Laboratories, 2009",
-            "description": "This data collection contains data from censuses of publicly funded crime laboratories in 2009. The data were collected to examine change and stability in the operations of crime laboratories serving federal, state, and local jurisdictions. The Bureau of Justice Statistics (BJS) first surveyed forensic crime laboratories in 1998, focusing solely on agencies that performed DNA analysis. The National Institute of Justice (NIJ) funded the 1998 study as part of its DNA Laboratory Improvement Program. The BJS' National Study of DNA Laboratories was repeated in 2001. An expanded version of the data collection, called the Census of Publicly Funded Forensic Crime Laboratories, was first conducted among all forensic crime laboratories in 2002. For the 2009 study, data were collected from 2010 to 2011 on the organization, functions, budget, staffing, workload, and performance expectations of the nation's forensic crime laboratories operating in 2009. A total of 397 of the 411 eligible crime laboratories operating in 2009 responded to the census, including at least 1 laboratory from every state. The nation's publicly funded forensic crime laboratories performed a variety of forensic services in 2009, including DNA testing and controlled substance identification for federal, state, and local jurisdictions. The 2009 Census of Publicly Funded Forensic Crime Laboratories obtained detailed information on the types of forensic requests received by these laboratories and the resources needed to complete them. The census also collected data on crime laboratory budgets, personnel, accreditations, and backlogged cases.",
-            "modified": "2018-01-26T12:59:16",
-            "accessLevel": "public",
-            "identifier": "85",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Census of Publicly Funded Forensic Crime Laboratories, 2002 and 2005"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection contains data from censuses of publicly funded crime laboratories in 2009. The data were collected to examine change and stability in the operations of crime laboratories serving federal, state, and local jurisdictions. The Bureau of Justice Statistics (BJS) first surveyed forensic crime laboratories in 1998, focusing solely on agencies that performed DNA analysis. The National Institute of Justice (NIJ) funded the 1998 study as part of its DNA Laboratory Improvement Program. The BJS' National Study of DNA Laboratories was repeated in 2001. An expanded version of the data collection, called the Census of Publicly Funded Forensic Crime Laboratories, was first conducted among all forensic crime laboratories in 2002. For the 2009 study, data were collected from 2010 to 2011 on the organization, functions, budget, staffing, workload, and performance expectations of the nation's forensic crime laboratories operating in 2009. A total of 397 of the 411 eligible crime laboratories operating in 2009 responded to the census, including at least 1 laboratory from every state. The nation's publicly funded forensic crime laboratories performed a variety of forensic services in 2009, including DNA testing and controlled substance identification for federal, state, and local jurisdictions. The 2009 Census of Publicly Funded Forensic Crime Laboratories obtained detailed information on the types of forensic requests received by these laboratories and the resources needed to complete them. The census also collected data on crime laboratory budgets, personnel, accreditations, and backlogged cases.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34340.v2",
+                    "title": "Census of Publicly Funded Forensic Crime Laboratories, 2009"
+                }
+            ],
+            "identifier": "85",
+            "isPartOf": "2443",
+            "issued": "2012-11-26T15:33:04",
             "keyword": [
                 "DNA fingerprinting",
                 "budgets",
@@ -4980,54 +4974,54 @@
                 "personnel",
                 "policies and procedures"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2018-01-26T12:59:16",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2443",
-            "dataQuality": false,
-            "issued": "2012-11-26T15:33:04",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34340.v2",
-                    "title": "Census of Publicly Funded Forensic Crime Laboratories, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Census of State Adult Correctional Facilities, 1979",
-            "description": "This census, designed by the Bureau of Justice Statistics\r\n and conducted by the United States Census Bureau, includes\r\n all state correctional facilities known to the Census Bureau in 1979.\r\n Each facility is classified into one of ten categories such as\r\n community center, prison farm, road camp, or reception center. Data\r\n for 1979 include number of inmates by security classification and by\r\n sex, number of full- and part-time staff, number of paid and volunteer\r\n staff broken down by position, age, pay, and education, number and age of\r\n facilities, type of facilities provided in each cell by size of cell,\r\n hospital facilities available, programs provided for the inmates, job\r\ntraining, and inmate IQ scores.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "86",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Census of Publicly Funded Forensic Crime Laboratories, 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This census, designed by the Bureau of Justice Statistics\r\n and conducted by the United States Census Bureau, includes\r\n all state correctional facilities known to the Census Bureau in 1979.\r\n Each facility is classified into one of ten categories such as\r\n community center, prison farm, road camp, or reception center. Data\r\n for 1979 include number of inmates by security classification and by\r\n sex, number of full- and part-time staff, number of paid and volunteer\r\n staff broken down by position, age, pay, and education, number and age of\r\n facilities, type of facilities provided in each cell by size of cell,\r\n hospital facilities available, programs provided for the inmates, job\r\ntraining, and inmate IQ scores.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07852.v2",
+                    "title": "Census of State Adult Correctional Facilities, 1979"
+                }
+            ],
+            "identifier": "86",
+            "isPartOf": "2168",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (adults)",
@@ -5046,54 +5040,54 @@
                 "prison overcrowding",
                 "prison violence"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2168",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07852.v2",
-                    "title": "Census of State Adult Correctional Facilities, 1979"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Census of State Adult Correctional Facilities, 1984",
-            "description": "This study provides a descriptive analysis of confinement\r\nfacilities and state-operated community-based correctional facilities\r\nnationwide. Decision-makers, practitioners, and researchers may use the\r\ncensus to analyze the current conditions and needs of state\r\ncorrectional facilities for adults. Variables of interest include\r\nphysical security, age of facilities, functions of facilities,\r\nprograms, inmate work assignments, staff employment, facilities under\r\ncourt order/consent decree for conditions of confinement, capital and\r\noperating expenditures, custody level of residents/inmates, one-day and\r\naverage daily population counts, race/ethnicity of inmates, inmate work\r\nassignments, inmate deaths, special inmate counts, and assaults and\r\nincidents by inmates. The institution is the unit of analysis.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "87",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Census of State Adult Correctional Facilities, 1979"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This study provides a descriptive analysis of confinement\r\nfacilities and state-operated community-based correctional facilities\r\nnationwide. Decision-makers, practitioners, and researchers may use the\r\ncensus to analyze the current conditions and needs of state\r\ncorrectional facilities for adults. Variables of interest include\r\nphysical security, age of facilities, functions of facilities,\r\nprograms, inmate work assignments, staff employment, facilities under\r\ncourt order/consent decree for conditions of confinement, capital and\r\noperating expenditures, custody level of residents/inmates, one-day and\r\naverage daily population counts, race/ethnicity of inmates, inmate work\r\nassignments, inmate deaths, special inmate counts, and assaults and\r\nincidents by inmates. The institution is the unit of analysis.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08444.v1",
+                    "title": "Census of State Adult Correctional Facilities, 1984"
+                }
+            ],
+            "identifier": "87",
+            "isPartOf": "2168",
+            "issued": "1987-01-12T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (adults)",
@@ -5112,54 +5106,54 @@
                 "prison security",
                 "prison violence"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-11-04T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2168",
-            "dataQuality": false,
-            "issued": "1987-01-12T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08444.v1",
-                    "title": "Census of State Adult Correctional Facilities, 1984"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Census of State and Federal Adult Correctional Facilities, 1990  ",
-            "description": "This census is the fourth enumeration of state adult\r\ncorrectional institutions and the first of federal institutions\r\nsponsored by the Bureau of Justice Statistics and conducted by the\r\nBureau of the Census. Earlier censuses were completed in 1974 (ICPSR\r\n7811), 1979 (ICPSR 7852), and 1984 (ICPSR 8444). Separate\r\nquestionnaires were devised for confinement facilities and for\r\ncommunity-based facilities. Variables describing the facilities\r\ninclude physical security, age, functions, capacity, confinement\r\nspace, available medical facilities, programs, inmate/resident work\r\nassignments, staff employment, facilities under court order/consent\r\ndecree for conditions of confinement, capital and operating\r\nexpenditures, custody level of inmates/residents, one-day count and\r\naverage daily population, race/ethnicity of inmates/residents,\r\ninmate/resident deaths, special inmate/resident counts, and assaults\r\nand incidents by inmates. An addendum on drug control activities in\r\nstate and federal facilities was included for the first time in the\r\n1990 census. Facilities were asked to provide information on the\r\nfollowing: procedures used with inmates/residents, visitors, and staff\r\nto keep out illegal drugs and drug paraphernalia, inmate/resident\r\ndrug-testing practices, including the criteria for testing\r\ninmates/residents, the number of inmates/residents tested in total and\r\nby specific drug, and the number that tested positive, staff drug\r\ntesting, including groups and basis for testing, number tested, and\r\nprocedures when tests were positive, and capacity and enrollment in\r\nvarious types of drug treatment and intervention programs.",
-            "modified": "2001-12-21T00:00:00",
-            "accessLevel": "public",
-            "identifier": "88",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Census of State Adult Correctional Facilities, 1984"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This census is the fourth enumeration of state adult\r\ncorrectional institutions and the first of federal institutions\r\nsponsored by the Bureau of Justice Statistics and conducted by the\r\nBureau of the Census. Earlier censuses were completed in 1974 (ICPSR\r\n7811), 1979 (ICPSR 7852), and 1984 (ICPSR 8444). Separate\r\nquestionnaires were devised for confinement facilities and for\r\ncommunity-based facilities. Variables describing the facilities\r\ninclude physical security, age, functions, capacity, confinement\r\nspace, available medical facilities, programs, inmate/resident work\r\nassignments, staff employment, facilities under court order/consent\r\ndecree for conditions of confinement, capital and operating\r\nexpenditures, custody level of inmates/residents, one-day count and\r\naverage daily population, race/ethnicity of inmates/residents,\r\ninmate/resident deaths, special inmate/resident counts, and assaults\r\nand incidents by inmates. An addendum on drug control activities in\r\nstate and federal facilities was included for the first time in the\r\n1990 census. Facilities were asked to provide information on the\r\nfollowing: procedures used with inmates/residents, visitors, and staff\r\nto keep out illegal drugs and drug paraphernalia, inmate/resident\r\ndrug-testing practices, including the criteria for testing\r\ninmates/residents, the number of inmates/residents tested in total and\r\nby specific drug, and the number that tested positive, staff drug\r\ntesting, including groups and basis for testing, number tested, and\r\nprocedures when tests were positive, and capacity and enrollment in\r\nvarious types of drug treatment and intervention programs.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09908.v2",
+                    "title": "Census of State and Federal Adult Correctional Facilities, 1990  "
+                }
+            ],
+            "identifier": "88",
+            "isPartOf": "2168",
+            "issued": "1993-10-31T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (adults)",
@@ -5178,54 +5172,54 @@
                 "prison overcrowding",
                 "prison violence"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2001-12-21T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2168",
-            "dataQuality": false,
-            "issued": "1993-10-31T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09908.v2",
-                    "title": "Census of State and Federal Adult Correctional Facilities, 1990  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Census of State and Federal Adult Correctional Facilities, 1995      ",
-            "description": "This census is the fifth enumeration of state adult\r\n correctional institutions and the second of federal institutions\r\n sponsored by the Bureau of Justice Statistics and conducted by the\r\n Bureau of the Census. Earlier censuses were completed in 1974 (ICPSR\r\n 7811), 1979 (ICPSR 7852), 1984 (ICPSR 8444), and 1990 (ICPSR 9908).\r\n Unlike the previous censuses, all respondents in 1995 were sent the\r\n same survey form. For each facility, information was provided on\r\n physical security, age, functions, capacity, court orders for specific\r\n conditions, one-day counts and average populations, race/ethnicity of\r\n inmates, inmate work assignments, inmate deaths, special inmate\r\ncounts, assaults, and incidents caused by inmates.",
-            "modified": "2003-03-21T00:00:00",
-            "accessLevel": "public",
-            "identifier": "89",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Census of State and Federal Adult Correctional Facilities, 1990  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This census is the fifth enumeration of state adult\r\n correctional institutions and the second of federal institutions\r\n sponsored by the Bureau of Justice Statistics and conducted by the\r\n Bureau of the Census. Earlier censuses were completed in 1974 (ICPSR\r\n 7811), 1979 (ICPSR 7852), 1984 (ICPSR 8444), and 1990 (ICPSR 9908).\r\n Unlike the previous censuses, all respondents in 1995 were sent the\r\n same survey form. For each facility, information was provided on\r\n physical security, age, functions, capacity, court orders for specific\r\n conditions, one-day counts and average populations, race/ethnicity of\r\n inmates, inmate work assignments, inmate deaths, special inmate\r\ncounts, assaults, and incidents caused by inmates.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06953.v1",
+                    "title": "Census of State and Federal Adult Correctional Facilities, 1995      "
+                }
+            ],
+            "identifier": "89",
+            "isPartOf": "2168",
+            "issued": "1998-04-20T00:00:00",
             "keyword": [
                 "census data",
                 "correctional facilities (adults)",
@@ -5241,54 +5235,54 @@
                 "prison construction",
                 "prison overcrowding"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2003-03-21T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2168",
-            "dataQuality": false,
-            "issued": "1998-04-20T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06953.v1",
-                    "title": "Census of State and Federal Adult Correctional Facilities, 1995      "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Census of State and Federal Adult Correctional Facilities, 2000      ",
-            "description": "This census is the sixth enumeration of state adult\r\n correctional institutions and the third of federal institutions\r\n sponsored by the Bureau of Justice Statistics and conducted by the\r\n Bureau of the Census. Earlier censuses were completed in 1974 (ICPSR\r\n 7811), 1979 (ICPSR 7852), 1984 (ICPSR 8444), 1990 (ICPSR 9908), and\r\n 1995 (ICPSR 6953). For each facility, information was provided on\r\n physical security, age, functions, capacity, court orders for specific\r\n conditions, one-day counts and average populations, race/ethnicity of\r\n inmates, inmate work assignments, inmate deaths, special inmate\r\ncounts, assaults, and incidents caused by inmates.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "90",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Census of State and Federal Adult Correctional Facilities, 1995      "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This census is the sixth enumeration of state adult\r\n correctional institutions and the third of federal institutions\r\n sponsored by the Bureau of Justice Statistics and conducted by the\r\n Bureau of the Census. Earlier censuses were completed in 1974 (ICPSR\r\n 7811), 1979 (ICPSR 7852), 1984 (ICPSR 8444), 1990 (ICPSR 9908), and\r\n 1995 (ICPSR 6953). For each facility, information was provided on\r\n physical security, age, functions, capacity, court orders for specific\r\n conditions, one-day counts and average populations, race/ethnicity of\r\n inmates, inmate work assignments, inmate deaths, special inmate\r\ncounts, assaults, and incidents caused by inmates.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04021.v1",
+                    "title": "Census of State and Federal Adult Correctional Facilities, 2000      "
+                }
+            ],
+            "identifier": "90",
+            "isPartOf": "2168",
+            "issued": "2004-07-09T00:00:00",
             "keyword": [
                 "census data",
                 "correctional facilities (adults)",
@@ -5304,54 +5298,54 @@
                 "prison construction",
                 "prison overcrowding"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-11-04T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2168",
-            "dataQuality": false,
-            "issued": "2004-07-09T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04021.v1",
-                    "title": "Census of State and Federal Adult Correctional Facilities, 2000      "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Census of State and Federal Adult Correctional Facilities, 2005",
-            "description": "This census is the seventh enumeration of state adult correctional institutions and the fourth of federal institutions sponsored by the Bureau of Justice Statistics and conducted by the Bureau of the Census. Earlier censuses were completed in 1979 (ICPSR 7852), 1984 (ICPSR 8444), 1990 (ICPSR 9908), 1995 (ICPSR 6953), and 2000 (ICPSR 4021). For each facility, information was provided on physical security, age, functions, capacity, court orders for specific conditions, one-day counts and average populations, race/ethnicity of inmates, inmate work assignments, inmate deaths, special inmate counts, assaults, and incidents caused by inmates.",
-            "modified": "2017-05-12T10:43:33",
-            "accessLevel": "public",
-            "identifier": "91",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Census of State and Federal Adult Correctional Facilities, 2000      "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This census is the seventh enumeration of state adult correctional institutions and the fourth of federal institutions sponsored by the Bureau of Justice Statistics and conducted by the Bureau of the Census. Earlier censuses were completed in 1979 (ICPSR 7852), 1984 (ICPSR 8444), 1990 (ICPSR 9908), 1995 (ICPSR 6953), and 2000 (ICPSR 4021). For each facility, information was provided on physical security, age, functions, capacity, court orders for specific conditions, one-day counts and average populations, race/ethnicity of inmates, inmate work assignments, inmate deaths, special inmate counts, assaults, and incidents caused by inmates.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24642.v3",
+                    "title": "Census of State and Federal Adult Correctional Facilities, 2005"
+                }
+            ],
+            "identifier": "91",
+            "isPartOf": "2168",
+            "issued": "2009-04-03T11:24:27",
             "keyword": [
                 "census data",
                 "correctional facilities (adults)",
@@ -5367,162 +5361,162 @@
                 "prison construction",
                 "prison overcrowding"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2017-05-12T10:43:33",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2168",
-            "dataQuality": false,
-            "issued": "2009-04-03T11:24:27",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24642.v3",
-                    "title": "Census of State and Federal Adult Correctional Facilities, 2005"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Census of State and Local Law Enforcement Agencies (CSLLEA), 2000: [United States]",
-            "description": "To ensure an accurate sampling frame for its Law\r\nEnforcement Management and Administrative Statistics (LEMAS) survey,\r\nthe Bureau of Justice Statistics periodically sponsors a census of the\r\nnation's state and local law enforcement agencies. This census, known\r\nas the Directory Survey, includes all state and local law enforcement\r\nagencies that are publicly funded and employ at least one full-time or\r\npart-time sworn officer with general arrest powers. As in previous\r\nyears, the 2000 Directory Survey collected data on the number of sworn\r\nand nonsworn personnel employed by each agency, including both\r\nfull-time and part-time employees. The pay period that included June\r\n30, 2000, was the reference date for all personnel data. A 97.4\r\npercent response rate was obtained from the 17,784 state and local law\r\nenforcement agencies operating in the United States. This data\r\ncollection contains June 2000 data from the fourth Directory Survey.\r\nPrevious directory censuses were conducted in 1986 (DIRECTORY OF LAW\r\nENFORCEMENT AGENCIES, 1986: [UNITED STATES] [ICPSR 8696]), 1992\r\n(DIRECTORY OF LAW ENFORCEMENT AGENCIES, 1992: [UNITED STATES] [ICPSR\r\n2266]), and 1996 (DIRECTORY OF LAW ENFORCEMENT AGENCIES, 1996: [UNITED\r\nSTATES] [ICPSR 2260]). Variables include personnel totals, type of\r\ngovernment, type of agency, and whether the agency had the legal\r\nauthority to hold a person beyond arraignment for 48 or more hours.",
-            "modified": "2009-07-08T18:05:17",
-            "accessLevel": "public",
-            "identifier": "92",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Census of State and Federal Adult Correctional Facilities, 2005"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "To ensure an accurate sampling frame for its Law\r\nEnforcement Management and Administrative Statistics (LEMAS) survey,\r\nthe Bureau of Justice Statistics periodically sponsors a census of the\r\nnation's state and local law enforcement agencies. This census, known\r\nas the Directory Survey, includes all state and local law enforcement\r\nagencies that are publicly funded and employ at least one full-time or\r\npart-time sworn officer with general arrest powers. As in previous\r\nyears, the 2000 Directory Survey collected data on the number of sworn\r\nand nonsworn personnel employed by each agency, including both\r\nfull-time and part-time employees. The pay period that included June\r\n30, 2000, was the reference date for all personnel data. A 97.4\r\npercent response rate was obtained from the 17,784 state and local law\r\nenforcement agencies operating in the United States. This data\r\ncollection contains June 2000 data from the fourth Directory Survey.\r\nPrevious directory censuses were conducted in 1986 (DIRECTORY OF LAW\r\nENFORCEMENT AGENCIES, 1986: [UNITED STATES] [ICPSR 8696]), 1992\r\n(DIRECTORY OF LAW ENFORCEMENT AGENCIES, 1992: [UNITED STATES] [ICPSR\r\n2266]), and 1996 (DIRECTORY OF LAW ENFORCEMENT AGENCIES, 1996: [UNITED\r\nSTATES] [ICPSR 2260]). Variables include personnel totals, type of\r\ngovernment, type of agency, and whether the agency had the legal\r\nauthority to hold a person beyond arraignment for 48 or more hours.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03484.v4",
+                    "title": "Census of State and Local Law Enforcement Agencies (CSLLEA), 2000: [United States]"
+                }
+            ],
+            "identifier": "92",
+            "isPartOf": "2436",
+            "issued": "2002-10-02T00:00:00",
             "keyword": [
                 "census data",
                 "law enforcement",
                 "police departments",
                 "police officers"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-07-08T18:05:17",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2436",
-            "dataQuality": false,
-            "issued": "2002-10-02T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03484.v4",
-                    "title": "Census of State and Local Law Enforcement Agencies (CSLLEA), 2000: [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Census of State and Local Law Enforcement Agencies (CSLLEA), 2004 [United States]",
-            "description": "To ensure an accurate sampling frame for its Law\r\nEnforcement Management and Administrative Statistics (LEMAS) survey,\r\nthe Bureau of Justice Statistics sponsors a census of the\r\nnation's state and local law enforcement agencies, known\r\nas the Directory Survey. This census, which is conducted every four years, includes all state and local law enforcement\r\nagencies operating nationwide that are publicly funded and employ at least one full-time or part-time sworn officer with general arrest powers. As in previous\r\nyears, the 2004 census collected data on the number of sworn\r\nand nonsworn personnel employed by each agency, including both\r\nfull-time and part-time employees. The pay period that included September\r\n30, 2004, was the reference date for all personnel data. Variables include personnel totals, type of government, type of agency, and whether the agency had the legal authority to hold a person beyond arraignment for 48 or more hours.\r\nPrevious censuses were conducted in 1986 (DIRECTORY OF LAW\r\nENFORCEMENT AGENCIES, 1986: [UNITED STATES] [ICPSR 8696]), 1992\r\n(DIRECTORY OF LAW ENFORCEMENT AGENCIES, 1992: [UNITED STATES] [ICPSR\r\n2266]), 1996 (DIRECTORY OF LAW ENFORCEMENT AGENCIES, 1996: [UNITED\r\nSTATES] [ICPSR 2260]), and 2000 (Census of State and Local Law Enforcement Agencies (CSLLEA), 2000: [United States] [ICPSR 3484]).",
-            "modified": "2011-05-23T09:42:02",
-            "accessLevel": "public",
-            "identifier": "93",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Census of State and Local Law Enforcement Agencies (CSLLEA), 2000: [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "To ensure an accurate sampling frame for its Law\r\nEnforcement Management and Administrative Statistics (LEMAS) survey,\r\nthe Bureau of Justice Statistics sponsors a census of the\r\nnation's state and local law enforcement agencies, known\r\nas the Directory Survey. This census, which is conducted every four years, includes all state and local law enforcement\r\nagencies operating nationwide that are publicly funded and employ at least one full-time or part-time sworn officer with general arrest powers. As in previous\r\nyears, the 2004 census collected data on the number of sworn\r\nand nonsworn personnel employed by each agency, including both\r\nfull-time and part-time employees. The pay period that included September\r\n30, 2004, was the reference date for all personnel data. Variables include personnel totals, type of government, type of agency, and whether the agency had the legal authority to hold a person beyond arraignment for 48 or more hours.\r\nPrevious censuses were conducted in 1986 (DIRECTORY OF LAW\r\nENFORCEMENT AGENCIES, 1986: [UNITED STATES] [ICPSR 8696]), 1992\r\n(DIRECTORY OF LAW ENFORCEMENT AGENCIES, 1992: [UNITED STATES] [ICPSR\r\n2266]), 1996 (DIRECTORY OF LAW ENFORCEMENT AGENCIES, 1996: [UNITED\r\nSTATES] [ICPSR 2260]), and 2000 (Census of State and Local Law Enforcement Agencies (CSLLEA), 2000: [United States] [ICPSR 3484]).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR28001.v1",
+                    "title": "Census of State and Local Law Enforcement Agencies (CSLLEA), 2004 [United States]"
+                }
+            ],
+            "identifier": "93",
+            "isPartOf": "2436",
+            "issued": "2010-12-15T09:06:30",
             "keyword": [
                 "census data",
                 "law enforcement",
                 "police departments",
                 "police officers"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-05-23T09:42:02",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2436",
-            "dataQuality": false,
-            "issued": "2010-12-15T09:06:30",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR28001.v1",
-                    "title": "Census of State and Local Law Enforcement Agencies (CSLLEA), 2004 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Census of State and Local Law Enforcement Agencies (CSLLEA), 2008",
-            "description": "The BJS Census of State and Local Law Enforcement Agencies (CSLLEA) is conducted every 4 years to provide a complete enumeration of agencies and their employees. Employment data are reported by agencies for sworn and nonsworn (civilian) personnel and, within these categories, by full-time or part-time status. The pay period that included September 30, 2008, was the reference date for all personnel data.\r\nAgencies also complete a checklist of functions they regularly perform, or have primary responsibility for, within the following areas: patrol and response, criminal investigation, traffic and vehicle-related functions, detention-related functions, court-related functions, special public safety functions (e.g., animal control), task force participation, and specialized functions (e.g., search and rescue).\r\nThe CSLLEA provides national data on the number of state and local law enforcement agencies and employees for local police departments, sheriffs' offices, state law enforcement agencies, and special jurisdiction agencies. It also serves as the sampling frame for BJS surveys of law enforcement agencies.",
-            "modified": "2011-08-03T13:27:33",
-            "accessLevel": "public",
-            "identifier": "94",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Census of State and Local Law Enforcement Agencies (CSLLEA), 2004 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The BJS Census of State and Local Law Enforcement Agencies (CSLLEA) is conducted every 4 years to provide a complete enumeration of agencies and their employees. Employment data are reported by agencies for sworn and nonsworn (civilian) personnel and, within these categories, by full-time or part-time status. The pay period that included September 30, 2008, was the reference date for all personnel data.\r\nAgencies also complete a checklist of functions they regularly perform, or have primary responsibility for, within the following areas: patrol and response, criminal investigation, traffic and vehicle-related functions, detention-related functions, court-related functions, special public safety functions (e.g., animal control), task force participation, and specialized functions (e.g., search and rescue).\r\nThe CSLLEA provides national data on the number of state and local law enforcement agencies and employees for local police departments, sheriffs' offices, state law enforcement agencies, and special jurisdiction agencies. It also serves as the sampling frame for BJS surveys of law enforcement agencies.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR27681.v1",
+                    "title": "Census of State and Local Law Enforcement Agencies (CSLLEA), 2008"
+                }
+            ],
+            "identifier": "94",
+            "isPartOf": "2436",
+            "issued": "2011-08-03T13:27:33",
             "keyword": [
                 "census data",
                 "law enforcement",
@@ -5530,54 +5524,53 @@
                 "police departments",
                 "police officers"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-08-03T13:27:33",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2436",
-            "dataQuality": false,
-            "issued": "2011-08-03T13:27:33",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR27681.v1",
-                    "title": "Census of State and Local Law Enforcement Agencies (CSLLEA), 2008"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Census of State and Local Law Enforcement Training Academies, 2006",
-            "description": "As of year-end 2006 a total of 648 state and local law\r\nenforcement academies were providing basic training to\r\nentry-level recruits in the United States. State agencies\r\napproved 98 percent of these academies. This data collection describes\r\nthe academies in terms of their personnel, expenditures,\r\nfacilities, curricula, and trainees using data from the 2006\r\nCensus of State and Local Law Enforcement Training Academies (CLETA)\r\nsponsored by the Bureau of Justice Statistics (BJS).\r\nThe 2006 CLETA, like the initial 2002 study, collected data\r\nfrom all state and local academies that provided basic law\r\nenforcement training. Academies that provided only\r\nin-service training, corrections and detention training, or\r\nother special types of training were excluded. Federal training\r\nacademies were also excluded.",
-            "modified": "2012-09-13T09:01:46",
-            "accessLevel": "public",
-            "identifier": "95",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Census of State and Local Law Enforcement Agencies (CSLLEA), 2008"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "As of year-end 2006 a total of 648 state and local law\r\nenforcement academies were providing basic training to\r\nentry-level recruits in the United States. State agencies\r\napproved 98 percent of these academies. This data collection describes\r\nthe academies in terms of their personnel, expenditures,\r\nfacilities, curricula, and trainees using data from the 2006\r\nCensus of State and Local Law Enforcement Training Academies (CLETA)\r\nsponsored by the Bureau of Justice Statistics (BJS).\r\nThe 2006 CLETA, like the initial 2002 study, collected data\r\nfrom all state and local academies that provided basic law\r\nenforcement training. Academies that provided only\r\nin-service training, corrections and detention training, or\r\nother special types of training were excluded. Federal training\r\nacademies were also excluded.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR27262.v1",
+                    "title": "Census of State and Local Law Enforcement Training Academies, 2006"
+                }
+            ],
+            "identifier": "95",
+            "issued": "2010-05-24T14:16:44",
             "keyword": [
                 "census data",
                 "law enforcement",
@@ -5587,53 +5580,53 @@
                 "police recruits",
                 "police training"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2012-09-13T09:01:46",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "2010-05-24T14:16:44",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR27262.v1",
-                    "title": "Census of State and Local Law Enforcement Training Academies, 2006"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Census of State Felony Courts, 1985: [United States]",
-            "description": "The purpose of this study was to provide a current listing\r\nof all felony courts in this country and to provide a universe from\r\nwhich a sample of courts could be selected based on felony caseload.\r\nThe study includes information on all state felony courts in the United\r\nStates, including the number of cases filed and disposed by conviction,\r\nacquittal, dismissal, or other means. Court administrators were asked\r\nto indicate the manner in which cases filed and disposed were counted,\r\nsuch as by defendant, charge, or indictment information. The total\r\nnumber of cases disposed during the period was also collected for\r\njuvenile delinquents and for traffic offenses (moving violations) where\r\napplicable. Finally, data were gathered on whether felonies reduced to\r\nmisdemeanors were included in the felony count and whether lower courts\r\nin the jurisdiction accepted guilty pleas to felonies.",
-            "modified": "1992-02-16T00:00:00",
-            "accessLevel": "public",
-            "identifier": "96",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Census of State and Local Law Enforcement Training Academies, 2006"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of this study was to provide a current listing\r\nof all felony courts in this country and to provide a universe from\r\nwhich a sample of courts could be selected based on felony caseload.\r\nThe study includes information on all state felony courts in the United\r\nStates, including the number of cases filed and disposed by conviction,\r\nacquittal, dismissal, or other means. Court administrators were asked\r\nto indicate the manner in which cases filed and disposed were counted,\r\nsuch as by defendant, charge, or indictment information. The total\r\nnumber of cases disposed during the period was also collected for\r\njuvenile delinquents and for traffic offenses (moving violations) where\r\napplicable. Finally, data were gathered on whether felonies reduced to\r\nmisdemeanors were included in the felony count and whether lower courts\r\nin the jurisdiction accepted guilty pleas to felonies.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08667.v2",
+                    "title": "Census of State Felony Courts, 1985: [United States]"
+                }
+            ],
+            "identifier": "96",
+            "issued": "1988-06-01T00:00:00",
             "keyword": [
                 "convictions (law)",
                 "court cases",
@@ -5642,53 +5635,53 @@
                 "juvenile delinquency",
                 "states (USA)"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1992-02-16T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1988-06-01T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08667.v2",
-                    "title": "Census of State Felony Courts, 1985: [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Census of Tribal Justice Agencies, 2002",
-            "description": "The study compiles data on the law enforcement, courts and\r\n administration, corrections and intermediate sanctions, criminal\r\n history records, and justice statistics of the federally recognized\r\n American Indian tribal governing bodies. The data determine which\r\n tribes have sworn law enforcement personnel and the source of\r\n authority, what the number and type of tribal court systems are, who\r\n performs the tribal detention function and what types of sanctions are\r\n imposed. It also looks at whether tribes have access to state and\r\nnational criminal record systems.",
-            "modified": "2006-07-13T00:00:00",
-            "accessLevel": "public",
-            "identifier": "97",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Census of State Felony Courts, 1985: [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The study compiles data on the law enforcement, courts and\r\n administration, corrections and intermediate sanctions, criminal\r\n history records, and justice statistics of the federally recognized\r\n American Indian tribal governing bodies. The data determine which\r\n tribes have sworn law enforcement personnel and the source of\r\n authority, what the number and type of tribal court systems are, who\r\n performs the tribal detention function and what types of sanctions are\r\n imposed. It also looks at whether tribes have access to state and\r\nnational criminal record systems.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04439.v1",
+                    "title": "Census of Tribal Justice Agencies, 2002"
+                }
+            ],
+            "identifier": "97",
+            "issued": "2006-07-13T00:00:00",
             "keyword": [
                 "Native Americans",
                 "correctional facilities",
@@ -5704,53 +5697,53 @@
                 "substance abuse",
                 "treatment programs"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2006-07-13T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "2006-07-13T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04439.v1",
-                    "title": "Census of Tribal Justice Agencies, 2002"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Commercial Victimization Surveys, 1972-1975 [United States]: Cities Sample",
-            "description": "The National Crime Surveys, of which these Commercial\r\nVictimization Surveys are a part, were conducted to obtain current and\r\nreliable measures of serious crime in the United States. The\r\nCommercial Victimization Surveys are restricted to coverage of\r\nburglary and robbery incidents. They include all types of commercial\r\nestablishments as well as political, cultural, and religious\r\norganizations. The survey includes a series of questions about the\r\nbusiness, e.g., type and size, form of ownership, insurance, security,\r\nand break-in and robbery characteristics. Time and place, weapon,\r\ninjury, entry evidence, offender characteristics, and stolen property\r\ndata were collected for each of the incidents. Data on both victimized\r\nand nonvictimized establishments in 26 different cities were collected\r\nduring 1972, 1973, and 1974. In the 1975 survey, data from the 13\r\ncities surveyed during 1972 and 1973 were collected again.",
-            "modified": "2006-01-12T00:00:00",
-            "accessLevel": "public",
-            "identifier": "98",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Census of Tribal Justice Agencies, 2002"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Surveys, of which these Commercial\r\nVictimization Surveys are a part, were conducted to obtain current and\r\nreliable measures of serious crime in the United States. The\r\nCommercial Victimization Surveys are restricted to coverage of\r\nburglary and robbery incidents. They include all types of commercial\r\nestablishments as well as political, cultural, and religious\r\norganizations. The survey includes a series of questions about the\r\nbusiness, e.g., type and size, form of ownership, insurance, security,\r\nand break-in and robbery characteristics. Time and place, weapon,\r\ninjury, entry evidence, offender characteristics, and stolen property\r\ndata were collected for each of the incidents. Data on both victimized\r\nand nonvictimized establishments in 26 different cities were collected\r\nduring 1972, 1973, and 1974. In the 1975 survey, data from the 13\r\ncities surveyed during 1972 and 1973 were collected again.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08002.v2",
+                    "title": "Commercial Victimization Surveys, 1972-1975 [United States]: Cities Sample"
+                }
+            ],
+            "identifier": "98",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "armed robbery",
                 "burglary",
@@ -5766,53 +5759,53 @@
                 "urban crime",
                 "victimization"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08002.v2",
-                    "title": "Commercial Victimization Surveys, 1972-1975 [United States]: Cities Sample"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Commercial Victimization Surveys, 1973-1977 [United States]: National Sample",
-            "description": "These Commercial Victimization Surveys were collected as\r\npart of the National Crime Surveys. They document burglary and robbery\r\nincidents for all types of commercial establishments, as well as\r\npolitical, cultural, and religious organizations. Business\r\ncharacteristics gathered include form of ownership and operation, size\r\nand type of business, and security measures. Information regarding the\r\nreported incidents includes time and place, weapon involvement,\r\noffender and entry characteristics, injuries and deaths, and type and\r\nvalue of stolen property. Data were collected by calendar quarter for\r\nfour quarters in 1973-1976 and for two quarters in 1977, while the\r\nactual incidents reported in the files reflect those occurring six\r\nmonths prior to the interview date.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2006-01-12T00:00:00",
-            "accessLevel": "public",
-            "identifier": "99",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Commercial Victimization Surveys, 1972-1975 [United States]: Cities Sample"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These Commercial Victimization Surveys were collected as\r\npart of the National Crime Surveys. They document burglary and robbery\r\nincidents for all types of commercial establishments, as well as\r\npolitical, cultural, and religious organizations. Business\r\ncharacteristics gathered include form of ownership and operation, size\r\nand type of business, and security measures. Information regarding the\r\nreported incidents includes time and place, weapon involvement,\r\noffender and entry characteristics, injuries and deaths, and type and\r\nvalue of stolen property. Data were collected by calendar quarter for\r\nfour quarters in 1973-1976 and for two quarters in 1977, while the\r\nactual incidents reported in the files reflect those occurring six\r\nmonths prior to the interview date.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08003.v2",
+                    "title": "Commercial Victimization Surveys, 1973-1977 [United States]: National Sample"
+                }
+            ],
+            "identifier": "99",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "armed robbery",
                 "burglary",
@@ -5827,53 +5820,59 @@
                 "urban crime",
                 "victimization"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2006-01-12T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08003.v2",
-                    "title": "Commercial Victimization Surveys, 1973-1977 [United States]: National Sample"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Corrections Statistical Analysis - Prisoners",
-            "description": "National Prisoner Statistics (NPS) on inmates under the jurisdiction of both federal and state correctional authorities.",
-            "modified": "2011-01-01T00:00:00",
-            "accessLevel": "public",
-            "identifier": "100",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Commercial Victimization Surveys, 1973-1977 [United States]: National Sample"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "National Prisoner Statistics (NPS) on inmates under the jurisdiction of both federal and state correctional authorities.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://csat.bjs.ojp.gov/map-query",
+                    "title": "Correctional Statistics Analysis - Prisoners (Map)"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://csat.bjs.ojp.gov/advanced-query",
+                    "mediaType": "text/html",
+                    "title": "Corrections Statistical Analysis - Prisoners"
+                }
+            ],
+            "identifier": "100",
+            "issued": "2011-01-01T00:00:00",
             "keyword": [
                 "Average annual change",
                 "Capacity",
@@ -5892,59 +5891,53 @@
                 "Supervised mandatory releases",
                 "Unconditio"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-01-01T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "2011-01-01T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://csat.bjs.ojp.gov/map-query",
-                    "title": "Correctional Statistics Analysis - Prisoners (Map)"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://csat.bjs.ojp.gov/advanced-query",
-                    "mediaType": "text/html",
-                    "title": "Corrections Statistical Analysis - Prisoners"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Criminal Victimization and Perceptions of Community Safety in 12 United States Cities, 1998",
-            "description": "This collection presents survey data from 12 cities in the\r\nUnited States regarding criminal victimization, perceptions of\r\ncommunity safety, and satisfaction with local police. Participating\r\ncities included Chicago, IL, Kansas City, MO, Knoxville, TN, Los\r\nAngeles, CA, Madison, WI, New York, NY, San Diego, CA, Savannah, GA,\r\nSpokane, WA, Springfield, MA, Tucson, AZ, and Washington, DC. The\r\nsurvey used the current National Crime Victimization Survey (NCVS)\r\nquestionnaire with a series of supplemental questions measuring the\r\nattitudes in each city. Respondents were asked about incidents that\r\noccurred within the past 12 months. Information on the following\r\ncrimes was collected: violent crimes of rape, robbery, aggravated\r\nassault, and simple assault, personal crimes of theft, and household\r\ncrimes of burglary, larceny, and motor vehicle theft.\r\nPart 1, Household-Level Data, covers the number of household\r\nrespondents, their ages, type of housing, size of residence, number of\r\ntelephone lines and numbers, and language spoken in the household.\r\nPart 2, Person-Level Data, includes information on respondents' sex,\r\nrelationship to householder, age, marital status, education, race,\r\ntime spent in the housing unit, personal crime and victimization\r\nexperiences, perceptions of neighborhood crime, job and professional\r\ndemographics, and experience and satisfaction with local police.\r\nVariables in Part 3, Incident-Level Data, concern the details of\r\ncrimes in which the respondents were involved, and the police response\r\nto the crimes.",
-            "modified": "2006-01-18T00:00:00",
-            "accessLevel": "public",
-            "identifier": "101",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Corrections Statistical Analysis - Prisoners"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This collection presents survey data from 12 cities in the\r\nUnited States regarding criminal victimization, perceptions of\r\ncommunity safety, and satisfaction with local police. Participating\r\ncities included Chicago, IL, Kansas City, MO, Knoxville, TN, Los\r\nAngeles, CA, Madison, WI, New York, NY, San Diego, CA, Savannah, GA,\r\nSpokane, WA, Springfield, MA, Tucson, AZ, and Washington, DC. The\r\nsurvey used the current National Crime Victimization Survey (NCVS)\r\nquestionnaire with a series of supplemental questions measuring the\r\nattitudes in each city. Respondents were asked about incidents that\r\noccurred within the past 12 months. Information on the following\r\ncrimes was collected: violent crimes of rape, robbery, aggravated\r\nassault, and simple assault, personal crimes of theft, and household\r\ncrimes of burglary, larceny, and motor vehicle theft.\r\nPart 1, Household-Level Data, covers the number of household\r\nrespondents, their ages, type of housing, size of residence, number of\r\ntelephone lines and numbers, and language spoken in the household.\r\nPart 2, Person-Level Data, includes information on respondents' sex,\r\nrelationship to householder, age, marital status, education, race,\r\ntime spent in the housing unit, personal crime and victimization\r\nexperiences, perceptions of neighborhood crime, job and professional\r\ndemographics, and experience and satisfaction with local police.\r\nVariables in Part 3, Incident-Level Data, concern the details of\r\ncrimes in which the respondents were involved, and the police response\r\nto the crimes.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR02743.v1",
+                    "title": "Criminal Victimization and Perceptions of Community Safety in 12 United States Cities, 1998"
+                }
+            ],
+            "identifier": "101",
+            "issued": "1999-10-01T00:00:00",
             "keyword": [
                 "assault",
                 "attitudes",
@@ -5959,53 +5952,54 @@
                 "robbery",
                 "victimization"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2006-01-18T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1999-10-01T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR02743.v1",
-                    "title": "Criminal Victimization and Perceptions of Community Safety in 12 United States Cities, 1998"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Directory of Law Enforcement Agencies, 1986: [United States]",
-            "description": "This dataset lists law enforcement agencies and contains \r\n variables regarding employment categories such as total full-time, \r\n part-time, sworn-in, and other employees. It also contains FIPS codes \r\nand populations.",
-            "modified": "1992-02-16T00:00:00",
-            "accessLevel": "public",
-            "identifier": "102",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Criminal Victimization and Perceptions of Community Safety in 12 United States Cities, 1998"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This dataset lists law enforcement agencies and contains \r\n variables regarding employment categories such as total full-time, \r\n part-time, sworn-in, and other employees. It also contains FIPS codes \r\nand populations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08696.v1",
+                    "title": "Directory of Law Enforcement Agencies, 1986: [United States]"
+                }
+            ],
+            "identifier": "102",
+            "isPartOf": "2436",
+            "issued": "1987-10-12T00:00:00",
             "keyword": [
                 "authority",
                 "full-time employment",
@@ -6016,54 +6010,54 @@
                 "police departments",
                 "policies and procedures"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1992-02-16T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2436",
-            "dataQuality": false,
-            "issued": "1987-10-12T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08696.v1",
-                    "title": "Directory of Law Enforcement Agencies, 1986: [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Directory of Law Enforcement Agencies, 1992:  [United States]  ",
-            "description": "To ensure an accurate sampling frame for its Law\r\n Enforcement Management and Administrative Statistics (LEMAS) survey,\r\n the Bureau of Justice Statistics periodically sponsors a census of the\r\n nation's state and local law enforcement agencies. This census, known\r\n as the Directory Survey, gathers data on all police and sheriffs'\r\n departments that are publicly funded and employ at least one full-time\r\n or part-time sworn officer with general arrest powers. This data\r\n collection, compiled in July 1992, represents the second such census,\r\n with the first occurring in 1986 (DIRECTORY OF LAW ENFORCEMENT\r\n AGENCIES, 1986: [UNITED STATES] [ICPSR 8696]). Variables include\r\n personnel totals, type of agency, geographic location of agency, and\r\n whether the agency had the legal authority to hold a person beyond\r\narraignment for 48 or more hours.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "103",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Directory of Law Enforcement Agencies, 1986: [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "To ensure an accurate sampling frame for its Law\r\n Enforcement Management and Administrative Statistics (LEMAS) survey,\r\n the Bureau of Justice Statistics periodically sponsors a census of the\r\n nation's state and local law enforcement agencies. This census, known\r\n as the Directory Survey, gathers data on all police and sheriffs'\r\n departments that are publicly funded and employ at least one full-time\r\n or part-time sworn officer with general arrest powers. This data\r\n collection, compiled in July 1992, represents the second such census,\r\n with the first occurring in 1986 (DIRECTORY OF LAW ENFORCEMENT\r\n AGENCIES, 1986: [UNITED STATES] [ICPSR 8696]). Variables include\r\n personnel totals, type of agency, geographic location of agency, and\r\n whether the agency had the legal authority to hold a person beyond\r\narraignment for 48 or more hours.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR02266.v1",
+                    "title": "Directory of Law Enforcement Agencies, 1992:  [United States]  "
+                }
+            ],
+            "identifier": "103",
+            "isPartOf": "2436",
+            "issued": "1998-02-23T00:00:00",
             "keyword": [
                 "authority",
                 "full-time employment",
@@ -6074,54 +6068,54 @@
                 "police departments",
                 "policies and procedures"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-11-04T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2436",
-            "dataQuality": false,
-            "issued": "1998-02-23T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR02266.v1",
-                    "title": "Directory of Law Enforcement Agencies, 1992:  [United States]  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Directory of Law Enforcement Agencies, 1996:  [United States]  ",
-            "description": "To ensure an accurate sampling frame for its Law\r\n Enforcement Management and Administrative Statistics (LEMAS) survey,\r\n the Bureau of Justice Statistics periodically sponsors a census of the\r\n nation's state and local law enforcement agencies. This census, known\r\n as the Directory Survey, gathers data on 49 primary state law\r\n enforcement agencies and all sheriffs' departments, local police\r\n departments, and special police agencies (state or local) that are\r\n publicly funded and employ at least one sworn officer with general\r\n arrest powers. The 1996 Directory Survey collected data on the number\r\n of sworn and nonsworn personnel employed by each agency, including\r\n both full-time and part-time employees. Within the full-time sworn\r\n category, data were collected from all agencies on the number who were\r\n uniformed officers with regularly assigned duties that included\r\n responding to calls for service. For agencies with at least 10\r\n full-time sworn officers, the number whose primary duties were related\r\n to investigations, court operations, or jail operations was also\r\n obtained. This data collection, compiled in June 1996, represents the\r\n third such census, with the first occurring in 1986 (DIRECTORY OF LAW\r\n ENFORCEMENT AGENCIES, 1986: [UNITED STATES] [ICPSR 8696]) and the\r\n second in 1992 (DIRECTORY OF LAW ENFORCEMENT AGENCIES, 1992: [UNITED\r\n STATES] [ICPSR 2266]). Variables include personnel totals, type of\r\n government, type of agency, and whether the agency had the legal\r\nauthority to hold a person beyond arraignment for 48 or more hours.",
-            "modified": "1998-09-11T00:00:00",
-            "accessLevel": "public",
-            "identifier": "104",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Directory of Law Enforcement Agencies, 1992:  [United States]  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "To ensure an accurate sampling frame for its Law\r\n Enforcement Management and Administrative Statistics (LEMAS) survey,\r\n the Bureau of Justice Statistics periodically sponsors a census of the\r\n nation's state and local law enforcement agencies. This census, known\r\n as the Directory Survey, gathers data on 49 primary state law\r\n enforcement agencies and all sheriffs' departments, local police\r\n departments, and special police agencies (state or local) that are\r\n publicly funded and employ at least one sworn officer with general\r\n arrest powers. The 1996 Directory Survey collected data on the number\r\n of sworn and nonsworn personnel employed by each agency, including\r\n both full-time and part-time employees. Within the full-time sworn\r\n category, data were collected from all agencies on the number who were\r\n uniformed officers with regularly assigned duties that included\r\n responding to calls for service. For agencies with at least 10\r\n full-time sworn officers, the number whose primary duties were related\r\n to investigations, court operations, or jail operations was also\r\n obtained. This data collection, compiled in June 1996, represents the\r\n third such census, with the first occurring in 1986 (DIRECTORY OF LAW\r\n ENFORCEMENT AGENCIES, 1986: [UNITED STATES] [ICPSR 8696]) and the\r\n second in 1992 (DIRECTORY OF LAW ENFORCEMENT AGENCIES, 1992: [UNITED\r\n STATES] [ICPSR 2266]). Variables include personnel totals, type of\r\n government, type of agency, and whether the agency had the legal\r\nauthority to hold a person beyond arraignment for 48 or more hours.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR02260.v1",
+                    "title": "Directory of Law Enforcement Agencies, 1996:  [United States]  "
+                }
+            ],
+            "identifier": "104",
+            "isPartOf": "2436",
+            "issued": "1998-09-11T00:00:00",
             "keyword": [
                 "authority",
                 "full-time employment",
@@ -6132,54 +6126,54 @@
                 "police departments",
                 "policies and procedures"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1998-09-11T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2436",
-            "dataQuality": false,
-            "issued": "1998-09-11T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR02260.v1",
-                    "title": "Directory of Law Enforcement Agencies, 1996:  [United States]  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1982  ",
-            "description": "These criminal justice expenditure and employment (CJEE)\r\n data are taken from a special compilation of sources available from\r\n the Census Bureau's Annual Surveys of Governments, Finance Statistics\r\n and Employment Statistics. Levels of government covered are federal,\r\n state, county, municipal, and towns and townships. Information is\r\n included on total employment, total police protection, police\r\n protection with arrest powers, other police protection, judicial-legal\r\n employment, corrections employment, total expenditures, police\r\n protection expenditures, judicial-legal expenditures, and corrections\r\n expenditures. Types of expenditures include direct current, capital\r\n outlay, equipment, and intergovernmental. Types of employment include\r\ntotal, full-time, part-time, and full-time equivalent.",
-            "modified": "1997-02-13T00:00:00",
-            "accessLevel": "public",
-            "identifier": "105",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Directory of Law Enforcement Agencies, 1996:  [United States]  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These criminal justice expenditure and employment (CJEE)\r\n data are taken from a special compilation of sources available from\r\n the Census Bureau's Annual Surveys of Governments, Finance Statistics\r\n and Employment Statistics. Levels of government covered are federal,\r\n state, county, municipal, and towns and townships. Information is\r\n included on total employment, total police protection, police\r\n protection with arrest powers, other police protection, judicial-legal\r\n employment, corrections employment, total expenditures, police\r\n protection expenditures, judicial-legal expenditures, and corrections\r\n expenditures. Types of expenditures include direct current, capital\r\n outlay, equipment, and intergovernmental. Types of employment include\r\ntotal, full-time, part-time, and full-time equivalent.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08382.v1",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1982  "
+                }
+            ],
+            "identifier": "105",
+            "isPartOf": "2429",
+            "issued": "1985-10-09T00:00:00",
             "keyword": [
                 "correctional system",
                 "criminal justice system",
@@ -6193,54 +6187,54 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1997-02-13T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "1985-10-09T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08382.v1",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1982  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1983  ",
-            "description": "These criminal justice expenditure and employment (CJEE)\r\n data are taken from a special compilation of sources available from\r\n the Census Bureau's Annual Surveys of Governments, Finance Statistics\r\n and Employment Statistics. Levels of government covered are federal,\r\n state, county, municipal, and towns and townships. Information is\r\n included on total employment, total police protection, police\r\n protection with arrest powers, other police protection, judicial-legal\r\n employment, corrections employment, total expenditures, police\r\n protection expenditures, judicial-legal expenditures, and corrections\r\n expenditures. Types of expenditures include direct current, capital\r\n outlay, equipment, and intergovernmental. Types of employment include\r\ntotal, full-time, part-time, and full-time equivalent.",
-            "modified": "1997-04-14T00:00:00",
-            "accessLevel": "public",
-            "identifier": "106",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1982  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These criminal justice expenditure and employment (CJEE)\r\n data are taken from a special compilation of sources available from\r\n the Census Bureau's Annual Surveys of Governments, Finance Statistics\r\n and Employment Statistics. Levels of government covered are federal,\r\n state, county, municipal, and towns and townships. Information is\r\n included on total employment, total police protection, police\r\n protection with arrest powers, other police protection, judicial-legal\r\n employment, corrections employment, total expenditures, police\r\n protection expenditures, judicial-legal expenditures, and corrections\r\n expenditures. Types of expenditures include direct current, capital\r\n outlay, equipment, and intergovernmental. Types of employment include\r\ntotal, full-time, part-time, and full-time equivalent.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08455.v1",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1983  "
+                }
+            ],
+            "identifier": "106",
+            "isPartOf": "2429",
+            "issued": "1986-11-07T00:00:00",
             "keyword": [
                 "correctional system",
                 "criminal justice system",
@@ -6254,54 +6248,54 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1997-04-14T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "1986-11-07T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08455.v1",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1983  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1984  ",
-            "description": "These criminal justice expenditure and employment (CJEE)\r\n data are taken from a special compilation of sources available from\r\n the Census Bureau's Annual Surveys of Governments, Finance Statistics\r\n and Employment Statistics. Levels of government covered are federal,\r\n state, county, municipal, and towns and townships. Information is\r\n included on total employment, total police protection, police\r\n protection with arrest powers, other police protection, judicial-legal\r\n employment, corrections employment, total expenditures, police\r\n protection expenditures, judicial-legal expenditures, and corrections\r\n expenditures. Types of expenditures include direct current, capital\r\n outlay, equipment, and intergovernmental. Types of employment include\r\ntotal, full-time, part-time, and full-time equivalent.",
-            "modified": "1998-04-20T00:00:00",
-            "accessLevel": "public",
-            "identifier": "107",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1983  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These criminal justice expenditure and employment (CJEE)\r\n data are taken from a special compilation of sources available from\r\n the Census Bureau's Annual Surveys of Governments, Finance Statistics\r\n and Employment Statistics. Levels of government covered are federal,\r\n state, county, municipal, and towns and townships. Information is\r\n included on total employment, total police protection, police\r\n protection with arrest powers, other police protection, judicial-legal\r\n employment, corrections employment, total expenditures, police\r\n protection expenditures, judicial-legal expenditures, and corrections\r\n expenditures. Types of expenditures include direct current, capital\r\n outlay, equipment, and intergovernmental. Types of employment include\r\ntotal, full-time, part-time, and full-time equivalent.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09162.v2",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1984  "
+                }
+            ],
+            "identifier": "107",
+            "isPartOf": "2429",
+            "issued": "1989-12-15T00:00:00",
             "keyword": [
                 "correctional system",
                 "criminal justice system",
@@ -6315,54 +6309,54 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1998-04-20T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "1989-12-15T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09162.v2",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1984  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1985  ",
-            "description": "These criminal justice expenditure and employment (CJEE)\r\n data are taken from a special compilation of sources available from\r\n the Census Bureau's Annual Surveys of Governments, Finance Statistics\r\n and Employment Statistics. Levels of government covered are federal,\r\n state, county, municipal, and towns and townships. Information is\r\n included on total employment, total police protection, police\r\n protection with arrest powers, other police protection, judicial-legal\r\n employment, corrections employment, total expenditures, police\r\n protection expenditures, judicial-legal expenditures, and corrections\r\n expenditures. Types of expenditures include direct current, capital\r\n outlay, equipment, and intergovernmental. Types of employment include\r\ntotal, full-time, part-time, and full-time equivalent.",
-            "modified": "1998-05-20T00:00:00",
-            "accessLevel": "public",
-            "identifier": "108",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1984  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These criminal justice expenditure and employment (CJEE)\r\n data are taken from a special compilation of sources available from\r\n the Census Bureau's Annual Surveys of Governments, Finance Statistics\r\n and Employment Statistics. Levels of government covered are federal,\r\n state, county, municipal, and towns and townships. Information is\r\n included on total employment, total police protection, police\r\n protection with arrest powers, other police protection, judicial-legal\r\n employment, corrections employment, total expenditures, police\r\n protection expenditures, judicial-legal expenditures, and corrections\r\n expenditures. Types of expenditures include direct current, capital\r\n outlay, equipment, and intergovernmental. Types of employment include\r\ntotal, full-time, part-time, and full-time equivalent.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09161.v2",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1985  "
+                }
+            ],
+            "identifier": "108",
+            "isPartOf": "2429",
+            "issued": "1989-09-26T00:00:00",
             "keyword": [
                 "correctional system",
                 "criminal justice system",
@@ -6376,54 +6370,54 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1998-05-20T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "1989-09-26T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09161.v2",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1985  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1986",
-            "description": "These criminal justice expenditure and employment (CJEE)\r\n data are taken from a special compilation of sources available from\r\n the Census Bureau's Annual Surveys of Governments, Finance Statistics\r\n and Employment Statistics. Levels of government covered are federal,\r\n state, county, municipal, and towns and townships. Information is\r\n included on total employment, total police protection, police\r\n protection with arrest powers, other police protection, judicial-legal\r\n employment, corrections employment, total expenditures, police\r\n protection expenditures, judicial-legal expenditures, and corrections\r\n expenditures. Types of expenditures include direct current, capital\r\n outlay, equipment, and intergovernmental. Types of employment include\r\ntotal, full-time, part-time, and full-time equivalent.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "109",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1985  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These criminal justice expenditure and employment (CJEE)\r\n data are taken from a special compilation of sources available from\r\n the Census Bureau's Annual Surveys of Governments, Finance Statistics\r\n and Employment Statistics. Levels of government covered are federal,\r\n state, county, municipal, and towns and townships. Information is\r\n included on total employment, total police protection, police\r\n protection with arrest powers, other police protection, judicial-legal\r\n employment, corrections employment, total expenditures, police\r\n protection expenditures, judicial-legal expenditures, and corrections\r\n expenditures. Types of expenditures include direct current, capital\r\n outlay, equipment, and intergovernmental. Types of employment include\r\ntotal, full-time, part-time, and full-time equivalent.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09160.v1",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1986"
+                }
+            ],
+            "identifier": "109",
+            "isPartOf": "2429",
+            "issued": "1989-09-26T00:00:00",
             "keyword": [
                 "correctional system",
                 "criminal justice system",
@@ -6437,54 +6431,54 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-11-04T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "1989-09-26T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09160.v1",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1986"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]: CJEE Extracts File, 1987  ",
-            "description": "These criminal justice expenditure and employment (CJEE)\r\n data are taken from a special compilation of sources available from\r\n the Census Bureau's Annual Surveys of Governments, Finance Statistics\r\n and Employment Statistics. Levels of government covered are federal,\r\n state, county, municipal, and towns and townships. Information is\r\n included on total employment, total police protection, police\r\n protection with arrest powers, other police protection, judicial-legal\r\n employment, corrections employment, total expenditures, police\r\n protection expenditures, judicial-legal expenditures, and corrections\r\n expenditures. Types of expenditures include direct current, capital\r\n outlay, equipment, and intergovernmental. Types of employment include\r\ntotal, full-time, part-time, and full-time equivalent.",
-            "modified": "1997-12-12T00:00:00",
-            "accessLevel": "public",
-            "identifier": "110",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1986"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These criminal justice expenditure and employment (CJEE)\r\n data are taken from a special compilation of sources available from\r\n the Census Bureau's Annual Surveys of Governments, Finance Statistics\r\n and Employment Statistics. Levels of government covered are federal,\r\n state, county, municipal, and towns and townships. Information is\r\n included on total employment, total police protection, police\r\n protection with arrest powers, other police protection, judicial-legal\r\n employment, corrections employment, total expenditures, police\r\n protection expenditures, judicial-legal expenditures, and corrections\r\n expenditures. Types of expenditures include direct current, capital\r\n outlay, equipment, and intergovernmental. Types of employment include\r\ntotal, full-time, part-time, and full-time equivalent.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09396.v1",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]: CJEE Extracts File, 1987  "
+                }
+            ],
+            "identifier": "110",
+            "isPartOf": "2429",
+            "issued": "1990-10-16T00:00:00",
             "keyword": [
                 "correctional system",
                 "criminal justice system",
@@ -6498,54 +6492,54 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1997-12-12T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "1990-10-16T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09396.v1",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]: CJEE Extracts File, 1987  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1988  ",
-            "description": "These criminal justice expenditure and employment (CJEE)\r\n data are taken from a special compilation of sources available from\r\n the Census Bureau's Annual Surveys of Governments, Finance Statistics\r\n and Employment Statistics. Levels of government covered are federal,\r\n state, county, municipal, and towns and townships. Information is\r\n included on total employment, total police protection, police\r\n protection with arrest powers, other police protection, judicial-legal\r\n employment, corrections employment, total expenditures, police\r\n protection expenditures, judicial-legal expenditures, and corrections\r\n expenditures. Types of expenditures include direct current, capital\r\n outlay, equipment, and intergovernmental. Types of employment include\r\ntotal, full-time, part-time, and full-time equivalent.",
-            "modified": "1997-08-25T00:00:00",
-            "accessLevel": "public",
-            "identifier": "111",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]: CJEE Extracts File, 1987  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These criminal justice expenditure and employment (CJEE)\r\n data are taken from a special compilation of sources available from\r\n the Census Bureau's Annual Surveys of Governments, Finance Statistics\r\n and Employment Statistics. Levels of government covered are federal,\r\n state, county, municipal, and towns and townships. Information is\r\n included on total employment, total police protection, police\r\n protection with arrest powers, other police protection, judicial-legal\r\n employment, corrections employment, total expenditures, police\r\n protection expenditures, judicial-legal expenditures, and corrections\r\n expenditures. Types of expenditures include direct current, capital\r\n outlay, equipment, and intergovernmental. Types of employment include\r\ntotal, full-time, part-time, and full-time equivalent.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09554.v1",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1988  "
+                }
+            ],
+            "identifier": "111",
+            "isPartOf": "2429",
+            "issued": "1991-10-23T00:00:00",
             "keyword": [
                 "correctional system",
                 "criminal justice system",
@@ -6559,54 +6553,54 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1997-08-25T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "1991-10-23T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09554.v1",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1988  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]: CJEE Extracts File, 1989",
-            "description": "These criminal justice expenditure and employment (CJEE)\r\n data are taken from a special compilation of sources available from the\r\n Census Bureau's Annual Surveys of Governments, Finance Statistics and\r\n Employment Statistics. Levels of government covered are federal, state,\r\n county, municipal, and towns and townships. Information is included on\r\n total employment, total police protection, police protection with arrest\r\n powers, other police protection, judicial-legal employment, corrections\r\n employment, total expenditures, police protection expenditures,\r\n judicial-legal expenditures, and corrections expenditures. Types of\r\n expenditures include direct current, capital outlay, equipment, and\r\n intergovernmental. Types of employment include total, full-time,\r\npart-time, and full-time equivalent.",
-            "modified": "2004-04-07T00:00:00",
-            "accessLevel": "public",
-            "identifier": "112",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1988  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These criminal justice expenditure and employment (CJEE)\r\n data are taken from a special compilation of sources available from the\r\n Census Bureau's Annual Surveys of Governments, Finance Statistics and\r\n Employment Statistics. Levels of government covered are federal, state,\r\n county, municipal, and towns and townships. Information is included on\r\n total employment, total police protection, police protection with arrest\r\n powers, other police protection, judicial-legal employment, corrections\r\n employment, total expenditures, police protection expenditures,\r\n judicial-legal expenditures, and corrections expenditures. Types of\r\n expenditures include direct current, capital outlay, equipment, and\r\n intergovernmental. Types of employment include total, full-time,\r\npart-time, and full-time equivalent.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09773.v2",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]: CJEE Extracts File, 1989"
+                }
+            ],
+            "identifier": "112",
+            "isPartOf": "2429",
+            "issued": "1992-10-31T00:00:00",
             "keyword": [
                 "correctional system",
                 "criminal justice system",
@@ -6620,54 +6614,54 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2004-04-07T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "1992-10-31T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09773.v2",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]: CJEE Extracts File, 1989"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1990   ",
-            "description": "These criminal justice expenditure and employment (CJEE)\r\n data are taken from a special compilation of sources available from\r\n the Census Bureau's Annual Surveys of Governments, Finance Statistics\r\n and Employment Statistics. Levels of government covered are federal,\r\n state, county, municipal, and towns and townships. Information is\r\n included on total employment, total police protection, police\r\n protection with arrest powers, other police protection, judicial-legal\r\n employment, corrections employment, total expenditures, police\r\n protection expenditures, judicial-legal expenditures, and corrections\r\n expenditures. Types of expenditures include direct current, capital\r\n outlay, equipment, and intergovernmental. Types of employment include\r\ntotal, full-time, part-time, and full-time equivalent.",
-            "modified": "1993-05-13T00:00:00",
-            "accessLevel": "public",
-            "identifier": "113",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]: CJEE Extracts File, 1989"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These criminal justice expenditure and employment (CJEE)\r\n data are taken from a special compilation of sources available from\r\n the Census Bureau's Annual Surveys of Governments, Finance Statistics\r\n and Employment Statistics. Levels of government covered are federal,\r\n state, county, municipal, and towns and townships. Information is\r\n included on total employment, total police protection, police\r\n protection with arrest powers, other police protection, judicial-legal\r\n employment, corrections employment, total expenditures, police\r\n protection expenditures, judicial-legal expenditures, and corrections\r\n expenditures. Types of expenditures include direct current, capital\r\n outlay, equipment, and intergovernmental. Types of employment include\r\ntotal, full-time, part-time, and full-time equivalent.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06006.v1",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1990   "
+                }
+            ],
+            "identifier": "113",
+            "isPartOf": "2429",
+            "issued": "1993-05-13T00:00:00",
             "keyword": [
                 "correctional system",
                 "criminal justice system",
@@ -6681,54 +6675,54 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1993-05-13T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "1993-05-13T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06006.v1",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1990   "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1991  ",
-            "description": "These criminal justice expenditure and employment (CJEE)\r\n data are taken from a special compilation of sources available from\r\n the Census Bureau's Annual Surveys of Governments, Finance Statistics\r\n and Employment Statistics. Levels of government covered are federal,\r\n state, county, municipal, and towns and townships. Information is\r\n included on total employment, total police protection, police\r\n protection with arrest powers, other police protection, judicial-legal\r\n employment, corrections employment, total expenditures, police\r\n protection expenditures, judicial-legal expenditures, and corrections\r\n expenditures. Types of expenditures include direct current, capital\r\n outlay, equipment, and intergovernmental. Types of employment include\r\ntotal, full-time, part-time, and full-time equivalent.",
-            "modified": "1994-05-20T00:00:00",
-            "accessLevel": "public",
-            "identifier": "114",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1990   "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These criminal justice expenditure and employment (CJEE)\r\n data are taken from a special compilation of sources available from\r\n the Census Bureau's Annual Surveys of Governments, Finance Statistics\r\n and Employment Statistics. Levels of government covered are federal,\r\n state, county, municipal, and towns and townships. Information is\r\n included on total employment, total police protection, police\r\n protection with arrest powers, other police protection, judicial-legal\r\n employment, corrections employment, total expenditures, police\r\n protection expenditures, judicial-legal expenditures, and corrections\r\n expenditures. Types of expenditures include direct current, capital\r\n outlay, equipment, and intergovernmental. Types of employment include\r\ntotal, full-time, part-time, and full-time equivalent.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06259.v1",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1991  "
+                }
+            ],
+            "identifier": "114",
+            "isPartOf": "2429",
+            "issued": "1994-05-20T00:00:00",
             "keyword": [
                 "correctional system",
                 "criminal justice system",
@@ -6742,54 +6736,54 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1994-05-20T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "1994-05-20T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06259.v1",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1991  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1992  ",
-            "description": "These criminal justice expenditure and employment (CJEE)\r\n data are taken from a special compilation of sources available from\r\n the Census Bureau's Annual Surveys of Governments, Finance Statistics\r\n and Employment Statistics. Levels of government covered are federal,\r\n state, county, municipal, and towns and townships. Information is\r\n included on total employment, total police protection, police\r\n protection with arrest powers, other police protection, judicial-legal\r\n employment, corrections employment, total expenditures, police\r\n protection expenditures, judicial-legal expenditures, and corrections\r\n expenditures. Types of expenditures include direct current, capital\r\n outlay, equipment, and intergovernmental. Types of employment include\r\ntotal, full-time, part-time, and full-time equivalent.",
-            "modified": "1996-01-22T00:00:00",
-            "accessLevel": "public",
-            "identifier": "115",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1991  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These criminal justice expenditure and employment (CJEE)\r\n data are taken from a special compilation of sources available from\r\n the Census Bureau's Annual Surveys of Governments, Finance Statistics\r\n and Employment Statistics. Levels of government covered are federal,\r\n state, county, municipal, and towns and townships. Information is\r\n included on total employment, total police protection, police\r\n protection with arrest powers, other police protection, judicial-legal\r\n employment, corrections employment, total expenditures, police\r\n protection expenditures, judicial-legal expenditures, and corrections\r\n expenditures. Types of expenditures include direct current, capital\r\n outlay, equipment, and intergovernmental. Types of employment include\r\ntotal, full-time, part-time, and full-time equivalent.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06579.v1",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1992  "
+                }
+            ],
+            "identifier": "115",
+            "isPartOf": "2429",
+            "issued": "1996-01-22T00:00:00",
             "keyword": [
                 "correctional system",
                 "criminal justice system",
@@ -6803,54 +6797,54 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1996-01-22T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "1996-01-22T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06579.v1",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1992  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]: CJEE Extracts File, 1993",
-            "description": "This file provides data on federal, state, and local\r\n governmental expenditures and employment for criminal justice\r\n activities in the United States. Information is supplied on police\r\n protection, judicial and legal services, and correctional institutions\r\n and agencies. Variables describing each of these criminal justice\r\n functions include number of and payroll for full-time, part-time, and\r\n full-time equivalent employees, current total and general\r\nexpenditures, capital outlay, and intergovernmental expenditures.",
-            "modified": "2007-04-18T00:00:00",
-            "accessLevel": "public",
-            "identifier": "116",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1992  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This file provides data on federal, state, and local\r\n governmental expenditures and employment for criminal justice\r\n activities in the United States. Information is supplied on police\r\n protection, judicial and legal services, and correctional institutions\r\n and agencies. Variables describing each of these criminal justice\r\n functions include number of and payroll for full-time, part-time, and\r\n full-time equivalent employees, current total and general\r\nexpenditures, capital outlay, and intergovernmental expenditures.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06795.v2",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]: CJEE Extracts File, 1993"
+                }
+            ],
+            "identifier": "116",
+            "isPartOf": "2429",
+            "issued": "2001-01-12T00:00:00",
             "keyword": [
                 "correctional system",
                 "criminal justice system",
@@ -6864,54 +6858,54 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2007-04-18T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "2001-01-12T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06795.v2",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]: CJEE Extracts File, 1993"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1994  ",
-            "description": "This file provides data on federal, state, and local\r\n governmental expenditures and employment for criminal justice\r\n activities in the United States. Information is supplied on police\r\n protection, judicial and legal services, and correctional institutions\r\n and agencies. Variables describing each of these criminal justice\r\n functions include number of and payroll for full-time, part-time, and\r\n full-time equivalent employees, current total and general\r\nexpenditures, capital outlay, and intergovernmental expenditures.",
-            "modified": "2001-02-01T00:00:00",
-            "accessLevel": "public",
-            "identifier": "117",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]: CJEE Extracts File, 1993"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This file provides data on federal, state, and local\r\n governmental expenditures and employment for criminal justice\r\n activities in the United States. Information is supplied on police\r\n protection, judicial and legal services, and correctional institutions\r\n and agencies. Variables describing each of these criminal justice\r\n functions include number of and payroll for full-time, part-time, and\r\n full-time equivalent employees, current total and general\r\nexpenditures, capital outlay, and intergovernmental expenditures.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR02257.v1",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1994  "
+                }
+            ],
+            "identifier": "117",
+            "isPartOf": "2429",
+            "issued": "2001-02-01T00:00:00",
             "keyword": [
                 "correctional system",
                 "criminal justice system",
@@ -6925,54 +6919,54 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2001-02-01T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "2001-02-01T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR02257.v1",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1994  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1995  ",
-            "description": "This file provides data on federal, state, and local\r\n governmental expenditures and employment for criminal justice\r\n activities in the United States. Information is supplied on police\r\n protection, judicial and legal services, and correctional institutions\r\n and agencies. Variables describing each of these criminal justice\r\n functions include number of and payroll for full-time, part-time, and\r\n full-time equivalent employees, current total and general\r\nexpenditures, capital outlay, and intergovernmental expenditures.",
-            "modified": "2001-01-25T00:00:00",
-            "accessLevel": "public",
-            "identifier": "118",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1994  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This file provides data on federal, state, and local\r\n governmental expenditures and employment for criminal justice\r\n activities in the United States. Information is supplied on police\r\n protection, judicial and legal services, and correctional institutions\r\n and agencies. Variables describing each of these criminal justice\r\n functions include number of and payroll for full-time, part-time, and\r\n full-time equivalent employees, current total and general\r\nexpenditures, capital outlay, and intergovernmental expenditures.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR02840.v1",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1995  "
+                }
+            ],
+            "identifier": "118",
+            "isPartOf": "2429",
+            "issued": "2001-01-25T00:00:00",
             "keyword": [
                 "correctional system",
                 "criminal justice system",
@@ -6986,54 +6980,54 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2001-01-25T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "2001-01-25T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR02840.v1",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1995  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1996      ",
-            "description": "This file provides data on federal, state, and local\r\n governmental expenditures and employment for criminal justice\r\n activities in the United States. Information is supplied on police\r\n protection, judicial and legal services, and correctional institutions\r\n and agencies. Variables describing each of these criminal justice\r\n functions include number of and payroll for full-time, part-time, and\r\n full-time equivalent employees, current total and general\r\nexpenditures, capital outlay, and intergovernmental expenditures.",
-            "modified": "2001-08-24T00:00:00",
-            "accessLevel": "public",
-            "identifier": "119",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1995  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This file provides data on federal, state, and local\r\n governmental expenditures and employment for criminal justice\r\n activities in the United States. Information is supplied on police\r\n protection, judicial and legal services, and correctional institutions\r\n and agencies. Variables describing each of these criminal justice\r\n functions include number of and payroll for full-time, part-time, and\r\n full-time equivalent employees, current total and general\r\nexpenditures, capital outlay, and intergovernmental expenditures.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03063.v2",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1996      "
+                }
+            ],
+            "identifier": "119",
+            "isPartOf": "2429",
+            "issued": "2001-01-25T00:00:00",
             "keyword": [
                 "correctional system",
                 "criminal justice system",
@@ -7047,54 +7041,54 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2001-08-24T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "2001-01-25T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03063.v2",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1996      "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1997  ",
-            "description": "This file provides data on federal, state, and local\r\n governmental expenditures and employment for criminal justice\r\n activities in the United States. Information is supplied on police\r\n protection, judicial and legal services, and correctional institutions\r\n and agencies. Variables describing each of these criminal justice\r\n functions include number of and payroll for full-time, part-time, and\r\n full-time equivalent employees, current total and general\r\nexpenditures, capital outlay, and intergovernmental expenditures.",
-            "modified": "2001-08-06T00:00:00",
-            "accessLevel": "public",
-            "identifier": "120",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1996      "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This file provides data on federal, state, and local\r\n governmental expenditures and employment for criminal justice\r\n activities in the United States. Information is supplied on police\r\n protection, judicial and legal services, and correctional institutions\r\n and agencies. Variables describing each of these criminal justice\r\n functions include number of and payroll for full-time, part-time, and\r\n full-time equivalent employees, current total and general\r\nexpenditures, capital outlay, and intergovernmental expenditures.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03229.v1",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1997  "
+                }
+            ],
+            "identifier": "120",
+            "isPartOf": "2429",
+            "issued": "2001-08-06T00:00:00",
             "keyword": [
                 "correctional system",
                 "criminal justice system",
@@ -7108,54 +7102,54 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2001-08-06T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "2001-08-06T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03229.v1",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1997  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1998  ",
-            "description": "This file provides data on federal, state, and local\r\n governmental expenditures and employment for criminal justice\r\n activities in the United States. Information is supplied on police\r\n protection, judicial and legal services, and correctional institutions\r\n and agencies. Variables describing each of these criminal justice\r\n functions include number of and payroll for full-time, part-time, and\r\n full-time-equivalent employees, current total and general\r\nexpenditures, capital outlay, and intergovernmental expenditures.",
-            "modified": "2002-06-07T00:00:00",
-            "accessLevel": "public",
-            "identifier": "121",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1997  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This file provides data on federal, state, and local\r\n governmental expenditures and employment for criminal justice\r\n activities in the United States. Information is supplied on police\r\n protection, judicial and legal services, and correctional institutions\r\n and agencies. Variables describing each of these criminal justice\r\n functions include number of and payroll for full-time, part-time, and\r\n full-time-equivalent employees, current total and general\r\nexpenditures, capital outlay, and intergovernmental expenditures.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03408.v1",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1998  "
+                }
+            ],
+            "identifier": "121",
+            "isPartOf": "2429",
+            "issued": "2002-06-07T00:00:00",
             "keyword": [
                 "correctional system",
                 "criminal justice system",
@@ -7169,54 +7163,54 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "2002-06-07T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03408.v1",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1998  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1999  ",
-            "description": "This file provides data on federal, state, and local\r\n governmental expenditures and employment for criminal justice\r\n activities in the United States. Information is supplied on police\r\n protection, judicial and legal services, and correctional institutions\r\n and agencies. Variables describing each of these criminal justice\r\n functions include number of and payroll for full-time, part-time, and\r\n full-time-equivalent employees, current total and general\r\nexpenditures, capital outlay, and intergovernmental expenditures.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2002-06-07T00:00:00",
-            "accessLevel": "public",
-            "identifier": "122",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1998  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This file provides data on federal, state, and local\r\n governmental expenditures and employment for criminal justice\r\n activities in the United States. Information is supplied on police\r\n protection, judicial and legal services, and correctional institutions\r\n and agencies. Variables describing each of these criminal justice\r\n functions include number of and payroll for full-time, part-time, and\r\n full-time-equivalent employees, current total and general\r\nexpenditures, capital outlay, and intergovernmental expenditures.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03409.v1",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1999  "
+                }
+            ],
+            "identifier": "122",
+            "isPartOf": "2429",
+            "issued": "2002-06-07T00:00:00",
             "keyword": [
                 "correctional system",
                 "criminal justice system",
@@ -7230,54 +7224,54 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2002-06-07T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "2002-06-07T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03409.v1",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1999  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 2000  ",
-            "description": "This file provides data on federal, state, and local\r\n governmental expenditures and employment for criminal justice\r\n activities in the United States. Information is supplied on police\r\n protection, judicial and legal services, and correctional institutions\r\n and agencies. Variables describing each of these criminal justice\r\n functions include number of and payroll for full-time, part-time, and\r\n full-time-equivalent employees, current total and general\r\nexpenditures, capital outlay, and intergovernmental expenditures.",
-            "modified": "2004-05-05T00:00:00",
-            "accessLevel": "public",
-            "identifier": "123",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 1999  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This file provides data on federal, state, and local\r\n governmental expenditures and employment for criminal justice\r\n activities in the United States. Information is supplied on police\r\n protection, judicial and legal services, and correctional institutions\r\n and agencies. Variables describing each of these criminal justice\r\n functions include number of and payroll for full-time, part-time, and\r\n full-time-equivalent employees, current total and general\r\nexpenditures, capital outlay, and intergovernmental expenditures.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03961.v1",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 2000  "
+                }
+            ],
+            "identifier": "123",
+            "isPartOf": "2429",
+            "issued": "2004-05-05T00:00:00",
             "keyword": [
                 "correctional system",
                 "criminal justice system",
@@ -7291,54 +7285,54 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2004-05-05T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "2004-05-05T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03961.v1",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 2000  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 2001  ",
-            "description": "This file provides data on federal, state, and local\r\n governmental expenditures and employment for criminal justice activities\r\n in the United States. Information is supplied on police protection,\r\n judicial and legal services, and correctional institutions and agencies.\r\n Variables describing each of these criminal justice functions include\r\n number of, and payroll for, full-time, part-time, and\r\n full-time-equivalent employees, current total and general expenditures,\r\ncapital outlay, and intergovernmental expenditures.",
-            "modified": "2004-04-28T00:00:00",
-            "accessLevel": "public",
-            "identifier": "124",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 2000  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This file provides data on federal, state, and local\r\n governmental expenditures and employment for criminal justice activities\r\n in the United States. Information is supplied on police protection,\r\n judicial and legal services, and correctional institutions and agencies.\r\n Variables describing each of these criminal justice functions include\r\n number of, and payroll for, full-time, part-time, and\r\n full-time-equivalent employees, current total and general expenditures,\r\ncapital outlay, and intergovernmental expenditures.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03962.v1",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 2001  "
+                }
+            ],
+            "identifier": "124",
+            "isPartOf": "2429",
+            "issued": "2004-04-28T00:00:00",
             "keyword": [
                 "correctional system",
                 "criminal justice system",
@@ -7352,54 +7346,54 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2004-04-28T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "2004-04-28T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03962.v1",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 2001  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 2002",
-            "description": "This file provides data on federal, state, and local\r\n governmental expenditures and employment for criminal justice\r\n activities in the United States. Information is supplied on police\r\n protection, judicial and legal services, and correctional institutions\r\n and agencies. Variables describing each of these criminal justice\r\n functions include number of, and payroll for, full-time, part-time,\r\n and full-time-equivalent employees, current total and general\r\nexpenditures, capital outlay, and intergovernmental expenditures.",
-            "modified": "2005-12-19T00:00:00",
-            "accessLevel": "public",
-            "identifier": "125",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 2001  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This file provides data on federal, state, and local\r\n governmental expenditures and employment for criminal justice\r\n activities in the United States. Information is supplied on police\r\n protection, judicial and legal services, and correctional institutions\r\n and agencies. Variables describing each of these criminal justice\r\n functions include number of, and payroll for, full-time, part-time,\r\n and full-time-equivalent employees, current total and general\r\nexpenditures, capital outlay, and intergovernmental expenditures.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04365.v1",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 2002"
+                }
+            ],
+            "identifier": "125",
+            "isPartOf": "2429",
+            "issued": "2005-12-19T00:00:00",
             "keyword": [
                 "correctional system",
                 "criminal justice system",
@@ -7413,54 +7407,54 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "2005-12-19T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04365.v1",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 2002"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 2003",
-            "description": "This file provides data on federal, state, and local\r\n governmental expenditures and employment for criminal justice\r\n activities in the United States. Information is supplied on police\r\n protection, judicial and legal services, and correctional institutions\r\n and agencies. Variables describing each of these criminal justice\r\n functions include number of, and payroll for, full-time, part-time,\r\n and full-time-equivalent employees, current total and general\r\nexpenditures, capital outlay, and intergovernmental expenditures.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-12-19T00:00:00",
-            "accessLevel": "public",
-            "identifier": "126",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 2002"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This file provides data on federal, state, and local\r\n governmental expenditures and employment for criminal justice\r\n activities in the United States. Information is supplied on police\r\n protection, judicial and legal services, and correctional institutions\r\n and agencies. Variables describing each of these criminal justice\r\n functions include number of, and payroll for, full-time, part-time,\r\n and full-time-equivalent employees, current total and general\r\nexpenditures, capital outlay, and intergovernmental expenditures.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04366.v1",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 2003"
+                }
+            ],
+            "identifier": "126",
+            "isPartOf": "2429",
+            "issued": "2005-12-19T00:00:00",
             "keyword": [
                 "correctional system",
                 "criminal justice system",
@@ -7474,54 +7468,54 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-12-19T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "2005-12-19T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04366.v1",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 2003"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System:  CJEE Annual Files, 1971-1979   ",
-            "description": "This survey provides information on criminal justice\r\nemployment and expenditures for all states, counties, certain municipal\r\ngovernments, and Puerto Rico. Specific variables include full- and\r\npart-time employees and payroll, expenditures for current operations,\r\ncapital outlay and contributions to employee benefits, and\r\nintergovernmental expenditures paid to state and local governments.\r\nSectors represented in this survey include police protection, judicial\r\nservices, legal services and prosecution, public defense, and corrections,\r\nas well as other criminal justice services.",
-            "modified": "2001-03-26T00:00:00",
-            "accessLevel": "public",
-            "identifier": "127",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Expenditure and Employment Data for the Criminal Justice System [United States]:  CJEE Extracts File, 2003"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This survey provides information on criminal justice\r\nemployment and expenditures for all states, counties, certain municipal\r\ngovernments, and Puerto Rico. Specific variables include full- and\r\npart-time employees and payroll, expenditures for current operations,\r\ncapital outlay and contributions to employee benefits, and\r\nintergovernmental expenditures paid to state and local governments.\r\nSectors represented in this survey include police protection, judicial\r\nservices, legal services and prosecution, public defense, and corrections,\r\nas well as other criminal justice services.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07618.v2",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System:  CJEE Annual Files, 1971-1979   "
+                }
+            ],
+            "identifier": "127",
+            "isPartOf": "2429",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "correctional system",
                 "criminal justice system",
@@ -7535,54 +7529,54 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2001-03-26T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07618.v2",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System:  CJEE Annual Files, 1971-1979   "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System: CJEE Individual Units File and Estimates File, 1985",
-            "description": "This survey provides criminal justice expenditure and\r\n employment (CJEE) data and for all states, counties, and certain\r\n municipal governments. Specific variables include full- and part-time\r\n employees and payroll, expenditures for current operations, capital\r\n outlay and contributions to employee benefits, and intergovernmental\r\n expenditures paid to state and local governments. Sectors represented\r\n in this survey include police protection, judicial services, legal\r\n services and prosecution, public defense, and corrections, as well as\r\nother criminal justice services.",
-            "modified": "1993-03-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "128",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Expenditure and Employment Data for the Criminal Justice System:  CJEE Annual Files, 1971-1979   "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This survey provides criminal justice expenditure and\r\n employment (CJEE) data and for all states, counties, and certain\r\n municipal governments. Specific variables include full- and part-time\r\n employees and payroll, expenditures for current operations, capital\r\n outlay and contributions to employee benefits, and intergovernmental\r\n expenditures paid to state and local governments. Sectors represented\r\n in this survey include police protection, judicial services, legal\r\n services and prosecution, public defense, and corrections, as well as\r\nother criminal justice services.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08650.v1",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System: CJEE Individual Units File and Estimates File, 1985"
+                }
+            ],
+            "identifier": "128",
+            "isPartOf": "2429",
+            "issued": "1987-10-12T00:00:00",
             "keyword": [
                 "correctional system",
                 "criminal justice system",
@@ -7596,54 +7590,54 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1993-03-04T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "1987-10-12T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08650.v1",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System: CJEE Individual Units File and Estimates File, 1985"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System: CJEE individual Units File and Estimates File, 1988",
-            "description": "This survey provides criminal justice expenditure and\r\n employment (CJEE) data for all states, counties, and certain municipal\r\n governments. Specific variables include full- and part-time employees\r\n and payroll, expenditures for current operations, capital outlay and\r\n contributions to employee benefits, and intergovernmental expenditures\r\n paid to state and local governments. Sectors represented in this\r\n survey include police protection, judicial services, legal services\r\n and prosecution, public defense, and corrections, as well as other\r\ncriminal justice services.",
-            "modified": "1996-12-19T00:00:00",
-            "accessLevel": "public",
-            "identifier": "129",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Expenditure and Employment Data for the Criminal Justice System: CJEE Individual Units File and Estimates File, 1985"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This survey provides criminal justice expenditure and\r\n employment (CJEE) data for all states, counties, and certain municipal\r\n governments. Specific variables include full- and part-time employees\r\n and payroll, expenditures for current operations, capital outlay and\r\n contributions to employee benefits, and intergovernmental expenditures\r\n paid to state and local governments. Sectors represented in this\r\n survey include police protection, judicial services, legal services\r\n and prosecution, public defense, and corrections, as well as other\r\ncriminal justice services.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09446.v1",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System: CJEE individual Units File and Estimates File, 1988"
+                }
+            ],
+            "identifier": "129",
+            "isPartOf": "2429",
+            "issued": "1991-03-05T00:00:00",
             "keyword": [
                 "correctional system",
                 "criminal justice system",
@@ -7657,55 +7651,55 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1996-12-19T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "1991-03-05T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09446.v1",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System: CJEE individual Units File and Estimates File, 1988"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Expenditure and Employment Data for the Criminal Justice System: CJEE Longitudinal File, 1971-1979, 1985, 1988   ",
-            "description": "This survey provides criminal justice expenditure and\r\n employment (CJEE) data for all states and counties in the United\r\n States, certain municipal governments, and Puerto Rico. Specific\r\n variables include full- and part-time employees and payroll,\r\n expenditures for current operations, capital outlay, equipment,\r\n construction, land, and contributions to employee benefits, and\r\n intergovernmental expenditures paid to state and local\r\n governments. Sectors represented in this survey include police\r\n protection, judicial, legal services and prosecution, public defense,\r\ncorrections, and other criminal justice services.",
-            "modified": "1996-11-21T00:00:00",
-            "accessLevel": "public",
-            "identifier": "130",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
-                "hasEmail": "mailto:askbjs@usdoj.gov"
+            "title": "Expenditure and Employment Data for the Criminal Justice System: CJEE individual Units File and Estimates File, 1988"
         },
-            "keyword": [
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
+                "hasEmail": "mailto:askbjs@usdoj.gov"
+            },
+            "dataQuality": false,
+            "description": "This survey provides criminal justice expenditure and\r\n employment (CJEE) data for all states and counties in the United\r\n States, certain municipal governments, and Puerto Rico. Specific\r\n variables include full- and part-time employees and payroll,\r\n expenditures for current operations, capital outlay, equipment,\r\n construction, land, and contributions to employee benefits, and\r\n intergovernmental expenditures paid to state and local\r\n governments. Sectors represented in this survey include police\r\n protection, judicial, legal services and prosecution, public defense,\r\ncorrections, and other criminal justice services.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07636.v6",
+                    "title": "Expenditure and Employment Data for the Criminal Justice System: CJEE Longitudinal File, 1971-1979, 1985, 1988   "
+                }
+            ],
+            "identifier": "130",
+            "isPartOf": "2429",
+            "issued": "1984-03-18T00:00:00",
+            "keyword": [
                 "correctional system",
                 "criminal justice system",
                 "employment",
@@ -7718,54 +7712,54 @@
                 "state government",
                 "wages and salaries"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1996-11-21T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2429",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07636.v6",
-                    "title": "Expenditure and Employment Data for the Criminal Justice System: CJEE Longitudinal File, 1971-1979, 1985, 1988   "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Criminal Case Processing Statistics (FCCPS)",
-            "description": "The Federal Criminal Case Processing Statistics (FCCPS) data tool is an interface that can be used to analyze federal case processing data. Users can generate various statistics in the areas of federal law enforcement, prosecution/courts, and incarceration from 1998. Users can also look up data based on title and section of the U.S. Criminal Code from 1994. This data tool includes offenders held for violating federal laws. It excludes commitments from the D.C. Superior Court.",
-            "modified": "2010-01-01T00:00:00",
-            "accessLevel": "public",
-            "identifier": "131",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Expenditure and Employment Data for the Criminal Justice System: CJEE Longitudinal File, 1971-1979, 1985, 1988   "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The Federal Criminal Case Processing Statistics (FCCPS) data tool is an interface that can be used to analyze federal case processing data. Users can generate various statistics in the areas of federal law enforcement, prosecution/courts, and incarceration from 1998. Users can also look up data based on title and section of the U.S. Criminal Code from 1994. This data tool includes offenders held for violating federal laws. It excludes commitments from the D.C. Superior Court.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.bjs.gov/fjsrc/",
+                    "mediaType": "text/html",
+                    "title": "Federal Criminal Case Processing Statistics (FCCPS)"
+                }
+            ],
+            "identifier": "131",
+            "issued": "2010-01-01T00:00:00",
             "keyword": [
                 "Suspects in investigations",
                 "Persons arrested and booked",
@@ -7776,54 +7770,53 @@
                 "Prisoners entering Federal prison",
                 "Prisoners in Federal prison at year-end"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-01-01T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "2010-01-01T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.bjs.gov/fjsrc/",
-                    "mediaType": "text/html",
-                    "title": "Federal Criminal Case Processing Statistics (FCCPS)"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Gender of Prisoners Admitted to State and Federal Institutions in the United States, 1926-1987",
-            "description": "This data collection includes tabulations of annual adult\r\n admissions to federal and state correctional institutions by gender\r\n for the years 1926 through 1987. The two data files have identical\r\n structures: Part 1 includes information on male admissions, and Part 2\r\n includes information on female admissions. The 3,348 cases in each\r\n part include one case for each of the 62 years of the collection for\r\n each of the following 54 categories: the 50 states, the District of\r\n Columbia, federal institutional totals, state cumulative totals, and\r\n United States totals (the sum of the federal and state cumulative\r\n totals). The figures were drawn from a voluntary reporting program in\r\n which each state, the District of Columbia, and the Federal Bureau of\r\n Prisons reported summary and detailed statistics, as part of the\r\n National Prisoner Statistics reporting series. Each file also includes\r\nindividual state and United States general population figures.",
-            "modified": "2006-01-12T00:00:00",
-            "accessLevel": "public",
-            "identifier": "161",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Federal Criminal Case Processing Statistics (FCCPS)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection includes tabulations of annual adult\r\n admissions to federal and state correctional institutions by gender\r\n for the years 1926 through 1987. The two data files have identical\r\n structures: Part 1 includes information on male admissions, and Part 2\r\n includes information on female admissions. The 3,348 cases in each\r\n part include one case for each of the 62 years of the collection for\r\n each of the following 54 categories: the 50 states, the District of\r\n Columbia, federal institutional totals, state cumulative totals, and\r\n United States totals (the sum of the federal and state cumulative\r\n totals). The figures were drawn from a voluntary reporting program in\r\n which each state, the District of Columbia, and the Federal Bureau of\r\n Prisons reported summary and detailed statistics, as part of the\r\n National Prisoner Statistics reporting series. Each file also includes\r\nindividual state and United States general population figures.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09517.v1",
+                    "title": "Gender of Prisoners Admitted to State and Federal Institutions in the United States, 1926-1987"
+                }
+            ],
+            "identifier": "161",
+            "issued": "1991-10-23T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "federal correctional facilities",
@@ -7833,106 +7826,106 @@
                 "male inmates",
                 "state"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2006-01-12T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1991-10-23T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09517.v1",
-                    "title": "Gender of Prisoners Admitted to State and Federal Institutions in the United States, 1926-1987"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Historical Statistics on Prisoners in State and Federal institutions, Yearend 1925-1986: [United States]",
-            "description": "This data collection supplies annual data on the size of\r\n the prison population and the size of the general population in the\r\n United States for the period 1925 to 1986. These yearend counts\r\n include tabulations for prisons in each of the 50 states and the\r\n District of Columbia, as well as the federal prisons, and are intended\r\n to provide a measure of the overall size of the prison population. The\r\n figures were provided from a voluntary reporting program in which each\r\n state, the District of Columbia, and the Federal Bureau of Prisons\r\n reported summary statistics as part of the statistical information on\r\nprison populations in the United States.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "162",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Gender of Prisoners Admitted to State and Federal Institutions in the United States, 1926-1987"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection supplies annual data on the size of\r\n the prison population and the size of the general population in the\r\n United States for the period 1925 to 1986. These yearend counts\r\n include tabulations for prisons in each of the 50 states and the\r\n District of Columbia, as well as the federal prisons, and are intended\r\n to provide a measure of the overall size of the prison population. The\r\n figures were provided from a voluntary reporting program in which each\r\n state, the District of Columbia, and the Federal Bureau of Prisons\r\n reported summary statistics as part of the statistical information on\r\nprison populations in the United States.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08912.v1",
+                    "title": "Historical Statistics on Prisoners in State and Federal institutions, Yearend 1925-1986: [United States]"
+                }
+            ],
+            "identifier": "162",
+            "issued": "1989-05-04T00:00:00",
             "keyword": [
                 "United States",
                 "crime",
                 "criminal justice system",
                 "inmates"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-11-04T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1989-05-04T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08912.v1",
-                    "title": "Historical Statistics on Prisoners in State and Federal institutions, Yearend 1925-1986: [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Juvenile Defendants in Criminal Courts (JDCC):  Survey of 40 Counties in the United States, 1998  ",
-            "description": "This is an independent sample of juvenile defendants drawn\r\nfrom the State Court Processing Statistics (SCPS) for 1998 (see ICPSR\r\n2038). SCPS 1998 tracked felony cases filed in May 1998 until final\r\ndisposition or until one year had elapsed from the date of filing.\r\nSCPS 1998 presents data on felony cases filed in approximately\r\n40 of the nation's 75 most populous counties in 1998. These 75\r\ncounties account for more than a third of the United States population\r\nand approximately half of all reported crimes. The cases from these 40\r\njurisdictions were weighted to represent all felony filings during the\r\nmonth of May in the 75 most populous counties. Data were collected on\r\narrest charges, demographic characteristics, criminal history,\r\npretrial release and detention, adjudication, and sentencing. Within\r\neach sampled site, data were gathered on each juvenile felony\r\ncase. Cases were tracked through adjudication or for up to one\r\nyear. The source used to identify the upper age for juveniles and the\r\nfiling mechanism appropriate to each state was the OJJDP publication,\r\nTrying Juveniles as Adults in Criminal Court: An Analysis of State\r\nTransfer Provisions (December 1998).",
-            "modified": "2003-09-25T00:00:00",
-            "accessLevel": "public",
-            "identifier": "163",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Historical Statistics on Prisoners in State and Federal institutions, Yearend 1925-1986: [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This is an independent sample of juvenile defendants drawn\r\nfrom the State Court Processing Statistics (SCPS) for 1998 (see ICPSR\r\n2038). SCPS 1998 tracked felony cases filed in May 1998 until final\r\ndisposition or until one year had elapsed from the date of filing.\r\nSCPS 1998 presents data on felony cases filed in approximately\r\n40 of the nation's 75 most populous counties in 1998. These 75\r\ncounties account for more than a third of the United States population\r\nand approximately half of all reported crimes. The cases from these 40\r\njurisdictions were weighted to represent all felony filings during the\r\nmonth of May in the 75 most populous counties. Data were collected on\r\narrest charges, demographic characteristics, criminal history,\r\npretrial release and detention, adjudication, and sentencing. Within\r\neach sampled site, data were gathered on each juvenile felony\r\ncase. Cases were tracked through adjudication or for up to one\r\nyear. The source used to identify the upper age for juveniles and the\r\nfiling mechanism appropriate to each state was the OJJDP publication,\r\nTrying Juveniles as Adults in Criminal Court: An Analysis of State\r\nTransfer Provisions (December 1998).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03750.v1",
+                    "title": "Juvenile Defendants in Criminal Courts (JDCC):  Survey of 40 Counties in the United States, 1998  "
+                }
+            ],
+            "identifier": "163",
+            "issued": "2003-09-25T00:00:00",
             "keyword": [
                 "case processing",
                 "court cases",
@@ -7948,53 +7941,54 @@
                 "state courts",
                 "statistical data"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2003-09-25T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "2003-09-25T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03750.v1",
-                    "title": "Juvenile Defendants in Criminal Courts (JDCC):  Survey of 40 Counties in the United States, 1998  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Juvenile Detention and Correctional Facility Census, 1971",
-            "description": "The purpose of this census was to provide information on\r\njuvenile detention centers throughout the United States. The data\r\ninclude information on type of facility, level of government\r\nadministering the facility, resident population by sex, by age range,\r\nby detention status, and by offense, admissions and discharges,\r\naverage length of stay, staffing and expenditures, age and capacity of\r\nfacility, and programs and services available.",
-            "modified": "2008-02-06T00:00:00",
-            "accessLevel": "public",
-            "identifier": "164",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Juvenile Defendants in Criminal Courts (JDCC):  Survey of 40 Counties in the United States, 1998  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of this census was to provide information on\r\njuvenile detention centers throughout the United States. The data\r\ninclude information on type of facility, level of government\r\nadministering the facility, resident population by sex, by age range,\r\nby detention status, and by offense, admissions and discharges,\r\naverage length of stay, staffing and expenditures, age and capacity of\r\nfacility, and programs and services available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07637.v2",
+                    "title": "Juvenile Detention and Correctional Facility Census, 1971"
+                }
+            ],
+            "identifier": "164",
+            "isPartOf": "2588",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "census data",
                 "correctional facilities (juveniles)",
@@ -8010,54 +8004,54 @@
                 "restitution centers",
                 "status offenses"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-02-06T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2588",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07637.v2",
-                    "title": "Juvenile Detention and Correctional Facility Census, 1971"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Juvenile Detention and Correctional Facility Census, 1973",
-            "description": "This survey provides information on the characteristics and\r\n administration of juvenile detention and correctional facilities. Six\r\n types of facilities are covered in this study: (1) detention centers,\r\n (2) shelters, (3) reception or diagnostic centers, (4) ranches,\r\n forestry camps, and farms, (5) halfway houses and group homes, and (6)\r\n training schools. Survey items include facility capacity, number of\r\n full-and part-time staff, number of admissions and discharges, average\r\n quarterly population, and expenditures by the facility. Data for\r\nfacility residents include age and sex, and average length of stay.",
-            "modified": "2008-06-04T13:26:37",
-            "accessLevel": "public",
-            "identifier": "165",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Juvenile Detention and Correctional Facility Census, 1971"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This survey provides information on the characteristics and\r\n administration of juvenile detention and correctional facilities. Six\r\n types of facilities are covered in this study: (1) detention centers,\r\n (2) shelters, (3) reception or diagnostic centers, (4) ranches,\r\n forestry camps, and farms, (5) halfway houses and group homes, and (6)\r\n training schools. Survey items include facility capacity, number of\r\n full-and part-time staff, number of admissions and discharges, average\r\n quarterly population, and expenditures by the facility. Data for\r\nfacility residents include age and sex, and average length of stay.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07639.v3",
+                    "title": "Juvenile Detention and Correctional Facility Census, 1973"
+                }
+            ],
+            "identifier": "165",
+            "isPartOf": "2588",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "census data",
                 "correctional facilities",
@@ -8065,54 +8059,54 @@
                 "criminal justice system",
                 "juvenile delinquency"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-06-04T13:26:37",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2588",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07639.v3",
-                    "title": "Juvenile Detention and Correctional Facility Census, 1973"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Juvenile Detention and Correctional Facility Census, 1974",
-            "description": "The 1974 census includes juvenile detention and\r\ncorrectional facilities that were operated by state or local\r\ngovernments in November 1974, and had been in operation for at least a\r\nmonth prior to June 30, 1974. There is one record for each juvenile\r\ndetention facility that had a population of at least 50 percent\r\njuveniles. Each record is classified into one of six categories:\r\ndetention centers or shelters, reception or diagnostic centers,\r\ntraining schools, ranches, forestry camps and farms, and halfway\r\nhouses and group homes. Data include state, county, and city\r\nidentification, level of government responsible for the facility, type\r\nof agency, agency identification, resident population by sex, age\r\nrange, detention status, and offense, admissions and departures of\r\npopulation, average length of stay, staffing and expenditures, age and\r\ncapacity of the facility, and programs and services available.",
-            "modified": "2008-03-26T09:12:22",
-            "accessLevel": "public",
-            "identifier": "166",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Juvenile Detention and Correctional Facility Census, 1973"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 1974 census includes juvenile detention and\r\ncorrectional facilities that were operated by state or local\r\ngovernments in November 1974, and had been in operation for at least a\r\nmonth prior to June 30, 1974. There is one record for each juvenile\r\ndetention facility that had a population of at least 50 percent\r\njuveniles. Each record is classified into one of six categories:\r\ndetention centers or shelters, reception or diagnostic centers,\r\ntraining schools, ranches, forestry camps and farms, and halfway\r\nhouses and group homes. Data include state, county, and city\r\nidentification, level of government responsible for the facility, type\r\nof agency, agency identification, resident population by sex, age\r\nrange, detention status, and offense, admissions and departures of\r\npopulation, average length of stay, staffing and expenditures, age and\r\ncapacity of the facility, and programs and services available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07706.v2",
+                    "title": "Juvenile Detention and Correctional Facility Census, 1974"
+                }
+            ],
+            "identifier": "166",
+            "isPartOf": "2588",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "census data",
                 "correctional facilities (juveniles)",
@@ -8120,54 +8114,54 @@
                 "juvenile crime",
                 "juvenile offenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-03-26T09:12:22",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2588",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07706.v2",
-                    "title": "Juvenile Detention and Correctional Facility Census, 1974"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Juvenile Detention and Correctional Facility Census, 1975",
-            "description": "The 1975 census includes juvenile detention and\r\ncorrectional facilities that were operated by state or local\r\ngovernments in November, 1975, and had been in operation at least a\r\nmonth prior to June 30, 1975. There is one record for each juvenile\r\ndetention facility that had a population of at least 50 percent\r\njuveniles. Each record is classified into one of six categories:\r\ndetention centers or shelters, reception or diagnostic centers,\r\ntraining schools, ranches, forestry camps and farms, and halfway\r\nhouses and group homes. Data include state, county, and city\r\nidentification, level of government responsible for the facility, type\r\nof agency, agency identification, resident population by sex, age\r\nrange, detention status, and offense, admissions and departures of\r\npopulation, average length of stay, staffing and expenditures, age and\r\ncapacity of the facility, and programs and services available.",
-            "modified": "2008-01-29T00:00:00",
-            "accessLevel": "public",
-            "identifier": "167",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Juvenile Detention and Correctional Facility Census, 1974"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 1975 census includes juvenile detention and\r\ncorrectional facilities that were operated by state or local\r\ngovernments in November, 1975, and had been in operation at least a\r\nmonth prior to June 30, 1975. There is one record for each juvenile\r\ndetention facility that had a population of at least 50 percent\r\njuveniles. Each record is classified into one of six categories:\r\ndetention centers or shelters, reception or diagnostic centers,\r\ntraining schools, ranches, forestry camps and farms, and halfway\r\nhouses and group homes. Data include state, county, and city\r\nidentification, level of government responsible for the facility, type\r\nof agency, agency identification, resident population by sex, age\r\nrange, detention status, and offense, admissions and departures of\r\npopulation, average length of stay, staffing and expenditures, age and\r\ncapacity of the facility, and programs and services available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07707.v3",
+                    "title": "Juvenile Detention and Correctional Facility Census, 1975"
+                }
+            ],
+            "identifier": "167",
+            "isPartOf": "2588",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "census data",
                 "correctional facilities (juveniles)",
@@ -8175,54 +8169,54 @@
                 "juvenile crime",
                 "juvenile offenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-01-29T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2588",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07707.v3",
-                    "title": "Juvenile Detention and Correctional Facility Census, 1975"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Juvenile Detention and Correctional Facility Census, 1977",
-            "description": "The 1977 Juvenile Detention and Correctional Facility\r\nCensus, is the fifth in a series of surveys of state and local public\r\nresidential facilities in the juvenile justice system. There is one\r\nrecord for each juvenile detention facility that had a population of\r\nat least 50 percent juveniles. Each record is classified into one of\r\nsix categories: detention centers or shelters, reception or diagnostic\r\ncenters, training schools, ranches, forestry camps and farms, and\r\nhalfway houses and group homes. Data include state, county, and city\r\nidentification, level of government responsible for the facility, type\r\nof agency, agency identification, resident population by sex, age\r\nrange, detention status, and offense, admissions and departures of\r\npopulation, average length of stay, staffing and expenditures, age and\r\ncapacity of the facility, and programs and services available.",
-            "modified": "2008-03-26T09:06:55",
-            "accessLevel": "public",
-            "identifier": "168",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Juvenile Detention and Correctional Facility Census, 1975"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 1977 Juvenile Detention and Correctional Facility\r\nCensus, is the fifth in a series of surveys of state and local public\r\nresidential facilities in the juvenile justice system. There is one\r\nrecord for each juvenile detention facility that had a population of\r\nat least 50 percent juveniles. Each record is classified into one of\r\nsix categories: detention centers or shelters, reception or diagnostic\r\ncenters, training schools, ranches, forestry camps and farms, and\r\nhalfway houses and group homes. Data include state, county, and city\r\nidentification, level of government responsible for the facility, type\r\nof agency, agency identification, resident population by sex, age\r\nrange, detention status, and offense, admissions and departures of\r\npopulation, average length of stay, staffing and expenditures, age and\r\ncapacity of the facility, and programs and services available.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07758.v2",
+                    "title": "Juvenile Detention and Correctional Facility Census, 1977"
+                }
+            ],
+            "identifier": "168",
+            "isPartOf": "2588",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "census data",
                 "correctional facilities (juveniles)",
@@ -8237,54 +8231,54 @@
                 "restitution centers",
                 "status offenses"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-03-26T09:06:55",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2588",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07758.v2",
-                    "title": "Juvenile Detention and Correctional Facility Census, 1977"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Law Enforcement Agency Identifiers Crosswalk [United States], 1996     ",
-            "description": "Researchers have long been able to analyze crime and law\r\nenforcement data at the individual agency level (see UNIFORM CRIME\r\nREPORTING PROGRAM DATA: [UNITED STATES] [ICPSR 9028]) and at the\r\ncounty level (see, for example, UNIFORM CRIME REPORTING PROGRAM DATA\r\n[UNITED STATES]: COUNTY-LEVEL DETAILED ARREST AND OFFENSE DATA, 1997\r\n[ICPSR 2764]). However, analyzing crime data at the intermediate\r\nlevel, the city or place, has been difficult. To facilitate the\r\ncreation and analysis of place-level data, the Bureau of Justice\r\nStatistics (BJS) and the National Archive of Criminal Justice Data\r\n(NACJD) created the Law Enforcement Agency Identifiers Crosswalk. The\r\ncrosswalk file was designed to provide geographic and other\r\nidentification information for each record included in either the\r\nFederal Bureau of Investigation's Uniform Crime Reports (UCR) files or\r\nBJS's Directory of Law Enforcement Agencies. The main variables for\r\neach record are the UCR originating agency identifier number, agency\r\nname, mailing address, Census Bureau's government identification\r\nnumber, UCR state and county codes, and Federal Information Processing\r\nStandards (FIPS) state, county, and place codes. These variables make\r\nit possible for researchers to take police agency-level data, combine\r\nthem with Bureau of the Census and BJS data, and perform place-level,\r\njurisdiction-level, and government-level analyses.",
-            "modified": "2001-09-20T00:00:00",
-            "accessLevel": "public",
-            "identifier": "169",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Juvenile Detention and Correctional Facility Census, 1977"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "Researchers have long been able to analyze crime and law\r\nenforcement data at the individual agency level (see UNIFORM CRIME\r\nREPORTING PROGRAM DATA: [UNITED STATES] [ICPSR 9028]) and at the\r\ncounty level (see, for example, UNIFORM CRIME REPORTING PROGRAM DATA\r\n[UNITED STATES]: COUNTY-LEVEL DETAILED ARREST AND OFFENSE DATA, 1997\r\n[ICPSR 2764]). However, analyzing crime data at the intermediate\r\nlevel, the city or place, has been difficult. To facilitate the\r\ncreation and analysis of place-level data, the Bureau of Justice\r\nStatistics (BJS) and the National Archive of Criminal Justice Data\r\n(NACJD) created the Law Enforcement Agency Identifiers Crosswalk. The\r\ncrosswalk file was designed to provide geographic and other\r\nidentification information for each record included in either the\r\nFederal Bureau of Investigation's Uniform Crime Reports (UCR) files or\r\nBJS's Directory of Law Enforcement Agencies. The main variables for\r\neach record are the UCR originating agency identifier number, agency\r\nname, mailing address, Census Bureau's government identification\r\nnumber, UCR state and county codes, and Federal Information Processing\r\nStandards (FIPS) state, county, and place codes. These variables make\r\nit possible for researchers to take police agency-level data, combine\r\nthem with Bureau of the Census and BJS data, and perform place-level,\r\njurisdiction-level, and government-level analyses.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR02876.v1",
+                    "title": "Law Enforcement Agency Identifiers Crosswalk [United States], 1996     "
+                }
+            ],
+            "identifier": "169",
+            "isPartOf": "2632",
+            "issued": "2000-03-15T00:00:00",
             "keyword": [
                 "crime mapping",
                 "crime patterns",
@@ -8292,54 +8286,54 @@
                 "information systems",
                 "law enforcement agencies"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2001-09-20T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2632",
-            "dataQuality": false,
-            "issued": "2000-03-15T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR02876.v1",
-                    "title": "Law Enforcement Agency Identifiers Crosswalk [United States], 1996     "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Law Enforcement Agency Identifiers Crosswalk [United States], 2000",
-            "description": "Researchers have long been able to analyze crime and law\r\nenforcement data at the individual agency level (see UNIFORM CRIME\r\nREPORTING PROGRAM DATA: [UNITED STATES] [ICPSR 9028]) and at the\r\ncounty level (see, for example, UNIFORM CRIME REPORTING PROGRAM DATA\r\n[UNITED STATES]: COUNTY-LEVEL DETAILED ARREST AND OFFENSE DATA, 1997\r\n[ICPSR 2764]). However, analyzing crime data at the intermediate\r\nlevel, the city or place, has been difficult. To facilitate the\r\ncreation and analysis of place-level data, the Bureau of Justice\r\nStatistics (BJS) and the National Archive of Criminal Justice Data\r\n(NACJD) created the Law Enforcement Agency Identifiers Crosswalk. The\r\ncrosswalk file was designed to provide geographic and other\r\nidentification information for each record included in either the\r\nFederal Bureau of Investigation's Uniform Crime Reports (UCR) files or\r\nBJS's Directory of Law Enforcement Agencies.  The main variables for\r\neach record are the UCR originating agency identifier number, agency\r\nname, mailing address, Census Bureau's government identification\r\nnumber, UCR state and county codes, and Federal Information Processing\r\nStandards (FIPS) state, county, and place codes. These variables make\r\nit possible for researchers to take police agency-level data, combine\r\nthem with Bureau of the Census and BJS data, and perform place-level,\r\njurisdiction-level, and government-level analyses.",
-            "modified": "2004-09-16T00:00:00",
-            "accessLevel": "public",
-            "identifier": "170",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Law Enforcement Agency Identifiers Crosswalk [United States], 1996     "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "Researchers have long been able to analyze crime and law\r\nenforcement data at the individual agency level (see UNIFORM CRIME\r\nREPORTING PROGRAM DATA: [UNITED STATES] [ICPSR 9028]) and at the\r\ncounty level (see, for example, UNIFORM CRIME REPORTING PROGRAM DATA\r\n[UNITED STATES]: COUNTY-LEVEL DETAILED ARREST AND OFFENSE DATA, 1997\r\n[ICPSR 2764]). However, analyzing crime data at the intermediate\r\nlevel, the city or place, has been difficult. To facilitate the\r\ncreation and analysis of place-level data, the Bureau of Justice\r\nStatistics (BJS) and the National Archive of Criminal Justice Data\r\n(NACJD) created the Law Enforcement Agency Identifiers Crosswalk. The\r\ncrosswalk file was designed to provide geographic and other\r\nidentification information for each record included in either the\r\nFederal Bureau of Investigation's Uniform Crime Reports (UCR) files or\r\nBJS's Directory of Law Enforcement Agencies.  The main variables for\r\neach record are the UCR originating agency identifier number, agency\r\nname, mailing address, Census Bureau's government identification\r\nnumber, UCR state and county codes, and Federal Information Processing\r\nStandards (FIPS) state, county, and place codes. These variables make\r\nit possible for researchers to take police agency-level data, combine\r\nthem with Bureau of the Census and BJS data, and perform place-level,\r\njurisdiction-level, and government-level analyses.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04082.v1",
+                    "title": "Law Enforcement Agency Identifiers Crosswalk [United States], 2000"
+                }
+            ],
+            "identifier": "170",
+            "isPartOf": "2632",
+            "issued": "2004-09-16T00:00:00",
             "keyword": [
                 "crime mapping",
                 "crime patterns",
@@ -8347,54 +8341,54 @@
                 "information systems",
                 "law enforcement agencies"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2004-09-16T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2632",
-            "dataQuality": false,
-            "issued": "2004-09-16T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04082.v1",
-                    "title": "Law Enforcement Agency Identifiers Crosswalk [United States], 2000"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Law Enforcement Management and Administrative Statistics (LEMAS), 1987",
-            "description": "This survey, the first in the Bureau of Justice Statistics' program on Law Enforcement Management and Administrative Statistics (LEMAS), presents information on three types of general purpose law enforcement agencies: state police, local police, and sheriffs' departments. Data from the primary state police agency in each of 49 states (Hawaii does not have a state police agency) are also presented. Variables include size of the populations served by the typical police or sheriffs' department, levels of employment and spending, various functions of the department, average salary levels for uniformed officers, and other matters relating to management and personnel.",
-            "modified": "2012-08-01T17:08:19",
-            "accessLevel": "public",
-            "identifier": "171",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Law Enforcement Agency Identifiers Crosswalk [United States], 2000"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This survey, the first in the Bureau of Justice Statistics' program on Law Enforcement Management and Administrative Statistics (LEMAS), presents information on three types of general purpose law enforcement agencies: state police, local police, and sheriffs' departments. Data from the primary state police agency in each of 49 states (Hawaii does not have a state police agency) are also presented. Variables include size of the populations served by the typical police or sheriffs' department, levels of employment and spending, various functions of the department, average salary levels for uniformed officers, and other matters relating to management and personnel.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09222.v3",
+                    "title": "Law Enforcement Management and Administrative Statistics (LEMAS), 1987"
+                }
+            ],
+            "identifier": "171",
+            "isPartOf": "2430",
+            "issued": "1989-12-15T00:00:00",
             "keyword": [
                 "administration",
                 "budgets",
@@ -8407,54 +8401,54 @@
                 "wages and salaries",
                 "workers"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2012-08-01T17:08:19",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2430",
-            "dataQuality": false,
-            "issued": "1989-12-15T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09222.v3",
-                    "title": "Law Enforcement Management and Administrative Statistics (LEMAS), 1987"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Law Enforcement Management and Administrative Statistics (LEMAS), 1990",
-            "description": "This survey, the second in the Bureau of Justice Statistics' program on Law Enforcement and Administrative Statistics (LEMAS), presents information on four types of general-purpose law enforcement agencies: state police, local police, special police, and sheriff's departments. Variables include size of the population served by the police or sheriff's department, levels of employment and spending, various functions of the department, average salary levels for uniformed officers, and other matters related to management and personnel.",
-            "modified": "2012-08-02T12:21:58",
-            "accessLevel": "public",
-            "identifier": "172",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Law Enforcement Management and Administrative Statistics (LEMAS), 1987"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This survey, the second in the Bureau of Justice Statistics' program on Law Enforcement and Administrative Statistics (LEMAS), presents information on four types of general-purpose law enforcement agencies: state police, local police, special police, and sheriff's departments. Variables include size of the population served by the police or sheriff's department, levels of employment and spending, various functions of the department, average salary levels for uniformed officers, and other matters related to management and personnel.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09749.v3",
+                    "title": "Law Enforcement Management and Administrative Statistics (LEMAS), 1990"
+                }
+            ],
+            "identifier": "172",
+            "isPartOf": "2430",
+            "issued": "1993-04-03T00:00:00",
             "keyword": [
                 "administration",
                 "budgets",
@@ -8467,54 +8461,54 @@
                 "wages and salaries",
                 "workers"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2012-08-02T12:21:58",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2430",
-            "dataQuality": false,
-            "issued": "1993-04-03T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09749.v3",
-                    "title": "Law Enforcement Management and Administrative Statistics (LEMAS), 1990"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Law Enforcement Management and Administrative Statistics (LEMAS), 1993",
-            "description": "This survey, the third in the Bureau of Justice Statistics'\r\nprogram on Law Enforcement and Administrative Statistics (LEMAS),\r\npresents information on five types of general-purpose law enforcement\r\nagencies: state police, county police, special police (state and local),\r\nmunicipal police, and sheriff's departments. Variables include size of\r\nthe population served by the police or sheriff's department, levels of\r\nemployment and spending, various functions of the department, average\r\nsalary levels for uniformed officers, policies and programs, and other\r\nmatters related to management and personnel.",
-            "modified": "2012-08-02T12:23:48",
-            "accessLevel": "public",
-            "identifier": "173",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Law Enforcement Management and Administrative Statistics (LEMAS), 1990"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This survey, the third in the Bureau of Justice Statistics'\r\nprogram on Law Enforcement and Administrative Statistics (LEMAS),\r\npresents information on five types of general-purpose law enforcement\r\nagencies: state police, county police, special police (state and local),\r\nmunicipal police, and sheriff's departments. Variables include size of\r\nthe population served by the police or sheriff's department, levels of\r\nemployment and spending, various functions of the department, average\r\nsalary levels for uniformed officers, policies and programs, and other\r\nmatters related to management and personnel.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06708.v3",
+                    "title": "Law Enforcement Management and Administrative Statistics (LEMAS), 1993"
+                }
+            ],
+            "identifier": "173",
+            "isPartOf": "2430",
+            "issued": "1996-09-30T00:00:00",
             "keyword": [
                 "administration",
                 "budgets",
@@ -8527,54 +8521,54 @@
                 "wages and salaries",
                 "workers"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2012-08-02T12:23:48",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2430",
-            "dataQuality": false,
-            "issued": "1996-09-30T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06708.v3",
-                    "title": "Law Enforcement Management and Administrative Statistics (LEMAS), 1993"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Law Enforcement Management and Administrative Statistics (LEMAS), 2007",
-            "description": "Every three to four years, the Bureau of Justice Statistics (BJS) surveys a nationally\r\nrepresentative sample of state and local law enforcement agencies. The surveys\r\nare conducted as part of the Law Enforcement Management and Administrative\r\nStatistics (LEMAS) program. Data include agency\r\npersonnel, expenditures and pay, operations, community policing\r\ninitiatives, equipment, computers and information systems, and written\r\npolicies. The LEMAS survey has been conducted in 1987, 1990, 1993,\r\n1997, 1999 (limited scope), 2000, 2003, and 2007.",
-            "modified": "2011-07-07T14:33:29",
-            "accessLevel": "public",
-            "identifier": "174",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Law Enforcement Management and Administrative Statistics (LEMAS), 1993"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "Every three to four years, the Bureau of Justice Statistics (BJS) surveys a nationally\r\nrepresentative sample of state and local law enforcement agencies. The surveys\r\nare conducted as part of the Law Enforcement Management and Administrative\r\nStatistics (LEMAS) program. Data include agency\r\npersonnel, expenditures and pay, operations, community policing\r\ninitiatives, equipment, computers and information systems, and written\r\npolicies. The LEMAS survey has been conducted in 1987, 1990, 1993,\r\n1997, 1999 (limited scope), 2000, 2003, and 2007.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR31161.v1",
+                    "title": "Law Enforcement Management and Administrative Statistics (LEMAS), 2007"
+                }
+            ],
+            "identifier": "174",
+            "isPartOf": "2430",
+            "issued": "2011-07-07T14:33:29",
             "keyword": [
                 "administration",
                 "budgets",
@@ -8587,54 +8581,54 @@
                 "wages and salaries",
                 "workers"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-07-07T14:33:29",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2430",
-            "dataQuality": false,
-            "issued": "2011-07-07T14:33:29",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR31161.v1",
-                    "title": "Law Enforcement Management and Administrative Statistics (LEMAS), 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Law Enforcement Management and Administrative Statistics (LEMAS): 1997 Sample Survey of Law Enforcement Agencies",
-            "description": "This survey, the fourth in the Bureau of Justice Statistics' program on Law Enforcement and Administrative Statistics (LEMAS), presents information on law enforcement agencies: state police, county police, special police (state and local), municipal police, and sheriff's departments. Variables include size of the population served by the police or sheriff's department, levels of employment and spending, various functions of the department, average salary levels for uniformed officers, policies and programs, and other matters related to management and personnel.",
-            "modified": "2008-12-04T09:55:18",
-            "accessLevel": "public",
-            "identifier": "175",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Law Enforcement Management and Administrative Statistics (LEMAS), 2007"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This survey, the fourth in the Bureau of Justice Statistics' program on Law Enforcement and Administrative Statistics (LEMAS), presents information on law enforcement agencies: state police, county police, special police (state and local), municipal police, and sheriff's departments. Variables include size of the population served by the police or sheriff's department, levels of employment and spending, various functions of the department, average salary levels for uniformed officers, policies and programs, and other matters related to management and personnel.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR02700.v1",
+                    "title": "Law Enforcement Management and Administrative Statistics (LEMAS): 1997 Sample Survey of Law Enforcement Agencies"
+                }
+            ],
+            "identifier": "175",
+            "isPartOf": "2430",
+            "issued": "1999-06-16T00:00:00",
             "keyword": [
                 "administration",
                 "budgets",
@@ -8647,54 +8641,54 @@
                 "wages and salaries",
                 "workers"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-12-04T09:55:18",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2430",
-            "dataQuality": false,
-            "issued": "1999-06-16T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR02700.v1",
-                    "title": "Law Enforcement Management and Administrative Statistics (LEMAS): 1997 Sample Survey of Law Enforcement Agencies"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Law Enforcement Management and Administrative Statistics (LEMAS): 1999 Sample Survey of Law Enforcement Agencies",
-            "description": "This survey, the fourth in the Bureau of Justice Statistics' program on Law Enforcement Management and Administrative Statistics (LEMAS), presents information on law enforcement agencies: state police, county police, special police (state and local), municipal police, and sheriff's departments. Variables include size of the population served by the police or sheriff's department, levels of employment and spending, various functions of the department, average salary levels for uniformed officers, policies and programs, and other matters related to management and personnel.",
-            "modified": "2008-12-09T08:40:36",
-            "accessLevel": "public",
-            "identifier": "176",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Law Enforcement Management and Administrative Statistics (LEMAS): 1997 Sample Survey of Law Enforcement Agencies"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This survey, the fourth in the Bureau of Justice Statistics' program on Law Enforcement Management and Administrative Statistics (LEMAS), presents information on law enforcement agencies: state police, county police, special police (state and local), municipal police, and sheriff's departments. Variables include size of the population served by the police or sheriff's department, levels of employment and spending, various functions of the department, average salary levels for uniformed officers, policies and programs, and other matters related to management and personnel.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03079.v2",
+                    "title": "Law Enforcement Management and Administrative Statistics (LEMAS): 1999 Sample Survey of Law Enforcement Agencies"
+                }
+            ],
+            "identifier": "176",
+            "isPartOf": "2430",
+            "issued": "2001-02-23T00:00:00",
             "keyword": [
                 "administration",
                 "budgets",
@@ -8707,54 +8701,54 @@
                 "wages and salaries",
                 "workers"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-12-09T08:40:36",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2430",
-            "dataQuality": false,
-            "issued": "2001-02-23T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03079.v2",
-                    "title": "Law Enforcement Management and Administrative Statistics (LEMAS): 1999 Sample Survey of Law Enforcement Agencies"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Law Enforcement Management and Administrative Statistics (LEMAS): 2000 Sample Survey of Law Enforcement Agencies",
-            "description": "This survey, the sixth in the Bureau of Justice Statistics'\r\nprogram on Law Enforcement and Administrative Statistics (LEMAS),\r\npresents information on law enforcement agencies in the United States:\r\nstate police, county police, special police (state and local),\r\nmunicipal police, and sheriff's departments. Variables include size of\r\nthe population served by the police or sheriff's department, levels of\r\nemployment and spending, various functions of the department, average\r\nsalary levels for uniformed officers, policies and programs, and other\r\nmatters related to management and personnel.This survey, the sixth in the Bureau of Justice Statistics' program on Law Enforcement and Administrative Statistics (LEMAS), presents information on law enforcement agencies in the United States: state police, county police, special police (state and local), municipal police, and sheriff's departments. Variables include size of the population served by the police or sheriff's department, levels of employment and spending, various functions of the department, average salary levels for uniformed officers, policies and programs, and other matters related to management and personnel.",
-            "modified": "2008-12-08T12:00:58",
-            "accessLevel": "public",
-            "identifier": "177",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Law Enforcement Management and Administrative Statistics (LEMAS): 1999 Sample Survey of Law Enforcement Agencies"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This survey, the sixth in the Bureau of Justice Statistics'\r\nprogram on Law Enforcement and Administrative Statistics (LEMAS),\r\npresents information on law enforcement agencies in the United States:\r\nstate police, county police, special police (state and local),\r\nmunicipal police, and sheriff's departments. Variables include size of\r\nthe population served by the police or sheriff's department, levels of\r\nemployment and spending, various functions of the department, average\r\nsalary levels for uniformed officers, policies and programs, and other\r\nmatters related to management and personnel.This survey, the sixth in the Bureau of Justice Statistics' program on Law Enforcement and Administrative Statistics (LEMAS), presents information on law enforcement agencies in the United States: state police, county police, special police (state and local), municipal police, and sheriff's departments. Variables include size of the population served by the police or sheriff's department, levels of employment and spending, various functions of the department, average salary levels for uniformed officers, policies and programs, and other matters related to management and personnel.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03565.v2",
+                    "title": "Law Enforcement Management and Administrative Statistics (LEMAS): 2000 Sample Survey of Law Enforcement Agencies"
+                }
+            ],
+            "identifier": "177",
+            "isPartOf": "2430",
+            "issued": "2003-01-23T00:00:00",
             "keyword": [
                 "administration",
                 "budgets",
@@ -8767,54 +8761,54 @@
                 "wages and salaries",
                 "workers"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-12-08T12:00:58",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2430",
-            "dataQuality": false,
-            "issued": "2003-01-23T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03565.v2",
-                    "title": "Law Enforcement Management and Administrative Statistics (LEMAS): 2000 Sample Survey of Law Enforcement Agencies"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Law Enforcement Management and Administrative Statistics (LEMAS): 2003 Sample Survey of Law Enforcement Agencies ",
-            "description": "The Law Enforcement Management and Administrative\r\nStatistics (LEMAS) survey collects data from a nationally\r\nrepresentative sample of publicly funded State and local law\r\nenforcement agencies in the United States. Data include agency\r\npersonnel, expenditures and pay, operations, community policing\r\ninitiatives, equipment, computers and information systems, and written\r\npolicies. The LEMAS survey has been conducted in 1987, 1990, 1993,\r\n1997, 1999 (limited scope), 2000, and 2003.",
-            "modified": "2006-05-10T00:00:00",
-            "accessLevel": "public",
-            "identifier": "178",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "Law Enforcement Management and Administrative Statistics (LEMAS): 2000 Sample Survey of Law Enforcement Agencies"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The Law Enforcement Management and Administrative\r\nStatistics (LEMAS) survey collects data from a nationally\r\nrepresentative sample of publicly funded State and local law\r\nenforcement agencies in the United States. Data include agency\r\npersonnel, expenditures and pay, operations, community policing\r\ninitiatives, equipment, computers and information systems, and written\r\npolicies. The LEMAS survey has been conducted in 1987, 1990, 1993,\r\n1997, 1999 (limited scope), 2000, and 2003.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04411.v1",
+                    "title": "Law Enforcement Management and Administrative Statistics (LEMAS): 2003 Sample Survey of Law Enforcement Agencies "
+                }
+            ],
+            "identifier": "178",
+            "isPartOf": "2430",
+            "issued": "2006-05-10T00:00:00",
             "keyword": [
                 "administration",
                 "budgets",
@@ -8827,54 +8821,53 @@
                 "wages and salaries",
                 "workers"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2006-05-10T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2430",
-            "dataQuality": false,
-            "issued": "2006-05-10T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04411.v1",
-                    "title": "Law Enforcement Management and Administrative Statistics (LEMAS): 2003 Sample Survey of Law Enforcement Agencies "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Murder Cases in 33 Large Urban Counties in the United States, 1988",
-            "description": "This study was conducted in an effort to better understand \r\n the circumstances surrounding murder cases in large urban areas. To \r\n evaluate the 75 largest counties in the nation, 33 counties were \r\n chosen. The ranking of these counties was based on a combination of \r\n crime data and population data. The criteria for including a case on a \r\n roster from which cases would be sampled was that (1) one or more \r\n defendants must have been arrested for murder and (2) the case must \r\n have been adjudicated during 1988. These cases were a sample of about \r\n half of all those in the 33 counties studied that had a murder charge \r\n brought to the prosecutors in 1988, or earlier, and that were disposed \r\n during 1988. When statistically weighted, the sample cases represent a \r\n total of 9,576 murder defendants in the nation's 75 largest counties. \r\n Demographic information on victims and defendants includes sex, date of \r\n birth, area of residence, and occupation. Variables are also provided \r\n on the circumstances of the crime, including the relationship between the \r\n victim and the defendant, the type of weapon used, the time of death, \r\nand the number of victims.",
-            "modified": "2006-01-12T00:00:00",
-            "accessLevel": "public",
-            "identifier": "179",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Law Enforcement Management and Administrative Statistics (LEMAS): 2003 Sample Survey of Law Enforcement Agencies "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This study was conducted in an effort to better understand \r\n the circumstances surrounding murder cases in large urban areas. To \r\n evaluate the 75 largest counties in the nation, 33 counties were \r\n chosen. The ranking of these counties was based on a combination of \r\n crime data and population data. The criteria for including a case on a \r\n roster from which cases would be sampled was that (1) one or more \r\n defendants must have been arrested for murder and (2) the case must \r\n have been adjudicated during 1988. These cases were a sample of about \r\n half of all those in the 33 counties studied that had a murder charge \r\n brought to the prosecutors in 1988, or earlier, and that were disposed \r\n during 1988. When statistically weighted, the sample cases represent a \r\n total of 9,576 murder defendants in the nation's 75 largest counties. \r\n Demographic information on victims and defendants includes sex, date of \r\n birth, area of residence, and occupation. Variables are also provided \r\n on the circumstances of the crime, including the relationship between the \r\n victim and the defendant, the type of weapon used, the time of death, \r\nand the number of victims.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09907.v1",
+                    "title": "Murder Cases in 33 Large Urban Counties in the United States, 1988"
+                }
+            ],
+            "identifier": "179",
+            "issued": "1993-10-11T00:00:00",
             "keyword": [
                 "felony offenses",
                 "murder",
@@ -8883,53 +8876,53 @@
                 "urban areas",
                 "urban crime"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1993-10-11T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09907.v1",
-                    "title": "Murder Cases in 33 Large Urban Counties in the United States, 1988"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Surveys: Cities Attitude Sub-Sample, 1972-1975",
-            "description": "This subsample of the national crime surveys consists of\r\ndata on personal and household victimization for persons aged 12 and\r\nolder in 26 major United States cities in the period 1972-1975. The\r\nNational Crime Surveys were designed by the Bureau of Justice\r\nStatistics to meet three primary objectives: (1) to develop\r\ndetailed information about the victims and consequences of crime,\r\n(2) to estimate the numbers and types of crimes not reported to\r\npolice, and (3) to provide uniform measures of selected types of\r\ncrimes in order to permit reliable comparisons over time and between\r\nareas. The surveys provide measures of victimization on the basis\r\nof six crimes (including attempts): rape, robbery, assault, burglary,\r\nlarceny, and motor vehicle theft. The total National Crime Survey\r\nemployed two distinct samples: a National Sample, and a Cities Sample.\r\nThe cities sample consists of information about victimization in 26\r\nmajor United States cities. The data collection was conducted by the\r\nUnited States Census Bureau, initial processing of the data and\r\ndocumentation was performed by the Data Use and Access Laboratories\r\n(DUALabs), and subsequent processing was performed by the ICPSR under\r\ngrants from the Bureau of Justice Statistics (BJS). This Cities\r\nAttitude Sub-Sample study also includes information on personal attitudes\r\nand perceptions of crime and the police, the fear of crime, and the\r\neffect of this fear on behavioral patterns such as choice of shopping\r\nareas and places of entertainment. Data are provided on reasons for\r\nrespondents' choice of neighborhood, and feelings about neighborhood,\r\ncrime, personal safety, and the local police. Also specified are date,\r\ntype, place, and nature of the incidents, injuries suffered, hospital\r\ntreatment and medical expenses incurred, offender's personal profile,\r\nrelationship of offender to victim, property stolen and value, items\r\nrecovered and value, insurance coverage, and police report and reasons\r\nif incident was not reported to the police. Demographic items cover\r\nage, sex, marital status, race, ethnicity, education, employment, family\r\nincome, and previous residence and reasons for migrating. This subsample\r\nis a one-half random sample of the Complete Sample, NATIONAL CRIME\r\nSURVEYS: CITIES, 1972-1975 (ICPSR 7658), in which an attitude\r\nquestionnaire was administered. The subsample contains data from the\r\nsame 26 cities that were used in the Complete Sample.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2006-01-12T00:00:00",
-            "accessLevel": "public",
-            "identifier": "180",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Murder Cases in 33 Large Urban Counties in the United States, 1988"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This subsample of the national crime surveys consists of\r\ndata on personal and household victimization for persons aged 12 and\r\nolder in 26 major United States cities in the period 1972-1975. The\r\nNational Crime Surveys were designed by the Bureau of Justice\r\nStatistics to meet three primary objectives: (1) to develop\r\ndetailed information about the victims and consequences of crime,\r\n(2) to estimate the numbers and types of crimes not reported to\r\npolice, and (3) to provide uniform measures of selected types of\r\ncrimes in order to permit reliable comparisons over time and between\r\nareas. The surveys provide measures of victimization on the basis\r\nof six crimes (including attempts): rape, robbery, assault, burglary,\r\nlarceny, and motor vehicle theft. The total National Crime Survey\r\nemployed two distinct samples: a National Sample, and a Cities Sample.\r\nThe cities sample consists of information about victimization in 26\r\nmajor United States cities. The data collection was conducted by the\r\nUnited States Census Bureau, initial processing of the data and\r\ndocumentation was performed by the Data Use and Access Laboratories\r\n(DUALabs), and subsequent processing was performed by the ICPSR under\r\ngrants from the Bureau of Justice Statistics (BJS). This Cities\r\nAttitude Sub-Sample study also includes information on personal attitudes\r\nand perceptions of crime and the police, the fear of crime, and the\r\neffect of this fear on behavioral patterns such as choice of shopping\r\nareas and places of entertainment. Data are provided on reasons for\r\nrespondents' choice of neighborhood, and feelings about neighborhood,\r\ncrime, personal safety, and the local police. Also specified are date,\r\ntype, place, and nature of the incidents, injuries suffered, hospital\r\ntreatment and medical expenses incurred, offender's personal profile,\r\nrelationship of offender to victim, property stolen and value, items\r\nrecovered and value, insurance coverage, and police report and reasons\r\nif incident was not reported to the police. Demographic items cover\r\nage, sex, marital status, race, ethnicity, education, employment, family\r\nincome, and previous residence and reasons for migrating. This subsample\r\nis a one-half random sample of the Complete Sample, NATIONAL CRIME\r\nSURVEYS: CITIES, 1972-1975 (ICPSR 7658), in which an attitude\r\nquestionnaire was administered. The subsample contains data from the\r\nsame 26 cities that were used in the Complete Sample.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07663.v2",
+                    "title": "National Crime Surveys: Cities Attitude Sub-Sample, 1972-1975"
+                }
+            ],
+            "identifier": "180",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -8944,53 +8937,53 @@
                 "robbery",
                 "victimization"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07663.v2",
-                    "title": "National Crime Surveys: Cities Attitude Sub-Sample, 1972-1975"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Surveys: Cities, 1972-1975",
-            "description": "This sample of the National Crime Survey contains\r\ninformation about victimization in 26 central cities in the United\r\nStates. The data are designed to achieve three primary objectives: 1)\r\nto develop detailed information about the victims and consequences of\r\ncrime, 2) to estimate the numbers and types of crimes not reported to\r\npolice, and 3) to provide uniform measures of selected types of crimes\r\nand permit reliable comparisons over time and between areas of the\r\ncountry. Information about each household or personal victimization was\r\nrecorded. The data include type of crime (attempts are covered as\r\nwell), description of offender, severity of crime, injuries or losses,\r\ntime and place of occurrence, age, race and sex of offender(s),\r\nrelationship of offenders to victims, education, migration, labor force\r\nstatus, occupation, and income of persons involved.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2006-01-12T00:00:00",
-            "accessLevel": "public",
-            "identifier": "181",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Surveys: Cities Attitude Sub-Sample, 1972-1975"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This sample of the National Crime Survey contains\r\ninformation about victimization in 26 central cities in the United\r\nStates. The data are designed to achieve three primary objectives: 1)\r\nto develop detailed information about the victims and consequences of\r\ncrime, 2) to estimate the numbers and types of crimes not reported to\r\npolice, and 3) to provide uniform measures of selected types of crimes\r\nand permit reliable comparisons over time and between areas of the\r\ncountry. Information about each household or personal victimization was\r\nrecorded. The data include type of crime (attempts are covered as\r\nwell), description of offender, severity of crime, injuries or losses,\r\ntime and place of occurrence, age, race and sex of offender(s),\r\nrelationship of offenders to victims, education, migration, labor force\r\nstatus, occupation, and income of persons involved.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07658.v3",
+                    "title": "National Crime Surveys: Cities, 1972-1975"
+                }
+            ],
+            "identifier": "181",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "census data",
                 "cities",
@@ -8999,53 +8992,53 @@
                 "households",
                 "victimization"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2006-01-12T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07658.v3",
-                    "title": "National Crime Surveys: Cities, 1972-1975"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Surveys:  Crime School Supplement, 1989",
-            "description": "This supplement to the National Crime Surveys was designed\r\nto collect data on crime victimization in schools in the United States.\r\nStudent respondents were asked a series of questions to determine their\r\nschool attendance in the last six months. Other questions concerning\r\nschools were posed, including type of school, distance from home, and\r\ngeneral attendance and monitoring policies. The data present\r\ninformation on the response of the school to student violation of\r\nrules, accessibility of drugs, and violence in school, including types\r\nof violence and student reaction. Other variables cover general violent\r\ncrimes, personal larceny crimes, and household crimes and offer\r\ninformation on date, time, and place of crime. Demographic\r\ncharacteristics of household members such as age, sex, race, education,\r\nemployment, median family income, and marital status are provided.",
-            "modified": "1995-03-31T00:00:00",
-            "accessLevel": "public",
-            "identifier": "182",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Surveys: Cities, 1972-1975"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This supplement to the National Crime Surveys was designed\r\nto collect data on crime victimization in schools in the United States.\r\nStudent respondents were asked a series of questions to determine their\r\nschool attendance in the last six months. Other questions concerning\r\nschools were posed, including type of school, distance from home, and\r\ngeneral attendance and monitoring policies. The data present\r\ninformation on the response of the school to student violation of\r\nrules, accessibility of drugs, and violence in school, including types\r\nof violence and student reaction. Other variables cover general violent\r\ncrimes, personal larceny crimes, and household crimes and offer\r\ninformation on date, time, and place of crime. Demographic\r\ncharacteristics of household members such as age, sex, race, education,\r\nemployment, median family income, and marital status are provided.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09394.v2",
+                    "title": "National Crime Surveys:  Crime School Supplement, 1989"
+                }
+            ],
+            "identifier": "182",
+            "issued": "1990-08-15T00:00:00",
             "keyword": [
                 "crime in schools",
                 "national crime surveys",
@@ -9054,53 +9047,53 @@
                 "school violence",
                 "student behavior"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1995-03-31T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1990-08-15T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09394.v2",
-                    "title": "National Crime Surveys:  Crime School Supplement, 1989"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Surveys:  National Sample of Rape Victims, 1973-1982",
-            "description": "The purpose of this study was to provide an in-depth look\r\nat rapes and attempted rapes in the United States. Part 1 of the\r\ncollection offers data on rape victims and contains variables\r\nregarding the characteristics of the crime, such as the setting, the\r\nrelationship between the victim and offender, the likelihood of\r\ninjury, and the reasons why rape is not reported to police. Part 2\r\ncontains data on a control group of females who were victims of no\r\ncrime or of crimes other than rape. The information contained is\r\nsimilar to that found in Part 1.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "183",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Surveys:  Crime School Supplement, 1989"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of this study was to provide an in-depth look\r\nat rapes and attempted rapes in the United States. Part 1 of the\r\ncollection offers data on rape victims and contains variables\r\nregarding the characteristics of the crime, such as the setting, the\r\nrelationship between the victim and offender, the likelihood of\r\ninjury, and the reasons why rape is not reported to police. Part 2\r\ncontains data on a control group of females who were victims of no\r\ncrime or of crimes other than rape. The information contained is\r\nsimilar to that found in Part 1.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08625.v3",
+                    "title": "National Crime Surveys:  National Sample of Rape Victims, 1973-1982"
+                }
+            ],
+            "identifier": "183",
+            "issued": "1987-01-12T00:00:00",
             "keyword": [
                 "census data",
                 "crime",
@@ -9113,53 +9106,53 @@
                 "residential environment",
                 "victimization"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-11-04T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1987-01-12T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08625.v3",
-                    "title": "National Crime Surveys:  National Sample of Rape Victims, 1973-1982"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Surveys:  National Sample, 1973-1983   ",
-            "description": "The National Crime Survey (NCS), a study of personal and\r\nhousehold victimization, measures victimization for six selected\r\ncrimes, including attempts. The NCS was designed to achieve three\r\nprimary objectives: to develop detailed information about the victims\r\nand consequences of crime, to estimate the number and types of crimes\r\nnot reported to police, and to provide uniform measures of selected\r\ntypes of crime. The surveys cover the following types of crimes,\r\nincluding attempts: rape, robbery, assault, burglary, larceny, and\r\nauto or motor vehicle theft. Crimes such as murder, kidnapping,\r\nshoplifting, and gambling are not covered. Questions designed to\r\nobtain data on the characteristics and circumstances of the\r\nvictimization were asked in each incident report. Items such as time\r\nand place of occurrence, injuries suffered, medical expenses incurred,\r\nnumber, age, race, and sex of offender(s), relationship of offender(s)\r\nto victim (stranger, casual acquaintance, relative, etc.), and other\r\ndetailed data relevant to a complete description of the incident were\r\nincluded. Legal and technical terms, such as assault and larceny, were\r\navoided during the interviews. Incidents were later classified in more\r\ntechnical terms based upon the presence or absence of certain\r\nelements. In addition, data were collected in the study to obtain\r\ninformation on the victims' education, migration, labor force status,\r\noccupation, and income. Full data for each year are contained in Parts\r\n101-110. Incident-level extract files (Parts 1-10, 41) are available\r\nto provide users with files that are easy to manipulate. The\r\nincident-level datasets contain each incident record that appears in\r\nthe full sample file, the victim's person record, and the victim's\r\nhousehold information. These data include person and household\r\ninformation for incidents only. Subsetted person-level files also are\r\navailable as Parts 50-79. All of the variables for victims are\r\nrepeated for a maximum of four incidents per victim. There is one\r\nperson-level subset file for each interview quarter of the complete\r\nnational sample from 1973 through the second interview quarter in\r\n1980.",
-            "modified": "1998-10-05T00:00:00",
-            "accessLevel": "public",
-            "identifier": "184",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Surveys:  National Sample of Rape Victims, 1973-1982"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Survey (NCS), a study of personal and\r\nhousehold victimization, measures victimization for six selected\r\ncrimes, including attempts. The NCS was designed to achieve three\r\nprimary objectives: to develop detailed information about the victims\r\nand consequences of crime, to estimate the number and types of crimes\r\nnot reported to police, and to provide uniform measures of selected\r\ntypes of crime. The surveys cover the following types of crimes,\r\nincluding attempts: rape, robbery, assault, burglary, larceny, and\r\nauto or motor vehicle theft. Crimes such as murder, kidnapping,\r\nshoplifting, and gambling are not covered. Questions designed to\r\nobtain data on the characteristics and circumstances of the\r\nvictimization were asked in each incident report. Items such as time\r\nand place of occurrence, injuries suffered, medical expenses incurred,\r\nnumber, age, race, and sex of offender(s), relationship of offender(s)\r\nto victim (stranger, casual acquaintance, relative, etc.), and other\r\ndetailed data relevant to a complete description of the incident were\r\nincluded. Legal and technical terms, such as assault and larceny, were\r\navoided during the interviews. Incidents were later classified in more\r\ntechnical terms based upon the presence or absence of certain\r\nelements. In addition, data were collected in the study to obtain\r\ninformation on the victims' education, migration, labor force status,\r\noccupation, and income. Full data for each year are contained in Parts\r\n101-110. Incident-level extract files (Parts 1-10, 41) are available\r\nto provide users with files that are easy to manipulate. The\r\nincident-level datasets contain each incident record that appears in\r\nthe full sample file, the victim's person record, and the victim's\r\nhousehold information. These data include person and household\r\ninformation for incidents only. Subsetted person-level files also are\r\navailable as Parts 50-79. All of the variables for victims are\r\nrepeated for a maximum of four incidents per victim. There is one\r\nperson-level subset file for each interview quarter of the complete\r\nnational sample from 1973 through the second interview quarter in\r\n1980.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07635.v6",
+                    "title": "National Crime Surveys:  National Sample, 1973-1983   "
+                }
+            ],
+            "identifier": "184",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "census data",
                 "crime",
@@ -9170,53 +9163,53 @@
                 "residential environment",
                 "victimization"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1998-10-05T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07635.v6",
-                    "title": "National Crime Surveys:  National Sample, 1973-1983   "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Surveys:  National Sample, 1979-1987 [Revised Questionnaire]    ",
-            "description": "The purpose of the National Crime Surveys is to provide\r\ndata on the level of crime victimization in the United States and to\r\ncollect data on the characteristics of crime incidents and victims.\r\nInformation about each household and personal victimization was\r\nrecorded. The data include type of crime, description of the offender,\r\nseverity of crime, injuries or losses, and demographic characteristics\r\nof household members.",
-            "modified": "2004-06-17T00:00:00",
-            "accessLevel": "public",
-            "identifier": "185",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Surveys:  National Sample, 1973-1983   "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of the National Crime Surveys is to provide\r\ndata on the level of crime victimization in the United States and to\r\ncollect data on the characteristics of crime incidents and victims.\r\nInformation about each household and personal victimization was\r\nrecorded. The data include type of crime, description of the offender,\r\nseverity of crime, injuries or losses, and demographic characteristics\r\nof household members.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08608.v7",
+                    "title": "National Crime Surveys:  National Sample, 1979-1987 [Revised Questionnaire]    "
+                }
+            ],
+            "identifier": "185",
+            "issued": "1987-06-26T00:00:00",
             "keyword": [
                 "census data",
                 "crime",
@@ -9229,53 +9222,53 @@
                 "victims",
                 "violent crime"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2004-06-17T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1987-06-26T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08608.v7",
-                    "title": "National Crime Surveys:  National Sample, 1979-1987 [Revised Questionnaire]    "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Surveys:  National Sample, 1986-1992 [Near-Term Data]  ",
-            "description": "The objective of the National Crime Surveys is to provide\r\n data on the level of crime victimization in the United States and to\r\n collect information on the characteristics of crime incidents and\r\n victims. Each respondent was asked a series of screen questions to\r\n determine if he or she was victimized during the six-month period\r\n preceding the first day of the month of the interview. Screen\r\n questions cover the following types of crimes, including attempts:\r\n rape, robbery, assault, burglary, larceny, and motor vehicle\r\n theft. The data include type of crime, description of the offender,\r\n severity of the crime, injuries or losses, and demographic information\r\n on household members such as age, sex, race, education, employment,\r\nmedian family income, marital status, and military history.",
-            "modified": "2000-09-11T00:00:00",
-            "accessLevel": "public",
-            "identifier": "186",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Surveys:  National Sample, 1979-1987 [Revised Questionnaire]    "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The objective of the National Crime Surveys is to provide\r\n data on the level of crime victimization in the United States and to\r\n collect information on the characteristics of crime incidents and\r\n victims. Each respondent was asked a series of screen questions to\r\n determine if he or she was victimized during the six-month period\r\n preceding the first day of the month of the interview. Screen\r\n questions cover the following types of crimes, including attempts:\r\n rape, robbery, assault, burglary, larceny, and motor vehicle\r\n theft. The data include type of crime, description of the offender,\r\n severity of the crime, injuries or losses, and demographic information\r\n on household members such as age, sex, race, education, employment,\r\nmedian family income, marital status, and military history.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08864.v7",
+                    "title": "National Crime Surveys:  National Sample, 1986-1992 [Near-Term Data]  "
+                }
+            ],
+            "identifier": "186",
+            "issued": "1990-05-01T00:00:00",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -9289,53 +9282,53 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2000-09-11T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1990-05-01T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08864.v7",
-                    "title": "National Crime Surveys:  National Sample, 1986-1992 [Near-Term Data]  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Surveys:  Redesign Data, 1975-1979",
-            "description": "These data are a product of the National Crime Surveys\r\nRedesign Project. The purpose of the data collection was to create\r\nseveral different data files from existing public-use National Crime\r\nSurveys files. For each crime, information is gathered on the victim's\r\nhousing unit and household and the incident itself. A personal history\r\nand interview are also included. Several data files contain National\r\nCrime Survey and Uniform Crime Report data on the following index\r\ncrimes: robbery, larceny-theft, burglary, motor vehicle theft, rape,\r\nand aggravated assault.",
-            "modified": "2006-01-12T00:00:00",
-            "accessLevel": "public",
-            "identifier": "187",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Surveys:  National Sample, 1986-1992 [Near-Term Data]  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These data are a product of the National Crime Surveys\r\nRedesign Project. The purpose of the data collection was to create\r\nseveral different data files from existing public-use National Crime\r\nSurveys files. For each crime, information is gathered on the victim's\r\nhousing unit and household and the incident itself. A personal history\r\nand interview are also included. Several data files contain National\r\nCrime Survey and Uniform Crime Report data on the following index\r\ncrimes: robbery, larceny-theft, burglary, motor vehicle theft, rape,\r\nand aggravated assault.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08484.v1",
+                    "title": "National Crime Surveys:  Redesign Data, 1975-1979"
+                }
+            ],
+            "identifier": "187",
+            "issued": "1987-02-26T00:00:00",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -9351,53 +9344,53 @@
                 "robbery",
                 "victimization"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2006-01-12T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1987-02-26T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08484.v1",
-                    "title": "National Crime Surveys:  Redesign Data, 1975-1979"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Surveys: Reverse Record Check Studies: Washington, DC, San Jose, and Baltimore, 1970-1971",
-            "description": "These surveys were part of a series of pretests conducted\r\nduring the early 1970s to reveal problems associated with doing a\r\nnationwide study on victimization. They were done to determine the most\r\neffective reference period to use when questioning respondents in order\r\nto gain the fullest and most reliable information, to measure the\r\ndegree to which respondents move incidents occurring outside the\r\nreference period into that period when questioned, and to explore the\r\npossibility of identifying incidents by a few broad general questions\r\nas opposed to a series of more specific probing questions.",
-            "modified": "2006-01-18T00:00:00",
-            "accessLevel": "public",
-            "identifier": "188",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Surveys:  Redesign Data, 1975-1979"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These surveys were part of a series of pretests conducted\r\nduring the early 1970s to reveal problems associated with doing a\r\nnationwide study on victimization. They were done to determine the most\r\neffective reference period to use when questioning respondents in order\r\nto gain the fullest and most reliable information, to measure the\r\ndegree to which respondents move incidents occurring outside the\r\nreference period into that period when questioned, and to explore the\r\npossibility of identifying incidents by a few broad general questions\r\nas opposed to a series of more specific probing questions.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08693.v1",
+                    "title": "National Crime Surveys: Reverse Record Check Studies: Washington, DC, San Jose, and Baltimore, 1970-1971"
+                }
+            ],
+            "identifier": "188",
+            "issued": "1987-10-12T00:00:00",
             "keyword": [
                 "assault",
                 "crime",
@@ -9407,53 +9400,53 @@
                 "robbery",
                 "victimization"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2006-01-18T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1987-10-12T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08693.v1",
-                    "title": "National Crime Surveys: Reverse Record Check Studies: Washington, DC, San Jose, and Baltimore, 1970-1971"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Surveys: Victim Risk Supplement, 1983  ",
-            "description": "This special one-time survey was designed to collect data\r\non persons aged 12 and over reporting household victimizations. The\r\nsupplement, administered over a one-month period as part of the\r\nNational Crime Survey, gathered data on people's lifestyles in order\r\nto determine whether certain lifestyles were related to crime\r\nvictimization. Five questionnaires used by the Census Bureau for data\r\ncollection served as the data collection model for this\r\nsupplement. The first and second questionnaires, VRS-1 and VRS-2,\r\ncontained basic screen questions and an incident report,\r\nrespectively. VRS-3, the third questionnaire, was completed for every\r\nhousehold member aged 16 or older, and included items specifically\r\ndesigned to determine whether a person's lifestyle at work, home, or\r\nduring leisure time affected the risk of crime victimization. The\r\ninterviewers completed the fourth and fifth questionnaires, VRS-4 and\r\nVRS-5. They were instructed to answer questions about the respondents'\r\nneighborhoods and behavior during the interview.",
-            "modified": "1999-02-25T00:00:00",
-            "accessLevel": "public",
-            "identifier": "189",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Surveys: Reverse Record Check Studies: Washington, DC, San Jose, and Baltimore, 1970-1971"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This special one-time survey was designed to collect data\r\non persons aged 12 and over reporting household victimizations. The\r\nsupplement, administered over a one-month period as part of the\r\nNational Crime Survey, gathered data on people's lifestyles in order\r\nto determine whether certain lifestyles were related to crime\r\nvictimization. Five questionnaires used by the Census Bureau for data\r\ncollection served as the data collection model for this\r\nsupplement. The first and second questionnaires, VRS-1 and VRS-2,\r\ncontained basic screen questions and an incident report,\r\nrespectively. VRS-3, the third questionnaire, was completed for every\r\nhousehold member aged 16 or older, and included items specifically\r\ndesigned to determine whether a person's lifestyle at work, home, or\r\nduring leisure time affected the risk of crime victimization. The\r\ninterviewers completed the fourth and fifth questionnaires, VRS-4 and\r\nVRS-5. They were instructed to answer questions about the respondents'\r\nneighborhoods and behavior during the interview.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08316.v2",
+                    "title": "National Crime Surveys: Victim Risk Supplement, 1983  "
+                }
+            ],
+            "identifier": "189",
+            "issued": "1985-12-20T00:00:00",
             "keyword": [
                 "crime",
                 "criminal justice system",
@@ -9467,53 +9460,59 @@
                 "victimization",
                 "work environment"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1999-02-25T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1985-12-20T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08316.v2",
-                    "title": "National Crime Surveys: Victim Risk Supplement, 1983  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "NCVS Victimization Analysis Tool (NVAT)",
-            "description": "This dynamic analysis tool allows you to examine National Crime Victimization Survey (NCVS) data on both violent and property victimization by select victim, household, and incident characteristics.\r\n\r\nThe NCVS is the nation's primary source of information on criminal victimization. It is an annual data collection conducted by the U.S. Census Bureau for the Bureau of Justice Statistics. The NCVS collects information from a nationally representative sample of U.S. households on nonfatal crimes, reported and not reported to the police, against persons age 12 or older.\r\n\r\nViolent crimes measured by the NCVS include rape and sexual assault, robbery, aggravated assault, and simple assault. Property crimes include burglary/trespassing, motor-vehicle theft, and theft.",
-            "modified": "2012-01-01T00:00:00",
-            "accessLevel": "public",
-            "identifier": "191",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Surveys: Victim Risk Supplement, 1983  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This dynamic analysis tool allows you to examine National Crime Victimization Survey (NCVS) data on both violent and property victimization by select victim, household, and incident characteristics.\r\n\r\nThe NCVS is the nation's primary source of information on criminal victimization. It is an annual data collection conducted by the U.S. Census Bureau for the Bureau of Justice Statistics. The NCVS collects information from a nationally representative sample of U.S. households on nonfatal crimes, reported and not reported to the police, against persons age 12 or older.\r\n\r\nViolent crimes measured by the NCVS include rape and sexual assault, robbery, aggravated assault, and simple assault. Property crimes include burglary/trespassing, motor-vehicle theft, and theft.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://bjs.ojp.gov/national-crime-victimization-survey-ncvs-api",
+                    "title": "National Crime Victimization Survey (NCVS) API"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://ncvs.bjs.ojp.gov/Home",
+                    "mediaType": "text/html",
+                    "title": "National Crime Victimization Survey Data Dashboard (N-DASH)"
+                }
+            ],
+            "identifier": "191",
+            "issued": "2012-01-01T00:00:00",
             "keyword": [
                 "Aggravated assault",
                 "Crime classification",
@@ -9526,59 +9525,54 @@
                 "Simple assault",
                 "Household victimization rate"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2012-01-01T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "2012-01-01T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://bjs.ojp.gov/national-crime-victimization-survey-ncvs-api",
-                    "title": "National Crime Victimization Survey (NCVS) API"
-                },
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://ncvs.bjs.ojp.gov/Home",
-                    "mediaType": "text/html",
-                    "title": "National Crime Victimization Survey Data Dashboard (N-DASH)"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey Longitudinal File, 1995-1999",
-            "description": "The National Crime Victimization Survey (NCVS) Series,\r\n previously called the National Crime Surveys (NCS), has been\r\n collecting data on personal and household victimization through an\r\n ongoing survey of a nationally-representative sample of residential\r\n addresses since 1973. Occasionally there have been extract or\r\n supplement files created from the NCVS data series. This extract, the\r\n National Crime Victimization Survey Longitudinal File, 1995-1999,\r\n contains records from sample J19, rotations 2, 3, and 4. The Rotation\r\n 2 sample was introduced in Quarter 3, 1995, and expired in Quarter 4,\r\n 1998. The Rotation 3 sample was introduced in Quarter 1, 1996, and\r\n expired in Quarter 1, 1999. The Rotation 4 sample was introduced in\r\n Quarter 3, 1996, and expired in Quarter 4, 1999. The NCVS was designed\r\n with four primary objectives: (1) to develop detailed information\r\n about the victims and consequences of crime, (2) to estimate the\r\n number and types of crimes not reported to the police, (3) to provide\r\n uniform measures of selected types of crimes, and (4) to permit\r\n comparisons over time and types of areas. The survey categorized\r\n crimes as \"personal\" or \"property.\" Personal crimes include rape and\r\n sexual attack, robbery, aggravated and simple assault, and\r\n purse-snatching/pocket-picking, while property crimes include\r\n burglary, theft, motor vehicle theft, and vandalism. Each respondent\r\n was asked a series of screen questions designed to determine whether\r\n she or he was victimized during the six-month period preceding the\r\n first day of the month of the interview. A \"household respondent\" was\r\n also asked to report on crimes against the household as a whole (e.g.,\r\n burglary, motor vehicle theft). The data include type of crime, month,\r\n time, and location of the crime, relationship between victim and\r\n offender, characteristics of the offender, self-protective actions\r\n taken by the victim during the incident and results of those actions,\r\n consequences of the victimization, type of property lost, whether the\r\n crime was reported to police and reasons for reporting or not\r\n reporting, and offender use of weapons, drugs, and alcohol. Basic\r\n demographic information such as age, race, gender, and income was also\r\ncollected to enable analysis of crime by various subpopulations.",
-            "modified": "2007-03-14T00:00:00",
-            "accessLevel": "public",
-            "identifier": "192",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "title": "NCVS Victimization Analysis Tool (NVAT)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey (NCVS) Series,\r\n previously called the National Crime Surveys (NCS), has been\r\n collecting data on personal and household victimization through an\r\n ongoing survey of a nationally-representative sample of residential\r\n addresses since 1973. Occasionally there have been extract or\r\n supplement files created from the NCVS data series. This extract, the\r\n National Crime Victimization Survey Longitudinal File, 1995-1999,\r\n contains records from sample J19, rotations 2, 3, and 4. The Rotation\r\n 2 sample was introduced in Quarter 3, 1995, and expired in Quarter 4,\r\n 1998. The Rotation 3 sample was introduced in Quarter 1, 1996, and\r\n expired in Quarter 1, 1999. The Rotation 4 sample was introduced in\r\n Quarter 3, 1996, and expired in Quarter 4, 1999. The NCVS was designed\r\n with four primary objectives: (1) to develop detailed information\r\n about the victims and consequences of crime, (2) to estimate the\r\n number and types of crimes not reported to the police, (3) to provide\r\n uniform measures of selected types of crimes, and (4) to permit\r\n comparisons over time and types of areas. The survey categorized\r\n crimes as \"personal\" or \"property.\" Personal crimes include rape and\r\n sexual attack, robbery, aggravated and simple assault, and\r\n purse-snatching/pocket-picking, while property crimes include\r\n burglary, theft, motor vehicle theft, and vandalism. Each respondent\r\n was asked a series of screen questions designed to determine whether\r\n she or he was victimized during the six-month period preceding the\r\n first day of the month of the interview. A \"household respondent\" was\r\n also asked to report on crimes against the household as a whole (e.g.,\r\n burglary, motor vehicle theft). The data include type of crime, month,\r\n time, and location of the crime, relationship between victim and\r\n offender, characteristics of the offender, self-protective actions\r\n taken by the victim during the incident and results of those actions,\r\n consequences of the victimization, type of property lost, whether the\r\n crime was reported to police and reasons for reporting or not\r\n reporting, and offender use of weapons, drugs, and alcohol. Basic\r\n demographic information such as age, race, gender, and income was also\r\ncollected to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04414.v1",
+                    "title": "National Crime Victimization Survey Longitudinal File, 1995-1999"
+                }
+            ],
+            "identifier": "192",
+            "isPartOf": "2432",
+            "issued": "2007-03-14T00:00:00",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -9599,54 +9593,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2007-03-14T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2007-03-14T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04414.v1",
-                    "title": "National Crime Victimization Survey Longitudinal File, 1995-1999"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, 1992 [Record-Type Files]",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
-            "modified": "2008-07-29T21:55:15",
-            "accessLevel": "public",
-            "identifier": "193",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey Longitudinal File, 1995-1999"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR22929.v1",
+                    "title": "National Crime Victimization Survey, 1992 [Record-Type Files]"
+                }
+            ],
+            "identifier": "193",
+            "isPartOf": "2432",
+            "issued": "2008-07-29T21:55:15",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -9667,54 +9661,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-07-29T21:55:15",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2008-07-29T21:55:15",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR22929.v1",
-                    "title": "National Crime Victimization Survey, 1992 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, 1992-2005: Concatenated Incident-Level Files",
-            "description": "This data collection is an extract created from the\r\nindividual years of the National Crime Victimization Survey. Each\r\nrecord contains information on a crime incident occurring in the given\r\ncalendar year. Part 1 contains all crime incidents, and data Part\r\n2 contains the crimes of rape and attempted rape only. The National\r\nCrime Victimization Survey (NCVS), previously called the\r\nNational Crime Surveys (NCS), has been collecting data on personal and\r\nhousehold victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since\r\n1973. The NCVS was designed with four primary objectives: (1) to\r\ndevelop detailed information about the victims and consequences of\r\ncrime, (2) to estimate the number and types of crimes not reported to\r\nthe police, (3) to provide uniform measures of selected types of\r\ncrimes, and (4) to permit comparisons over time and types of\r\nareas. The survey categorizes crimes as \"personal\" or \"property.\"\r\nPersonal crimes include rape and sexual attack, robbery, aggravated\r\nand simple assault, and purse-snatching/pocket-picking, while property\r\ncrimes include burglary, theft, motor vehicle theft, and\r\nvandalism. Each respondent is asked a series of screen questions\r\ndesigned to determine whether she or he was victimized during the\r\nsix-month period preceding the first day of the month of the\r\ninterview. A \"household respondent\" is also asked to report on crimes\r\nagainst the household as a whole (e.g., burglary, motor vehicle\r\ntheft). The data include type of crime, month, time, and location of\r\nthe crime, relationship between victim and offender, characteristics\r\nof the offender, self-protective actions taken by the victim during\r\nthe incident and results of those actions, consequences of the\r\nvictimization, type of property lost, whether the crime was reported\r\nto police and reasons for reporting or not reporting, and offender use\r\nof weapons, drugs, and alcohol. Basic demographic information such as\r\nage, race, gender, and income is also collected, to enable analysis of\r\ncrime by various subpopulations.",
-            "modified": "2008-12-16T13:56:19",
-            "accessLevel": "public",
-            "identifier": "199",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, 1992 [Record-Type Files]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection is an extract created from the\r\nindividual years of the National Crime Victimization Survey. Each\r\nrecord contains information on a crime incident occurring in the given\r\ncalendar year. Part 1 contains all crime incidents, and data Part\r\n2 contains the crimes of rape and attempted rape only. The National\r\nCrime Victimization Survey (NCVS), previously called the\r\nNational Crime Surveys (NCS), has been collecting data on personal and\r\nhousehold victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since\r\n1973. The NCVS was designed with four primary objectives: (1) to\r\ndevelop detailed information about the victims and consequences of\r\ncrime, (2) to estimate the number and types of crimes not reported to\r\nthe police, (3) to provide uniform measures of selected types of\r\ncrimes, and (4) to permit comparisons over time and types of\r\nareas. The survey categorizes crimes as \"personal\" or \"property.\"\r\nPersonal crimes include rape and sexual attack, robbery, aggravated\r\nand simple assault, and purse-snatching/pocket-picking, while property\r\ncrimes include burglary, theft, motor vehicle theft, and\r\nvandalism. Each respondent is asked a series of screen questions\r\ndesigned to determine whether she or he was victimized during the\r\nsix-month period preceding the first day of the month of the\r\ninterview. A \"household respondent\" is also asked to report on crimes\r\nagainst the household as a whole (e.g., burglary, motor vehicle\r\ntheft). The data include type of crime, month, time, and location of\r\nthe crime, relationship between victim and offender, characteristics\r\nof the offender, self-protective actions taken by the victim during\r\nthe incident and results of those actions, consequences of the\r\nvictimization, type of property lost, whether the crime was reported\r\nto police and reasons for reporting or not reporting, and offender use\r\nof weapons, drugs, and alcohol. Basic demographic information such as\r\nage, race, gender, and income is also collected, to enable analysis of\r\ncrime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04699.v3",
+                    "title": "National Crime Victimization Survey, 1992-2005: Concatenated Incident-Level Files"
+                }
+            ],
+            "identifier": "199",
+            "isPartOf": "2432",
+            "issued": "2007-05-02T00:00:00",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -9735,54 +9729,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-12-16T13:56:19",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2007-05-02T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04699.v3",
-                    "title": "National Crime Victimization Survey, 1992-2005: Concatenated Incident-Level Files"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, 1993 [Record-Type Files]",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
-            "modified": "2008-07-29T21:50:20",
-            "accessLevel": "public",
-            "identifier": "200",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, 1992-2005: Concatenated Incident-Level Files"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR22928.v1",
+                    "title": "National Crime Victimization Survey, 1993 [Record-Type Files]"
+                }
+            ],
+            "identifier": "200",
+            "isPartOf": "2432",
+            "issued": "2008-07-29T21:50:20",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -9803,54 +9797,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-07-29T21:50:20",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2008-07-29T21:50:20",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR22928.v1",
-                    "title": "National Crime Victimization Survey, 1993 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, 1994 [Record-Type Files]",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
-            "modified": "2008-07-29T21:20:30",
-            "accessLevel": "public",
-            "identifier": "201",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, 1993 [Record-Type Files]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR22927.v1",
+                    "title": "National Crime Victimization Survey, 1994 [Record-Type Files]"
+                }
+            ],
+            "identifier": "201",
+            "isPartOf": "2432",
+            "issued": "2008-07-29T21:20:30",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -9871,54 +9865,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-07-29T21:20:30",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2008-07-29T21:20:30",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR22927.v1",
-                    "title": "National Crime Victimization Survey, 1994 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, 1995 [Record-Type Files]",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
-            "modified": "2008-07-29T21:07:01",
-            "accessLevel": "public",
-            "identifier": "202",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, 1994 [Record-Type Files]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR22926.v1",
+                    "title": "National Crime Victimization Survey, 1995 [Record-Type Files]"
+                }
+            ],
+            "identifier": "202",
+            "isPartOf": "2432",
+            "issued": "2008-07-29T21:07:01",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -9939,57 +9933,57 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-07-29T21:07:01",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2008-07-29T21:07:01",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR22926.v1",
-                    "title": "National Crime Victimization Survey, 1995 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, 1996 [Record-Type Files]",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
-            "modified": "2008-07-29T19:48:19",
-            "accessLevel": "public",
-            "identifier": "203",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, 1995 [Record-Type Files]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
-            "keyword": [
-                "assault",
-                "auto theft",
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR22925.v1",
+                    "title": "National Crime Victimization Survey, 1996 [Record-Type Files]"
+                }
+            ],
+            "identifier": "203",
+            "isPartOf": "2432",
+            "issued": "2008-07-29T19:48:19",
+            "keyword": [
+                "assault",
+                "auto theft",
                 "burglary",
                 "crime",
                 "crime costs",
@@ -10007,54 +10001,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-07-29T19:48:19",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2008-07-29T19:48:19",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR22925.v1",
-                    "title": "National Crime Victimization Survey, 1996 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, 1997 [Record-Type Files]",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
-            "modified": "2008-07-29T17:09:10",
-            "accessLevel": "public",
-            "identifier": "204",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, 1996 [Record-Type Files]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR22924.v1",
+                    "title": "National Crime Victimization Survey, 1997 [Record-Type Files]"
+                }
+            ],
+            "identifier": "204",
+            "isPartOf": "2432",
+            "issued": "2008-07-29T17:09:10",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -10075,54 +10069,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-07-29T17:09:10",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2008-07-29T17:09:10",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR22924.v1",
-                    "title": "National Crime Victimization Survey, 1997 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, 1998 [Record-Type Files]",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
-            "modified": "2008-07-27T12:24:14",
-            "accessLevel": "public",
-            "identifier": "205",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, 1997 [Record-Type Files]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR22923.v1",
+                    "title": "National Crime Victimization Survey, 1998 [Record-Type Files]"
+                }
+            ],
+            "identifier": "205",
+            "isPartOf": "2432",
+            "issued": "2008-07-27T12:24:14",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -10143,54 +10137,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-07-27T12:24:14",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2008-07-27T12:24:14",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR22923.v1",
-                    "title": "National Crime Victimization Survey, 1998 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, 1999 [Record-Type Files]",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
-            "modified": "2008-07-27T11:44:18",
-            "accessLevel": "public",
-            "identifier": "206",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, 1998 [Record-Type Files]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR22922.v1",
+                    "title": "National Crime Victimization Survey, 1999 [Record-Type Files]"
+                }
+            ],
+            "identifier": "206",
+            "isPartOf": "2432",
+            "issued": "2008-07-27T11:44:18",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -10211,54 +10205,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-07-27T11:44:18",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2008-07-27T11:44:18",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR22922.v1",
-                    "title": "National Crime Victimization Survey, 1999 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, 2000 [Record-Type Files]",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
-            "modified": "2008-07-27T11:04:46",
-            "accessLevel": "public",
-            "identifier": "207",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, 1999 [Record-Type Files]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR22921.v1",
+                    "title": "National Crime Victimization Survey, 2000 [Record-Type Files]"
+                }
+            ],
+            "identifier": "207",
+            "isPartOf": "2432",
+            "issued": "2008-07-27T11:04:46",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -10279,54 +10273,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-07-27T11:04:46",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2008-07-27T11:04:46",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR22921.v1",
-                    "title": "National Crime Victimization Survey, 2000 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, 2001 [Record-Type Files]",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
-            "modified": "2008-12-10T14:25:56",
-            "accessLevel": "public",
-            "identifier": "208",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, 2000 [Record-Type Files]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR22920.v2",
+                    "title": "National Crime Victimization Survey, 2001 [Record-Type Files]"
+                }
+            ],
+            "identifier": "208",
+            "isPartOf": "2432",
+            "issued": "2008-07-26T18:40:38",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -10347,54 +10341,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-12-10T14:25:56",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2008-07-26T18:40:38",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR22920.v2",
-                    "title": "National Crime Victimization Survey, 2001 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, 2002 [Record-Type Files]",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
-            "modified": "2008-12-10T15:38:10",
-            "accessLevel": "public",
-            "identifier": "209",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, 2001 [Record-Type Files]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR22902.v2",
+                    "title": "National Crime Victimization Survey, 2002 [Record-Type Files]"
+                }
+            ],
+            "identifier": "209",
+            "isPartOf": "2432",
+            "issued": "2008-07-27T10:50:40",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -10415,54 +10409,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-12-10T15:38:10",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2008-07-27T10:50:40",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR22902.v2",
-                    "title": "National Crime Victimization Survey, 2002 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, 2003 [Record-Type Files]",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
-            "modified": "2008-12-10T16:44:06",
-            "accessLevel": "public",
-            "identifier": "210",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, 2002 [Record-Type Files]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR22901.v2",
+                    "title": "National Crime Victimization Survey, 2003 [Record-Type Files]"
+                }
+            ],
+            "identifier": "210",
+            "isPartOf": "2432",
+            "issued": "2008-07-26T14:13:31",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -10483,54 +10477,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-12-10T16:44:06",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2008-07-26T14:13:31",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR22901.v2",
-                    "title": "National Crime Victimization Survey, 2003 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, 2004 [Record-Type Files]",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
-            "modified": "2008-12-11T09:18:27",
-            "accessLevel": "public",
-            "identifier": "212",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, 2003 [Record-Type Files]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a\r\nnationally-representative sample of residential addresses since 1972. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, and motor vehicle theft. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR22900.v2",
+                    "title": "National Crime Victimization Survey, 2004 [Record-Type Files]"
+                }
+            ],
+            "identifier": "212",
+            "isPartOf": "2432",
+            "issued": "2008-07-26T13:15:20",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -10551,54 +10545,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-12-11T09:18:27",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2008-07-26T13:15:20",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR22900.v2",
-                    "title": "National Crime Victimization Survey, 2004 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, 2005 [Record-Type Files]",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
-            "modified": "2008-12-11T16:21:07",
-            "accessLevel": "public",
-            "identifier": "214",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, 2004 [Record-Type Files]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR22746.v2",
+                    "title": "National Crime Victimization Survey, 2005 [Record-Type Files]"
+                }
+            ],
+            "identifier": "214",
+            "isPartOf": "2432",
+            "issued": "2008-07-26T12:22:39",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -10619,54 +10613,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-12-11T16:21:07",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2008-07-26T12:22:39",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR22746.v2",
-                    "title": "National Crime Victimization Survey, 2005 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, 2006 [Record-Type Files]",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
-            "modified": "2009-08-25T09:38:00",
-            "accessLevel": "public",
-            "identifier": "215",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, 2005 [Record-Type Files]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR22560.v3",
+                    "title": "National Crime Victimization Survey, 2006 [Record-Type Files]"
+                }
+            ],
+            "identifier": "215",
+            "isPartOf": "2432",
+            "issued": "2008-08-04T21:41:30",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -10687,54 +10681,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-08-25T09:38:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2008-08-04T21:41:30",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR22560.v3",
-                    "title": "National Crime Victimization Survey, 2006 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, 2007 [Collection Year Record-Type Files]",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations. This version of the NCVS, referred to as the collection year, contains records from interviews conducted in the 12 months of the given year.",
-            "modified": "2009-08-24T07:47:49",
-            "accessLevel": "public",
-            "identifier": "216",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, 2006 [Record-Type Files]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations. This version of the NCVS, referred to as the collection year, contains records from interviews conducted in the 12 months of the given year.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24741.v2",
+                    "title": "National Crime Victimization Survey, 2007 [Collection Year Record-Type Files]"
+                }
+            ],
+            "identifier": "216",
+            "isPartOf": "2432",
+            "issued": "2009-02-09T15:55:25",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -10755,54 +10749,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-08-24T07:47:49",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2009-02-09T15:55:25",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24741.v2",
-                    "title": "National Crime Victimization Survey, 2007 [Collection Year Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, 2007 [Record-Type Files]",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
-            "modified": "2009-08-24T08:20:54",
-            "accessLevel": "public",
-            "identifier": "217",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, 2007 [Collection Year Record-Type Files]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR25141.v3",
+                    "title": "National Crime Victimization Survey, 2007 [Record-Type Files]"
+                }
+            ],
+            "identifier": "217",
+            "isPartOf": "2432",
+            "issued": "2009-04-07T09:19:28",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -10823,54 +10817,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-08-24T08:20:54",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2009-04-07T09:19:28",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR25141.v3",
-                    "title": "National Crime Victimization Survey, 2007 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, 2008 [Collection Year Record-Type Files]",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations. This version of the NCVS, referred to as the collection year, contains records from interviews conducted in the 12 months of the given year.",
-            "modified": "2009-09-11T09:56:29",
-            "accessLevel": "public",
-            "identifier": "218",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, 2007 [Record-Type Files]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations. This version of the NCVS, referred to as the collection year, contains records from interviews conducted in the 12 months of the given year.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR25461.v2",
+                    "title": "National Crime Victimization Survey, 2008 [Collection Year Record-Type Files]"
+                }
+            ],
+            "identifier": "218",
+            "isPartOf": "2432",
+            "issued": "2009-07-06T16:39:50",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -10891,54 +10885,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-09-11T09:56:29",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2009-07-06T16:39:50",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR25461.v2",
-                    "title": "National Crime Victimization Survey, 2008 [Collection Year Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, 2008 [Record-Type Files]",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
-            "modified": "2011-03-31T11:29:02",
-            "accessLevel": "public",
-            "identifier": "219",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, 2008 [Collection Year Record-Type Files]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR26382.v2",
+                    "title": "National Crime Victimization Survey, 2008 [Record-Type Files]"
+                }
+            ],
+            "identifier": "219",
+            "isPartOf": "2432",
+            "issued": "2010-01-26T15:53:53",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -10959,54 +10953,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-31T11:29:02",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2010-01-26T15:53:53",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR26382.v2",
-                    "title": "National Crime Victimization Survey, 2008 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, 2009",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations. This version of the NCVS, referred to as the collection year, contains records from interviews conducted in the 12 months of the given year.",
-            "modified": "2011-07-11T15:59:51",
-            "accessLevel": "public",
-            "identifier": "220",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, 2008 [Record-Type Files]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations. This version of the NCVS, referred to as the collection year, contains records from interviews conducted in the 12 months of the given year.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR28543.v1",
+                    "title": "National Crime Victimization Survey, 2009"
+                }
+            ],
+            "identifier": "220",
+            "isPartOf": "2432",
+            "issued": "2011-07-11T15:59:51",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -11027,54 +11021,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-07-11T15:59:51",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2011-07-11T15:59:51",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR28543.v1",
-                    "title": "National Crime Victimization Survey, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, 2010",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations. This version of the NCVS, referred to as the collection year, contains records from interviews conducted in the 12 months of the given year.",
-            "modified": "2012-06-22T09:23:50",
-            "accessLevel": "public",
-            "identifier": "221",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations. This version of the NCVS, referred to as the collection year, contains records from interviews conducted in the 12 months of the given year.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR31202.v2",
+                    "title": "National Crime Victimization Survey, 2010"
+                }
+            ],
+            "identifier": "221",
+            "isPartOf": "2432",
+            "issued": "2011-09-22T13:59:21",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -11095,54 +11089,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2012-06-22T09:23:50",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2011-09-22T13:59:21",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR31202.v2",
-                    "title": "National Crime Victimization Survey, 2010"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, [United States], 2011",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations. This version of the NCVS, referred to as the collection year, contains records from interviews conducted in the 12 months of the given year.",
-            "modified": "2021-01-25T13:57:58",
-            "accessLevel": "public",
-            "identifier": "222",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, 2010"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations. This version of the NCVS, referred to as the collection year, contains records from interviews conducted in the 12 months of the given year.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34061.v2",
+                    "title": "National Crime Victimization Survey, [United States], 2011"
+                }
+            ],
+            "identifier": "222",
+            "isPartOf": "2432",
+            "issued": "2012-10-25T15:41:38",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -11163,54 +11157,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-01-25T13:57:58",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2012-10-25T15:41:38",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34061.v2",
-                    "title": "National Crime Victimization Survey, [United States], 2011"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, [United States], 2012",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations. This version of the NCVS, referred to as the collection year, contains records from interviews conducted in the 12 months of the given year.",
-            "modified": "2021-01-26T11:15:48",
-            "accessLevel": "public",
-            "identifier": "223",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, [United States], 2011"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
```

